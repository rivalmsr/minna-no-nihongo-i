# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-17 · total sesi: 1_

---

## Per pola kalimat
| Tag | Benar | Total | Akurasi | Status |
|-----|-------|-------|---------|--------|
| L9-から-sebab | 1 | 1 | 100% | ⚪ |
| L10-あります | 1 | 1 | 100% | ⚪ |
| L10-に-keberadaan | 0 | 1 | 0% | ⚪ |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 1 | 1 | 100% | ⚪ |
| に | 0 | 1 | 0% | ⚪ |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 1 | 1 | 100% | ⚪ |
| Lesson 10 | 1 | 2 | 50% | ⚪ |

---

## Weak areas (prioritas soal berikutnya)
_Belum cukup data untuk status resmi (butuh ≥3 attempt per tag)._

**Sinyal awal yang perlu diperhatikan:**
1. `L10-に-keberadaan` — keliru memilih **で** untuk kalimat keberadaan
   (あそこ**に** ねこが います). Perkuat beda **に** (tempat keberadaan) vs
   **で** (tempat aktivitas).
