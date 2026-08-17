# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-17 · total sesi: 2_

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
| L10-います | 1 | 1 | 100% | ⚪ |
| L10-に-keberadaan | 2 | 3 | 67% | 🟡 |
| L10-posisi | 0 | 1 | 0% | ⚪ |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 2 | 2 | 100% | ⚪ |
| に | 1 | 3 | 33% | 🔴 LEMAH |
| で | 1 | 1 | 100% | ⚪ |
| が | 3 | 3 | 100% | 🟢 |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 9 | 6 | 6 | 100% | 🟢 |
| Lesson 10 | 5 | 7 | 71% | 🟡 |

---

## Weak areas (prioritas soal berikutnya)
1. 🔴 **に (partikel)** — 33% (1/3). Masih tertukar, terutama saat menyusun
   pola keberadaan/posisi. Perkuat **に** (tempat *benda/orang berada*) vs
   **で** (tempat *aktivitas*).
2. 🟡 **L10-に-keberadaan** — 67% (2/3). Pola `[tempat]に[benda]が あります/います`.
3. 🟡 **Lesson 10** — 71% (5/7). Terutama **susun kalimat posisi**
   (`[benda]の[posisi]に …`) — lihat sinyal di bawah.

**Sinyal yang perlu diperhatikan:**
- `L10-posisi` 0/1 (susun kalimat): urutan benar =
  `スーパーの となり に きっさてん が あります` → posisi ★ (ke-3) = **きっさてん**,
  bukan partikel に. Latih urutan `[benda]の[posisi] に [benda] が あります`.
