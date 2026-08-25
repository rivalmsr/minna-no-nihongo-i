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
