#!/usr/bin/env python3
"""kb.py — Engine bookkeeping deterministik untuk KB Minna no Nihongo I.

Memindahkan lapisan pembukuan `/quiz` & `/jlpt` (hitung skor, status, ranking
weak-area, seleksi cakupan, render tracker) dari model ke kode deterministik.

Sumber kebenaran = JSONL append-only:
  progress/attempts.jsonl  — 1 objek JSON per sesi (append)
  progress/baseline.json   — agregat awal (impor sekali dari tabel .md lama)
File .md tracker = VIEW yang di-generate (evaluation / jlpt-evaluation / history).

Stdlib only. Detail desain: docs/engine-bookkeeping-plan.md
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import random
import re
import sys

# ── Path ────────────────────────────────────────────────────────────────────
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRESS = os.path.join(REPO_ROOT, "progress")
BASELINE_PATH = os.path.join(PROGRESS, "baseline.json")
ATTEMPTS_PATH = os.path.join(PROGRESS, "attempts.jsonl")
EVAL_PATH = os.path.join(PROGRESS, "evaluation.md")
JLPT_PATH = os.path.join(PROGRESS, "jlpt-evaluation.md")
HISTORY_PATH = os.path.join(PROGRESS, "history.md")

# ── Status & akurasi ──────────────────────────────────────────────────────────
# Ambang KB: akurasi <60% 🔴 · 60–79% 🟡 · ≥80% 🟢 · Total<3 → ⚪ (belum cukup data)
RED, YELLOW, GREEN, GREY = "🔴", "🟡", "🟢", "⚪"

# Subtipe JLPT: (tag, label kolom, sesi) — urutan tetap sesuai jlpt-evaluation.md
SUBTYPE_META = [
    ("MG-yomi", "Baca kanji (cara baca)", 1),
    ("MG-hyouki", "Tulis kanji (penulisan)", 1),
    ("MG-bunmyaku", "Kosakata dalam konteks", 1),
    ("MG-ruigi", "Sinonim / 言い換え類義", 1),
    ("DK-bunpou", "Tata bahasa (grammar)", 2),
    ("DK-narabekae", "Susun kalimat (★)", 2),
    ("DK-bunshou", "Tata bahasa dalam teks (cloze)", 2),
    ("DK-dokkai", "Bacaan pendek", 2),
    ("DK-joho", "Bacaan informasi (info-search)", 2),
]


def accuracy(benar: int, total: int) -> int:
    """Persentase akurasi, pembulatan half-up (mengikuti hitung manual)."""
    if not total:
        return 0
    return int(math.floor(benar / total * 100 + 0.5))


def status(benar: int, total: int) -> str:
    """Status emoji dari akurasi; ⚪ bila attempt < 3."""
    if total < 3:
        return GREY
    acc = accuracy(benar, total)
    if acc < 60:
        return RED
    if acc < 80:
        return YELLOW
    return GREEN


# ── Grading (bandingkan jawaban vs kunci) ─────────────────────────────────────
def grade(q: dict) -> bool:
    """Benar/salah satu soal. Prioritas: override > key/submitted > correct (legacy).

    Untuk pilihan ganda, menilai = `submitted == key` (deterministik). `override`
    (correct/incorrect) dipakai HANYA untuk soal rancu. `correct` boolean = kompat lama.
    """
    if "override" in q:
        return q["override"] == "correct"
    if "key" in q and "submitted" in q:
        return str(q["submitted"]).strip() == str(q["key"]).strip()
    if "correct" in q:
        return bool(q["correct"])
    raise ValueError(f"question qno={q.get('qno')}: tak ada key/submitted maupun correct")


# ── Agregasi ─────────────────────────────────────────────────────────────────
def _bump(agg: dict, dim: str, tag: str, correct: int) -> None:
    d = agg.setdefault(dim, {})
    cell = d.setdefault(tag, {"benar": 0, "total": 0})
    cell["total"] += 1
    cell["benar"] += correct


def aggregate(baseline: dict, attempts: list, kind: str) -> dict:
    """Gabung baseline[kind] + semua attempt berkind sama → {dim:{tag:{benar,total}}}.

    kind=quiz  → dim pola / partikel / lesson (dari question["tags"]).
    kind=jlpt  → dim subtype (dari question["subtype"]).
    """
    agg: dict = json.loads(json.dumps(baseline.get(kind, {})))  # deep copy
    for sess in attempts:
        if sess.get("kind") != kind:
            continue
        for q in sess.get("questions", []):
            correct = 1 if grade(q) else 0
            if kind == "jlpt":
                st = q.get("subtype")
                if st:
                    _bump(agg, "subtype", st, correct)
            else:
                for dim, tags in (q.get("tags") or {}).items():
                    for tag in tags:
                        _bump(agg, dim, tag, correct)
    return agg


# ── Ranking weak-area ─────────────────────────────────────────────────────────
_STATUS_RANK = {RED: 0, YELLOW: 1}  # hanya 🔴/🟡 yang masuk weak-list


def rank_weak(agg: dict, limit: int = 5) -> list[dict]:
    """Daftar tag berstatus 🔴 lalu 🟡, urut akurasi terendah dulu. Maks `limit`."""
    rows = []
    for dim, tags in agg.items():
        for tag, c in tags.items():
            st = status(c["benar"], c["total"])
            if st in _STATUS_RANK:
                rows.append(
                    {
                        "dim": dim,
                        "tag": tag,
                        "benar": c["benar"],
                        "total": c["total"],
                        "acc": accuracy(c["benar"], c["total"]),
                        "status": st,
                    }
                )
    rows.sort(key=lambda r: (_STATUS_RANK[r["status"]], r["acc"], r["tag"]))
    return rows[:limit]


# ── Randomisasi posisi jawaban ────────────────────────────────────────────────
def spread_positions(n: int, k: int = 4, seed: int | None = None) -> list[int]:
    """n posisi kunci (1..k) tersebar merata lalu diacak — hindari selalu #1."""
    base = [(i % k) + 1 for i in range(n)]
    random.Random(seed).shuffle(base)
    return base


# ── I/O sumber ───────────────────────────────────────────────────────────────
def load_baseline(path: str = BASELINE_PATH) -> dict:
    if not os.path.exists(path):
        return {"quiz": {}, "jlpt": {}, "meta": {}}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_attempts(path: str = ATTEMPTS_PATH) -> list[dict]:
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


# ── Parser tabel Markdown (dipakai HANYA sekali di `import`) ───────────────────
_HEADER_WORDS = {"Tag", "Benar", "Total", "Akurasi", "Status", "Partikel",
                 "Lesson", "Subtipe"}


def _split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_separator(cells: list[str]) -> bool:
    return all(c and set(c) <= set("-: ") for c in cells)


def parse_tracker_tables(path: str, sections: list[tuple]) -> dict:
    """Parse tabel pipe Markdown per-section.

    sections: list (heading_substr, dim, tag_col, benar_col, total_col).
    Return {dim: {tag: {benar, total}}}.
    """
    out: dict = {}
    cur = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("## "):
                cur = next((s for s in sections if s[0] in line), None)
                continue
            if not cur or not line.lstrip().startswith("|"):
                continue
            cells = _split_row(line)
            _, dim, tag_col, benar_col, total_col = cur
            if len(cells) <= max(tag_col, benar_col, total_col):
                continue
            if _is_separator(cells) or cells[tag_col] in _HEADER_WORDS:
                continue
            tag = cells[tag_col].strip("`")  # jlpt pakai backtick; quiz polos
            try:
                benar, total = int(cells[benar_col]), int(cells[total_col])
            except ValueError:
                continue
            out.setdefault(dim, {})[tag] = {"benar": benar, "total": total}
    return out


def parse_total_sesi(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.search(r"total sesi:\s*(\d+)", line)
            if m:
                return int(m.group(1))
    return 0


# ── CLI handler ───────────────────────────────────────────────────────────────
def cmd_import(args) -> int:
    quiz = parse_tracker_tables(EVAL_PATH, [
        ("Per pola kalimat", "pola", 0, 1, 2),
        ("Per partikel", "partikel", 0, 1, 2),
        ("Per lesson", "lesson", 0, 1, 2),
    ])
    jlpt = parse_tracker_tables(JLPT_PATH, [
        ("Sesi 1", "subtype", 1, 2, 3),
        ("Sesi 2", "subtype", 1, 2, 3),
    ])
    baseline = {
        "quiz": quiz,
        "jlpt": jlpt,
        "meta": {
            "quiz_sesi": parse_total_sesi(EVAL_PATH),
            "jlpt_sesi": parse_total_sesi(JLPT_PATH),
        },
    }
    with open(BASELINE_PATH, "w", encoding="utf-8") as f:
        json.dump(baseline, f, ensure_ascii=False, indent=1)
        f.write("\n")
    m = baseline["meta"]
    print(f"OK → {os.path.relpath(BASELINE_PATH, REPO_ROOT)}")
    print(f"quiz: pola {len(quiz.get('pola', {}))} · partikel "
          f"{len(quiz.get('partikel', {}))} · lesson {len(quiz.get('lesson', {}))} | "
          f"jlpt: subtype {len(jlpt.get('subtype', {}))} | "
          f"sesi quiz {m['quiz_sesi']} jlpt {m['jlpt_sesi']}")
    return 0


def _fmt_row(tag: str, cell: dict, backtick: bool = False, label: str | None = None) -> str:
    b, t = cell["benar"], cell["total"]
    tagcol = f"`{tag}`" if backtick else tag
    prefix = f"| {label} " if label is not None else ""
    return f"{prefix}| {tagcol} | {b} | {t} | {accuracy(b, t)}% | {status(b, t)} |"


def _splice_tables(text: str, section_specs: list, row_fn) -> str:
    """Ganti HANYA baris data tiap tabel; sisanya (preamble/heading/prosa) utuh.

    section_specs: list (heading_substr, key). row_fn(key) → list[str] baris data.
    """
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        spec = next((s for s in section_specs if line.startswith("## ") and s[0] in line), None)
        if spec is None:
            out.append(line)
            i += 1
            continue
        out.append(line)  # heading
        i += 1
        # salin sampai (termasuk) baris separator
        while i < len(lines):
            cur = lines[i]
            out.append(cur)
            i += 1
            if cur.lstrip().startswith("|") and _is_separator(_split_row(cur)):
                break
        # lewati baris data lama
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            i += 1
        out.extend(row_fn(spec[1]))
    return "\n".join(out)


def _replace_meta_line(text: str, date: str, sesi: int) -> str:
    return re.sub(
        r"_Terakhir diperbarui:[^_]*total sesi:\s*\d+_",
        f"_Terakhir diperbarui: {date} · total sesi: {sesi}_",
        text,
        count=1,
    )


def _sessions_of(attempts: list, kind: str) -> list:
    return [s for s in attempts if s.get("kind") == kind]


def render_evaluation(text: str, agg: dict, date: str | None, sesi: int) -> str:
    def rows(dim):
        return [_fmt_row(tag, c) for tag, c in agg.get(dim, {}).items()]

    text = _splice_tables(
        text,
        [("Per pola kalimat", "pola"), ("Per partikel", "partikel"), ("Per lesson", "lesson")],
        rows,
    )
    if date:
        text = _replace_meta_line(text, date, sesi)
    return text


def render_jlpt(text: str, agg: dict, date: str | None, sesi: int) -> str:
    sub = agg.get("subtype", {})

    def rows(session_key):
        sess = int(session_key[-1])
        # Subtipe JLPT = himpunan tertutup (SUBTYPE_META) → selalu tampilkan semua
        # baris sesi ini, termasuk yang belum ada attempt (⚪ 0/0), agar tracker
        # mendokumentasikan struktur ujian lengkap.
        return [
            _fmt_row(tag, sub.get(tag, {"benar": 0, "total": 0}), backtick=True, label=label)
            for tag, label, s in SUBTYPE_META
            if s == sess
        ]

    text = _splice_tables(text, [("Sesi 1", "s1"), ("Sesi 2", "s2")], rows)
    if date:
        text = _replace_meta_line(text, date, sesi)
    return text


def rerender_trackers(baseline: dict, attempts: list) -> None:
    """Tulis ulang evaluation.md & jlpt-evaluation.md dari baseline+attempts."""
    meta = baseline.get("meta", {})
    q_sessions = _sessions_of(attempts, "quiz")
    j_sessions = _sessions_of(attempts, "jlpt")
    # date/sesi hanya di-update bila ada sesi baru; pure render = biarkan
    q_date = q_sessions[-1]["date"] if q_sessions else None
    j_date = j_sessions[-1]["date"] if j_sessions else None
    q_sesi = meta.get("quiz_sesi", 0) + len(q_sessions)
    j_sesi = meta.get("jlpt_sesi", 0) + len(j_sessions)

    with open(EVAL_PATH, encoding="utf-8") as f:
        eval_txt = f.read()
    with open(JLPT_PATH, encoding="utf-8") as f:
        jlpt_txt = f.read()

    eval_out = render_evaluation(eval_txt, aggregate(baseline, attempts, "quiz"), q_date, q_sesi)
    jlpt_out = render_jlpt(jlpt_txt, aggregate(baseline, attempts, "jlpt"), j_date, j_sesi)

    with open(EVAL_PATH, "w", encoding="utf-8") as f:
        f.write(eval_out)
    with open(JLPT_PATH, "w", encoding="utf-8") as f:
        f.write(jlpt_out)


def cmd_render(args) -> int:
    rerender_trackers(load_baseline(), load_attempts())
    print(f"OK → {os.path.relpath(EVAL_PATH, REPO_ROOT)} · "
          f"{os.path.relpath(JLPT_PATH, REPO_ROOT)}")
    return 0


def _validate_session(s: dict) -> dict:
    for k in ("kind", "date", "questions"):
        if k not in s:
            raise SystemExit(f"session.json kurang field wajib: {k}")
    if s["kind"] not in ("quiz", "jlpt"):
        raise SystemExit("field `kind` harus 'quiz' atau 'jlpt'")
    qs = s["questions"]
    if s["kind"] == "jlpt" and any(q.get("subtype") is None for q in qs):
        raise SystemExit("sesi jlpt: tiap question wajib punya `subtype`")
    # Skor DITURUNKAN engine dari grade(), bukan dipercaya dari model.
    try:
        n, correct = len(qs), sum(1 for q in qs if grade(q))
    except ValueError as e:
        raise SystemExit(str(e))
    if s.get("n") is not None and s["n"] != n:
        print(f"WARN: n model={s['n']} ≠ {n} (dihitung engine); pakai {n}", file=sys.stderr)
    if s.get("correct") is not None and s["correct"] != correct:
        print(f"WARN: correct model={s['correct']} ≠ {correct} (dihitung engine); "
              f"pakai {correct}", file=sys.stderr)
    s["n"], s["correct"] = n, correct
    return s


def _prepend_history(session: dict) -> None:
    with open(HISTORY_PATH, encoding="utf-8") as f:
        text = f.read()
    acc = accuracy(session["correct"], session["n"])
    row = (f"| {session['date']} | {session.get('cakupan', '')} | {session['n']} | "
           f"{session['correct']}/{session['n']} ({acc}%) | {session.get('history_note', '')} |")
    out, inserted = [], False
    for line in text.split("\n"):
        out.append(line)
        if not inserted and line.lstrip().startswith("|") and _is_separator(_split_row(line)):
            out.append(row)
            inserted = True
    if not inserted:
        raise SystemExit("history.md: baris separator tabel tak ditemукан")
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


def _replace_weak_section(path: str, heading_substr: str, narrative: str) -> None:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(rf"(?m)^##[^\n]*{re.escape(heading_substr)}[^\n]*$", text)
    if not m:
        raise SystemExit(f"{os.path.basename(path)}: heading '{heading_substr}' tak ditemukan")
    new = text[: m.end()] + "\n" + narrative.strip("\n") + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)


def _touched_cells(session: dict) -> list:
    """(dim, tag) unik yang disentuh sesi (urut kemunculan)."""
    kind = session["kind"]
    seen, cells = set(), []
    for q in session.get("questions", []):
        if kind == "jlpt":
            pairs = [("subtype", q["subtype"])] if q.get("subtype") else []
        else:
            pairs = [(d, t) for d, ts in (q.get("tags") or {}).items() for t in ts]
        for p in pairs:
            if p not in seen:
                seen.add(p)
                cells.append(p)
    return cells


def session_deltas(baseline: dict, existing: list, session: dict) -> tuple:
    """Hitung before/after tiap tag yang disentuh sesi. PURE — tak menulis apa pun.

    Return (rows, agg_after). rows = list dict {dim, tag, before, after} di mana
    before/after = (benar, total, akurasi, status).
    """
    kind = session["kind"]
    before = aggregate(baseline, existing, kind)
    after = aggregate(baseline, existing + [session], kind)

    def cell(agg, dim, tag):
        c = agg.get(dim, {}).get(tag, {"benar": 0, "total": 0})
        return (c["benar"], c["total"], accuracy(c["benar"], c["total"]),
                status(c["benar"], c["total"]))

    rows = [
        {"dim": dim, "tag": tag, "before": cell(before, dim, tag),
         "after": cell(after, dim, tag)}
        for dim, tag in _touched_cells(session)
    ]
    return rows, after


def _print_weak(agg: dict, label: str = "Weak (deterministik)") -> None:
    weak = rank_weak(agg)
    if weak:
        print(f"{label}:")
        for w in weak:
            print(f"  {w['status']} {w['tag']} ({w['dim']}) {w['benar']}/{w['total']} {w['acc']}%")


def cmd_record(args) -> int:
    with open(args.session, encoding="utf-8") as f:
        session = _validate_session(json.load(f))
    baseline = load_baseline()
    existing = load_attempts()
    kind = session["kind"]
    acc = accuracy(session["correct"], session["n"])

    # DRY-RUN: hitung & cetak hasil TANPA menulis (putus chicken-and-egg narasi).
    if getattr(args, "dry_run", False):
        rows, after = session_deltas(baseline, existing, session)
        print(f"DRY-RUN (tak menulis apa pun) → {kind} {session['date']} "
              f"{session['correct']}/{session['n']} ({acc}%)")
        if rows:
            print("Delta per tag (before → after):")
            for r in rows:
                bb, bt, ba, bs = r["before"]
                ab, at, aa, ast = r["after"]
                print(f"  {r['tag']} ({r['dim']}): {bb}/{bt} {ba}% {bs} → "
                      f"{ab}/{at} {aa}% {ast}")
        _print_weak(after, "Weak setelah sesi ini")
        print("→ Pakai angka DI ATAS untuk menulis weak_narrative/history_note, "
              "lalu jalankan lagi TANPA --dry-run.")
        return 0

    # RUN sungguhan
    with open(ATTEMPTS_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(session, ensure_ascii=False) + "\n")
    attempts = load_attempts()
    rerender_trackers(baseline, attempts)
    _prepend_history(session)
    if session.get("weak_narrative"):
        if kind == "quiz":
            _replace_weak_section(EVAL_PATH, "Weak areas", session["weak_narrative"])
        else:
            _replace_weak_section(JLPT_PATH, "Weak types", session["weak_narrative"])
    print(f"OK recorded → {kind} {session['date']} "
          f"{session['correct']}/{session['n']} ({acc}%)")
    _print_weak(aggregate(baseline, attempts, kind))
    return 0


def tag_to_lesson(tag: str) -> str | None:
    """Pola tag berformat `L<num>-...` → 'Lesson <num>'."""
    m = re.match(r"^L(\d+)-", tag)
    return f"Lesson {int(m.group(1))}" if m else None


def latest_lesson() -> str | None:
    nums = [
        int(m.group(1))
        for p in glob.glob(os.path.join(REPO_ROOT, "lessons", "lesson-*.md"))
        if (m := re.search(r"lesson-(\d+)\.md", p))
    ]
    return f"Lesson {max(nums)}" if nums else None


def compute_scope(agg: dict, mode: str, n: int = 12) -> dict:
    """Deterministik: daftar lesson + bobot tag berdasarkan weak-area & mode."""
    weak = rank_weak(agg, limit=8)
    weak_pola = [w for w in weak if w["dim"] == "pola"]
    weak_lessons: list[str] = []
    for w in weak:
        les = w["tag"] if w["dim"] == "lesson" else tag_to_lesson(w["tag"])
        if les and les not in weak_lessons:
            weak_lessons.append(les)

    if mode == "review":
        lessons = weak_lessons[:3]
        pool = weak_pola or weak
    elif mode.startswith("lesson-"):
        lessons = [f"Lesson {int(mode.split('-', 1)[1])}"]
        pool = [w for w in weak_pola if tag_to_lesson(w["tag"]) in lessons]
    else:  # adaptif (default)
        lessons = weak_lessons[:2]
        lt = latest_lesson()
        if lt and lt not in lessons:
            lessons.append(lt)
        pool = weak_pola or weak

    weights = []
    if pool:
        per = max(1, n // min(len(pool), 4))
        for w in pool[:4]:
            weights.append({"tag": w["tag"], "n": per})
    return {"lessons": lessons, "weights": weights}


def vehicles_red() -> list[str]:
    """Item 🔴 (verb/kosakata Minna) dari anchor anki-weak-items.md sbg bias kendaraan."""
    path = os.path.join(PROGRESS, "anki-weak-items.md")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        m = re.search(r"Verb/kosakata \(Minna\):\*\*(.+)", f.read())
    if not m:
        return []
    out = []
    for tok in m.group(1).split(","):
        tok = re.sub(r"[🔴🟡⚪🩸]", "", tok)
        tok = re.sub(r"\s+(I{1,3})\b", "", tok).strip()
        if tok:
            out.append(tok)
    return out[:12]


def build_summary(baseline: dict, attempts: list, kind: str) -> dict:
    """Breakdown deterministik untuk `/summary` (PURE). Dipakai model sbg sumber angka."""
    agg = aggregate(baseline, attempts, kind)
    dims = ["subtype"] if kind == "jlpt" else ["pola", "partikel", "lesson"]
    breakdown = {}
    for dim in dims:
        breakdown[dim] = [
            {"tag": tag, "benar": c["benar"], "total": c["total"],
             "acc": accuracy(c["benar"], c["total"]),
             "status": status(c["benar"], c["total"])}
            for tag, c in agg.get(dim, {}).items()
        ]
    sess = _sessions_of(attempts, kind)
    last = None
    if sess:
        s = sess[-1]
        last = {"date": s["date"], "mode": s.get("mode"), "n": s.get("n"),
                "correct": s.get("correct"),
                "acc": accuracy(s.get("correct", 0), s.get("n", 0))}
    return {
        "kind": kind,
        "sesi": baseline.get("meta", {}).get(f"{kind}_sesi", 0) + len(sess),
        "breakdown": breakdown,
        "weak": rank_weak(agg),
        "last_session": last,
    }


def cmd_summary(args) -> int:
    out = build_summary(load_baseline(), load_attempts(), args.kind)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


def cmd_plan(args) -> int:
    baseline = load_baseline()
    attempts = load_attempts()
    agg = aggregate(baseline, attempts, args.kind)
    n = args.n
    scope = compute_scope(agg, args.mode, n)
    out = {
        "kind": args.kind,
        "mode": args.mode,
        "n": n,
        "lessons": scope["lessons"],
        "weights": scope["weights"],
        "vehicles_red": vehicles_red(),
        "answer_positions": spread_positions(n, 4),
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="kb.py", description="Engine bookkeeping KB")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("import", help="Impor baseline.json dari tabel .md lama").set_defaults(func=cmd_import)
    sub.add_parser("render", help="Regen tracker .md dari baseline+attempts").set_defaults(func=cmd_render)
    pr = sub.add_parser("record", help="Ingest satu session.json")
    pr.add_argument("session", help="Path session.json")
    pr.add_argument("--dry-run", action="store_true",
                    help="Hitung & cetak hasil (delta + weak) TANPA menulis apa pun")
    pr.set_defaults(func=cmd_record)
    pp = sub.add_parser("plan", help="Cetak session-plan JSON")
    pp.add_argument("--kind", choices=["quiz", "jlpt"], default="quiz")
    pp.add_argument("--mode", default="adaptif")
    pp.add_argument("--n", type=int, default=12)
    pp.set_defaults(func=cmd_plan)
    ps = sub.add_parser("summary", help="Cetak breakdown lengkap JSON (untuk /summary)")
    ps.add_argument("--kind", choices=["quiz", "jlpt"], default="quiz")
    ps.set_defaults(func=cmd_summary)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args) or 0


if __name__ == "__main__":
    raise SystemExit(main())
