import os,html,datetime,re
def fix(h):
    sl=CUR[0];d=CUR[1];me='./index.html' if sl=='' else '../'*d+sl+'/index.html'
    h=re.sub(r'href="([^"#:]*/)(#[^"]*)?"',lambda m:'href="'+m.group(1)+'index.html'+(m.group(2) or '')+'"',h)
    return h.replace('href="'+me+'"','href="#top"')
# ===== НАСТРОЙКИ: меняйте только здесь =====
NAME="Вячеслав Макаренко"
TAG="Автоматизация заявок и записей"
BASE=""            # для username.github.io/repo/ укажите "/repo" (нужно только для страницы 404)
TELEGRAM="https://t.me/RDDGCorpor"
VK="https://vk.ru/cr4zyf0x"
WHATSAPP=""        # например https://wa.me/79001234567
VIBER=""           # например viber://chat?number=%2B79001234567
EMAIL=""           # например you@mail.ru
# ===========================================
OUT=os.path.dirname(os.path.abspath(__file__))
D=[("avtoservis","Автосервис","#b45309","Поток заявок и заказов в автосервисе","Можно рассмотреть автоматизацию приёма заявки, предварительной записи, уведомлений и учёта статусов ремонта.",
["Клиент звонит, пишет в мессенджер или оставляет заявку на сайте","Администратор записывает данные в разные места","Трудно понять, кто принял обращение","Клиенту нужно сообщить о ходе ремонта"],
["Клиент оставляет обращение через доступный канал","Фиксируются имя, контакт, автомобиль и описание проблемы","Сотрудник получает уведомление","Заказ получает статус: «Новая заявка», «Ожидает диагностики», «В работе», «Готово»","Сотрудник связывается с клиентом"],
["Форма записи на диагностику","Сбор марки и модели автомобиля","Уведомление администратора","Таблица со статусами заказ-нарядов","Напоминание сотруднику перезвонить","История обращений"],
"Без подтверждения не обещаем: автоматическую диагностику, интеграцию с любой программой учёта, оценку стоимости ремонта без осмотра, синхронизацию со всеми мессенджерами.","Обсудить процесс заявок в автосервисе"),
("stomatologiya","Стоматология","#0e7490","Записи и напоминания о приёме","Автоматизация может помочь упорядочить обращения, записи и напоминания о приёме.",
["Записи приходят по телефону и через мессенджеры","Администратор вручную напоминает о визите","Пациент переносит приём, а расписание надо обновить","Новые обращения обрабатываются с задержкой"],
["Пациент оставляет запрос на запись","Администратор получает уведомление","Фиксируются контакт, желаемое время и услуга","Администратор подтверждает свободный слот","Пациенту уходит подтверждение или напоминание, если канал позволяет"],
["Форма запроса на запись","Уведомление администратора","Список обращений со статусами","Напоминание сотруднику подтвердить время","Шаблоны ответов на организационные вопросы"],
"Фокус только на организации записи и общения. Медицинские данные, диагнозы и рекомендации не собираем и не обрабатываем.","Обсудить запись и напоминания для клиники"),
("salon-krasoty","Салон красоты","#be185d","Записи, напоминания и история визитов","Можно упорядочить записи, напоминания и обращения клиентов.",
["Запись приходит в личные сообщения мастеров","Клиент не получил подтверждение","Свободные окна сложно быстро показать","История визитов потерялась"],
["Клиент оставляет запрос на услугу и время","Администратор выбирает мастера или слот","Запись получает статус: «Ожидает подтверждения», «Подтверждена», «Перенесена», «Завершена»","Клиент получает подтверждение или напоминание, если доступна интеграция"],
["Форма записи","Сбор пожеланий по услуге и мастеру","Уведомление администратора","Напоминание подтвердить или перенести запись","База контактов и истории визитов","Шаблоны ответов о правилах записи"],
"","Обсудить автоматизацию записи в салоне"),
("veterinarnaya-klinika","Ветеринарная клиника","#4d7c0f","Обращения владельцев не теряются","Автоматизация может помогать клинике не терять обращения и удобнее организовывать запись.",
["Владелец пишет в разные мессенджеры","Обращение нужно быстро передать администратору","Повторные приёмы требуют напоминаний","Сложно отследить, кому нужно ответить"],
["Владелец оставляет заявку на запись","Фиксируются контакты и общая информация о визите","Сотрудник получает уведомление и связывается с владельцем","При согласованном процессе создаётся напоминание о повторном визите"],
["Форма запроса на приём","Контакт владельца и тема обращения","Уведомления ответственному","Список статусов обращений","Шаблоны ответов о графике и подготовке к визиту"],
"Ветеринарных рекомендаций и оценки состояния животного автоматизация не даёт. Фокус на организации обращений и визитов.","Обсудить обработку обращений клиники"),
("remont-tehniki","Ремонт техники","#4338ca","Заявки, устройства и этапы ремонта","Автоматизация может помогать фиксировать заявки, устройства и этапы ремонта.",
["Техника принимается через звонки и сообщения","Описание неисправности сложно найти","Клиент не знает, принят ли заказ","Теряется история обращений по устройству"],
["Клиент отправляет заявку с устройством и описанием проблемы","Мастер или администратор получает уведомление","Заявка получает номер и статус","Статус меняется: «Принято», «Диагностика», «Ожидает согласования», «В ремонте», «Готово»","Клиенту отправляют обновление доступным способом"],
["Форма приёма заявки","Тип устройства и описание неисправности","Таблица заказов со статусами","Уведомления о готовности, если поддерживает канал","История заказов и контактов"],
"","Обсудить учёт заказов на ремонт"),
("fitnes-studiya","Фитнес-клуб","#c2410c","Заявки на пробные занятия","Автоматизация помогает организовать заявки на пробные занятия, расписание и обратную связь.",
["Заявки приходят через сайт и соцсети","Менеджер не успевает всем ответить","Расписание и контакты ведутся в разных местах","После пробного занятия забывают связаться"],
["Посетитель оставляет заявку на пробное занятие","Менеджер получает уведомление","Фиксируются направление и удобное время","Менеджер подтверждает расписание","После занятия создаётся задача связаться, если человек согласен"],
["Форма заявки на пробное","Распределение по направлениям","Статусы: «Новая», «Связались», «Записан», «Посетил»","Напоминания о занятиях","Сбор обратной связи"],
"","Обсудить автоматизацию заявок студии")]
e=html.escape
def PH(sl,pre):
    j=os.path.exists(os.path.join(OUT,'images',sl+'.jpg'))
    return (f'url({pre}/{sl}.jpg),' if j else '')+f'url({pre}/{sl}.svg)'
CUR=['',0]
CSS="""*{box-sizing:border-box}:root{--ink:#14222e;--mut:#4f5f6b;--bg:#f6f8fa;--ln:#d5dde3;--ac:#0f766e}
body{margin:0;font:17px/1.6 system-ui,'Segoe UI',Roboto,sans-serif;color:var(--ink);background:var(--bg)}
h1,h2,h3{font-family:Georgia,'Times New Roman',serif;line-height:1.2;margin:0 0 .6em}h1{font-size:clamp(2rem,5vw,3.2rem)}h2{font-size:1.7rem}h3{font-size:1.15rem}
a{color:inherit}.w{max-width:1040px;margin:0 auto;padding:0 20px}section{padding:44px 0}p{max-width:68ch}
header{background:#fff;border-bottom:1px solid var(--ln);position:sticky;top:0;z-index:5}
.hd{display:flex;align-items:center;gap:16px;min-height:64px;flex-wrap:wrap}.logo{font-family:Georgia,serif;font-weight:700;text-decoration:none;font-size:1.1rem;margin-right:auto}
nav ul{list-style:none;display:flex;gap:18px;margin:0;padding:0;align-items:center}nav a{text-decoration:none;padding:8px 2px}nav a:hover{text-decoration:underline}
.sub{display:none;position:absolute;background:#fff;border:1px solid var(--ln);padding:8px 14px;flex-direction:column;gap:2px}li.dd{position:relative}li.dd:hover .sub,li.dd:focus-within .sub{display:flex}
.btn{display:inline-block;background:var(--ac);color:#fff;padding:12px 22px;border-radius:6px;text-decoration:none;font-weight:600;min-height:44px;border:0;font-size:1rem}.btn.o{background:none;color:var(--ink);border:2px solid var(--ink)}
#mb{display:none;background:none;border:2px solid var(--ink);border-radius:6px;padding:10px 14px;font-size:1rem;min-height:44px}
.g{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}.card{background:#fff;border:1px solid var(--ln);border-left:6px solid var(--c,var(--ac));padding:20px;border-radius:4px}
.flow{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:26px 0;padding:0;list-style:none}.flow li{background:#fff;border:2px solid var(--c,var(--ac));padding:10px 14px;border-radius:4px;font-weight:600}.flow li+li:before{content:"›";margin-right:10px;color:var(--mut)}
ol.st{padding-left:1.3em}ol.st li,ul.ls li{margin:.4em 0}.note{background:#fff;border:1px dashed var(--mut);padding:14px 18px;border-radius:4px}.tag{display:inline-block;background:#e3eef0;padding:2px 10px;border-radius:99px;font-size:.85rem}
.hero{background:#fff;border-bottom:1px solid var(--ln)}.cta{background:#14222e;color:#fff}.cta .btn{background:#fff;color:#14222e}.cta .btn.o{background:none;color:#fff;border-color:#fff}
.tiles{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;margin-top:24px}
.tile{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:300px;border-radius:20px;overflow:hidden;color:#fff;text-decoration:none;isolation:isolate;border:2px solid transparent;transition:border-color .25s,box-shadow .25s}
.tile .ph{position:absolute;inset:0;z-index:-2;background-size:cover;background-position:center;transition:transform .5s}
.tile:before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(to top,rgba(10,20,28,.88) 0%,rgba(10,20,28,.45) 55%,rgba(10,20,28,.1) 100%)}
.tile div.tx{padding:26px}.tile h3{font-size:1.7rem;margin:0 0 .3em;color:#fff}.tile p{margin:0 0 .8em;max-width:36ch}.tile .go{font-weight:600;border-bottom:2px solid currentColor}
.tile:hover,.tile:focus-visible{border-color:#fff;box-shadow:0 0 0 4px rgba(255,255,255,.25)}.tile:hover .ph{transform:scale(1.05)}
@media(max-width:820px){.tiles{grid-template-columns:1fr}.tile{min-height:240px}}
footer{border-top:1px solid var(--ln);padding:32px 0;color:var(--mut);font-size:.95rem}footer a{display:block;padding:3px 0}.fg{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}.bt{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px}
:focus-visible{outline:3px solid #f59e0b;outline-offset:2px}
@media(max-width:820px){#mb{display:block}nav{display:none;width:100%}nav.open{display:block}nav ul{flex-direction:column;align-items:flex-start;padding-bottom:14px}.sub{display:flex;position:static;border:0;padding:0 0 0 14px}.hd{padding:8px 0}}"""
CSS+="""
html{scroll-behavior:smooth}body{background:#f2f5f7;letter-spacing:.005em}
h1{letter-spacing:-.02em;font-weight:700}h2{font-size:clamp(1.6rem,3vw,2.1rem);letter-spacing:-.01em}p{color:#33434f}
section{padding:60px 0}
header{background:rgba(255,255,255,.92);backdrop-filter:blur(8px)}
.logo:before{content:"";display:inline-block;width:14px;height:14px;background:var(--ac);border-radius:4px 10px 4px 10px;margin-right:10px;vertical-align:-1px}
nav a{border-radius:6px;padding:8px 10px;transition:background .2s}nav a:hover{background:#e8eef2;text-decoration:none}
.btn{box-shadow:0 2px 0 rgba(0,0,0,.15);transition:transform .15s,box-shadow .15s,filter .15s}.btn:hover{transform:translateY(-2px);box-shadow:0 6px 14px rgba(20,34,46,.22);filter:brightness(1.08)}
.hero{background:radial-gradient(circle at 85% 20%,color-mix(in srgb,var(--ac) 14%,#fff) 0,transparent 45%),linear-gradient(#fff,color-mix(in srgb,var(--ac) 5%,#fff));border-bottom:1px solid var(--ln)}
.hero section{padding:84px 20px 72px}.hero h1{max-width:18ch}.hero p{font-size:1.15rem}
.flow li{box-shadow:0 2px 6px rgba(20,34,46,.07);border-width:1px;border-bottom-width:4px}.flow li+li:before{content:"→";font-weight:700}
.card{padding:26px;border-radius:14px;border:1px solid var(--ln);border-left-width:6px;box-shadow:0 1px 3px rgba(20,34,46,.05);transition:box-shadow .2s,transform .2s}.card:hover{box-shadow:0 10px 24px rgba(20,34,46,.1)}
.card h3{font-size:1.25rem}.card a{color:var(--ac);font-weight:600}
ul.ls{list-style:none;padding:0}ul.ls li{position:relative;padding-left:26px}ul.ls li:before{content:"";position:absolute;left:4px;top:.62em;width:9px;height:9px;border-radius:50%;background:var(--ac)}
ol.st{list-style:none;counter-reset:s;padding:0}ol.st li{counter-increment:s;position:relative;padding:12px 0 12px 54px;border-bottom:1px solid var(--ln)}ol.st li:before{content:counter(s);position:absolute;left:0;top:8px;width:38px;height:38px;border-radius:50%;background:var(--ac);color:#fff;display:grid;place-items:center;font-weight:700}
.note{border-radius:12px;background:#fff8e6;border:1px solid #f0d58a;color:#5a4710}
.tag{background:color-mix(in srgb,var(--ac) 14%,#fff);color:var(--ac);font-weight:600;margin-bottom:8px}
.tiles{gap:28px}.tile{min-height:340px;border-radius:24px;box-shadow:0 8px 24px rgba(20,34,46,.18)}.tile h3{font-size:2rem}.tile .go{font-size:.95rem;border:0;background:rgba(255,255,255,.18);padding:8px 16px;border-radius:99px;display:inline-block;transition:background .2s}.tile:hover .go{background:rgba(255,255,255,.34)}
.cta{background:linear-gradient(135deg,#14222e,#1d3a46);padding:20px 0}.cta h2{color:#fff}.cta p{color:#c9d6de}.cta .btn{box-shadow:none}
footer{background:#101c26;color:#aebcc6;border:0;margin-top:0}footer strong{color:#fff}footer a{color:#aebcc6;text-decoration:none}footer a:hover{color:#fff;text-decoration:underline}
@media(max-width:820px){section{padding:42px 0}.hero section{padding:52px 20px 44px}.tile{min-height:260px}.tile h3{font-size:1.6rem}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""
CSS+="""
body{background:#0a131a;color:#e6edf2}h1,h2,h3{color:#fff}p{color:#b6c5d0}a{color:inherit}
header{background:rgba(10,19,26,.78);border-bottom:1px solid rgba(255,255,255,.08)}.logo{color:#fff}.hd{flex-wrap:nowrap;gap:12px}
nav ul{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:99px;padding:4px;gap:2px}nav li a{display:block;color:#dbe6ed;padding:8px 14px;border-radius:99px;font-size:.92rem;font-weight:600}nav a:hover{background:rgba(255,255,255,.12)}
.sub{background:#12212b;border:1px solid rgba(255,255,255,.12);border-radius:14px;top:100%;padding:8px;min-width:220px}.sub a{border-radius:8px}
.hd>.btn{white-space:nowrap;padding:10px 18px;min-height:42px}#mb{color:#fff;border-color:rgba(255,255,255,.4);margin-left:auto}
.btn{box-shadow:0 0 0 1px rgba(255,255,255,.12) inset}.btn.o{color:#fff;border-color:rgba(255,255,255,.55)}
.btn.big{padding:16px 34px;font-size:1.05rem;border-radius:12px;box-shadow:0 0 0 3px rgba(255,255,255,.22),0 0 32px color-mix(in srgb,var(--ac) 70%,transparent)}
.hero{min-height:82vh;display:flex;align-items:flex-end;border:0;background:radial-gradient(60% 55% at 78% 30%,color-mix(in srgb,var(--ac) 55%,transparent),transparent 70%),radial-gradient(40% 40% at 15% 90%,rgba(245,158,11,.18),transparent 70%),linear-gradient(180deg,#0d1c26,#0a131a)}
.hero>section{padding-bottom:56px}.hero h1{max-width:16ch;font-size:clamp(2.4rem,6vw,4.4rem)}.hero p{color:#c4d2dc}
.flow li{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-bottom:3px solid var(--c,var(--ac));color:#fff;backdrop-filter:blur(6px)}.flow li+li:before{color:#7fd6cc}
.chips{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px}.chips span{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:12px;padding:8px 14px;font-size:.9rem;color:#dbe6ed}
.card{background:#101d27;border-color:#22343f;color:#e6edf2}.card p,.card li{color:#b6c5d0}.card a{color:#7fd6cc}
.tile{min-height:400px}.tile:before{background:linear-gradient(to top,rgba(6,12,17,.96) 0%,rgba(6,12,17,.7) 38%,rgba(6,12,17,0) 75%)}.tile p{color:#e8eef2;font-size:1.05rem}.tile div.tx{padding:30px}.tile h3{font-size:2.2rem}
.tile:hover,.tile:focus-visible{box-shadow:0 0 36px rgba(127,214,204,.35)}.tile .ph{filter:saturate(1.15)}
.note{background:#241d0a;border-color:#6b5514;color:#f3dd9a}.tag{background:rgba(127,214,204,.15);color:#7fd6cc}
ol.st li{border-color:#22343f;color:#dbe6ed}ul.ls li{color:#c9d6de}
.cta{background:radial-gradient(60% 120% at 80% 0,color-mix(in srgb,var(--ac) 45%,transparent),transparent 70%),#0d1c26}
footer{background:#070d12}
@media(max-width:980px){#mb{display:block}nav{display:none;width:100%;order:9}nav.open{display:block}.hd{flex-wrap:wrap}nav ul{flex-direction:column;align-items:stretch;border-radius:16px;padding:8px}.sub{display:flex;position:static;background:none;border:0}}
@media(max-width:820px){.hero{min-height:70vh}.tile{min-height:300px}.tile h3{font-size:1.7rem}}
"""
CSS+="""
.hero.d{background-size:cover;background-position:right center;min-height:76vh}.hero.d h1{max-width:15ch}
.ci{display:flex;gap:16px;align-items:flex-start;border-left-width:1px;border-top:3px solid var(--c)}.ci p{margin:0;color:#dbe6ed}
.ic{flex:none;width:48px;height:48px;border-radius:14px;display:grid;place-items:center;color:#fff;background:color-mix(in srgb,var(--c) 70%,#0a131a);box-shadow:0 0 18px color-mix(in srgb,var(--c) 45%,transparent)}
.two{display:grid;grid-template-columns:1.1fr 1fr;gap:32px;align-items:start;margin:26px 0}.pic{border-radius:22px;min-height:420px;background-size:cover;background-position:center;position:sticky;top:90px;box-shadow:0 10px 30px rgba(0,0,0,.4)}.pic.sm{min-height:190px;position:static;border-radius:12px;margin-bottom:14px}
.tl{list-style:none;margin:0;padding:0;position:relative}.tl:before{content:"";position:absolute;left:19px;top:10px;bottom:10px;width:2px;background:linear-gradient(var(--c),transparent)}
.tl li{position:relative;display:flex;gap:18px;align-items:flex-start;padding:10px 0}.tl b{flex:none;width:40px;height:40px;border-radius:50%;background:var(--c);color:#fff;display:grid;place-items:center;z-index:1;box-shadow:0 0 0 5px #0a131a}
.tl div{background:#101d27;border:1px solid #22343f;border-radius:12px;padding:14px 18px;color:#e6edf2;flex:1}
.ba{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:center;margin-top:24px}.ar{font-size:2rem;color:#7fd6cc}
@media(max-width:820px){.two{grid-template-columns:1fr}.pic{position:static;min-height:240px}.ba{grid-template-columns:1fr}.ar{transform:rotate(90deg);text-align:center}.hero.d{min-height:64vh}}
"""
CSS+="""
header{transition:transform .3s ease}header.hide{transform:translateY(-110%)}
nav li a,nav ul{white-space:nowrap}.btn,.btn.o{border-radius:12px}
.two{grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);align-items:stretch}.two>*{min-width:0}
.pic{position:relative;top:auto;background-position:78% center;min-height:420px}
@media(max-width:1180px){nav li a{padding:8px 10px;font-size:.88rem}}
@media(max-width:820px){.two{grid-template-columns:minmax(0,1fr)}.pic{min-height:260px;background-position:80% center}}
"""
CSS+="""
main>section.w{padding-top:64px;padding-bottom:64px}.cta{padding:60px 0}
.gb{grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:22px}.svc{flex-direction:column;gap:14px}.svc h3{margin:0 0 .4em}
@media(max-width:820px){main>section.w{padding-top:44px;padding-bottom:44px}.cta{padding:44px 0}}
"""
CSS+="""
footer strong{display:block;margin-bottom:6px}.dis{margin-top:26px;padding:18px 22px;border:1px solid rgba(255,255,255,.28);border-radius:12px;background:rgba(255,255,255,.04);color:#e6edf2;font-size:1.02rem;line-height:1.6}.dis b{color:#fff}
"""
CSS+="""
body{overflow-x:clip}.hero{min-height:min(82vh,720px)}.hero.d{min-height:min(76vh,680px)}
@media(max-width:820px){
body{font-size:16px}h2{font-size:1.5rem}
.hero,.hero.d{min-height:0}.hero>section{padding:48px 20px 40px}.hero h1,.hero.d h1{font-size:2.05rem;max-width:none}.hero p{font-size:1.02rem}
.hero.d{position:relative;background-position:70% center}.hero.d:before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,19,26,.6),rgba(10,19,26,.93))}.hero.d>section{position:relative}
.flow{flex-direction:column;align-items:stretch;gap:8px;margin:20px 0}.flow li{width:100%;padding:10px 14px}.flow li+li:before{content:"↓";margin-right:8px}
.hero .btn,.cta .btn{display:block;width:100%;text-align:center;margin:0 0 10px}.btn.big{padding:16px 20px}
.chips{gap:8px;margin-top:16px}.chips span{font-size:.82rem;padding:6px 10px}
.hd{min-height:56px;gap:8px}.logo{font-size:1rem}.hd>.btn{font-size:.82rem;padding:8px 12px;min-height:40px}#mb{padding:8px 12px;min-height:40px}
nav li a{padding:12px 14px}.sub a{padding:10px 14px}
.card{padding:20px}.ic{width:42px;height:42px;border-radius:12px}
.tile{min-height:270px;border-radius:20px}.tile div.tx{padding:22px}.tile h3{font-size:1.6rem}.tile p{font-size:1rem}.tile .go{padding:10px 16px}
.pic{min-height:220px;border-radius:16px}.tl div{padding:12px 14px}.tl b{width:36px;height:36px}.tl:before{left:17px}
.dis{padding:16px;font-size:1rem}footer{padding:28px 0}
}
@media(max-width:400px){.hd>.btn{display:none}.logo{font-size:.95rem}}
"""
CSS+="""
.hero{position:relative}.hero>section{position:relative;z-index:1}
.hero:after{content:"";position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(to bottom,rgba(10,19,26,0),#0a131a 92%);pointer-events:none}
"""
def chans():
    c=[]
    if TELEGRAM:c.append(("Написать в Telegram",TELEGRAM))
    if VK:c.append(("Написать во ВКонтакте",VK))
    if WHATSAPP:c.append(("Написать в WhatsApp",WHATSAPP))
    if VIBER:c.append(("Написать в Viber",VIBER))
    if EMAIL:c.append(("Написать на почту","mailto:"+EMAIL+"?subject=Автоматизация&body=Здравствуйте! У меня [тип бизнеса]. Сейчас обращения обрабатываются так: [описание]. Хочу обсудить автоматизацию."))
    return c
def page(path,title,desc,body,depth,color="#0f766e"):
    CUR[0]=path;CUR[1]=depth;p="../"*depth
    L=lambda s:p+s
    dd="".join(f'<a href="{L(s)}/">{n}</a>' for s,n,*_ in D)
    cs="".join(f'<a class="btn o" href="{u}">{t}</a>' for t,u in chans())
    nav=f'''<header><div class="w hd"><a class="logo" href="{L("")or "./"}">{e(NAME)}</a><button id="mb" aria-expanded="false" aria-controls="nv">Меню</button>
<nav id="nv"><ul><li><a href="{L("")or "./"}">Главная</a></li><li class="dd"><a href="#" onclick="return false">Направления ▾</a><div class="sub">{dd}</div></li><li><a href="{L("uslugi/")}">Услуги</a></li><li><a href="{L("portfolio/")}">Портфолио</a></li><li><a href="{L("obo-mne/")}">Обо мне</a></li><li><a href="{L("kontakty/")}">Контакты</a></li></ul></nav>
<a class="btn" href="{L("kontakty/")}">Обсудить задачу</a></div></header>'''
    foot=f'''<footer><div class="w fg"><div><strong>{e(NAME)}</strong><br>Автоматизация заявок и записей для малого бизнеса.<br>Здесь собраны демонстрационные примеры решений для разных сфер.</div>
<div><strong>Направления</strong>{dd}</div><div><strong>Навигация</strong><a href="{L("uslugi/")}">Услуги</a><a href="{L("portfolio/")}">Портфолио</a><a href="{L("obo-mne/")}">Обо мне</a><a href="{L("kontakty/")}">Контакты</a>{"".join(f'<a href="{u}">{t}</a>' for t,u in chans())}</div></div>
<div class="w"><div class="dis"><b>Важно:</b> этот сайт — демонстрационный проект для презентации моих навыков и примеров возможной автоматизации. Описанные сценарии показывают, как могут быть организованы заявки и записи, но сами по себе не являются подключёнными сервисами для реальных компаний. Упоминания сфер бизнеса не означают, что эти организации являются моими клиентами.</div></div><div class="w" style="margin-top:18px">© {datetime.date.today().year} {e(NAME)}</div></footer>'''
    js="<script>var b=document.getElementById('mb'),n=document.getElementById('nv');b.onclick=function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)};var h=document.querySelector('header'),ly=0;addEventListener('scroll',function(){var y=scrollY;if(n.classList.contains('open')||y<60){h.classList.remove('hide')}else if(y>ly+6){h.classList.add('hide')}else if(y<ly-6){h.classList.remove('hide')}ly=y},{passive:true})</script>"
    os.makedirs(os.path.join(OUT,path),exist_ok=True)
    open(os.path.join(OUT,path,"index.html" if path!="404" else "../404.html") if path!="404" else os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(fix(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(desc)}"><style>:root{{--ac:{color}}}{CSS}</style></head><body id="top">{nav}<main>{body}</main>{foot}{js}</body></html>'))
def cta(text,depth):
    return f'<section class="cta"><div class="w"><h2>Опишите, как у вас сейчас устроены обращения</h2><p>Расскажу, что можно упростить, и сколько это может занять. Стоимость обсуждается после уточнения задачи.</p><a class="btn" href="{"../"*depth}kontakty/">{text}</a></div></section>'
ul=lambda a:'<ul class="ls">'+"".join(f"<li>{e(x)}</li>" for x in a)+"</ul>"
flow=lambda a,c:f'<ul class="flow" style="--c:{c}">'+"".join(f"<li>{e(x)}</li>" for x in a)+"</ul>"
# главная
CAP={"avtoservis":"Заявки на ремонт, статусы заказов и связь с клиентом","stomatologiya":"Запись на приём и напоминания пациентам","salon-krasoty":"Запись к мастерам и контроль обращений","veterinarnaya-klinika":"Заявки, запись и напоминания о визитах","remont-tehniki":"Учёт заказов и уведомления об этапах ремонта","fitnes-studiya":"Заявки на пробные занятия и работа с расписанием"}
cards="".join(f'<a class="tile" href="{s}/"><div class="ph" style="background-image:{PH(s,'images')},linear-gradient(135deg,{c},#14222e)"></div><div class="tx"><h3>{n}</h3><p>{CAP[s]}</p><span class="go">Смотреть решения →</span></div></a>' for s,n,c,h,lead,sit,sc,tasks,no,ct in D)
home=f'''<div class="hero"><section class="w"><h1>Автоматизация для бизнеса, где много обращений и записей</h1><p>Заявки, записи и сообщения можно собрать в понятный процесс: быстрее отвечать клиентам, не забывать о записях и видеть историю работы с ними.</p>
{flow(["Клиент написал","Заявка сохранена","Сотрудник получил уведомление","Клиенту ответили"],"#0f766e")}<a class="btn big" href="kontakty/">Обсудить задачу</a> <a class="btn o" href="#napr">Посмотреть направления</a><div class="chips"><span>6 направлений с примерами</span><span>Демо-проекты без выдуманных отзывов</span></div></section></div>
<section class="w"><h2>Знакомые ситуации</h2>{ul(["Клиент написал в один из мессенджеров, и сообщение потерялось","Администратор забыл перезвонить","Записи ведутся в разных таблицах и блокнотах","Сотрудник не видит, на каком этапе заказ","Трудно найти прошлую переписку или историю визитов"])}<p>Автоматизация может помочь объединить часть этих процессов.</p></section>
<section class="w" id="napr"><h2>Выберите направление — покажу, что можно автоматизировать</h2><p>Для каждого бизнеса — отдельные примеры задач, сценарии работы и возможные решения.</p><div class="tiles">{cards}</div></section>
<section class="w"><h2>Что можно автоматизировать</h2><div class="note">Конкретный набор зависит от задачи и доступных инструментов.</div>{ul(["Сбор заявок из доступных каналов","Уведомления сотрудникам о новых обращениях","Запись данных в таблицу или CRM","Напоминания о записи","Статусы заявок и заказов","Базовая история обращений","Простые формы заявок","Передача обращения ответственному"])}</section>
<section class="w"><h2>Каналы связи</h2><p>Каналы подключаются под задачу, автоматически ничего не включено. Например: «Новая заявка из формы отправляется администратору». Звонки учитываем, если есть понятный способ их фиксировать.</p>{ul(["Сайт","Telegram","WhatsApp","Viber","Электронная почта"])}</section>
<section class="w"><h2>Как проходит работа</h2><ol class="st"><li>Вы описываете задачу.</li><li>Уточняю процесс и ограничения.</li><li>Предлагаю простой вариант решения.</li><li>Согласуем сроки, объём и стоимость.</li><li>Настраиваем и проверяем вместе.</li></ol></section>
<section class="w"><h2>Примеры работ</h2><div class="g"><div class="card"><span class="tag">Демо-проект</span><h3>Заявки автосервиса</h3><p>Задача: собрать обращения в одном месте. Показан сценарий со статусами заказа.</p><a href="portfolio/">Подробнее</a></div><div class="card"><span class="tag">Демо-проект</span><h3>Запись в салон</h3><p>Задача: упорядочить запись и подтверждения.</p><a href="portfolio/">Подробнее</a></div></div></section>
{cta("Обсудить задачу",0)}'''
page("","Автоматизация заявок и записей для малого бизнеса",f"{NAME}: настройка сбора заявок, уведомлений и учёта обращений для автосервисов, клиник, салонов и студий.",home,0)
IC=["M4 5h16v11H9l-5 4z","M12 4a8 8 0 1 0 0 16a8 8 0 0 0 0-16zM12 8v4l3 2","M4 5h16v14H4zM4 10h16M10 10v9","M12 4a4 4 0 1 0 0 8a4 4 0 0 0 0-8zM5 20a7 7 0 0 1 14 0","M3 6h6l2 2h10v11H3z","M6 16v-5a6 6 0 0 1 12 0v5l2 2H4zM10 21h4","M5 12l4 4 10-10","M6 3h9l4 4v14H6zM9 12h7M9 16h7"]
def ic(i,c):return f'<span class="ic" style="--c:{c}"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{IC[i%len(IC)]}"/></svg></span>'
def cardsi(a,c,off=0):return '<div class="g">'+"".join(f'<div class="card ci" style="--c:{c}">{ic(i+off,c)}<p>{e(x)}</p></div>' for i,x in enumerate(a))+'</div>'
for s,n,c,h,lead,sit,sc,tasks,no,ct in D:
    img=PH(s,"../images")
    tl="".join(f'<li><b>{i+1}</b><div>{e(x)}</div></li>' for i,x in enumerate(sc))
    b=f'''<div class="hero d" style="--c:{c};background-image:linear-gradient(90deg,rgba(10,19,26,.96) 8%,rgba(10,19,26,.7) 50%,rgba(10,19,26,.15)),{img}"><section class="w"><h1>{h}</h1><p>{lead}</p><a class="btn big" href="../kontakty/">Обсудить автоматизацию: {n.lower()}</a> <a class="btn o" href="../#napr">Другие направления</a><div class="chips"><span>Сценарий из {len(sc)} шагов</span><span>{len(tasks)} задач для рассмотрения</span><span>Без обещаний результата</span></div></section></div>
<section class="w"><h2>С чем сталкивается этот бизнес</h2>{cardsi(sit,c)}</section>
<section class="w"><h2>Как это может работать</h2><p>Пример сценария: от обращения клиента до ответа сотрудника.</p><div class="two"><ol class="tl" style="--c:{c}">{tl}</ol><div class="pic" style="background-image:{img.replace("../","../")}" role="img" aria-label="Иллюстрация: {n}"></div></div><p>Статусы и сообщения настраиваются только в пределах реально доступных инструментов.</p></section>
<section class="w"><h2>Зачем это нужно</h2><p>Смысл простой: обращение не теряется, сотрудник видит, что делать дальше, а история остаётся перед глазами. Что именно получится, зависит от вашего процесса и выбранных инструментов.</p><div class="ba"><div class="card" style="--c:#7b8b96"><h3>Как часто бывает</h3>{ul(sit[:3])}</div><div class="ar">→</div><div class="card" style="--c:{c}"><h3>Как можно организовать</h3>{ul(tasks[:3])}</div></div></section>
<section class="w"><h2>Что можно рассмотреть</h2>{cardsi(tasks,c,3)}{f'<div class="note" style="margin-top:20px">{no}</div>' if no else ''}</section>{cta(ct,1)}'''
    page(s,f"{n}: автоматизация заявок и записи",lead,b,1,c)
S=[("Приём заявок","Обращения теряются между каналами","Единое место для заявок"),("Уведомления","Сотрудник не знает о новой заявке","Сообщение ответственному"),("Формы записи и заказа","Данные собираются неполно","Короткая форма с нужными полями"),("База заявок и клиентов","Информация разбросана","Таблица или простая CRM"),("Статусы и этапы","Непонятно, что на каком этапе","Список статусов заказа или записи"),("Напоминания","Забывают перезвонить или подтвердить","Напоминание сотруднику или клиенту"),("Консультация по процессу","Неясно, с чего начать","Разбор процесса и простой план")]
sv="".join(f'<div class="card ci svc">{ic(i,"#0f766e")}<div><h3>{a}</h3><p><b>Проблема:</b> {b}.</p><p><b>Результат:</b> {c}.</p></div></div>' for i,(a,b,c) in enumerate(S))
page("uslugi","Услуги","Услуги по автоматизации приёма заявок, уведомлений и учёта обращений.",f'<section class="w"><h1>Услуги</h1><p>Стоимость назначается после обсуждения задачи.</p><div class="g gb">{sv}</div><div class="note" style="margin-top:28px"><b>Для любой услуги:</b> понадобятся описание вашего процесса и доступы к сервисам, которыми вы уже пользуетесь. Срок и стоимость зависят от объёма и инструментов. Интеграции возможны не со всеми системами, это уточняем заранее.</div></section>'+cta("Обсудить задачу",1),1)
page("portfolio","Портфолио","Демонстрационные проекты по автоматизации заявок.",f'<section class="w"><h1>Портфолио</h1><p>Реальных заказов пока нет, поэтому ниже учебные и демонстрационные проекты. Они так и подписаны.</p><div class="g"><div class="card"><div class="pic sm" style="background-image:{PH("avtoservis","../images")}"></div><span class="tag">Демо-проект</span><h3>Заявки автосервиса</h3><p><b>Сфера:</b> автосервис. <b>Задача:</b> собрать обращения в одном месте. <b>Сценарий:</b> заявка, уведомление, статусы заказа. <b>Ограничения:</b> смоделированный сценарий без реальных клиентов.</p><a class="btn o" href="../kontakty/">Обсудить похожую задачу</a></div><div class="card"><div class="pic sm" style="background-image:{PH("salon-krasoty","../images")}"></div><span class="tag">Учебный пример</span><h3>Запись в салон красоты</h3><p><b>Сфера:</b> салон. <b>Задача:</b> упорядочить запись и подтверждения. <b>Сценарий:</b> запрос, выбор мастера, статус записи. <b>Ограничения:</b> демонстрация, не рабочая система.</p><a class="btn o" href="../kontakty/">Обсудить похожую задачу</a></div></div></section>',1)
page("obo-mne","Обо мне",f"{NAME}: чем занимаюсь и как работаю.",f'''<section class="w"><h1>Обо мне</h1><p>Меня зовут {e(NAME)}. Я помогаю малому бизнесу упорядочить приём заявок и записей: продумываю простые сценарии обработки обращений, настраиваю формы и собираю заявки в удобную таблицу.</p></section>
<section class="w"><div class="ba" style="grid-template-columns:1fr 1fr"><div class="card" style="--c:#0f766e"><h3>Что я могу сделать</h3>{ul(["Создать форму для заявок, записи или предварительного заказа.","Настроить сбор ответов в таблицу с контактами, датой обращения и его статусом.","Продумать понятные этапы обработки заявки: например, «Новая», «Связались», «Записан», «Завершена».","Подготовить шаблоны ответов на частые вопросы клиентов.","Настроить простые уведомления о новых заявках, если выбранный сервис это поддерживает.","Описать сценарий работы с обращениями для владельца или сотрудников бизнеса.","Подготовить демонстрационный вариант решения под конкретную сферу.","Помочь определить, какие части процесса можно упростить и какие инструменты для этого подойдут."])}</div><div class="card" style="--c:#b45309"><h3>Что пока не делаю</h3>{ul(["Не разрабатываю сложные корпоративные CRM-системы.","Не подключаю закрытые системы без необходимых доступов и технических возможностей.","Не создаю сервисы, которые ставят диагнозы или дают медицинские рекомендации.","Не обещаю гарантированный рост продаж или определённое количество клиентов.","Не берусь за автоматизацию, если нужный сервис не позволяет безопасно и надёжно её настроить."])}</div></div><p style="margin-top:24px">Конкретный состав работ, сроки и стоимость обсуждаются после того, как станет понятна задача.</p></section>{cta("Обсудить задачу",1)}''',1)
cb="".join(f'<a class="btn" href="{u}">{t}</a>' for t,u in chans()) or '<div class="note">Контакты пока не указаны. Заполните TELEGRAM, WHATSAPP, VIBER или EMAIL в начале build.py и пересоберите сайт.</div>'
page("kontakty","Контакты","Как связаться и обсудить автоматизацию.",f'<section class="w"><h1>Контакты</h1><p>Напишите, какая у вас сфера, в чём проблема и какой результат нужен. Заготовка сообщения: «Здравствуйте! У меня [тип бизнеса]. Сейчас обращения обрабатываются так: [описание]. Хочу обсудить автоматизацию.»</p><div class="bt">{cb}</div><p>Я отвечу вручную. Заявки на сайте не сохраняются, он работает без серверной части.</p></section>',1)
page("404","Страница не найдена","Такой страницы нет.",f'<section class="w"><h1>Страница не найдена</h1><a class="btn" href="{BASE}/">На главную</a><ul class="ls">'+"".join(f'<li><a href="{BASE}/{s}/">{n}</a></li>' for s,n,*_ in D)+'</ul></section>',0)
