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
| **Grading mekanis** (`submitted==key`) | **Validasi "tepat SATU kunci"** sebelum soal tampil |
| Menerapkan `override`+`note` (bila disuplai) | **Menerbitkan** `override`+`note` (hanya soal rancu) |

### Aturan anti-take-over (WAJIB — mencegah saling ambil peran)
Batas di atas **dua arah**; pelanggaran salah satunya = bug proses, bukan sekadar gaya.

- **Engine menilai MEKANIS & BUTA kualitas soal.** `kb.py` hanya membandingkan
  `submitted==key`; ia **tidak bisa dan tidak boleh** menebak apakah soal rancu / punya
  >1 jawaban sah. Grading "salah" dari engine untuk soal cacat = **engine benar**; cacatnya
  di hulu (penyusunan), bukan di grading.
- **Validasi ketunggalan kunci = 100% MODEL, di langkah 3 (sebelum soal tampil).** Randomisasi
  posisi kunci (engine, `answer_positions`) **hanya mengacak letak** — ia **bukan** validasi
  bahwa kunci tunggal. Tak ada tahap engine yang menangkap soal ambigu; itu tanggung jawab
  penyusun soal. Cek tiap opsi dipasang ke kalimat; >1 opsi sah → **ganti soal**, jangan
  andalkan override.
- **Model DILARANG:** menghitung/menulis angka tabel, menulis `correct` boolean sendiri,
  atau mengedit `evaluation.md`/`jlpt-evaluation.md`/`history.md` dengan tangan (tertimpa
  render & memutus reprodusibilitas).
- **Engine DILARANG:** mengarang kalimat, gloss opsi, pembahasan, atau narasi Sinyal/Rekomendasi.
- **Satu-satunya kanal model → grading = `override`+`note` di `session.json`.** Ini **patch
  pasca-fakta untuk soal rancu yang LOLOS dari validasi langkah 3**, bukan rutinitas. Tiap
  override **wajib** disertai: (a) `note` alasan, dan (b) bila polanya bisa berulang, entri
  `docs/perbaikan-kb.md` (Problem→Fix→Tanggal) supaya soal sejenis tak dibuat lagi. Override
  yang sering = sinyal validasi langkah 3 lemah, bukan solusi.

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
 "answer_positions":[3,1,4,2,2,4,1,3,4,1,2,3],
 "avoid_vehicles":["のみます","だします","いきます"]}
```
Field kondisional:
- `lessons` **hanya bab quizzable** (yang punya tag pola di `quiz-taxonomy.md`;
  `quizzable_lessons() = all_lessons() ∩ taxonomy_lessons()`). Bab tanpa tag tak disodorkan
  (lihat B3). Mode adaptif tanpa weak-area → `"maintenance":true` + `"review_reason"` (B2).
- `--kind quiz` menambah **`"avoid_vehicles"`** = list verb/kosakata kendaraan yang baru
  dipakai 2 sesi quiz terakhir, dari `recent_vehicles(attempts)` (field `vehicles` per
  question di `attempts.jsonl`). Skill condongkan ke kendaraan LAIN — **rotasi PERMUKAAN
  anti-monoton, BUKAN pola** (pola lemah `weights` tetap diulang). Prioritas bila bentrok:
  kecocokan pola > item 🔴 Anki > `avoid_vehicles` (rotasi mengalah).
- `--kind jlpt` menambah **`"avoid_themes"`** = tema teks (`{dokkai,joho,bunshou}`) mock JLPT
  terakhir, dari `recent_themes(attempts)`; skill memilih tema BEDA (rotasi anti-monoton, B4).
- `--kind jlpt` juga menambah **`"avoid_items"`** = **dict per-subtipe** item 2 mock terakhir,
  dari `recent_items_by_subtype(attempts)`; skill pilih item BEDA per subtipe. Enam subtipe
  non-teks: `MG-yomi`/`MG-hyouki` & `MG-bunmyaku`/`MG-ruigi` (identitas = `key`),
  `DK-bunpou`/`DK-narabekae` (identitas = pola id di `tags`, fallback `key`). Bias LUNAK: weak
  pola (`evaluation.md`) & item 🔴 Anki tetap boleh menang. (Subtipe berteks pakai `avoid_themes`.)

## 4. Modul & signature (`scripts/kb.py`)

Fungsi pure (unit-tested):
```python
def status(benar:int, total:int) -> str          # ⚪ jika total<3; else 🔴<60 🟡<80 🟢
def accuracy(benar:int, total:int) -> int         # round-half-up(benar/total*100)
def load_baseline(path) -> dict
def load_attempts(path) -> list[dict]
def aggregate(baseline:dict, attempts:list, kind:str) -> dict   # {dim:{tag:{benar,total}}}
def rank_weak(agg:dict, limit:int=5) -> list[dict]            # 🔴→🟡, akurasi asc
def tag_to_lesson(tag:str) -> str|None                        # "L<n>-..." → "Lesson <n>"
def taxonomy_lessons() -> set[str]                            # bab bertag di quiz-taxonomy.md
def quizzable_lessons() -> list[str]                          # all_lessons ∩ taxonomy (B3)
def maintenance_lessons(agg, attempts, limit=3) -> list[str]  # bab paling lama tak diuji (B2)
def recent_themes(attempts, kind="jlpt") -> dict              # tema mock terakhir (B4)
def recent_items_by_subtype(attempts, kind="jlpt", lookback=2) -> dict[str,list[str]]
                                                              # item 2 mock terakhir per subtipe
                                                              # non-teks → avoid_items (rotasi)
def recent_vehicles(attempts, kind="quiz", lookback=2) -> list[str]
                                                              # kendaraan verb/kosakata 2 sesi
                                                              # quiz terakhir → avoid_vehicles
def compute_scope(agg, mode, n=12, attempts=None) -> dict     # lessons + weights (+maintenance)
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
  → cetak session-plan JSON. Baca `progress/anki-weak-items.md` (`vehicles_red`),
  `reference/quiz-taxonomy.md` (batasi `lessons` ke bab quizzable, B3), dan untuk `--kind
  jlpt` sertakan `avoid_themes` + `avoid_items` (dict per-subtipe) dari `attempts.jsonl` (B4).
- `kb.py summary --kind {quiz,jlpt}` → breakdown lengkap JSON (per dim + `weak` + `sesi`
  + `last_session`) untuk skill `/summary`; deterministik, read-only.

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

## 9. Ekstensi (2026-08-29, ✅ terimplementasi) — grading pindah ke engine

**Motivasi:** untuk soal pilihan ganda dengan kunci yang ditentukan saat generate,
"menilai" = `submitted == key` — perbandingan mekanis yang **tak butuh model**. Saat ini
model menulis `correct: true/false` ke `session.json` → satu error-surface (salah-ingat
kunci / salah-tulis boolean). Pindahkan perbandingan ke engine; model cukup menaruh
**kunci** (saat generate) + **jawaban user**, plus **override** untuk soal rancu.

### Kontrak `session.json` — field question (baru)
```json
{"qno":1,"key":"に","submitted":"に","subtype":null,"tags":{...}}
{"qno":3,"key":"はじまります","submitted":"はじまりました",
 "override":"correct","note":"もう ambigu tense","tags":{...}}
```
- `key` = label opsi benar (persis string panel). `submitted` = label yang user klik.
- `override` ∈ {`correct`,`incorrect`} — **opsional**, hanya untuk soal cacat/rancu; memaksa
  hasil mengabaikan perbandingan. `note` = alasan (untuk jejak).
- **Backward-compat:** `correct` boolean lama tetap diterima (baris `attempts.jsonl` yang
  sudah ada tak perlu migrasi).

### Fungsi grading (pure)
```python
def grade(q) -> bool:
    if "override" in q:               return q["override"] == "correct"
    if "key" in q and "submitted" in q: return q["submitted"].strip() == q["key"].strip()
    if "correct" in q:                return bool(q["correct"])   # legacy
    raise ValueError("question tak punya key/submitted maupun correct")
```
- `aggregate`, `session_deltas`, hitung `n`/`correct` sesi → semua pakai `grade(q)`,
  bukan `q["correct"]` langsung.
- `_validate_session` **menurunkan** `correct=sum(grade(q))` & `n=len(q)` dari engine
  (tak percaya angka dari model); kalau model tetap kirim `correct`/`n` yang beda → warn.

### Diagram peran (sesudah)
```
generate  → MODEL tetapkan key tiap soal (judgment bahasa)  ← satu-satunya "kecerdasan"
submit    → user klik → MODEL taruh submitted (+ override bila rancu)
grade     → ENGINE: correct = (submitted == key)            ← pindah dari model
tally     → ENGINE: skor/status/ranking (sudah)
```

### Risiko & mitigasi
- **String key ≠ submitted** (furigana/spasi beda) → false-negative. Mitigasi: `.strip()`;
  aturan "key harus == label panel persis". (Normalisasi lebih jauh dihindari agar sederhana.)
- **Salah pakai override** → batasi hanya soal ter-flag rancu; `note` wajib diisi.
- **Legacy tak rusak** → cabang `correct` dipertahankan; golden/aggregate lama tetap lolos.

### Verifikasi
- Unit test `grade`: match / mismatch / override / legacy.
- `record --dry-run` dgn `session.json` ber-`key/submitted` → `correct` count = hitungan engine.
- Golden test lama tetap lolos (sesi22 pakai `correct` legacy → agregat identik).

### File tersentuh (ekstensi)
`scripts/kb.py` (`grade`, `aggregate`, `_validate_session`, `_touched_cells` tetap),
`scripts/test_kb.py`, `.claude/skills/{quiz,jlpt}/SKILL.md` (skema question + "engine yang
menilai"), doc ini, `docs/perbaikan-kb.md`.

## 8. File tersentuh
- Baru: `scripts/kb.py`, `scripts/test_kb.py`, `progress/attempts.jsonl`, `progress/baseline.json`,
  `docs/engine-bookkeeping-plan.md` (dokumen ini).
- Berubah jadi GENERATED: `progress/evaluation.md`, `progress/jlpt-evaluation.md`, `progress/history.md`.
- Berubah (integrasi): `.claude/skills/quiz/SKILL.md`, `.claude/skills/jlpt/SKILL.md`,
  `docs/cara-kerja.md`, `docs/perbaikan-kb.md`, `docs/estimasi-token.md`, `README.md`, `CLAUDE.md`.

## 10. Backlog (observasi pemakaian)

> Bukan bug pembukuan (integritas angka & audit trail sudah benar) — murni **kualitas
> heuristik `plan`**. Dicatat saat pemakaian, dikerjakan bila mulai mengganggu.

### B1 — `plan.weights` masih kasar (dump ke satu tag)
- **Amatan (quiz 2026-08-30):** `kb.py plan --mode adaptif` mengembalikan
  `weights:[{tag:"L16-に-naik", n:12}]` — **seluruh 12 soal** ditumpuk ke satu-satunya tag
  🟡, bukan "mayoritas ke weak, sisanya ke bab terbaru" seperti kontrak `/quiz`. Praktis
  field ini tak terpakai; model menyebar campuran soal manual (4 L16 + sisanya L19).
- **Arah fix:** `compute_scope` mengembalikan alokasi campuran, mis. proporsi ~60% weak
  (dibagi antar tag 🔴/🟡 by akurasi asc) + ~40% bab terbaru, dgn cap per-tag supaya tak
  menumpuk semua ke satu tag. Sertakan `lesson`/`subtype` target per slot, bukan cuma `tag`.

### B2 — perilaku saat **0 weak area** (maintenance mode) — ✅ SELESAI 2026-08-30
- **Amatan (quiz 2026-08-30):** setelah sesi ini, `evaluation.md` **tak punya 🔴/🟡 lagi**
  (semua 🟢/⚪). Mode `adaptif` **menyempit ke bab terbaru saja** (`plan` → `lessons:["Lesson 19"]`,
  `weights:[]`) — L2–L18 tak lagi diprobe, decay tak terdeteksi.
- **Fix (terimplementasi):** `compute_scope` mendeteksi "tak ada weak-area" pada mode adaptif →
  **mode maintenance**: `lessons` = 3 bab **paling lama tak diuji** (spaced review lawan decay),
  urut `lesson_last_tested()` dari `attempts.jsonl` (bab belum pernah diuji = prioritas teratas),
  tie-break akurasi terendah; `weights:[]` (sebar merata). Output `plan` menyertakan
  `"maintenance":true` + `"review_reason"`. Skill `/quiz` (§"Menentukan cakupan default" butir 5)
  memberi tahu user "review pemeliharaan", bukan kelemahan baru.
- **File:** `scripts/kb.py` (`_lesson_nums`/`all_lessons`/`lesson_last_tested`/`maintenance_lessons`
  + cabang di `compute_scope`), `scripts/test_kb.py` (2 test), `.claude/skills/quiz/SKILL.md`.
- **Verifikasi:** `plan --mode adaptif` kini → `lessons:["Lesson 2","Lesson 3","Lesson 4"]`
  `maintenance:true`; 15 test kb lulus.

### B3 — `plan` sadar-taxonomy (cakupan hanya bab bertag) — ✅ SELESAI 2026-08-31
- **Amatan (quiz maintenance 2026-08-31):** `maintenance_lessons` memilih dari `all_lessons()`
  (semua file `lessons/*.md`) → menyodorkan **L2/L3** yang **tak punya tag** di `quiz-taxonomy.md`
  (dulu dibatasi L4–L19) → soal L2/L3 tak bisa ditandai; saran bentrok cakupan valid.
- **Fix:** (1) tambah tag pola L2/L3 ke `quiz-taxonomy.md` (source-of-truth `lesson-02..19`);
  (2) `taxonomy_lessons()` parse tag `L<n>-` → `quizzable_lessons() = all_lessons() ∩ taxonomy`;
  `maintenance_lessons()` menyeleksi dari `quizzable_lessons()` (fallback `all_lessons()` bila
  taxonomy tak terbaca). Bab tanpa tag tak disodorkan (defensif untuk lesson baru belum ditandai).
- **File:** `scripts/kb.py`, `reference/quiz-taxonomy.md`, `scripts/test_kb.py` (3 test).

### B4 — rotasi tema teks `/jlpt` (anti-monoton) — ✅ SELESAI 2026-08-31
- **Amatan:** cerita `DK-dokkai`/`DK-joho`/`DK-bunshou` selalu bertema sama (taman/perpustakaan)
  tiap mock karena model menyalin contoh template.
- **Fix (JSONL+engine, bukan parse view):** field opsional **`themes`** di `session.json` (jlpt)
  → `record` persist ke `attempts.jsonl`; `recent_themes(attempts)` → `plan --kind jlpt`
  mengembalikan **`avoid_themes`**; skill pilih tema beda + tulis `themes` saat record. Iterasi
  awal (tag `[tema:]` di prosa `history_note` lalu grep `history.md`) dibuang karena mem-parse
  view. Mock 2026-08-31 di-backfill `themes`.
- **File:** `scripts/kb.py`, `.claude/skills/jlpt/SKILL.md`, `scripts/test_kb.py`
  (`test_recent_themes`), `progress/attempts.jsonl` (backfill).
