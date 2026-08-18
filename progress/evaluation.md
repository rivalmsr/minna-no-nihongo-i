# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-18 · total sesi: 3_

---

## Per pola kalimat
| Tag | Benar | Total | Akurasi | Status |
|-----|-------|-------|---------|--------|
| L9-から-sebab | 2 | 2 | 100% | ⚪ |
| L9-が-suka | 1 | 1 | 100% | ⚪ |
| L9-が-paham | 1 | 1 | 100% | ⚪ |
| L9-が-pandai | 1 | 1 | 100% | ⚪ |
| L9-punya | 1 | 1 | 100% | ⚪ |
| L10-あります | 2 | 2 | 100% | ⚪ |
| L10-います | 2 | 2 | 100% | ⚪ |
| L10-に-keberadaan | 4 | 5 | 80% | 🟢 |
| L10-posisi | 1 | 2 | 50% | ⚪ |
| L18-ことができます | 1 | 1 | 100% | ⚪ |
| L18-まえに | 1 | 1 | 100% | ⚪ |
| L18-辞書形-konjugasi | 1 | 1 | 100% | ⚪ |
| L19-たことがあります | 1 | 1 | 100% | ⚪ |
| L19-なります | 0 | 1 | 0% | ⚪ |
| L19-たり | 1 | 1 | 100% | ⚪ |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 2 | 2 | 100% | ⚪ |
| に | 2 | 5 | 40% | 🔴 LEMAH |
| で | 2 | 2 | 100% | ⚪ |
| が | 5 | 5 | 100% | 🟢 |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 9 | 11 | 82% | 🟢 |
| Lesson 18 | 3 | 3 | 100% | 🟢 |
| Lesson 19 | 2 | 3 | 67% | 🟡 |

---

## Weak areas (prioritas soal berikutnya)
1. 🔴 **に (partikel)** — 40% (2/5). Membaik dari 33%, tapi masih lemah. Titik
   kegagalan bergeser: sekarang **に + なります** (`N に なります`) yang tertukar
   dengan が. Kuatkan に sebagai penanda **hasil perubahan** & **tujuan**, bukan subjek.
2. 🟡 **Lesson 19** — 67% (2/3). Gara-gara **なります** (lihat sinyal).

**Sinyal yang perlu diperhatikan:**
- `L19-なります` 0/1: `大学生（だいがくせい）に なります` — N/な-adj pakai **に**,
  い-adj → **く** (`おおきく なります`). Bukan が.
- `L10-posisi` 1/2 (⚪, belum cukup data): pola susun `[benda]の[posisi]に …` —
  sesi ini benar (`銀行の となりに`), pantau lagi untuk konfirmasi.
- **Kemajuan:** に-keberadaan vs で-aktivitas kini 🟢 (Q1 & Q4 benar).
