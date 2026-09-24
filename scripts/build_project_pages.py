from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]/'dist'
projects=[
 dict(slug='java-security-fixer',name='Java Security Fixer',en='Java Security Fixer',repo='https://github.com/karligorkem/java-security-fixer',stack='Java 21 · Spring Boot · PostgreSQL · Docker',
 problem='Statik analiz araçlarının dağınık bulgularını geliştiricinin güvenle inceleyebileceği bir akışa taşımak.',
 solution='Semgrep, SpotBugs ve FindSecBugs bulgularını CWE ve OWASP bilgileriyle ilişkilendiren bir backend ve arayüz. İzole çalışma alanı, güvenli dosya doğrulaması, diff önizlemesi ve kullanıcı onaylı düzeltme akışı içerir.',
 evidence='Kaynak kod çalıştırılmadan analiz edilir; öneri doğrudan üretim koduna yazılmaz. Doğrulama adımları ve geri alma tasarımı depoda belgelenmiştir.',
 enproblem='Bring scattered static-analysis findings into a workflow developers can review safely.',
 ensolution='A Spring Boot application that connects Semgrep, SpotBugs and FindSecBugs findings with CWE and OWASP context. It includes isolated workspaces, file validation, diff previews and user-approved fixes.',
 enevidence='Uploaded code is not executed during analysis; proposed changes are not applied to production code without approval. The repository documents validation and rollback.'),
 dict(slug='dboptima',name='DB Optima',en='DB Optima',repo='https://github.com/karligorkem/dboptima',stack='Python · FastAPI · PostgreSQL · Docker',
 problem='Yavaş PostgreSQL sorguları için indeks önerilerini tahmine bırakmadan ölçülebilir sonuçlarla değerlendirmek.',
 solution='EXPLAIN ANALYZE planlarını inceler, indeks adayları üretir ve ML modeliyle önceliklendirir. Geçici indeksle önce ve sonra benchmark çalıştırır; nihai kararı ölçülen iyileşmeye göre saklar.',
 evidence='Yerel örnek sorguda medyan süre 29,217 ms’den 0,03 ms’ye indi. Bu sonuç tek test iş yüküne aittir; farklı veri ve donanımda değişir.',
 enproblem='Evaluate PostgreSQL index recommendations against measured query performance.',
 ensolution='Analyzes EXPLAIN ANALYZE plans, generates index candidates and prioritizes them with an ML model. A before/after benchmark makes the final recommendation, and results are persisted.',
 enevidence='In one local sample query, median latency decreased from 29.217 ms to 0.03 ms. This is specific to that workload and is not a general performance claim.'),
 dict(slug='rag-analiz',name='RAG Analiz',en='RAG Analysis',repo='https://github.com/karligorkem/RAG-Analiz',stack='FastAPI · Qdrant · Docker · CrossEncoder',
 problem='Uzun PDF belgelerinde ilgili bilgiyi bulmak ve yanıtın dayandığı sayfayı göstermek.',
 solution='PDF doğrulama, parçalara ayırma, embedding araması ve CrossEncoder yeniden sıralamasını birleştirir. Yanıtlar doküman ve sayfa düzeyinde kaynak kartlarıyla sunulur.',
 evidence='Değerlendirme ekranı Hit@K, MRR ve gecikme ölçümlerini karşılaştırır. Yeterli kaynak bulunmadığında model çağrısı yapılmadan açık yanıt döndürülür.',
 enproblem='Find information in long PDFs and show the page supporting each answer.',
 ensolution='Combines PDF validation, chunking, embedding retrieval and CrossEncoder reranking. Answers include source cards with document and page references.',
 enevidence='An evaluation workflow tracks Hit@K, MRR and latency. When source evidence is insufficient, the application returns an explicit response without calling the language model.'),
 dict(slug='cloud-scheduler-ai',name='Cloud Scheduler AI',en='Cloud Scheduler AI',repo='https://github.com/karligorkem/cloud-scheduler-ai',stack='Python · Gymnasium · MaskablePPO · pytest',
 problem='Kısıtlı CPU, RAM ve GPU kaynakları altında görevleri yerleştirirken kuyruk bekleme süresini azaltmak.',
 solution='Sentetik görevleri ve iki sunuculu ortamı simüle eder. First Fit, Best Fit, Best Fit RAM ve iki PPO yaklaşımını aynı seed’lerle karşılaştırır; geçersiz atamaları eylem maskesiyle engeller.',
 evidence='100 sentetik senaryoda ortalama bekleme First Fit için 14,5425, PPO için 13,2940 adımdır. PPO, Best Fit yöntemlerine karşı belirgin üstünlük göstermemiştir.',
 enproblem='Reduce queue wait time while placing jobs under CPU, RAM and GPU constraints.',
 ensolution='Simulates synthetic jobs and a two-server environment. Compares First Fit, Best Fit, Best Fit RAM and two PPO variants on matched seeds, with action masks for invalid placements.',
 enevidence='Across 100 synthetic scenarios, mean wait was 14.5425 steps for First Fit and 13.2940 for PPO. PPO did not show a clear advantage over Best Fit methods.'),
 dict(slug='gelir-pusulasi',name='Gelir Pusulası',en='Revenue Compass',repo='https://github.com/karligorkem/gelir-tahmin-platform',stack='Java · Spring Boot · FastAPI · XGBoost',
 problem='Günlük gelir tahmininde veri hatalarını tespit etmek ve model seçimini basit bir yöntemle karşılaştırmak.',
 solution='CSV verisini doğrular; XGBoost, CatBoost, LightGBM ve Extra Trees modellerini birden fazla geçmiş pencere üzerinde yarıştırır. Kazanan model basit 7 günlük tahmini geçerse yayınlanır ve 7–90 günlük tahmin üretir.',
 evidence='Rossmann verisindeki örnek değerlendirmede 135 günlük backtest için WAPE %8,92 ve basit modele göre MAE iyileşmesi %70,08 raporlanmıştır. Sonuçlar yalnızca bu veri setine aittir.',
 enproblem='Validate daily revenue data and compare predictive models against a simple baseline.',
 ensolution='Validates CSV input and compares XGBoost, CatBoost, LightGBM and Extra Trees across multiple backtest windows. A model is published only when it beats the seven-day baseline, then produces 7–90 day forecasts.',
 enevidence='An example Rossmann evaluation reports 8.92% WAPE over 135 backtest days and 70.08% MAE improvement over the baseline. These results are dataset-specific.'),
 dict(slug='tir-yukleme',name='Tır Yükleme Optimizasyonu',en='Truck Loading Optimization',repo=None,stack='Python · Streamlit · Yerleşim algoritmaları',
 problem='Dikdörtgen yükleri araç hacmine çakıştırmadan yerleştirmek ve kullanılmayan alanı görünür kılmak.',
 solution='Yüklerin farklı yönlerini dener, yerleştirme kısıtlarını kontrol eder ve sonucu üç boyutlu gösterir. Yerleşmeyen parçalar ve hacim kullanımı alternatif planları değerlendirmeyi kolaylaştırır.',
 evidence='Proje yerleşim ve görselleştirme prototipidir. Farklı yük kombinasyonlarında en iyi sonucu garanti ettiğine dair bir iddia yoktur.',
 enproblem='Place rectangular cargo without overlap and make unused trailer space visible.',
 ensolution='Tries item rotations, checks placement constraints and visualizes the result in 3D. Unplaced items and utilized volume help compare loading plans.',
 enevidence='This is a placement and visualization prototype; it does not claim an optimal result for every cargo mix.'),
]
css='''*{box-sizing:border-box}html{font-family:Tahoma,Verdana,sans-serif;font-size:16px;color:#1d2e49}body{margin:0;min-height:100vh;background:#5ba5db url("../../xp-wallpaper.png") center/cover fixed}a{color:#174b99}a:focus-visible{outline:3px solid #ffbd36;outline-offset:2px}.wrap{max-width:970px;margin:30px auto 70px;padding:0 15px}.panel{background:white;border:3px solid #1553ba;border-radius:9px;box-shadow:0 16px 40px #052c6780;overflow:hidden}.bar{background:linear-gradient(#589afb,#1155c6);color:white;padding:10px 16px;font-weight:bold}.content{padding:29px clamp(18px,5vw,45px)}.nav{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-bottom:22px}.eyebrow{font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;color:#55739a;font-weight:bold}h1{color:#164b9b;font-size:clamp(1.8rem,4vw,2.6rem);margin:6px 0 9px}h2{color:#164b9b;font-size:1.2rem;margin:24px 0 8px}p{line-height:1.65;margin:0 0 12px}.lead{font-size:1.12rem;max-width:67ch}.tags{display:flex;gap:7px;flex-wrap:wrap;margin:18px 0}.tag{background:#e0ebfb;color:#244c80;border-radius:3px;padding:5px 8px;font-size:.83rem;font-weight:bold}.evidence{padding:17px 20px;background:#edf5ff;border-left:4px solid #2874d3;margin:18px 0}.evidence strong{display:block;margin-bottom:7px}.chart{max-width:700px;margin:22px auto;background:#f5f9ff;border:1px solid #cbdcf1;border-radius:5px;padding:17px}.barrow{display:grid;grid-template-columns:125px 1fr 75px;gap:10px;align-items:center;margin:10px 0;font-size:.9rem}.track{height:18px;background:#deebf8;border-radius:2px}.fill{height:100%;background:linear-gradient(90deg,#2462c2,#67aaff);border-radius:2px}.chart small{color:#536886;line-height:1.5}.links{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}.button{display:inline-block;background:linear-gradient(#fff,#e1ebfa);border:1px solid #5d83bd;border-radius:4px;padding:10px 13px;text-decoration:none;font-weight:bold}.button:hover{background:#dbeafe}@media(max-width:600px){.wrap{margin:8px auto 50px;padding:0 7px}.content{padding:21px 17px}.barrow{grid-template-columns:90px 1fr 60px;font-size:.78rem;gap:5px}}'''
def figure(slug,lang):
 if slug=='dboptima': rows=[('Before' if lang=='en' else 'Önce','29.217 ms',100),('After' if lang=='en' else 'Sonra','0.03 ms',2)]
 elif slug=='cloud-scheduler-ai':rows=[('First Fit','14.54',100),('Best Fit','13.30',91.4),('PPO','13.29',91.4)]
 elif slug=='gelir-pusulasi':rows=[('WAPE','8.92%',8.92),('MAE gain' if lang=='en' else 'MAE kazanımı','70.08%',70.08)]
 else:return ''
 title='Measured example' if lang=='en' else 'Ölçülen örnek sonuç'
 body=''.join(f'<div class="barrow"><span>{a}</span><div class="track"><div class="fill" style="width:{w}%"></div></div><b>{b}</b></div>' for a,b,w in rows)
 note='Source: project README. Metrics are specific to the evaluation scenario.' if lang=='en' else 'Kaynak: proje README dosyası. Ölçümler değerlendirme senaryosuna özeldir.'
 return f'<figure class="chart"><strong>{title}</strong>{body}<small>{note}</small></figure>'
def page(d,lang):
 en=lang=='en';back='Back to portfolio' if en else 'Portfolyoya dön';other='Türkçe' if en else 'English';title=d['en'] if en else d['name'];lead=d['enproblem'] if en else d['problem'];solution=d['ensolution'] if en else d['solution'];evidence=d['enevidence'] if en else d['evidence'];src='Source code' if en else 'Kaynak kod';backurl='../../' if en else '../../';langurl='../../../projects/'+d['slug']+'/' if en else '../../en/projects/'+d['slug']+'/'
 repo=f'<a class="button" href="{d["repo"]}" target="_blank" rel="noopener noreferrer">{src} ↗</a>' if d['repo'] else ''
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(lead)}"><title>{escape(title)} | Görkem Karlı</title><style>{css.replace('../../xp-wallpaper.png', '../../../xp-wallpaper.png' if en else '../../xp-wallpaper.png')}</style></head><body><main class="wrap"><article class="panel"><div class="bar">📁 {escape(title)}</div><div class="content"><nav class="nav"><a href="{backurl}">← {back}</a><a href="{langurl}" lang="{'tr' if en else 'en'}">{other}</a></nav><p class="eyebrow">{'Project case study' if en else 'Proje incelemesi'}</p><h1>{escape(title)}</h1><p class="lead">{escape(lead)}</p><div class="tags">{''.join(f'<span class="tag">{escape(t.strip())}</span>' for t in d['stack'].split('·'))}</div><h2>{'The approach' if en else 'Çözüm yaklaşımı'}</h2><p>{escape(solution)}</p>{figure(d['slug'],lang)}<h2>{'Results and scope' if en else 'Sonuç ve kapsam'}</h2><div class="evidence"><strong>{'What the project demonstrates' if en else 'Projenin gösterdiği sonuç'}</strong><p>{escape(evidence)}</p></div><div class="links">{repo}<a class="button" href="{backurl}">{back}</a></div></div></article></main></body></html>'''
for d in projects:
 for lang in ('tr','en'):
  dest=ROOT/('en/projects' if lang=='en' else 'projects')/d['slug']/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(d,lang))
print('Generated',len(projects)*2,'project pages')
