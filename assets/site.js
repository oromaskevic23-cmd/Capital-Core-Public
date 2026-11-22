/* Native links work without JavaScript. This only improves the language menu. */
for (const menu of document.querySelectorAll('.language-menu')) {
  document.addEventListener('click', event => { if (!menu.contains(event.target)) menu.open = false; });
  menu.addEventListener('keydown', event => {
    if (event.key === 'Escape') { menu.open = false; menu.querySelector('summary').focus(); }
  });
}

/* IMPERIAL Core — optional visual layer, with original locale navigation preserved. */
if (document.body.classList.contains('ecosystem')) {
  const sheet=document.createElement('link');
  sheet.rel='stylesheet';sheet.href='/Capital-Core-Public/assets/imperial-sovereign.css?v=20261122-finalref';
  sheet.onload=()=>{
    const script=document.createElement('script');
    script.src='/Capital-Core-Public/assets/imperial-sovereign.js?v=20261122-finalref';
    script.defer=true;document.body.appendChild(script);
  };
  document.head.appendChild(sheet);
}
