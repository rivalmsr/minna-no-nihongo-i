# Evaluasi Latihan — Tracker Kelemahan

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-24 · total sesi: 12_

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
| L14-te-konjugasi | 7 | 9 | 78% | 🟡 |
| L14-てください | 1 | 2 | 50% | ⚪ |
| L14-ています-progresif | 0 | 1 | 0% | ⚪ |
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
| Lesson 14 | 7 | 9 | 78% | 🟡 |
| Lesson 16 | 2 | 2 | 100% | ⚪ |
| Lesson 17 | 9 | 10 | 90% | 🟢 |
| Lesson 18 | 14 | 16 | 88% | 🟢 |
| Lesson 19 | 46 | 52 | 88% | 🟢 |

---

## Weak areas (prioritas soal berikutnya)
_Tidak ada 🔴. Sesi 2026-08-24 (sesi 12, `lesson 14, 19`) skor **10/12 (83%)**. **L14-te
NAIK 67%→78% 🟡** — tinggal **2%** ke 🟢! ります/います/します 音便 semua benar. 2 error SATU
AKAR: 音便 **き/ぎ** (`かきます→かいて` bukan `かきて`; `およぎます` た形 `およいだ` bukan `およいで`).
い-form dikenali, tapi (a) aturan **き→いて** untuk かきます belum otomatis & (b) **て vs た** pada
ぎ masih goyah._
1. 🟡 **L14-te-konjugasi** — 78% (7/9). NAIK dari 67%; **hampir 🟢**. Sisa error khusus 音便
   **き→いて** (かきます→かいて, bukan tempel て langsung ala grup II). Butuh 1–2 soal き/ぎ-verb
   benar untuk tembus 🟢.
2. ⚪ **L14-ています-progresif** — 0% (0/1, data tipis). Error `かきて` di sini; sama akar き→いて.
   Pantau; belum cukup data untuk vonis.

**Sinyal yang perlu diperhatikan:**
- ⚠️ **音便 き/ぎ→いて/いだ belum otomatis.** Dua error sesi 12 keduanya di sini: `かきます→かいて`
  (dipilih `かきて`) & `およぎます`→ た `およいだ` (dipilih て `およいで`). Bandingkan: ります/います/
  します-音便 sudah mantap (`だして`,`とって`,`けして` semua benar). **Fokus drill: verb akhiran
  き & ぎ** (かきます, ききます, およぎます, いそぎます) + tegaskan て vs た.
- ✅ **て ↔ た umumnya DIKUASAI** — `いった`(例外), `きいたり`, `く なります` benar. `L19-た` 🟢
  (93%), `たことがあります` 🟢 (91%), `たり` 🟢 (92%). Slip hanya pada ぎ-verb (音便 + て/た).
- ✅ **辞書形 & ない-stem DIKUASAI.** Partikel `に` 🟢 (81%), `へ` benar (たことがあります).
- **Rekomendasi:** 1 sesi pendek fokus verb き/ぎ (`/quiz verbs lesson 14`) kemungkinan besar
  menuntaskan L14-te ke 🟢. Setelah itu pertimbangkan bab baru (L20+) atau `/jlpt` mock.
