# Rencana: Integrasi Data Anki ke Knowledge Base

> **Status: RENCANA — belum dieksekusi.** Dokumen forward-looking. Dibuat 2026-08-23,
> direvisi 2026-08-23 setelah verifikasi. Eksekusi menyusul, per fase, setelah disetujui.

## 0. Koreksi penting (hasil verifikasi 2026-08-23)

Draf awal dokumen ini mengira **pipeline verb rusak & file basi**. Setelah dicek, itu
**KELIRU**:

- Folder sumber `.txt` **tidak hilang** — user memindahkannya ke
  `~/rdeveloper/personal/learn-anki/Minna no Nihongo I/` (MNN01–20.txt lengkap). Ini
  yang di-update user ke depan sebagai bahan Anki per lesson.
- Path itu **persis** yang di-resolve `scripts/sync-anki-verbs.sh`
  (`$PROJECT_ROOT/../../learn-anki/...`). **Script jalan normal.**
- Menjalankan ulang script menghasilkan output **identik** dengan `anki-verbs.md`
  sekarang (hanya tanggal berubah) → **file tidak basi, 87 verb akurat.**
- Kekhawatiran "87 vs ~113" = alarm palsu: 113 dari collection kehitung **duplikat**
  (います, でます muncul 2×/bab) + kartu di luar `.txt` kurasian. Sumber of truth = `.txt`.

**Konsekuensi:** "Fase A — perbaiki pipeline rusak" versi lama **DIBATALKAN** (tidak ada
yang rusak). Yang tersisa & benar-benar bernilai = **sinyal kesulitan** (lihat §2).

## 1. Konteks & pembagian sumber

Ada **dua sumber Anki**, dengan peran berbeda — jangan dicampur:

| Sumber | Lokasi | Berisi | Peran |
|--------|--------|--------|-------|
| **File `.txt` (kurasi user)** | `~/rdeveloper/personal/learn-anki/Minna no Nihongo I/MNN*.txt` | kata, arti, grup verb, bab (dari nama file) | **Source of truth** daftar verb → sudah dipakai `anki-verbs.md` |
| **Collection Anki** | `~/Library/Application Support/Anki2/User 1/collection.anki2` | `lapses`, `ease`, `ivl`, tag `leech`, revlog | **Sinyal kesulitan empiris** — BELUM dipakai KB sama sekali |

Isi collection (per 2026-08-23): deck **Minna** 896 kartu (0 baru, ~80% matang),
**Kanji N5** 107 kartu (sedang jalan). Deck N4 & Oxford 3000 A1 di luar cakupan.

Temuan berguna di collection:
- **Bab** tersimpan sebagai tag `MNNXX` (skema sama seperti nama file `.txt`).
- Tag **`leech`** = penanda bawaan Anki untuk kartu yang **berulang kali gagal** —
  sinyal kesulitan siap-pakai, di samping angka `lapses`.
- Contoh verb lapses tertinggi: だします (13×), もらいます (13×), つけます (12×),
  けします (12×). Sinyal ini **tidak ada** di `.txt`, hanya di collection.

> **Insight inti (tetap berlaku):** `progress/evaluation.md` melacak kelemahan per
> **pola grammar**; Anki melacak kelemahan per **item kosakata/kanji**. Menikahkan
> keduanya → `/quiz` & `/jlpt` bisa memilih "kendaraan" kosakata/kanji yang benar-benar
> sulit, **di dalam** pola yang lemah. Selaras dengan filosofi CLAUDE.md.

## 2. Rencana per fase (revisi)

### ~~Fase A — Perbaiki pipeline~~ — DIBATALKAN

Tidak ada yang rusak (lihat §0). Pipeline `.txt → anki-verbs.md` sehat. Cukup jalankan
`bash scripts/sync-anki-verbs.sh` seperti biasa saat deck `.txt` berubah.

### Fase A′ (baru) — Perkaya `anki-verbs.md` dengan sinyal kesulitan (opsional)

**Ide:** tambah kolom **kesulitan** ke tiap verb, digabung dari collection.

- Baca `collection.anki2` (salin ke temp dulu untuk hindari lock; query read-only).
- Untuk tiap verb `.txt`, cocokkan **ます形** ke Front kartu di deck Minna, ambil
  `lapses` + apakah bertag `leech`.
- Tandai: 🔴 = `leech` atau `lapses ≥ 8` · 🟡 = `lapses 4–7` · ⚪ = `lapses 0–3`.
- Tulis kolom baru di tabel `anki-verbs.md` supaya `/quiz` bisa memberi porsi lebih ke
  verb yang empiris sering lupa.

**Catatan implementasi:**
- Ini membuat `sync-anki-verbs.sh` bergantung pada **dua** sumber (`.txt` + collection).
  Kalau collection tak ada (mesin lain), harus **gagal anggun** → tetap tulis tabel
  tanpa kolom kesulitan, jangan error.
- Cocokkan by **Front string** (mis. `だします I`). Hati-hati verb berpasangan/duplikat.

**Keputusan yang perlu diambil dulu:** apakah kolom kesulitan cukup berharga untuk
menambah ketergantungan ke collection? Atau lebih baik dipisah sebagai Fase B?

### Fase B — Laporan item lemah (data baru) — ✅ SELESAI 2026-08-23

- ✅ `scripts/sync-anki-weak-items.sh` — regen `progress/anki-weak-items.md` dari
  `collection.anki2` (salin ke temp → query read-only; resolusi deck tahan subdeck
  `\x1f`; gagal anggun bila collection tak ada).
- ✅ `progress/anki-weak-items.md` — section **Kosakata/Verb lemah** (Minna) &
  **Kanji lemah** (N5), + anchor 🔴 ringkas. Kanji berbacaan (furigana). File turunan.
- **Ambang final:** 🔴 = `leech` atau `lapses ≥ 8` · 🟡 = `lapses 5–7` · ⚪ (`lapses 3–4`)
  hanya dihitung. Kartu suspended: tidak ada di kedua deck, jadi tak jadi isu.
- ✅ Terdaftar di `README.md` & `CLAUDE.md` (bukan file yatim).
- Hasil awal: Minna 🔴19/🟡57 · Kanji N5 🔴7/🟡16.

### Fase C — Integrasi ke skill /quiz & /jlpt (mengikat)

- Update `.claude/skills/quiz/SKILL.md` & `jlpt/SKILL.md`: saat memilih kendaraan
  kosakata/kanji, **boboti** ke item lemah Anki (dari A′/B), **di dalam** pola lemah
  `evaluation.md`. Soal grammar tetap hanya dari `lessons/`.
- **Keputusan:** bobotnya jangan menenggelamkan tujuan utama (uji pola). Anki = pemilih
  *kosakata*, bukan pengganti *pola*. Sediakan anchor ringkas agar hemat token.

## 3. Perawatan konsistensi KB — ad-hoc, BUKAN skill `/lint`

Kita menimbang mengadopsi pola "LLM wiki" (Karpathy) dengan operasi **Lint** (cek
kontradiksi, klaim basi, file yatim, cross-ref rusak). **Keputusan: TIDAK membuat skill
`/lint` formal.** Alasan:

- KB ini **kecil & berbatas** (1 buku, ~18 lesson, 1 target N5, 1 pembaca). Pola LLM-wiki
  bersinar untuk korpus besar/heterogen yang terus membengkak — bukan kasus ini.
- KB **sudah menjalankan** inti pola itu secara organik: schema doc (CLAUDE.md), alur
  ingest (aturan update saat tambah lesson), query (/quiz, /jlpt). Menambah seremoni =
  over-engineering.

**Gantinya:** cek konsistensi dilakukan **ad-hoc saat perlu** — mis. saat terasa ada
yang basi, sehabis menambah lesson/sumber, atau saat menyentuh file turunan. Yang
diperiksa saat itu: file turunan vs sumbernya masih sinkron, cross-ref (`evaluation.md`
↔ lesson, tag taxonomy ↔ lesson) masih valid, tidak ada halaman yatim. Prosedur ringan,
bukan infrastruktur.

## 4. Urutan eksekusi & status

1. ~~Fase A′ atau B~~ → **Fase B SELESAI** (2026-08-23). A′ (kolom kesulitan di verb
   pool) diputuskan **tidak** dikerjakan — pilih file terpisah agar pipeline verb yang
   sehat tidak dikaitkan ke collection.
2. **Fase C — BELUM.** Berikutnya: wiring `anki-weak-items.md` ke `/quiz` & `/jlpt`
   (memilih kendaraan kosakata/kanji condong ke item lemah, di dalam pola lemah). Butuh
   edit `SKILL.md` + anchor-read agar hemat token. Menunggu keputusan.

Eksekusi menunggu persetujuan. Saat mengeksekusi, patuhi konvensi CLAUDE.md (furigana
wajib, file turunan tak diedit tangan, update README/taxonomy bila perlu, laporkan tiap
perubahan).
