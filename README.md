# 🕷️ Şikayetvar Scraper

Bu proje, Python ve Selenium kullanarak **[Sikayetvar.com](https://www.sikayetvar.com)** üzerindeki belirli kurum veya markalara ait şikayet verilerini otomatik olarak çeken ve analiz edilebilir **JSON** formatında kaydeden bir veri kazıma (web scraping) aracıdır.

Varsayılan olarak *"Feyziye Mektepleri Vakfı Işık Okulları"* verilerini çekecek şekilde ayarlanmıştır ancak kolayca özelleştirilebilir.

## 🚀 Özellikler

* **Otomatik Sayfalama:** Sayfalar arasında (Pagination) otomatik olarak gezinir ve verileri toplar.
* **Detaylı Veri Çekimi:** Her şikayet için aşağıdaki verileri alır:
    * 📝 Şikayet Başlığı
    * 💬 Şikayet İçeriği/Özeti
    * ⭐ Şikayet Puanı
    * 🔗 Şikayet Linki (Eksikse otomatik oluşturur)
    * 📸 Görsel durumu (Kanıt fotoğrafı var mı?)
* **Headless Mode:** Tarayıcıyı arka planda (arayüzsüz) çalıştırır, işinizi bölmez.
* **Akıllı URL Oluşturma:** Linki olmayan şikayetler için başlıktan yola çıkarak geçerli URL üretir.
* **JSON Çıktısı:** Verileri `UTF-8` formatında, düzgün girintili (indented) JSON dosyasına kaydeder.

## 🛠️ Kurulum

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
* Python 3.7+
* Google Chrome Tarayıcısı

### Adım 1: Projeyi Klonlayın
```bash
git clone [https://github.com/alifatihuzun/Web-Scraping-Project.git](https://github.com/alifatihuzun/Web-Scraping-Project.git)
cd Web-Scraping-Project
Adım 2: Sanal Ortam Oluşturun (Önerilen)
Bash

python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
Adım 3: Gerekli Kütüphaneleri Yükleyin
Bash

pip install -r requirements.txt
(Eğer requirements.txt dosyanız yoksa pip install selenium komutu yeterlidir.)

💻 Kullanım
Kurulum tamamlandıktan sonra scripti çalıştırmak için terminale şu komutu yazın:

Bash

python main.py
(Not: Python dosyanızın adı main.py değilse, kendi dosya adınızı yazın örn: python scrape.py)

İşlem tamamlandığında proje klasöründe şikayetlerin bulunduğu bir .json dosyası oluşacaktır: feyziye-mektepleri-vakfi-isik-okullari-kurumlari-sikayetler.json

Hedef Kurumu Değiştirme
Farklı bir markayı taramak istiyorsanız kod içerisindeki base_url ve dosya kaydetme ismini değiştirmeniz yeterlidir.

📂 Dosya Yapısı
.
├── main.py             # Ana scraping kodu
├── requirements.txt    # Gerekli kütüphaneler
├── .gitignore          # Git'e yüklenmeyecek dosyalar
├── README.md           # Proje dokümantasyonu
└── *.json              # Çıktı dosyası (Git'e yüklenmez)
⚠️ Yasal Uyarı (Disclaimer)
Bu proje sadece eğitim ve kişisel gelişim amaçlıdır.

Web scraping işlemleri sırasında hedef sitenin (sikayetvar.com) robots.txt dosyasına ve Kullanım Koşullarına (Terms of Service) riayet ediniz.

Site sunucularını yormamak adına istekler arasına bekleme süresi (time.sleep) konulmuştur, bu süreyi kaldırmayınız.

Elde edilen verilerin ticari kullanımı veya izinsiz dağıtımı kullanıcının sorumluluğundadır.

🤝 Katkıda Bulunma
Hata düzeltmeleri, özellik eklemeleri ve iyileştirmeler için Pull Request göndermekten çekinmeyin!

Bu repoyu Fork'layın.

Yeni bir dal oluşturun (git checkout -b feature/yeni-ozellik).

Değişikliklerinizi yapın ve Commit'leyin (git commit -m 'Yeni özellik eklendi').

Branch'inizi Push'layın (git push origin feature/yeni-ozellik).

Bir Pull Request oluşturun.

📄 Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
