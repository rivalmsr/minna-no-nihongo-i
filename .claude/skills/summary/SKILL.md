---
name: summary
description: Tampilkan rincian LENGKAP hasil latihan — breakdown per pola/partikel/lesson, 3 area terlemah, dan rekomendasi. Pelengkap tampilan ringkas /quiz & /jlpt (yang cuma cetak soal salah). Pakai saat user menjalankan /summary (tracker /quiz, evaluation.md) atau /summary jlpt (tracker mock, jlpt-evaluation.md).
---

# Skill: /summary — Rincian Lengkap Hasil Latihan

`/quiz` & `/jlpt` sengaja mencetak tampilan **ringkas** (skor + hanya soal salah) demi
hemat token. Skill ini menyajikan **rincian lengkap** on-demand: breakdown per
pola/partikel/lesson (atau subtipe), 3 area terlemah, dan rekomendasi. **Read-only** —
tidak menulis file apa pun.

## Argumen

`/summary [jlpt]`

- `/summary` (polos) → tracker **`/quiz`**: baca `progress/evaluation.md`.
- `/summary jlpt` → tracker **`/jlpt`**: baca `progress/jlpt-evaluation.md`.

## Sumber data & mode

1. **Rincian sesi terakhir (bila ada di konteks):** kalau `/summary` dijalankan **tepat
   setelah** sesi `/quiz`/`/jlpt` di percakapan yang sama, data per-soal sesi itu masih ada
   di konteks → tampilkan **breakdown sesi itu** (akurasi per pola/partikel/lesson atau per
   subtipe, highlight yang salah).
2. **State tracker (selalu):** baca file tracker terkait untuk **weak areas + status
   terkini** dan **skor sesi terakhir** (baris teratas `progress/history.md`).
3. Kalau tak ada data sesi di konteks (dijalankan di sesi/percakapan baru) → cukup mode
   state tracker: skor terakhir dari `history.md` + weak areas + rekomendasi.

## Hemat token (WAJIB)

Skill ini **melengkapi** mode hemat, jadi jangan boros:
- **Baca hanya file tracker** yang relevan: `evaluation.md` **atau** `jlpt-evaluation.md`
  (bukan keduanya kecuali diminta). Plus baris **teratas** `history.md` untuk skor terakhir.
- **Jangan** baca lesson, kosakata, taxonomy, atau anki-* — tak diperlukan untuk merangkum.
- Rangkum, jangan salin mentah seluruh tabel kalau tak perlu; fokus ke **weak areas +
  ringkasan status per lesson/subtipe**.

## Langkah eksekusi

1. Parse argumen (`jlpt` → tracker mock; selain itu → tracker quiz).
2. **Ambil angka dari engine (disarankan):** `python3 scripts/kb.py summary --kind
   <quiz|jlpt>` → JSON `breakdown` (per pola/partikel/lesson atau subtipe, dgn
   akurasi+status), `weak` (maks 5, terurut), `last_session`, `sesi`. **Pakai angka ini
   apa adanya** — jangan hitung/ranking sendiri (deterministik, sumber tunggal). Prosa
   narasi untuk **weak areas** boleh dibaca dari `evaluation.md`/`jlpt-evaluation.md`
   (bagian yang model tulis) bila perlu konteks kualitatif. (Fallback tanpa engine: baca
   tracker `.md` langsung.)
3. Sajikan (lihat format di bawah) — bungkus angka engine dengan furigana + rekomendasi.

## Format tampilan

Semua kanji **berfurigana**. Struktur:

- **Skor sesi terakhir** — dari `history.md` (tanggal · cakupan · benar/total %).
- **Breakdown sesi terakhir** (bila tersedia di konteks) — akurasi per pola/partikel/lesson
  (`/quiz`) atau per subtipe (`/jlpt`); tandai yang salah.
- **Status tracker per lesson/subtipe** — ringkas (🔴/🟡/🟢/⚪), soroti yang belum 🟢.
- **3 area terlemah** — dari bagian Weak areas tracker (tag + akurasi, urut terendah).
- **Rekomendasi** — materi yang perlu diulang + saran perintah:
  - Tracker quiz → `/quiz review` atau `/quiz lesson X`.
  - Tracker jlpt → `/jlpt review` / `/jlpt moji` / `/jlpt bunpou`; bila lemahnya pola
    grammar, arahkan juga ke `/quiz review`.

## Catatan

- **Read-only.** Jangan sentuh `evaluation.md`, `jlpt-evaluation.md`, `history.md`, atau
  file lain. Kalau user mau latihan lagi, arahkan ke `/quiz` / `/jlpt`.
- Nada ringkas & membantu, Bahasa Indonesia. Angka harus konsisten dengan tracker (jangan
  mengarang skor).
