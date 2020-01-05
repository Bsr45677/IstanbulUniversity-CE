---
description: Projeye katkı sağlamak isteyenler için bilgilendirme
---

# 💖 Katkıda Bulunma Rehberi

<!-- TODO: Forkları güncelleme alanı eklenecek -->

## 💡 İçerik Desteğinde Bulunma veya Fikir Belirtme

- 📙 Ders notun, ders notu ihtiyacın, tavsiyelerin veya hata tespitlerin varsa [🦋 Issue](https://github.com/yedhrab/IstanbulUniversity-CE/issues) açabilirsin
  - 📈 Bu yapı sayesinde aranan dersler daha belirgin olacaktır.
- 💡 **Yapıcı** eleştirileriniz veya fikirleriniz varsa sağ üst köşedeki  **🏹 Edit on Github** alanından fikirlerinizi belirtebilirsiniz

> 📌 **Formata ([markdown](https://lib.yemreak.com/1-programlama-notlari/0-genel-notlar/2-markdown)'a) uygun şekilde katkıda bulunursanız hoş olur 😊**

## 📙 Ders Notları Ekleme

Açık kaynaklı projeye ders notların ile katkı sağlamak için:

- 💫 Ders notlarınızı [📕 Online2PDF](https://online2pdf.com/) ile PDF'e çeviriniz.
- [👮‍ Adlandırma Kuralı](#adlandirma-kurali)'na göre adlandırın
- [🚙 Dosya Konumlandırması](#dosya-konumlandirmasi)'na göre alaklı dizinine koyun
- [⏫ GitHub üzerinde dosya yükleme](#github-uezerinde-dosya-yuekleme) alanı işine yaracaktır.

> 👨‍💻 Dosyaya link vermene **gerek yoktur**, scriptim ile otomatik halletmekteyim.

### 👮‍ Adlandırma Kuralı <a name="adlandirma-kurali"></a>

| 👮‍ Kural | 📑 Format                                                      |
| --------- | ---------------------------------------------------------------- |
| 📕 Öğrenci notları       |  `<tip> <yıl> <ders_kodu> ~ <sahibi>`                 |
| 📃 Sınav       |  `<tip> <yıl> <ders_kodu>`                 |
| 📚 Ders notu | `<hafta>.hafta <yıl> <ders kodu>` veya orjinal ismi ile kalabilir |

> ❣️ `Vize, Final veya Büt` özellikleri, tarihinden daha önemli olduğundan ilk onlar yazılmalıdır

| 👮‍ Kural | 📜 Açıklama                                                      |
| --------- | ---------------------------------------------------------------- |
| Tip       | `Vize`, `Final`, `Quiz`, tüm notlar için `Tam` vs                |
| Yıl       | `2019`, `2020`                                                   |
| Ders Kodu | Dersinin adının baş harfleri (`NYP` Nesneye yönelik programlama) |
| Sahibi    | Hocanın verdiği notsa boş bırakın, aksi halde isminizi lütfedin ✨|
| Hafta | Kaçıncı haftanın notu olduğu (`1`, `2`, `Son`) |

### 🚙 Dosya Konumlandırması <a name="dosya-konumlandirmasi"></a>

| ⭐ Örnek Dosya İsmi                     | 📁 Koyulması gereken yer                                        |
| -------------------------------------- | --------------------------------------------------------------- |
| `2018 Final Notu BM ~ YEmreAk.pdf`     | `donem6\bilgisayar-mimarisi\ogrenci-notlari` |
| `2018 Tam Calculus ~ Asma Mirkhan.pdf` | `donem1\calculus-1\ogrenci-notlari`      |
| `Final 2018 BM.pdf`                    | `donem6\bilgisayar-mimarisi\sinav-sorulari`  |
| `BPG1- Giris.pdf` | `donem7\bilisim-proje-gelistirme\ders-icerigi\sunumlar` |

## 📑 İçerik Yazma Formatı

Başlık ile alakalı bir emoji koyman verimlilik adına çok etkilidir.

- Windows üzerinde, <kbd>❖ Win</kbd> <kbd>Ş</kbd> ile emoji klavyesini açabilirsin
- Linux için [😎 Emoji Selector](https://extensions.gnome.org/extension/1162/emoji-selector/) eklentisini kullanabilirsin

```md
## 🌟 Başlık

Giriş cümlesi veya alakalı cümle.

- Alaklı maddesel bilgiler
- Bilgi 2

> Varsa ek yorum

<!-- Tablo oluşturman gerekiyorsa -->
| Tablo        | Tablo1                      |
| ------------ | --------------------------- |
| `<değişken>` | Tablosal yapı ile örnekleme |

- `<değişken>` Tablo değişkenlerini açıklama
  - Örn: `kod` örneklendirme


<!-- Tek bağlantı varsa -->
> [Kaynak ismi](https://yemreak.com)

<!-- Birden fazla bağlantı varsa -->
> Ek bağlantılar:
>
> - [Link](https://yemreak.com)
> - [Link](https://yemreak.com)
> - [Link](https://yemreak.com)

```

## ✍ Çalışma Notları

Markdown hakkında detaylı açıklamalara [📑 Markdown](https://lib.yemreak.com/1-programlama-notlari/0-genel-notlar/2-markdown) bağlantısından erişebilirsin

- Her şey **dinamik** olmalı
- Önemli notlar ve başlıklar **bold**
- Butonlar ve tıklanabilir öğeler <kbd>button</kbd> `<kbd>button</kbd>`
- Terimler _italik_ `_italik_`
  - Önce normal yaz, sonrasında <kbd>✲ Ctrl</kbd> + <kbd>H</kbd> ile metinleri italik hale dönüştür
- Kalıplar ve sabit ifadeler \` arasına yazılmalı
- Kodlar ``` arasına yazılmalı
- Matematikler (latex) $latex$ `$$latex$$ (gitbook) veya $latex$ (github) `

## 🏃‍ Web Üzerinden Projeye Hızlıca Katkıda Bulunma

GitHub projelerini `clone` yapıp, internetini harcamak yerine web üzerinden katkıda bulunabilirsin.

- [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/YEmreAk/IstanbulUniversity-CE)
 ile online sanal makineden işlemlerinizi yapabilirsiniz
- Katkı sağlama işlemi GitHub hesabı gerektirir.
- Güncel bilgiler için [🌍 GitHub Web](https://lib.yemreak.com/proje-yoenetimi/github/github-web) yazıma bakabilirsin

> Videolar faydalı olmadıysa bana WhatsApp veya Mail üzerinden atabilirsin.

## ⚓ GitHook'lar

- ❣️ Bu alana sadece **ne olduğunu biliyorsan** bakmanı tavsiye ederim.
- 📢 Ders notu ekleme gibi işlemler, yaptıktan sonra bilene haber edebilirsiniz
- 💁‍♂️ Zaten eklenme işlemleri ile oluşan *pull request* bilen tarafından kabul edilecektir

### 💫 GitBook İndekslemesini Yapma

Projeyi güncelleme işlemi için alttaki komutları veya `integrate.sh` scriptini kullanın

- `pip3 install ypackage` ile ypackage paketimi indirin
- `ygitbookintegration .` komutu ile entegrasyonu sağlayın

> Komut hakkında detaylar için `ygitbookintegration -h` yazabilirsiniz.
