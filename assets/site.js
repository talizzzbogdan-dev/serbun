(function(){
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  var root=document.documentElement, nav=document.getElementById('nav'), hero=document.getElementById('hero');
  var tx=0,ty=0,cx=0,cy=0;

  /* mobile menu */
  var bg=document.getElementById('burger');
  if(bg) bg.addEventListener('click',function(){
    var o=root.classList.toggle('menu-open'); bg.setAttribute('aria-expanded',o);
  });
  document.querySelectorAll('.mnav a').forEach(function(a){a.addEventListener('click',function(){root.classList.remove('menu-open')})});

  /* nav state + scroll parallax */
  function onScroll(){
    var y=window.scrollY||0;
    if(nav) nav.classList.toggle('is-stuck',y>40);
    if(hero){
      var h=hero.offsetHeight, p=Math.min(Math.max(y/h,0),1);
      root.style.setProperty('--sy',(y*.18).toFixed(1));
      root.style.setProperty('--sz',(p*.05).toFixed(4));
    }
  }
  addEventListener('scroll',onScroll,{passive:true}); onScroll();

  /* mouse parallax on hero (desktop) */
  if(hero && !reduce && matchMedia('(hover:hover) and (min-width:901px)').matches){
    hero.addEventListener('mousemove',function(e){
      var r=hero.getBoundingClientRect();
      tx=((e.clientX-r.left)/r.width-.5)*2; ty=((e.clientY-r.top)/r.height-.5)*2;
    });
    hero.addEventListener('mouseleave',function(){tx=0;ty=0});
    (function loop(){
      cx+=(tx-cx)*.07; cy+=(ty-cy)*.07;
      root.style.setProperty('--mx',cx.toFixed(4)); root.style.setProperty('--my',cy.toFixed(4));
      requestAnimationFrame(loop);
    })();
  }

  /* magnetic buttons */
  if(!reduce && matchMedia('(hover:hover)').matches){
    document.querySelectorAll('[data-mag]').forEach(function(el){
      el.addEventListener('mousemove',function(e){
        var r=el.getBoundingClientRect();
        el.style.transform='translate('+((e.clientX-r.left-r.width/2)*.22)+'px,'+((e.clientY-r.top-r.height/2)*.3)+'px)';
      });
      el.addEventListener('mouseleave',function(){el.style.transform=''});
    });
  }

  /* scroll reveal + count-up */
  var io=new IntersectionObserver(function(es){
    es.forEach(function(en){
      if(!en.isIntersecting) return;
      en.target.classList.add('in'); io.unobserve(en.target);
      var c=en.target.querySelector('[data-count]');
      if(c){
        var to=+c.dataset.count, t0=performance.now(), d=reduce?1:1800;
        (function step(t){
          var k=Math.min((t-t0)/d,1), e=1-Math.pow(1-k,4), v=Math.round(to*e);
          c.textContent=c.dataset.fmt?String(v).replace(/\B(?=(\d{3})+(?!\d))/g,' '):v;
          if(k<1) requestAnimationFrame(step);
        })(t0);
      }
    });
  },{threshold:.15,rootMargin:'0px 0px -6% 0px'});
  document.querySelectorAll('.sr').forEach(function(el){io.observe(el)});

  /* gallery filter */
  var fb=document.querySelectorAll('.filters button');
  fb.forEach(function(b){b.addEventListener('click',function(){
    fb.forEach(function(x){x.classList.remove('on')}); b.classList.add('on');
    var f=b.dataset.f;
    document.querySelectorAll('.mason .gi').forEach(function(t){
      t.classList.toggle('off',f!=='all' && t.dataset.c!==f);
    });
  })});

  /* lead form: no backend yet, so compose the message for copy/send */
  var f=document.getElementById('lead'), res=document.getElementById('res');
  if(f) f.addEventListener('submit',function(e){
    e.preventDefault();
    var d=new FormData(f), dt=d.get('date');
    var txt='Здравствуйте! Меня зовут '+d.get('name')+'. Планирую: '+String(d.get('type')).toLowerCase()+(dt?', дата '+dt.split('-').reverse().join('.'):'')+(d.get('guests')?', гостей примерно '+d.get('guests'):'')+'. Контакт: '+d.get('contact')+'. Свободна ли дата?';
    res.innerHTML='';
    res.appendChild(document.createTextNode('Заявка готова. Отправьте её по номеру +375 (29) 577-32-23:\n\n'+txt));
    var b=document.createElement('button');b.type='button';b.textContent='Скопировать';
    b.onclick=function(){try{navigator.clipboard.writeText(txt).then(function(){b.textContent='Скопировано'})}catch(_){}};
    res.appendChild(document.createElement('br'));res.appendChild(b);
    res.classList.add('show');
  });

  var lb=document.getElementById('lb');
  if(lb){document.querySelectorAll('.mason .gi img').forEach(function(i){i.addEventListener('click',function(){lb.querySelector('img').src=i.src;lb.classList.add('on')})});
    lb.addEventListener('click',function(){lb.classList.remove('on')});}
})();