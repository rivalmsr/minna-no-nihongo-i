# CLAUDE.md — Konteks Project

> Hub konteks yang **selalu ter-load** tiap sesi. Ringkas & menyeluruh; detail
> panjang ada di docs yang ditunjuk. Beberapa hal di sini pernah hilang konteks —
> jadi sengaja dipusatkan di file ini.

## Ide project

Knowledge base pribadi untuk belajar bahasa Jepang dari buku **Minna no Nihongo I
(みんなの日本語 I)**, target **JLPT N5**. Penjelasan ditulis **Bahasa Indonesia**,
contoh kalimat **Bahasa Jepang**. Dibaca/dirapikan di **Obsidian** (vault `.obsidian/`).

Dua fungsi utama:
1. **Catatan materi yang sudah dipelajari** — per pelajaran (課) di `lessons/*.md`,
   ditambah referensi terkumpul di `reference/*`.
2. **Latihan adaptif `/quiz`** — active recall + evaluasi titik lemah dari materi
   yang sudah dicatat.

## Struktur (indeks lengkap → `README.md`)

```
lessons/lesson-02.md … lesson-19.md   catatan per pelajaran (source of truth tata bahasa)
reference/
  quiz-taxonomy.md    tag pola & partikel untuk /quiz (indeks)
  n5-vocabulary.md    pool kosakata JLPT N5 (sumber kosakata /quiz)
  anki-verbs.md       pool kata kerja — AUTO-GENERATED dari deck Anki (jangan edit tangan)
  particles.md        ringkasan partikel
  vocabulary.md       kosakata terkumpul per lesson (referensi penulisan; besar — hindari saat quiz)
progress/
  evaluation.md       tracker kelemahan per pola/partikel/lesson (diupdate /quiz)
  history.md          riwayat tiap sesi /quiz
scripts/sync-anki-verbs.sh   regen anki-verbs.md dari learn-anki/ (gitignored)
.claude/skills/quiz/         skill /quiz (detail operasional lengkap)
```

Daftar pelajaran lengkap (judul + topik + status) ada di tabel `README.md`.

## /quiz — tujuan & aturan inti (PENTING)

**Tujuan:** active recall & melatih pemahaman **materi yang SUDAH dipelajari**, sambil
**mengevaluasi titik lemah** yang masih perlu diasah.

- **Hanya uji materi yang ada di KB ini.** Source of truth tata bahasa = `lessons/`.
  Kosakata = `reference/n5-vocabulary.md`. Kata kerja = `reference/anki-verbs.md`.
  Jangan pakai pola/materi di luar lesson yang tersedia.
- **Bobotkan ke weak areas** di `progress/evaluation.md`; sisanya konfirmasi materi
  yang sudah dikuasai. Perbarui evaluasi + history tiap sesi (hitung eksplisit, jangan
  mengarang skor).
- **Kata kerja = KENDARAAN active recall, bukan drill lepas.** Verb dari `anki-verbs.md`
  dipakai untuk memaksa **produksi bentuk & pemakaian** (て/ない/辞書/た) **DI DALAM pola
  yang sudah dipelajari & masih lemah**. JANGAN bikin soal konjugasi terisolasi seperti
  "「およぎます」→ bentuk た?" yang lepas dari materi. Contoh benar:
  "おきなわへ（いった）ことが あります" — user tetap memproduksi た-form sambil melatih pola
  たことがあります / partikel に / なります.
- **Preferensi tampilan & mode** (semua tersimpan, jangan dilupakan):
  - Mode ujian: **jawab semua soal dulu**, koreksi & analisis muncul **di akhir**.
  - Default **12 soal** (3 panel AskUserQuestion penuh 4+4+4).
  - Soal tampil **besar & tebal** di chat (kalimat Jepang pakai H1 `#`); klik jawaban
    lewat panel AskUserQuestion.
  - **Semua kanji wajib berfurigana** — termasuk di tabel hasil & ringkasan.
  - Soal susun kalimat (文法2) pakai format nomor 1–4 + posisi ★ gaya JLPT asli.
- **Hemat token:** baca **anchor** lesson (header + Topik + "Ringkasan cepat", ~20 baris),
  bukan file utuh. Detail pola/partikel/kosakata dibaca on-demand via `Grep`. Jangan
  `Read` utuh `vocabulary.md` / `particles.md` / lesson penuh saat quiz.

Detail lengkap (parsing argumen, cakupan adaptif, template soal, langkah eksekusi) ada
di `.claude/skills/quiz/SKILL.md`.

## /jlpt — variant mock ujian tertulis N5 (skill terpisah)

`/quiz` utama = latihan **harian adaptif** grammar; **jangan diubah** untuk kebutuhan
JLPT. Untuk simulasi ujian ada skill terpisah **`/jlpt`** (`.claude/skills/jlpt/SKILL.md`):

- **Meniru struktur ujian tertulis N5, 2 sesi:** Sesi 1 **文字・語彙** (baca kanji, tulis
  kanji, kosakata konteks, sinonim) + Sesi 2 **文法・読解** (grammar, susun kalimat,
  bacaan pendek, info-search). `聴解` (listening) di luar cakupan (butuh audio).
- **Reuse penuh** konvensi /quiz (furigana wajib, kanji besar H1, mode ujian, panel
  AskUserQuestion, hemat token, source of truth lesson). Kosakata/kanji dari
  `n5-vocabulary.md`; sinonim dari `n5-synonyms.md`.
- **Tracker terpisah** `progress/jlpt-evaluation.md` (per subtipe JLPT). `/jlpt` **boleh
  membaca** `evaluation.md` untuk membiaskan soal grammar ke pola lemah, tapi **hanya
  menulis** `jlpt-evaluation.md` + baris berlabel `JLPT` di `history.md`. **Jangan sentuh**
  `evaluation.md`. Tag subtipe (`MG-*`, `DK-*`) ada di `reference/quiz-taxonomy.md`.
- **Hint fading (scaffolding):** hint di `description` opsi panel **dipudarkan bertahap**
  mengikuti penguasaan — bukan dicabut mendadak (soal jadi beban) atau dibiarkan penuh
  (skor tak jujur). Materi 🔴/🟡/⚪ → hint penuh; menuju 🟢 → hint netral; mantap 🟢 →
  hint dihilangkan (opsi polos gaya ujian asli). Putuskan per subtipe/pola dari tracker.
  Detail di `.claude/skills/jlpt/SKILL.md` ("Hint fading").

## Konvensi menulis catatan lesson

- Struktur tiap `lessons/lesson-0X.md`: judul `# 第X課 — 練習A`, blok **Topik**,
  blockquote **"Ringkasan cepat"** (menyebut SEMUA pola bab), tabel struktur/konjugasi,
  lalu tiap pola diberi **Rumus / Contoh / Catatan**. `→` menandai jenis kalimat.
  Contoh dalam hiragana/katakana; penjelasan Bahasa Indonesia. Konvensi anchor ini
  yang membuat baca-hemat-token valid — patuhi selalu.
- Tiap lesson diakhiri **"Catatan koreksi ejaan (dari catatan asli)"** — daftar tiap
  typo Jepang yang diperbaiki + alasannya.
- **Jaga keutuhan isi.** Saat mengedit catatan, jangan buang materi; **laporkan tiap
  perubahan** yang dilakukan.
- **Saat menambah lesson baru**, update juga: `README.md` (diagram folder + tabel Daftar
  Pelajaran), `reference/quiz-taxonomy.md` (tag pola/partikel baru — WAJIB sebelum quiz
  memakainya), `reference/vocabulary.md` (bagian per-lesson), `reference/particles.md`
  (partikel baru).
- `reference/anki-verbs.md` **auto-generated** — jangan edit tangan. Kalau deck Anki
  bertambah/berubah, jalankan `bash scripts/sync-anki-verbs.sh` untuk re-sync sebelum
  menyusun soal verb.
