from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import re

# -----------------------------
# Güvenli Manuel URL Oluşturma Fonksiyonu
# -----------------------------
def baslik_to_url_safe(baslik):
    """
    Başlıktan düzgün manuel URL oluşturur.
    Türkçe karakterleri çevirir, özel karakterleri temizler ve kelimeleri tire ile birleştirir.
    """
    text = baslik.lower()
    replacements = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
        'â': 'a', 'î': 'i', 'û': 'u'
    }
    for tr, en in replacements.items():
        text = text.replace(tr, en)

    # Tüm özel karakterleri boşluk ile değiştir
    text = re.sub(r'[^a-z0-9 ]', ' ', text)

    # Kelimeleri boşluk ile ayır ve boş olanları çıkar
    words = [w for w in text.split() if w]

    # Kelimeleri tire ile birleştir
    url_path = '-'.join(words)

    url = f"https://www.sikayetvar.com/bahcesehir-universitesi/{url_path}"
    return url

# -----------------------------
# Selenium Ayarları
# -----------------------------
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)  # chromedriver PATH ayarlı olmalı

veriler = []
onceki_veriler = set()
page = 1
base_url = "https://www.sikayetvar.com"

while True:
    print(f"Sayfa {page} çekiliyor...")

    url = f"{base_url}/feyziye-mektepleri-vakfi-isik-okullari?page={page}"
    driver.get(url)
    time.sleep(2)

    articles = driver.find_elements(By.CSS_SELECTOR, "article.card-v2")
    yeni_veri_sayisi = 0

    for article in articles:
        try:
            layer_element = article.find_element(By.CLASS_NAME, "complaint-layer")
            baslik = layer_element.text.strip()
            href = layer_element.get_attribute("href")
            if href:
                link = href
            else:
                link = baslik_to_url_safe(baslik)
        except:
            baslik, link = "", ""

        try:
            yorum = article.find_element(By.CLASS_NAME, "complaint-description").text.strip()
        except:
            yorum = ""

        try:
            puan = article.find_element(By.CLASS_NAME, "rate-num").text.strip()
        except:
            puan = ""

        # Görsel kontrolü
        try:
            article.find_element(By.CSS_SELECTOR, ".complaint-attachments img")
            image = 1
        except:
            image = 0

        key = (baslik, yorum, puan, link, image)
        if key not in onceki_veriler and (baslik or yorum):
            veriler.append({
                "baslik": baslik,
                "yorum": yorum,
                "puan": puan,
                "link": link,
                "image": image
            })
            onceki_veriler.add(key)
            yeni_veri_sayisi += 1

    if yeni_veri_sayisi == 0:
        print("Yeni veri bulunamadı. Sayfalar bitmiş olabilir.")
        break

    page += 1
    time.sleep(1)

driver.quit()

# JSON dosyasına yaz
with open("feyziye-mektepleri-vakfi-isik-okullari-kurumlari-sikayetler.json", "w", encoding="utf-8") as f:
    json.dump(veriler, f, ensure_ascii=False, indent=4)

print(f"{len(veriler)} şikayet başarıyla kaydedildi.")
