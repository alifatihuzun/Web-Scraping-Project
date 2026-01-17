# Şikayetvar Scraper 🕷️

Bu proje, Python ve Selenium kullanarak [Sikayetvar.com](https://www.sikayetvar.com) üzerindeki belirli bir kurum veya marka hakkındaki şikayet verilerini (başlık, içerik, puan, link vb.) çeker ve JSON formatında kaydeder.

## 🚀 Özellikler

* **Otomatik Sayfalama:** Sayfalar arasında otomatik gezinir.
* **Veri Çıkarma:** Şikayet başlığı, açıklama, puan, görsel durumu ve link bilgilerini alır.
* **Link Düzeltme:** Eksik linkler için başlıktan URL üreten yardımcı fonksiyon içerir.
* **JSON Çıktısı:** Verileri `UTF-8` formatında JSON dosyasına kaydeder.
* **Headless Mode:** Tarayıcıyı arka planda (arayüzsüz) çalıştırır.

## 🛠️ Kurulum

1.  Repoyu klonlayın:
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/REPO_ISMI.git](https://github.com/KULLANICI_ADIN/REPO_ISMI.git)
    cd REPO_ISMI
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3.  Google Chrome ve ChromeDriver'ın yüklü olduğundan emin olun.

## 💻 Kullanım

Script içerisindeki `base_url` veya hedef kurumu değiştirebilirsiniz. Varsayılan olarak "Feyziye Mektepleri Vakfı Işık Okulları" ayarlanmıştır.

Projeyi çalıştırmak için:

```bash
python main.py
