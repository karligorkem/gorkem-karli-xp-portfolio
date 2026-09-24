from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path('/workspace/scratch/1c8802059e87/output/pdf/Gorkem_Karli_CV.pdf')
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DejaVu', normal='DejaVu', bold='DejaVu-Bold')
blue=colors.HexColor('#174c9a'); dark=colors.HexColor('#25334a'); muted=colors.HexColor('#53657d')
styles={
 'name':ParagraphStyle('name',fontName='DejaVu-Bold',fontSize=17,leading=21,textColor=blue,spaceAfter=3),
 'role':ParagraphStyle('role',fontName='DejaVu-Bold',fontSize=9,leading=13,textColor=dark,spaceAfter=5),
 'contact':ParagraphStyle('contact',fontName='DejaVu',fontSize=8.6,leading=12.5,textColor=muted,spaceAfter=8),
 'heading':ParagraphStyle('heading',fontName='DejaVu-Bold',fontSize=9,leading=12,textColor=blue,spaceBefore=9,spaceAfter=3),
 'body':ParagraphStyle('body',fontName='DejaVu',fontSize=9,leading=13.2,textColor=dark,spaceAfter=3),
 'bullet':ParagraphStyle('bullet',fontName='DejaVu',fontSize=9,leading=13.2,textColor=dark,leftIndent=10,firstLineIndent=-7,spaceAfter=2),
}
doc=SimpleDocTemplate(str(OUTPUT),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=15*mm,title='Görkem Karlı - Özgeçmiş',author='Görkem Karlı')
story=[]
def para(txt,style='body'):story.append(Paragraph(txt,styles[style]))
def heading(txt):para(txt,'heading')
para('GÖRKEM KARLI','name')
para('Bilgisayar Mühendisliği Öğrencisi | Backend, Python ve Veri Uygulamaları','role')
para('İstanbul / Ankara  ·  gorkemkarli467@gmail.com  ·  github.com/karligorkem<br/>linkedin.com/in/görkem-karlı-56b181378','contact')
heading('PROFESYONEL PROFİL')
para('Java ve Spring Boot ile REST API geliştirme; Python ve FastAPI ile veri odaklı servisler oluşturma üzerine proje deneyimi. PostgreSQL, Docker, test otomasyonu, makine öğrenmesi ve RAG uygulamalarını backend sistemleriyle birleştiren çalışmalar yürütüyorum.')
heading('EĞİTİM')
para('<b>Düzce Üniversitesi</b> | Bilgisayar Mühendisliği, Lisans')
heading('DENEYİM')
para('<b>Sersim, Kayseri</b> | Yazılım Geliştirme Stajyeri | 2024')
para('• Üretim sahasındaki hata kayıt ve raporlama ihtiyacına yönelik React Native / Expo mobil uygulamasının geliştirilmesinde görev aldım.','bullet')
para('• Barkod ve QR okuma, fotoğraflı hata bildirimi, token tabanlı API erişimi ve çevrimdışı kuyruğun senkronizasyonu üzerinde çalıştım.','bullet')
para('<b>Mondihome</b> | Staj')
heading('SEÇİLMİŞ PROJELER')
projects=[
 ('Java Security Fixer','Java 21 · Spring Boot · PostgreSQL · Docker','Semgrep, SpotBugs ve FindSecBugs bulgularını CWE/OWASP bilgileriyle ilişkilendiren; kullanıcı onaylı düzeltme ve doğrulama akışı sunan güvenlik platformu.'),
 ('DB Optima','Python · FastAPI · PostgreSQL · Docker','EXPLAIN ANALYZE planlarından indeks adayları üretir; ML sıralamasını önce/sonra benchmark ile sınar ve ölçülen sonucu kaydeder.'),
 ('RAG Analiz','FastAPI · Qdrant · Docker','PDF içeriklerinde embedding araması, yeniden sıralama ve sayfa düzeyinde kaynak gösteren belge analizi uygulaması.'),
 ('Cloud Scheduler AI','Python · Gymnasium · pytest','CPU/RAM/GPU kısıtları altında iş yerleştirme simülasyonu; klasik stratejileri MaskablePPO ile aynı sentetik senaryolarda karşılaştırır.'),
 ('Gelir Pusulası','Spring Boot · FastAPI · XGBoost','Günlük gelir verisi için CSV doğrulama, çoklu model karşılaştırması, geriye dönük test ve 7–90 günlük tahmin sunar.'),
]
for name,tech,desc in projects:
 para(f'<b>{name}</b> | {tech}')
 para(desc)
heading('TEKNİK ARAÇLAR')
para('<b>Backend:</b> Java, Spring Boot, Python, FastAPI, REST API, OpenAPI')
para('<b>Veri ve ML:</b> PostgreSQL, SQLAlchemy, Alembic, pandas, XGBoost, Qdrant, RAG')
para('<b>Test ve altyapı:</b> pytest, JUnit, Testcontainers, Git, Docker, Docker Compose')
doc.build(story)
(ROOT/'dist'/'Gorkem_Karli_CV.pdf').write_bytes(OUTPUT.read_bytes())
print(OUTPUT)
