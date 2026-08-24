# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-24 · total sesi: 13_

---

## Per pola kalimat
| Tag | Benar | Total | Akurasi | Status |
|-----|-------|-------|---------|--------|
| L9-から-sebab | 2 | 2 | 100% | ⚪ |
| L9-が-suka | 1 | 1 | 100% | ⚪ |
| L9-が-paham | 1 | 1 | 100% | ⚪ |
| L9-が-pandai | 1 | 1 | 100% | ⚪ |
| L9-punya | 1 | 1 | 100% | ⚪ |
| L10-あります | 5 | 5 | 100% | 🟢 |
| L10-います | 2 | 2 | 100% | ⚪ |
| L10-に-keberadaan | 12 | 15 | 80% | 🟢 |
| L10-posisi | 7 | 8 | 88% | 🟢 |
| L13-に-tujuan | 1 | 1 | 100% | ⚪ |
| L14-te-konjugasi | 19 | 21 | 90% | 🟢 |
| L14-てください | 4 | 5 | 80% | 🟢 |
| L14-ています-progresif | 2 | 3 | 67% | 🟡 |
| L14-ましょうか | 1 | 1 | 100% | ⚪ |
| L16-てから | 2 | 2 | 100% | ⚪ |
| L17-ない-konjugasi | 8 | 9 | 89% | 🟢 |
| L17-なければなりません | 3 | 3 | 100% | 🟢 |
| L17-なくてもいいです | 4 | 5 | 80% | 🟢 |
| L17-ないでください | 1 | 1 | 100% | ⚪ |
| L18-ことができます | 8 | 9 | 89% | 🟢 |
| L18-まえに | 5 | 6 | 83% | 🟢 |
| L18-辞書形-konjugasi | 9 | 11 | 82% | 🟢 |
| L19-たことがあります | 10 | 11 | 91% | 🟢 |
| L19-た-konjugasi | 14 | 15 | 93% | 🟢 |
| L19-なります | 19 | 22 | 86% | 🟢 |
| L19-たり | 11 | 12 | 92% | 🟢 |
| L19-に-vs-を-のぼる | 5 | 5 | 100% | 🟢 |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 2 | 2 | 100% | ⚪ |
| に | 21 | 26 | 81% | 🟢 |
| で | 6 | 6 | 100% | 🟢 |
| を | 3 | 3 | 100% | 🟢 |
| の | 1 | 1 | 100% | ⚪ |
| が | 7 | 7 | 100% | 🟢 |
| へ | 1 | 1 | 100% | ⚪ |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 26 | 30 | 87% | 🟢 |
| Lesson 13 | 1 | 1 | 100% | ⚪ |
| Lesson 14 | 19 | 21 | 90% | 🟢 |
| Lesson 16 | 2 | 2 | 100% | ⚪ |
| Lesson 17 | 9 | 10 | 90% | 🟢 |
| Lesson 18 | 14 | 16 | 88% | 🟢 |
| Lesson 19 | 46 | 52 | 88% | 🟢 |

---

## Weak areas (prioritas soal berikutnya)
_Tidak ada 🔴. Sesi 2026-08-24 (sesi 13, `verbs lesson 14`) skor **12/12 (100%)** — PERFECT.
**音便 き→いて / ぎ→いで TUNTAS:** semua 12 benar & tak tertipu distraktor (ひいて, おいて,
およいで, いそいで, ぬいで), tetap **び→んで** (よんで, tak over-generalize), grup II tempel
(つけて), し→して (だして). **L14-te-konjugasi 78%→90% 🟢** & **Lesson 14 → 🟢**. Semua bentuk
verb pokok (て・ない・辞書・た) kini 🟢. **Praktis tak ada weak area tersisa.**_
1. 🟡 **L14-ています-progresif** — 67% (2/3). Satu-satunya 🟡 tersisa; data tipis (1 error lama
   `かきて`, kini 2 benar berturut `ひいて`/`およいで`). Akar き→いて sudah beres; butuh 1 attempt
   lagi untuk tembus 🟢. Bukan prioritas mendesak.

**Sinyal yang perlu diperhatikan:**
- ✅ **音便 grup I DIKUASAI PENUH** — き→いて (ひいて/おいて), ぎ→いで (およいで/いそいで/ぬいで),
  び→んで (よんで), し→して (だして), り/い/ち→って semua stabil. Tidak over-generalize いて/いで.
- ✅ **4 bentuk verb pokok (て・ない・辞書・た) semua 🟢.** `L19-た` 🟢 (93%), `辞書形` 🟢 (82%),
  `ない` 🟢 (89%), `て` 🟢 (90%). Konjugasi bukan lagi titik lemah.
- ✅ **Partikel に 🟢 (81%), へ benar. Pola L18/L19 semua 🟢.**
- **Rekomendasi (fokus geser dari konjugasi):** materi grammar N5 Minna I sudah terkonsolidasi.
  Pertimbangkan: (a) **bab baru L20+** bila dicatat (butuh materi dari user), atau (b) **`/jlpt`
  mock** untuk uji terpadu tertulis (文字語彙 + 文法読解). `/quiz review` sudah kurang perlu —
  tak ada 🔴 & cuma 1 🟡 tipis.
