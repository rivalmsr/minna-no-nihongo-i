#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# sync-anki-weak-items.sh
# Regenerasi progress/anki-weak-items.md dari collection Anki desktop.
#
# Sumber = collection.anki2 (SQLite) milik Anki desktop. Menarik SINYAL KESULITAN
# empiris (lapses + tag `leech`) untuk deck "Minna no Nihongo I" & "Japanese Kanji^_N5",
# lalu menuliskannya sebagai daftar item lemah bertingkat. Dipakai /quiz & /jlpt untuk
# memilih "kendaraan" kosakata/kanji yang benar-benar sering dilupakan.
#
# File output = TURUNAN, jangan diedit tangan. Jalankan ulang tiap kali mau refresh.
#
# Pakai:  bash scripts/sync-anki-weak-items.sh [path/ke/collection.anki2]
# Env:    ANKI_COLLECTION=... (override lokasi collection)
# ---------------------------------------------------------------------------
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$PROJECT_ROOT/progress/anki-weak-items.md"

# --- Lokasi collection (default macOS; bisa dioverride) --------------------
COL="${1:-${ANKI_COLLECTION:-}}"
if [ -z "$COL" ]; then
  # default macOS; ambil profil pertama yang punya collection.anki2
  for c in "$HOME/Library/Application Support/Anki2/"*/collection.anki2; do
    [ -f "$c" ] && COL="$c" && break
  done
fi
if [ -z "${COL:-}" ] || [ ! -f "$COL" ]; then
  echo "ERROR: collection.anki2 tidak ditemukan." >&2
  echo "Set ANKI_COLLECTION=... atau beri path sebagai argumen pertama." >&2
  exit 1
fi

# --- Salin dulu (hindari lock kalau Anki terbuka), query read-only --------
TMP="$(mktemp -t anki-col.XXXXXX).anki2"
trap 'rm -f "$TMP"' EXIT
cp "$COL" "$TMP"

python3 - "$TMP" "$OUT" <<'PY'
import sqlite3, sys, re, datetime

db, out = sys.argv[1], sys.argv[2]
con = sqlite3.connect(db)

# Nama kolom deck memakai collation `unicase` yg tak ada di sqlite CLI/py → jangan
# WHERE/ORDER pakai kolom name; ambil semua lalu cocokkan di Python. Nama deck bisa
# memuat pemisah hierarki chr(31) (subdeck, mis. "Japanese Kanji"+\x1f+"N5").
US = chr(31)  # pemisah field Anki (juga pemisah level deck di kolom name)
decks = []
for did, name in con.execute("SELECT id, name FROM decks"):
    parts = [p.strip() for p in name.split(US)]
    decks.append((did, name, parts))

def find_deck(pred):
    for did, name, parts in decks:
        if pred(name, parts):
            return did
    return None

DID_MINNA = find_deck(lambda name, parts: parts[-1] == "Minna no Nihongo I")
DID_KANJI = find_deck(lambda name, parts: parts[-1] == "N5" and "Kanji" in name)

def rows(did):
    if not did:
        return []
    q = """SELECT n.flds, n.tags, c.lapses
           FROM cards c JOIN notes n ON n.id=c.nid WHERE c.did=?"""
    for flds, tags, lapses in con.execute(q, (did,)):
        yield flds.split(US), (tags or ""), (lapses or 0)

def is_leech(tags):
    return " leech " in f" {tags} "

def bab(tags):
    m = re.findall(r"MNN0*(\d+)", tags)
    return f"L{int(m[0])}" if m else "—"

def tier(lapses, leech):
    if leech or lapses >= 8:
        return "🔴"
    if lapses >= 5:
        return "🟡"
    if lapses >= 3:
        return "⚪"
    return None

# --- Kumpulkan MINNA (kosakata + verb) ---
minna = []
for flds, tags, lapses in rows(DID_MINNA):
    front, back = flds[0], (flds[1] if len(flds) > 1 else "")
    t = tier(lapses, is_leech(tags))
    if t:
        minna.append((t, lapses, is_leech(tags), front, back, bab(tags)))

# --- Kumpulkan KANJI N5 (Back = "bacaan | arti") ---
kanji = []
for flds, tags, lapses in rows(DID_KANJI):
    front, back = flds[0], (flds[1] if len(flds) > 1 else "")
    if " | " in back:
        yomi, arti = [x.strip() for x in back.split(" | ", 1)]
    else:
        yomi, arti = "", back
    t = tier(lapses, is_leech(tags))
    if t:
        kanji.append((t, lapses, is_leech(tags), front, yomi, arti))

# urut: lapses desc
minna.sort(key=lambda r: (-r[1], r[3]))
kanji.sort(key=lambda r: (-r[1], r[3]))

def count(lst, sym):
    return sum(1 for r in lst if r[0] == sym)

def leech_mark(leech):
    return " 🩸" if leech else ""

today = datetime.date.today().isoformat()

# --- Anchor: gabungan 🔴 dua deck ---
crit_v = [r for r in minna if r[0] == "🔴"]
crit_k = [r for r in kanji if r[0] == "🔴"]

L = []
w = L.append
w("# Item Lemah Anki (勉強の弱点) — Sumber Sinyal Kesulitan Empiris")
w("")
w("> ⚙️ **FILE AUTO-GENERATED — jangan edit tangan.** Regenerasi dari collection Anki")
w("> desktop dengan `bash scripts/sync-anki-weak-items.sh`. Sinyal = `lapses` (berapa")
w("> kali kartu \"gagal\"/lupa) + tag `leech` Anki (🩸 = kartu bermasalah kronis).")
w("> Ini **pelengkap** `evaluation.md` (kelemahan per POLA): file ini kelemahan per ITEM.")
w("")
w("Dipakai `/quiz` & `/jlpt` untuk memilih **kendaraan kosakata/kanji** yang benar-benar")
w("sering dilupakan — **di dalam** pola lemah dari `evaluation.md`. Bukan drill hafalan")
w("arti (itu tugas Anki), tapi memaksa item sulit ini muncul di soal produksi.")
w("")
w("Tingkat: **🔴** = `leech` atau `lapses ≥ 8` · **🟡** = `lapses 5–7` · **⚪** = `lapses 3–4`")
w("(⚪ hanya dihitung, tak didaftar). **🩸** = bertag `leech`.")
w("")
w("> Ringkasan cepat (anchor — baca ini saja saat quiz): PRIORITAS TINGGI 🔴")
w(">")
w("> **Verb/kosakata (Minna):** " + (", ".join(f"{r[3]}{leech_mark(r[2])}" for r in crit_v) or "—"))
w(">")
w("> **Kanji N5:** " + (", ".join(f"{r[3]}（{r[4]}）{leech_mark(r[2])}" for r in crit_k) or "—"))
w("")
w(f"Total ditandai — Minna: 🔴{count(minna,'🔴')} · 🟡{count(minna,'🟡')} · ⚪{count(minna,'⚪')}"
  f"  |  Kanji N5: 🔴{count(kanji,'🔴')} · 🟡{count(kanji,'🟡')} · ⚪{count(kanji,'⚪')}")
w("")

# --- Tabel Minna (🔴 + 🟡) ---
w("## Kosakata / Verb lemah — Minna no Nihongo I")
w("")
w("| | Item | Arti | Bab | lapses |")
w("|---|------|------|-----|:------:|")
for t, lp, lc, front, back, b in minna:
    if t == "⚪":
        continue
    w(f"| {t}{leech_mark(lc)} | {front} | {back} | {b} | {lp} |")
w("")

# --- Tabel Kanji N5 (🔴 + 🟡) ---
w("## Kanji lemah — Japanese Kanji N5")
w("")
w("| | Kanji | Bacaan | Arti | lapses |")
w("|---|:---:|--------|------|:------:|")
for t, lp, lc, kj, yomi, arti in kanji:
    if t == "⚪":
        continue
    w(f"| {t}{leech_mark(lc)} | {kj} | {yomi} | {arti} | {lp} |")
w("")
w("---")
w(f"_Auto-generated {today} oleh `scripts/sync-anki-weak-items.sh` dari `collection.anki2`._")

open(out, "w").write("\n".join(L) + "\n")
print(f"OK → {out}")
print(f"Minna: 🔴{count(minna,'🔴')} 🟡{count(minna,'🟡')} ⚪{count(minna,'⚪')}  |  "
      f"Kanji N5: 🔴{count(kanji,'🔴')} 🟡{count(kanji,'🟡')} ⚪{count(kanji,'⚪')}")
PY