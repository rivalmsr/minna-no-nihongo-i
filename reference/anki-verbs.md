# Pool Kata Kerja (動詞) — Sumber Active Recall Quiz

> ⚙️ **FILE AUTO-GENERATED — jangan edit tangan.** Regenerasi dari deck Anki dengan
> `bash scripts/sync-anki-verbs.sh`. Upstream source of truth = folder
> `learn-anki/Minna no Nihongo I/MNN*.txt` (yang kamu update untuk Anki). Jalankan
> ulang script tiap kali deck bertambah/berubah agar /quiz tetap sinkron.

Ekstraksi **semua kata kerja** dari deck Anki. Tujuan file ini bukan menghafal arti
(itu tugas Anki), tapi **membiasakan MEMAKAI kata kerja** dalam kalimat &
mengkonjugasikannya — konsep **active recall**. `/quiz` memakai file ini sebagai
kolam verb utama untuk soal konjugasi & pemakaian.

> Ringkasan cepat (anchor — baca ini saja saat quiz):
> - **87 verb**, dikelompokkan **grup I (46) / II (25) / III (16)** (penentu bentuk て・ない・辞書・た).
> - **Grup II** paling mudah: buang ます → tempel langsung (`たべます→たべて／たべない／たべる／たべた`).
> - **Grup III** cuma 2 pola: `〜します` & `〜きます` (irregular, hafal).
> - **Grup I** butuh **音便** (lihat tabel 音便 di bawah) untuk bentuk て／た.
> - Bab konjugasi: **て = L14**, **ない = L17**, **辞書形 = L18**, **た = L19**.
> - Soal tata bahasa tetap **hanya** dari lesson yang tersedia di `lessons/`.

## Cara pakai untuk active recall (target soal)

Alih-alih "apa arti のみます?", soal harus memaksa **produksi bentuk & konteks**:
- **Konjugasi:** `およぎます` → bentuk て? (`およいで`) · ない? (`およがない`) · た? (`およいだ`)
- **Pemakaian dalam pola in-scope:** `〜てください`, `〜ています`, `〜なければなりません`,
  `〜たことがあります`, `〜たり〜たり`, `〜ことができます`, dll. dengan verb dari pool ini.
- **Pasangan mirip / 他動詞↔自動詞:** `はじめます（を）↔はじまります（が）`, `でます↔だします`,
  `のります（に）↔おります（を）`, `つけます↔けします`, `あけます↔しめます`.

## 音便 bentuk て／た — GRUP I (yang paling sering lupa)

| Akhiran ます | → て | → た | Contoh |
|-------------|------|------|--------|
| 〜います・〜ちます・〜ります | って | った | かいます→かって, まちます→まって, とります→とって |
| 〜みます・〜びます・〜にます | んで | んだ | のみます→のんで, よびます→よんで, あそびます→あそんで |
| 〜きます | いて | いた | かきます→かいて（**例外 いきます→いって**） |
| 〜ぎます | いで | いだ | およぎます→およいで／およいだ |
| 〜します | して | した | はなします→はなして／はなした |

Grup II: buang ます, tempel て／ない／る／た langsung. Grup III: `します→して／しない／する／した`,
`きます→きて／こない／くる／きた`.

---

## GRUP I (46) — perlu 音便 untuk て／た
| ます形 | Arti | Bab |
|--------|------|-----|
| あります | ada (benda mati) | L10 |
| かかります | memakan, perlu (digunakan untuk waktu dan uang) | L11 |
| やすみます | tidak masuk [kerja] | L11 |
| あそびます | bermain | L13 |
| およぎます | berenang | L13 |
| けします | mematikan, memadamkan | L14 |
| いそぎます | buru-buru | L14 |
| まちます | menunggu | L14 |
| もちます | membawa | L14 |
| とります | mengambil | L14 |
| てつだいます | membantu | L14 |
| よびます | memanggil | L14 |
| はなします | berbicara | L14 |
| つかいます | memakai | L14 |
| すわります | duduk | L14 |
| たちます | berdiri | L14 |
| はいります | masuk | L14 |
| ふります | turun | L14 |
| おきます | meletakkan, menaruh | L15 |
| つくります | membuat, membangun, memproduksi | L15 |
| うります | menjual | L15 |
| しります | mengetahui, mengenal | L15 |
| すみます | tinggal | L15 |
| おもいだします | teringat | L15 |
| いらっしゃいます | ada (bentuk sopan dari います) | L15 |
| のります | naik | L16 |
| だします | mengeluarkan, menyerahkan, mengirim | L16 |
| おろします | mengeluarkan/mengambil | L16 |
| はいります | masuk | L16 |
| おします | menekan | L16 |
| のみます | minum | L16 |
| はじまります | mulai | L16 |
| なくします | kehilangan | L17 |
| はらいます | membayar | L17 |
| かえします | mengembalikan | L17 |
| ぬぎます | membuka (baju, sepatu, dll.) | L17 |
| もっていきます | membawa pergi | L17 |
| [くすりを〜] のみます | minum | L17 |
| [おふろに〜] はいります | mandi, masuk tempat mandi | L17 |
| あらいます | mencuci | L18 |
| ひきます | bermain (untuk bermain alat musik senar dan piano) | L18 |
| うたいます | bernyanyi, menyanyi | L18 |
| のぼります | naik | L19 |
| とまります | menginap | L19 |
| なります | menjadi | L19 |
| いります | memerlukan | L20 |

## GRUP II (25) — buang ます, tempel langsung
| ます形 | Arti | Bab |
|--------|------|-----|
| います | ada (benda hidup) | L10 |
| います | ada | L11 |
| むかえます | menjemput | L13 |
| つかれます | lelah (jika menyatakan keadaan lelah, digunakan bentuk た seperti つかれました) | L13 |
| つけます | menyalakan, memasang, menghidupkan | L14 |
| あけます | membuka | L14 |
| しめます | menutup | L14 |
| とめます | menghentikan, memarkir | L14 |
| みせます | memperlihatkan | L14 |
| おしえます | memberitahukan | L14 |
| でます | keluar | L14 |
| おります | turun | L16 |
| のりかえます | ganti, pindah | L16 |
| あびます | mandi | L16 |
| いれます | memasukkan | L16 |
| でます | tamat | L16 |
| はじめます | memulai | L16 |
| おぼえます | mengingat, menghafal | L17 |
| わすれます | lupa | L17 |
| でかけます | pergi, keluar, berangkat | L17 |
| できます | dapat, bisa, mampu | L18 |
| あつめます | mengumpulkan | L18 |
| すてます | membuang | L18 |
| かえます | mengganti, menukar | L18 |
| しらべます | memeriksa, meneliti, mengecek | L20 |

## GRUP III (16) — します／きます (irregular)
| ます形 | Arti | Bab |
|--------|------|-----|
| けっこんします | menikah | L13 |
| かいものします | berbelanja | L13 |
| しょくじします | makan | L13 |
| さんぽします | berjalan-jalan | L13 |
| コピーします | memfotokopi | L14 |
| けんきゅうします | meneliti | L15 |
| けんがくします | mengunjungi untuk observasi | L16 |
| でんわします | menelepon | L16 |
| もってきます | membawa datang | L17 |
| しんぱいします | mengkhawatirkan | L17 |
| ざんぎょうします | melembur | L17 |
| しゅっちょうします | dinas | L17 |
| うんてんします | menyetir, mengendarai | L18 |
| よやくします | memesan (reservasi) | L18 |
| そうじします | membersihkan | L19 |
| せんたくします | mencuci pakaian | L19 |

---

_Auto-generated 2026-08-29 oleh `scripts/sync-anki-verbs.sh` dari
`learn-anki/Minna no Nihongo I/MNN*.txt`. Total 87 verb._
