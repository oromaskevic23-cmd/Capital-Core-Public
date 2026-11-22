/* IMPERIAL Core reference-faithful premium redesign.
   Progressive enhancement only, all existing locale HTML documents, SEO data, translations,
   original Founder portrait and owner-approved corporate symbol are preserved.
   All visual modules link to actual source/evidence, not simulated dashboards. */
(()=>{
"use strict";
const body=document.body;if(!body.classList.contains("ecosystem"))return;
const hero=document.querySelector(".company-hero"),main=document.querySelector("main");
if(!hero||!main||document.querySelector("#ic-ecosystem"))return;
const lang=(document.documentElement.lang||"en").split("-")[0];
const translations={
en:{headline:["The Sovereign","AI Ecosystem"],desc:"Enterprise orchestration, verified execution, and intelligent systems — in one unified ecosystem.",cta:"Explore the Ecosystem",evidence:"Engineering Evidence",modules:"Explore the IMPERIAL Core Ecosystem",view:"View all modules",arch:"Platform Architecture",archintro:"A federated architecture designed for multiple organizations, professional teams and bounded AI agent execution. All operational claims require evidence.",cap:"Trusted Capabilities for the Enterprise",architect:"The Architect Behind IMPERIAL Core",footer:"Build Your AI Sovereignty with IMPERIAL Core",contact:"Request a Private Demo",strap:"THE ARCHITECTURE",links:"Open verified source",labels:["AI Command Center","Intelligence & Routing","Specialized AI Agents","Defensive Security","Identity & Governance","Agent Trust Research"],trust:["Federated Orchestration","Independent execution domains under bounded authority","Verified Engineering","Tests, releases and auditable evidence","Zero Trust Governance","Identity is not authority; approval is explicit","Human Sovereignty","Owner retains final architectural authority"],chip:["HANTER","Federated Orchestration","Verified Engineering","Zero Trust","Audit Ledger","AI Systems"]},
ru:{headline:["Суверенная","AI-экосистема"],desc:"Федеративная оркестрация, управляемые AI-агенты, проверяемая разработка и подотчётное исполнение в единой архитектуре.",cta:"Исследовать экосистему",evidence:"Инженерные доказательства",modules:"Экосистема IMPERIAL Core",view:"Все модули",arch:"Архитектура платформы",archintro:"Федеративная архитектура для организаций, профессиональных команд и AI-агентов с ограниченными полномочиями. Работа каждого компонента требует доказательств.",cap:"Технологические принципы Enterprise",architect:"Архитектор IMPERIAL Core",footer:"Создавайте AI-будущее с IMPERIAL Core",contact:"Обсудить демонстрацию",strap:"АРХИТЕКТУРА",links:"Открыть исходники",labels:["Командный центр AI","Интеллект и маршрутизация","Специализированные AI-агенты","Защитная безопасность","Идентичность и управление","Исследования доверия"],trust:["Федеративная оркестрация","Автономные домены с ограниченными полномочиями","Проверяемая разработка","Тесты, релизы и проверяемые свидетельства","Управление Zero Trust","Идентичность не даёт полномочий без одобрения","Власть человека","Финальная архитектурная власть у владельца"],chip:["HANTER","Федеративная оркестрация","Проверяемая разработка","Zero Trust","Audit Ledger","AI-системы"]},
uk:{headline:["Суверенна","AI-екосистема"],desc:"Федеративна оркестрація, керовані AI-агенти, перевірена розробка й підзвітне виконання в єдиній архітектурі.",cta:"Дослідити екосистему",evidence:"Інженерні докази",modules:"Екосистема IMPERIAL Core",view:"Усі модулі",arch:"Архітектура платформи",archintro:"Федеративна архітектура для організацій, професійних команд та AI-агентів з обмеженими повноваженнями.",cap:"Принципи Enterprise",architect:"Архітектор IMPERIAL Core",footer:"Будуйте AI-майбутнє з IMPERIAL Core",contact:"Обговорити демонстрацію",strap:"АРХІТЕКТУРА",links:"Переглянути код",labels:["Командний центр AI","Інтелект і маршрутизація","Спеціалізовані AI-агенти","Кіберзахист","Ідентичність і управління","Дослідження довіри"],trust:["Федеративна оркестрація","Обмежені повноваження","Перевірена розробка","Тести й докази","Управління Zero Trust","Дозвіл має бути явним","Суверенітет людини","Власник зберігає остаточне рішення"],chip:["HANTER","Федеративна оркестрація","Перевірка","Zero Trust","Audit Ledger","AI-системи"]},
ar:{headline:["المنظومة السيادية","للذكاء الاصطناعي"],desc:"تنسيق اتحادي ووكلاء ذكاء اصطناعي محكومون وهندسة قابلة للتحقق وتنفيذ خاضع للمساءلة.",cta:"استكشف المنظومة",evidence:"الأدلة الهندسية",modules:"استكشف منظومة IMPERIAL Core",view:"جميع الوحدات",arch:"معمارية المنصة",archintro:"معمارية اتحادية للمؤسسات والفرق المهنية ووكلاء الذكاء الاصطناعي بصلاحيات محددة، مع متطلبات إثبات مستقلة.",cap:"قدرات الحوكمة للمؤسسات",architect:"مهندس IMPERIAL Core المعماري",footer:"ابنِ سيادتك في الذكاء الاصطناعي مع IMPERIAL Core",contact:"اطلب عرضاً خاصاً",strap:"المعمارية",links:"عرض المصدر",labels:["مركز قيادة الوكلاء","الذكاء والتوجيه","وكلاء متخصصون","الأمن الدفاعي","الهوية والحوكمة","أبحاث الثقة"],trust:["التنسيق الاتحادي","صلاحيات محددة","هندسة قابلة للتحقق","اختبارات وأدلة","حوكمة انعدام الثقة","التصريح صريح","السيادة البشرية","القرار النهائي للمالك"],chip:["HANTER","التنسيق الاتحادي","التحقق","Zero Trust","Audit Ledger","أنظمة الذكاء"]},
de:{headline:["Das souveräne","KI-Ökosystem"],desc:"Föderierte Orchestrierung, kontrollierte KI-Agenten, verifizierte Entwicklung und verantwortbare Ausführung.",cta:"Ökosystem entdecken",evidence:"Technische Nachweise",modules:"Das IMPERIAL Core Ökosystem",view:"Alle Module",arch:"Plattformarchitektur",archintro:"Föderierte Architektur für Organisationen, Teams und KI-Agenten mit begrenzten Befugnissen.",cap:"Enterprise-Grundsätze",architect:"Der Architekt von IMPERIAL Core",footer:"Gestalten Sie Ihre KI-Souveränität",contact:"Private Demo anfragen",strap:"ARCHITEKTUR",links:"Quellen ansehen",labels:["KI-Kommandozentrale","Intelligenz und Routing","Spezialisierte KI-Agenten","Defensive Sicherheit","Identität und Governance","Vertrauensforschung"],trust:["Föderierte Orchestrierung","Begrenzte Zuständigkeiten","Verifizierte Entwicklung","Tests und Belege","Zero Trust Governance","Explizite Genehmigungen","Menschliche Souveränität","Letzte Entscheidung beim Eigentümer"],chip:["HANTER","Föderierte Orchestrierung","Verifizierung","Zero Trust","Audit Ledger","KI-Systeme"]},
fr:{headline:["L’écosystème","IA souverain"],desc:"Orchestration fédérée, agents IA gouvernés, ingénierie vérifiable et exécution responsable.",cta:"Explorer l'écosystème",evidence:"Preuves techniques",modules:"L'écosystème IMPERIAL Core",view:"Tous les modules",arch:"Architecture de la plateforme",archintro:"Architecture fédérée pour organisations, équipes et agents IA à autorisations limitées.",cap:"Capacités pour les entreprises",architect:"L'architecte d'IMPERIAL Core",footer:"Construisez votre souveraineté IA",contact:"Demander une démo privée",strap:"ARCHITECTURE",links:"Voir les sources",labels:["Centre de commande IA","Intelligence et routage","Agents IA spécialisés","Sécurité défensive","Identité et gouvernance","Recherche sur la confiance"],trust:["Orchestration fédérée","Périmètres limités","Ingénierie vérifiée","Tests et preuves","Gouvernance Zero Trust","Approbation explicite","Souveraineté humaine","Autorité finale du fondateur"],chip:["HANTER","Orchestration fédérée","Vérification","Zero Trust","Audit Ledger","Systèmes IA"]},
es:{headline:["El ecosistema","de IA soberana"],desc:"Orquestación federada, agentes de IA gobernados, ingeniería verificable y ejecución responsable.",cta:"Explorar el ecosistema",evidence:"Evidencia técnica",modules:"El ecosistema IMPERIAL Core",view:"Todos los módulos",arch:"Arquitectura de la plataforma",archintro:"Arquitectura federada para organizaciones, equipos profesionales y agentes de IA con permisos delimitados.",cap:"Capacidades empresariales",architect:"El arquitecto de IMPERIAL Core",footer:"Construye tu soberanía de IA",contact:"Solicitar demostración",strap:"ARQUITECTURA",links:"Ver código",labels:["Centro de mando de IA","Inteligencia y enrutamiento","Agentes de IA especializados","Seguridad defensiva","Identidad y gobernanza","Investigación de confianza"],trust:["Orquestación federada","Permisos delimitados","Ingeniería verificada","Pruebas y evidencia","Gobernanza Zero Trust","Aprobación explícita","Soberanía humana","Autoridad final del fundador"],chip:["HANTER","Orquestación federada","Verificación","Zero Trust","Audit Ledger","Sistemas IA"]},
pt:{headline:["O ecossistema","de IA soberana"],desc:"Orquestração federada, agentes de IA governados, engenharia verificável e execução responsável.",cta:"Explorar o ecossistema",evidence:"Evidências técnicas",modules:"Ecossistema IMPERIAL Core",view:"Todos os módulos",arch:"Arquitetura da plataforma",archintro:"Arquitetura federada para organizações, equipes e agentes de IA com permissões limitadas.",cap:"Capacidades empresariais",architect:"O arquiteto do IMPERIAL Core",footer:"Construa sua soberania de IA",contact:"Solicitar demonstração",strap:"ARQUITETURA",links:"Ver fontes",labels:["Centro de comando de IA","Inteligência e roteamento","Agentes de IA especializados","Segurança defensiva","Identidade e governança","Pesquisa em confiança"],trust:["Orquestração federada","Permissões limitadas","Engenharia verificada","Testes e evidências","Governança Zero Trust","Aprovação explícita","Soberania humana","Autoridade final do fundador"],chip:["HANTER","Orquestração federada","Verificação","Zero Trust","Audit Ledger","Sistemas IA"]},
ja:{headline:["主権を守る","AIエコシステム"],desc:"フェデレーテッド・オーケストレーション、管理されたAIエージェント、検証可能なエンジニアリング。",cta:"エコシステムを見る",evidence:"開発証拠",modules:"IMPERIAL Coreエコシステム",view:"すべてのモジュール",arch:"プラットフォーム構造",archintro:"組織、専門チーム、権限を限定したAIエージェントのためのフェデレーテッド・アーキテクチャ。",cap:"企業向けの設計原則",architect:"IMPERIAL Coreの設計者",footer:"IMPERIAL CoreでAIの主権を",contact:"デモを相談",strap:"アーキテクチャ",links:"ソースを見る",labels:["AI指令センター","知能とルーティング","専門AIエージェント","防御的セキュリティ","IDとガバナンス","信頼の研究"],trust:["連合型オーケストレーション","権限を限定","検証可能な開発","テストと証拠","ゼロトラスト","明示的な承認","人間の主権","最終権限は所有者"],chip:["HANTER","連合型","検証","Zero Trust","Audit Ledger","AIシステム"]},
zh:{headline:["自主可信的","AI生态系统"],desc:"联邦编排、受治理的 AI 智能体、可验证工程与可追责执行。",cta:"探索生态系统",evidence:"工程证据",modules:"探索 IMPERIAL Core 生态系统",view:"查看全部模块",arch:"平台架构",archintro:"面向组织、专业团队以及权限受限 AI 智能体的联邦架构。",cap:"企业级设计能力",architect:"IMPERIAL Core 架构师",footer:"借助 IMPERIAL Core 构建 AI 自主能力",contact:"申请私人演示",strap:"架构",links:"查看源代码",labels:["AI指挥中心","智能与路由","专业 AI 智能体","防御安全","身份与治理","可信研究"],trust:["联邦编排","权限边界","可验证工程","测试与证据","零信任治理","显式审批","人类主权","最终决策权归所有者"],chip:["HANTER","联邦编排","工程验证","Zero Trust","Audit Ledger","AI 系统"]}};
const t=translations[lang]||translations.en;
const link=(href,label,cls)=>{const a=document.createElement("a");a.href=href;a.className=cls||"";a.textContent=label;return a;};
const div=(cls,tag="div")=>{const x=document.createElement(tag);x.className=cls;return x;};
const textEl=(tag,cls,txt)=>{const n=div(cls,tag);n.textContent=txt;return n;};

// Architectural roof, glass lounge and gold diamond sculpture are decorative
// website art. No photographs of people or fictional founder likenesses.
const terrace=div("ic-hero-terrace");terrace.setAttribute("aria-hidden","true");
terrace.innerHTML='<svg viewBox="0 0 730 448" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin slice"><defs><linearGradient id="icRoof" x1="0" y1="0" x2="1" y2=".8"><stop stop-color="#1e1210"/><stop offset=".5" stop-color="#37251b"/><stop offset="1" stop-color="#0b111a"/></linearGradient><linearGradient id="icGlass" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#0a0c11" stop-opacity=".9"/><stop offset="1" stop-color="#101622" stop-opacity="0"/></linearGradient><linearGradient id="icGold" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff0c6"/><stop offset=".55" stop-color="#dfa44f"/><stop offset="1" stop-color="#a76b36"/></linearGradient><filter id="icB"><feGaussianBlur stdDeviation="7"/></filter></defs><path d="M0 0H660Q672 71 631 107Q595 131 515 122Q410 108 300 120H0Z" fill="url(#icRoof)" opacity=".93"/><path d="M0 64Q165 41 312 71T592 94Q636 93 641 43" stroke="#ffcd78" stroke-width="12" opacity=".75" filter="url(#icB)"/><path d="M0 64Q165 41 312 71T592 94Q636 93 641 43" stroke="#f9c275" stroke-width="3.5" opacity=".95"/><path d="M0 105H525V356H0Z" fill="url(#icGlass)" opacity=".85"/><g opacity=".64" stroke="#b3814a" stroke-width="3"><path d="M74 101V355M164 96V352M260 98V348M364 107V346M473 119V349"/><path d="M0 348H531"/></g><g opacity=".78"><ellipse cx="293" cy="381" rx="175" ry="17" fill="#c48e5a" opacity=".3"/><path d="M122 356Q127 305 191 313L337 313Q403 312 411 352L404 382H122Z" fill="#887366"/><path d="M135 356Q152 331 178 330H371Q403 334 402 355V373H135Z" fill="#cbb5a0"/><path d="M166 325Q195 303 220 329L213 348H163ZM235 320Q271 303 298 325L286 350H228ZM315 328Q336 302 364 329L359 349H307Z" fill="#e8d6bf"/></g><g transform="translate(548 302)" stroke="url(#icGold)" fill="none" stroke-width="4"><path d="M0 16 25 0h50l26 16-52 68L0 16Z"/><path d="M0 16h101M25 0l24 84L75 0M49 84l7-68"/><path d="M49 85V117"/><ellipse cx="49" cy="120" rx="65" ry="11" fill="#53321c" opacity=".8"/></g><ellipse cx="599" cy="398" rx="92" ry="9" fill="#ffca73" opacity=".52" filter="url(#icB)"/></svg>';
hero.prepend(terrace);

const originalHero=hero.querySelector(".hero-copy");if(!originalHero)return;
const h1=originalHero.querySelector("h1"),intro=originalHero.querySelector(".intro");
if(h1){h1.textContent="";h1.append(document.createTextNode(t.headline[0]),document.createElement("br"));const em=document.createElement("em");em.textContent=t.headline[1];h1.append(em);}
if(intro)intro.textContent=t.desc;
const actions=originalHero.querySelector(".actions");
if(actions){actions.replaceChildren(link("#ic-ecosystem",t.cta+"  →","button primary"),link("#ic-platform",lang==="en"?"Platform Overview  ↗":t.arch+"  ↗","button secondary"));}
const github="https://github.com/oromaskevic23-cmd/";
const features=[
 ["diamond","HANTER",github+"HANTER-Public"],
 ["layers",t.chip[1],github+"Nano-Core-Agents-Public"],
 ["cpu",t.chip[2],github+"CONSTRUCTOR-AI"],
 ["shield",t.chip[3],github+"ZERO-TRUST"],
 ["database",t.chip[4],github+"AUDIT-LEDGER"],
 ["network",t.chip[5],github+"VELION-LLM-Public"]
];
const icons={
diamond:'<path d="M4 10 9 3h14l5 7-12 16L4 10Z"/><path d="M4 10h24M9 3l7 23 7-23"/>',
layers:'<path d="m2 9 14-7 14 7-14 7L2 9ZM2 16l14 7 14-7M2 23l14 7 14-7"/>',
cpu:'<rect x="8" y="8" width="16" height="16" rx="2"/><rect x="13" y="13" width="6" height="6"/><path d="M12 1v7M20 1v7M12 24v7M20 24v7M1 12h7M1 20h7M24 12h7M24 20h7"/>',
shield:'<path d="M16 2 28 7v9c0 8-5 12-12 15C9 28 4 24 4 16V7L16 2Z"/><path d="m11 16 4 4 7-8"/>',
database:'<ellipse cx="16" cy="7" rx="11" ry="5"/><path d="M5 7v18c0 7 22 7 22 0V7M5 16c0 7 22 7 22 0"/>',
network:'<circle cx="16" cy="5" r="4"/><circle cx="6" cy="25" r="4"/><circle cx="26" cy="25" r="4"/><path d="M13 8 8 21M19 8l5 13M10 25h12"/>',
passport:'<rect x="6" y="2" width="20" height="28" rx="3"/><circle cx="16" cy="13" r="4"/><path d="M11 22h10"/>',
brain:'<path d="M14 5c-8-6-15 5-9 10-4 7 3 14 9 11V5ZM18 5c8-6 15 5 9 10 4 7-3 14-9 11V5ZM14 17h4"/>',
star:'<path d="m16 2 4 10 10 4-10 4-4 10-4-10-10-4 10-4z"/>'};
function svgIcon(name){const span=div("ic-icon");span.innerHTML='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+(icons[name]||icons.diamond)+'</svg>';return span;}
const featurebar=div("ic-featurebar");features.forEach(([ico,label,href])=>{const a=link(href,"","ic-feature");a.append(svgIcon(ico),textEl("span","",label));featurebar.append(a);});
hero.append(featurebar);
const shell=div("ic-expo");
const showcase=div("ic-showcase","section");showcase.id="ic-ecosystem";
const heading=div("ic-section-heading");heading.append(textEl("h2","",t.modules),link("#projects",t.view+"  →","ic-view-all"));showcase.append(heading);
const cards=div("ic-module-grid");
/* Original vector module artwork, no generated personal photographs. */
function visualArt(cls){
 const prefix='<svg viewBox="0 0 420 170" xmlns="http://www.w3.org/2000/svg" fill="none" aria-hidden="true">';
 const end='</svg>';
 if(cls==="ic-card-velion"){
   const lines=Array.from({length:22},(_,i)=>{const y=30+i*5;const dy=Math.sin(i*.45)*18;return '<path d="M125 '+y+' C218 '+(y-58+dy)+' 264 '+(y+60-dy)+' 420 '+(y-22)+'" stroke="#F1BD74" stroke-opacity="'+(.12+(i%6)*.053).toFixed(2)+'" stroke-width="1.2"/>';}).join("");
   return prefix+'<defs><radialGradient id="vg"><stop stop-color="#E8A95C" stop-opacity=".34"/><stop offset="1" stop-color="#E8A95C" stop-opacity="0"/></radialGradient></defs><circle cx="310" cy="78" r="115" fill="url(#vg)"/>'+lines+end;
 }
 if(cls==="ic-card-nca"){
   const cube=(x,y,n)=>'<g transform="translate('+x+' '+y+')" opacity="'+n+'"><path d="M0 0 26-14 52 0 26 15Z" stroke="#FFD69B" stroke-width="1.8" fill="#CB8B484F"/><path d="M0 0V31L26 46V15Z" stroke="#F4C07E" stroke-width="1.7" fill="#6B48365A"/><path d="M52 0V31L26 46V15Z" stroke="#EFB875" stroke-width="1.7" fill="#D69B5D66"/></g>';
   return prefix+cube(255,44,1)+cube(326,77,.94)+cube(215,93,.85)+cube(298,126,.8)+'<path d="M281 88 326 96M265 127l52 17M348 103l-24 18" stroke="#F1C27B" stroke-opacity=".65" stroke-width="1.7"/>'+end;
 }
 if(cls==="ic-card-cyber"){
   return prefix+'<g transform="translate(310 87)"><circle r="75" stroke="#E7A65C" stroke-opacity=".34"/><circle r="58" stroke="#F5C080" stroke-opacity=".55" stroke-dasharray="6 12"/><circle r="43" stroke="#F5CE8B" stroke-opacity=".55"/><path d="M0-39 30-27v25C30 24 16 36 0 42-16 36-30 24-30-2v-25Z" fill="#B7833540" stroke="#FFD592" stroke-width="2"/><path d="m-13 0 10 10 21-22" stroke="#FFE0AA" stroke-width="2.3"/></g>'+end;
 }
 if(cls==="ic-card-agy"){
  return prefix+'<defs><radialGradient id="rg"><stop stop-color="#F6C487" stop-opacity=".39"/><stop offset="1" stop-color="#E3AD5C" stop-opacity="0"/></radialGradient></defs><circle cx="321" cy="90" r="79" fill="url(#rg)"/><g stroke="#F6C281" stroke-width="2" fill="#0B1523"><path d="M322 15c-34 0-57 27-57 60 0 23 9 39 27 48v28l27 8 23-14-3-28c17-16 25-35 25-55 0-26-17-47-42-47Z"/><path d="M279 53c13-17 28-24 45-24m-41 69 35 12 30-21M283 76h65M319 30v85M293 53l26-15 29 19M292 121l27 12 25-17" stroke-opacity=".7"/><path d="M280 76h20l8 8-7 7h-22Zm53 0h20l-2 15h-20l-6-7Z" fill="#DBA765" opacity=".8"/><path d="M311 145l17 2" stroke="#FFDCA9" stroke-width="3"/></g>'+end;
 }
 if(cls==="ic-card-hanter"){
  const screens=Array.from({length:8},(_,i)=>{
   const x=170+(i%4)*55,y=22+Math.floor(i/4)*52;
   return '<rect x="'+x+'" y="'+y+'" width="48" height="41" rx="3" fill="#0A233E" stroke="#6BC7FC" stroke-opacity=".65" stroke-width="1.3"/><path d="M'+(x+8)+' '+(y+29)+'l9-10 8 6 9-18" fill="none" stroke="#7EE0FF" stroke-opacity=".8" stroke-width="1.2"/>';
  }).join("");
  return prefix+'<defs><radialGradient id="hc"><stop stop-color="#84E2FF" stop-opacity=".55"/><stop offset="1" stop-color="#84E2FF" stop-opacity="0"/></radialGradient></defs><rect x="160" y="10" width="260" height="150" rx="9" fill="#0B1A32" stroke="#D7A15C" stroke-opacity=".65"/>'+screens+'<circle cx="320" cy="93" r="55" fill="url(#hc)"/><circle cx="320" cy="93" r="37" stroke="#A9E7FF" stroke-width="1.6" opacity=".75"/><ellipse cx="320" cy="93" rx="18" ry="37" stroke="#B5E9FF" stroke-width="1.4" opacity=".65"/><path d="M283 93h74M287 76h67M289 109h62" stroke="#B7F1FF" stroke-width="1.3" opacity=".66"/>'+end;
 }
 return "";
}

const modules=[
 ["HANTER",t.labels[0],"diamond",github+"HANTER-Public","ic-card-hanter"],
 ["VELION",t.labels[1],"layers",github+"VELION-LLM-Public","ic-card-velion"],
 ["Nano Core Agents",t.labels[2],"network",github+"Nano-Core-Agents-Public","ic-card-nca"],
 ["CYBER HAK",t.labels[3],"shield",github+"CYBER-HAK-Public","ic-card-cyber"],
 ["AI Passport",t.labels[4],"passport","https://github.com/oromaskevic23-cmd/oromaskevic23-cmd/blob/main/docs/AI_PASSPORT_CONCEPT.md","ic-card-passport"],
 ["AGY",t.labels[5],"brain",github+"AGY","ic-card-agy"]
];
modules.forEach(([name,description,ico,href,cls],i)=>{
 const card=link(href,"","ic-module "+cls);card.setAttribute("aria-label",name+" — "+description);
 const glow=div("ic-module-visual");glow.setAttribute("aria-hidden","true");glow.innerHTML=visualArt(cls);card.append(glow);
 const content=div("ic-module-content");content.append(svgIcon(ico),textEl("h3","",name),textEl("p","",description));
 card.append(content);card.append(textEl("span","ic-module-arrow","↗"));cards.append(card);
});
showcase.append(cards);shell.append(showcase);
const architecture=div("ic-architecture","section");architecture.id="ic-platform";
const diagram=div("ic-diagram");
const art=div("ic-diagram-art");
const diamond=div("ic-diagram-diamond");const brand=document.createElement("img");
brand.src="/Capital-Core-Public/assets/imperial-core-diamond-20261116.jpg";brand.alt="";brand.decoding="async";brand.loading="lazy";
diamond.append(brand);art.append(diamond);
const orbit=div("ic-diagram-orbit");orbit.setAttribute("aria-hidden","true");art.append(orbit);

const artGold=div("ic-architecture-illustration");
artGold.setAttribute("aria-hidden","true");
artGold.innerHTML='<svg viewBox="0 0 580 290" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet"><defs><radialGradient id="aGlow"><stop stop-color="#ffbe71" stop-opacity=".38"/><stop offset="1" stop-color="#ffbe71" stop-opacity="0"/></radialGradient><linearGradient id="aGold" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff0c5"/><stop offset=".65" stop-color="#e8a55d"/><stop offset="1" stop-color="#91632f"/></linearGradient></defs><ellipse cx="284" cy="218" rx="230" ry="82" fill="url(#aGlow)"/><g stroke="#ecad64" opacity=".68" fill="none"><ellipse cx="288" cy="227" rx="227" ry="35" stroke-width="2"/><ellipse cx="288" cy="219" rx="186" ry="28" stroke-width="1.6"/><ellipse cx="288" cy="211" rx="144" ry="23" stroke-width="1.6"/></g><g stroke="url(#aGold)" stroke-width="2.4" fill="#211625" fill-opacity=".52"><path d="M216 102h143l37 40-105 111-111-111Z"/><path d="M180 142h216M216 102l75 151 68-151M245 102l46 151 32-151"/></g><g fill="#131a29ce" stroke="#f2c485" stroke-width="1.6"><rect x="32" y="79" width="115" height="119" rx="6"/><rect x="433" y="79" width="115" height="119" rx="6"/></g><g fill="#f9d4a5" font-family="Georgia" font-size="17"><text x="52" y="146">HANTER</text><text x="461" y="146">VELION</text></g></svg>';
art.prepend(artGold);

const nodeNames=["HANTER","VELION","Nano Core Agents","Zero Trust"];
nodeNames.forEach((n,i)=>art.append(textEl("span","ic-diagram-node ic-node-"+i,n)));
diagram.append(art);
const copy=div("ic-architecture-copy");copy.append(textEl("p","ic-kicker",t.strap),textEl("h2","",t.arch),textEl("p","ic-architecture-desc",t.archintro));
const principles=div("ic-principles");
const destinations=[
 [icons.layers,t.trust[0],t.trust[1],github+"Nano-Core-Agents-Public"],
 [icons.cpu,t.trust[2],t.trust[3],github+"CONSTRUCTOR-AI"],
 [icons.shield,t.trust[4],t.trust[5],github+"GUARDIAN-CORE"],
 [icons.diamond,t.trust[6],t.trust[7],"https://github.com/oromaskevic23-cmd/oromaskevic23-cmd/blob/main/docs/UNIFIED_ECOSYSTEM_EVIDENCE.md"]
];
destinations.forEach(([markup,title,description,url])=>{
 const a=link(url,"","ic-principle");a.innerHTML='<span class="ic-principle-icon"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6">'+markup+'</svg></span>';
 a.append(textEl("strong","",title),textEl("small","",description));principles.append(a);
});
copy.append(principles);architecture.append(diagram,copy);shell.append(architecture);
const capabilities=div("ic-capabilities","section");capabilities.id="ic-capabilities";capabilities.append(textEl("h2","",t.cap));
const capGrid=div("ic-capability-grid");
[
 ["star",t.trust[2],t.trust[3],github+"CONSTRUCTOR-AI"],
 ["network",t.trust[0],t.trust[1],github+"HANTER-Public"],
 ["shield",t.trust[4],t.trust[5],github+"ZERO-TRUST"],
 ["diamond",t.trust[6],t.trust[7],github+"APPROVAL-GATEWAY"]
].forEach(([icon,title,sub,href])=>{const c=link(href,"","ic-capability");c.append(svgIcon(icon),textEl("strong","",title),textEl("p","",sub));capGrid.append(c);});
capabilities.append(capGrid);shell.append(capabilities);
const founder=document.querySelector(".company-founder");
if(founder){founder.hidden=true;founder.style.display="none";} // No person or portrait on this screenshot-faithful homepage.
const cta=div("ic-closing","section");cta.id="ic-closing";cta.append(textEl("h2","",t.footer),link("mailto:oromaskevic23@gmail.com?subject=IMPERIAL%20Core%20Private%20Demo",t.contact+"  →","button primary"));shell.append(cta);
hero.insertAdjacentElement("afterend",shell);
const nv=document.querySelector(".header .main-nav");
if(nv){
 const dest=[
  ["Platform","#ic-platform"],["Solutions","#ic-capabilities"],["Ecosystem","#ic-ecosystem"],
  ["Resources","https://oromaskevic23-cmd.github.io/oromaskevic23-cmd/engineering/"],
  ["About Us","https://oromaskevic23-cmd.github.io/oromaskevic23-cmd/"],
  ["Contact","mailto:oromaskevic23@gmail.com?subject=IMPERIAL%20Core"]
 ];
 nv.replaceChildren(...dest.map(([name,url])=>link(url,name,"ic-nav-link")));
}
const header=document.querySelector(".header");
if(header && !header.querySelector(".ic-nav-access")){
 const mail=link("mailto:oromaskevic23@gmail.com?subject=IMPERIAL%20Core%20Access","Request Access   →","ic-nav-access");
 const langMenu=header.querySelector(".language-menu");
 header.insertBefore(mail,langMenu||null);
}
// Display only the sections shown in the approved reference; preserve every
// original content node, locale, and evidence source in the underlying HTML.
for(const child of Array.from(main.children)){
 if(child!==hero && child!==shell){child.hidden=true;child.style.display="none";}
}
body.classList.add("ic-sovereign");
})();