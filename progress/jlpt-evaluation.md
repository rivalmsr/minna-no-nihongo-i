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

_Terakhir diperbarui: 2026-08-29 · total sesi: 9_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 17 | 18 | 94% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 17 | 18 | 94% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 15 | 18 | 83% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 18 | 18 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 21 | 25 | 84% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 9 | 11 | 82% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 17 | 18 | 94% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 16 | 18 | 89% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
🎉 DK-narabekae 78%🟡→82%🟢: dua susun kalimat benar (stem+に行きます & て-rangkaian) menutup satu-satunya subtipe 🟡. Kini SELURUH 8 subtipe 🟢 (83–100%). Tak ada 🔴/🟡 tersisa. Titik terlemah tinggal MG-bunmyaku 83% (15/18) — turun tipis dari soal 6 (だす vs かく, sinyal discourse-order/kosakata konteks 🔴), disusul DK-bunpou 84% & DK-joho 89%; semua sudah aman. Rekomendasi: JLPT tertulis N5 matang penuh — pantau saja lewat mock berkala; fokus energi ke pola /quiz yang masih 🟡 (evaluation.md).
