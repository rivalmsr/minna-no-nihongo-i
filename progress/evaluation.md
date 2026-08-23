# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-23 · total sesi: 11_

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
| L14-te-konjugasi | 2 | 3 | 67% | 🟡 |
| L14-てください | 0 | 1 | 0% | ⚪ |
| L16-てから | 2 | 2 | 100% | ⚪ |
| L17-ない-konjugasi | 8 | 9 | 89% | 🟢 |
| L17-なければなりません | 3 | 3 | 100% | 🟢 |
| L17-なくてもいいです | 4 | 5 | 80% | 🟢 |
| L17-ないでください | 1 | 1 | 100% | ⚪ |
| L18-ことができます | 8 | 9 | 89% | 🟢 |
| L18-まえに | 5 | 6 | 83% | 🟢 |
| L18-辞書形-konjugasi | 9 | 11 | 82% | 🟢 |
| L19-たことがあります | 9 | 10 | 90% | 🟢 |
| L19-た-konjugasi | 11 | 12 | 92% | 🟢 |
| L19-なります | 18 | 21 | 86% | 🟢 |
| L19-たり | 10 | 11 | 91% | 🟢 |
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

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 26 | 30 | 87% | 🟢 |
| Lesson 13 | 1 | 1 | 100% | ⚪ |
| Lesson 14 | 1 | 2 | 50% | ⚪ |
| Lesson 16 | 2 | 2 | 100% | ⚪ |
| Lesson 17 | 9 | 10 | 90% | 🟢 |
| Lesson 18 | 14 | 16 | 88% | 🟢 |
| Lesson 19 | 43 | 48 | 90% | 🟢 |

---

## Weak areas (prioritas soal berikutnya)
_Tidak ada 🔴. Sesi 2026-08-23 (sesi 11, `lesson 19`) skor **12/12 (100%)** — PERFECT.
**て ↔ た SEKARANG DIKUASAI:** semua 8 soal た-form benar termasuk `のぼった` (kemarin salah
`のぼって`), `いった` (例外), `およいだ`, `のんだ`. `L19-た-konjugasi` naik 🟡→🟢 (92%). Partikel
`に` tembus 🟢 (81%). **Nyaris tak ada weak area tersisa** — hanya L14-te tinggal ekor data lama._
1. 🟡 **L14-te-konjugasi** — 67% (2/3). Satu-satunya 🟡 tersisa; data tipis (ekor error lama
   `まって`). Tak diuji sesi ini. Butuh 1–2 soal て-konjugasi benar untuk tembus 🟢.

**Sinyal yang perlu diperhatikan:**
- ✅ **て ↔ た DIKUASAI** — sesi 11 semua た-form benar (`のんだ`, `かいた`, `いった`, `およいだ`,
  `のぼった`, `そうじした`, susun `たべた`/`見たり`). Error kemarin (`のぼって`) **tidak terulang**.
  `L19-た` 🟢 (92%), `たことがあります` 🟢 (90%), `たり` 🟢 (91%).
- ✅ **辞書形 tetap DIKUASAI** (sesi 10) & **ない-stem DIKUASAI** (sesi 9). Semua 4 bentuk verb
  pokok (て・ない・辞書・た) kini 🟢. Konjugasi 音便 grup I stabil.
- ✅ **Partikel に tembus 🟢** (81%, 21/26) setelah akumulasi `医者に/じょうずに なります`. を juga
  🟢 (かいだんを のぼる).
- `L19-なります` (い→く, N/な→に) 🟢 (86%); のぼる に↔を 🟢 (100%).
- **Fokus berikutnya bukan lagi bentuk verb.** Pertimbangkan: (a) lanjut bab baru (L20+ bila
  dicatat), (b) konsolidasi L14-te lewat `/quiz review`, atau (c) `/jlpt` mock untuk uji terpadu.
- **Sesi 2026-08-23 (sesi 11) skor 12/12 (100%)** — sempurna, tidak ada error.
