# Implementation Plan — Engine Bookkeeping Deterministik (JSONL)

## 1. Context

`/quiz` & `/jlpt` sekarang dijalankan **penuh oleh model**, termasuk **bookkeeping**:
menghitung ulang skor, menentukan status 🔴🟡🟢, meranking weak-area, memilih cakupan,
mengacak posisi jawaban, dan menulis ulang tabel Markdown di `progress/`. Bagian ini tak
butuh model, tapi **boros token**, **rawan salah hitung**, dan **tak reprodusibel**.

Plan ini memindahkan **hanya lapisan bookkeeping** ke engine Python deterministik dengan
**JSONL append-only sebagai sumber kebenaran** dan `.md` sebagai **view generated** —
mengikuti pola repo yang sudah ada (`reference/anki-verbs.md`, `progress/anki-weak-items.md`
di-generate dari sumber via `scripts/*.sh`).

**Out of scope:** pembuatan kalimat Jepang, distraktor, pembahasan, teks bacaan → tetap
model. Engine hanya angka, ranking, seleksi, render, penyimpanan.

### Batas engine vs model
| ENGINE (kode) | MODEL (string yang disuplai ke engine) |
|---|---|
| Benar/Total per pola·partikel·lesson·subtipe | Kalimat soal, opsi, distraktor, pembahasan |
| Akurasi %, status (⚪ bila Total<3) | Paragraf naratif "Sinyal/Rekomendasi" |
| Ranking weak-area/type (numerik, maks 5) | Catatan kualitatif baris history |
| Header `Terakhir diperbarui` + `total sesi` | — |
| Baris tabel history | — |
| Seleksi cakupan + bobot + bias item 🔴 | — |
| Sebar posisi kunci (1/2/3/4) | — |

## 2. Keputusan terkunci
- Sumber: **JSONL append-only** `progress/attempts.jsonl` + `progress/baseline.json` (commit).
- Bahasa: **Python 3 stdlib saja** (tanpa dependency), konsisten `scripts/*.sh`.
- `evaluation.md` / `jlpt-evaluation.md` / `history.md` → **GENERATED view** (commit,
  ditandai `AUTO-GENERATED — jangan edit tangan`).

## 3. Kontrak data (definitif)

### `progress/attempts.jsonl` — 1 objek JSON / sesi (append)
```json
{"kind":"quiz","date":"2026-08-28","mode":"review","n":12,"correct":10,
 "history_note":"<prosa kualitatif model>",
 "weak_narrative":"<paragraf Sinyal/Rekomendasi model>",
 "questions":[
   {"qno":1,"correct":true,"subtype":null,
    "tags":{"pola":["L16-他動詞-自動詞"],"partikel":["が"],"lesson":["Lesson 16"]}}
 ]}
```
- `kind` ∈ {quiz, jlpt}. Renderer `evaluation.md` **hanya** baca `kind=quiz`
  (menjamin `/jlpt` tak menyentuh angka `evaluation.md`).
- `subtype` (MG-*/DK-*) hanya untuk `kind=jlpt`.
- `weak_narrative` dipakai dari sesi **terbaru** per-kind (snapshot state); `history_note`
  **semua** sesi diakumulasi ke `history.md`.

### `progress/baseline.json` — agregat awal (impor sekali)
```json
{"quiz":{"pola":{"L19-なります":{"benar":22,"total":25}},
         "partikel":{"に":{"benar":35,"total":43}},
         "lesson":{"Lesson 16":{"benar":12,"total":16}}},
 "jlpt":{"subtype":{"DK-narabekae":{"benar":7,"total":9}}},
 "meta":{"quiz_sesi":21,"jlpt_sesi":8}}
```
Render: `count(tag) = baseline[tag] + Σ attempts bertag`. Sesi baru = tambah attempts.

### Session-plan (output `kb.py plan`, dikonsumsi model)
```json
{"kind":"quiz","mode":"review","lessons":["Lesson 16","Lesson 15"],
 "weights":[{"tag":"L16-に-naik","n":3},{"tag":"L15-に-vs-で-statis","n":3}],
 "vehicles_red":["きゅうこう","おります","でかけます"],
 "answer_positions":[3,1,4,2,2,4,1,3,4,1,2,3]}
```

## 4. Modul & signature (`scripts/kb.py`)

Fungsi pure (unit-tested):
```python
def status(benar:int, total:int) -> str          # ⚪ jika total<3; else 🔴<60 🟡<80 🟢
def accuracy(benar:int, total:int) -> int         # round-half-up(benar/total*100)
def load_baseline(path) -> dict
def load_attempts(path) -> list[dict]
def aggregate(baseline:dict, attempts:list, kind:str) -> dict   # {dim:{tag:{benar,total}}}
def rank_weak(agg:dict, limit:int=5) -> list[dict]            # 🔴→🟡, akurasi asc
def tag_to_lesson(tag:str, taxonomy:dict) -> str|None
def compute_scope(agg, taxonomy, latest_lesson, mode) -> dict  # lessons + weights
def spread_positions(n:int, k:int=4, seed:int|None=None) -> list[int]
def render_evaluation(agg:dict, narrative:str, meta:dict) -> str
def render_jlpt(agg:dict, narrative:str, meta:dict) -> str
def render_history(sessions:list) -> str
```
CLI (argparse):
- `kb.py import` — parse tabel `evaluation.md`+`jlpt-evaluation.md` → tulis `baseline.json`.
- `kb.py render` — regen 3 `.md` dari baseline+attempts (idempoten).
- `kb.py record <session.json>` — validasi skema → append `attempts.jsonl` → `render`.
  - `--dry-run` — hitung & cetak **delta per tag (before→after)** + weak ranking **TANPA
    menulis**. Alur 2 langkah: dry-run → tulis prosa pakai angka engine → record sungguhan.
    Menutup "chicken-and-egg" narasi (prosa butuh angka final; angka butuh record).
- `kb.py plan --kind {quiz,jlpt} --mode {adaptif,review,lesson-N,moji,bunpou,mock}`
  → cetak session-plan JSON (baca `progress/anki-weak-items.md` untuk `vehicles_red`).

## 5. Task berurutan (dengan acceptance criteria)

**T1 — Fungsi pure + test.** `status/accuracy/aggregate/rank_weak/spread_positions` +
`scripts/test_kb.py`. ✔ test lulus untuk kasus batas (total<3→⚪; 59→🔴; 60→🟡; 80→🟢;
ranking urut; posisi tersebar rata).

**T2 — `import` baseline.** Parser tabel pipe Markdown → `baseline.json` (+ meta sesi).
✔ `baseline.json` memuat semua baris tabel dengan angka persis.

**T3 — Renderer + `render`.** Reproduksi format sekarang; slot prosa dari field model.
✔ **golden test**: `import` lalu `render` → `git diff` tabel+weak-numerik+header = **nol**.

**T4 — `record`.** Validasi → append `attempts.jsonl` → re-render + prepend history.
✔ umpan sesi nyata (quiz sesi 21 = 10/12; jlpt mock 8 = 14/16) → angka identik existing.

**T5 — `plan`.** `compute_scope`+`rank_weak`+bias 🔴+`spread_positions` → session-plan JSON.
✔ `plan --mode review` memuat tag 🟡 kini; `answer_positions` tersebar.

**T6 — Integrasi skill & docs.** SKILL.md quiz/jlpt (record+plan), tandai `.md`
AUTO-GENERATED, update `docs/cara-kerja.md`, `perbaikan-kb.md`, `estimasi-token.md`,
`README.md`, `CLAUDE.md`. ✔ satu sesi `/quiz` end-to-end memakai engine.

## 6. Verifikasi end-to-end
1. `python3 scripts/kb.py import && python3 scripts/kb.py render` → `git diff` angka/tabel = 0.
2. `python3 scripts/test_kb.py` → semua lulus.
3. `python3 scripts/kb.py record <sesi21>.json` → reproduksi angka existing + history +1.
4. `python3 scripts/kb.py plan --kind quiz --mode review` → JSON weak 🟡 + posisi tersebar.

## 7. Risiko & mitigasi
- **Narasi kualitatif hilang** → disuplai model via `history_note`/`weak_narrative`; engine menempatkan.
- **Angka engine ≠ file manual** → golden test T3 sebagai jaring pengaman sebelum dipercaya.
- **`/jlpt` bocor ke `evaluation.md`** → pemisahan `kind`; renderer evaluation hanya `kind=quiz`.
- **Furigana** → tabel hanya tag ASCII/kana (tak perlu furigana); prosa ber-furigana dari model.
- **Idempotensi** → `render` = fungsi murni (baseline+attempts); aman diulang.
- **Parser Markdown rapuh** → dipakai **hanya sekali** di `import`; setelah itu sumber = JSONL.

## 8. File tersentuh
- Baru: `scripts/kb.py`, `scripts/test_kb.py`, `progress/attempts.jsonl`, `progress/baseline.json`,
  `docs/engine-bookkeeping-plan.md` (dokumen ini).
- Berubah jadi GENERATED: `progress/evaluation.md`, `progress/jlpt-evaluation.md`, `progress/history.md`.
- Berubah (integrasi): `.claude/skills/quiz/SKILL.md`, `.claude/skills/jlpt/SKILL.md`,
  `docs/cara-kerja.md`, `docs/perbaikan-kb.md`, `docs/estimasi-token.md`, `README.md`, `CLAUDE.md`.
