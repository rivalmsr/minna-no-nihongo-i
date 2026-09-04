# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

> ⚙️ **Tabel AUTO-GENERATED oleh `scripts/kb.py`** (`render`/`record`) dari sumber
> `progress/attempts.jsonl` + `baseline.json` (hanya sesi `kind=jlpt`). **Jangan edit angka
> tabel dengan tangan.** Prosa **Weak types** = milik model (`weak_narrative` saat `record`).

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-09-04 · total sesi: 15_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 29 | 30 | 97% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 28 | 30 | 93% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 27 | 30 | 90% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 30 | 30 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 29 | 33 | 88% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 14 | 16 | 88% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 9 | 10 | 90% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 29 | 30 | 97% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 27 | 30 | 90% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
🎉 Tidak ada 🔴 maupun 🟡 — SEMBILAN subtipe JLPT tetap 🟢. Mock 2026-09-04 skor 15/16 (94%), Sesi 2 sempurna 8/8. Satu-satunya miss di MG-hyouki 28/30 (turun tipis 96%→93%): 「みず」ditulis 氷 (こおり/es) padahal 水 (air) — keliru bentuk mirip beda satu coretan, bukan salah konsep. Subtipe lain naik/stabil: MG-ruigi 100% (30/30), MG-yomi & DK-dokkai 97%, MG-bunmyaku & DK-joho & DK-bunshou 90%, DK-bunpou 88%, DK-narabekae naik 87%→88%. ✅ DK-narabekae kali ini diuji BERSIH (potongan diacak にほんへ/くる/まえに/にほんごを, tanpa bocoran urutan/posisi) → まえに benar = sinyal VALID, memperbaiki keraguan mock 2026-09-03. Sinyal: tak ada kelemahan pola/subtipe tersisa; miss 水↔氷 = ketelitian bentuk kanji mirip, bukan pemahaman. Rekomendasi: lanjut mock berkala lawan decay; sesekali sisipkan pasangan kanji mirip (水/氷/永, 木/本/未) di MG-hyouki agar pembedaan coretan makin refleks. Rotasi tema jaga hindari sekolah-rutinitas/jadwal-bus/surat-jalan-jalan di mock berikut.
