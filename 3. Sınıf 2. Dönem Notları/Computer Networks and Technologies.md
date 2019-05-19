# Computer Networks and Technologies <!-- omit in toc -->

- Drive üzerindeki yedeklemeye erişmek için [buraya 📂](https://drive.google.com/open?id=1rgSo9gVGWsB9WtAEfxZHv_uAdAni560a) tıklamalısın.
  - Bu metnin PDF hali **ders notum** dizinindedir.
- Dersle alternatif bir kaynak için bu [video serisine 📺](https://www.youtube.com/playlist?list=PL1XUdfGZZ4rQ0UPDx__7W4LmeLab227vb) kitap için [bu siteye 🌐](http://www-net.cs.umass.edu/kurose-ross-ppt-6e/) bakabilirsin.

> **[RFC](https://www.ietf.org/rfc/rfc2616.txt)** her şeyin olduğu bir dökümandır.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönelebilirsin.

- [Sınav Hakkında](#s%C4%B1nav-hakk%C4%B1nda)
  - [Vize Hakkında](#vize-hakk%C4%B1nda)
  - [Final Hakkında](#final-hakk%C4%B1nda)
- [Giriş](#giri%C5%9F)
  - [Temel Terimler](#temel-terimler)
  - [Network Structure (Ağ Yapısı)](#network-structure-a%C4%9F-yap%C4%B1s%C4%B1)
  - [Network Edge](#network-edge)
    - [Access Network (Bağlantı Türleri)](#access-network-ba%C4%9Flant%C4%B1-t%C3%BCrleri)
    - [Physcial Media (Fiziksel Veri İşlemleri)](#physcial-media-fiziksel-veri-i%CC%87%C5%9Flemleri)
      - [Fiber Optik Kablo](#fiber-optik-kablo)
    - [Radya Bağlantı](#radya-ba%C4%9Flant%C4%B1)
      - [Satellite (Uydu Bağlantısı)](#satellite-uydu-ba%C4%9Flant%C4%B1s%C4%B1)
  - [Network Core](#network-core)
    - [Circuit Switching (Devre Anahtarlama)](#circuit-switching-devre-anahtarlama)
    - [Packet Switching (Paket Anahtarlama)](#packet-switching-paket-anahtarlama)
    - [Packet Yönteminin Circuit Switching Yöntemine Göre Farkı](#packet-y%C3%B6nteminin-circuit-switching-y%C3%B6ntemine-g%C3%B6re-fark%C4%B1)
  - [Internet Structure (Internet Alt yapısı)](#internet-structure-internet-alt-yap%C4%B1s%C4%B1)
    - [Interter Tiers](#interter-tiers)
    - [Paketlerin iletimi](#paketlerin-iletimi)
    - [Packet Delay & Loss (Gecikme ve Kayıp)](#packet-delay--loss-gecikme-ve-kay%C4%B1p)
    - [Packet Switching Delay](#packet-switching-delay)
    - [Internet Delay](#internet-delay)
    - [Protocol Layers (Protokol Katmanları)](#protocol-layers-protokol-katmanlar%C4%B1)
    - [Internet Protocol Stack (TCP / IP)](#internet-protocol-stack-tcp--ip)
      - [ISO / OSI Reference Model](#iso--osi-reference-model)
    - [Encapsulation (Kapsülleme)](#encapsulation-kaps%C3%BClleme)
  - [Network Security](#network-security)
    - [Kötü Niyetli Uygulamalar](#k%C3%B6t%C3%BC-niyetli-uygulamalar)
      - [Trojan Horse](#trojan-horse)
      - [Worm](#worm)
      - [Virus](#virus)
      - [Spyware Malwawre](#spyware-malwawre)
    - [Kötü Niyetli Saldırılar](#k%C3%B6t%C3%BC-niyetli-sald%C4%B1r%C4%B1lar)
      - [DoS](#dos)
      - [Packet Sniffing (Paket Yakalama)](#packet-sniffing-paket-yakalama)
      - [IP Spoofing (IP Aldatmacası)](#ip-spoofing-ip-aldatmacas%C4%B1)
  - [Internetin Geçmişi](#internetin-ge%C3%A7mi%C5%9Fi)
- [Application Layer (Uygulama Katmanı)](#application-layer-uygulama-katman%C4%B1)
  - [*Network* Uygulaması Oluşturmak](#network-uygulamas%C4%B1-olu%C5%9Fturmak)
  - [Application Architectures (Uygulama Mimarileri)](#application-architectures-uygulama-mimarileri)
    - [Client-Server Architecture](#client-server-architecture)
    - [Pear-to-Pear Architecture (Kişiden kişiye Mimarisi)](#pear-to-pear-architecture-ki%C5%9Fiden-ki%C5%9Fiye-mimarisi)
    - [Client-Server ve Peer-to-Peer Karışımı](#client-server-ve-peer-to-peer-kar%C4%B1%C5%9F%C4%B1m%C4%B1)
  - [Processes Communicating (İletişim Sistemleri)](#processes-communicating-i%CC%87leti%C5%9Fim-sistemleri)
    - [Socket Yapısı](#socket-yap%C4%B1s%C4%B1)
    - [Adressing Processes (İşlemleri Adresleme)](#adressing-processes-i%CC%87%C5%9Flemleri-adresleme)
  - [Transport Service Requirements](#transport-service-requirements)
  - [Internet Transport Protocols Services (Taşıma Protokolleri Hizmetleri)](#internet-transport-protocols-services-ta%C5%9F%C4%B1ma-protokolleri-hizmetleri)
    - [TCP (Transmission Control Protocol) Review](#tcp-transmission-control-protocol-review)
    - [UDP (User Datagram Protocol) Review](#udp-user-datagram-protocol-review)
    - [Securing TCP (TCP'de Güvenlik)](#securing-tcp-tcpde-g%C3%BCvenlik)
  - [Web ve HTTP](#web-ve-http)
  - [HTTP (Hypertext Transfer Protocol)](#http-hypertext-transfer-protocol)
    - [Temel HTTP Yapısı](#temel-http-yap%C4%B1s%C4%B1)
    - [HTTP Veri Aktarımı](#http-veri-aktar%C4%B1m%C4%B1)
    - [HTTP Bağlantıları](#http-ba%C4%9Flant%C4%B1lar%C4%B1)
      - [Non-Persistent HTTP](#non-persistent-http)
      - [Persistent HTTP](#persistent-http)
    - [HTTP Request Message (İstek Mesajı)](#http-request-message-i%CC%87stek-mesaj%C4%B1)
    - [HTTP Status Code (Durum Kodları)](#http-status-code-durum-kodlar%C4%B1)
    - [Cookie (Çerezler)](#cookie-%C3%A7erezler)
    - [Proxy Server & Cache](#proxy-server--cache)
      - [Conditional GET (Koşullu GET)](#conditional-get-ko%C5%9Fullu-get)
  - [Domain Name System (DNS)](#domain-name-system-dns)
    - [DNS Resolution Examples (DNS Çözümleme Örnekleri)](#dns-resolution-examples-dns-%C3%A7%C3%B6z%C3%BCmleme-%C3%B6rnekleri)
    - [DNS Record (DNS Kayıtları)](#dns-record-dns-kay%C4%B1tlar%C4%B1)
      - [Inserting DNS Record](#inserting-dns-record)
      - [Attacking DNS](#attacking-dns)
  - [P2P (Peer to Peer)](#p2p-peer-to-peer)
    - [P2p File Distribution (Dosya Paylaşımı)](#p2p-file-distribution-dosya-payla%C5%9F%C4%B1m%C4%B1)
  - [Video Streaming and CDNs: context](#video-streaming-and-cdns-context)
    - [Video Streamin](#video-streamin)
    - [Content Distribution Networks (İçerik Dağıtım Ağları)](#content-distribution-networks-i%CC%87%C3%A7erik-da%C4%9F%C4%B1t%C4%B1m-a%C4%9Flar%C4%B1)
- [Transport Layer](#transport-layer)
  - [Internet Transport Layer Protocols](#internet-transport-layer-protocols)
  - [Multiplexing (Çoğullama)](#multiplexing-%C3%A7o%C4%9Fullama)
  - [Demultiplexing (Azaltma / Parçalama)](#demultiplexing-azaltma--par%C3%A7alama)
    - [TCP / UDP Demux](#tcp--udp-demux)
    - [TCP / UDP Demux Examples](#tcp--udp-demux-examples)
  - [UDP (User Datagram Protocol)](#udp-user-datagram-protocol)
    - [UDP Checksum](#udp-checksum)
  - [Reliable Data Transfer (RDT)](#reliable-data-transfer-rdt)
    - [Rdt 1.0](#rdt-10)
    - [Rdt 2.0](#rdt-20)
      - [Rdt 2.0 Kusurları](#rdt-20-kusurlar%C4%B1)
    - [Rdt 2.1](#rdt-21)
    - [Rdt 2.2](#rdt-22)
    - [Rdt 3.0](#rdt-30)
  - [Pipelined Protocols](#pipelined-protocols)
  - [TCP (Transmission Control Protocol)](#tcp-transmission-control-protocol)
- [Network Layer](#network-layer)
  - [Forward & Route](#forward--route)
  - [Network Layer Service Models](#network-layer-service-models)
  - [Router Mimarisi](#router-mimarisi)
    - [Import Port Function](#import-port-function)
    - [Switching Fabric](#switching-fabric)
    - [Input & Output Queuing](#input--output-queuing)
  - [The Internet Network Layer](#the-internet-network-layer)
    - [IP Protocol](#ip-protocol)
    - [IP Adressing](#ip-adressing)
    - [Subnet (Alt ağlar)](#subnet-alt-a%C4%9Flar)
    - [CIDR (Classless InterDomain Routing)](#cidr-classless-interdomain-routing)
    - [DHCP (Dynamic Host Configuration Protocol)](#dhcp-dynamic-host-configuration-protocol)
    - [DHCP Client-Server Senaryasu](#dhcp-client-server-senaryasu)
    - [ISP Adresleme](#isp-adresleme)
    - [ISP Adressleme Hiyerarşisi](#isp-adressleme-hiyerar%C5%9Fisi)
    - [NAT (Network Adress Translation)](#nat-network-adress-translation)
- [Hauwei Dersi](#hauwei-dersi)
  - [Yazılım Notları](#yaz%C4%B1l%C4%B1m-notlar%C4%B1)
  - [Temel Kavramlar](#temel-kavramlar)
    - [SubnetMask Host ve Bit Hesaplamaları](#subnetmask-host-ve-bit-hesaplamalar%C4%B1)
    - [IPv4 Classes](#ipv4-classes)
  - [Layer Özellikleri](#layer-%C3%B6zellikleri)
  - [*MAC* varken Neden *IP* Adresi Var](#mac-varken-neden-ip-adresi-var)
  - [Static Route](#static-route)
  - [RIP - Routing Information Protocol](#rip---routing-information-protocol)
    - [RIP-2 Özellikleri](#rip-2-%C3%B6zellikleri)
    - [RIP-2 Örneği](#rip-2-%C3%B6rne%C4%9Fi)
  - [OSPF Open Shortest Part First](#ospf-open-shortest-part-first)
    - [OSPF Package Types](#ospf-package-types)
  - [BGP](#bgp)
  - [Comparing Protocol](#comparing-protocol)
  - [Collision & Broadcast Domain](#collision--broadcast-domain)
  - [TCP / IP Model](#tcp--ip-model)
    - [TCP Transmission Types](#tcp-transmission-types)
  - [Virtual LAN (VLAN)](#virtual-lan-vlan)
    - [VLAN Avantajları](#vlan-avantajlar%C4%B1)
  - [Spanning Tree Protocol (STP)](#spanning-tree-protocol-stp)
    - [STP Port State](#stp-port-state)
  - [Sınav Soruları](#s%C4%B1nav-sorular%C4%B1)
- [Lisans ve Teferruatlar](#lisans-ve-teferruatlar)

## Sınav Hakkında

### Vize Hakkında

- 1, 2, 3, 4.1, 4.2 numaralı *Chapter*'lardan sorumluyuz
- Sınav formatı karışıktır.
- 2.3 ve 2.7 dahil değildir

> **Network Layer**'a kadar olan kısım vize için notlarımdır

### Final Hakkında

Final sınavı konu kapsamı:

- Chapter 4
  - Kendi notlarım **Network Layer** adı altındadır
- HUAWEI-WEEK1, HUAWEI-WEEK2, HUAWEI-WEEK3
  - **Huawei dersi** adı altındadır

> **Network Layer** ve sonrası final için notlarımdır

## Giriş

### Temel Terimler

| Terim             | Açıklama                                                       |
| ----------------- | -------------------------------------------------------------- |
| ISP               | İnternet servis sağlayıcıları                                  |
| Packets           | İnternet üzerinde gönderilen veriler                           |
| Protocols         | *Packet* aktarım kuralları ve hiyerarşisi                      |
| Routers ve Switch | *Packet*'ların yönlendirilmesini sağlarlar                     |
| Client            | Ağa bağlandığımzı araç (bilgisayarımız)                        |
| Server            | Ağ hizmetini sunan, sunucu                                     |
| Host              | End system, son *server* ya da *client*                        |
| RFS, IETF         | İnternet standartları                                          |
| Stream            | Veri akışı                                                     |
| Upstream          | Bizden internete *stream*                                      |
| Downstream        | İnternetten bize *stream*                                      |
| Bandwitdh         | Bant genişliği, saniye aktarılan bit (1sn de olan *streaming*) |
| Transmission rate | Saniyede aktarılan bit                                         |

### Network Structure (Ağ Yapısı)

| Terim                           | Açıklama                                                    |
| ------------------------------- | ----------------------------------------------------------- |
| Network Edge                    | Ağdaki uç noktaları ele alır (bilgisayarlar ve uygulamalar) |
| Access networks, physical media | Kablolu ve kablosuz iletişim bağlantıları                   |
| Network Core                    | Birbirine bağlı router'lar ve internet (network of network) |

- Edge router: İnternete ilk adımın atıldığı yönlendiriciler (routers)

![network sturcture](../res/network%20structures.png)

### Network Edge

Bizden internete olan gerçekleşen adımları ele alır.

| Yöntem          | Açıklama                                          | Örnek             |
| --------------- | ------------------------------------------------- | ----------------- |
| Hosts System    | *Host*'lar arası iletişim                         | Web, email        |
| Client / Server | *Client* istekte bulunur, *server* karşılık verir | Web browsers      |
| Peer to peer    | Neredeyse hiç *server* kullanılmaz                | Skype, BitTorrent |

#### Access Network (Bağlantı Türleri)

- Dial Up: Telefon çalışırken modem, modem çalışırken telefonun çalışmadığı eski bir sistem.
- DSL: *Splitter* ile telefon ve internet eş zamanlı kullanabilmekte.
  - ADSL: Asimetrik anlamındadır, download ve upload hızı farklı olur.
- Wireless LAN: Ev içerisindeki kablasuz ağlar: WiFi
- Wide-Area wireless acces: Mobil operatörler tarafından sunulan ağlar: 3G, 4G, LTE

#### Physcial Media (Fiziksel Veri İşlemleri)

Fiziksel verilerin (*bit*'lerin) aktarılmasını ele alır.

- Kablo yapısı TP (twisted pair) iç içe sarmal 2 kablodur.
- Guided: yönetimli (kablo vs ile), unguided: dağınık olarak yayılan (radyo dalgaları) verilerdir.

##### Fiber Optik Kablo

- Cam içerisinde bilgiler ışık yoluyla aktarılır
- Işığın farklı frekanslarıyla birden fazla bilgi yollanabilir
- Işık hızıyla iletilir
- Elektromanyetik gürültüden etkilenmez
- Veri kaybı çok düşüktür

#### Radya Bağlantı

- LAN (WiFi)
- Wide-area (geniş alan bağlantıları) 3G, 4G

##### Satellite (Uydu Bağlantısı)

- Gecikmesi çok fazladır. (250ms)

### Network Core

Birbirine bağlı çok sayıda *router*'dan oluşur. Network of network olarak da tabir edilen interneti ele alır.

![network_core](../res/network_core.png)

| Aktarım Yöntemi   | Açıklama                                               |
| ----------------- | ------------------------------------------------------ |
| Circuit Switching | Her arama için özel devre kullanılır, telefon ağı gibi |
| Packet Switching  | Veri ağa ayrık *packet*'lar halinde gönderilir         |

#### Circuit Switching (Devre Anahtarlama)

*Bandwitdh* parçalara bölünür, her parça sadece kendi sahibi tarafından kullanılır.

- Genellikle telefon hatlarında kullanılır
- Garantili performans sunar
- Kaynaklar paylaşılmaz, kullanılmayanlar boşta bekler (verimsiz)
- Frekans ve Zaman bölme olarak iki yöntemi vardır. (FDM, TDM)

![fdm_tdm](../res/fdm_tdm.png)

#### Packet Switching (Paket Anahtarlama)

*Hostlar* çok yüksek miktarda gelen veriyi parçalayarak yollarlar, her bir parçaya **packets** denir. Her bir *packet* tam *bandwitdh* kullanır ve host tarafından **tamamlanmadan** yollanmaz (storage & forward).

- *Packet*'ların bir sırası yoktur
- Her bilgisayar *packet* iletimi için aynı yolu kullanır
- Kaynaklar boşta kalmaz. (verimli)
- Her bir *packet* $L$ kadar bit içeriyor ve *transmission rate* $R$ ise transmission delay $D=L/R$ formülü ile bulunur
- Kaynak çekişmesi olabilir. (olumsuz)
  - Toplamk kaynak talebi kullanılanı aşabilir
  - Trafik sıkışıklığı, *packet*'in kuyruğu ve bağlatıyı kullanmak için beklemesi
  - *Packet*'lar aynı anda bir yönlendiriciye iletirilir
    - Buffer'ı yetmezse *packet* kaybı olur

![packet_switching](../res/packet_switching.png)

#### Packet Yönteminin Circuit Switching Yöntemine Göre Farkı

- Basit, arama algoritmalarının kurulmaına gerek yoktur
- Kaynaklar paylaşıldığından ağı daha fazla kullanıcı kullanabilir
- Güvenilir veri transferi ve sıkışıklık için protokellere ihtiyaç vardır.
  - Yoksa verilerinizi çalarlar 🙁

### Internet Structure (Internet Alt yapısı)

#### Interter Tiers

Her bir katman üst katmanının müşterisidir.

| Tier (Katman) | Açıklama                                                                                        |
| ------------- | ----------------------------------------------------------------------------------------------- |
| *Tier-1*      | Global *ISP* evrensel servis sağlayıcılarıdır. Birbirlerine bağlıdırlar Örn: Superonline, TTNet |
| *Tier-2*      | Regional *ISP* bölgesel servis sağlayıcılarıdır. Birbirlerine değil *Tier-1*'e bağlıdırlar      |
| *Tier-3*      | Son kullanıcı ağlarıdır, *Tier-2*'e bağlanırlar                                                 |

![isps](../res/ısps.png)

#### Paketlerin iletimi

Paketler *tier-3*'ten *tier-1*'e ardından hedef *tier-3*'e doğru yol izlerler.

![packet_forwarding](../res/packet_forwarding.png)

- *Router*'lar arası verilerin yayıldığı alana **pipe** denir
- Kalın bağlantılarda (links) veri aktarımı daha fazladır
- Ince alanlara **bottleneck link** denir

![throughput](../res/throughput.png)

#### Packet Delay & Loss (Gecikme ve Kayıp)

*Packet*'lar *router*'ın *buffer* (arrabellek) alanında kuytukta beklerler

- Gelen *packet* sayısı çıkandan fazla ise fazlalık *packet*'lar *buffer*'a konulur
- *Buffer* yeterli alana sahip değilse *packet* atılır, kayıp *packet*'lar önceki *node*'dan tekrar istenir

![packet_loss](../res/packet_loss_delay.png)

#### Packet Switching Delay

| Olay              | Açıklama                                          |
| ----------------- | ------------------------------------------------- |
| Nodel Processing  | Hatalı bitlerin kontrol edildiği aşama            |
| Queueing Delay    | *Buffer*'da sıralanmanın olduğu aşama             |
| Transmisson Delay | Yayılım için *packet*'ların *router*'a iletilmesi |
| Propagation Delay | *Router*'daki paketlerin yayılması                |

![caravan_analogy](../res/caravan_analogy.png)
![caravan_analogy2](../res/caravan_analogy2.png)

#### Internet Delay

Traceroute programı kaynaktan hedefe yol üzerinde bulunan *router*'lardaki gecikmenin ölçümünü sağlar.

- Windows için tracert
- Linux için tracepath

![tracepath](../res/tracepath.png)

#### Protocol Layers (Protokol Katmanları)

Ağ yapıları karmaşıktır. Bilgisayarlar, *routers*, *protocols* ... Katman yapısıyla:

- Karmaşık sistem parçalarının ilişkilerini tanımlamaya olanak sağlar
- Modüler olması sistemin bakımını ve güncelleştirilmesini kolaylaştırır
  - Bir katmandaki servis uygulamasını değiştirmek, sistemi etkilemez

#### Internet Protocol Stack (TCP / IP)

| Öge         | Açıklama                                                                   |
| ----------- | -------------------------------------------------------------------------- |
| application | Ağ uygulamalarını destekleyen uygulamalar                                  |
| transport   | Veri aktarımı, TCP, UDP                                                    |
| network     | Kaynaktan hedefe *datagram*'ları yönlendirir: IP, yönlendirme protokolleri |
| link        | Komşu ağ elemanları arasında veri transferi: PPP, Ethernet                 |
| physical    | Hattaki bitler (*bits in wire*)                                            |

![ips](../res/ips.png)

##### ISO / OSI Reference Model

Internet protocol *stack*'te bu katmanlar yoktur, gerekirse program ile uygulanır

| Ek Öğe       | Açıklama                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------- |
| presentation | Uygulamaların verilerin anlamlarını yorumlamasını sağlar: *encryption*, *compression* ... |
| session      | Senkronizasyon, denetim veri değişimi ...                                                 |

![iso_osi](../res/iso_osi.png)

#### Encapsulation (Kapsülleme)

Veri transferleri *encapsulation* ile yapılmaktadır.

![encopsulation](../res/encapsulation.png)

### Network Security

Hiçbir *protocol* güvenlik tedbirleri barındırmaz. 📛

#### Kötü Niyetli Uygulamalar

##### Trojan Horse

Faydalı yazılımların gizli bir parçasıdır, web sayfalarında bulunur. (Acitve-x, plugin)

##### Worm

Pasif olarak alınan nesnenin kendini çalıştırması ile bulaşır, çoğalır diğer bilgisayarlara da yayılır.

##### Virus

Alınan nesne ile bulaşır (e-posta). Nesne açıldığında *virus* bulaşır, çoğalır diğer bilgisayarlara da yayılır.

##### Spyware Malwawre

Casus yazılımlar olarak da bilinir. Klavye tuş basımlarını ve girdiğimiz web sitelerinin bilgilerini çalar.

#### Kötü Niyetli Saldırılar

##### DoS

Denial of service olarak da bilinir. Saldırganların kaynağa çok fazla *packet* göndererek erişim dışı bırakmasıdır.

![dos](../res/dos.png)

##### Packet Sniffing (Paket Yakalama)

Yerel ağa bağlı bir ağ kartından *Wireshark* uygulaması ile başka *packet*'lar de yakalanır.

![packet_sniffing](../res/packet_sniffing.png)

##### IP Spoofing (IP Aldatmacası)

Yanlış IP adresiyle *packet* gönderilir

![ip_spoofing](../res/ip_spoofing.png)

### Internetin Geçmişi

[Buradaki](https://drive.google.com/drive/folders/1d3JzZlHNYqeE3RryDVdAyHKTSmSykjGt) slaytın 62. sayfasına bakarak erişebilirsin.

<!-- TODO -->

## Application Layer (Uygulama Katmanı)

![network_apps](../res/network_apps.png)

### *Network* Uygulaması Oluşturmak

Farkı *end systems* (son kullanıcı sistemleri) üzeründe  çalıştırılır. Örneğin, web server yazılımı ağ üzerinden web browser yazılımı ile bağlantı kurar

> Temel ağ cihazları, kullanıcı programlarını çalıştırmaz. 😔

### Application Architectures (Uygulama Mimarileri)

2 farklı yapı kullanılmaktadır; client-server, peer-to-peer (P2P)

#### Client-Server Architecture

Server Özellikleri:

- Her zaman açık
- *Static IP* (değişmeyen, kalıcı IP)

*Client* özellikleri:

- Belirlenen zamanlarda *server* ile iletişim kurabilirler
- *Dynamic IP*
- Birbiri ile iletişim kuramazlar

#### Pear-to-Pear Architecture (Kişiden kişiye Mimarisi)

- *Server* her zaman açık değildir
- Rastgele *end system*'lerle doğrudan iletişim olur (arada *server* olmaz)
- Bilgisayarlar zaman zaman bağlanabilir ve *dynamic IP* kullanabilirler

> Yönetmesi oldukça zordur.

#### Client-Server ve Peer-to-Peer Karışımı

![client_p2p](../res/client-p2p.png)

### Processes Communicating (İletişim Sistemleri)

| İşlem          | Açıklama                                              |
| -------------- | ----------------------------------------------------- |
| Process        | Bir bilgisayarda çalışan programlar, yapılan işlemler |
| Client Process | İletişimi başlatan *process*'ler                      |
| Server Process | Bağlantıyı bekleyen *process*'ler                     |

#### Socket Yapısı

*IP* adresi ve *port* numarasından oluşan, *process*'lerin alınıp / verildiği kısma **socket** adı verilir.

- *Client*, *process*'i kapının dışına koyar.
- *Server*, *process*'i kapıdan içeri alır
- Buradaki kapı olarak adlandırılan *socket*'tir

#### Adressing Processes (İşlemleri Adresleme)

Mesajların alınması için *process*'in bir tanımlayıcısı (*identifier*) olması gerekmektedir. 0 ile 1023 arası *well-known ports* olarak bilinmektedir. Tanımlayıcı:

- *IP* adresi, örn: 128.119.245.12
- *Port* numarası, örn: 80

içerir.

Örnek *port* numaraları:

- *HTTP* server: 80
- *Mail* server: 25

> Windows için `ipconfig`, linux için `ifconfig` ile IP adresinizi öğrenebilirsiniz.

### Transport Service Requirements

| Özellik        | Açıklama                                                                         |
| -------------- | -------------------------------------------------------------------------------- |
| Data Integrity | Metin aktarımlarında çok önemlidir, ses gibi verilerim aktarılmasında önemsizdir |
| Timing         | Ses aktarımlarında gecikmenin en az olması gereklidir.                           |
| Throughput     | Multimedya uygulamaları etkili olmak için daha az veri kullanmayı tercihi eder   |
| Security       | Şifreleme ve verinin değiştirilmemesini ele alır                                 |

![trans_services](../res/trans_services.png)

### Internet Transport Protocols Services (Taşıma Protokolleri Hizmetleri)

*Protocol*'lerin hiç biri alttaki özellikleri taşımaz, sonradan bunlara uygun sistemler oluşturulur ve entegre edilir.

- Timing (düşük gecikme)
- Min throughput (düşük veri aktarımı)
- Guarantee (garantili taşıma)
- Security (güvenli taşıma)
  - Şifreleme (*enctryption*) içermez
  - Socket ve internet verileri olduğu gibi (*cleartext*) gönderilir.

![tcp_udp_segment_format](../res/tcp_udp_segment_format.png)

#### TCP (Transmission Control Protocol) Review

| Özellik            | Açıklama                                             |
| ------------------ | ---------------------------------------------------- |
| Reliable transport | Güvenilir veri aktarımı                              |
| Flow control       | Veri akışı denetimi                                  |
| Congestion control | *Network* aşırı yoğun olduğunda veri akışını azaltır |

> Detayları *transport layer* altında işlenmekte, [buraya](#tcp-transmission-control-protocol) tıklayarak gidebilirsin.

#### UDP (User Datagram Protocol) Review

UDP yayıncılıkta tercih edilen bir *protocol*'dür. Amacı tamamıyla hızı arttırmak ve maaliyeti düşürmektir.

- *Packet*'in varıp, varmadığıyla ve güvenliğiyle ilgilenmez (*Unreliable transport*), varmazsa tekrar gönderir.
- Tıkanıklık kontrolüne (*congestion control*) ihtiyaç yoktur, olabildiğince hızlı gönderir
- Bağlantı kurmaya gerek yok, zaman kaybına neden olur
- Basitir, *sender* ve *reciver* asla birbiriyle iletişimde değildiir
- Olumsuz geri dönüş yoktur.

> Detayları *transport layer* altında işlenmekte, [buraya](#udp-user-datagram-protocol) tıklayarak gidebilirsin.

#### Securing TCP (TCP'de Güvenlik)

TCP'de güvenlik SSL ile sağlanır, uygulamalar **SSL kütüphanesi** yardımıyla TCP ile etkileşir. SSL'in sağladıkları:

- Şifreli (*encreypted*) TCP bağlantısı
- Veri bütunlüğü (*data integrity*)
- Uç sistem doğrulaması (*end-point authentication*)

### Web ve HTTP

- Web sayfası *base HTML* dosyasının referans ettiği objelerden oluşur.
- Web sayfaları objelerden oluşur, bu dosyalar; HTML, JPEG, JAVA applet vs. olabilir.
- Her obje *URL*'ler ile adreslenir.

![url_ex](../res/url_ex.png)

### HTTP (Hypertext Transfer Protocol)

#### Temel HTTP Yapısı

*Applicataion Layer* (uygulama katmanı) *protocol*'üdür.

![http_overview](../res/http_overview.png)

- *Client*: Tarayıcılar, *Server*: Apache Web Server

#### HTTP Veri Aktarımı

HTTP, TCP kullanır.

- *Client* TCP bağlantısını başlatır.
  - *Server*'a 80 *port*'unda *socket* oluşturur
- *Server* TCP bağlantısını kabul eder
- *Client* ve *Server* arasında HTTP mesajları aktarılır
- TCP bağlantısı kapatılır

> HTTP *stateless* (durumsuz) olarak tanımlanır. Eski istekler (*requests*) hakkında bilgi sahibi değildir.

#### HTTP Bağlantıları

| Bağlantı Türü                   | Açıklama                                                               |
| ------------------------------- | ---------------------------------------------------------------------- |
| non-persistent (kalıcı olmayan) | En fazla bir obje TCP üzerinden gönderilir ardından bağlantı kapatılır |
| persistent (kalıcı)             | Çok sayıda obje TCP üzerinden gönderilebilir                           |

> **RTT**, bir *packet*'in *client-server* arasında gidiş geliş süresi

##### Non-Persistent HTTP

Sunucuyu her defasında açmak için *RTT* kaybı yaşanacaktır, tek bir veri alınacaksa ideal seçimdir

![non_persistend_http](../res/non_persistent_http.png)

##### Persistent HTTP

- Sunucu tek bir seferde açılacak lakin kapatılmak için *request* bekleyecektir, bu da fazladan *RTT* kaybı demektir.

#### HTTP Request Message (İstek Mesajı)

![http_request](../res/http_request.png)

- `sp`: Boşluk
- `cr`: \r karakteri
- `lf`: \n, satır sonu karakteri

![http_request_ex](../res/http_request_ex.png)

#### HTTP Status Code (Durum Kodları)

| Status Code | Açıklama                   |
| ----------- | -------------------------- |
| 200         | OK                         |
| 301         | Moved Permanently          |
| 400         | Bad Request                |
| 404         | Not Found                  |
| 505         | HTTP Version not Supported |

#### Cookie (Çerezler)

Bir websitesine ilk kez girdiğimizde bilgilerimiz **cookie** adıyla *server* veri tabanında saklanır.

> Web siteleri kişisel bilgilerimizi saklarlar. 😕

![cookie_ex](../res/cookie_ex.png)

#### Proxy Server & Cache

*Client* isteklerini *server* ile uzun süren bağlantılardan kaçınarak hızlıca halletmeyi amaçlar. Belli başlı *server*'lar *cache*'e atılır ve *server*'a istek yollamak yerine yerel ağdaki *proxy server*'a istek yollanarak çok hızlıca işlem halledilir.

> *LAN* (yerel ağ) diğer *network*'lere kıyasla çok hızlıdır.

![proxy_ex](../res/proxy_ex.png)

##### Conditional GET (Koşullu GET)

Bu yöntemler *Proxy server* önbelleğinde (*cache*) bulunan verilerin güncel olup olmadığı sorgulanır.

![conditional_get](../res/conditional_get.png)

### Domain Name System (DNS)

Internette adresler IP (192.168.1.1) ile tanımlanır. DNS'ler ile IP'lere isimler (google.com) atanır.

> DNS eşleştirilmesi yapıldığında *Local DNS*'de *cache*'e alınır, bundan dolayı TLD sık kullanılmaz.

| DNS Türü      | Açıklama                                                                            |
| ------------- | ----------------------------------------------------------------------------------- |
| Local         | DNS hiyerarşisine ait değildir, her istek ilk burada eşleştirilmeye çalışılır       |
| Root          | Yerel (*local*) DNS sunucularının çözemedikleri isimler için buraya danışılır       |
| TLD           | Top-level domain, *com, org, net, tr ...* gibi ülke etki alanlarından sorumludurlar |
| Authoritative | Yetkili isim sunucuları, kurumlardaki sunucuların isimlerini eşleştirir             |

![dns_hierarchy](../res/dns_hierarchy.png)

#### DNS Resolution Examples (DNS Çözümleme Örnekleri)

![dns_resolution_ex1](../res/dns_resolution_ex1.png)
![dns_resolution_ex2](../res/dns_resolution_ex2.png)

#### DNS Record (DNS Kayıtları)

Kayıtların formatı `(name, value, type, ttl)` şeklindedir.

| Type  | Açıklama                                     |
| ----- | -------------------------------------------- |
| A     | `name`: hostname, `value`: IP                |
| NS    | `name`: domain, `value`: hostname            |
| CNAME | `name`: takma isim, `value`: domain          |
| MX    | name: alakalı isim, value: *mailserver* ismi |

##### Inserting DNS Record

- DNS *server* ismi ve IP adersi belirlenir
- TLD *Server*'lara alttaki şekilde kayıt edilir

```sh
(dns1.manolyatekstil.com, 212.212.212.1, A)
(manolyatekstil.com, dns1.manolyatekstil.com, NS) # Nameserver
```

##### Attacking DNS

![attacking_dns](../res/attacking_dns.png)

### P2P (Peer to Peer)

![p2p_scheme](../res/p2p_schema.png)

- *Server* *torrent*'e katılanları izler ve her zaman açık olmaz
- *Network*'teki bilgisayarlar rastgele erişim kurarlar
- Eş bilgisayarlar zaman zaman bağlantı kurarlar ve IP adresleri değişebilir

| Terim   | Açıklama                       |
| ------- | ------------------------------ |
| Chunk   | 256KB'lik *packet*'lar         |
| Torrent | *Chunk* alışveriişi yapan grup |

#### P2p File Distribution (Dosya Paylaşımı)

Hızlı veri aktarımı sağlayan bir yapıdır.

![p2p_client_graph](../res/p2p_client_graph.png)

- *Chunk*'lar indirilirken aynı zamanda karşıya da yüklenir
- Çok yükleme yapan çok hızlı indirir
- İsteğe bağlı yükleme veya indirme iptal edilebilir

### Video Streaming and CDNs: context

#### Video Streamin

Her video, resin topluluğundan ver resimler de *pixel*'lerden oluşur. Her *pixel* de *bit*'lerden oluşmakta ve bunların aktarımları gerçekleşmektedir. *Bit* sayısını azaltmak için;

| Yöntem               | Açıklama                                                             |
| -------------------- | -------------------------------------------------------------------- |
| spatial (uzaysal)    | N tane renk göndermek yerine, rengi ve tekrar etme sayısını gönderir |
| Temportal (zamansal) | Sadece bir önceki resim ile farklı olaran yerleri gönderir           |

#### Content Distribution Networks (İçerik Dağıtım Ağları)

İçerikler kopyalanarak birden fazla *server*'dan akatarılır.

![netflix_structure](../res/netflix_structure.png)

## Transport Layer

*Network layer*, *host*'lar arası mantıksal iletişimi sağlarken; *transport layer*, ***process***'ler arası mantıksal iletişimi sağlar

![transport_layer](../res/transport_layer.png)

### Internet Transport Layer Protocols

Yine, [UDP](#udp-user-datagram-protocol) ve [TCP](#tcp-transmission-control-protocol) protocolleri kullanılır. 😉

### Multiplexing (Çoğullama)

| Multiplexing Yeri   | Açıklama                                                                              |
| ------------------- | ------------------------------------------------------------------------------------- |
| Gönderen bilgisayar | Birden çok *socket*'ten verileri toplar, başlık ekliyerek **segment** haline getirir. |
| Alıcı bilgisayar    | Alınan *segment*'leri doğru *socket*'e teslim eder                                    |

![multiplexing_transport_layer](../res/multiplexing_transport_layer.png)

### Demultiplexing (Azaltma / Parçalama)

- Bilgisayarlardan IP *datagram*'ları alınır.
  - *Datagram*'larda *source IP* ve *dest IP* vardır
  - Her *datagram* bir *segment* taşır
  - Her *segment*'in kaynak ve *dest port* numaları vardır

#### TCP / UDP Demux

UDP'de yönlendirme:

- *Source IP*
- *Destination port* numarası

TCP'de yönlendirme:

- *Source IP*
- *Destination IP*
- *Source port* numarası
- *Destination port* numarası

ile olmaktadır.

> *Socket*, *source IP* ve *destination port* numarasından oluşur.

#### TCP / UDP Demux Examples

UDP Demux:

![udp_demux](../res/udp_demux.png)

TCP Demux:

![tcp_demux](../res/tcp_demux.png)

### UDP (User Datagram Protocol)

UDP yayıncılıkta tercih edilen bir *protocol*'dür. Amacı tamamıyla hızı arttırmak ve maaliyeti düşürmektir.

- *Packet*'in varıp, varmadığıyla ve güvenliğiyle ilgilenmez (*Unreliable transport*), varmazsa tekrar gönderir.
- Tıkanıklık kontrolüne (*congestion control*) ihtiyaç yoktur, olabildiğince hızlı gönderir
- Bağlantı kurmaya gerek yok, zaman kaybına neden olur
- Basitir, *sender* ve *reciver* asla birbiriyle iletişimde değildiir
- Olumsuz geri dönüş yoktur.

![udp_segment](../res/udp_segment.png)

#### UDP Checksum

Aktarılan *segment*'deki hataları algılamak için kullanılan yöntemdir.

![udp_checksum](../res/udp_checksum.png)

### Reliable Data Transfer (RDT)

#### Rdt 1.0

Tam güvenlikli bir kanaldır.

- *Bit* ve *packet* kayıpları yoktur
- *Sender* ve *reciver* verileri güvenli kanaldan (*underlying channel*) alır

#### Rdt 2.0

Bitlerde hatalar söz konusu olabilir.

- *Bit* hataları *checksum* ile algılanır.
- *Acknowledgements (ACKs)* paket alındı bilgisi, *negative acknowledgements (NAKs)* paketin hatalı olduğu bilgisi gibi *feedback*'ler vardır.

##### Rdt 2.0 Kusurları

- ACK / NAK mesajları bozulması durumunda geçerli *packet* yeniden gönderilir
- *Sender* her gelen *packet*'e *segment* numarası ekler, birden fazla gelen *packet*'ları *reciever* atar
- *Sender* bir *packet* gönderdikten sonra *feedback* için bekler, bu da zamandan kayıp demektir.

#### Rdt 2.1

*Sender*:

- *Packet*'lara *segment* numarası ekler.
- ACK / NAK bozuk alınıp alınmadığını kontrol eder

*Reciever*:

- Alınan *packet*'ların eşsiz olup olmadığını kontrol eder
- ACK / NAK mesajlarının *sender* tarafından alınıp alınmadığını bilmez

#### Rdt 2.2

NAK içermez, sadece ACK kullanarak rdt 2.1 ile aynı görevi yapar.

- NAK yerine *packet* başarılı alındığında ACK mesajları gönderilir.
- Çift ACK mesajı NAK gibi kabul edilir, *packet* yeniden gönderilir.

#### Rdt 3.0

Rdt 2.2'ye ek olarak:

- *Sender* belli sürede ACK mesajı almazsa (*timeout*) *packet* yeniden gönderilir.
- Eşsiz olmayan *packet*'lar *segment* numaraları ile ayırt edilir.

![rdt_3.0](../res/rdt_3.0.png)

### Pipelined Protocols

Bir *packet* göndermek yerine birden fazla gönderilir.

- *Reciver* aldığı her sağlam *packet* için *ack* gönderir
  - Hatalı *packet*'ler için *ack* gitmez
  - Kaçırılan paketler için en son gönderilen *ack* gönderilir
- Tekrar eden *ack*'lar *sender* tarafından görmezden gelinir ve *packet* yeniden gönderilir
  - Bu yapıya **Go back N (GDN)** adı verilir.

> Selective repeat ?

![pipeline_gbn](../res/pipeline_gbn.png)

### TCP (Transmission Control Protocol)

> Sıkıldım 😓

<div class="page"/>

## Network Layer

- Veriler segment
- Application data
- Network katmanına geçerken bilgi datagram olarak devam ediyor
- Router'larda network katmanından sonrakiler var network dahil
- Transport katmanında TCP / UDP, ağ katmanında IP protokolleri uygulanır

### Forward & Route

- Routung, 2 route arası aktarma
- Routing, kaynaktan asıl hedefe iletişim algoritması. Bir sürü forward
- Tablonun genel adı *control plane*'dir
- Forward işlemlerindeki router'lardaki control pane kullanılır, her bir route'un control pane'i bitlere karşılık hedef bilgisi taşır
- Remote Controller ile tablolar manuel olarak dolduruluyor (?)

### Network Layer Service Models

- İnternet hız sunuyor, güvenlik değil. Güvenlik işlemlerini application katmanında yapıyor (Best efford)
- ATM güvenilik sağlayabilyor (4-9 sayfa 5)

<div class="page"/>

### Router Mimarisi

Yönlendircinin 2 görevi vardır:

- Yönlendirme algoritmaları ve protocol'lerin (RIP, OSPF, BGP) çalıştırılması
- Datagram'ları gelen porttan giden port'a yönlendirilmesi
- Datagram'lar hedefe *Control Panel* tablosuyla yönlendirilir

#### Import Port Function

| Import Port Function         | Açıklama |
| ---------------------------- | -------- |
| Destination-Based Forwarding | 7        |
| Longest Prefix Mathcing      | 8        |

#### Switching Fabric

| Switching Fabric | Açıklama                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Memory           | Eski düzen, yavaş                                                                          |
| Bus              | Paket kaybı olabiliyor, kurumsal ağlar için uygundur                                       |
| Crossbar         | Datagramlar parçalanıyor, parçalar işlemciler üzerinde birleştiriliyor, en hızlı yöntemdir |

#### Input & Output Queuing

- *Queue delay* ve *buffer*'ın dolu olmasından dolayı kayıp olur (Output)
  - $(RTT.C) / \sqrt{N}$
- Gecikme ve giriş buffer'ında yer kalmaz ise kayıp oluşabilir (Input)
  - Head of the Line (HOL)
- Scheduling mechanisims
  - *FIFO* first in first out
  - *Priority schedulung*, en az bekleyeceği yere yönlendirir
  - *Round Rubin (RR)*, boyutu az olanı önce işleme sokma
  - *Weighted Fair Queuing (WFQ)*, RR'ın genelleştirilmiş hali
    - Büyük paketleri parçalasyarak adil miktarda alır ve gönderir

<div class="page"/>

### The Internet Network Layer

- Segment (TCP; UDP)
- Datagram (IP, ROUTE vs)
- Frame (link layer)

#### IP Protocol

- IPv4 = 4byte (32 bit)
- IPv6 = 16byte (128 bit)
- Büyük IP datagramları ağ içlerinde parçalanıp (*fragmentation*) yollanır, son hedefte (*final destination*) da işlemcide birleştirilir (*reassambled*)
  - Üst bilgi uzunluğu $Head = 20$bit
  - Bölünme varsa $fragflag = 1$
  - $Offset = (length - Head) / 8$

#### IP Adressing

- IP Adresleri kablonun (switch, router) adresidir, PC'nin değil
- Her bir bağlantı *interface* olarak tanımalanır (253.1.1.1)
- IPv4 32 bittir, uzun olduğunda 4x8bit olarak parçalanır (x.x.x.x)

#### Subnet (Alt ağlar)

- IP'lerin ortak kısmı yazılır, değişken kısmı $0$ olarak gösterilir
- 223.1.1.1, 223.1.1.4 vs. için 223.1.1.0 *subnet*'i kullanılır
  - IP'in sol kısmı 223.1.1 **subnet**, sağ kısmı **host** bölümüdür
  - 223.1.3.0 / 24 değerinden 24 kısmı subnet için ayrılan biti (*subnet mask*) temsil eder
  - Sadece *host* arası değil *router* arasında da *subnet* olur
- Subnet'ler birbiri ile iletişimde değildir (*isolated*)

#### CIDR (Classless InterDomain Routing)

- Özel bir class yapısı yoktur
- Kendimize ait *subnet* ve *host* adresimiz vardır
- Belirli *class* verilerine uygun olarak maske kullanılırsa *classful* olur

<div class="page"/>

#### DHCP (Dynamic Host Configuration Protocol)

- Bu protokol sayesinde IP adresleri otomatik olarak atanır
- Dinamik olarak IP ataması yapılır, boş IP adresleri hemen başkalarına verilir

| DHCP Mesaj Tipi | Açıklama                             | İsteğe Bağlı |
| --------------- | ------------------------------------ | ------------ |
| discover        | Broadcast (yayınlama) bulunma işlemi | Evet         |
| offer           | Sunucunun verdiği cevap              | Evet         |
| request         | Sunucudan IP isteme                  | Hayır        |
| ack             | Sunucunun IP adresini göndermesi     | Hayır        |

#### DHCP Client-Server Senaryasu

- Bilgisayar ağa bağlanır
- DHCP Discover mesajını gönderir
  - IP adresi almak için DHCP *server*'ını bulmaya çaışıyor
  - Kendi IP'sine 0.0.0.0 dest IP'ye 255.255.255.255
- DHCP offer mesajı alır
  - *DHCP*, *IP* adresi sunuyor, istiyor musun diyor
- DHCP request mesajı gönderir
  - *Host* verilen *IP*'yi kabul ettiği bilgisini gönderiyor
- DHCP ack mesajı alır
  - *IP* adresini atanıyor
  - *Subnet* bilgisi atanıyor
  - *DNS server*'ın IP adresi bilgisi veriliyor
  - *Gateway*, Diğer ağalara çıkısı sağlayan adresi
- ilerleme hiyerarşisi: `DHCP -> UDP -> IP -> Ethernet -> Physical`
  - App - Transport - Network - Link - Physical
  - Sistemdeki tüm bilgisayarları geziyor

> Default Gateway, internete erişim yaptığımız IP adresimizdir, *local network* üzerinden olan IP adresi ile internete erişmeyiz. Her *local network*'ün çıkış IP'si aynıdır

<div class="page"/>

#### ISP Adresleme

ISP adres bloğu ICANN (Internet Corporation for Assigned Names and Numbers)

- IP adresi
- DNS
- Domaint

#### ISP Adressleme Hiyerarşisi

Yeni bir ISP'ye geçildiğinde yeni olandaki IP adresinin **subnet mask** değeri daha fazladır, bu sebeple

- İlk arama yenisinde yapılır yenide yoksa eski IP'ye bakılır
- Aktarımlarda sorun oluşturulması engellenir
- Örn: Turkcell'ten TTNet'e taşındığı zaman, TTNeT'deki IP verisinde olan *subnet mask* değeri (x.x.x.x / 23) değeri fazladır

> *Subnet mask*, subnet için ayrılan bit sayısı

#### NAT (Network Adress Translation)

*Local network*'ler internet ile etkileşime geçerken tek bir IP kullanırlar

- ISP'lerde IP uzunluğu önemsizdir, tek IP kullanılır
- *Local network* (yerel ağ) üzerindeki değişikler ISP'yi etkilemez (tam tersi de geçerli)
- *Local network* içindeki kullanıcılar internet üzerinde gözükmez (güvenlik amaçlı)
- Giden *datagram* verilerinde IP adresi yerine NAT IP adresi konulur, gelenlerde de NAT IP yerine IP adresine çevrilir
- LAN = Local area network (IP)
- WAN = World area network (NAT IP)
- NAT 16bit *port-number* alanı sayesinde 60.000 *LAN-side adress* destekler

## Hauwei Dersi

Adı sonradan değiştirilmeli 🤔

> Notlar tam değildir, katıldığım (ve dinlediğim 😄) kısımlar yazılmıştır.

### Yazılım Notları

- `eNSP` Hauwei'nin sunduğu *network* similasyın uygulaması

### Temel Kavramlar

| Kavram          | Açıklama                                                                         |
| --------------- | -------------------------------------------------------------------------------- |
| IP Adresi       | İnternete bağlanma adresimiz                                                     |
| SubnetMask      | Kimlik ve grupları ayırmak için kullanılır                                       |
| Default Gateway | İki farklı *network*'ün iletişimini sağlar, local networkten çıkış IP'si aynıdır |
| Subnet ID       | Last IP & (logic and) SubnetMask                                                 |

#### SubnetMask Host ve Bit Hesaplamaları

$255.255.b.a$ olan subnetmask için:

- $host = (256 - b)(256 - a) - 2$
  - 0 ve 255 kullanılamaz, ondan - 2
- $bit = 32 - log_2 (host + 2)$
  - Subnet içina ayrılan bit (*subnet mask*)

Subnet splitting:

- $m \geq log_2(subnet)$
  - $subnet$: istenen subnet sayısı
  - $m$ kadar host kısmına 1 yazılır (x.x.x.x / 21 ise 22 olacak)
- $host = 2^n - 2$
  - $n$: Bir subnetteki host sayısı
- $2^n$ kadar arttırılacak şekilde IP'ler gruplanır
- Başlangıç ve bitiş dahil olmaz

#### IPv4 Classes

$IP.0.0.0$ için temel formül:

- $IP_{class} = IP_{class - 1} + 2^{8 - harf}$
  - $harf$ A -> 0 olmak üzere alfabetik sıra
  - $IP_{0} = 0$

| Class | IP Karşılığı | Artış |
| ----- | ------------ | ----- |
| A     | 0.0.0.0      | 0     |
| B     | 128.0.0.0    | 128   |
| C     | 192.0.0.0    | 64    |
| D     | 224.0.0.0    | 32    |
| E     | 240.0.0.0    | 16    |

### Layer Özellikleri

| Layer2                                 | Layer3                                                                                 |
| -------------------------------------- | -------------------------------------------------------------------------------------- |
| Aynı *network*'teki haberleşme (local) | Farklı *network*'teki haberlerşme                                                      |
| Modemlerdeki *LAN* portlarının katmanı | Modemdeki *ADSL* portunun katmanı                                                      |
| *Switch* ile gerçekleşir               | *Router* ile gerçekleşir                                                               |
| *MAC* adresleri ile haberleşilir       | Asıl hedefe *IP* adresi ile gidilir, *MAC* adresleri hedefe gidiş sırasında kullanılır |
| *Gateway* olmaz                        | *Gateway* olur                                                                         |

- *Router*, *switch*lerin haberleşmesini sağlar
- *switch*, aynı ağdaki bilgisayarların haberleşmesini sağlar
- *Gateway*, asıl hedefini belirtir ve hedefe giderken başka yerlere gitmesiyle ilgilnemez bilgisi olmaz. (kargo şirkerlerine paket vermek gibi)

### *MAC* varken Neden *IP* Adresi Var

- Paket alışverisi *IP* adresi ile yapılmaktadır (layer3)
- Router arasında aktarım yapılırken, Source *MAC* adresi sabit kalarak, Destination *MAC* adresleri değişmektedir
  - Source *MAC*, kaynağın kimliğini tutar
  - Destination *MAC*, paketin gönderileceği kaynağın adresini tutar.
  - *IP*, asıl kaynağın sanal adresini tutar
- Her kaynak bildiği hedefe paketi yollar (gateway yapısı)
  - Bildiği adres olarak ifade edilen *MAC* adresidir

### Static Route

Her iki router için de bu komutlardan biri tanımlanırsa bağlantı mümkün olur.

- ip route-static [dest_ip] [subnet] [dest_port]
- ip route-static [dest_ip] [subnet] Serial [port_number]
- ip route-static [dest_ip] [subnetmask] Serial [port_number]

### RIP - Routing Information Protocol

- Interior Gateway Protocol (IGP)
- Distance vector algorithm
- Ufak çaplı *network*'lerde kullanılır

| Rip - 1                              | Rip - 2                                         |
| ------------------------------------ | ----------------------------------------------- |
| Classful routing protocol            | Classless routuing protocol                     |
| Broadcast route updates              | Multicast route updates 224.0.0.9               |
| UDP 520 port send and recieve packet | UDP 520 port send and recieve packet            |
| Metric (Hop count)                   | Metric (Hop count)                              |
|                                      | Support external route tag, route summarization |
|                                      | Specified next hop and authentication (MD5)     |
|                                      | Classless inter-domain routing (CIDR)           |

#### RIP-2 Özellikleri

- Timer
- Split Horizon
- Poison Reverse
- Trigger Update
  - Route bilgisi değişirse hemen güncelleme paketini komşusuna gönderir

#### RIP-2 Örneği

Temel sistem:

- `rip`
- `version 2`
- `network <network_id>`
  - Kaç *network*'e bağlıysa o kadar `network ...` komutu yazılır
  - `<network_id>` sonu `.0` olan IP adresidir
- `quit`

![huaweri_rip_ex](../res/huawei_rip_ex.png)

### OSPF Open Shortest Part First

- Link State interior gateway protocol (IGP)
- SPF Algorith
- Kurumsal *network*'lerde kullanılır

#### OSPF Package Types

> Genel olarak Link State (LS) olanları barındırır.

- Hello
- Database Description (DD)
- Link State Request (LSR)
- Link State Update (LSU)
- Link State Acknowledgement (LSAck)

### BGP

- BGP, **TCP 179** portunu kullanır
- Büyük çaplı *network*'lerde kullanılır
- BGP neighbor reletionship yapısı: `Idle - Connect - Opensent - OenConnect - Estanblished` şeklindedir

### Comparing Protocol

| RIP - 2                               | OSPF                                       | IS - IS                                    | BGP                                    |
| ------------------------------------- | ------------------------------------------ | ------------------------------------------ | -------------------------------------- |
| Interior Gateway Protocol (IGP)       | Link State interior gateway protocol (IGP) | Link State Interior Gateway Protocol (IGP) | Exterior Gateway Protocol (EGP)        |
| Distance vector algorithm             | SPF Algorith                               | SPF algorithm                              | Optimal route between ASs              |
| Ufak çaplı *network*'lerde kullanılır | Kurumsal *network*'lerde kullanılır        | Büyük çaplı *network*'lerde kullanılır     | Büyük çaplı *network*'lerde kullanılır |

> BGP, **TCP 179** portunu kullanır.
>
>

### Collision & Broadcast Domain

| Metod            | Hub     | Repeater | Switch          | Bridge   | Router   |
| ---------------- | ------- | -------- | --------------- | -------- | -------- |
| Collision Domain | Geçirir | Geçirir  | Geçirmez        | Geçirmez | Geçirmez |
| Broadcast Domain | Geçirir | Geçirir  | Seçici geçirgen | Geçirir  | Geçirmez |

### TCP / IP Model

| TCP                 | UDP               |
| ------------------- | ----------------- |
| Connection-Oriented | Connection-less   |
| Windowing           | No Windowing      |
| Error Recovery      | No Error Recovery |
| Ordered Data        | No Ordered Data   |

> UDP hız odaklıdır.

#### TCP Transmission Types

- Connection 3-Way Handshake
- Connection Termination
- Normal Data Transmission
- Error Recovery
- Windowing

### Virtual LAN (VLAN)

Switch içerisinde switch yapısı oluştururak, sanal bir ağ yapısı sunar

- VLAN içerisindeki kendi aralarında haberleşebilir, diğer LAN üyeleri mesaj gönderemez
  - VLAN'ı switch, LAN'ı da router'a bağlı host'lar olarak düşünebiliriz.
  - VLAN, little switch olarak da tanımlanır
- Güvenlik amaçlı yapılmıştır, fiziksel olarak Router ve Switch almak pahalıya gelmektedir
- *Access* ve *Trunk Port* olarak 2 *port*'u vardır
- *Trunk port*, switchler arası portlar

#### VLAN Avantajları

- Geliştirilmiş güvenlik
- Düşük maalyet
- Verimli performans
- Yönetim kolaylığı

### Spanning Tree Protocol (STP)

- *Root bridge*'ın tüm portları elden atanır (*designated port*)
- *Root bridge*'e giden en kısa yol *root port* olarak seçilir

#### STP Port State

- Listening
- Learning
- Forwarding
- Disabled

### Sınav Soruları

> Copyright © ~ Sena Modanlıoğlu

![huawei1](../res/Huawei1.jpeg)

![huawei2](../res/Huawei2.jpeg)

![huawei3](../res/Huawei3.jpeg)

## Lisans ve Teferruatlar

Bu yazı **MIT** lisanslıdır. Lisanslar hakkında bilgi almak için [buraya](https://choosealicense.com/licenses/) bakmanda fayda var.

- [Website](https://yemreak.com)
- [Github](https://github.com/yedehrab)
- [GitLab](https://gitlab.com/yedehrab)

> Yardım veya destek için [iletişime](mailto::yyunussemree@gmail.com) geçebilrsiniz 😇.

~ Yunus Emre Ak

> Katkı sağlayanlar:
>
> - Sefa Yalçındağ (Final konularına beraber çalışıldı)
> - Sena Modanlıoğlu (Huawei sınav soruları)