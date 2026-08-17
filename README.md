# みんなの日本語 I — Knowledge Base

Basis pengetahuan (knowledge base) untuk belajar bahasa Jepang menggunakan buku
**Minna no Nihongo I (みんなの日本語 I)**. Penjelasan ditulis dalam Bahasa Indonesia,
dengan contoh kalimat dalam Bahasa Jepang.

## Struktur

```
minna-no-nihongo-i/
├── README.md              <- file ini (indeks)
├── lessons/               <- catatan per pelajaran (課 / ka)
│   ├── lesson-02.md       <- 第2課: kata tunjuk & partikel の
│   ├── lesson-03.md       <- 第3課: kata tunjuk tempat, asal & harga
│   ├── lesson-04.md       <- 第4課: waktu, hari, から/まで, に & kata kerja
│   ├── lesson-05.md       <- 第5課: gerak ke tempat (へ), で, と, に
│   ├── lesson-06.md       <- 第6課: objek (を), tempat で, ajakan ませんか/ましょう
│   ├── lesson-07.md       <- 第7課: alat/bahasa で, memberi/menerima に, もう
│   ├── lesson-08.md       <- 第8課: kata sifat な & い (deskriptif, negatif, + benda)
│   ├── lesson-09.md       <- 第9課: が (suka/pandai/paham/punya), あります/います, から (karena)
│   └── lesson-10.md       <- 第10課: keberadaan に + あります/います, kata posisi
├── reference/
│   ├── particles.md       <- ringkasan partikel
│   ├── vocabulary.md      <- kosakata terkumpul (per lesson)
│   ├── n5-vocabulary.md   <- pool kosakata JLPT N5 (sumber soal /quiz)
│   └── quiz-taxonomy.md   <- daftar tag pola & partikel untuk /quiz
├── progress/              <- data latihan (diperbarui otomatis oleh /quiz)
│   ├── evaluation.md      <- tracker kelemahan per pola/partikel/lesson
│   └── history.md         <- riwayat sesi latihan
└── .claude/skills/quiz/   <- skill /quiz (latihan adaptif)
    └── SKILL.md
```

## Daftar Pelajaran

| Pelajaran | Judul | Topik utama | Status |
|-----------|-------|-------------|--------|
| [第2課 (Lesson 2)](lessons/lesson-02.md) | Kata tunjuk & kepemilikan | これ/それ/あれ, この/その/あの, partikel の | 練習A ✅ |
| [第3課 (Lesson 3)](lessons/lesson-03.md) | Tempat, asal & harga | ここ/そこ/あそこ, こちら系, どこ/どちら, いくら | 練習A ✅ |
| [第4課 (Lesson 4)](lessons/lesson-04.md) | Waktu, hari & kata kerja | じ/ふん, ようび, から/まで, に, ます-form | 練習A ✅ |
| [第5課 (Lesson 5)](lessons/lesson-05.md) | Pergi ke tempat | へ, いきます/きます/かえります, で, と, に | 練習A ✅ |
| [第6課 (Lesson 6)](lessons/lesson-06.md) | Aktivitas & ajakan | を, します, で (tempat), に (あいます), ませんか/ましょう | 練習A ✅ |
| [第7課 (Lesson 7)](lessons/lesson-07.md) | Alat, bahasa & memberi/menerima | で (alat/bahasa), に (あげます/もらいます), もう | 練習A ✅ |
| [第8課 (Lesson 8)](lessons/lesson-08.md) | Kata sifat | な-adj, い-adj, negatif, どう/どんな | 練習A ✅ |
| [第9課 (Lesson 9)](lessons/lesson-09.md) | Suka, bisa, punya & sebab | が, すき/じょうず/わかります, あります/います, から | 練習A ✅ |
| [第10課 (Lesson 10)](lessons/lesson-10.md) | Keberadaan & posisi | に (tempat), あります/います, うえ/した/となり/あいだ | 練習A ✅ |

## Latihan adaptif (`/quiz`)

Skill `/quiz` membuat soal gaya **JLPT N5** dari catatan lesson (source of truth)
dengan kosakata dari pool N5, menilai jawabanmu, lalu memperbarui
`progress/evaluation.md` untuk melacak materi yang lemah dan **memperbanyak soal
pada materi itu** di sesi berikutnya.

| Perintah | Aksi |
|----------|------|
| `/quiz` | Sesi adaptif hemat, 10 soal (baca materi lemah + bab terbaru saja) |
| `/quiz lesson 9-10` | Batasi cakupan ke Lesson 9–10 |
| `/quiz review` | Fokus hanya ke weak areas |
| `/quiz lesson 8 5` | 5 soal, hanya Lesson 8 |

Hasil & analisis (akurasi per pola/partikel/lesson) tersimpan di folder
`progress/` — bisa dibaca rapi di Obsidian.

## Cara pakai sebagai Claude Project

1. Unggah folder ini (atau file `.md` di dalamnya) sebagai *Project knowledge*.
2. Tanyakan hal seperti:
   - "Jelaskan perbedaan これ dan この"
   - "Buatkan latihan soal dari pola kalimat di Lesson 2"
   - "Koreksi kalimat Jepang saya berdasarkan catatan ini"

## Konvensi penulisan

- **Kanji/Hiragana** ditulis apa adanya sesuai buku.
- Setiap pola kalimat diberi **rumus**, **contoh**, dan **catatan**.
- `→` menandai keterangan/hasil dari sebuah kalimat.
