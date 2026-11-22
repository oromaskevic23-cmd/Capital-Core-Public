/* IMPERIAL Core immersive visual scenes. No permissions, payments, tracking or external JavaScript. */
(function(){
  'use strict';
  const body=document.body;
  if(!body.classList.contains('ecosystem'))return;
  const hero=document.querySelector('.company-hero');
  const content=hero&&hero.querySelector('.company-hero .hero-copy');
  if(!hero||!content||hero.querySelector('.ic-experience-nav'))return;
  const language=document.documentElement.lang.toLowerCase().slice(0,2);
  const words={
    en:['Skyline','Sky Tower','Parachute Flight','Command Center','Explore the viewpoints','Dubai skyline panorama','Above the skyline','Aerial flight concept','AI command visualization'],
    ru:['Панорама','Небоскрёб','Полёт','Командный центр','Выберите панораму','Панорама Дубая','Высоко над городом','Визуализация полёта','Визуализация AI-командного центра'],
    uk:['Панорама','Хмарочос','Політ','Командний центр','Оберіть панораму','Панорама Дубая','Над містом','Візуалізація польоту','Візуалізація AI-командного центру'],
    de:['Skyline','Wolkenkratzer','Freiflug','Kommandozentrale','Perspektive wählen','Dubai-Panorama','Hoch über Dubai','Flugvisualisierung','KI-Kommandozentrale'],
    fr:['Panorama','Gratte-ciel','Vol libre','Centre de commande','Choisir une vue','Panorama de Dubaï','Au-dessus de la ville','Visualisation de vol','Centre de commande IA'],
    es:['Panorama','Rascacielos','Vuelo','Centro de mando','Elige una vista','Panorama de Dubái','Sobre la ciudad','Visualización del vuelo','Centro de mando de IA'],
    pt:['Panorama','Arranha-céus','Voo','Centro de comando','Escolha uma vista','Panorama de Dubai','Acima da cidade','Visualização do voo','Centro de comando de IA'],
    ja:['都市景観','超高層ビル','空中飛行','司令センター','景色を選択','ドバイの街並み','都市の上空','飛行ビジュアル','AI司令センター'],
    zh:['城市天际线','摩天大楼','空中飞行','指挥中心','选择视角','迪拜城市全景','城市上空','飞行可视化','AI指挥中心'],
    ar:['الأفق','برج شاهق','التحليق','مركز القيادة','اختر المشهد','أفق دبي','فوق المدينة','تصور الرحلة','مركز قيادة الذكاء الاصطناعي']
  };
  const w=words[language]||words.en;
  const local='/Capital-Core-Public/assets/imperial-skyline-fallback.svg';
  const canonicalDiamond='/Capital-Core-Public/assets/imperial-core-diamond-20261116.jpg';
  const scenes=[
    {id:'skyline',label:w[0],caption:w[5],image:'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=2000&q=80'},
    {id:'tower',label:w[1],caption:w[6],image:'https://images.unsplash.com/photo-1546412414-e1885259563a?auto=format&fit=crop&w=2000&q=80'},
    {id:'flight',label:w[2],caption:w[7],image:'https://images.unsplash.com/photo-1526495124232-a04e1849168c?auto=format&fit=crop&w=2000&q=80'},
    {id:'command',label:w[3],caption:w[8],image:local}
  ];
  const background=document.createElement('div');
  background.className='ic-experience-bg';
  background.setAttribute('aria-hidden','true');
  const front=document.createElement('div'),back=document.createElement('div');
  front.className='ic-scene-photo is-visible';back.className='ic-scene-photo';
  front.style.backgroundImage='url("'+local+'")';
  background.append(front,back);
  hero.prepend(background);
  const orbit=document.createElement('div');orbit.className='ic-orbit';orbit.setAttribute('aria-hidden','true');hero.appendChild(orbit);
  const command=document.createElement('div');command.className='ic-command-grid';command.setAttribute('aria-hidden','true');hero.appendChild(command);
  const flight=document.createElement('div');flight.className='ic-flight-object';flight.setAttribute('aria-hidden','true');
  flight.innerHTML='<svg viewBox="0 0 210 250" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 84C26 17 183 9 191 83L105 99Z" fill="#DFA865" stroke="#FFE7B0" stroke-width="4"/><path d="M20 84Q44 58 64 89Q86 58 105 99Q132 58 149 90Q169 58 191 83" stroke="#715338" stroke-width="2"/><path d="M20 84L98 175M64 89L102 171M105 99L105 174M149 90L108 172M191 83L111 175" stroke="#F7E8CB" stroke-width="2"/><circle cx="105" cy="188" r="13" fill="#EDD6B4"/><path d="M101 202L90 228M110 202L123 230M98 207L77 211M111 208L132 208" stroke="#E3D4C5" stroke-width="8" stroke-linecap="round"/><path d="M96 173L114 173L117 204L93 204Z" fill="#1D3148" stroke="#DDA968" stroke-width="3"/></svg>';
  hero.appendChild(flight);
  const altitude=document.createElement('div');altitude.className='ic-altitude';altitude.setAttribute('aria-hidden','true');
  altitude.innerHTML='<small>IMPERIAL CORE · EXPERIENCE</small><span>Dubai / UAE</span>';
  hero.appendChild(altitude);
  // Render the Architect-approved diamond, using its original unchanged asset.
  const plaque=document.createElement('figure');plaque.className='ic-brand-plaque';
  plaque.setAttribute('aria-hidden','true');
  const diamond=document.createElement('img');diamond.src=canonicalDiamond;diamond.alt='';
  diamond.loading='lazy';diamond.decoding='async';plaque.appendChild(diamond);hero.appendChild(plaque);
  const dock=document.createElement('div');dock.className='ic-experience-nav';dock.setAttribute('role','group');dock.setAttribute('aria-label',w[4]);
  const caption=document.createElement('p');caption.className='ic-scene-caption';caption.setAttribute('aria-live','polite');
  scenes.forEach(function(s,i){
    const button=document.createElement('button');button.type='button';button.className='ic-scene-button';
    button.dataset.icScene=s.id;button.setAttribute('aria-pressed',i===0?'true':'false');
    const num=document.createElement('span');num.className='ic-scene-num';num.textContent=String(i+1).padStart(2,'0');
    const text=document.createElement('span');text.textContent=s.label;button.append(num,text);
    dock.appendChild(button);
  });
  content.append(dock,caption);
  body.classList.add('ic-ready');
  let current=front,previous=back,selectionToken=0;
  function select(id){
    const s=scenes.find(function(x){return x.id===id;});if(!s)return;
    const token=++selectionToken;
    hero.dataset.icScene=s.id;caption.textContent=s.caption;
    dock.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.icScene===id));});
    const next=previous,old=current;
    const apply=function(url){
      if(token!==selectionToken)return;
      next.style.backgroundImage='url("'+url+'")';
      next.classList.add('is-visible');
      old.classList.remove('is-visible');
      current=next;previous=old;
    };
    if(s.image===local){apply(local);return;}
    const preloader=new Image();preloader.decoding='async';
    preloader.onload=function(){apply(s.image);};
    preloader.onerror=function(){apply(local);};
    preloader.src=s.image;
  }
  dock.addEventListener('click',function(e){
    const button=e.target.closest('button[data-ic-scene]');if(button&&dock.contains(button))select(button.dataset.icScene);
  });
  dock.addEventListener('keydown',function(e){
    if(e.key!=='ArrowRight'&&e.key!=='ArrowLeft')return;
    const a=Array.from(dock.querySelectorAll('button'));const i=a.indexOf(document.activeElement);if(i<0)return;
    e.preventDefault();const delta=e.key==='ArrowRight'?1:-1;a[(i+delta+a.length)%a.length].focus();
  });
  const sectionScenes={'#about':'tower','#projects':'flight','#evidence':'command','#ai-passport':'command','#dubai-2027':'tower','#contact':'skyline'};
  document.addEventListener('click',function(e){
    const a=e.target.closest('a[href^="#"]');
    if(a&&sectionScenes[a.getAttribute('href')])select(sectionScenes[a.getAttribute('href')]);
  });
  select('skyline');
})();