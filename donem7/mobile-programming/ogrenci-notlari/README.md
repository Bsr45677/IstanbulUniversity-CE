---
description: Mobil programlama (Mobile Programming) için öğrenci notları
---

# 📕 Öğrenci Notları \| MP

## 📢 Önemli Hususlar

* ⚠️ Notlarda her konu olmayabilir, lütfen dikkatli bakınız. ~ YEmreAk
* ✍ Mobil çalışırken aldığım notları [Android ~ YEmreAk](https://android.yemreak.com/) üzerinde derlemekteyim
* 🌟 Android için faydalı kaynakları [Learn ~ YEmreAk](https://learn.yemreak.com/android) üzerinde derlemekteyi**z**nakları [Learn ~ YEmreAk](https://learn.yemreak.com/android) üzerinde derlemekteyi**z**

## 📗 Final için YEmreAk Notları

🌟 [Android ~ YEmreAk](https://android.yemreak.com/) üzerinde özel olarak derlediğim konular

* [📢 Broadcast](https://android.yemreak.com/haberlesme/broadcast/)
  * [🔰 Giriş \| Broadcast](https://android.yemreak.com/haberlesme/broadcast/giris)
  * [🏗️ Broadcast Oluşturma](https://android.yemreak.com/haberlesme/broadcast/olusturma)
  * [📡 Broadcast Alma](https://android.yemreak.com/haberlesme/broadcast/receiver)
* [🌍 İnternete Bağlanma](https://android.yemreak.com/haberlesme/internete-baglanma)
* [🗂️ RcycleView](https://android.yemreak.com/gui/rcycleview)
* [⏰ Alarm](https://android.yemreak.com/arkaplan/alarm)
* [👨‍💼 Verilerin Yönetimi](https://android.yemreak.com/veriler/)
  * [🔸 Veri Saklama Yöntemleri](https://android.yemreak.com/veriler/veri-saklama-yoentemleri)
  * [📂 Dosya İşlemleri](https://android.yemreak.com/veriler/dosya-islemleri)
  * [👐 Shared Preferences](https://android.yemreak.com/veriler/shared-preferences)
  * [🗃️ SQLite](https://android.yemreak.com/veriler/sqlite)
  * [💽 Room Database](https://android.yemreak.com/veriler/room-database)
* [💫 Asenkron İşlemler](https://android.yemreak.com/arkaplan/asynctask-ve-asynctaskloader)
* [🌞 Foreground Service](https://android.yemreak.com/arkaplan/foreground-service)
* [🪐 Servisler](https://android.yemreak.com/arkaplan/android-servisleri)
* [💌 HTTP İstekleri](https://android.yemreak.com/haberlesme/http-istekleris)

## 📗 Vize için YEmreAk Notları

🌟 [Android ~ YEmreAk](https://android.yemreak.com/) üzerinde özel olarak derlediğim konular

* [🔰 Android'e Giriş](https://android.yemreak.com/giris)
  * [📃 Activity ve Intent'ler](https://android.yemreak.com/giris/activity-ve-intentler)
  * [💫 Activity Yaşam Döngüsü](https://android.yemreak.com/giris/activity-yasam-doenguesue)
  * [🏹 Implicit intents](https://android.yemreak.com/giris/implicit-intents)
  * [🏁 Activity launch modes](https://android.yemreak.com/giris/activity-launch-modes)
  * [⭐ Activity Örnekleri](https://android.yemreak.com/giris/activity-oernekleri)
* [👮‍♂️ İzinlerin Yönetimi](https://android.yemreak.com/temel/izinlerin-yoenetimi)

## 🖨 Not Kağıdı Çıkarma

[Android Developer Fundamentals \(Version 2\) — Concepts](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/) bağlantısındaki sayfaları yazdırmak için:

* Sitede yazdırmak istediğiniz sayfaya girin
* Chrome console'u açın
* Alttaki scripti kopyalayın
* Ardından sayfalarda ilerleyip `print()` yazın

```javascript
function print() {
    var mywindow = window.open('', 'PRINT', 'height=400,width=600');

    mywindow.document.write('<html><head><title>' + document.title  + '</title>');
    mywindow.document.write('</head><body >');
    mywindow.document.write('<h1>' + document.title  + '</h1>');
    mywindow.document.write($("div.page-inner")[0].innerHTML);
    mywindow.document.write('</body></html>');

    mywindow.document.close(); // necessary for IE >= 10
    mywindow.focus(); // necessary for IE >= 10*/
    mywindow.print()
}
```

## 📂 Dosyalar

<!--YPackage.YGitbookIntegration-tarafından-otomatik-oluşturulmuştur-->

- [2019 Final MP ~ YEmreAk](2019%20Final%20MP%20~%20YEmreAk.pdf)
- [2019 Final PDF (Eksik v1) MP ~ YEmreAK](2019%20Final%20PDF%20%28Eksik%20v1%29%20MP%20~%20YEmreAK.pdf)
- [2019 Vize MP ~ YEmreAk](2019%20Vize%20MP%20~%20YEmreAk.pdf)
- [2019 Vize Sınav Kağıdı](2019%20Vize%20S%C4%B1nav%20Ka%C4%9F%C4%B1d%C4%B1.pdf)
- [4.3 Menus and pickers GitBook](4.3%20Menus%20and%20pickers%20GitBook.pdf)

<!--YPackage.YGitbookIntegration-tarafından-otomatik-oluşturulmuştur-->
