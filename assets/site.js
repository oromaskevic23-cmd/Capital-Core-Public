/* Native links work without JavaScript. This only improves the language menu. */
for (const menu of document.querySelectorAll('.language-menu')) {
  document.addEventListener('click', event => { if (!menu.contains(event.target)) menu.open = false; });
  menu.addEventListener('keydown', event => {
    if (event.key === 'Escape') { menu.open = false; menu.querySelector('summary').focus(); }
  });
}

/* Progressive enhancement: the original site remains intact if immersive files cannot load. */
if (document.body.classList.contains('ecosystem')) {
  const sheet=document.createElement('link');
  sheet.rel='stylesheet';sheet.href='/Capital-Core-Public/assets/imperial-experience.css?v=20261122';
  sheet.onload=()=>{
    const script=document.createElement('script');script.src='/Capital-Core-Public/assets/imperial-experience.js?v=20261122';script.defer=true;document.body.appendChild(script);
  };
  document.head.appendChild(sheet);
}
