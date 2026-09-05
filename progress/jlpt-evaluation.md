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

_Terakhir diperbarui: 2026-09-05 · total sesi: 16_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 31 | 32 | 97% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 30 | 32 | 94% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 28 | 32 | 88% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 32 | 32 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 30 | 34 | 88% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 15 | 17 | 88% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 11 | 12 | 92% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 31 | 32 | 97% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 29 | 32 | 91% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
🎉 Tidak ada 🔴 maupun 🟡 — SEMBILAN subtipe JLPT tetap 🟢. Mock 2026-09-05 skor 15/16 (94%), Sesi 2 sempurna 8/8 (DK-bunpou 88%, DK-narabekae 88%, DK-bunshou 92%, DK-dokkai 97%, DK-joho 91% — semua stabil/naik). Satu-satunya miss di MG-bunmyaku (turun tipis 90%→88%, tetap 🟢): 「みちを（　）ください」 dijawab かって (beli) padahal おしえて (menunjukkan/mengajari jalan) — bukan salah pola, tapi kurang menangkap cue 「わからない道を…ください」 yang menuntut おしえる, sementara かう tak logis untuk 'jalan'. Subtipe lain: MG-ruigi 100%, MG-yomi & DK-dokkai 97%, MG-hyouki 94%, DK-joho 91%. Sinyal: tak ada kelemahan pola/subtipe tersisa; miss = kecerobohan makna kolokasi (おしえる vs かう), bukan tata bahasa. Rekomendasi: lanjut mock berkala lawan decay; sesekali sisipkan soal MG-bunmyaku kolokasi verba+objek (道を おしえる, 写真を とる, 電気を つける) agar pasangan kata makin refleks. Rotasi tema jaga hindari keluarga-masak/menu-kafe/buku-harian-belanja di mock berikut.
