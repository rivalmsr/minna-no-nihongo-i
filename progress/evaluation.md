# Evaluasi Latihan — Tracker Kelemahan

> ⚙️ **Tabel AUTO-GENERATED oleh `scripts/kb.py`** (`render`/`record`) dari sumber
> `progress/attempts.jsonl` + `baseline.json`. **Jangan edit angka tabel dengan tangan**
> (tertimpa saat render). Prosa **Weak areas** = milik model, disuplai lewat
> `weak_narrative` saat `kb.py record`. Detail: `docs/engine-bookkeeping-plan.md`.

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-09-10 · total sesi: 35_

---

## Per pola kalimat
| Tag | Benar | Total | Akurasi | Status |
|-----|-------|-------|---------|--------|
| L4-jam | 7 | 8 | 88% | 🟢 |
| L5-で-transport | 3 | 3 | 100% | 🟢 |
| L6-を-objek | 2 | 2 | 100% | ⚪ |
| L7-に-memberi | 7 | 8 | 88% | 🟢 |
| L7-に-menerima | 9 | 10 | 90% | 🟢 |
| L7-で-alat | 3 | 3 | 100% | 🟢 |
| L7-で-bahasa | 4 | 5 | 80% | 🟢 |
| L7-もう | 3 | 3 | 100% | 🟢 |
| L8-adj-negatif | 2 | 2 | 100% | ⚪ |
| L8-adj-benda | 2 | 2 | 100% | ⚪ |
| L8-どう-どんな | 3 | 3 | 100% | 🟢 |
| L9-から-sebab | 3 | 3 | 100% | 🟢 |
| L9-が-suka | 2 | 2 | 100% | ⚪ |
| L9-が-paham | 2 | 2 | 100% | ⚪ |
| L9-が-pandai | 1 | 1 | 100% | ⚪ |
| L9-punya | 2 | 2 | 100% | ⚪ |
| L10-あります | 6 | 6 | 100% | 🟢 |
| L10-います | 3 | 3 | 100% | 🟢 |
| L10-に-keberadaan | 13 | 16 | 81% | 🟢 |
| L10-posisi | 8 | 9 | 89% | 🟢 |
| L11-まい | 2 | 2 | 100% | ⚪ |
| L11-かい-frekuensi | 2 | 2 | 100% | ⚪ |
| L11-かかります | 2 | 2 | 100% | ⚪ |
| L12-より | 2 | 2 | 100% | ⚪ |
| L12-のほうが | 2 | 2 | 100% | ⚪ |
| L12-lampau-positif | 2 | 2 | 100% | ⚪ |
| L13-に-tujuan | 11 | 13 | 85% | 🟢 |
| L13-を-meninggalkan | 8 | 8 | 100% | 🟢 |
| L13-で-vs-を | 8 | 10 | 80% | 🟢 |
| L13-ています-keadaan | 12 | 15 | 80% | 🟢 |
| L14-te-konjugasi | 36 | 38 | 95% | 🟢 |
| L14-てください | 6 | 7 | 86% | 🟢 |
| L14-ています-progresif | 5 | 6 | 83% | 🟢 |
| L14-ましょうか | 1 | 1 | 100% | ⚪ |
| L15-てもいいです | 3 | 3 | 100% | 🟢 |
| L15-てはいけません | 4 | 5 | 80% | 🟢 |
| L15-ています-keadaan | 8 | 9 | 89% | 🟢 |
| L15-に-vs-で-statis | 9 | 11 | 82% | 🟢 |
| L16-てから | 9 | 10 | 90% | 🟢 |
| L16-て-urutan | 1 | 1 | 100% | ⚪ |
| L16-他動詞-自動詞 | 6 | 7 | 86% | 🟢 |
| L16-に-naik | 11 | 13 | 85% | 🟢 |
| L17-ない-konjugasi | 15 | 16 | 94% | 🟢 |
| L17-なければなりません | 6 | 7 | 86% | 🟢 |
| L17-なくてもいいです | 5 | 6 | 83% | 🟢 |
| L17-ないでください | 3 | 3 | 100% | 🟢 |
| L18-ことができます | 9 | 10 | 90% | 🟢 |
| L18-まえに | 11 | 12 | 92% | 🟢 |
| L18-辞書形-konjugasi | 14 | 16 | 88% | 🟢 |
| L19-たことがあります | 16 | 17 | 94% | 🟢 |
| L19-た-konjugasi | 23 | 24 | 96% | 🟢 |
| L19-なります | 24 | 29 | 83% | 🟢 |
| L19-たり | 16 | 17 | 94% | 🟢 |
| L19-に-vs-を-のぼる | 6 | 6 | 100% | 🟢 |
| L5-と-dengan | 2 | 2 | 100% | ⚪ |
| L5-どこも | 1 | 1 | 100% | ⚪ |
| L6-で-tempat | 1 | 1 | 100% | ⚪ |
| L6-ませんか | 1 | 1 | 100% | ⚪ |
| L6-に-bertemu | 1 | 1 | 100% | ⚪ |
| L4-から-まで | 2 | 2 | 100% | ⚪ |
| L4-kata-kerja | 1 | 1 | 100% | ⚪ |
| L4-に-waktu | 2 | 2 | 100% | ⚪ |
| L5-へ-tujuan | 2 | 2 | 100% | ⚪ |
| L2-の-jenis | 1 | 1 | 100% | ⚪ |
| L2-この-benda | 1 | 1 | 100% | ⚪ |
| L2-なん | 1 | 1 | 100% | ⚪ |
| L2-の-milik | 1 | 1 | 100% | ⚪ |
| L3-どこ | 1 | 1 | 100% | ⚪ |
| L3-いくら | 1 | 1 | 100% | ⚪ |
| L3-どこの-asal | 1 | 1 | 100% | ⚪ |
| L3-ここ-tempat | 1 | 1 | 100% | ⚪ |
| L11-が-vs-を | 1 | 1 | 100% | ⚪ |
| L20-普通形-動詞 | 4 | 5 | 80% | 🟢 |
| L20-普通形-い形 | 3 | 3 | 100% | 🟢 |
| L20-普通形-な形-名詞 | 3 | 3 | 100% | 🟢 |
| L20-普通体-会話 | 1 | 1 | 100% | ⚪ |
| L12-lampau-negatif | 1 | 1 | 100% | ⚪ |
| L16-gabung-sifat | 1 | 2 | 50% | ⚪ |
| L21-と思います | 2 | 2 | 100% | ⚪ |
| L21-でしょう | 2 | 2 | 100% | ⚪ |
| L21-と言いました | 1 | 2 | 50% | ⚪ |
| L21-言葉-うごきます | 1 | 1 | 100% | ⚪ |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 6 | 6 | 100% | 🟢 |
| に | 61 | 70 | 87% | 🟢 |
| で | 23 | 27 | 85% | 🟢 |
| を | 28 | 29 | 97% | 🟢 |
| の | 3 | 3 | 100% | 🟢 |
| が | 16 | 16 | 100% | 🟢 |
| へ | 5 | 5 | 100% | 🟢 |
| と | 4 | 4 | 100% | 🟢 |
| より | 1 | 1 | 100% | ⚪ |
| まで | 1 | 1 | 100% | ⚪ |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 4 | 12 | 13 | 92% | 🟢 |
| Lesson 5 | 8 | 8 | 100% | 🟢 |
| Lesson 6 | 5 | 5 | 100% | 🟢 |
| Lesson 7 | 26 | 29 | 90% | 🟢 |
| Lesson 8 | 8 | 8 | 100% | 🟢 |
| Lesson 9 | 10 | 10 | 100% | 🟢 |
| Lesson 10 | 30 | 34 | 88% | 🟢 |
| Lesson 11 | 7 | 7 | 100% | 🟢 |
| Lesson 12 | 7 | 7 | 100% | 🟢 |
| Lesson 13 | 41 | 48 | 85% | 🟢 |
| Lesson 14 | 31 | 33 | 94% | 🟢 |
| Lesson 15 | 24 | 28 | 86% | 🟢 |
| Lesson 16 | 27 | 32 | 84% | 🟢 |
| Lesson 17 | 16 | 17 | 94% | 🟢 |
| Lesson 18 | 23 | 25 | 92% | 🟢 |
| Lesson 19 | 64 | 72 | 89% | 🟢 |
| Lesson 2 | 4 | 4 | 100% | 🟢 |
| Lesson 3 | 4 | 4 | 100% | 🟢 |
| Lesson 20 | 11 | 12 | 92% | 🟢 |
| Lesson 21 | 6 | 7 | 86% | 🟢 |

---

## Weak areas (prioritas soal berikutnya)
**Tak ada area 🔴/🟡 tersisa** — kedua 🟡 lama lulus ambang 80% sesi ini. 1) **L7-で-bahasa 4/5 80% 🟢** (dari 75% 🟡): 「さようなら」は英語で何ですか ✓ — kontras で-media↔partikel lain kini mantap, resmi lewat ambang. 2) **Lesson 21 6/7 86% 🟢** (dari 75% 🟡): tiga soal L21 semua benar — **L21-と言いました** 1/2 (miss lama 0/1 kini terangkat): 「あした休みます」と + 部長に (lawan bicara) → 言いました ✓, kunci arah lewat に-pendengar berhasil membedakan dari 思います; **L21-と思います** 有名だと ✓ (な-adj positif pakai だ); **L21-でしょう** 学生でしょう？ ✓ (N tanpa だ). Kontras だ(と思います)↔tanpa-だ(でしょう) sudah terpisah bersih. **Satu-satunya miss: L19-なります 24/29 83% 🟢** (turun tipis dari 86%) — 「寒（さむ）（　）なります」 dijawab **に**, seharusnya **く**: 寒い = い-adj → 寒くなります; に hanya untuk な-adj/名詞 (元気になります/病気になります). Bukan titik lemah baru (sampel 29, masih 🟢) tapi tandai: jangan campur aturan く (い-adj) vs に (な-adj/N). **Rekomendasi:** sesi depan = **maintenance** (tak ada weak) — sapa bab yang paling lama tak diuji + selipkan 1 soal い-adj→く なります untuk konfirmasi slip L19 bukan pola.
