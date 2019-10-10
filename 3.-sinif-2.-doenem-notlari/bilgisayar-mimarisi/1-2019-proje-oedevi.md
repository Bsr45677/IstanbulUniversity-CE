# 2019 Proje Ödevi

## 🗽 Açıklama

Proje ödevinin PDF'ine [buradan](https://github.com/yedhrab/IstanbulUniversity-CE/tree/ad5ffcd6c9a7d2d69f67d0a5559f092531cb8d13/res/2019_bilgisayar_mimarisi_proje.pdf) ulaşabilirsin.

* Proje için hazırladığımız [PDF](https://github.com/yedhrab/IstanbulUniversity-CE/tree/ad5ffcd6c9a7d2d69f67d0a5559f092531cb8d13/res/16BitMipsVHDL.pdf)'e ve [repository](https://github.com/yedhrab/16BitMipsVHDL)'e yazılara tıklayarak erişebilirsin
* Grup sayısı 5 kişiliktir
* Son teslim tarihi: 20 Mayıs 2019 Pazartesi
* Proje'yi yapabilmek için **XILINX ISE Design Studio kurulumu** yapmanız gerekmekte

## XILINX ISE Design Studio

* Resmi sitesinde indirmek için [buraya](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/design-tools.html) tıklayabilirsin
  * Username: `yemreak`
  * Password: `yemreak.com1`
* **XILINX ISE Design Studio**'yu direkt olarak [buradan](https://xilinx-ax-dl.entitlenow.com/dl/ul/2018/02/21/R209898474/Xilinx_ISE_S6_Win10_14.7_ISE_VMs_0206_1.zip/70f417f0787735862bdf9e9e3107e2af/5CC73BF4?akdm=0&filename=Xilinx_ISE_S6_Win10_14.7_ISE_VMs_0206_1.zip) indirebilirsin.
* **Drive** üzerinden indirmek için [buraya](https://drive.google.com/open?id=1-4j-ZBZmA5axu2G3ebxcITROWsR2IUny) bakabilirsin.
* `VirtualBox host only adaptor disappeared (Interface (‘VirtualBox Host-Only Ethernet Adapter’) is not a Host-Only Adapter interface (VERR_INTERNAL_ERROR) SOLVED` hatası için [buraya](https://darrenoneill.eu/?p=627) bakabilirsin.

## XILINX Kullanımı

Hocanın hazırlamış olduğu videolar:

* [XILINX ile VHDL PROGRAMLAMA! - Full Adder \(Tam Toplayıcı\) Tasarımı \#1](https://www.youtube.com/watch?v=-SZuTT3xa18)
* [XILINX ile VHDL PROGRAMLAMA! - Full Adder \(Tam Toplayıcı\) Tasarımı \#2](https://www.youtube.com/watch?v=H7jihUQz-Io)
* [XILINX ile VHDL PROGRAMLAMA! - Full Adder \(Tam Toplayıcı\) Tasarımı \#3](https://www.youtube.com/watch?v=Sw5ktjHl1zc)

> Alttaki bilgilerde yapılacak işlermler özetlenmiştir.

### Proje Oluşturma

* `New Project`
* Top-level source type: `HDL`
* `XST`, `ISIM`, Preffered Language: `VHDL`

### Proje İşlemleri

* `New Source` &gt; `VHDL_module`
* Modülü boş bırakın devam edin.

### Simüle Etme

* Similasyon oluşturmak için [buraya](https://youtu.be/H7jihUQz-Io?t=637) bakabilirsin.
  * `Start with a semantic of the top-level block`
* Simülasyona veri girişi için [buraya](https://youtu.be/Sw5ktjHl1zc?t=576) bakabailirsin.
  * `restart` Yeniden başlatma
  * `put <pbje_ismi> <değer>` Veri atama
    * Örn: `put tt_g1 0`
  * `run all` Hepsini çalıştırma

## Teslim Şekli

* Similasyon sonuçları raporlanacak ve pdf haline getirilecek
* Verilen _instruction_'ların hepsi gerçekleştirilecek
* Sonuçlar similatörde gösterilecek
* PDF ile `.vhd` uzantılı kaynak kodlarını sisteme yüklenecek
  * Aksis - Döküman paylaşımı - Bilgisayar Mimarisi - Proje

## Faydalı Bağlantılar

* [16bit Mips VHDL](https://www.fpga4student.com/2017/09/vhdl-code-for-mips-processor.html)
* [MIPS-Processor-VHDL - Github](https://github.com/cm4233/MIPS-Processor-VHDL)
* [PiJoules/MIPS-processor](https://github.com/PiJoules/MIPS-processor)
* [Proje 2019 BM](https://github.com/yedhrab/IstanbulUniversity-CE/tree/ad5ffcd6c9a7d2d69f67d0a5559f092531cb8d13/3.%20Sınıf%202.%20Dönem%20Notları/Bilgisayar%20Mimarisi/Ders%20İçeriği/2019%20Proje%20Ödevi/Proje%202019%20BM.pdf)

