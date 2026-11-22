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
en:{headline:["The Sovereign","AI Ecosystem"],desc:"Federated orchestration, governed AI agents, verified engineering and accountable execution — within one architectural vision.",cta:"Explore the Ecosystem",evidence:"Engineering Evidence",modules:"Explore the IMPERIAL Core Ecosystem",view:"View all modules",arch:"Platform Architecture",archintro:"A federated architecture designed for multiple organizations, professional teams and bounded AI agent execution. All operational claims require evidence.",cap:"Trusted Capabilities for the Enterprise",architect:"The Architect Behind IMPERIAL Core",footer:"Build Your AI Sovereignty with IMPERIAL Core",contact:"Request a Private Demo",strap:"THE ARCHITECTURE",links:"Open verified source",labels:["AI Command Center","Intelligence & Routing","Specialized AI Agents","Defensive Security","Identity & Governance","Agent Trust Research"],trust:["Federated Orchestration","Independent execution domains under bounded authority","Verified Engineering","Tests, releases and auditable evidence","Zero Trust Governance","Identity is not authority; approval is explicit","Human Sovereignty","Owner retains final architectural authority"],chip:["HANTER","Federated Orchestration","Verified Engineering","Zero Trust","Audit Ledger","AI Systems"]},
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
const originalHero=hero.querySelector(".hero-copy");if(!originalHero)return;
const h1=originalHero.querySelector("h1"),intro=originalHero.querySelector(".intro");
if(h1){h1.textContent="";h1.append(document.createTextNode(t.headline[0]),document.createElement("br"));const em=document.createElement("em");em.textContent=t.headline[1];h1.append(em);}
if(intro)intro.textContent=t.desc;
const actions=originalHero.querySelector(".actions");
if(actions){actions.replaceChildren(link("#ic-ecosystem",t.cta+"  →","button primary"),link("https://oromaskevic23-cmd.github.io/oromaskevic23-cmd/engineering/",t.evidence+"  ↗","button secondary"));}
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
 const glow=div("ic-module-visual");glow.setAttribute("aria-hidden","true");card.append(glow);
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
const capabilities=div("ic-capabilities","section");capabilities.append(textEl("h2","",t.cap));
const capGrid=div("ic-capability-grid");
[
 ["star",t.trust[2],t.trust[3],github+"CONSTRUCTOR-AI"],
 ["network",t.trust[0],t.trust[1],github+"HANTER-Public"],
 ["shield",t.trust[4],t.trust[5],github+"ZERO-TRUST"],
 ["diamond",t.trust[6],t.trust[7],github+"APPROVAL-GATEWAY"]
].forEach(([icon,title,sub,href])=>{const c=link(href,"","ic-capability");c.append(svgIcon(icon),textEl("strong","",title),textEl("p","",sub));capGrid.append(c);});
capabilities.append(capGrid);shell.append(capabilities);
const founder=document.querySelector(".company-founder");
if(founder){founder.id="architect";const title=founder.querySelector("h2");if(title)title.textContent=t.architect;founder.classList.add("ic-architect");shell.append(founder);}
const cta=div("ic-closing","section");cta.append(textEl("h2","",t.footer),link("mailto:oromaskevic23@gmail.com?subject=IMPERIAL%20Core%20Private%20Demo",t.contact+"  →","button primary"));shell.append(cta);
hero.insertAdjacentElement("afterend",shell);
const nv=document.querySelector(".header .main-nav");if(nv){const a=nv.querySelector('a[href="#about"]');if(a)a.href="#ic-ecosystem";}
body.classList.add("ic-sovereign");
})();