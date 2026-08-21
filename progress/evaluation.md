# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-21 · total sesi: 7_

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
| L18-ことができます | 1 | 1 | 100% | ⚪ |
| L18-まえに | 1 | 1 | 100% | ⚪ |
| L18-辞書形-konjugasi | 1 | 1 | 100% | ⚪ |
| L19-たことがあります | 4 | 4 | 100% | 🟢 |
| L19-なります | 11 | 14 | 79% | 🟡 |
| L19-たり | 5 | 6 | 83% | 🟢 |
| L19-に-vs-を-のぼる | 3 | 3 | 100% | 🟢 |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 2 | 2 | 100% | ⚪ |
| に | 15 | 20 | 75% | 🟡 |
| で | 6 | 6 | 100% | 🟢 |
| を | 2 | 2 | 100% | ⚪ |
| の | 1 | 1 | 100% | ⚪ |
| が | 6 | 6 | 100% | 🟢 |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 26 | 30 | 87% | 🟢 |
| Lesson 13 | 1 | 1 | 100% | ⚪ |
| Lesson 18 | 3 | 3 | 100% | 🟢 |
| Lesson 19 | 23 | 27 | 85% | 🟢 |

---

## Weak areas (prioritas soal berikutnya)
_Tidak ada 🔴. Semua lesson & pola sudah 🟢 kecuali dua 🟡 yang tinggal selangkah dari hijau._
1. 🟡 **に (partikel)** — 75% (15/20). Naik dari 71%. Error historis dari `なります`
   い-adj sudah tak muncul; sisa deficit tinggal ekor data lama. Butuh ~beberapa
   soal に benar lagi untuk tembus 🟢.
2. 🟡 **L19-なります** — 79% (11/14). **Nyaris 🟢.** Sesi 2026-08-21: い-adj 3/3
   BENAR (termasuk `いい→よく`) → titik lemah lama tampaknya sudah teratasi. Cukup
   1–2 soal benar lagi untuk hijau.

**Sinyal yang perlu diperhatikan:**
- `L19-なります` — **い-adj → く SUDAH DIKUASAI** (sesi 2026-08-21: `寒く`, `高く`,
  `よく` semua benar). な-adj/N → に juga aman. Tak perlu dibobot berat lagi; cukup
  1–2 soal konfirmasi untuk naikkan ke 🟢.
- `に (partikel)` — hanya perlu akumulasi soal benar; tak ada pola error aktif.
- `に vs で`: **DIKUASAI** — L10-に-keberadaan naik ke 🟢 (80%), sesi ini 2/2 benar.
- **Sesi 2026-08-21 skor 12/12 (100%)** — semua weak area lama membaik; Lesson 19
  & L10-に-keberadaan lulus ke 🟢.
