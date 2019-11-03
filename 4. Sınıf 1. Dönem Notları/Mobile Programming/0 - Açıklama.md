# 🗽 Açıklama

- Ders android tabanlı ilerlemektedir
- Android 4.0 sürümü temel alınacaktır

> Android notlarım için [buraya](https://android.yemreak.com) bakabilirsin

## 📢 Duyurular

- Ders **LAB** yerine **D521**'de işlenmektedir.
- 📧 Mail grubu linkine [buradan](https://groups.google.com/forum/#!forum/iuce_mobile_programming/join) erişebilirsin
- [👨‍🏫 Classroom](https://classroom.google.com) kodu `xxvyra6`

## 📃 Android Developer Fundamentals için Print metodu

[Android Developer Fundamentals (Version 2) — Concepts](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/) bağlantısındaki sayfaları yazdırmak için:

- Sitede yazdırmak istediğiniz sayfaya girin
- Chrome console'u açın
- Alttaki scripti kopyalayın
- Ardından sayfalarda ilerleyip `print()` yazın

```js
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
