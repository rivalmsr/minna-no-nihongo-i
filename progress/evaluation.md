# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-19 · total sesi: 4_

---

## Per pola kalimat
| Tag | Benar | Total | Akurasi | Status |
|-----|-------|-------|---------|--------|
| L9-から-sebab | 2 | 2 | 100% | ⚪ |
| L9-が-suka | 1 | 1 | 100% | ⚪ |
| L9-が-paham | 1 | 1 | 100% | ⚪ |
| L9-が-pandai | 1 | 1 | 100% | ⚪ |
| L9-punya | 1 | 1 | 100% | ⚪ |
| L10-あります | 3 | 3 | 100% | 🟢 |
| L10-います | 2 | 2 | 100% | ⚪ |
| L10-に-keberadaan | 5 | 7 | 71% | 🟡 |
| L10-posisi | 2 | 3 | 67% | 🟡 |
| L13-に-tujuan | 1 | 1 | 100% | ⚪ |
| L18-ことができます | 1 | 1 | 100% | ⚪ |
| L18-まえに | 1 | 1 | 100% | ⚪ |
| L18-辞書形-konjugasi | 1 | 1 | 100% | ⚪ |
| L19-たことがあります | 2 | 2 | 100% | ⚪ |
| L19-なります | 1 | 3 | 33% | 🔴 LEMAH |
| L19-たり | 1 | 2 | 50% | ⚪ |
| L19-に-vs-を-のぼる | 1 | 1 | 100% | ⚪ |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 2 | 2 | 100% | ⚪ |
| に | 6 | 10 | 60% | 🟡 |
| で | 2 | 2 | 100% | ⚪ |
| が | 6 | 6 | 100% | 🟢 |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 12 | 15 | 80% | 🟢 |
| Lesson 13 | 1 | 1 | 100% | ⚪ |
| Lesson 18 | 3 | 3 | 100% | 🟢 |
| Lesson 19 | 5 | 8 | 63% | 🟡 |

---

## Weak areas (prioritas soal berikutnya)
1. 🔴 **L19-なります** — 33% (1/3). Titik kegagalan jelas: **い-adjektiva** (`さむい
   → さむく なります`) tertukar jadi `さむいに`. Kuatkan aturan: **N/な-adj + に**,
   tapi **い-adj → buang い + く**.
2. 🟡 **に (partikel)** — 60% (6/10). Naik pesat dari 40%! Sisa keplesetnya: **に
   (keberadaan) vs で (aktivitas)** — masih sesekali tertukar.
3. 🟡 **Lesson 19** — 63% (5/8). Ditarik turun oleh なります + たり (rendaku).
4. 🟡 **L10-posisi** — 67% (2/3). Sesi ini benar; masih pantau.
5. 🟡 **L10-に-keberadaan** — 71% (5/7). Q3 salah pilih で.

**Sinyal yang perlu diperhatikan:**
- `L19-なります` 1/3: **い-adj → く** (`さむく なります`), **N/な-adj → に**
  (`大学生に なります`). Jangan `〜いに`, jangan が.
- `L19-たり` 1/2: **rendaku** bentuk た/たり — verba akhiran ん/ぐ/ぶ/む → **だ/だり**
  (`読む → 読んだり`, bukan 読んたり).
- `に vs で`: **に** = tempat **keberadaan** (あります/います); **で** = tempat
  **aktivitas**. Q3 (`こうえんに 子供が います`) salah pilih で.
