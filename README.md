# みんなの日本語 I — Knowledge Base

Basis pengetahuan (knowledge base) untuk belajar bahasa Jepang menggunakan buku
**Minna no Nihongo I (みんなの日本語 I)**. Penjelasan ditulis dalam Bahasa Indonesia,
dengan contoh kalimat dalam Bahasa Jepang.

## Struktur

```
minna-no-nihongo-i/
├── README.md              <- file ini (indeks)
├── CLAUDE.md              <- hub konteks project (ide, aturan /quiz, konvensi)
├── lessons/               <- catatan per pelajaran (課 / ka)
│   ├── lesson-02.md       <- 第2課: kata tunjuk & partikel の
│   ├── lesson-03.md       <- 第3課: kata tunjuk tempat, asal & harga
│   ├── lesson-04.md       <- 第4課: waktu, hari, から/まで, に & kata kerja
│   ├── lesson-05.md       <- 第5課: gerak ke tempat (へ), で, と, に
│   ├── lesson-06.md       <- 第6課: objek (を), tempat で, ajakan ませんか/ましょう
│   ├── lesson-07.md       <- 第7課: alat/bahasa で, memberi/menerima に, もう
│   ├── lesson-08.md       <- 第8課: kata sifat な & い (deskriptif, negatif, + benda)
│   ├── lesson-09.md       <- 第9課: が (suka/pandai/paham/punya), あります/います, から (karena)
│   ├── lesson-10.md       <- 第10課: keberadaan に + あります/います, kata posisi
│   ├── lesson-11.md       <- 第11課: satuan hitung (〜つ/まい/にん/かい), durasi, かかります
│   ├── lesson-12.md       <- 第12課: bentuk lampau, perbandingan より/どちら/いちばん
│   ├── lesson-13.md       <- 第13課: 語彙/動詞 — 〜に行きます, 〜ています, を (meninggalkan)
│   ├── lesson-14.md       <- 第14課: bentuk 〜て — てください, ましょうか, ています
│   ├── lesson-15.md       <- 第15課: てもいいです, てはいけません, ています (keadaan/kebiasaan)
│   ├── lesson-16.md       <- 第16課: 〜て/〜てから (urutan aksi), は〜が, gabung sifat (で/くて)
│   ├── lesson-17.md       <- 第17課: bentuk ない — ないでください, なければなりません, なくてもいいです
│   ├── lesson-18.md       <- 第18課: bentuk kamus (辞書形) — ことができます, しゅみ, まえに
│   └── lesson-19.md       <- 第19課: bentuk た — たことがあります, たり〜たり, なります
├── reference/
│   ├── particles.md       <- ringkasan partikel
│   ├── vocabulary.md      <- kosakata terkumpul (per lesson)
│   ├── n5-vocabulary.md   <- pool kosakata JLPT N5 (sumber soal /quiz & /jlpt)
│   ├── n5-synonyms.md     <- pool sinonim/parafrase N5 (sumber soal sinonim /jlpt)
│   ├── anki-verbs.md      <- pool kata kerja (AUTO-GENERATED dari deck Anki; jangan edit tangan)
│   └── quiz-taxonomy.md   <- tag pola & partikel (/quiz) + tag subtipe JLPT (/jlpt)
├── progress/              <- data latihan (diperbarui otomatis oleh /quiz & /jlpt)
│   ├── evaluation.md      <- tracker kelemahan /quiz (per pola/partikel/lesson)
│   ├── jlpt-evaluation.md <- tracker mock /jlpt (per subtipe ujian JLPT)
│   ├── anki-weak-items.md <- item lemah dari collection Anki (AUTO-GENERATED; lapses+leech)
│   └── history.md         <- riwayat sesi latihan (dibagi /quiz & /jlpt, entri berlabel)
├── docs/
│   ├── cara-kerja.md          <- flow & logika bisnis KB (diagram) — mulai baca dari sini
│   ├── perbaikan-kb.md        <- log perbaikan sistem/aturan (problem→fix→tanggal)
│   └── anki-integration-plan.md <- rencana + status integrasi data Anki
├── scripts/
│   ├── sync-anki-verbs.sh      <- regen anki-verbs.md dari learn-anki/ (folder deck Anki; gitignored)
│   └── sync-anki-weak-items.sh <- regen anki-weak-items.md dari collection.anki2 (Anki desktop)
└── .claude/skills/
    ├── quiz/SKILL.md      <- skill /quiz (latihan harian adaptif)
    ├── jlpt/SKILL.md      <- skill /jlpt (mock ujian tertulis N5, 2 sesi)
    └── sync-anki/SKILL.md <- skill /sync-anki (refresh anki-verbs.md & anki-weak-items.md)
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
| [第11課 (Lesson 11)](lessons/lesson-11.md) | Satuan hitung | 〜つ/いくつ, 〜まい, 〜にん, 〜かい, どのくらい, かかります | 練習A ✅ |
| [第12課 (Lesson 12)](lessons/lesson-12.md) | Lampau & perbandingan | でした/くなかった, より, どちら〜のほうが, いちばん | 練習A ✅ |
| [第13課 (Lesson 13)](lessons/lesson-13.md) | 語彙 — kata kerja | 〜に行きます, 〜ています, 食事/食べます, を (meninggalkan) | 語彙/動詞 ✅ · 形容詞 ⬜ |
| [第14課 (Lesson 14)](lessons/lesson-14.md) | Bentuk 〜て | konjugasi て, 〜てください, 〜ましょうか, 〜ています | 練習A ✅ |
| [第15課 (Lesson 15)](lessons/lesson-15.md) | Izin, larangan & keadaan | 〜てもいいです, 〜てはいけません, 〜ています (しって/すんで) | 言葉 ✅ · 練習A ✅ |
| [第16課 (Lesson 16)](lessons/lesson-16.md) | Urutan aksi & gabung sifat | 〜て/〜てから, は〜が, な で・い くて, 他動詞/自動詞 | 言葉 ✅ · 練習A ✅ |
| [第17課 (Lesson 17)](lessons/lesson-17.md) | Bentuk ない | 〜ないでください, 〜なければなりません, 〜なくてもいいです, を→は | 練習A ✅ |
| [第18課 (Lesson 18)](lessons/lesson-18.md) | Bentuk kamus (辞書形) | 〜ことができます, N が できます, しゅみ, 〜まえに | 練習A ✅ |
| [第19課 (Lesson 19)](lessons/lesson-19.md) | Bentuk た | 〜たことがあります, 〜たり〜たりします, 〜なります | 言葉 ✅ · 練習A ✅ |

## Latihan adaptif (`/quiz`)

Skill `/quiz` membuat soal gaya **JLPT N5** dari catatan lesson (source of truth)
dengan kosakata dari pool N5, menilai jawabanmu, lalu memperbarui
`progress/evaluation.md` untuk melacak materi yang lemah dan **memperbanyak soal
pada materi itu** di sesi berikutnya.

| Perintah | Aksi |
|----------|------|
| `/quiz` | Sesi adaptif hemat, 12 soal (baca materi lemah + bab terbaru saja) |
| `/quiz lesson 9-10` | Batasi cakupan ke Lesson 9–10 |
| `/quiz review` | Fokus hanya ke weak areas |
| `/quiz lesson 8 5` | 5 soal, hanya Lesson 8 |

Hasil & analisis (akurasi per pola/partikel/lesson) tersimpan di folder
`progress/` — bisa dibaca rapi di Obsidian.

## Mock ujian tertulis (`/jlpt`)

Skill `/jlpt` mensimulasikan **ujian tertulis JLPT N5 penuh** dengan **2 sesi** seperti
ujian asli — `聴解` (listening) di luar cakupan karena butuh audio:

- **Sesi 1 · 文字・語彙** — baca kanji (cara baca), tulis kanji (penulisan), kosakata
  dalam konteks, sinonim/言い換え類義.
- **Sesi 2 · 文法・読解** — tata bahasa, susun kalimat (★), bacaan pendek, bacaan
  informasi (info-search).

Hasil dilacak **terpisah per subtipe** di `progress/jlpt-evaluation.md` (tracker
grammar `/quiz` tak terganggu).

| Perintah | Aksi |
|----------|------|
| `/jlpt` | Mock penuh 2 sesi, 16 soal (8 文字・語彙 + 8 文法・読解) |
| `/jlpt moji` | Hanya Sesi 1 文字・語彙 (12 soal) |
| `/jlpt bunpou` | Hanya Sesi 2 文法・読解 (12 soal) |
| `/jlpt review` | Fokus ke subtipe yang lemah |

> `/quiz` = latihan **harian adaptif** grammar · `/jlpt` = **simulasi ujian** meniru
> struktur JLPT. Keduanya pakai referensi & konvensi yang sama.

## Refresh data Anki (`/sync-anki`)

Skill `/sync-anki` me-regenerasi file turunan Anki yang jadi bahan `/quiz` & `/jlpt`,
lalu memberi notifikasi (`✅ Sukses updated` / `ℹ️ No data updated`).

| Perintah | Aksi |
|----------|------|
| `/sync-anki` | Refresh **keduanya** — `anki-verbs.md` + `anki-weak-items.md` |
| `/sync-anki weak` | Hanya `progress/anki-weak-items.md` (item lemah) |
| `/sync-anki verbs` | Hanya `reference/anki-verbs.md` (pool kata kerja) |

> ⚠️ Untuk weak-items: **buka Anki desktop & Sync dulu** kalau baru review di iPhone —
> sync iPhone saja tak update `collection.anki2` lokal.

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
