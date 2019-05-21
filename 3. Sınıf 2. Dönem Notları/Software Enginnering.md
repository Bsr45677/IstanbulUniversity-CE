# Software Engineering <!-- omit in toc -->

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönelebilirsin.

- [Ders Hakkında](#ders-hakk%C4%B1nda)
  - [Ders Kaynakları](#ders-kaynaklar%C4%B1)
  - [Vize Hakkında](#vize-hakk%C4%B1nda)
  - [Final Hakkında](#final-hakk%C4%B1nda)
- [Giriş](#giri%C5%9F)
  - [Sık Sorulan Sorular](#s%C4%B1k-sorulan-sorular)
  - [İyi bir Yazılımın Temel Özellikleri](#i%CC%87yi-bir-yaz%C4%B1l%C4%B1m%C4%B1n-temel-%C3%B6zellikleri)
- [UML Diagrams](#uml-diagrams)
  - [Use-Case Diagram](#use-case-diagram)
    - [Extend-Include Kavramları](#extend-include-kavramlar%C4%B1)
    - [General / Specialized Use Cases](#general--specialized-use-cases)
  - [Sequence Diagram](#sequence-diagram)
  - [Class Diagram](#class-diagram)
    - [Class Diagram Structure (Yapısı)](#class-diagram-structure-yap%C4%B1s%C4%B1)
    - [Multiplicity](#multiplicity)
    - [Child / Parent Class](#child--parent-class)
  - [Satate Diagram](#satate-diagram)
- [Faydalı Linkler](#faydal%C4%B1-linkler)

## Ders Hakkında

- Hocası: *Atakan Kurt*
- Vakti: Salı 9:00
- *Yoklama var*
- 1 Arasınav 1 Final
- Google grubu için [buraya](https://groups.google.com/forum/#!forum/software2019) tıklayabilirsin.
 bakabilirsin

### Ders Kaynakları

Ders içerikleri drive üzerinden yedeklenmektedir, [buraya][Drive] tıklayarak erişebilirsin.

- Dersin baz aldığı slaytların sitesi için [buraya](https://iansommerville.com/software-engineering-book/slides/)
- Labdaki UML çalışmalarına [buradan](https://drive.google.com/open?id=1ktuvuBlt1beX84tDpJYQSEqvhbl-i_x1) erişebilirsin

### Vize Hakkında

> Bilgiler alıntıdır.

- %60 test ve boşluk doldurma (20 tane)
  - Temel software process aktiviteleri nelerdir?
  - Implemenral development avantajları
  - Hangisi uml diagram tipi değilgir?
  - Hangisi extreme programming özelliği değildir
  - Chapter 1-8
- %40 UML Diagram
  - Sequence diagram
  - State diagram
  - Use case diagram
  - Class diagram
  - Activity diagram

### Final Hakkında

- Tum dönem dahil
  - Ağırlıklı vize sonrası slaytlar (9,11,19,22 sonrası)
- Test ağırlıklı
- Kolay
- [Jira], Git, [Confluence]

## Giriş

### Sık Sorulan Sorular

![freq_ask_q](../res/frequently_asked_q.png)
![freq_ask_q2](../res/freq_ask_q2.png)

### İyi bir Yazılımın Temel Özellikleri

- Sürdürülebilirlik (Maintainablity)
- Güvenilirlik ve Güvenelik (Dependability and Security)
- Etkinlik (Efficienty)
- Kabul Edilebilirlik (Acceptability)

![essential_attr_for_good_software](../res/essential_attr_for_good_software.png)

## UML Diagrams

### Use-Case Diagram

Video 📹 için [buraya](https://www.youtube.com/watch?v=zid-MVo7M-E) bakabilirsin.

![use_case](../res/use_case.png)

#### Extend-Include Kavramları

| Kavram  | Açıklama                                       |
| ------- | ---------------------------------------------- |
| Include | Eyleme dahil olan ativiteler                   |
| Extend  | Eylem sırasında oluşabilecek olası aktiviteler |

![use_case_extend](../res/use_case_extend.png)

Her hapşırmada gözler kapatılır (include), ama isteğe bağlı olarak özür dilenir (extend).

#### General / Specialized Use Cases

![use_case_gen_spec](../res/use_case_gen_spec.png)

### Sequence Diagram

Video 📹 için [buraya](https://www.youtube.com/watch?v=pCK6prSq8aw) bakabilirsin.

![seq_diagram](../res/sequence_diagram.png)

### Class Diagram

Video 📹 için [buraya](https://www.youtube.com/watch?v=UI6lqHOVHic) bakabilirsin.

![class_diagram_ex](../res/class_daigram_ex.png)

#### Class Diagram Structure (Yapısı)

![class_diagram_structure](../res/class_diagram.png)

#### Multiplicity

![multiplicity](../res/multiplicity.png)

Bir lobi olur ama en az bir banyo içerir.

#### Child / Parent Class

![child_parent](../res/chlld_parent.png)

### Satate Diagram

Web sitesi üzerinden açıklama için [buraya](https://www.lucidchart.com/pages/uml-state-machine-diagram) bakabilirsin.

![state_diagram](../res/state_diagram.png)

## Faydalı Linkler

- [Diagram Çizme Uygulamaları](https://www.lucidchart.com/)

[Drive]: https://github.com/yedhrab/IstanbulUniversity-CE.git
[Confluence]: https://www.atlassian.com/software/confluence
[Jira]: https://www.atlassian.com/software/jira