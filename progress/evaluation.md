# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-20 · total sesi: 6_

---

## Per pola kalimat
| Tag | Benar | Total | Akurasi | Status |
|-----|-------|-------|---------|--------|
| L9-から-sebab | 2 | 2 | 100% | ⚪ |
| L9-が-suka | 1 | 1 | 100% | ⚪ |
| L9-が-paham | 1 | 1 | 100% | ⚪ |
| L9-が-pandai | 1 | 1 | 100% | ⚪ |
| L9-punya | 1 | 1 | 100% | ⚪ |
| L10-あります | 4 | 4 | 100% | 🟢 |
| L10-います | 2 | 2 | 100% | ⚪ |
| L10-に-keberadaan | 10 | 13 | 77% | 🟡 |
| L10-posisi | 6 | 7 | 86% | 🟢 |
| L13-に-tujuan | 1 | 1 | 100% | ⚪ |
| L18-ことができます | 1 | 1 | 100% | ⚪ |
| L18-まえに | 1 | 1 | 100% | ⚪ |
| L18-辞書形-konjugasi | 1 | 1 | 100% | ⚪ |
| L19-たことがあります | 3 | 3 | 100% | 🟢 |
| L19-なります | 6 | 9 | 67% | 🟡 |
| L19-たり | 4 | 5 | 80% | 🟢 |
| L19-に-vs-を-のぼる | 2 | 2 | 100% | ⚪ |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 2 | 2 | 100% | ⚪ |
| に | 12 | 17 | 71% | 🟡 |
| で | 5 | 5 | 100% | 🟢 |
| を | 1 | 1 | 100% | ⚪ |
| の | 1 | 1 | 100% | ⚪ |
| が | 6 | 6 | 100% | 🟢 |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 22 | 26 | 85% | 🟢 |
| Lesson 13 | 1 | 1 | 100% | ⚪ |
| Lesson 18 | 3 | 3 | 100% | 🟢 |
| Lesson 19 | 15 | 19 | 79% | 🟡 |

---

## Weak areas (prioritas soal berikutnya)
_Tidak ada 🔴. Sisa 🟡 makin sedikit — に↔で & posisi & たり sudah membaik ke 🟢/aman._
1. 🟡 **L19-なります** — 67% (6/9). **Titik gagal spesifik: い-adjektiva** (`暑い →
   暑く なります`). な-adj/N (→ に) sudah konsisten benar; yang meleset selalu **い-adj**
   yang salah pakai に. Kuatkan HANYA kasus い-adj → く.
2. 🟡 **に (partikel)** — 71% (12/17). Naik dari 62%. Sisa error ikut dari `なります`
   い-adj (salah に) — bukan lagi dari に↔で keberadaan (sesi ini 4/4 benar).
3. 🟡 **L10-に-keberadaan** — 77% (10/13). Membaik pesat; に↔で sudah dikuasai.
4. 🟡 **Lesson 19** — 79% (15/19). Ditahan hanya oleh なります い-adj.

**Sinyal yang perlu diperhatikan:**
- `L19-なります` (PRIORITAS TUNGGAL): **い-adj → buang い + く** (`暑く なります`,
  `寒く なります`, `安く なります`); **な-adj/N → に** (`上手に`, `二十歳に`). Pola
  error yang konsisten: user pakai **に untuk semua** → salah di い-adj. Perbanyak
  soal い-adj + なります.
- `に vs で`: **SUDAH MEMBAIK** (sesi 2026-08-20 review: 4/4). に = keberadaan
  (あります/います), で = aktivitas. Pantau sesekali saja.
- `L19-たり`: rendaku sudah benar (`読む→読んだり`, `遊ぶ→遊んだり`). Naik ke 🟢.
