---
description: Projeye katkı sağlamak isteyenler için bilgilendirme
---

# 💖 Katkıda Bulunma Rehberi

<!-- TODO: Forkları güncelleme alanı eklenecek -->

## 💡 İçerik Desteğinde Bulunma veya Fikir Belirtme

- 📙 Ders notun, ders notu ihtiyacın, tavsiyelerin veya hata tespitlerin varsa [🦋 Issue](https://github.com/yedhrab/IstanbulUniversity-CE/issues) açabilirsin
  - 📈 Bu yapı sayesinde aranan dersler daha belirgin olacaktır.
- 💡 **Yapıcı** eleştirileriniz veya fikirleriniz varsa sağ üst köşedeki  **🏹 Edit on Github** alanından fikirlerinizi belirtebilirsiniz

> 📌 **Formata ([markdown](https://wiki.yemreak.com/1-programlama-notlari/0-genel-notlar/2-markdown)'a) uygun şekilde katkıda bulunursanız hoş olur 😊**

## 📙 Ders Notları Ekleme

Açık kaynaklı projeye ders notların ile katkı sağlamak için:

- 💫 Ders notlarınızı [📕 Online2PDF](https://online2pdf.com/) ile PDF'e çeviriniz.
- [👮‍ Adlandırma Kuralı](#adlandirma-kurali)'na göre adlandırın
- [🚙 Dosya Konumlandırması](#dosya-konumlandirmasi)'na göre alaklı dizinine koyun
- [⏫ GitHub üzerinde dosya yükleme](#github-uezerinde-dosya-yuekleme) alanı işine yaracaktır.

> 👨‍💻 Dosyaya link vermene **gerek yoktur**, scriptim ile otomatik halletmekteyim.

### 👮‍ Adlandırma Kuralı <a name="adlandirma-kurali"></a>

Adlandırma kuralı `<yıl> <tip> <ders_kodu> ~ <sahibi>` şeklindedir.

| 👮‍ Kural | 📜 Açıklama                                                      |
| --------- | ---------------------------------------------------------------- |
| Yıl       | `2019`, `2020`                                                   |
| Tip       | `Vize`, `Final`, `Quiz`, tüm notlar için `Tam` vs                |
| Ders Kodu | Dersinin adının baş harfleri (`NYP` Nesneye yönelik programlama) |
| Sahibi    | Hocanın verdiği notsa boş bırakın, aksi halde isminiz ✨          |

### 🚙 Dosya Konumlandırması <a name="dosya-konumlandirmasi"></a>

| ⭐ Örnek Dosya İsmi                     | 📁 Koyulması gereken yer                                        |
| -------------------------------------- | --------------------------------------------------------------- |
| `2018 Final Notu BM ~ YEmreAk.pdf`     | `3. Sınıf 2. Dönem Notları/Bilgisayar Mimarisi/Öğrenci Notları` |
| `2018 Final BM.pdf`                    | `3. Sınıf 2. Dönem Notları/Bilgisayar Mimarisi/Sınav Soruları`  |
| `2018 Tam Calculus ~ Asma Mirkhan.pdf` | `1. Sınıf 1. Dönem Notları - Calculus 1 - Öğrenci Notları`      |


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

Markdown hakkında detaylı açıklamalara [📑 Markdown](https://wiki.yemreak.com/1-programlama-notlari/0-genel-notlar/2-markdown) bağlantısından erişebilirsin

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
- Güncel bilgiler için [🌍 GitHub Web](https://wiki.yemreak.com/proje-yoenetimi/github/github-web) yazıma bakabilirsin

> Videolar faydalı olmadıysa bana WhatsApp veya Mail üzerinden atabilirsin.

## ⚓ GitHook'lar

### 💫 GitBook İndekslemesini Yapma

```sh
# pip install ypackage
ygitbookintegration . -ll 2
```

### 👀 Neler Değişti Commit'i Tanımlama

```sh
#!/bin/sh
# .git/hooks/pre-push dosyasında

remote="$1"
url="$2"

echo "---
description: Sitede neler olup bittiğinin 📜 raporudur. Buradaki terimleri 🔍 arama motorunda aratarak sayfaya erişebilirsin
---
" > CHANGELOG.md && \
ygitchangelog.exe >> CHANGELOG.md && git add CHANGELOG.md && git commit -m "👀 Neler Değişti alanı yenilendi" && exit 0
```
