# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-22 · total sesi: 9_

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
| L14-te-konjugasi | 1 | 2 | 50% | ⚪ |
| L14-てください | 0 | 1 | 0% | ⚪ |
| L16-てから | 1 | 1 | 100% | ⚪ |
| L17-ない-konjugasi | 6 | 7 | 86% | 🟢 |
| L17-なければなりません | 3 | 3 | 100% | 🟢 |
| L17-なくてもいいです | 2 | 3 | 67% | 🟡 |
| L17-ないでください | 1 | 1 | 100% | ⚪ |
| L18-ことができます | 5 | 6 | 83% | 🟢 |
| L18-まえに | 3 | 4 | 75% | 🟡 |
| L18-辞書形-konjugasi | 5 | 7 | 71% | 🟡 |
| L19-たことがあります | 5 | 5 | 100% | 🟢 |
| L19-た-konjugasi | 3 | 3 | 100% | 🟢 |
| L19-なります | 13 | 16 | 81% | 🟢 |
| L19-たり | 6 | 7 | 86% | 🟢 |
| L19-に-vs-を-のぼる | 4 | 4 | 100% | 🟢 |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 2 | 2 | 100% | ⚪ |
| に | 18 | 23 | 78% | 🟡 |
| で | 6 | 6 | 100% | 🟢 |
| を | 2 | 2 | 100% | ⚪ |
| の | 1 | 1 | 100% | ⚪ |
| が | 7 | 7 | 100% | 🟢 |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 26 | 30 | 87% | 🟢 |
| Lesson 13 | 1 | 1 | 100% | ⚪ |
| Lesson 14 | 0 | 1 | 0% | ⚪ |
| Lesson 16 | 1 | 1 | 100% | ⚪ |
| Lesson 17 | 7 | 8 | 88% | 🟢 |
| Lesson 18 | 9 | 11 | 82% | 🟢 |
| Lesson 19 | 29 | 33 | 88% | 🟢 |

---

## Weak areas (prioritas soal berikutnya)
_Tidak ada 🔴. Sesi review "pemilihan bentuk verb" (2026-08-22, sesi 9): **ない-stem
DIKUASAI** (semua pola ない benar), sisa titik lemah menyempit ke **辞書形 vs て**
sebelum `ことができます` / `まえに`._
1. 🟡 **L18-辞書形-konjugasi** — 71% (5/7). Salah `およぎます→` sebelum ことができます:
   pilih **て-form** (`およいで`) padahal butuh **辞書形** (`およぐ`). Bentuk lain
   (くる/みる/かく) benar.
2. 🟡 **L17-なくてもいいです** — 67% (2/3). Sesi ini 2/2 benar (`たべ`, `はらわ`);
   deficit tinggal ekor data lama (`おきる` sesi sebelumnya). Nyaris 🟢.
3. 🟡 **L18-まえに** — 75% (3/4). Sesi ini 2/2 benar (`かく`, `くる`). Nyaris 🟢.
4. 🟡 **に (partikel)** — 78% (18/23). Tak diuji sesi ini; masih menunggu akumulasi
   soal に benar untuk tembus 🟢.

**Sinyal yang perlu diperhatikan:**
- 🔺 **辞書形 vs て — sisa kebingungan (fokus berikutnya):** error sesi 9 = Q4
  `ことができます` pilih て-form (`およいで`) alih-alih 辞書形 (`およぐ`), & Q9
  `てください` pilih ない-form (`またない`) alih-alih て-form (`まって`). Akar: masih
  goyah membedakan **辞書形 ↔ て** dan kapan pola minta て. Ingat: `ことができます`/
  `まえに` = **辞書形**; `てください`/`てから` = **て-form**.
- ✅ **ない-stem DIKUASAI** — sesi 9 semua pola ない benar (`いか`なければ, `たべ`/`はらわ`
  なくても, `とらないで`, `おき`なければ). `L17-ない-konjugasi` naik 🟢 (86%),
  `なければなりません` 🟢 (100%). Kekeliruan `おきる` (sesi 8) tak terulang.
- `L19-なります` (い-adj→く, N/な→に) & `L19-た-konjugasi` (音便 grup I): tetap 🟢.
- `に (partikel)`: hanya perlu akumulasi soal benar; tak ada pola error aktif.
- **Sesi 2026-08-22 (sesi 9) skor 10/12 (83%)** — 2 salah = 辞書形↔て, bukan ない-stem.
