# Görkem Karlı — XP temalı portfolyo

Bilgisayar mühendisliği, backend ve veri projelerini Windows XP'den ilham alan bir masaüstünde sunan statik portfolyo.

## İçerik

- Türkçe ve İngilizce masaüstü arayüzleri
- Altı proje için Türkçe ve İngilizce inceleme sayfaları
- İndirilebilir, tek sayfalık PDF özgeçmiş
- GitHub, LinkedIn ve e-posta bağlantıları
- Fare, dokunmatik ekran ve klavye ile açılabilen pencereler

## Yerel kullanım

`dist/` dizinini herhangi bir statik dosya sunucusuyla yayınlayın. Örneğin:

```bash
python3 -m http.server 8000 --directory dist
```

Ardından `http://localhost:8000` adresini açın. Uygulama bağımlılığı veya API anahtarı yoktur.

## İçeriği güncelleme

- Türkçe ana sayfa: `dist/index.html`
- İngilizce ana sayfa üreticisi: `scripts/build_english_home.py`
- Proje sayfası verileri ve üreticisi: `scripts/build_project_pages.py`
- PDF özgeçmiş üreticisi: `scripts/build_cv.py`
- Duvar kâğıdı: `dist/xp-wallpaper.png`

Metinleri değiştirdikten sonra ilgili üreticiyi çalıştırın. PDF üreticisi ReportLab ve sistemde DejaVu Sans fontları gerektirir; üretilmiş statik dosyaları görüntülemek için bunlar gerekmez.

## Canlı site

https://gorkem-karli-xp-portfolio.gorkemkarli41.chatgpt.site
