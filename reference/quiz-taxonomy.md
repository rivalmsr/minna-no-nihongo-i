# Quiz Taxonomy — Tag Pola & Partikel

Daftar **tag stabil** yang dipakai skill `/quiz` untuk menandai tiap soal, supaya
analisis di `progress/evaluation.md` konsisten antar sesi. Setiap soal ditandai
minimal satu **tag pola** + tag **partikel** yang relevan + **lesson** asalnya.

> Aturan: tata bahasa soal **hanya** boleh dari pola di tabel ini (source of truth =
> `lessons/lesson-04..10.md`). Jangan buat tag baru saat menilai; pakai yang ada di sini.
> Kalau ada lesson baru ditambahkan, perbarui tabel ini lebih dulu.

## Tag pola (per lesson)

| Tag | Lesson | Pola |
|-----|--------|------|
| `L4-jam` | 4 | Menyatakan waktu (じ/ふん, ごぜん/ごご) |
| `L4-hari` | 4 | Hari + と penghubung (なんようび) |
| `L4-から-まで` | 4 | Rentang waktu から〜まで |
| `L4-に-waktu` | 4 | Partikel に titik waktu (〜じに おきます) |
| `L4-kata-kerja` | 4 | Konjugasi ます/ません/ました/ませんでした |
| `L5-へ-tujuan` | 5 | Gerak ke tempat 〜へ いきます/きます/かえります |
| `L5-で-transport` | 5 | Alat transportasi 〜で |
| `L5-と-dengan` | 5 | Dengan siapa 〜と (ひとりで) |
| `L5-に-tanggal` | 5 | Keterangan waktu bertanggal 〜に |
| `L5-どこも` | 5 | どこも + 〜ません |
| `L6-を-objek` | 6 | Objek 〜を + kata kerja |
| `L6-します` | 6 | 〜を します (melakukan/bermain) |
| `L6-で-tempat` | 6 | Tempat aktivitas 〜で |
| `L6-に-bertemu` | 6 | 〜に あいます |
| `L6-ませんか` | 6 | Ajakan sopan 〜ませんか |
| `L6-ましょう` | 6 | Ajakan 〜ましょう |
| `L7-で-alat` | 7 | Alat/media 〜で (はしで、にほんごで) |
| `L7-で-bahasa` | 7 | "dalam bahasa" 〜で |
| `L7-に-memberi` | 7 | 〜に あげます/かします/おしえます (kepada) |
| `L7-に-menerima` | 7 | 〜に もらいます/かります/ならいます (dari) |
| `L7-もう` | 7 | もう + kata kerja lampau (まだです) |
| `L8-な-adj` | 8 | な-adjektiva (deskriptif) |
| `L8-い-adj` | 8 | い-adjektiva (deskriptif) |
| `L8-adj-negatif` | 8 | Negatif (じゃありません / 〜くない, いい→よくない) |
| `L8-adj-benda` | 8 | Kata sifat + benda (な penghubung / い langsung) |
| `L8-どう-どんな` | 8 | どう (langsung) vs どんな (+ benda) |
| `L9-が-suka` | 9 | 〜が すきです |
| `L9-が-pandai` | 9 | 〜が じょうずです |
| `L9-が-paham` | 9 | 〜が わかります (よく/だいたい/すこし/ぜんぜん) |
| `L9-punya` | 9 | あります/います (kepemilikan) |
| `L9-から-sebab` | 9 | 〜から "karena" (どうして) |
| `L10-に-keberadaan` | 10 | Tempat keberadaan 〜に + あります/います |
| `L10-あります` | 10 | あります (benda mati/tumbuhan), なにも |
| `L10-います` | 10 | います (manusia/hewan), だれも |
| `L10-posisi` | 10 | Kata posisi (うえ/した/となり/なか/あいだ) |
| `L10-は-lokasi` | 10 | Subjek は + lokasi に + あります/います |

## Tag partikel

`は` · `が` · `を` · `で` · `に` · `へ` · `と` · `から` · `まで` · `も` · `の` · `か`

Untuk partikel multi-fungsi (で, に, から), tandai **juga** tag pola-nya supaya
kelihatan konteks mana yang lemah (mis. `で` bisa transport/tempat/alat/bahasa).
