---
name: sync-anki
description: Refresh data Anki yang dipakai /quiz & /jlpt — regenerasi reference/anki-verbs.md (pool kata kerja) dan progress/anki-weak-items.md (item lemah lapses+leech) dari sumber Anki lokal, tampilkan ringkasan, tawarkan commit. Pakai saat user menjalankan /sync-anki atau minta "update/refresh/sync anki (verbs / weak items)".
---

# Skill: /sync-anki — Refresh Data Anki

Regenerasi dua file turunan dari Anki yang jadi bahan `/quiz` & `/jlpt`:

| File output | Script | Sumber |
|---|---|---|
| `reference/anki-verbs.md` (pool kata kerja) | `scripts/sync-anki-verbs.sh` | `learn-anki/*.txt` (kurasi, gitignored) |
| `progress/anki-weak-items.md` (item lemah 🔴🟡⚪) | `scripts/sync-anki-weak-items.sh` | `collection.anki2` (Anki desktop) |

Kedua file **AUTO-GENERATED — jangan edit tangan.**

## Argumen

- `/sync-anki` → jalankan **kedua** script (default).
- `/sync-anki weak` (atau `weak-items`) → hanya `anki-weak-items.md`.
- `/sync-anki verbs` → hanya `anki-verbs.md`.

## ⚠️ Prasyarat WAJIB diingatkan (untuk weak-items)

`anki-weak-items.md` dibaca dari **`collection.anki2` desktop**. Kalau user review
harian di **iPhone**, data itu belum turun ke desktop sampai:
**buka Anki desktop → Sync**. Sync di iPhone saja **tidak** update file desktop.

**Sebelum menjalankan sync weak-items, tanya dulu:** "Sudah buka Anki desktop & Sync?"
Kalau belum → minta user Sync dulu, jangan lanjut (data jadi basi). Kalau sudah /
user bilang tak review di iPhone → lanjut. (Untuk mode `verbs` saja, prasyarat ini
tak berlaku — sumbernya `learn-anki/*.txt`, bukan collection.)

## Langkah eksekusi

1. Parse argumen (weak / verbs / keduanya).
2. Kalau mencakup weak-items → konfirmasi prasyarat Sync desktop (lihat atas).
3. Jalankan script terkait via Bash:
   - `bash scripts/sync-anki-verbs.sh`
   - `bash scripts/sync-anki-weak-items.sh`
4. Cek `git diff --stat` untuk file output → tentukan ada perubahan atau tidak, lalu
   **beri notifikasi singkat**:
   - **Ada data baru** (file berubah) → `✅ Sukses updated` + ringkasan yang dicetak
     script (mis. `Minna: 🔴20 🟡58 ⚪87 | Kanji N5: 🔴9 …`) + file mana yang berubah.
     Lalu **tawarkan commit** (pesan gaya repo `chore(progress): sync Anki weak items` /
     `chore(reference): sync Anki verbs`, angka ringkasan di body). Jangan commit tanpa izin.
   - **Tak ada data baru** (file tak berubah) → `ℹ️ No data updated` (sudah up-to-date).
     Tak perlu commit.

## Catatan

- Script pakai `set -euo pipefail`; kalau error (mis. `collection.anki2` tak ketemu),
  laporkan pesan error apa adanya dan sarankan set `ANKI_COLLECTION=...` atau beri path
  sebagai argumen — **jangan** karang datanya.
- Detail integrasi & rantai sync iPhone→desktop: `docs/anki-integration-plan.md`.
