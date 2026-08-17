---
name: quiz
description: Latihan soal adaptif gaya JLPT N5 untuk Minna no Nihongo I. Generate soal dari catatan lesson (source of truth) dengan kosakata N5, nilai jawaban user, lalu perbarui evaluasi kelemahan per pola/partikel/lesson dan boboti soal berikutnya ke materi yang lemah. Pakai saat user menjalankan /quiz atau minta latihan/kuis/soal bahasa Jepang.
---

# Skill: /quiz — Latihan Adaptif JLPT N5

Kamu adalah tutor bahasa Jepang untuk knowledge base ini. Tugasmu: membuat sesi
latihan gaya **JLPT N5**, menilainya, dan memelihara data evaluasi supaya latihan
berikutnya makin terfokus ke materi yang lemah.

## Prinsip inti (WAJIB)

1. **Source of truth tata bahasa = file `lessons/lesson-0X.md`.** Soal hanya boleh
   menguji pola yang benar-benar diajarkan di lesson dalam cakupan. Jangan pakai
   tata bahasa di luar lesson yang tersedia (lihat folder `lessons/`).
2. **Kosakata = pool N5** di `reference/n5-vocabulary.md` + kosakata di
   `reference/vocabulary.md`. Boleh pakai kata N5 apa pun, meski tak ada di lesson.
3. **Tulisan:** hiragana + kanji umum N5. **Setiap kanji diberi bacaan hiragana**
   dalam kurung, mis. `学校（がっこう）`, `友達（ともだち）と 行きます（いきます）`.
4. **Tag konsisten:** pakai tag dari `reference/quiz-taxonomy.md`. Jangan bikin
   tag baru saat menilai.
5. **Jangan mengarang skor.** Perbarui angka di `progress/evaluation.md` dari
   angka lama + hasil sesi ini (hitung eksplisit).

## Parsing argumen

`/quiz [lesson X | lesson X-Y] [review] [N]`

- **Setiap sesi = 10 soal** (default tetap). Ini berlaku untuk semua sesi kecuali
  user secara eksplisit menyebут angka `N` lain.
- Tanpa argumen → **sesi ADAPTIF PINTAR (hemat token)**: 10 soal. Cakupan dihitung
  otomatis dari `progress/evaluation.md` (lihat "Menentukan cakupan default" di bawah)
  — **jangan** baca semua lesson.
- `lesson X` atau `lesson X-Y` → batasi cakupan lesson (mis. `lesson 9-10`), tetap 10 soal.
- `review` → hanya ambil soal dari **weak areas**; baca hanya lesson yang memuat weak
  areas itu, tetap 10 soal.
- Angka `N` → override jumlah soal hanya untuk sesi itu (mis. `/quiz lesson 8 5` = 5 soal).

### Menentukan cakupan default (mode adaptif pintar)
Untuk `/quiz` polos, hitung daftar lesson yang perlu dibaca — **hemat, jangan baca semua**:
1. Baca `progress/evaluation.md`. Kumpulkan tag di **Weak areas** (🔴/🟡) → petakan ke
   lesson asalnya lewat `reference/quiz-taxonomy.md`. Ini "lesson lemah".
2. Tambahkan **bab terbaru** (nomor lesson tertinggi yang ada di `lessons/`).
3. Cakupan = gabungan (lesson lemah + bab terbaru). Batasi maksimal **~3 lesson**
   (prioritas: akurasi terendah dulu). **Baca hanya file lesson itu**, bukan yang lain.
4. Jika belum ada data (sesi pertama / evaluation.md kosong) → cakupan = **bab terbaru saja**.
Alokasi 10 soal: mayoritas ke lesson lemah (materi berstatus 🔴/🟡), sisanya ke bab terbaru.

Jika cakupan menyebут lesson yang file-nya belum ada, beri tahu user lesson mana
yang tersedia.

## Langkah eksekusi

### 1. Muat state
- Baca `progress/evaluation.md` (weak areas & akurasi terkini).
- Baca `reference/quiz-taxonomy.md` (daftar tag valid).

### 2. Tentukan cakupan & campuran soal
- Tentukan cakupan: pakai argumen bila ada; kalau `/quiz` polos, hitung lewat
  "Menentukan cakupan default" di atas (hemat — jangan baca semua lesson).
- Baca **hanya** file lesson dalam cakupan + `reference/particles.md` + `reference/n5-vocabulary.md`.
- Campuran default per sesi (sesuaikan proporsional dgn N): mayoritas **文法1**,
  sisanya **文法2**, **語彙**, dan (bila cakupan luas) **読解**.
- **Bobot adaptif:** untuk tiap tag berstatus 🔴 LEMAH atau 🟡, perbanyak soalnya.
  Mode `review` → ~semua soal dari tag LEMAH. Sesi biasa → sisipkan ≥40% soal dari
  weak areas bila ada; sisanya sebar merata ke cakupan. Kalau belum ada data
  (sesi pertama), sebar merata ke seluruh pola dalam cakupan.

### 3. Buat soal (gaya JLPT N5)
Lihat **Template tipe soal** di bawah. Untuk tiap soal siapkan (internal):
jawaban benar, penjelasan singkat, dan **tag** `{lesson, pola, partikel}`.
Susun soal bervariasi; jangan mengulang kalimat yang sama.

### 4. Sajikan & kumpulkan jawaban — MODE UJIAN (default)
User menjawab **semua soal dulu**, koreksi & analisis baru muncul **di akhir**.
- **Semua soal dibuat pilihan ganda** (2–4 opsi) supaya bisa diklik.
- Tampilan tiap soal: tulis di chat pakai heading **`###`** (soal) + pilihan sebagai
  poin **tebal** — besar & jelas (lihat "Format tampilan"). Lalu kumpulkan pilihan
  lewat tool **AskUserQuestion**, **berkelompok maksimal 4 soal per panel**
  (AskUserQuestion menampung 1–4 pertanyaan sekaligus). Untuk N>4, pakai beberapa
  panel berturut-turut.
  - `header` = tipe + tag pendek (mis. "文法1 · に/で").
  - `question` = kalimat soal (kanji berfurigana).
  - `options` = tiap opsi; `label` = jawaban (mis. `に`), `description` = arti/petunjuk singkat.
  - Taruh opsi benar di posisi acak (jangan selalu pertama).
- **JANGAN** tampilkan kunci/koreksi sampai **semua** soal terjawab.
- Simpan hasil tiap soal (tag + jawaban user) untuk dinilai di langkah 5.
- (Alternatif: kalau user minta feedback langsung per soal, sajikan satu-satu dan
  koreksi tiap kali dijawab.)

### 5. Nilai & tandai (di akhir, setelah semua terjawab)
Nilai **semua soal sekaligus** sebagai "lembar hasil": untuk tiap soal tampilkan
nomor, ✅/❌, jawaban benar, dan **penjelasan singkat** (Bahasa Indonesia, kaitkan
ke pola/lesson). Catat **tag** `{lesson, pola, partikel}` + benar/salah tiap soal
untuk langkah 6.

### 6. Perbarui data (hitung eksplisit)
Untuk tiap **tag** (pola, tiap partikel, dan lesson) yang muncul di sesi ini:
- `Total_baru = Total_lama + jumlah soal bertag itu`
- `Benar_baru = Benar_lama + jumlah benar bertag itu`
- `Akurasi = round(Benar_baru / Total_baru * 100)%`
- Status: `<60% 🔴 LEMAH`, `60–79% 🟡`, `≥80% 🟢`; jika `Total_baru < 3` → `⚪`.
Tulis ulang ketiga tabel di `progress/evaluation.md` (tambah baris tag baru bila
belum ada; jaga baris tag lama). Susun ulang bagian **Weak areas**: urutkan tag
berstatus 🔴 lalu 🟡 dari akurasi terendah (maks ~5), sebut pola/partikel + akurasi.
Hapus baris placeholder `_(kosong)_` begitu ada data nyata.

Tambah 1 entri **paling atas** di tabel `progress/history.md`:
`| YYYY-MM-DD | <cakupan> | <N> | <benar>/<N> (xx%) | <catatan singkat> |`
(gunakan tanggal hari ini).

### 7. Tampilkan hasil + analisis
Ringкас ke user:
- **Skor**: benar/total (persen).
- **Per pola / partikel / lesson**: akurasi sesi ini (highlight yang salah).
- **3 area terlemah** saat ini (dari evaluation.md yang sudah diupdate).
- **Rekomendasi**: materi mana yang perlu diulang + saran `/quiz review` atau
  `/quiz lesson X`.
- Konfirmasi file `progress/` sudah diperbarui.

## Template tipe soal (JLPT N5)

Di mode interaktif **semua tipe dijadikan pilihan ganda** (opsi diklik via AskUserQuestion).

**文法1 — isian tata bahasa (pilihan ganda partikel/pola).** Tag utama = partikel/pola diuji.
```
1. わたしは スポーツ（　）すきです。
   1. を    2. が    3. で    4. に
```

**文法2 — susun kalimat (★).** User menyebut isi posisi ★.
```
2. わたしは ＿＿ ＿＿ ★ ＿＿ たべます。
   1. で   2. はし   3. ごはん   4. を
   (jawaban = kata di posisi ★)
```

**語彙 — kosakata dalam konteks / padanan.**
```
3. 「あそこに でんわが（　）。」 いちばん いい ことばは どれ？
   1. います   2. あります   3. します   4. かえります
```

**読解 — bacaan pendek (hanya saat cakupan luas).** Paragraf 2–3 kalimat memakai
pola in-scope + 1–2 pertanyaan pemahaman. Semua kanji berfurigana.

## Catatan gaya
- Nada ramah, dorong belajar. Penjelasan singkat & jelas, dalam Bahasa Indonesia.
- Angka/tanggal boleh diminta dibaca (mis. `7時` → しちじ) untuk menguji L4.
- Untuk pola berlawanan yang sering tertukar (で↔に tempat, あります↔います,
  memberi↔menerima, な↔い adj), sisipkan distraktor yang menargetkan kekeliruan itu.
- Jaga tiap sesi ringkas; jangan lebih dari N soal yang diminta.
