import os
OUT='/home/claude/site2'
PHONE='+375 (29) 577-32-23'; TEL='tel:+375295773223'
NAV=[('wedding.html','Свадьбы'),('events.html','События'),('themes.html','Образы'),('services.html','Услуги и цены'),('gallery.html','Видео и фото'),('about.html','Обо мне')]

def head(title,desc):
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;1,500;1,700&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/base.css">
<link rel="stylesheet" href="assets/pages.css">
</head>
<body>
'''

def header(active):
    items=''.join('<li><a href="%s"%s>%s</a></li>'%(h,(' aria-current="page"' if h==active else ''),t) for h,t in NAV)
    mob=''.join(f'<a href="{h}" style="--i:{i}">{t}</a>' for i,(h,t) in enumerate([('index.html','Главная')]+NAV+[('contacts.html','Контакты')]))
    return f'''<header class="nav" id="nav">
  <a class="logo" href="index.html"><i></i>Александр Сербун</a>
  <ul class="menu">{items}</ul>
  <div class="nav__r"><a class="pill" href="contacts.html" data-mag><span>Узнать дату</span></a><button class="burger" id="burger" aria-label="Меню" aria-expanded="false"><span></span><span></span></button></div>
</header>
<nav class="mnav" aria-label="Меню">{mob}<small>{PHONE}</small></nav>
'''

def cta(h='Давайте <em>закрепим дату</em>'):
    return f'''<section class="sec sec--dark cta">
  <div class="wrap">
    <div class="kick">Контакты</div>
    <h2 class="h2 sr">{h}</h2>
    <p class="sub sr">Ваш праздник — ваша история. А я готов стать её частью в любом образе.</p>
    <div class="cta__row sr"><a class="pill pill--lg" href="contacts.html" data-mag><span>Оставить заявку</span><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a><a class="phone" href="{TEL}">{PHONE}</a></div>
  </div>
</section>
'''

def footer():
    links=''.join(f'<a href="{h}">{t}</a>' for h,t in NAV)
    return f'''<footer class="foot2">
  <div class="foot2__grid">
    <div><b>Александр Сербун</b><p>Ведущий · организатор мероприятий · праздники под ключ. Свадьбы, юбилеи, дни рождения, новогодние вечера, корпоративы.</p></div>
    <div><h4>Разделы</h4><a href="index.html">Главная</a>{links}<a href="contacts.html">Контакты</a></div>
    <div><h4>Связаться</h4><a href="{TEL}">{PHONE}</a><a href="contacts.html">Форма заявки</a></div>
  </div>
  <div class="foot2__bot">© Александр Сербун</div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
'''

def im(i,alt,ratio='3/4',cls='',pos='50% 25%'):
    return f'<figure class="gi {cls} sr" style="aspect-ratio:{ratio}"><img src="img/p/{i:02d}.jpg" alt="{alt}" loading="lazy" style="object-position:{pos}"></figure>'

def mos(items,cls='mos'):
    return f'<div class="{cls}">'+''.join(im(i,a,r,pos=p) for i,a,r,p in items)+'</div>'

CLIENTS=['Burger King (Беларусь)','Sbarro (Италия)','МинскКристаллТрейд','Marriott hotel','РУП «Белгоспроект»','BELITSOFT','Renaissance hotel','Hyatt Regency','Научно-технологический парк БНТУ «Политехник»','beCloud','EKT','Первый импортер Xiaomi в Беларуси','Все ведущие вузы страны']
def clients(dark=False):
    return '<div class="chips chips--cl sr">'+''.join(f'<span class="chip">{c}</span>' for c in CLIENTS)+'</div>'

REASONS=[("Современный стиль ведения","Без нафталина и шаблонных сценариев."),("Актуальные развлечения","Интерактивы, которые нравятся гостям сегодня."),("Уместный юмор","Шутки, которые работают для вашей аудитории."),("Современная подача традиций","Традиции в новом, живом формате."),("Мультимедийный формат","Экраны, видео, музыка и свет работают на программу."),("Оригинальные сценарные ходы","Авторские идеи под ваш праздник."),("Умение найти язык с каждым гостем","От юбиляра до самых юных гостей."),("Свадьбы по всему миру","Готов оказаться в любой точке мира.")]
def reasons():
    return '<div class="tk">'+''.join(f'<div class="tk__row sr"><span class="tk__n">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(REASONS,1))+'</div>'

def phead(kick,h1_lines,sub,crumb,word=''):
    lns=''.join(f'<span class="ln" style="--i:{i}"><span>{l}</span></span>' for i,l in enumerate(h1_lines))
    return f'''<section class="phead">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Главная</a><span>/</span><span>{crumb}</span></div>
    <div class="kick">{kick}</div>
    <h1 class="h1">{lns}</h1>
    <p class="sub">{sub}</p>
  </div>
  <div class="phead__word" aria-hidden="true">{word}</div>
</section>
'''

def page(fn,title,desc,active,body):
    open(f'{OUT}/{fn}','w',encoding='utf8').write(head(title,desc)+header(active)+body+footer())

PKG_ITEMS=[('Ведущий — Александр Сербун','Авторская развлекательная программа и интерактивы, без шаблонных сценариев.'),
('Профессиональный DJ','Музыка под ваш праздник и гостей.'),
('Звуковое оборудование до 4 кВт','Доставка, монтаж и демонтаж входят.'),
('Сценический свет','Световое оборудование для площадки.'),
('Микрофоны и караоке','Для тостов, поздравлений и песен гостей.'),
('Телевизор на стойке',''),
('Розыгрыш алкогольного подарка','Для одного из гостей.')]
def pkg_list():
    s='<ol class="list">'
    for i,(b,p) in enumerate(PKG_ITEMS,1):
        s+=f'<li class="sr"><span class="n">{i:02d}</span><div><b>{b}</b>{f"<p>{p}</p>" if p else ""}</div></li>'
    return s+'</ol>'
def pkg_block(kick='Пакет'):
    return f'''<div class="wrap pkg">
    <div class="pkg__left sr">
      <div class="kick">{kick}</div>
      <h2 class="h2">Один пакет — <em>всё включено</em></h2>
      <p class="sub">Вам не нужно искать отдельных специалистов и согласовывать их работу. Ведущий, DJ и техника — одна команда.</p>
      <div class="price"><b>3 200</b><span>руб.</span></div>
      <div class="chips"><span class="chip">Время начала и окончания не влияет на цену</span><span class="chip">Предоплата 600 руб. входит в стоимость</span></div>
    </div>
    {pkg_list()}
  </div>'''

ARROW='<svg class="tk__arrow" viewBox="0 0 24 24"><path d="M7 7h10v10M7 17 17 7"/></svg>'
def steps():
    return '''<div class="steps sr">
      <div class="step"><i>1</i><h3>Напишите дату</h3><p>Укажите дату, место и количество гостей. Подтвержу, свободна ли дата, и расскажу про формат.</p></div>
      <div class="step"><i>2</i><h3>Созвонимся на 5–10 минут</h3><p>Вы расскажете, каким видите праздник, а я предложу идеи по программе, музыке и тематике.</p></div>
      <div class="step"><i>3</i><h3>Закрепим дату</h3><p>Предоплата 600 руб. входит в общую стоимость. Дата остаётся за вами, дальше спокойно готовим детали.</p></div>
    </div>'''

def faq(items):
    return '<div class="faq">'+''.join(f'<details><summary>{q}<i></i></summary><p>{a}</p></details>' for q,a in items)+'</div>'

# ============ HOME ============
home=f'''<section class="hero" id="hero">
  <div class="stage-clip">
    <div class="stage-wrap">
      <div class="stage" id="stage">
        <img class="bg" src="img/hero-wide.jpg" alt="Ведущий мероприятий подбрасывает микрофон" fetchpriority="high">
        <div class="mic"><div class="mic-a"><img src="img/mic.png" alt=""></div></div>
      </div>
    </div>
  </div>
  <div class="eyebrow">Ведущий · DJ · Организатор</div>
  <h1 class="hero__title title">
    <span class="ln" style="--i:0"><span>Ваш праздник —</span></span>
    <span class="ln" style="--i:1"><span><em>ваша история<svg viewBox="0 0 300 14" preserveAspectRatio="none" aria-hidden="true"><path d="M2 9 C 40 2, 70 14, 110 7 S 190 3, 230 9 S 280 6, 298 5"/></svg></em></span></span>
  </h1>
  <div class="hero__spacer"></div>
  <div class="lower">
    <p class="lede rv" style="--d:0">Ведущий, DJ, звук и свет в одном пакете. А ещё тематические образы, артисты и организация праздника под ключ.</p>
    <div class="acts rv" style="--d:1">
      <a class="pill pill--lg" href="contacts.html" data-mag><span>Проверить дату</span><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      <a class="pill pill--lg pill--ghost" href="services.html" data-mag><span>Что входит</span></a>
    </div>
  </div>
  <aside class="avail rv" style="--d:2">
    <small><i class="dot"></i>Принимаю заявки</small>
    <b>Полный пакет</b>
    <span class="s">3 200 руб. Время начала и окончания на стоимость не влияет.</span>
  </aside>
  <div class="cue" aria-hidden="true"></div>
</section>

<section class="strip" aria-label="Форматы мероприятий">
  <div class="track">{('<span>Свадьбы</span><span>Юбилеи</span><span>Дни рождения</span><span>Новогодние вечера</span><span>Корпоративы</span>'*2)}</div>
</section>

<section class="nums">
  <div class="nums__grid">
    <div class="num sr" style="--d:0"><b><span data-count="3200" data-fmt="1">0</span><i> руб.</i></b><p>полный пакет: ведущий, DJ, звук, свет, караоке и программа</p></div>
    <div class="num sr" style="--d:1"><b><span data-count="600">0</span><i> руб.</i></b><p>предоплата за бронь даты, входит в стоимость</p></div>
    <div class="num sr" style="--d:2"><b><span data-count="1">0</span><i> команда</i></b><p>ведущий, DJ, техника, фото и видео, артисты: без поиска подрядчиков</p></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="kick">Разделы</div>
    <h2 class="h2 sr">Выберите <em>свой формат</em></h2>
    <div class="tk">
      <a class="tk__row has-arrow sr" href="wedding.html"><span class="tk__n">01</span><h3>Свадьбы</h3><p>Камерные и яркие, без навязанных конкурсов и шаблонных сценариев.</p>{ARROW}</a>
      <a class="tk__row has-arrow sr" href="events.html"><span class="tk__n">02</span><h3>Корпоративы и события</h3><p>Корпоративы, юбилеи, дни рождения, новогодние вечера.</p>{ARROW}</a>
      <a class="tk__row has-arrow sr" href="themes.html"><span class="tk__n">03</span><h3>Праздник в любом образе</h3><p>Мексиканский, итальянский, Голливуд, ретро: костюмированный образ ведущего.</p>{ARROW}</a>
      <a class="tk__row has-arrow sr" href="services.html"><span class="tk__n">04</span><h3>Услуги и цены</h3><p>Что входит в пакет, фото и видео, артисты и организация под ключ.</p>{ARROW}</a>
      <a class="tk__row has-arrow sr" href="gallery.html"><span class="tk__n">05</span><h3>Видео и фото</h3><p>Как это выглядит на самом деле.</p>{ARROW}</a>
      <a class="tk__row has-arrow sr" href="about.html"><span class="tk__n">06</span><h3>Обо мне</h3><p>Ведущий, организатор мероприятий, праздники под ключ.</p>{ARROW}</a>
    </div>
  </div>
</section>

<section class="sec sec--dark">
  <div class="wrap">
    <div class="kick">Как заказать</div>
    <h2 class="h2 sr">Три шага до <em>вашего праздника</em></h2>
    {steps()}
  </div>
</section>
'''
home=home+f'''<section class="sec sec--tight"><div class="wrap"><div class="kick">Моменты</div><h2 class="h2 sr" style="margin-bottom:36px">Праздники <em>изнутри</em></h2>'''+mos([(20,'Александр Сербун с микрофоном','3/4','30% 30%'),(77,'Караоке с гостями','3/4','60% 40%'),(83,'Образ мексиканца','3/4','35% 55%'),(36,'Микрофон в воздухе','3/4','50% 50%')])+'<div class="cta__row" style="margin-top:34px"><a class="pill pill--lg" href="gallery.html" data-mag><span>Вся галерея</span><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div></div></section>'+f'''<section class="sec sec--dark"><div class="wrap"><div class="kick">Мне доверяют</div><h2 class="h2 sr">Бренды и компании, <em>с которыми работаю</em></h2>{clients()}</div></section>'''+cta()
# home needs hero-specific head: reuse generic head, hero CSS already in base.css
page('index.html','Александр Сербун · Ведущий и организатор мероприятий','Александр Сербун: ведущий, DJ и организатор праздников под ключ. Свадьбы, юбилеи, корпоративы. Полный пакет — 3 200 руб.','index.html',home)

# ============ WEDDING ============
wed=phead('Свадьбы',['Свадьба без','<em>шаблонных сценариев</em>'],'Камерный вечер или яркая вечеринка: строим праздник на вашем стиле и пожеланиях, без навязанных конкурсов.','Свадьбы','Свадьба')
wed+=f'''<section class="sec sec--tight">
  <div class="wrap">
    <div class="kick">Какой будет ваша свадьба</div>
    <div class="g3 mt">
      <div class="card sr"><span class="n">01</span><h3>Камерная</h3><p>До 25 гостей. Здесь особенно важны атмосфера, эмоции и внимание к каждому гостю.</p></div>
      <div class="card sr"><span class="n">02</span><h3>Яркая вечеринка</h3><p>DJ, сценический свет, караоке и авторская программа с интерактивами.</p></div>
      <div class="card sr"><span class="n">03</span><h3>Тематическая</h3><p>Мексиканская, итальянская, в стиле Голливуда или ретро: костюмированный образ ведущего под вашу тему.</p></div>
    </div>
  </div>
</section>
<section class="sec" id="package">{pkg_block('Что входит')}</section>
<section class="sec sec--tight"><div class="wrap"><div class="kick">Из свадеб</div>{mos([(71,'Выездная церемония','3/4','60% 30%'),(51,'Свадебный вечер','3/4','80% 30%'),(41,'Танцы на лужайке','3/4','50% 40%'),(9,'Тост на свадьбе','3/4','50% 30%')])}</div></section>
<section class="sec sec--dark">
  <div class="wrap about">
    <div class="sr"><div class="kick">Фото и видео</div><h2 class="h2">Ваша свадьба <em>в кадре</em></h2>
    <p class="sub">Собственная команда фотографов и видеооператоров. Полный цикл съёмки под ключ — 1 200 USD. Единая координация, без поиска и контроля подрядчиков.</p>
    <div class="cta__row"><a class="pill pill--lg" href="services.html" data-mag><span>Все услуги</span><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div></div>
    <div class="g2">{im(75,'Церемония у арки','4/5',pos='50% 40%')}<div style="margin-top:40px">{im(65,'Молодожёны и ведущий','4/5',pos='45% 30%')}</div></div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="kick">Отзывы</div>
    <h2 class="h2 sr">Говорят <em>молодожёны</em></h2>
    <div class="g3 mt">
      <div class="card sr"><span class="n">«</span><h3>Отзыв пары</h3><p>Здесь будет текст отзыва, имена и дата свадьбы.</p></div>
      <div class="card sr"><span class="n">«</span><h3>Отзыв пары</h3><p>Здесь будет текст отзыва, имена и дата свадьбы.</p></div>
      <div class="card sr"><span class="n">«</span><h3>Отзыв пары</h3><p>Здесь будет текст отзыва, имена и дата свадьбы.</p></div>
    </div>
  </div>
</section>
<section class="sec sec--tight">
  <div class="wrap">
    <div class="kick">Вопросы и ответы</div>
    <h2 class="h2 sr" style="margin-bottom:40px">Что <em>спрашивают чаще всего</em></h2>
    {faq([('Влияет ли время начала и окончания на цену?','Нет. Время начала и окончания мероприятия на стоимость не влияет: мы подстраиваемся под ваш праздник, а не под часы.'),
    ('Сколько стоит и что входит?','Полный пакет — 3 200 руб. В него входят ведущий, DJ, звуковое оборудование до 4 кВт с доставкой, монтажом и демонтажем, сценический свет, микрофоны и караоке, телевизор на стойке, авторская программа и интерактивы.'),
    ('Как забронировать дату?','Предоплата — 600 руб., она входит в общую стоимость пакета. После бронирования дата закрепляется за вами.'),
    ('Можно ли свадьбу в определённой стилистике?','Да. Свадьба может быть мексиканской, итальянской, в стиле Голливуда, ретро или в совершенно необычной концепции. Стоимость костюмов и индивидуальной постановки согласуется отдельно.'),
    ('Вы поможете с фото, видео и артистами?','Да. Есть собственная команда фотографов и видеооператоров (1 200 USD под ключ), а также организация выступлений артистов. Участие и гонорары согласуются индивидуально.')])}
  </div>
</section>
'''+cta()
page('wedding.html','Свадьбы · Александр Сербун','Ведущий и DJ на свадьбу в Беларуси: полный пакет 3 200 руб., тематические образы, фото и видео.','wedding.html',wed)

# ============ EVENTS ============
ev=phead('Корпоративы и события',['Любой повод,','<em>один формат — ваш</em>'],'Корпоративы, юбилеи, дни рождения и новогодние вечера: программа, музыка и техника под вашу компанию.','События','События')
ev+=f'''<section class="sec sec--tight">
  <div class="wrap">
    <div class="tk">
      <div class="tk__row sr"><span class="tk__n">01</span><h3>Корпоративы</h3><p>Классический корпоратив с развлекательной программой или тематический вечер с полноценной шоу-концепцией. Также: подбор артистов, звёзд белорусской и российской эстрады, и комплексная организация под ключ.</p></div>
      <div class="tk__row sr"><span class="tk__n">02</span><h3>Юбилеи</h3><p>Продумаем формат с учётом вашей компании: необычная тематика, костюмированный образ ведущего, приглашённые артисты. Для расчёта нужны дата, место, количество гостей и возраст юбиляра.</p></div>
      <div class="tk__row sr"><span class="tk__n">03</span><h3>Дни рождения</h3><p>Один общий праздник на двух именинников в одном кафе рассматриваем как одно мероприятие. Программа строится так, чтобы у каждого был свой яркий момент, а у гостей единый отличный вечер.</p></div>
      <div class="tk__row sr"><span class="tk__n">04</span><h3>Новогодние вечера</h3><p>От семейного вечера для своих до зажигательной вечеринки. Можно в любой стилистике: итальянской, мексиканской или новогодней ретро.</p></div>
    </div>
  </div>
</section>
<section class="sec sec--tight"><div class="wrap"><div class="kick">Атмосфера вечеров</div>{mos([(61,'Гости на танцполе','3/4','50% 40%'),(62,'Танцы','3/4','50% 40%'),(78,'Вечеринка с караоке','3/4','50% 50%'),(4,'Выступление танцовщиц','3/4','50% 30%')])}</div></section>
<section class="sec" id="package">{pkg_block('Что входит')}</section>
<section class="sec sec--dark">
  <div class="wrap">
    <div class="kick">Нам доверяют</div>
    <h2 class="h2 sr">Мне <em>доверяют</em></h2>
    {clients()}
  </div>
  </div>
</section>
'''+cta('Расскажите про ваше <em>мероприятие</em>')
page('events.html','Корпоративы и события · Александр Сербун','Ведущий и DJ на корпоратив, юбилей, день рождения и новогодний вечер. Полный пакет 3 200 руб.','events.html',ev)

# ============ THEMES ============
themes=[('Мексиканский','Яркий, жаркий, с характером.'),('Итальянский','Стиль и атмосфера Италии.'),('Голливуд','Красная дорожка и свет софитов.'),('Ретро','Вечеринка из другой эпохи.')]
th=phead('Образы',['Праздник в','<em>любом образе</em>'],'Под выбранную тему готовлю костюмированный образ ведущего, манеру подачи, тематические элементы программы и развлечения. Каждую концепцию разрабатываем отдельно.','Образы','Образ')
th+='<section class="sec sec--tight"><div class="wrap"><div class="tk">'
for i,(n,d) in enumerate(themes,1):
    pic={1:(74,'50% 30%'),4:(70,'40% 30%')}.get(i)
    box=im(pic[0],'Образ: '+n,'4/3',pos=pic[1]) if pic else '<div class="ph" style="aspect-ratio:4/3"><span>Фото образа</span></div>'
    th+=f'<div class="tk__row sr" style="grid-template-columns:90px minmax(0,4fr) minmax(0,3fr) minmax(0,3fr);align-items:center"><span class="tk__n">{i:02d}</span><h3>{n}</h3><p>Костюмированный образ ведущего, манера подачи и элементы программы под тему «{n.lower()}».</p>{box}</div>'
th+=f'''<div class="tk__row sr" style="grid-template-columns:90px minmax(0,4fr) minmax(0,6fr)"><span class="tk__n">05</span><h3>Ваша идея</h3><p>Совершенно необычная концепция? Придумаем вместе и разработаем отдельно под ваш праздник и вашу компанию.</p></div>
</div><p class="note" style="color:var(--muted);margin-top:26px">Это не готовый шаблон, который повторяется из мероприятия в мероприятие. Стоимость костюмов и индивидуальной постановки согласуется отдельно.</p></div></section>'''+cta('Какой образ <em>выберете вы?</em>')
page('themes.html','Тематические образы · Александр Сербун','Мексиканский, итальянский, голливудский и ретро-образ ведущего для вашего праздника.','themes.html',th)

# ============ SERVICES ============
sv=phead('Услуги и цены',['Прозрачно:','<em>что и сколько</em>'],'Один пакет закрывает всё необходимое. Остальное подключаем по желанию.','Услуги и цены','Цены')
sv+=f'''<section class="sec sec--tight" id="package">{pkg_block('Полный пакет')}</section>
<section class="sec sec--dark">
  <div class="wrap">
    <div class="kick" style="color:#fff">Цены</div>
    <h2 class="h2 sr" style="margin-bottom:36px">Всё в <em>одной таблице</em></h2>
    <div class="ptable sr" style="border-color:#fff;color:#fff">
      <div style="border-color:rgba(255,255,255,.16)"><b>Полный пакет</b><span style="color:#aeada9">Ведущий, DJ, звук, свет, микрофоны, караоке, ТВ, программа</span><strong>3 200 руб.</strong></div>
      <div style="border-color:rgba(255,255,255,.16)"><b>Предоплата</b><span style="color:#aeada9">Закрепляет дату, входит в стоимость пакета</span><strong>600 руб.</strong></div>
      <div style="border-color:rgba(255,255,255,.16)"><b>Фото и видео</b><span style="color:#aeada9">Своя команда фотографов и операторов, полный цикл под ключ</span><strong>1 200 USD</strong></div>
      <div style="border-color:rgba(255,255,255,.16)"><b>Костюмы и постановка</b><span style="color:#aeada9">Индивидуальный образ ведущего и тематическая концепция</span><strong class="soft">Отдельно</strong></div>
      <div style="border-color:rgba(255,255,255,.16)"><b>Артисты и звёзды эстрады</b><span style="color:#aeada9">Подбор, переговоры, райдеры; гонорары согласуются индивидуально</span><strong class="soft">Индивидуально</strong></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="kick">Под ключ</div>
    <h2 class="h2 sr">От идеи до <em>финального аккорда</em></h2>
    <p class="sub sr">Я занимаюсь не только проведением, но и полной организацией мероприятий: концепция, сценарий, артисты, техника, съёмка и координация в одних руках.</p>
    <div class="tk">
      <div class="tk__row sr"><span class="tk__n">01</span><h3>Фото и видео</h3><p>Собственная команда фотографов и видеооператоров, полный цикл съёмки — <b>1 200 USD</b>. Единая координация, без поиска подрядчиков.</p></div>
      <div class="tk__row sr"><span class="tk__n">02</span><h3>Артисты и звёзды эстрады</h3><p>Музыкальные коллективы и кавер-группы, шоу-балет и танцевальные коллективы, артисты оригинального жанра, исполнители белорусской и российской эстрады.</p></div>
      <div class="tk__row sr"><span class="tk__n">03</span><h3>Идея и концепция</h3><p>Разработка идеи, тематики и сценария праздника под вашу компанию.</p></div>
      <div class="tk__row sr"><span class="tk__n">04</span><h3>Координация</h3><p>Все услуги в одних руках: вы получаете удовольствие от праздника, организацией занимаемся мы.</p></div>
    </div>
  </div>
</section>
<section class="sec sec--dark">
  <div class="wrap"><div class="kick">Как заказать</div><h2 class="h2 sr">Три шага до <em>вашего праздника</em></h2>{steps()}</div>
</section>
'''+cta()
page('services.html','Услуги и цены · Александр Сербун','Полный пакет ведущего с DJ — 3 200 руб., предоплата 600 руб., фото и видео — 1 200 USD.','services.html',sv)

# ============ GALLERY ============
G=[('look',[74,40,70]),('wed',[75,71,65,45]),('party',[61,62,77,4,35,17]),('host',[48,64,68,63,52,6])]
gal=phead('Видео и фото',['Как это','<em>выглядит</em>'],'Выступления и фрагменты праздников: свадьбы, вечеринки, тематические образы.','Видео и фото','Кадр')
gal+='''<section class="sec sec--tight"><div class="wrap">
<div class="filters"><button class="on" data-f="all">Все</button><button data-f="wed">Свадьбы</button><button data-f="party">Вечеринки</button><button data-f="look">Образы</button><button data-f="host">Портреты</button></div>
<div class="mason">
<figure class="gi gi--vid" data-c="look"><video src="img/clip.mp4" poster="img/clip.jpg" controls playsinline preload="none"></video></figure>'''
import itertools
mx=max(len(v) for _,v in G)
for k in range(mx):
    for c,v in G:
        if k<len(v): gal+=f'<figure class="gi" data-c="{c}"><img src="img/p/{v[k]:02d}.jpg" alt="Александр Сербун" loading="lazy"></figure>'
gal+='</div></div></section><div class="lb" id="lb"><img alt=""></div>'+cta()
page('gallery.html','Видео и фото · Александр Сербун','Видео и фотографии с мероприятий: свадьбы, корпоративы, юбилеи.','gallery.html',gal)

# ============ ABOUT ============
ab=phead('Обо мне',['Александр','<em>Сербун</em>'],'Ведущий, организатор мероприятий, праздники под ключ.','Обо мне','Обо мне')
ab+=f'''<section class="sec sec--tight">
  <div class="wrap about">
    <div class="about__img sr"><img src="img/p/64.jpg" alt="Александр Сербун" style="object-position:50% 8%"></div>
    <div class="sr">
      <p class="quote">Ваш праздник — ваша история. А я готов стать её частью <em>в любом образе!</em></p>
      <p class="sub">Ведущий, организатор и сценарист, более 15 лет опыта и большой опыт публичных выступлений. Каждое торжество делаю ярким и памятным, чтобы оно стало неповторимым.</p>
      <p class="sub" style="margin-top:14px">Работаю в паре со своим DJ и всегда готовим вам подарок. Готов оказаться в любой точке мира: свадьбы по всему миру.</p>
      <div class="chips"><span class="chip">15+ лет опыта</span><span class="chip">Instagram: serbunby</span></div>
    </div>
  </div>
</section>
<section class="sec sec--tight"><div class="wrap">{mos([(48,'Александр Сербун','3/4','50% 25%'),(68,'Александр Сербун','3/4','50% 40%'),(19,'Александр Сербун','3/4','60% 50%'),(3,'Александр Сербун','3/4','50% 25%')])}</div></section>
<section class="sec">
  <div class="wrap">
    <div class="kick">Выбрав меня, вы получите</div>
    <div class="g3 mt">
      <div class="card sr"><span class="n">01</span><h3>Яркого гостя</h3><p>На свой праздник: человека, готового разделить и приумножить вашу радость и хорошее настроение.</p></div>
      <div class="card sr"><span class="n">02</span><h3>Харизматичного ведущего</h3><p>Уверенная подача, чувство зала и умение найти язык с каждым гостем.</p></div>
      <div class="card sr"><span class="n">03</span><h3>Добросовестного помощника</h3><p>В режиссуре, координации и постановке вашего события.</p></div>
    </div>
  </div>
</section>
<section class="sec sec--tight">
  <div class="wrap">
    <div class="kick">8 причин</div>
    <h2 class="h2 sr" style="margin-bottom:36px">Почему стоит выбрать <em>именно меня</em></h2>
    {reasons()}
  </div>
</section>
<section class="sec sec--dark">
  <div class="wrap">
    <div class="kick">Мне доверяют</div>
    <h2 class="h2 sr">Компании, <em>для которых работал</em></h2>
    {clients()}
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="kick">Мой подход</div>
    <h2 class="h2 sr">Продаю не киловатты, <em>а результат</em></h2>
    <div class="g3 mt">
      <div class="card sr"><span class="n">01</span><h3>Комфорт клиента</h3><p>Вы получаете удовольствие от самого процесса, пока организационными вопросами занимаемся мы.</p></div>
      <div class="card sr"><span class="n">02</span><h3>Атмосфера для гостей</h3><p>Без навязанных конкурсов и шаблонных сценариев: программа строится на вашем стиле и пожеланиях.</p></div>
      <div class="card sr"><span class="n">03</span><h3>Единая координация</h3><p>Ведущий, DJ, техника, съёмка и артисты: одна команда вместо десятка подрядчиков.</p></div>
    </div>
  </div>
</section>
'''+cta()
page('about.html','Обо мне · Александр Сербун','Александр Сербун: ведущий, организатор мероприятий, праздники под ключ.','about.html',ab)

# ============ CONTACTS ============
ct=phead('Контакты',['Давайте','<em>закрепим дату</em>'],'Оставьте заявку или позвоните. Подтвержу, свободна ли дата, и предложу формат под ваш праздник.','Контакты','Дата')
ct+=f'''<section class="sec sec--tight">
  <div class="wrap contact">
    <div class="sr">
      <a class="phone" href="{TEL}" style="margin-top:0">{PHONE}</a>
      <div class="chips" style="margin-top:34px"><span class="chip">Telegram: добавим</span><span class="chip">Instagram: serbunby</span><span class="chip">Город: добавим</span></div>
      <p class="sub">Предоплата 600 руб. входит в стоимость и закрепляет дату за вами. Время начала и окончания на цену не влияет.</p>
    </div>
    <form class="form sr" id="lead" autocomplete="off" style="background:#121212;color:#fff">
      <div class="row2"><label>Ваше имя<input name="name" required placeholder="Как к вам обращаться"></label><label>Телефон или Telegram<input name="contact" required placeholder="+375 …"></label></div>
      <div class="row2"><label>Дата праздника<input name="date" type="date"></label><label>Гостей<input name="guests" inputmode="numeric" placeholder="Примерно"></label></div>
      <label>Тип праздника<select name="type"><option>Свадьба</option><option>Юбилей</option><option>День рождения</option><option>Новогодний вечер</option><option>Корпоратив</option><option>Другое</option></select></label>
      <button class="pill pill--lg" type="submit"><span>Отправить заявку</span><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
      <div class="result" id="res"></div>
    </form>
  </div>
</section>
'''
page('contacts.html','Контакты · Александр Сербун','Свободна ли ваша дата? Оставьте заявку или позвоните: +375 (29) 577-32-23.','contacts.html',ct)
print('ok')
