# CLAUDE.md — Konteks Project

> Hub konteks yang **selalu ter-load**. Sengaja ringkas: **aturan lintas-sesi** ada di
> sini; **detail operasional** di skill (`.claude/skills/*`); **desain sistem** di `docs/*`
> (mulai `docs/cara-kerja.md`); **indeks file lengkap** di `README.md`.

## Project

KB pribadi belajar bahasa Jepang dari **Minna no Nihongo I (みんなの日本語 I)**, target
**JLPT N5**. Penjelasan **Bahasa Indonesia**, contoh kalimat **Bahasa Jepang**; dibaca/
dirapikan di **Obsidian**. Dua fungsi: (1) **catatan materi** per 課 di `lessons/*.md` +
referensi `reference/*`; (2) **latihan adaptif** `/quiz` (harian) & `/jlpt` (mock ujian) —
active recall + evaluasi titik lemah dari materi yang sudah dicatat.

## Sumber kebenaran (source of truth)

| Untuk | File |
|---|---|
| Tata bahasa | `lessons/lesson-0X.md` — **jangan uji pola di luar ini** |
| Kosakata N5 | `reference/n5-vocabulary.md` · sinonim `reference/n5-synonyms.md` |
| Kata kerja | `reference/anki-verbs.md` — AUTO-GENERATED (jangan edit tangan) |
| Item lemah Anki | `progress/anki-weak-items.md` — AUTO-GENERATED (lapses+leech) |
| Skor & status | `progress/attempts.jsonl` (+ `baseline.json`) → engine `scripts/kb.py` |
| Tag pola/partikel/subtipe | `reference/quiz-taxonomy.md` |
| Tracker (view) | `evaluation.md` (/quiz) · `jlpt-evaluation.md` (/jlpt) · `history.md` — semua AUTO-GENERATED |

## Aturan lintas-sesi (WAJIB — jangan hilang)

1. **Pembukuan = engine, bukan manual.** Skor/status/ranking/seleksi cakupan `/quiz` &
   `/jlpt` dikerjakan `scripts/kb.py`; tracker `.md` = view AUTO-GENERATED. Tiap akhir
   sesi: tulis `session.json` → `python3 scripts/kb.py record <session.json>` (JANGAN
   hitung angka tabel dengan tangan). **Grading = engine:** tiap soal bawa `key`+`submitted`
   (soal rancu → `override`+`note`). **Angka narasi:** `kb.py record --dry-run` dulu, baru
   tulis prosa. Seleksi cakupan `kb.py plan`; breakdown `kb.py summary`. Detail:
   `docs/engine-bookkeeping-plan.md`.
2. **Log perbaikan.** Tiap kali **aturan/logika/skill diperbaiki** (bukan sekadar tambah
   materi atau update skor), catat 1 entri **Problem→Fix→Tanggal** di `docs/perbaikan-kb.md`
   (terbaru di atas) — jejak "kenapa" tiap keputusan desain.
3. **Jaga keutuhan isi.** Saat mengedit catatan, jangan buang materi; **laporkan tiap
   perubahan** yang dilakukan.
4. **Hemat token.** Baca **anchor** lesson (header + Topik + "Ringkasan cepat", ~20 baris),
   bukan file utuh; detail pola/partikel/kosakata via `Grep` on-demand. Jangan `Read` utuh
   `vocabulary.md` / `particles.md` / lesson penuh saat latihan.

## /quiz & /jlpt — inti (detail lengkap di skill)

`/quiz` = latihan **harian adaptif** grammar; **jangan diubah** untuk kebutuhan JLPT.
`/jlpt` = **simulasi ujian tertulis N5** (2 sesi: 文字・語彙 + 文法・読解; 聴解/listening di
luar cakupan). Langkah eksekusi, template soal, parsing argumen **ada di skill — jangan
ulang di sini:** `.claude/skills/{quiz,jlpt,summary,sync-anki}/SKILL.md`.

Yang tak boleh dilanggar:
- **Hanya uji materi di KB ini** (lihat tabel source of truth). Bobotkan ke **weak areas**
  (`evaluation.md`); sisanya konfirmasi materi yang sudah dikuasai.
- **Verb = kendaraan active recall**, bukan drill konjugasi lepas — paksa produksi bentuk
  (て/ない/辞書/た) **di dalam pola in-scope yang lemah**.
- **Bias LUNAK ke item 🔴 Anki** saat memilih kosakata pengisi soal (bukan pengganti pola;
  fallback ke kosakata lain bila janggal). Refresh: buka **Anki desktop & Sync dulu**
  (sync iPhone saja tak update file) → `bash scripts/sync-anki-weak-items.sh`. Detail:
  `docs/anki-integration-plan.md`.
- **/jlpt tracker terpisah:** boleh **baca** `evaluation.md` (bias ke pola lemah) tapi
  **hanya tulis** `jlpt-evaluation.md` + baris `JLPT` di `history.md`. **Jangan sentuh**
  `evaluation.md`.

## Preferensi tampilan (tersimpan — jangan dilupakan; contoh di skill)

- **Mode ujian:** jawab semua soal dulu, koreksi & analisis **di akhir**. Default **12 soal**
  (3 panel AskUserQuestion penuh 4+4+4).
- **Semua kanji berfurigana** — termasuk tabel hasil, ringkasan, **dan panel** (blank
  `（　）` → taruh furigana di luar blank: `大学生（だいがくせい）（　）`).
- Kalimat Jepang tampil **besar & tebal** (H1 `#`); jawaban diklik lewat panel AskUserQuestion.
- **Acak posisi kunci** (sebar merata 1/2/3/4; jangan selalu nomor 1 — berlaku /quiz & /jlpt).
  Soal susun kalimat (文法2): format nomor 1–4 + posisi **★** gaya JLPT asli.
- Keterangan opsi panel **simetris** (jangan cuma kunci yang bergloss = tell halus) &
  **hint fading** bertahap ikut penguasaan (🔴/🟡/⚪ penuh → 🟢 dihilangkan).
- **Hasil = RINGKAS:** skor + tabel **soal SALAH saja** + pembahasan ringkas + 1 baris area
  terlemah. Breakdown penuh via **`/summary`** (`/summary jlpt` untuk tracker mock).

## Konvensi catatan lesson

- Struktur `lessons/lesson-0X.md`: judul `# 第X課 …`, blok **Topik**, blockquote
  **"Ringkasan cepat"** (menyebut SEMUA pola bab), tabel struktur/konjugasi, lalu tiap pola
  diberi **Rumus / Contoh / Catatan**; `→` menandai jenis kalimat. Contoh hiragana/katakana,
  penjelasan Bahasa Indonesia. Konvensi anchor ini yang membuat baca-hemat-token valid.
- Akhiri tiap lesson dengan **"Catatan koreksi ejaan (dari catatan asli)"** (tiap typo
  Jepang yang diperbaiki + alasannya).
- **Saat menambah lesson baru, update juga:** `README.md` (diagram folder + tabel Daftar
  Pelajaran), `reference/quiz-taxonomy.md` (tag pola/partikel baru — WAJIB sebelum quiz
  memakainya), `reference/vocabulary.md` (bagian per-lesson), `reference/particles.md`
  (partikel baru).
- `reference/anki-verbs.md` auto-generated — jalankan `bash scripts/sync-anki-verbs.sh`
  untuk re-sync kalau deck Anki berubah.
