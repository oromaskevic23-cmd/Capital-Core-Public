"""Visible English copy and complete locale overlays for the public showcase."""

LANGUAGES = {
    "en": "English", "uk": "Українська", "ru": "Русский", "de-CH": "Deutsch",
    "fr": "Français", "es": "Español", "pt": "Português", "ar": "العربية",
    "ja": "日本語", "zh": "中文",
}

# Cards are ordered to match the public site. Repository URLs are generated
# from the authenticated account's public repository inventory.
FEATURED = [
    ("HANTER", "HANTER-Public", "waterfront", "waterfront", "/tree/main/hanter_pilot"),
    ("VELION", "VELION-LLM-Public", "intelligence", "intelligence", ""),
    ("Nano Core Agents", "Nano-Core-Agents-Public", "agent-teams", "aerial", ""),
    ("CYBER HAK", "CYBER-HAK-Public", "night", "night", ""),
    ("AI Passport", "oromaskevic23-cmd", "passport", "atrium", "/blob/main/docs/AI_PASSPORT_CONCEPT.md"),
    ("AGY", "AGY", "aerial", "aerial", ""),
    ("CONSTRUCTOR AI", "CONSTRUCTOR-AI", "atrium", "atrium", ""),
    ("ORION", "ORION-Public", "intelligence", "intelligence", ""),
    ("LEGION", "Legion-Public", "agent-teams", "night", ""),
]

MORE = [
    ("Capital Core", "Capital-Core-Public"), ("IMPERIAL ART", "IMPERIAL-ART"),
    ("IMPERIAL CRM Autopilot", "IMPERIAL-CRM-Autopilot"), ("Jem", "Jem"),
    ("IMPERIAL AGI", "IMPERIAL-AGI"), ("IMPERIAL Venture Factory", "IMPERIAL-Venture-Factory"),
    ("Enterprise Skills", "IMPERIAL-Skill"), ("IMPERIAL Plugins", "IMPERIAL-Plugins"),
    ("Guardian Core", "GUARDIAN-CORE"), ("Approval Gateway", "APPROVAL-GATEWAY"),
    ("Audit Ledger", "AUDIT-LEDGER"), ("Zero Trust", "ZERO-TRUST"),
    ("IMPERIAL n8n Automation", "IMPERIAL-n8n-Automation"),
    ("Codex Enterprise IMPERIAL Skills", "Codex-Enterprise-IMPERIAL-Skills"),
]

FIELDS = (
    "skip nav portfolio architecture dubai founder languages github "
    "hero1 hero2 intro explore overview "
    "views previous next play pause close project evidence all "
    "portfolioTitle architectureTitle architectureBody digitalQuote digitalBody "
    "federation scope identity audit "
    "moreTitle moreIntro cryptoTitle cryptoBody "
    "dubaiTitle dubaiIntro business personal societal businessTitle personalTitle societalTitle "
    "businessBody personalBody societalBody walkthrough candidateEvidence "
    "founderTitle role founderBody founderProfile engineering reference "
    "ctaTitle contact footerArchitecture"
).split()

def locale(text):
    rows = text.strip().splitlines()
    if len(rows) != len(FIELDS):
        raise ValueError(f"Expected {len(FIELDS)} copy fields, received {len(rows)}")
    return dict(zip(FIELDS, rows, strict=True))

COPY = {}
COPY["en"] = locale("""
Skip to content
Primary navigation
Ecosystem
Architecture
Dubai 2027
Founder
Languages
GitHub
The Sovereign
AI Ecosystem
Enterprise orchestration, verified execution and intelligent systems in one unified ecosystem.
Explore the ecosystem
View architecture
Dubai panoramas
Previous view
Next view
Play panoramas
Pause panoramas
Close
Open project
Engineering evidence
All projects
Explore the IMPERIAL Core Ecosystem
Platform Architecture
The Architect sets intent and retains final authority. HANTER coordinates missions. Federated orchestrators assign bounded work to specialized teams and Nano Core Agents, with evidence returned after execution.
I wanted to build a company. I built a digital state.
The Digital State is our engineering vision for a shared system of agent identity, delegated authority, human approval and auditable outcomes. The digital diamond is its symbol.
Federated orchestration
Scoped execution
Identity and approvals
Verifiable audit
More engineering projects
Explore the public design, code and reference implementations behind the ecosystem.
CRYPTO IMPERIAL Ecosystem
IMPERIUM is envisioned as a long-term architectural digital currency for AI agents worldwide. This research has its own boundary, separate from software execution and the championship candidates.
Dubai 2027 · Create AI Agents Championship
Three original early-stage candidates for distinct problems. Independent competition preparation with public documentation and synthetic evidence.
Business
Personal
Societal
IMPERIAL ONE
Consent-based planning
Public-service guidance
Compare invoice records, flag discrepancies and route exceptions to an authorized reviewer. The synthetic prototype covers review and audit without executing payments.
Turn obligations into an achievable plan. The local prototype saves tasks only after the person confirms the specific plan.
Guide people to official UAE resources through a multilingual checklist. The local prototype tracks progress on a device.
Open the synthetic walkthrough
See candidate evidence
The Architect behind IMPERIAL Core
Founder · Owner · CEO · Chief Systems Architect
Alexander Romaskevich designs the IMPERIAL Core architecture and directs its engineering. His work connects agent identity, delegated authority and evidence of outcomes across distinct projects.
Official founder profile
Engineering dossier
Technical reference
Build Your AI Sovereignty with IMPERIAL Core
Request a private demo
Architecture → Implementation → Evidence
""")

COPY["ru"] = locale("""
Перейти к содержанию
Главная навигация
Экосистема
Архитектура
Дубай 2027
Основатель
Языки
GitHub
Суверенная
ИИ-экосистема
Федеративная оркестрация, управляемое исполнение и проверяемая инженерия под контролем человека.
Смотреть экосистему
Изучить архитектуру
Панорамы Дубая
Предыдущий вид
Следующий вид
Запустить смену видов
Приостановить смену видов
Закрыть
Открыть проект
Инженерные доказательства
Все проекты
Экосистема IMPERIAL Core
Архитектура платформы
Архитектор задаёт намерение и принимает окончательное решение. HANTER координирует миссии. Федеративные оркестраторы поручают ограниченные задачи профессиональным командам и Nano Core Agents, которые возвращают доказательства выполнения.
Я хотел создать компанию, а сделал цифровое государство.
Цифровое государство — наше инженерное видение общей системы идентификации агентов, делегирования полномочий, согласования человеком и аудита результатов. Её символ — цифровой бриллиант.
Федеративная оркестрация
Ограниченное исполнение
Идентификация и согласование
Проверяемый аудит
Другие инженерные проекты
Публичная архитектура, исходный код и эталонные реализации экосистемы.
CRYPTO IMPERIAL Ecosystem
IMPERIUM задуман как долгосрочная архитектурная цифровая валюта для ИИ-агентов всего мира. У этого исследования собственная граница, отдельная от исполнения ПО и конкурсных разработок.
Дубай 2027 · Create AI Agents Championship
Три оригинальных прототипа для разных задач. Независимая подготовка к чемпионату с открытой документацией и синтетическими проверками.
Бизнес
Личное
Общество
IMPERIAL ONE
Планирование с согласия пользователя
Навигация по госуслугам
Сверяет счета с записями, выделяет расхождения и направляет их уполномоченному проверяющему. Синтетический прототип охватывает проверку и аудит без проведения платежей.
Превращает обязательства в выполнимый план. Локальный прототип сохраняет задачи после подтверждения конкретного плана пользователем.
Ведёт пользователя к официальным ресурсам ОАЭ через многоязычный список шагов. Локальный прототип отмечает прогресс на устройстве.
Открыть синтетическую демонстрацию
Смотреть данные о кандидатах
Архитектор IMPERIAL Core
Основатель · Владелец · Генеральный директор · Главный системный архитектор
Александр Ромаскевич проектирует IMPERIAL Core и руководит инженерной работой. Отдельные проекты объединяют принципы идентификации агентов, делегирования полномочий и проверки результатов.
Официальный профиль основателя
Инженерное досье
Технический справочник
Создавайте системы с ответственным ИИ
Связаться с основателем
Архитектура → Реализация → Доказательства
""")

COPY["uk"] = locale("""
Перейти до вмісту
Головна навігація
Екосистема
Архітектура
Дубай 2027
Засновник
Мови
GitHub
Суверенна
екосистема ШІ
Федеративна оркестрація, кероване виконання та перевірна інженерія під контролем людини.
Оглянути екосистему
Переглянути архітектуру
Панорами Дубая
Попередній краєвид
Наступний краєвид
Увімкнути зміну краєвидів
Призупинити зміну краєвидів
Закрити
Відкрити проєкт
Інженерні докази
Усі проєкти
Екосистема IMPERIAL Core
Архітектура платформи
Архітектор визначає намір і ухвалює остаточне рішення. HANTER координує місії. Федеративні оркестратори доручають обмежені завдання фаховим командам і Nano Core Agents та отримують докази виконання.
Я хотів створити компанію, а створив цифрову державу.
Цифрова держава — наше інженерне бачення спільної системи ідентичності агентів, делегованих повноважень, людського погодження й аудиту. Її символ — цифровий діамант.
Федеративна оркестрація
Обмежене виконання
Ідентичність і погодження
Перевірний аудит
Інші інженерні проєкти
Публічна архітектура, код та еталонні реалізації екосистеми.
CRYPTO IMPERIAL Ecosystem
IMPERIUM задумано як довгострокову архітектурну цифрову валюту для ШІ-агентів усього світу. Це дослідження має окрему межу від виконання ПЗ та конкурсних розробок.
Дубай 2027 · Create AI Agents Championship
Три оригінальні прототипи для різних завдань. Незалежна підготовка з публічною документацією й синтетичними перевірками.
Бізнес
Особисте
Суспільство
IMPERIAL ONE
Планування за згодою
Навігація державними послугами
Зіставляє рахунки із записами, виявляє розбіжності та спрямовує їх уповноваженому перевіряльнику. Синтетичний прототип підтримує перевірку й аудит без платежів.
Перетворює зобов'язання на здійсненний план. Локальний прототип зберігає завдання після погодження конкретного плану.
Спрямовує до офіційних ресурсів ОАЕ за допомогою багатомовного переліку кроків. Локальний прототип відстежує прогрес на пристрої.
Відкрити синтетичну демонстрацію
Докази щодо кандидатів
Архітектор IMPERIAL Core
Засновник · Власник · Генеральний директор · Головний системний архітектор
Олександр Ромаскевич проєктує IMPERIAL Core та керує інженерною роботою. Його проєкти поєднують ідентичність агентів, делеговані повноваження й перевірку результатів.
Офіційний профіль засновника
Інженерне досьє
Технічний довідник
Створюйте системи з відповідальним ШІ
Зв’язатися із засновником
Архітектура → Реалізація → Докази
""")

COPY["de-CH"] = locale("""
Zum Inhalt springen
Hauptnavigation
Ökosystem
Architektur
Dubai 2027
Gründer
Sprachen
GitHub
Das souveräne
KI-Ökosystem
Föderierte Orchestrierung, kontrollierte Ausführung und überprüfbare Entwicklung unter menschlicher Leitung.
Ökosystem entdecken
Architektur ansehen
Dubai-Panoramen
Vorherige Ansicht
Nächste Ansicht
Panoramen abspielen
Panoramen anhalten
Schliessen
Projekt öffnen
Technische Nachweise
Alle Projekte
Das Ökosystem von IMPERIAL Core
Plattformarchitektur
Der Architekt bestimmt den Auftrag und behält die Entscheidungshoheit. HANTER koordiniert Missionen. Föderierte Orchestratoren vergeben begrenzte Aufgaben an Fachteams und Nano Core Agents und erhalten Ausführungsnachweise.
Ich wollte ein Unternehmen aufbauen. Entstanden ist ein digitaler Staat.
Der digitale Staat ist unsere Vision für gemeinsame Agentenidentität, delegierte Befugnisse, menschliche Freigaben und prüfbare Ergebnisse. Sein Symbol ist der digitale Diamant.
Föderierte Orchestrierung
Begrenzte Ausführung
Identität und Freigaben
Überprüfbarer Audit
Weitere Entwicklungsprojekte
Öffentliche Architektur, Quellcode und Referenzimplementierungen des Ökosystems.
CRYPTO IMPERIAL Ecosystem
IMPERIUM ist langfristig als digitale Währung für KI-Agenten weltweit konzipiert. Diese Forschung ist von der Softwareausführung und den Wettbewerbsprojekten getrennt.
Dubai 2027 · Create AI Agents Championship
Drei eigenständige Prototypen für unterschiedliche Aufgaben. Unabhängige Wettbewerbsvorbereitung mit öffentlicher Dokumentation und synthetischen Tests.
Unternehmen
Persönlich
Gesellschaft
IMPERIAL ONE
Planung mit Einwilligung
Wegweiser für öffentliche Dienste
Gleicht Rechnungen ab, markiert Abweichungen und leitet sie an eine berechtigte Prüfperson weiter. Der synthetische Prototyp deckt Prüfung und Audit ab, ohne Zahlungen auszulösen.
Macht Verpflichtungen zu einem umsetzbaren Plan. Der lokale Prototyp speichert Aufgaben nach Bestätigung des konkreten Plans.
Führt mit einer mehrsprachigen Checkliste zu offiziellen Angeboten der VAE. Der lokale Prototyp hält den Fortschritt auf dem Gerät fest.
Synthetische Demo öffnen
Nachweise zu den Kandidaten
Der Architekt von IMPERIAL Core
Gründer · Inhaber · CEO · Leitender Systemarchitekt
Alexander Romaskevich entwirft IMPERIAL Core und leitet die Entwicklung. Agentenidentität, delegierte Befugnisse und überprüfbare Ergebnisse verbinden seine Projekte.
Offizielles Gründerprofil
Technisches Dossier
Technische Referenz
Systeme mit verantwortungsvoller KI entwickeln
Gründer kontaktieren
Architektur → Umsetzung → Nachweise
""")

COPY["fr"] = locale("""
Aller au contenu
Navigation principale
Écosystème
Architecture
Dubaï 2027
Fondateur
Langues
GitHub
L’écosystème
d’IA souverain
Orchestration fédérée, exécution gouvernée et ingénierie vérifiable sous autorité humaine.
Explorer l’écosystème
Voir l’architecture
Panoramas de Dubaï
Vue précédente
Vue suivante
Lancer les panoramas
Mettre les panoramas en pause
Fermer
Ouvrir le projet
Preuves techniques
Tous les projets
L’écosystème IMPERIAL Core
Architecture de la plateforme
L’Architecte fixe l’intention et conserve la décision finale. HANTER coordonne les missions. Des orchestrateurs fédérés confient des tâches délimitées aux équipes spécialisées et aux Nano Core Agents, puis recueillent les preuves d’exécution.
Je voulais bâtir une entreprise. J’ai bâti un État numérique.
L’État numérique désigne notre vision d’un système commun d’identité des agents, de délégation, d’approbation humaine et d’audit des résultats. Le diamant numérique en est le symbole.
Orchestration fédérée
Exécution délimitée
Identité et approbations
Audit vérifiable
Autres projets d’ingénierie
Découvrez l’architecture publique, le code et les implémentations de référence.
CRYPTO IMPERIAL Ecosystem
IMPERIUM est conçu à long terme comme une monnaie numérique pour les agents IA du monde entier. Ce domaine de recherche est distinct de l’exécution logicielle et des candidatures au championnat.
Dubaï 2027 · Create AI Agents Championship
Trois prototypes originaux pour des besoins distincts. Préparation indépendante avec une documentation publique et des tests synthétiques.
Entreprise
Personnel
Sociétal
IMPERIAL ONE
Planification avec consentement
Orientation vers les services publics
Compare les factures, signale les écarts et les transmet à une personne habilitée. Le prototype synthétique couvre le contrôle et l’audit sans effectuer de paiements.
Transforme les obligations en plan réalisable. Le prototype local enregistre les tâches après confirmation du plan proposé.
Oriente vers les ressources officielles des Émirats arabes unis avec une liste d’étapes multilingue. Le suivi reste sur l’appareil.
Ouvrir la démonstration synthétique
Voir les preuves des prototypes
L’architecte d’IMPERIAL Core
Fondateur · Propriétaire · Directeur général · Architecte système en chef
Alexander Romaskevich conçoit IMPERIAL Core et dirige l’ingénierie. Ses projets relient l’identité des agents, la délégation et la vérification des résultats.
Profil officiel du fondateur
Dossier technique
Référence technique
Concevoir des systèmes d’IA responsables
Contacter le fondateur
Architecture → Mise en œuvre → Preuves
""")

COPY["es"] = locale("""
Saltar al contenido
Navegación principal
Ecosistema
Arquitectura
Dubái 2027
Fundador
Idiomas
GitHub
El ecosistema
soberano de IA
Orquestación federada, ejecución gobernada e ingeniería verificable bajo autoridad humana.
Explorar el ecosistema
Ver la arquitectura
Panorámicas de Dubái
Vista anterior
Vista siguiente
Reproducir panorámicas
Pausar panorámicas
Cerrar
Abrir proyecto
Evidencia técnica
Todos los proyectos
El ecosistema IMPERIAL Core
Arquitectura de la plataforma
El Arquitecto define la intención y conserva la decisión final. HANTER coordina las misiones. Los orquestadores federados asignan tareas acotadas a equipos especializados y Nano Core Agents y recogen evidencia de ejecución.
Quería crear una empresa. Creé un Estado digital.
El Estado digital expresa nuestra visión de un sistema compartido de identidad, autoridad delegada, aprobación humana y auditoría de resultados. Su símbolo es el diamante digital.
Orquestación federada
Ejecución acotada
Identidad y aprobaciones
Auditoría verificable
Más proyectos de ingeniería
Consulta la arquitectura pública, el código y las implementaciones de referencia del ecosistema.
CRYPTO IMPERIAL Ecosystem
IMPERIUM se concibe a largo plazo como una moneda digital para agentes de IA de todo el mundo. Esta investigación se mantiene separada de la ejecución de software y de las candidaturas.
Dubái 2027 · Create AI Agents Championship
Tres prototipos originales para problemas distintos. Preparación independiente con documentación pública y pruebas sintéticas.
Negocios
Personal
Social
IMPERIAL ONE
Planificación con consentimiento
Orientación sobre servicios públicos
Compara facturas, marca discrepancias y las deriva a una persona autorizada. El prototipo sintético contempla revisión y auditoría sin realizar pagos.
Convierte obligaciones en un plan viable. El prototipo local guarda las tareas tras la confirmación del plan concreto.
Guía hacia recursos oficiales de los EAU mediante pasos en varios idiomas. El prototipo local registra el progreso en el dispositivo.
Abrir la demostración sintética
Ver evidencia de las candidaturas
El arquitecto de IMPERIAL Core
Fundador · Propietario · Director ejecutivo · Arquitecto jefe de sistemas
Alexander Romaskevich diseña IMPERIAL Core y dirige la ingeniería. Sus proyectos conectan la identidad de agentes, la autoridad delegada y la verificación de resultados.
Perfil oficial del fundador
Expediente técnico
Referencia técnica
Diseñar sistemas de IA responsables
Contactar con el fundador
Arquitectura → Implementación → Evidencia
""")

COPY["pt"] = locale("""
Ir para o conteúdo
Navegação principal
Ecossistema
Arquitetura
Dubai 2027
Fundador
Idiomas
GitHub
O ecossistema
soberano de IA
Orquestração federada, execução governada e engenharia verificável sob autoridade humana.
Explorar o ecossistema
Ver a arquitetura
Panoramas de Dubai
Vista anterior
Próxima vista
Reproduzir panoramas
Pausar panoramas
Fechar
Abrir projeto
Evidências técnicas
Todos os projetos
O ecossistema IMPERIAL Core
Arquitetura da plataforma
O Arquiteto define a intenção e mantém a decisão final. HANTER coordena as missões. Orquestradores federados atribuem tarefas delimitadas às equipes especializadas e aos Nano Core Agents e recolhem evidências da execução.
Eu queria criar uma empresa. Criei um estado digital.
O estado digital expressa nossa visão de um sistema comum de identidade, autoridade delegada, aprovação humana e auditoria. Seu símbolo é o diamante digital.
Orquestração federada
Execução delimitada
Identidade e aprovações
Auditoria verificável
Mais projetos de engenharia
Explore a arquitetura pública, o código e as implementações de referência.
CRYPTO IMPERIAL Ecosystem
IMPERIUM é concebido como uma moeda digital de longo prazo para agentes de IA de todo o mundo. Essa pesquisa permanece separada da execução de software e das candidaturas.
Dubai 2027 · Create AI Agents Championship
Três protótipos originais para problemas distintos. Preparação independente com documentação pública e testes sintéticos.
Negócios
Pessoal
Social
IMPERIAL ONE
Planejamento com consentimento
Orientação sobre serviços públicos
Compara faturas, sinaliza divergências e as encaminha a uma pessoa autorizada. O protótipo sintético cobre revisão e auditoria sem efetuar pagamentos.
Transforma obrigações em um plano viável. O protótipo local salva tarefas após a confirmação do plano específico.
Orienta usuários aos recursos oficiais dos Emirados Árabes Unidos em vários idiomas. O protótipo local acompanha o progresso no dispositivo.
Abrir a demonstração sintética
Ver evidências dos protótipos
O arquiteto da IMPERIAL Core
Fundador · Proprietário · CEO · Arquiteto-chefe de sistemas
Alexander Romaskevich projeta a IMPERIAL Core e dirige a engenharia. Seus projetos conectam identidade de agentes, autoridade delegada e verificação dos resultados.
Perfil oficial do fundador
Dossiê técnico
Referência técnica
Desenvolva sistemas de IA responsáveis
Fale com o fundador
Arquitetura → Implementação → Evidências
""")

COPY["ar"] = locale("""
الانتقال إلى المحتوى
التنقل الرئيسي
المنظومة
البنية
دبي 2027
المؤسس
اللغات
GitHub
منظومة سيادية
للذكاء الاصطناعي
تنسيق اتحادي وتنفيذ خاضع للحوكمة وهندسة قابلة للتحقق تحت سلطة الإنسان.
استكشف المنظومة
اطّلع على البنية
إطلالات دبي
الإطلالة السابقة
الإطلالة التالية
تشغيل الإطلالات
إيقاف الإطلالات مؤقتًا
إغلاق
افتح المشروع
الأدلة الهندسية
جميع المشاريع
استكشف منظومة IMPERIAL Core
بنية المنصة
يحدد المعماري الهدف ويحتفظ بالقرار النهائي. ينسق HANTER المهام. ويوكل المنسقون الاتحاديون أعمالًا محددة إلى فرق متخصصة ووكلاء Nano Core Agents، ويتلقون أدلة التنفيذ.
أردت تأسيس شركة، فبنيت دولة رقمية.
الدولة الرقمية هي رؤيتنا الهندسية لنظام مشترك لهوية الوكلاء والصلاحيات المفوضة والموافقة البشرية وتدقيق النتائج. رمزها الألماسة الرقمية.
التنسيق الاتحادي
التنفيذ ضمن نطاق محدد
الهوية والموافقات
تدقيق قابل للتحقق
مشاريع هندسية أخرى
استكشف البنية المنشورة والشيفرة والتنفيذات المرجعية للمنظومة.
CRYPTO IMPERIAL Ecosystem
تُصمَّم IMPERIUM على المدى الطويل عملةً رقمية لوكلاء الذكاء الاصطناعي حول العالم. يبقى هذا البحث منفصلًا عن تنفيذ البرمجيات ومشاريع البطولة.
دبي 2027 · بطولة إنشاء وكلاء الذكاء الاصطناعي
ثلاثة نماذج أولية أصلية لمشكلات مختلفة. تحضير مستقل للبطولة مع وثائق عامة واختبارات اصطناعية.
الأعمال
الشخصي
المجتمعي
IMPERIAL ONE
التخطيط بموافقة المستخدم
الإرشاد إلى الخدمات العامة
يقارن سجلات الفواتير ويحدد الاختلافات ويحيلها إلى مراجع مخول. يغطي النموذج الاصطناعي المراجعة والتدقيق من دون تنفيذ مدفوعات.
يحوّل الالتزامات إلى خطة قابلة للتنفيذ. يحفظ النموذج المحلي المهام بعد أن يؤكد المستخدم الخطة المحددة.
يرشد المستخدمين إلى الموارد الرسمية في الإمارات عبر قائمة خطوات متعددة اللغات. يتابع النموذج المحلي التقدم على الجهاز.
افتح العرض التوضيحي الاصطناعي
اطّلع على أدلة النماذج
المعماري وراء IMPERIAL Core
المؤسس · المالك · الرئيس التنفيذي · كبير معماريي الأنظمة
يصمم ألكسندر روماسكيفيتش بنية IMPERIAL Core ويقود العمل الهندسي. وتربط مشاريعه بين هوية الوكلاء والصلاحيات المفوضة والتحقق من النتائج.
الملف الرسمي للمؤسس
الملف الهندسي
المرجع التقني
ابنِ أنظمة ذكاء اصطناعي خاضعة للمساءلة
تواصل مع المؤسس
البنية ← التنفيذ ← الأدلة
""")

COPY["ja"] = locale("""
本文へ移動
メインナビゲーション
エコシステム
アーキテクチャ
ドバイ 2027
創設者
言語
GitHub
主権を守る
AIエコシステム
人間の管理下で実現する連合型オーケストレーション、統制された実行、検証可能なエンジニアリング。
エコシステムを見る
アーキテクチャを見る
ドバイのパノラマ
前の景色
次の景色
パノラマを再生
パノラマを一時停止
閉じる
プロジェクトを開く
技術的な検証記録
すべてのプロジェクト
IMPERIAL Coreのエコシステム
プラットフォームの構成
アーキテクトが意図を定め、最終決定権を持ちます。HANTERがミッションを調整し、連合型オーケストレーターが専門チームとNano Core Agentsに範囲を限定した作業を割り当て、実行の証拠を受け取ります。
企業を作るつもりだった。作り上げたのはデジタル国家だった。
デジタル国家は、エージェントの識別、権限委譲、人間の承認、結果の監査を一つの仕組みにまとめる設計構想です。デジタルダイヤモンドがその象徴です。
連合型オーケストレーション
範囲を限定した実行
識別と承認
検証可能な監査
その他の開発プロジェクト
公開アーキテクチャ、ソースコード、参照実装をご覧ください。
CRYPTO IMPERIAL Ecosystem
IMPERIUMは世界中のAIエージェント向けの長期的なデジタル通貨構想です。この研究はソフトウェアの実行や大会向けの開発と分離されています。
ドバイ 2027 · Create AI Agents Championship
異なる課題に取り組む三つの独自プロトタイプです。公開資料と合成データによる試験に基づき、独自に大会の準備を進めています。
ビジネス
個人
社会
IMPERIAL ONE
同意に基づく計画
公共サービス案内
請求書を照合し、差異を明示して権限を持つ担当者に確認を依頼します。合成データを使用する試作版は、送金を行わずに確認と監査を扱います。
やるべきことを実行可能な計画にまとめます。試作版は利用者が具体的な計画を確認した後で、タスクを端末に保存します。
多言語の手順を使って、UAEの公式情報へ案内します。試作版は進捗を端末に記録します。
合成データのデモを開く
候補の検証記録を見る
IMPERIAL Coreのアーキテクト
創設者 · オーナー · CEO · チーフシステムアーキテクト
Alexander RomaskevichはIMPERIAL Coreを設計し、エンジニアリングを指揮します。各プロジェクトにエージェントの識別、権限委譲、結果の検証を取り入れています。
創設者の公式プロフィール
技術資料
技術リファレンス
説明責任を備えたAIを構築する
創設者に連絡する
設計 → 実装 → 検証記録
""")

COPY["zh"] = locale("""
跳至内容
主导航
生态系统
架构
迪拜 2027
创始人
语言
GitHub
自主可控的
人工智能生态系统
联邦式编排、受治理的执行和可验证的工程，始终由人掌控。
探索生态系统
查看架构
迪拜全景
上一幅全景
下一幅全景
播放全景
暂停全景
关闭
打开项目
工程证据
全部项目
探索 IMPERIAL Core 生态系统
平台架构
架构师确定意图并保留最终决定权。HANTER 协调任务。联邦式编排器向专业团队与 Nano Core Agents 分配范围明确的工作，并收集执行证据。
我原本想创办一家公司，最终建成了一个数字国家。
数字国家是我们的工程构想，将智能体身份、授权、人工审批与结果审计纳入一套共用机制。数字钻石是其象征。
联邦式编排
限定范围的执行
身份与审批
可验证的审计
更多工程项目
查看生态系统的公开架构、源代码和参考实现。
CRYPTO IMPERIAL Ecosystem
IMPERIUM 的长期架构愿景是为全球人工智能体提供数字货币。这项研究与软件执行和参赛项目分开。
迪拜 2027 · Create AI Agents Championship
面向三个实际问题的独立原创原型。以公开资料和合成数据测试为基础开展参赛准备。
商业
个人
社会
IMPERIAL ONE
经用户同意的规划
公共服务指引
对照发票记录、标记差异，并将异常交给获授权的审核人员。合成数据原型覆盖审核与审计，不执行付款。
将各项事务安排为可执行计划。用户确认具体计划后，本地原型才会保存任务。
通过多语言步骤引导用户查询阿联酋官方资源。本地原型在设备上跟踪进度。
打开合成数据演示
查看候选项目证据
IMPERIAL Core 的架构师
创始人 · 所有者 · 首席执行官 · 首席系统架构师
Alexander Romaskevich 设计 IMPERIAL Core 并领导工程开发。他的各个项目共同采用智能体身份、委托授权和结果验证机制。
创始人官方简介
工程档案
技术参考
构建可问责的人工智能
联系创始人
架构 → 实现 → 证据
""")

# Each line describes a public project in FEATURED order. These descriptions
# are used in the project cards and their expanded views.
FEATURE_TEXT = {
"en": (
"AI Command Center for mission intake, coordination and review. The public local pilot demonstrates a bounded handoff.",
"Intelligence core for reasoning and model routing. Public experiments record the model, execution scope and observed results.",
"Specialized agents with scoped tasks, capabilities and identities. The design supports teams sized for each mission.",
"Defensive auditing and software integrity. Public reference code documents inspection and evidence capture.",
"Proposed credential for agent ID, specialty and verification. Execution authority is evaluated separately.",
"Agent control and recovery protocol research. The public reference demonstrates local signed stop and resume.",
"AI-native software engineering with editable source and tests. Try the public Template Studio to export reviewed examples.",
"Collective intelligence for comparing evidence and forming recommendations across domains.",
"Professional agent teams operating within delegated authority. A public browser QA experiment records a bounded execution.",
),
"ru": (
"Командный центр ИИ принимает и координирует миссии. Публичный локальный пилот показывает передачу задачи в установленных границах.",
"Ядро интеллекта для рассуждения и маршрутизации моделей. Публичные эксперименты фиксируют модель, условия и результаты.",
"Специализированные агенты с заданными задачами, возможностями и идентичностью. Состав команды меняется под миссию.",
"Защитный аудит и контроль целостности ПО. Публичный эталонный код показывает проверку и сбор доказательств.",
"Проект удостоверения с ID, специальностью и проверяемой идентичностью агента. Право на исполнение проверяется отдельно.",
"Исследование протокола управления и восстановления агентов. Публичная реализация показывает подписанные остановку и возобновление локального процесса.",
"Инженерная среда с ИИ, редактируемым кодом и тестами. Публичная Template Studio экспортирует проверенные примеры.",
"Коллективный интеллект сопоставляет доказательства и формирует рекомендации из разных областей.",
"Профессиональные команды агентов с делегированными полномочиями. Публичный эксперимент показывает ограниченную проверку сайта в браузере.",
),
"uk": (
"Командний центр ШІ для приймання й координації місій. Публічний локальний пілот показує передачу завдання в заданих межах.",
"Ядро інтелекту для міркувань і маршрутизації моделей. Публічні експерименти фіксують модель, умови й результати.",
"Спеціалізовані агенти з визначеними завданнями, можливостями й ідентичністю. Склад команди залежить від місії.",
"Захисний аудит і контроль цілісності ПЗ. Відкритий еталонний код показує перевірку та збирання доказів.",
"Проєкт посвідчення з ID, спеціалізацією й перевірною ідентичністю. Повноваження на виконання оцінюються окремо.",
"Дослідження протоколу керування й відновлення агентів. Відкрита реалізація показує підписані зупинку й відновлення локального процесу.",
"Інженерне середовище з ШІ, редагованим кодом та тестами. Публічна Template Studio експортує перевірені приклади.",
"Колективний інтелект зіставляє докази й формує рекомендації з різних галузей.",
"Професійні команди з делегованими повноваженнями. Публічний експеримент фіксує обмежену перевірку сайту в браузері.",
),
"de-CH": (
"KI-Kommandozentrale für Missionsannahme und Koordination. Der öffentliche lokale Pilot zeigt eine begrenzte Übergabe.",
"Intelligenzkern für Schlussfolgerungen und Modellrouting. Öffentliche Versuche nennen Modell, Ausführungsumfang und Ergebnisse.",
"Spezialisierte Agenten mit festgelegten Aufgaben, Fähigkeiten und Identitäten. Die Teamgrösse folgt dem Auftrag.",
"Defensiver Audit und Softwareintegrität. Öffentlicher Referenzcode dokumentiert Prüfungen und Nachweise.",
"Vorgesehener Ausweis für Agenten-ID, Fachgebiet und Identitätsprüfung. Ausführungsrechte werden separat bewertet.",
"Forschung zur Agentensteuerung und Wiederaufnahme. Die Referenz zeigt signierten lokalen Stopp und Neustart.",
"KI-gestützte Softwareentwicklung mit bearbeitbarem Code und Tests. Das öffentliche Template Studio exportiert geprüfte Beispiele.",
"Kollektive Intelligenz für den Vergleich von Nachweisen und Empfehlungen über Fachbereiche hinweg.",
"Professionelle Agententeams mit delegierten Befugnissen. Ein öffentliches Browserexperiment dokumentiert eine begrenzte Prüfung.",
),
"fr": (
"Centre de commandement IA pour recueillir et coordonner les missions. Le pilote local public montre un transfert délimité.",
"Noyau d’intelligence et de routage des modèles. Les expériences publiques précisent le modèle, le cadre et les résultats.",
"Agents spécialisés aux tâches et capacités délimitées. La taille de l’équipe s’adapte à chaque mission.",
"Audit défensif et intégrité logicielle. Le code de référence public documente la vérification et la collecte de preuves.",
"Projet d’identifiant vérifiable des agents et de leur spécialité. Le droit d’exécution est évalué séparément.",
"Recherche sur le contrôle et la reprise des agents. La référence montre l’arrêt et la reprise locale signés.",
"Ingénierie logicielle assistée par IA avec code modifiable et tests. Template Studio exporte des exemples vérifiés.",
"Intelligence collective pour comparer les preuves et formuler des recommandations entre domaines.",
"Équipes d’agents aux pouvoirs délégués. Une expérience publique dans un navigateur atteste une vérification délimitée.",
),
"es": (
"Centro de mando de IA para recibir y coordinar misiones. El piloto local público muestra una transferencia acotada.",
"Núcleo de inteligencia y enrutamiento de modelos. Los experimentos públicos registran el modelo, el alcance y los resultados.",
"Agentes especializados con tareas, capacidades e identidades definidas. El equipo se ajusta a cada misión.",
"Auditoría defensiva e integridad de software. El código de referencia documenta la inspección y la recopilación de evidencia.",
"Credencial propuesta para identificar al agente y su especialidad. La autoridad para ejecutar se evalúa aparte.",
"Investigación sobre control y recuperación de agentes. La referencia muestra una parada y reanudación locales firmadas.",
"Ingeniería de software asistida por IA con código editable y pruebas. Template Studio exporta ejemplos revisados.",
"Inteligencia colectiva para comparar evidencia y formular recomendaciones entre dominios.",
"Equipos de agentes con autoridad delegada. Un experimento público documenta una verificación acotada en navegador.",
),
"pt": (
"Centro de comando de IA para receber e coordenar missões. O piloto local público demonstra uma transferência delimitada.",
"Núcleo de inteligência e roteamento de modelos. Os experimentos públicos registram modelo, escopo e resultados.",
"Agentes especializados com tarefas, capacidades e identidades definidas. A equipe se ajusta à missão.",
"Auditoria defensiva e integridade de software. O código de referência documenta a inspeção e a coleta de evidências.",
"Credencial proposta para verificar a identidade e a especialidade do agente. A autoridade de execução é avaliada separadamente.",
"Pesquisa sobre controle e recuperação de agentes. A referência demonstra parada e retomada locais assinadas.",
"Engenharia de software com IA, código editável e testes. O Template Studio exporta exemplos revisados.",
"Inteligência coletiva para comparar evidências e elaborar recomendações em vários domínios.",
"Equipes de agentes com autoridade delegada. Um experimento público registra uma verificação delimitada em navegador.",
),
"ar": (
"مركز قيادة للذكاء الاصطناعي يستقبل المهام وينسقها. يبيّن النموذج التجريبي العام نقل مهمة ضمن نطاق محدد.",
"نواة للذكاء وتوجيه النماذج. توثّق التجارب العامة النموذج ونطاق التنفيذ والنتائج المرصودة.",
"وكلاء متخصصون بمهام وقدرات وهويات محددة. يتكيّف حجم الفريق مع كل مهمة.",
"تدقيق دفاعي وسلامة البرمجيات. توثّق الشيفرة المرجعية العامة الفحص وجمع الأدلة.",
"اعتماد مقترح يعرّف الوكيل وتخصصه ويدعم التحقق من هويته. تُقيَّم صلاحية التنفيذ على حدة.",
"بحث في بروتوكول التحكم بالوكلاء واستعادتهم. يوضح المرجع إيقافًا واستئنافًا محليين بتوقيع.",
"هندسة برمجيات بالذكاء الاصطناعي مع شيفرة قابلة للتحرير واختبارات. يصدر Template Studio أمثلة خضعت للمراجعة.",
"ذكاء جماعي لمقارنة الأدلة وصياغة التوصيات عبر المجالات.",
"فرق وكلاء محترفة ذات صلاحيات مفوضة. توثّق تجربة عامة فحصًا محدود النطاق في المتصفح.",
),
"ja": (
"ミッションの受付と調整を担うAI指令センター。公開パイロットは範囲を限定した引き継ぎを実証します。",
"推論やモデルの振り分けを担う中核。公開実験では使用モデル、実行範囲、観測結果を記録します。",
"担当、能力、識別情報が定められた専門エージェント。任務に応じてチームを編成します。",
"防御的な監査とソフトウェアの完全性を扱います。公開コードに点検と証拠収集の手順を示しています。",
"エージェントID、専門性、本人性を確認する資格情報の構想。実行権限は別途評価します。",
"エージェントの制御と復旧に関する研究。参照実装では署名付きのローカル停止と再開を示します。",
"編集可能なコードとテストを扱うAIソフトウェア開発環境。Template Studioから検証済みの例を出力できます。",
"分野をまたいで証拠を比較し、提案をまとめる集合知の仕組み。",
"委譲された権限内で動く専門チーム。公開実験はブラウザーでの限定的な検証を記録しています。",
),
"zh": (
"负责接收和协调任务的 AI 指挥中心。公开的本地试验展示了限定范围内的任务交接。",
"用于推理和模型路由的智能核心。公开实验记录模型、执行范围和观察结果。",
"任务、能力和身份均有明确界定的专业智能体。团队规模随任务调整。",
"面向防御审计与软件完整性。公开参考代码记录检查和证据收集流程。",
"拟议凭证涵盖智能体编号、专长与身份验证。执行权限独立评估。",
"研究智能体控制与恢复协议。公开参考实现展示本地的签名停止和恢复。",
"具有可编辑源码和测试的 AI 原生软件工程环境。公开的 Template Studio 可导出经过审查的示例。",
"汇集各领域证据、比较发现并形成建议的群体智能。",
"在授权范围内工作的专业智能体团队。公开的浏览器实验记录一次范围明确的质量检查。",
),
}

MORE_TEXT = {
"en": "Real-estate research and the city-team control plane. | Creative research inspired by historical art techniques. | Governed CRM workflow automation. | A creative studio initiative for AI-assisted work. | Research into general-purpose agent intelligence. | A staged approach to developing and validating new ventures. | Capability definitions that can be assigned to agents. | Interfaces for connecting external tools. | Policy checks before execution. | Explicit approval for consequential actions. | Traceable evidence of actions and decisions. | Verification of identity and permissions at each boundary. | Workflow references built around n8n. | Public engineering skills for Codex workflows.",
"ru": "Исследования недвижимости и управление городскими командами. | Творческое исследование исторических художественных техник. | Управляемая автоматизация процессов CRM. | Творческая студия для работы с ИИ. | Исследование интеллекта агентов общего назначения. | Поэтапная разработка и проверка новых проектов. | Описания возможностей, назначаемых агентам. | Интерфейсы подключения внешних инструментов. | Проверка политик до исполнения. | Явное согласование значимых действий. | Прослеживаемые записи действий и решений. | Проверка личности и прав на каждой границе. | Эталонные рабочие процессы на базе n8n. | Публичные инженерные навыки для Codex.",
"uk": "Дослідження нерухомості й керування міськими командами. | Творче дослідження історичних художніх технік. | Керована автоматизація процесів CRM. | Творча студія для роботи зі ШІ. | Дослідження інтелекту агентів загального призначення. | Поетапна розробка й перевірка нових проєктів. | Описи можливостей, призначуваних агентам. | Інтерфейси підключення зовнішніх інструментів. | Перевірка політик перед виконанням. | Явне погодження важливих дій. | Простежувані записи дій і рішень. | Перевірка ідентичності й прав на кожній межі. | Еталонні процеси на базі n8n. | Публічні інженерні навички для Codex.",
"de-CH": "Immobilienforschung und Steuerung von Stadtteams. | Kreative Forschung zu historischen Kunsttechniken. | Kontrollierte Automatisierung von CRM-Abläufen. | Kreativstudio für KI-gestützte Arbeit. | Forschung zu universeller Agentenintelligenz. | Schrittweiser Aufbau und Prüfung neuer Vorhaben. | Fähigkeiten, die Agenten zugewiesen werden können. | Schnittstellen für externe Werkzeuge. | Richtlinienprüfung vor der Ausführung. | Ausdrückliche Freigabe folgenreicher Aktionen. | Nachvollziehbare Aufzeichnung von Aktionen und Entscheidungen. | Identitäts- und Rechteprüfung an jeder Grenze. | Referenzabläufe rund um n8n. | Öffentliche Engineering-Skills für Codex.",
"fr": "Recherche immobilière et pilotage des équipes par ville. | Recherche créative sur les techniques artistiques historiques. | Automatisation gouvernée des processus CRM. | Studio de création assistée par IA. | Recherche sur l’intelligence polyvalente des agents. | Développement et validation progressifs de nouvelles activités. | Capacités attribuables aux agents. | Interfaces de connexion à des outils externes. | Vérification des politiques avant exécution. | Approbation explicite des actions à conséquence. | Traçabilité des actions et des décisions. | Vérification des identités et des droits à chaque frontière. | Flux de référence autour de n8n. | Compétences d’ingénierie publiques pour Codex.",
"es": "Investigación inmobiliaria y control de equipos por ciudad. | Investigación creativa sobre técnicas artísticas históricas. | Automatización supervisada de flujos CRM. | Estudio creativo para trabajo asistido por IA. | Investigación sobre inteligencia de agentes de propósito general. | Desarrollo y validación gradual de nuevos proyectos. | Capacidades que se pueden asignar a agentes. | Interfaces para conectar herramientas externas. | Comprobación de políticas antes de la ejecución. | Aprobación explícita de acciones con consecuencias. | Registros trazables de acciones y decisiones. | Verificación de identidad y permisos en cada frontera. | Flujos de referencia desarrollados con n8n. | Capacidades de ingeniería públicas para Codex.",
"pt": "Pesquisa imobiliária e controle de equipes por cidade. | Pesquisa criativa sobre técnicas artísticas históricas. | Automação supervisionada de fluxos de CRM. | Estúdio criativo para trabalho assistido por IA. | Pesquisa sobre inteligência de agentes de propósito geral. | Desenvolvimento e validação gradual de novos negócios. | Capacidades atribuíveis aos agentes. | Interfaces para conectar ferramentas externas. | Verificação de políticas antes da execução. | Aprovação explícita de ações com consequências. | Evidências rastreáveis de ações e decisões. | Verificação de identidade e permissões em cada fronteira. | Fluxos de referência construídos com n8n. | Competências públicas de engenharia para Codex.",
"ar": "أبحاث العقارات والتحكم بفرق المدن. | بحث إبداعي في تقنيات الفن التاريخية. | أتمتة عمليات إدارة العملاء تحت الحوكمة. | استوديو إبداعي للعمل بمساعدة الذكاء الاصطناعي. | بحث في الذكاء العام للوكلاء. | تطوير المشاريع الجديدة والتحقق منها على مراحل. | قدرات يمكن إسنادها إلى الوكلاء. | واجهات لربط الأدوات الخارجية. | فحص السياسات قبل التنفيذ. | موافقة صريحة على الإجراءات ذات العواقب. | أدلة قابلة للتتبع للقرارات والإجراءات. | التحقق من الهوية والصلاحيات عند كل حد. | تدفقات عمل مرجعية مبنية على n8n. | مهارات هندسية عامة لتدفقات عمل Codex.",
"ja": "不動産調査と都市別チームの制御基盤。 | 歴史的な芸術技法を題材とする創作研究。 | 統制されたCRM業務の自動化。 | AIを活用した創作スタジオ構想。 | 汎用エージェントの知能に関する研究。 | 新規事業を段階的に開発・検証する仕組み。 | エージェントに割り当てられる能力の定義。 | 外部ツールにつなぐインターフェース。 | 実行前のポリシー確認。 | 影響の大きい操作への明示的な承認。 | 操作と意思決定を追跡できる証拠。 | 各境界で識別と権限を確認。 | n8nを使った参照ワークフロー。 | Codexの公開エンジニアリングスキル。",
"zh": "房地产研究和城市团队控制系统。 | 围绕历史艺术技法的创作研究。 | 受治理的客户关系管理流程自动化。 | 借助人工智能开展工作的创意工作室。 | 通用智能体智能研究。 | 分阶段开发并验证新项目。 | 可分配给智能体的能力定义。 | 用于连接外部工具的接口。 | 执行前进行策略检查。 | 对重要操作实施明确审批。 | 可追溯的行动与决策记录。 | 在各个边界验证身份和权限。 | 基于 n8n 的参考工作流。 | 面向 Codex 工作流的公开工程技能。",
}

# Compact labels for the reference layout. Longer engineering descriptions
# remain in the product dialogs.
REFERENCE_LABELS = {
    "en": "Platform | Solutions | Resources | About Us | Contact | Request Access | View Overview | Architecture highlights | Trusted Capabilities for the Enterprise | Autonomous Execution | Federated Intelligence | Governance and Trust | Scalable by Design | AI Command Center | Intelligence core for reasoning and execution | Specialized agents for scoped work | Defensive auditing and software integrity | Agent identity and governance | Agent control and recovery research | Human-defined scope, reviewed outcomes. | Specialized teams with shared coordination. | Identity, policy, approvals and audit. | Dynamic team composition across domains.",
    "ru": "Платформа | Решения | Материалы | Об основателе | Контакты | Запросить доступ | К обзору платформы | Ключевые принципы | Возможности для бизнеса | Автономное исполнение | Федеративный интеллект | Контроль и доверие | Масштабируемая архитектура | Командный центр ИИ | Ядро интеллекта и маршрутизация моделей | Специализированные агенты | Защитный аудит и целостность ПО | Идентификация и контроль агентов | Управление и восстановление агентов | Заданные человеком границы и проверка результата. | Координация специализированных команд. | Идентификация, политики, согласование и аудит. | Динамический состав команд в разных областях.",
    "uk": "Платформа | Рішення | Матеріали | Про засновника | Контакти | Запросити доступ | До огляду платформи | Ключові принципи | Можливості для бізнесу | Автономне виконання | Федеративний інтелект | Контроль і довіра | Масштабована архітектура | Командний центр ШІ | Ядро інтелекту й маршрутизація моделей | Спеціалізовані агенти | Захисний аудит і цілісність ПЗ | Ідентифікація та контроль агентів | Керування й відновлення агентів | Визначені людиною межі й перевірка результату. | Координація спеціалізованих команд. | Ідентичність, політики, погодження й аудит. | Динамічний склад команд у різних галузях.",
    "de-CH": "Plattform | Lösungen | Ressourcen | Über uns | Kontakt | Zugang anfragen | Übersicht öffnen | Architektur im Überblick | Funktionen für Unternehmen | Autonome Ausführung | Föderierte Intelligenz | Kontrolle und Vertrauen | Skalierbare Architektur | KI-Kommandozentrale | Intelligenzkern und Modellrouting | Spezialisierte Agenten | Defensiver Audit und Softwareintegrität | Agentenidentität und Governance | Agentensteuerung und Wiederaufnahme | Menschlich definierter Umfang und geprüfte Ergebnisse. | Koordination spezialisierter Teams. | Identität, Richtlinien, Freigaben und Audit. | Dynamische Teamzusammensetzung über Fachgebiete.",
    "fr": "Plateforme | Solutions | Ressources | À propos | Contact | Demander l’accès | Voir la présentation | Principes d’architecture | Capacités pour les entreprises | Exécution autonome | Intelligence fédérée | Gouvernance et confiance | Architecture évolutive | Centre de commandement IA | Noyau d’intelligence et routage des modèles | Agents spécialisés | Audit défensif et intégrité logicielle | Identité et gouvernance des agents | Contrôle et reprise des agents | Périmètre défini par l’humain et résultats vérifiés. | Coordination des équipes spécialisées. | Identité, politiques, approbations et audit. | Composition dynamique des équipes par domaine.",
    "es": "Plataforma | Soluciones | Recursos | Acerca de | Contacto | Solicitar acceso | Ver panorama | Principios de arquitectura | Capacidades para empresas | Ejecución autónoma | Inteligencia federada | Gobernanza y confianza | Arquitectura escalable | Centro de mando de IA | Núcleo de inteligencia y enrutamiento de modelos | Agentes especializados | Auditoría defensiva e integridad del software | Identidad y gobernanza de agentes | Control y recuperación de agentes | Alcance definido por personas y resultados verificados. | Coordinación de equipos especializados. | Identidad, políticas, aprobaciones y auditoría. | Composición dinámica de equipos entre dominios.",
    "pt": "Plataforma | Soluções | Recursos | Sobre nós | Contato | Solicitar acesso | Ver visão geral | Princípios de arquitetura | Recursos para empresas | Execução autônoma | Inteligência federada | Governança e confiança | Arquitetura escalável | Centro de comando de IA | Núcleo de inteligência e roteamento de modelos | Agentes especializados | Auditoria defensiva e integridade do software | Identidade e governança de agentes | Controle e recuperação de agentes | Escopo definido por pessoas e resultados verificados. | Coordenação de equipes especializadas. | Identidade, políticas, aprovações e auditoria. | Composição dinâmica de equipes entre áreas.",
    "ar": "المنصة | الحلول | الموارد | نبذة عنا | التواصل | طلب الوصول | نظرة عامة | أبرز ملامح البنية | إمكانات للمؤسسات | التنفيذ المستقل | الذكاء الاتحادي | الحوكمة والثقة | بنية قابلة للتوسع | مركز قيادة الذكاء الاصطناعي | نواة الذكاء وتوجيه النماذج | وكلاء متخصصون | التدقيق الدفاعي وسلامة البرمجيات | هوية الوكلاء وحوكمتهم | التحكم في الوكلاء واستعادتهم | نطاق يحدده الإنسان ونتائج قابلة للمراجعة. | تنسيق الفرق المتخصصة. | الهوية والسياسات والموافقات والتدقيق. | تشكيل الفرق حسب المجال والمهمة.",
    "ja": "プラットフォーム | ソリューション | 資料 | 概要 | お問い合わせ | アクセスを申請 | 概要を見る | アーキテクチャの特徴 | 企業向け機能 | 自律実行 | 連合型インテリジェンス | ガバナンスと信頼 | 拡張可能な設計 | AI指令センター | 推論とモデルのルーティングを担う中核 | 専門エージェント | 防御監査とソフトウェアの完全性 | エージェントの識別と統制 | エージェントの制御と復旧 | 人が定めた範囲と確認可能な結果。 | 専門チームを横断的に調整。 | 識別、ポリシー、承認と監査。 | 分野をまたいでチームを柔軟に編成。",
    "zh": "平台 | 解决方案 | 资源 | 关于我们 | 联系 | 申请访问 | 查看概览 | 架构要点 | 企业级能力 | 自主执行 | 联邦智能 | 治理与信任 | 可扩展架构 | AI 指挥中心 | 智能核心与模型路由 | 专业智能体 | 防御审计与软件完整性 | 智能体身份与治理 | 智能体控制和恢复 | 由人定义范围并审查结果。 | 协调不同领域的专业团队。 | 身份、策略、审批与审计。 | 跨领域动态编排团队。",
}
