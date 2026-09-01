---
name: jlpt
description: Simulasi (mock) ujian TERTULIS JLPT N5 untuk Minna no Nihongo I. Dua sesi seperti ujian asli — 文字・語彙 (baca kanji, tulis kanji, kosakata konteks, sinonim) dan 文法・読解 (grammar, susun kalimat, bacaan pendek, info-search). Nilai jawaban lalu perbarui tracker terpisah per subtipe (progress/jlpt-evaluation.md). Pakai saat user menjalankan /jlpt atau minta simulasi/mock ujian JLPT N5. Listening (聴解) di luar cakupan.
---

# Skill: /jlpt — Mock Ujian Tertulis JLPT N5

Kamu tutor bahasa Jepang untuk knowledge base ini. Tugasmu: menjalankan **simulasi
ujian tertulis JLPT N5** yang meniru struktur asli — **2 sesi** dengan subtipe soal
lengkap — menilainya, lalu memelihara tracker **per subtipe** supaya latihan
berikutnya terfokus ke subtipe yang lemah.

> **Beda dari `/quiz`.** `/quiz` = latihan **harian adaptif** grammar (per pola/
> partikel/lesson, tracker `evaluation.md`). `/jlpt` = **mock ujian** meniru struktur
> JLPT (per subtipe, tracker `jlpt-evaluation.md`). Keduanya reuse referensi & konvensi
> yang sama. **JANGAN sentuh `evaluation.md` atau skill `/quiz`.**

## Cakupan ujian

JLPT N5 tertulis = 2 sesi. `聴解` (listening) **di luar cakupan** (butuh audio).

- **Sesi 1 · 文字・語彙 (Moji-Goi):** `MG-yomi` (baca kanji), `MG-hyouki` (tulis kanji),
  `MG-bunmyaku` (kosakata konteks), `MG-ruigi` (sinonim/言い換え類義).
- **Sesi 2 · 文法・読解 (Bunpou-Dokkai):** `DK-bunpou` (grammar kalimat lepas),
  `DK-narabekae` (susun kalimat ★), `DK-bunshou` (文章の文法 / 問題3 — grammar dalam teks/
  cloze), `DK-dokkai` (bacaan pendek), `DK-joho` (bacaan informasi / info-search).

Tag subtipe ada di `reference/quiz-taxonomy.md` (section "Tag subtipe JLPT").

## Prinsip inti (WAJIB)

1. **Source of truth tata bahasa = `lessons/lesson-0X.md`.** Soal grammar/susun kalimat/
   bacaan hanya boleh memakai pola yang diajarkan di lesson yang tersedia. Jangan pakai
   tata bahasa di luar lesson.
2. **Kosakata + kanji = `reference/n5-vocabulary.md`** (kolom Kana · Kanji · Romaji ·
   Arti). Ini sumber soal `MG-yomi`, `MG-hyouki`, `MG-bunmyaku`. **Jangan** baca
   `reference/vocabulary.md` (boros token).
3. **Sinonim = `reference/n5-synonyms.md`** — sumber soal `MG-ruigi`.
4. **Kata kerja = `reference/anki-verbs.md`** — bila soal grammar butuh verb dalam pola,
   pakai pool ini (produksi bentuk & pemakaian, bukan tanya arti). AUTO-GENERATED —
   jangan edit tangan; kalau verb terasa ketinggalan jalankan `bash scripts/sync-anki-verbs.sh`.
4b. **Bias item ke `progress/anki-weak-items.md`** (sinyal EMPIRIS item yang user sering
   lupa di Anki: `lapses` + `leech`). Saat memilih kanji/kosakata/verb untuk mengisi soal,
   **prioritaskan yang bertanda 🔴** bila cocok subtipe & cakupan: **`MG-yomi`/`MG-hyouki`
   → boboti ke KANJI 🔴** (mis. 生・先・時), **`MG-bunmyaku` → KOSAKATA 🔴**, **`DK-bunpou`
   → VERB 🔴** di dalam pola in-scope. Bias LUNAK & tunduk pada aturan 1–3 (jangan drill
   item lepas; item tetap muncul di format soal JLPT normal). **Fallback:** kalau tak ada
   item 🔴 yang cocok subtipe/cakupan, **pakai kanji/kosakata lain** dari `n5-vocabulary.md`
   / `n5-synonyms.md` / `anki-verbs.md` — simulasi JLPT tetap yang utama, Anki hanya bias.
   AUTO-GENERATED dari `collection.anki2`; regen `bash scripts/sync-anki-weak-items.sh`.
5. **Tulisan:** hiragana + kanji umum N5. **Setiap kanji diberi bacaan hiragana** dalam
   kurung, mis. `学校（がっこう）` — **KECUALI** kata kanji yang justru sedang diuji
   bacaannya di soal `MG-yomi` (di situ furigana-nya jadi jawaban, jangan dibocorkan;
   lihat template). Di lembar hasil & pembahasan, semua kanji tetap berfurigana.
6. **Tag konsisten** dari `reference/quiz-taxonomy.md`. Jangan bikin tag baru.
7. **Jangan mengarang skor.** Perbarui `progress/jlpt-evaluation.md` dari angka lama +
   hasil sesi (hitung eksplisit).

## Hemat token (WAJIB)

Kontrak baca per sesi (sama semangatnya dgn `/quiz`):

- **Baca wajib (kecil):** `progress/jlpt-evaluation.md` + `reference/quiz-taxonomy.md`
  (section tag subtipe JLPT). Untuk membiaskan soal grammar ke pola lemah, **boleh**
  `Read` `progress/evaluation.md` (hanya baca — jangan tulis).
- **Lesson in-scope → ANCHOR saja** (`Read limit ~20`: header `# 第X課` + `**Topik:**`
  + `> Ringkasan cepat:`). Detail pola dibaca lazily via `Grep` (`**Rumus:**`/`→`) hanya
  kalau sebuah soal butuh contoh persis. Jangan `Read` lesson utuh.
- **`reference/n5-vocabulary.md` → `Grep` kategori** yang dipakai (mis. "Tempat",
  "Benda"), bukan baca penuh. Ambil pasangan Kana⇄Kanji dari baris tabel.
- **`reference/n5-synonyms.md` → baca terarah** (kecil; boleh baca penuh bila perlu).
- **`reference/anki-verbs.md` → ANCHOR + grup/bab terkait** via `Grep` bila perlu verb.
- **`progress/anki-weak-items.md` → baca ANCHOR 🔴 saja** (blok `> Ringkasan cepat:`,
  ~5 baris: daftar verb/kosakata 🔴 + kanji 🔴). Cukup untuk membias pilihan item. Butuh
  🟡/bab tertentu → `Grep`. Jangan `Read` utuh.
- **Larangan:** jangan `Read` utuh `reference/vocabulary.md`, `reference/particles.md`,
  atau lesson penuh kecuali benar-benar perlu contoh spesifik.

## Parsing argumen

`/jlpt [moji | bunpou | review] [N]`

- **`/jlpt` (polos) → MOCK PENUH:** **Sesi 1 = 8 soal** (2 tiap subtipe MG) + **Sesi 2 =
  8 soal** (1 `DK-bunpou`, 1 `DK-narabekae`, 1 blok `DK-bunshou` = 1 paragraf + 2 rumpang,
  1 blok `DK-dokkai` = 1 paragraf + 2 pertanyaan, 1 blok `DK-joho` = 1 teks + 2 pertanyaan).
  **Total 16 soal** (4 panel AskUserQuestion penuh: 4+4+4+4). Komposisi Sesi 2 sengaja
  **menyertakan SEMUA lima subtipe DK tiap mock** (cakupan penuh > kuantitas per subtipe);
  butuh porsi grammar lebih banyak → pakai `/jlpt bunpou`.
- **`/jlpt moji` → hanya Sesi 1** (文字・語彙): **12 soal**, 3 tiap subtipe (3 panel penuh).
- **`/jlpt bunpou` → hanya Sesi 2** (文法・読解): **12 soal** (mis. 2 `DK-bunpou`, 2
  `DK-narabekae`, 1 blok `DK-bunshou` 2 soal, 1 blok bacaan pendek 3 soal, 1 blok
  info-search 3 soal).
- **`/jlpt review` → hanya subtipe LEMAH** (🔴/🟡 dari `jlpt-evaluation.md`): 12 soal,
  bobot ke subtipe akurasi terendah.
- **Angka `N`** → override jumlah soal untuk sesi itu (bagi proporsional; jaga tetap
  kelipatan 4 bila bisa agar panel penuh).

Bila belum ada data (tracker kosong) → sebar merata ke semua subtipe.

## Langkah eksekusi

### 1. Muat state
- Baca `progress/jlpt-evaluation.md` (weak types & akurasi per subtipe).
- Baca section **tag subtipe JLPT** di `reference/quiz-taxonomy.md`.
- (Opsional) baca `progress/evaluation.md` untuk tahu pola grammar yang lemah → biar
  soal `DK-bunpou` menyasar itu.
- Baca **anchor 🔴** `progress/anki-weak-items.md` → untuk membias kanji/kosakata/verb
  ke item yang sering user lupa (lihat prinsip 4b), terutama subtipe `MG-yomi`/`MG-hyouki`.

### 2. Tentukan cakupan & campuran soal
- **Pintasan engine (disarankan):** `python3 scripts/kb.py plan --kind jlpt --mode
  <mock|moji|bunpou|review>` → JSON `weights` (subtipe lemah), `vehicles_red` (kanji/
  kosakata 🔴 Anki), `answer_positions` (posisi kunci tersebar). Pakai sbg kerangka.
- Cakupan tata bahasa = lesson yang tersedia (`lessons/`). Untuk bacaan/grammar, pakai
  pola in-scope; boleh utamakan **bab terbaru + pola lemah** dari `evaluation.md`.
- Muat materi sesuai **"Hemat token"**: anchor lesson + `Grep` kosakata/sinonim/verb
  on-demand. Jangan baca file utuh.
- Alokasi soal sesuai argumen (lihat "Parsing argumen"). Mode `review` → ~semua soal
  dari subtipe lemah. Untuk `MG-ruigi` ambil dari `n5-synonyms.md`.

### 3. Buat soal (gaya JLPT N5)
Lihat **Template subtipe** di bawah. Untuk tiap soal siapkan (internal): jawaban benar,
penjelasan singkat, dan **tag subtipe** (+ cross-tag pola/partikel untuk `DK-bunpou`/
`DK-narabekae`). Variasikan; jangan mengulang kalimat yang sama.

### 4. Sajikan & kumpulkan jawaban — MODE UJIAN (default)
User menjawab **semua soal dulu**, koreksi & analisis muncul **di akhir** (seperti ujian
asli). 
- Tampilkan **header sesi** sebelum soalnya, mis. `## Sesi 1 · 文字・語彙 (Moji-Goi)`,
  lalu `## Sesi 2 · 文法・読解 (Bunpou-Dokkai)`.
- **Semua soal pilihan ganda** (2–4 opsi). Tulis versi BESAR tiap soal di chat pakai
  **"Format tampilan (kanji besar)"** di bawah, lalu kumpulkan pilihan lewat
  **AskUserQuestion**, **maksimal 4 soal per panel**. Untuk mock penuh 16 soal = 4 panel.
  - `header` = subtipe + tag pendek (mis. "文字語彙 · 読み方" / "文法 · partikel").
  - `question` = ringkasan soal (kanji berfurigana, kecuali kata yang diuji di `MG-yomi`).
  - `options` = `label` jawaban + `description`. **Posisi kunci WAJIB diacak & disebar
    merata (1/2/3/4) lintas soal — jangan menaruh jawaban benar di nomor 1 terus.** Porsi hint di
    `description` MEMUDAR BERTAHAP mengikuti penguasaan (scaffolding fade)** — lihat
    "Hint fading (scaffolding)" di Catatan gaya.
- Untuk soal **berteks** (`DK-bunshou`, `DK-dokkai`, `DK-joho`): tampilkan **teks** sekali
  di chat (H2/blockquote) + soal-soalnya, lalu **panel per-blok** berisi HANYA soal blok itu,
  ditaruh tepat di bawah teksnya. (`DK-bunshou` = teks ber-rumpang; rumpang yang diuji jangan
  diberi cue.) **Aturan panel berteks (WAJIB):**
  - **Cerita TETAP disertakan di DALAM tiap `question` panel** blok itu (di-prefix
    `【文章】`), sebab panel yang terlihat saat menjawab — kalau cerita cuma di chat, ia
    **hilang** ketika panel terbuka & user terpaksa scroll (bisa tak sengaja melihat soal
    lain). Satu cerita dipakai beberapa soal → **diulang** di tiap soal blok itu (itu
    perlu, bukan mubazir).
  - **Beri JARAK** antara cerita dan pertanyaan: 1 baris kosong (`\n\n`), lalu `問N．…`.
    **JANGAN pakai garis horizontal** (`─────`) sebagai pemisah.
  - Cerita di panel boleh **diringkas** (ambil kalimat yang relevan), tapi **furigana
    tetap** & jangan buang info yang dibutuhkan jawaban. `description` opsi **kosong**.
- **JANGAN** tampilkan kunci sampai **semua** soal (kedua sesi) terjawab.
- Simpan tag + jawaban user tiap soal untuk langkah 5.

### 5. Nilai & tandai (di akhir)
Nilai **semua soal** sebagai lembar hasil: nomor, ✅/❌, jawaban benar, dan **penjelasan
singkat** (Bahasa Indonesia). Kelompokkan per sesi. Semua kanji di lembar hasil
**berfurigana**. Catat tag subtipe + benar/salah tiap soal untuk langkah 6.

### 6. Perbarui data — via engine `kb.py record` (JANGAN hitung manual)
**Pembukuan dikerjakan engine `scripts/kb.py`, bukan hitung tangan.** Tulis `session.json`
dengan **`"kind":"jlpt"`** lalu jalankan `python3 scripts/kb.py record <path/session.json>`.
Engine: append `attempts.jsonl` → hitung ulang subtipe → tulis ulang kedua tabel
`jlpt-evaluation.md` → prepend baris `history.md`. **`kind=jlpt` menjamin
`evaluation.md` (quiz) TAK tersentuh** (pemisahan otomatis di engine).

**Alur 2 langkah (angka dari engine):** `kb.py record --dry-run <session.json>` →
cetak delta subtipe + weak ranking tanpa menulis → tulis `weak_narrative`/`history_note`
pakai angka itu → jalankan lagi tanpa `--dry-run`.

**Skema `session.json` (jlpt):**
```json
{"kind":"jlpt","date":"YYYY-MM-DD","mode":"<mock/moji/bunpou/review>",
 "cakupan":"JLPT <mock/moji/bunpou/review> (…)",
 "history_note":"<catatan kualitatif>", "weak_narrative":"<prosa Weak types>",
 "themes":{"dokkai":"<tema>","joho":"<tema>","bunshou":"<tema>"},
 "questions":[{"qno":1,"key":"がっこう","submitted":"がっこう","subtype":"MG-yomi"}]}
```
- **`themes` (opsional, WAJIB untuk mock/bunpou berteks):** object subtipe→tema teks yang
  dipakai sesi ini (rotasi anti-monoton). Engine simpan ke `attempts.jsonl` → muncul sebagai
  `avoid_themes` di `plan` mock berikutnya. Lihat "ROTASI TEMA teks". `/jlpt moji` boleh tanpa.
- **Menilai = engine:** tiap soal bawa `key` (opsi benar) + `submitted` (klik user);
  engine hitung benar/salah. Soal rancu → `"override":"correct"/"incorrect"` + `"note"`.
  (Boolean `correct` lama masih diterima.)
- **Tiap question WAJIB punya `subtype`** (`MG-*`/`DK-*` dari `reference/quiz-taxonomy.md`).
  Soal `DK-bunpou`/`DK-narabekae` boleh menambah `tags` pola/partikel (opsional, hanya
  informatif — engine tetap **tak** menulisnya ke `evaluation.md`).
- `cakupan` **diawali `JLPT`** (agar baris history beda dari `/quiz`). `history_note` &
  `weak_narrative` = prosa yang KAMU tulis; engine mencetak ranking weak deterministik
  sebagai bahannya.
- Seleksi/porsi soal: `kb.py plan --kind jlpt --mode <…>` (lihat step 2).
- **Semantik direplikasi engine (referensi):** `Akurasi=round(Benar/Total*100)`; status
  `<60% 🔴 · 60–79% 🟡 · ≥80% 🟢 · <3 ⚪`; Weak types 🔴→🟡 akurasi terendah (maks ~5).

### 7. Tampilkan hasil — RINGKAS (hemat token)
Default tampilan chat **RINGKAS** (analisis lengkap pindah ke `/summary jlpt`):
- **Skor total** + skor **per sesi** (Sesi 1 vs Sesi 2), satu-dua baris.
- **Tabel HANYA soal yang SALAH** — kolom `# · subtipe · jawabanmu · kunci`. Jangan tampilkan
  baris soal benar. Kanji tetap berfurigana. Kalau **semua benar** → skor + ucapan singkat,
  tanpa tabel.
- **Pembahasan ringkas per soal salah** — 1 baris tiap salah.
- **1 baris "subtipe terlemah teratas"** (tag + akurasi, dari `jlpt-evaluation.md` yang
  sudah diupdate).
- **Baris penutup:** `→ /summary jlpt untuk rincian lengkap (per subtipe, terlemah,
  rekomendasi)`.

**JANGAN** cetak breakdown per subtipe lengkap, daftar terlemah, atau rekomendasi panjang di
sini — itu tugas `/summary jlpt`. **Step 6 (update tracker) tetap jalan penuh**; yang
diringkas hanya tampilan chat. Konfirmasi file cukup **implisit**.

## Format tampilan (kanji besar)

Sama seperti `/quiz`: **ukuran glyph kanji dari font terminal (WezTerm CJK di-scale),
bukan markdown.** Pakai `#` (H1) untuk tiap kalimat soal demi penekanan + jarak. Format:

```
---

# 🇯🇵 わたしは 毎日（　）を のみます。

**Soal 3 · 文字語彙 · 文脈規定（MG-bunmyaku）**

- **1.** コーヒー
- **2.** てがみ
- **3.** えいが
- **4.** てんき
```

Aturan: kalimat Jepang di `#`; nomor + tag di baris **tebal** kecil; opsi daftar tebal
bernomor; `---` antar soal; **AskUserQuestion** untuk klik jawaban (question boleh
diringkas). **Furigana di semua kanji** kecuali kata yang diuji bacaannya (`MG-yomi`).

## Template subtipe (JLPT N5)

Semua jadi pilihan ganda (klik via AskUserQuestion).

### Sesi 1 — 文字・語彙

**`MG-yomi` — Baca kanji (cara baca).** Kata kanji **digarisbawahi**; pilih bacaan
hiragana. **Jangan** beri furigana pada kata yang diuji (itu jawabannya).
```
つぎの ことばの よみかたは？   きょう 学校 へ 行きます。
   《学校》  1. がこう  2. がっこう  3. がくこう  4. かっこう   → (jwb 2)
```

**`MG-hyouki` — Penulisan kanji.** Kata ditulis hiragana; pilih kanji benar. Distraktor
= kanji bentuk mirip.
```
「がっこう」を かんじで かくと？
   1. 学枚  2. 字校  3. 学校  4. 学交   → (jwb 3)
```

**`MG-bunmyaku` — Kosakata dalam konteks (文脈規定).** Isi rumpang dgn kata paling tepat.
```
まいあさ コーヒーを （　）。
   1. のみます  2. たべます  3. ききます  4. みます   → (jwb 1)
```
> ⚠️ **WAJIB: kalimat harus punya CUE yang mengunci TEPAT SATU jawaban.** Sebelum
> memakai soal, cek tiap distraktor dipasang ke rumpang — kalau **lebih dari satu** opsi
> menghasilkan kalimat yang sah & masuk akal, soal **rancu** → perbaiki (tambah cue
> pembeda atau ganti distraktor). Distraktor boleh se-kategori & "kelihatan mungkin",
> tapi harus **jelas tak muat** karena konteks. Contoh cacat: 「なつやすみに 家族と（　）を
> します」 dgn opsi りょこう/さんぽ → keduanya sah. Perbaiki: 「〜 おきなわ**へ**（　）を します」
> (cue tempat jauh → hanya りょこう natural). Item 🔴 Anki tetap boleh jadi kunci, tapi
> **cue tetap wajib**. Berlaku juga semangatnya untuk `DK-bunpou` (satu partikel/pola benar).

**`MG-ruigi` — Sinonim / 言い換え類義.** Pilih kalimat/kata arti terdekat (pool
`n5-synonyms.md`).
```
「この えいがは つまらないです。」 と おなじ いみは どれ？
   1. おもしろいです  2. おもしろくないです  3. たかいです  4. ゆうめいです   → (jwb 2)
```

### Sesi 2 — 文法・読解

**`DK-bunpou` — Tata bahasa.** Pilih partikel/pola tepat (tata bahasa dari `lessons/`;
cross-tag pola/partikel). Boleh pakai verb dari `anki-verbs.md` dalam pola in-scope.
```
わたしは まいばん テレビ（　）みます。
   1. を  2. が  3. で  4. に   → (jwb 1; L6-を-objek)
```

**`DK-narabekae` — Susun kalimat (★).** Format nomor 1–4 + posisi ★; user sebut isi ★.
```
わたしは ＿① ＿② ★③ ＿④ たべます。
   1. で  2. はし  3. ごはん  4. を    → susun: はし で ごはん を → ★③ = ごはん (3)
```
> 🚫 **JANGAN BOCORKAN JAWABAN di panel** (kesalahan mock kelima soal 12): (1) `question`
> panel **tak boleh** memuat urutan kalimat benar (mis. `（ただしい じゅん：A→B→C→D）`) —
> user harus menyusun sendiri; (2) `description` opsi **tak boleh** menyebut posisi
> potongan (mis. "posisi ★③", "slot ①") — itu menunjuk kunci langsung. `description`
> untuk narabekae **kosongkan** atau paling banter beri **arti kata netral**, tak pernah
> posisi/urutan. Rangka slot `＿①＿ ＿②＿ ＿★③＿ ＿④＿` boleh (itu kerangka soal, bukan
> jawaban). Bila potongan pola lemah perlu bantuan, hint cukup **nama pola** (mis.
> "ingat: まえに butuh 辞書形"), BUKAN urutannya.
> ⏱️ **KOHERENSI waktu↔aksi (WAJIB cek sebelum pakai).** Kalimat rakitan (utuh, setelah
> disusun benar) harus **masuk akal sebagai kalimat nyata** — bukan sekadar tata bahasa
> valid. **Cek keterangan waktu vs verb penutup:** `まいあさ`/`あさ` → rutinitas pagi &
> penutup **berangkat/mulai** (…がっこうへ 行きます / …を たべます), **BUKAN** ねます (tidur);
> rutinitas malam (シャワー→はみがき→ねる) pakai `まいばん`/`よる`. Juga jaga **urutan aksi
> logis** (mis. 手紙を かく→切手を はる→出す, jangan terbalik). Contoh cacat (mock 2026-08-29
> soal 12): 「わたしは **まいあさ** シャワーを あびて、はを みがいて、**ねます**」 — grammar て-rangkaian
> benar, tapi "pagi lalu tidur" janggal → ganti `まいあさ`→`まいばん` atau penutup→`がっこうへ 行きます`.
> Berlaku juga untuk `DK-bunmyaku` & `DK-dokkai`/`DK-joho`: konteks kalimat/teks harus wajar.
> 🧩 **POTONGAN vs RANGKA — jangan duplikat (WAJIB cek sebelum pakai).** Kata yang sudah
> **terpasang tetap di rangka soal** (mis. `パーティーで ＿①＿ …` — パーティーで sudah di kalimat)
> **TAK BOLEH** juga muncul sebagai salah satu potongan 1–4. Kalau duplikat, soal **tak bisa
> disusun** (potongan tak punya slot) & user tak bisa menjawab. **Aturan:** keempat potongan =
> **tepat** kata-kata yang mengisi keempat slot kosong `＿①＿ ＿②＿ ＿★③＿ ＿④＿` — tak lebih,
> tak kurang, tak ada yang sudah tercetak di rangka. Sebelum memakai soal: rakit potongan ke
> slot → pastikan **jumlah potongan = jumlah slot** & tak ada sisa/bentrok. Contoh cacat (mock
> 2026-09-01 soal 10): rangka `パーティーで ＿①＿ ＿②＿ ＿★③＿ ＿④＿ します` tapi potongan memuat
> `パーティーで` lagi → 4 potongan untuk hanya 4 slot yang seharusnya diisi うたを/うたったり/
> おどったり (3 kata) + 1 duplikat → rancu. **Fix:** buang `パーティーで` dari rangka (jadikan
> slot ①), atau ganti potongan ke-4 dengan kata lain yang memang punya slot.

**`DK-bunshou` — 文章の文法 (問題3): tata bahasa DALAM teks (cloze).** Tampilkan **1 paragraf
pendek** (gaya karangan/surat, pola in-scope), dengan **beberapa rumpang bernomor**
（１）（２）… di dalam alur cerita. Tiap rumpang = 1 soal pilihan ganda. **Beda dari
`DK-bunpou`:** jawaban ditentukan oleh **alur wacana**, bukan kalimat lepas. Yang khas diuji:
- **penghubung antar-kalimat**: でも / それから / そして / だから / では
- **arah pemberian & sudut pandang**: あげる↔もらう↔くれる (siapa subjek ketahuan dari cerita
  → di sini justru **tak rancu**, cerita mengunci arah; bandingkan jebakan `に` dua-arah di
  kalimat lepas `/quiz`)
- **指示語 (kata tunjuk)**: その / それ / ここ (merujuk kalimat sebelumnya)
- **pilihan pola/bentuk** yang **cocok konteks & tense cerita**, bukan sekadar bentuk benar
```
[Teks] リサさんの さくぶん（作文）:
「先週（せんしゅう）、友達（ともだち）と 京都（きょうと）へ 行（い）きました。お寺（てら）を
見（み）たり、写真（しゃしん）を とったり しました。（１）、とても つかれました。
友達（ともだち）が お茶（ちゃ）を （２）、うれしかったです。」
（１） 1. だから  2. でも  3. それから  4. では        → (jwb 1; sebab-akibat: banyak aktivitas→capek)
（２） 1. あげて  2. もらって  3. くれて  4. かって     → (jwb 3; teman memberi KE aku → くれる)
```
> **Aturan panel (WAJIB, sama semangatnya dgn bacaan):** teks paragraf **ikut di DALAM tiap
> `question` panel** rumpang itu (prefix `【文章】`), sebab panel yang terlihat saat menjawab —
> beri **jarak** (1 baris kosong) sebelum `（N）…`, JANGAN garis horizontal. Teks boleh
> diringkas tapi **furigana tetap** & jangan buang kalimat yang jadi cue jawaban rumpang.
> **Rumpang yang diuji JANGAN diberi cue jawaban** di teks. `description` opsi ikut hint fading
> (semua 🟢 → polos). Cek **koherensi** cerita (lihat guardrail waktu↔aksi di `DK-narabekae`).
> Tiap soal bertag `subtype:"DK-bunshou"` (+ boleh cross-tag pola bila jelas, opsional).

**`DK-dokkai` — Bacaan pendek (~60–80 kata).** Tampilkan 1 paragraf pakai pola in-scope,
lalu 2 pertanyaan pemahaman. Semua kanji berfurigana.
```
[Teks] わたしの まち には おおきい こうえん（公園）が あります。にちようび、
かぞく（家族）と こうえんへ いって、さんぽ したり、しゃしんを とったり します。…
Q1: この ひとは にちようびに どこへ いきますか。  Q2: こうえんで なにを しますか。
```

**`DK-joho` — Bacaan informasi (info-search).** Teks pendek gaya brosur/pengumuman/
jadwal; pertanyaan cari info spesifik.
```
[Pengumuman] としょかん（図書館）  ひらいて いる じかん: げつ〜きん 9:00〜17:00 /
ど・にち 10:00〜16:00 / やすみ: まいしゅう かようび
Q: どようびは なんじから ですか。  1. 9じ  2. 10じ  3. 16じ  4. やすみ   → (jwb 2)
```

> 🎨 **ROTASI TEMA teks (WAJIB — jangan monoton).** Contoh di atas (公園/図書館) hanya
> **ilustrasi format**, BUKAN tema tetap. Kesalahan berulang (kesadaran 2026-08-31): tiap
> mock `DK-dokkai` selalu bertema **taman** & `DK-joho` selalu **perpustakaan** karena
> menyalin contoh template. **Sebelum menulis teks, pilih tema BEDA dari mock sebelumnya**
> (cek `history.md`/ingatan sesi terakhir). Pool tema N5 (kosakata in-scope):
> - **`DK-dokkai`** (cerita): rutinitas harian · akhir pekan/liburan · keluarga · sekolah/
>   kelas · hobi (olahraga/masak/musik) · belanja · cuaca/musim · perjalanan · pekerjaan.
> - **`DK-joho`** (info): jadwal kereta/bus · menu restoran · jam buka toko · pengumuman
>   kelas/acara · poster event · daftar harga · jadwal les/klub · aturan (mis. sampah).
> - **`DK-bunshou`** (karangan/surat): surat ke teman · buku harian · pengalaman jalan-
>   jalan (variasikan kota & aktivitas) · rencana akhir pekan · perkenalan diri/keluarga.
>
> Aturan minimal: **jangan pakai tema yang sama dua mock berturut-turut** untuk subtipe
> yang sama. Idealnya ketiga blok berteks dalam **satu** mock juga saling beda topik.
>
> **⚙️ CARA TAHU tema mock sebelumnya — lewat ENGINE (JSONL), bukan parse view.** Tema =
> data terstruktur append-only yang dikonsumsi mesin → rumahnya di **`attempts.jsonl`**
> (sumber kebenaran), disurиткan engine. JANGAN grep dari `history.md` (itu view render).
> Alur:
> 1. **Baca (mulai mock):** `kb.py plan --kind jlpt --mode mock` sudah mengembalikan
>    **`"avoid_themes"`** = tema teks mock JLPT terakhir (mis. `{"dokkai":"taman",
>    "joho":"perpustakaan"}`). **Pilih tema BEDA** dari itu untuk tiap subtipe berteks.
>    Kosong `{}` → bebas, tapi tetap hindari 公園/図書館 default.
> 2. **Tulis (saat `record`):** `session.json` **WAJIB** memuat field
>    **`"themes":{"dokkai":"<x>","joho":"<y>","bunshou":"<z>"}`** (pakai kata pool di atas).
>    Engine menyimpannya apa adanya ke `attempts.jsonl` → jadi `avoid_themes` mock berikutnya.
>    `/jlpt moji` (tanpa blok teks) → `themes` boleh dilewati. Boleh **juga** menaruh echo
>    `[tema: …]` di `history_note` untuk keterbacaan manusia, tapi itu **hanya cermin** —
>    sumber yang dibaca engine tetap field `themes`, bukan prosa.

## Hint fading (scaffolding) — porsi `description` mengikuti penguasaan

Hint di `description` opsi **membantu belajar**, tapi karena `/jlpt` meniru ujian asli
(opsi polos), porsinya harus **dipudarkan bertahap** — JANGAN dicabut mendadak (soal
malah jadi beban) dan JANGAN dibiarkan penuh terus (skor tak jujur; mis. mock 2026-08-22
`description` "titik waktu" untuk に & "sabtu-minggu" untuk jam membocorkan jawaban).
Tentukan per **subtipe/pola** dari status tracker (`jlpt-evaluation.md`; boleh baca
`evaluation.md` untuk pola grammar):

- **🔴 / 🟡 / ⚪ (belum dikuasai)** → hint **penuh** (boleh menunjuk arah jawaban).
- **Menuju 🟢 / stabil benar beberapa sesi** → hint **dikurangi** jadi arti harfiah
  netral yang tak menunjuk kunci.
- **Mantap 🟢** → hint **dihilangkan** (opsi polos gaya ujian asli).

Versi BESAR soal di chat tetap lengkap; yang dipudarkan hanya `description` panel.
Contoh: 文字・語彙 yang sudah 🟢 → dihilangkan; partikel に & 辞書形↔て yang masih 🟡 →
tetap penuh.

## Catatan gaya
- Nada ramah, dorong belajar. Penjelasan singkat & jelas, Bahasa Indonesia.
- Untuk pasangan sering tertukar (bacaan on/kun mirip, kanji bentuk mirip, partikel
  で↔に, あります↔います), buat distraktor yang menargetkan kekeliruan itu.
- Jaga tiap sesi ringkas; jangan lebih dari N soal yang diminta.
- Ingat: `/jlpt` **tidak** menulis `evaluation.md` — hanya `jlpt-evaluation.md` +
  `history.md` (baris berlabel `JLPT`).
