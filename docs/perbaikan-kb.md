# Log Perbaikan KB (Improvement Log)

> Catatan **perbaikan sistem / knowledge** KB ini — bukan progres belajar (itu di
> `progress/`). Tiap entri: **Problem** (apa yang salah/kurang) → **Fix** (perbaikannya)
> → **Tanggal** + file terdampak. Entri terbaru **di atas**.
>
> Tujuan: supaya tiap keputusan desain & perbaikan aturan punya jejak "kenapa" — biar
> tak berulang & mudah ditinjau. Ini melengkapi `docs/cara-kerja.md` (peta cara kerja)
> dan `git log` (riwayat commit mentah).

## Cara menambah entri (untuk sesi berikutnya)
Setiap kali sebuah **aturan / logika / skill diperbaiki** (bukan sekadar tambah materi
atau update skor), tambahkan satu blok di paling atas daftar di bawah, format:

```
### YYYY-MM-DD — <judul singkat>
- **Problem:** <apa yang salah / kurang, sertakan contoh konkret bila ada>
- **Fix:** <apa yang diubah>
- **File:** <file yang tersentuh>
```

---

### 2026-09-02 — `MG-yomi`/`MG-hyouki` monoton: kanji baca/tulis JLPT berulang (先生/友達/時間)
- **Problem:** user menyadari soal baca-tulis kanji `/jlpt` terasa monoton — 先生／友達／時間
  muncul berkali-kali antar-mock. Penyebab: (1) rotasi tema (`avoid_themes`) hanya menyentuh
  3 subtipe berteks (dokkai/joho/bunshou); `MG-yomi`/`MG-hyouki` **tak punya penangkal
  pengulangan**. (2) Skill membias `MG-yomi`/`MG-hyouki` ke KANJI 🔴 Anki, padahal pool 🔴
  hanya ~10 kanji (生・先・年・千・時・北・友・会・南・東) → tiap mock nyaris pasti nyomot dari situ.
- **Fix:** dua sumbu (mirror mekanisme tema):
  1. **Engine `avoid_items`** — `kb.py` fungsi baru `recent_kanji_items()` mengumpulkan `key`
     soal `MG-yomi`/`MG-hyouki` dari **2 mock terakhir** di `attempts.jsonl`; `cmd_plan`
     (kind=jlpt) mengembalikannya sbg `avoid_items`. Tak perlu field baru saat `record` —
     identitas item sudah tersimpan di `key` tiap question (beda dari tema yang butuh field
     `themes` eksplisit).
  2. **Longgarkan bias 🔴** — prinsip 4b skill diubah: `MG-yomi`/`MG-hyouki` sumber utama =
     **seluruh kanji N5** (`n5-vocabulary.md`), kanji 🔴 disentuh **sesekali** (≈1/2 soal per
     subtipe), bukan default. Tambah subsection "ROTASI kanji baca/tulis" + wajib hindari
     `avoid_items` + variasikan kategori kanji antar-mock.
- **File:** `scripts/kb.py` (`recent_kanji_items`, `cmd_plan`), `.claude/skills/jlpt/SKILL.md`
  (prinsip 4b, langkah 1 & 2, subsection rotasi kanji).

### 2026-09-01 — `DK-narabekae` cacat: potongan duplikat kata yang sudah di rangka
- **Problem:** mock `/jlpt` 2026-09-01 soal 10 (susun kalimat) tak bisa dijawab — rangka
  `パーティーで ＿①＿ ＿②＿ ＿★③＿ ＿④＿ します` sudah memuat `パーティーで` **tetap di kalimat**,
  tetapi `パーティーで` juga muncul sebagai salah satu potongan 1–4. Akibatnya potongan (4 kata:
  パーティーで/うたを/うたったり/おどったり) melebihi slot kosong yang sebenarnya perlu diisi (hanya 3:
  うたを/うたったり/おどったり) → soal rancu, user tak bisa menyusun. User menandainya saat menjawab.
  Soal dibuang dari skor (15/15, tak dihitung), tapi **aturannya belum ada** sehingga bisa terulang.
- **Fix:** tambah guardrail **"POTONGAN vs RANGKA — jangan duplikat (WAJIB cek)"** di template
  `DK-narabekae` (`.claude/skills/jlpt/SKILL.md`): keempat potongan = **tepat** kata pengisi keempat
  slot kosong; tak ada potongan yang sudah tercetak tetap di rangka; sebelum pakai, rakit potongan
  → pastikan **jumlah potongan = jumlah slot**, tak ada sisa/bentrok. Sertakan contoh cacat + fix.
- **File:** `.claude/skills/jlpt/SKILL.md` (template `DK-narabekae`)

### 2026-08-31 — Rotasi tema teks `/jlpt` (dokkai/joho/bunshou monoton)
- **Problem:** soal berteks `/jlpt` selalu bertema sama — `DK-dokkai` = **taman (公園)**,
  `DK-joho` = **perpустakaan (図書館)** — tiap mock, karena model menyalin tema dari **contoh
  template** di `SKILL.md` alih-alih memvariasikan. User menandai keluhan ini. (Data tak bisa
  konfirmasi penuh: `attempts.jsonl` tak simpan teks soal, hanya kunci/tag.)
- **Fix:** tambah blok **ROTASI TEMA teks (WAJIB)** di `.claude/skills/jlpt/SKILL.md` setelah
  template `DK-joho` — tegaskan contoh 公園/図書館 hanya ilustrasi format; sediakan **pool tema
  N5** per subtipe (dokkai/joho/bunshou); aturan: jangan pakai tema sama dua mock berturut-turut,
  idealnya 3 blok berteks dalam satu mock saling beda topik.
- **Fix-2 (mekanisme, jawab "gimana tahu tema sebelumnya?") — via JSONL+engine, BUKAN parse
  view.** Iterasi pertama sempat keliru menaruh tag `[tema:]` di prosa `history_note` lalu
  `grep` dari `history.md` — itu melawan arah data (mem-parse view render; rapuh). Diperbaiki:
  tema = data terstruktur append-only → disimpan di **`attempts.jsonl`** (sumber kebenaran),
  disurиткan engine. Implementasi:
  - `session.json` (jlpt) dapat field opsional **`themes`** (`{dokkai,joho,bunshou}`); `record`
    sudah menulis seluruh dict sesi → otomatis persist (soft-validate object).
  - `recent_themes(attempts,"jlpt")` = tema sesi jlpt terbaru yang bertag; `plan --kind jlpt`
    kini mengembalikan **`avoid_themes`**. Skill baca `avoid_themes` → pilih tema beda; tulis
    `themes` saat record. Echo `[tema:]` di `history_note` boleh, tapi cuma cermin (bukan sumber).
  - Mock 2026-08-31 di-**backfill** `themes` (taman/perpustakaan/jalan-jalan-kyoto) agar
    `avoid_themes` langsung berisi. Test `test_recent_themes` mengunci (20/20 lolos).
- **File:** `.claude/skills/jlpt/SKILL.md`, `scripts/kb.py`, `scripts/test_kb.py`,
  `progress/attempts.jsonl` (backfill 1 baris)

### 2026-08-31 — Simetri hint panel = tingkat kedetailan, bukan cuma keberadaan
- **Problem:** aturan simetri `description` lama hanya mencegah "kunci bergloss vs distraktor `—`".
  Tapi di sesi /quiz 2026-08-31 muncul varian lebih halus yang **lolos** cek itu: **semua** opsi
  bergloss, tapi **kunci** diberi keterangan yang **menjabarkan persis konstruksi/verba target**
  sedang distraktor cuma gloss partikel generik → tetap **tell** (user pilih opsi yang glossnya
  paling "nyambung"). Contoh: (a) `どこ（　）行きません` — も digloss 「pembentuk どこ〜+ません」
  (menyebut ません yang sudah tampil); (b) `友達（　）会います` — に digloss 「target yang ditemui」
  (menempel ke 会います yang kelihatan).
- **Fix:** perketat klausa **Simetri `description`** di `SKILL.md` — simetri juga soal **tingkat
  kedetailan**: semua opsi harus gloss generik setara, kunci **tak boleh** dijelaskan lewat
  konstruksi/verba yang diuji. Dua contoh cacat どこも/会います dicantumkan + versi benarnya.
- **File:** `.claude/skills/quiz/SKILL.md`

### 2026-08-31 — `plan` sadar-taxonomy + tag pola L2/L3 (mismatch cakupan maintenance)
- **Problem:** mode **maintenance** (`kb.py plan --mode adaptif` tanpa weak-area) memilih bab
  paling lama tak diuji dari **`all_lessons()`** (semua file `lessons/*.md`), sehingga menyodorkan
  **Lesson 2 & 3** — padahal `reference/quiz-taxonomy.md` **tak punya tag pola** untuk L2/L3
  (dulu dibatasi L4–L19). Engine "buta" batas taxonomy: sarannya (L2–L4) bentrok dgn cakupan
  quiz yang valid, dan soal L2/L3 tak bisa ditandai tag apa pun. Ketahuan saat `/quiz` maintenance
  2026-08-31 (harus di-workaround manual ke L4–L6).
- **Fix (keduanya, sesuai keputusan user):**
  1. **Tambah tag pola L2 & L3** ke `quiz-taxonomy.md` (これ/それ/あれ, この/その/あの, の-jenis,
     の-milik, なん · ここ/そこ/あそこ, こちら-sopan, どこ, どちら-asal, どこの-asal, いくら) +
     ubah catatan source-of-truth `lesson-04..19` → `lesson-02..19`. Kini L2/L3 quizzable.
  2. **Engine sadar-taxonomy:** `taxonomy_lessons()` mem-parse tag `L<n>-` dari taxonomy →
     `quizzable_lessons()` = `all_lessons()` ∩ taxonomy; `maintenance_lessons()` menyeleksi
     dari `quizzable_lessons()` (fallback ke `all_lessons()` bila taxonomy tak terbaca).
     Bab tanpa tag tak akan disodorkan lagi (defensif untuk lesson baru yang belum ditandai).
- **File:** `scripts/kb.py`, `reference/quiz-taxonomy.md`, `scripts/test_kb.py`

### 2026-08-30 — `/quiz` maintenance mode saat 0 weak-area (spaced review, B2)
- **Problem:** setelah weak-area habis (semua 🟢/⚪), `kb.py plan --mode adaptif` **menyempit
  cakupan ke bab terbaru saja** (`lessons:["Lesson 19"]`, `weights:[]`). Padahal tujuan `/quiz`
  = deteksi kelemahan **seluruh** materi Minna; status 🟢 itu foto lama & bisa **luntur** (decay).
  Akibatnya `/quiz` polos akan terus mengulang bab terakhir; L2–L18 tak pernah diprobe ulang.
- **Fix:** `compute_scope` mode adaptif tanpa weak-area → **maintenance**: pilih 3 bab **paling
  lama tak diuji** (urut `lesson_last_tested()` dari `attempts.jsonl`; bab belum pernah diuji =
  prioritas), tie-break akurasi terendah; sebar merata (`weights:[]`). `plan` menandai
  `"maintenance":true`+`"review_reason"`; skill `/quiz` memberi tahu user ini "review pemeliharaan".
- **Scoping (penting):** maintenance **HANYA** untuk `mode == "adaptif"` (quiz). Sempat bocor
  ke semua mode `/jlpt` (mock/moji/bunpou) karena kondisi awal cuma cek `not weak_lessons and
  not weak_pola` — untuk JLPT itu selalu benar (agg berbasis *subtype*, tak punya dim pola/lesson),
  dan `maintenance_lessons` pakai *last-tested quiz* yang tak relevan buat JLPT. **Kenapa `/jlpt`
  tak butuh maintenance:** mock JLPT sudah **menguji SEMUA subtipe tiap sesi** (struktural
  selalu-luas), jadi tak ada penyempitan/decay per-subtipe yang perlu dilawan. Diperbaiki +
  di-lock dengan test `test_compute_scope_maintenance_only_adaptif`.
- **File:** `scripts/kb.py`, `scripts/test_kb.py` (3 test baru), `.claude/skills/quiz/SKILL.md`,
  `docs/engine-bookkeeping-plan.md` (B2 → SELESAI).

### 2026-08-30 — Tambah subtipe `DK-bunshou` (文章の文法 / 問題3) ke `/jlpt`
- **Problem:** mock `/jlpt` meniru struktur JLPT N5 tertulis, tapi **melewatkan satu seksi
  resmi**: 問題3「文章の文法」— paragraf pendek dgn beberapa rumpang, jawaban ditentukan **alur
  wacana** (penghubung antar-kalimat, arah pemberian あげ/もらい/くれ, 指示語, pilihan pola sesuai
  konteks), beda dari `DK-bunpou` (kalimat lepas). Akibatnya mock bukan 1:1 struktur ujian.
- **Fix:** tambah subtipe `DK-bunshou` di seluruh rantai — `reference/quiz-taxonomy.md` (tabel
  subtipe), `scripts/kb.py` `SUBTYPE_META` (urut setelah `DK-narabekae`), template subtipe +
  aturan panel berteks di `.claude/skills/jlpt/SKILL.md`, dan komposisi mock (Sesi 2 kini
  menyertakan blok `DK-bunshou` + semua 5 subtipe DK tiap mock). Sekalian: render tabel
  `jlpt-evaluation.md` diubah menampilkan **semua** subtipe (himpunan tertutup) termasuk yang
  0/0 (⚪) — dulu hanya subtipe yang sudah ada attempt yang muncul, jadi subtipe baru tak
  terlihat sampai dipakai.
- **File:** `reference/quiz-taxonomy.md`, `scripts/kb.py`, `.claude/skills/jlpt/SKILL.md`,
  `progress/jlpt-evaluation.md` (re-render).

### 2026-08-30 — Soal memberi↔menerima (あげる/もらう) tak boleh andalkan `に` (dua-arah)
- **Problem:** quiz 2026-08-30 soal 11 (`L7-に-menerima`) 「父（ちち）**に** 時計（とけい）を（　）」 opsi
  あげました/もらいました. Partikel `に` **dua-arah**: `父に…を あげました` (に = penerima) dan
  `父に…を もらいました` (に = pemberi) **sama-sama gramatikal & wajar** → soal punya **dua kunci**,
  melanggar "tepat satu jawaban benar". User pilih あげました (sah) → di-`override` benar saat grading.
- **Fix:** tambah butir guardrail — saat menguji memberi↔menerima, **jangan andalkan `に`**; kunci
  arahnya: uji **もらう** pakai **から** untuk pemberi (「父から…を（　）」, から tak bisa jadi penerima →
  あげる gugur); uji **あげる** pastikan penerima jelas bukan diri sendiri + konteks mematikan もらう.
- **File:** `.claude/skills/quiz/SKILL.md` ("Catatan gaya").

### 2026-08-30 — Hint opsi 自他動詞 tak boleh menyebut partikel penentu yang sudah di soal
- **Problem:** quiz 2026-08-30 soal 4 (`L16-他動詞-自動詞`) 「電気（でんき）**が**（　）…」 dgn opsi
  ついて/つけて, hint-nya menulis 「ついて = 自動詞, **subjek pakai が**」 / 「つけて = 他動詞,
  objek pakai を」. Kunci soal justru partikel `が` yang **sudah tampil di kalimat** → user bisa
  mencocokkan が-di-soal ke が-di-hint secara mekanis dan pilih ついて **tanpa menalar 自↔他**.
  Simetri gaya sudah oke (dua opsi sama-sama dijelaskan), tapi **isinya** membocorkan cue penentu.
  Tambahan: pola ini sudah 🟢 (83%) → mestinya hint sudah difade netral, bukan penuh.
- **Fix:** perkuat aturan simetri `description` — **larang menyebut cue penentu (partikel/keterangan
  waktu) yang sudah muncul di kalimat soal**. Gloss harus **netral berbasis makna** (「電気が… =
  lampu menyala sendiri」 vs 「だれかが 電気を… = menyalakan」), bukan menyebut が/を. Untuk pola
  自他 yang sudah 🟢, fade lebih jauh → opsi polos `—`, user menilai dari partikel di kalimat.
- **File:** `.claude/skills/quiz/SKILL.md` (aturan "Simetri `description`").

### 2026-08-29 — Guardrail koherensi waktu↔aksi di soal `/jlpt`
- **Problem:** mock 2026-08-29 soal 12 (`DK-narabekae`) merakit kalimat 「わたしは **まいあさ**
  シャワーを あびて、はを みがいて、**ねます**」 — tata bahasa て-rangkaian benar & jawabannya valid,
  tapi kalimatnya **janggal secara semantik** (rutinitas pagi tapi ditutup "tidur"). Soal susun
  kalimat/konteks dicek untuk grammar & ketaksaan jawaban, tapi belum dicek **kewajaran kalimat
  utuh** (keterangan waktu vs verb penutup, urutan aksi logis).
- **Fix:** tambah blockquote **⏱️ KOHERENSI waktu↔aksi (WAJIB cek)** di template `DK-narabekae`
  — kalimat rakitan harus masuk akal sebagai kalimat nyata: `まいあさ`/`あさ` → penutup berangkat/
  mulai (…行きます/…たべます), rutinitas malam (シャワー→はみがき→ねる) pakai `まいばん`/`よる`; jaga
  urutan aksi logis (かく→はる→だす). Berlaku juga `DK-bunmyaku`/`DK-dokkai`/`DK-joho`.
- **File:** `.claude/skills/jlpt/SKILL.md` (template `DK-narabekae`).

### 2026-08-29 — Grading pindah ke engine (`key`/`submitted`, `grade()`)
- **Problem:** untuk pilihan ganda, "menilai" = `submitted == key` (mekanis, tak butuh model),
  tapi model yang menulis `correct: true/false` ke `session.json` → error-surface (salah-ingat
  kunci / salah-tulis boolean). Kecerdasan bahasa sebenarnya cuma di **menentukan kunci** (saat
  generate), bukan di membandingkan.
- **Fix:** tiap soal `session.json` kini bawa **`key`** (opsi benar) + **`submitted`** (klik user);
  fungsi pure `grade(q)` di engine menghitung benar/salah. `override` (correct/incorrect) + `note`
  untuk soal rancu (satu-satunya kasus model ikut memutuskan). `_validate_session` **menurunkan**
  `n`/`correct` dari `grade()` (tak percaya angka model; `WARN` bila beda). Boolean `correct` lama
  tetap diterima → `attempts.jsonl` lama tak perlu migrasi (golden test tetap lolos).
- **File:** `scripts/kb.py` (`grade`, `aggregate`, `_validate_session`), `scripts/test_kb.py`
  (13 test), `.claude/skills/{quiz,jlpt}/SKILL.md`, `docs/engine-bookkeeping-plan.md` §9.

### 2026-08-29 — `kb.py record --dry-run` (putus chicken-and-egg narasi)
- **Problem:** `weak_narrative`/`history_note` (prosa) butuh **angka final** sesi, tapi angka
  final baru ada **setelah** `record` — padahal prosa itu bagian dari `session.json` yang
  di-`record`. Ketergantungan melingkar → model terpaksa **hitung delta manual** untuk
  menulis narasi (mengulang beban yang mau dihapus engine) & berisiko **prosa ≠ tabel**.
- **Fix:** flag `--dry-run` pada `record` — hitung & cetak **delta per tag (before→after)** +
  weak ranking **tanpa menulis apa pun** (helper pure `session_deltas`). Alur 2 langkah:
  dry-run → tulis prosa pakai angka yang dicetak engine → `record` sungguhan. Angka narasi
  jadi **benar by-construction** (bukan hasil hitung tangan). Bukan menambal bug (data selalu
  benar karena tabel dihitung dari data mentah, bukan prosa) — ini **robustness**: hilangkan
  ketergantungan pada disiplin manual. SKILL.md quiz/jlpt step 6 diperbarui ke alur 2 langkah.
- **File:** `scripts/kb.py`, `scripts/test_kb.py`, `.claude/skills/{quiz,jlpt}/SKILL.md`,
  `docs/engine-bookkeeping-plan.md`.

### 2026-08-28 — Bookkeeping /quiz & /jlpt dipindah ke engine deterministik (`kb.py`)
- **Problem:** pembukuan (hitung skor/akurasi, tentukan status 🔴🟡🟢, ranking weak-area,
  seleksi cakupan, tulis-ulang tabel) dikerjakan model **manual** tiap sesi → boros token,
  rawan salah hitung, tak reprodusibel.
- **Fix:** engine `scripts/kb.py` (Python stdlib, tanpa dependency). Sumber kebenaran =
  **JSONL append-only** (`progress/attempts.jsonl` + `baseline.json`); tracker `.md` jadi
  **VIEW yang di-generate**. Perintah: `import` (seed sekali), `render` (regen), `record
  <session.json>` (ingest sesi → re-render + prepend history), `plan` (seleksi cakupan +
  bobot 🟡 + `vehicles_red` 🔴 + posisi jawaban tersebar). **Golden test** (`scripts/test_kb.py`)
  menjamin render **nol-diff** dengan tabel lama sebelum dipercaya. Pemisahan `kind` menjaga
  `/jlpt` tak menyentuh `evaluation.md`. SKILL.md quiz/jlpt: step 6 → `kb.py record`, step 2 →
  `kb.py plan`; tracker `.md` ditandai **AUTO-GENERATED**. Batas: engine = angka; model =
  kalimat soal + prosa (`history_note`/`weak_narrative`).
- **File:** `scripts/kb.py`, `scripts/test_kb.py`, `progress/{attempts.jsonl,baseline.json}`,
  `progress/{evaluation,jlpt-evaluation,history}.md` (marker), `.claude/skills/{quiz,jlpt}/SKILL.md`,
  `docs/engine-bookkeeping-plan.md`, `README.md`, `CLAUDE.md`, `docs/cara-kerja.md`.

### 2026-08-28 — Soal 自他動詞 rancu karena distraktor tense (もう + はじまる)
- **Problem:** soal `/quiz review` (sesi 21) yang menguji 自動詞 vs 他動詞 memakai kalimat
  `テストが もう（　）。` dengan 4 opsi はじめます/はじめました/はじまります/はじまりました. Maksudnya
  menguji golongan verba (自 vs 他), tapi distraktor mencampur **tense** — dan `もう` valid
  untuk **dua-duanya**: `もう はじまります` ("sebentar lagi mulai") & `もう はじまりました`
  ("sudah mulai") sama-sama gramatikal. Jadi antara 2 opsi 自動詞 tak ada satu jawaban pasti
  → melanggar aturan "distraktor wajib jelas salah, tepat satu benar".
- **Fix:** saat menguji **自/他動詞**, jaga dimensi lain (tense/aspek) **konstan** — beri hanya
  2 opsi berpasangan 自↔他 pada tense yang sama (はじまります↔はじめます), atau kalau butuh 4 opsi
  pakai konteks yang mengunci tense (mis. tambах keterangan waktu eksplisit). Hindari `もう`
  sebagai satu-satunya penanda waktu karena ambigu (sudah/sebentar lagi). Soal yang terlanjur
  tampil dihitung **benar** bila user memilih golongan verba yang tepat.
- **File:** `.claude/skills/quiz/SKILL.md` (prinsip di "Catatan gaya" — contoh soal cacat baru).

### 2026-08-27 — Ringkasan hasil boros token; pisah ke /summary
- **Problem:** step 7 `/quiz` & `/jlpt` mencetak analisis PENUH tiap sesi (tabel semua
  soal benar+salah, breakdown per pola/partikel/lesson/subtipe, 3 area terlemah,
  rekomendasi panjang) — boros token padahal KB ini berprinsip hemat. Sebagian besar
  output berulang & bisa dilihat on-demand.
- **Fix:** step 7 kedua skill diringkas → hanya **skor + tabel soal SALAH saja +
  pembahasan ringkas + 1 baris area terlemah + hint `/summary`**. Analisis lengkap
  dipindah ke **skill baru `/summary`** (`/summary` = tracker quiz, `/summary jlpt` =
  tracker mock) yang **read-only** membaca `evaluation.md`/`jlpt-evaluation.md` +
  baris teratas `history.md`. **Step 6 (update tracker) tetap jalan penuh** — yang
  diringkas hanya tampilan chat, bukan pemeliharaan data.
- **File:** `.claude/skills/quiz/SKILL.md`, `.claude/skills/jlpt/SKILL.md`,
  `.claude/skills/summary/SKILL.md` (baru), `CLAUDE.md`, memory `quiz-summary-ringkas`

### 2026-08-26 — Keterangan opsi panel asimetris jadi tell halus
- **Problem:** `/quiz` sesi sweep L4-8 (soal 6, `おいしくないです`), di panel AskUserQuestion
  **hanya opsi BENAR** yang diberi `description` (`negatif い-adjektiva`), sedangkan tiga
  distraktor (bentuk keliru `おいしいじゃありません`/`おいしくです`/`おいしいでした`) diisi `—`. Pola
  "cuma jawaban benar yang punya keterangan, distraktor kosong" jadi **bocoran halus** —
  user bisa menebak kunci dari mana keterangan berada, bukan dari pemahaman. Skor jadi
  kurang jujur. (Berbeda dari soal partikel yang SEMUA opsinya diberi fungsi — itu sah.)
- **Fix:** aturan simetri `description` panel — **dalam satu soal, keterangan opsi harus
  konsisten**: entah (a) SEMUA opsi bermakna diberi gloss fungsi/arti netral yang tak
  menunjuk kunci (gaya soal partikel), atau (b) SEMUA opsi `—` bila distraktornya sekadar
  bentuk-salah/mengada-ada (nilai bentuk sendiri). **Jangan** hanya opsi benar yang diberi
  keterangan sementara distraktor `—` (atau sebaliknya). Tetap tunduk pada *hint fading*:
  porsi gloss dipudarkan untuk pola 🟢 — tapi pemudaran berlaku **merata ke semua opsi**,
  bukan menyisakan satu opsi bergloss sendirian.
- **File:** `.claude/skills/quiz/SKILL.md`, memory `quiz-panel-hint-symmetry`

### 2026-08-25 — Cerita bacaan hilang saat panel terbuka
- **Problem:** untuk soal bacaan (dokkai/joho), cerita cuma dicetak di chat lalu panel
  terpisah di bawah. Saat panel terbuka cerita **tak terlihat**, user harus scroll ke
  atas untuk membacanya — dan tak sengaja melihat soal/opsi lain yang belum dikerjakan.
- **Fix:** aturan penyajian bacaan — **cerita disertakan di dalam tiap `question` panel**
  blok itu (prefix `【文章】`), diulang untuk tiap soal (1 cerita → beberapa soal), dengan
  **jarak 1 baris kosong** sebelum `問N．` dan **tanpa garis horizontal**. `description`
  opsi kosong. Panel per-blok (hanya soal blok itu), diletakkan tepat di bawah ceritanya.
- **File:** `.claude/skills/jlpt/SKILL.md`, memory `jlpt-reading-panel-format`

### 2026-08-25 — Panel susun kalimat membocorkan jawaban
- **Problem:** `/jlpt` mock kelima soal 12 (DK-narabekae), panel AskUserQuestion bocor
  dua kali: (a) `question` memuat urutan benar `（ただしい じゅん：ごはんを→たべる→まえに→てを）`,
  (b) `description` tiap opsi menyebut posisinya (`まえに → "posisi ★③"`). Jawaban jadi
  terbaca tanpa mikir → skor "benar" palsu & tujuan susun kalimat gagal.
- **Fix:** aturan eksplisit — panel narabekae **tak boleh** memuat urutan kalimat benar
  maupun posisi per-potongan; `description` dikosongkan/arti netral; hint pola lemah cukup
  **nama pola**, bukan urutan. Rangka slot `①②★③④` tetap boleh (kerangka soal).
- **File:** `.claude/skills/jlpt/SKILL.md`, `.claude/skills/quiz/SKILL.md`, memory
  `quiz-susun-kalimat-format`

### 2026-08-25 — MG-bunmyaku & distraktor rancu (satu jawaban benar)
- **Problem:** beberapa soal pilihan ganda punya **>1 jawaban sah**, jadi rancu:
  (a) `/jlpt` soal 6 「なつやすみに 家族と（　）を します」 → `りょこう` **dan** `さんぽ`
  dua-duanya masuk akal; (b) `/quiz` soal 8 「〜ては（　）」 → `いけません` **dan**
  `なりません` dua-duanya bentuk larangan sah. Akar: distraktor dipilih tanpa memastikan
  konteks mengunci satu jawaban.
- **Fix:** tambah aturan eksplisit "kalimat wajib punya **cue** yang mengunci **tepat
  satu** jawaban; cek tiap distraktor sebelum dipakai; item 🔴 Anki boleh jadi kunci tapi
  cue tetap wajib." Diterapkan di template `MG-bunmyaku` (+semangat `DK-bunpou`) dan di
  Catatan gaya `/quiz`.
- **File:** `.claude/skills/jlpt/SKILL.md`, `.claude/skills/quiz/SKILL.md`

### 2026-08-25 — Posisi jawaban benar selalu di nomor 1
- **Problem:** pada sesi `/quiz`, hampir semua kunci jatuh di **opsi nomor 1** — user
  bisa menebak dari pola, bukan pemahaman (active recall jadi tak jujur). Aturan "posisi
  acak" sudah ada tapi tak dipatuhi.
- **Fix:** pertegas jadi "acak & **sebar merata** (1/2/3/4) lintas soal, jangan nomor 1
  terus" di hub yang selalu ter-load + kedua skill + memory.
- **File:** `CLAUDE.md`, `.claude/skills/quiz/SKILL.md`, `.claude/skills/jlpt/SKILL.md`,
  memory `quiz-randomize-answer-position`

### 2026-08-25 — Engine adaptif tak terdokumentasi eksplisit
- **Problem:** rumus skor, ambang status (🔴/🟡/🟢/⚪), & logika pembobotan cuma tersebar
  di SKILL.md — tak ada penjelasan terpusat "cara mesin adaptif menghitung".
- **Fix:** tambah bagian **"Engine adaptif — cara skor, status & pembobotan dihitung"**
  (ambang, rumus update, pembobotan, penyajian, pemisahan tracker quiz/jlpt).
- **File:** `docs/cara-kerja.md`

### 2026-08-25 — Refresh Anki manual & prasyarat gampang lupa
- **Problem:** update data Anki butuh 2 script terpisah + prasyarat "buka Anki desktop &
  Sync dulu" yang mudah terlupa (sync iPhone saja tak update `collection.anki2`).
- **Fix:** buat command **`/sync-anki`** yang membungkus kedua script, mengingatkan
  prasyarat Sync, dan memberi notif `✅ Sukses updated` / `ℹ️ No data updated`.
- **File:** `.claude/skills/sync-anki/SKILL.md`, `README.md`, `CLAUDE.md`

### 2026-08-25 — Bias Anki weak items tanpa aturan fallback
- **Problem:** aturan bias item lemah Anki hanya bilang "bila cocok" — tak eksplisit apa
  yang dilakukan **kalau tak ada item 🔴 yang cocok** dengan pola yang diuji.
- **Fix:** tambah klausa **fallback**: kalau tak ada item 🔴 cocok, pakai kosakata lain
  (`n5-vocabulary.md` / `anki-verbs.md`); pola tetap utama, Anki hanya bias lunak.
- **File:** `CLAUDE.md`, `.claude/skills/quiz/SKILL.md`, `.claude/skills/jlpt/SKILL.md`

### 2026-08-24 — Cara kerja KB belum ada peta untuk manusia
- **Problem:** logika bisnis & alur end-to-end cuma tersirat di CLAUDE.md/SKILL.md; sulit
  dipahami sebagai satu gambaran utuh.
- **Fix:** buat `docs/cara-kerja.md` (flow + diagram Mermaid + glosarium).
- **File:** `docs/cara-kerja.md`

### 2026-08-23 — /quiz & /jlpt belum memakai sinyal kesulitan empiris
- **Problem:** pemilihan kosakata/kanji soal tak memanfaatkan data item yang benar-benar
  sering user lupa (hanya pola dari `evaluation.md`).
- **Fix:** integrasi **item lemah Anki** (`lapses`+`leech`) → `progress/anki-weak-items.md`
  (auto-generated) + script sync; `/quiz` & `/jlpt` membias kendaraan soal ke item 🔴.
- **File:** `scripts/sync-anki-weak-items.sh`, `progress/anki-weak-items.md`,
  `docs/anki-integration-plan.md`, `CLAUDE.md`, kedua SKILL
