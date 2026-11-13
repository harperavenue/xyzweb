"""Builds the staging site: index.html plus one page per level.

Run:  python3 build.py
Edit the content dictionaries below, then rebuild. All pages share css/site.css.
"""
import html, pathlib

ROOT = pathlib.Path(__file__).parent
BRAND = "XYZ Partners"
TAGLINE = "Finance Expertise From Both Sides of the Deal"
CTA = "Let's have a discussion"

THEMES = ["Numbers you can trust", "One version of the truth", "Plans that hold",
          "Cash and capital, covered", "Ready for scrutiny", "Ready for the deal"]

FOUNDERS = {
    "pritpal": {"name": "Pritpal Aujla", "img": "pritpal.jpg", "leads": "Leads PE Fund and Firm",
                "short": "20 years as CFO / COO of PE Firms"},
    "bart": {"name": "Bart Bruckert", "img": "bart.jpg", "leads": "Leads Portfolio Company",
             "short": "10+ years as a PE-backed CFO"},
}

RESULTS = {
    "pritpal": [
        ("Spin-out", "$5B → $25B", "AUM after spinning out of a $70B+ manager; back office from 5 to 40 people"),
        ("Team build", "$75B+", "AUM today at PE Firms where we built finance teams from scratch"),
        ("Valuations", "20 → 5 days", "Quarter-end valuations, cut platform-wide"),
        ("Integrated systems", "IC → ENI", "Connected systems from the Fund investment committee to Firm ENI, replacing Excel"),
        ("Financing", "$5B+", "Subscription, NAV and hybrid facilities; Firm-level private debt and GP stake sales"),
    ],
    "bart": [
        ("Joint venture", "3 teams", "Finance team, processes, systems and banking built from scratch for a joint venture of three pro sports franchises"),
        ("Buyout", "$40M+", "Annualized EBITDA improvements, working with the sponsor after a $3.6B buyout"),
        ("Month-end close", "20 → 4 days", "Close cut by 80%, with better accuracy"),
        ("Lenders and liquidity", "6+ months", "Of liquidity pressure managed on 13-week cash flow, with new lender facilities"),
        ("Sale", "$7.2B", "Led corporate finance through the sale of a sponsor-backed media company to a strategic buyer"),
    ],
}

LEVELS = {
    "fund": {
        "slug": "pe-fund", "name": "PE Fund", "plural": "PE Funds", "founder": "pritpal", "pc": False,
        "question": "Can we give our LPs what they want, when they want it?",
        "lead": "Senior fund finance leadership that keeps LP reporting, cash and valuations ahead of the questions, working alongside your administrator, never in place of it.",
        "pains": [
            ("Hard to keep up", "LPs want more, faster; quarter-ends take weeks"),
            ("Disconnected systems", "One change doesn't flow through, so performance data lags"),
            ("Cash surprises", "Capital calls and distributions are hard to forecast"),
            ("Reporting risk", "One error can cost LP trust, and the next Fund"),
        ],
        "grid": ["Administrator oversight and shadow books",
                 "LP and Fund reporting · Investor relations support",
                 "Portfolio monitoring and KPI dashboards · Fund forecasting and returns",
                 "Capital call and distribution forecasting · Subscription and NAV facilities",
                 "Defensible valuations · Fund audit coordination · Fund tax and K-1 oversight",
                 "Due diligence and 100-day plans"],
        "themes": [
            ("Can we check what our administrator sends us?",
             "We review your administrator's work each period and keep shadow books where it matters, so errors are caught before an LP sees them.",
             ["Administrator oversight", "Shadow books"]),
            ("Can we answer any LP request within 48 hours?",
             "Quarterly reports, capital account statements and ad hoc requests, all drawn from one reconciled set of data.",
             ["LP and Fund reporting", "Investor relations support"]),
            ("How is each investment really performing?",
             "Portfolio Company KPIs collected in a consistent format and tied through to Fund-level returns.",
             ["Portfolio monitoring and KPI dashboards", "Fund forecasting and returns"]),
            ("Will a capital call ever catch us out?",
             "A rolling view of calls, distributions and facility headroom, so cash needs are known weeks ahead.",
             ["Capital call and distribution forecasting", "Subscription and NAV facilities"]),
            ("Would our valuations stand up to the auditors and the SEC?",
             "A repeatable valuation process with the support auditors expect, and Fund tax deliverables tracked to deadline.",
             ["Consistent, defensible valuations", "Fund audit coordination", "Oversight of Fund tax and K-1s"]),
            ("Can we move fast on the next investment?",
             "Finance diligence on targets, and a 100-day plan that sets up the new Portfolio Company's reporting from day one.",
             ["Deal support: due diligence", "100-day plans"]),
        ],
        "stats_head": "LPs want more detail, more often, more consistency",
        "stats_sub": "Being smaller is no free pass: LPs expect the same standards as larger firms.",
        "stats": [("44%", "of LPs say they are not getting the detailed performance reporting they need"),
                  ("74%", "expect daily or on-demand access to portfolio performance data"),
                  ("41%", "say technology and data demands have risen most since 2024")],
        "sources": "Sources: CSC, Future Private Capital CFO 2025 (200 LPs globally); SS&amp;C Intralinks 2026 LP Survey (370 LPs); Alter Domus, The capacity dividend, 2026 (administrator view). All three provide services to GPs.",
        "results": [0, 2, 3, 4],
    },
    "firm": {
        "slug": "pe-firm", "name": "PE Firm", "plural": "PE Firms", "founder": "pritpal", "pc": False,
        "question": "Is our back office built for where the Firm is going?",
        "lead": "Management company finance that shows what the Firm really earns, takes owner economics out of spreadsheets, and is ready for an SEC exam or a GP stake sale.",
        "pains": [
            ("Systems that can't keep up", "Hard to say why, but they fall behind as AUM grows"),
            ("Profitability hard to see", "FRE, Firm vs. Fund and controllable costs are unclear"),
            ("Owner economics by hand", "Carry, distributions and owner tax live in spreadsheets"),
            ("Key-person risk", "PE finance talent is scarce outside the hubs"),
        ],
        "grid": ["Management company close, A/P and payroll · Firm vs. Fund cost allocation",
                 "DE, FRE and ENI reporting, monthly to annual",
                 "Budgeting and forecasting by strategy · Profitability and cost control",
                 "Treasury and owner distributions · Firm-level debt facilities",
                 "SEC exam preparedness · Carried interest tracking · Owner tax oversight",
                 "Corporate model · GP stake and capital transactions"],
        "themes": [
            ("Is the management company run as tightly as the Funds?",
             "A disciplined monthly close for the management company, with costs split correctly between Firm and Funds.",
             ["Management company close, A/P and payroll", "Firm vs. Fund cost allocation"]),
            ("What did the Firm really earn this year?",
             "Distributable earnings, fee-related earnings and ENI, reported consistently from integrated systems rather than Excel.",
             ["Monthly to annual reporting on DE, FRE and ENI"]),
            ("Which costs can we actually control?",
             "Budgets and forecasts by strategy that show where the Firm makes money and which costs are within its control.",
             ["Budgeting and forecasting by strategy", "Firm profitability and cost control"]),
            ("Does the Firm have the cash and capital it needs?",
             "Cash, owner distributions and Firm-level facilities planned together, not managed in isolation.",
             ["Treasury and owner distributions", "Firm-level debt facilities"]),
            ("Would we be ready for an SEC exam tomorrow?",
             "Documented processes, carry tracked by partner and Fund, and owner tax reporting overseen with your advisers.",
             ["SEC exam preparedness", "Carried interest tracking and reporting", "Oversight of owner tax reporting"]),
            ("Could we support a GP stake sale or a Firm-level raise?",
             "A corporate model that buyers and lenders can rely on, and finance leadership through the transaction.",
             ["Corporate model", "GP stake and capital transactions"]),
        ],
        "stats_head": "Back offices must scale, so more GPs outsource",
        "stats_sub": "Scale is hard to reach in-house, and more GPs are turning to flexible support.",
        "stats": [("22–30", "people per $1B of AUM at smaller GPs, against 9 at $5–10B Firms"),
                  ("39%", "of GPs rank hiring and keeping skilled people as their top three-year concern"),
                  ("51%", "of GPs plan to expand outsourcing to drive growth")],
        "sources": "Sources: McKinsey, How private equity is tackling operational complexity, 2018 (24 GPs; total staff, not back office only); CSC, Future Private Capital CFO 2025 (300 GPs globally; CSC provides fund services).",
        "results": [0, 1, 3, 4],
    },
    "pc": {
        "slug": "portfolio-company", "name": "Portfolio Company", "plural": "Portfolio Companies", "founder": "bart", "pc": True,
        "question": "Can my team deliver what our owner needs?",
        "lead": "Senior finance leadership and hands-on support for PE-backed companies, so the CFO and the team can meet the owner's expectations without waiting months to hire.",
        "motto": "We work for management, not around it.",
        "pains": [
            ("Stretched team", "Demands outstrip capacity; hiring takes months"),
            ("No single version of the truth", "Everyone has different numbers"),
            ("Value-creation plan hard to track", "KPIs are scattered and board packs built by hand"),
            ("Late surprises", "Weak cash forecasts; exit prep left late"),
        ],
        "grid": ["Month-end close · A/P and A/R",
                 "Financial reporting and consolidation · Board and owner reporting",
                 "FP&amp;A and business intelligence · KPI tracking against the plan",
                 "13-week cash, covenants, banking and insurance",
                 "Audit readiness · Controls and documentation · Tax oversight",
                 "Exit readiness and sell-side diligence · Add-on integration"],
        "themes": [
            ("Can I trust my numbers by day five?",
             "A faster, cleaner close built on reconciled accounts and well-run payables and receivables.",
             ["Month-end close", "A/P and expense management", "A/R and billing"]),
            ("Does everyone see the same numbers?",
             "One consolidated set of numbers for management, the board and the PE owner.",
             ["Financial reporting and multi-entity consolidation", "Board and owner reporting"]),
            ("Is the value-creation plan on track?",
             "Budgets, forecasts and KPI dashboards tied to the investment thesis, so progress is visible every month.",
             ["FP&amp;A", "Business intelligence", "KPI tracking against the plan"]),
            ("Will we hit the covenant next quarter?",
             "A rolling 13-week cash view and covenant headroom, so there are no surprises for you or your lenders.",
             ["13-week cash forecasting", "Covenant reporting", "Banking and insurance"]),
            ("Will the audit go smoothly, and are we on top of tax?",
             "Audit-ready accounts and documented controls, with tax risk managed alongside your advisers.",
             ["Audit readiness and support", "Controls and process documentation", "Tax oversight with your advisers"]),
            ("Are we ready if a buyer calls tomorrow?",
             "Diligence-ready numbers well before a sale, and a clean finance integration for every add-on.",
             ["Exit readiness and sell-side diligence", "Add-on integration"]),
        ],
        "stats_head": "Portfolio Companies cannot hire their way out",
        "stats_sub": "A senior finance hire is a six-figure commitment, before the rest of the team is built, and talent often leaves after the deal.",
        "stats": [("$604K", "average total cash for a US PE-backed CFO, up 5% on 2024"),
                  ("84%", "of PE and VC-backed CFOs report a shortage of finance professionals"),
                  ("~3x", "the rise in attrition seen at competitors, in the year after a PE acquisition")],
        "sources": "Sources: Heidrick &amp; Struggles PE-backed CFO Compensation Survey 2025 (n=213 US CFOs); Vardis PE CFO Report 2025; Revelio Labs, PE Investments Bring Talent Divestment, February 2025.",
        "results": [0, 1, 2, 3, 4],
    },
}
ORDER = ["fund", "firm", "pc"]


# ---------------------------------------------------------------- shared bits
def head(title, desc, base):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{base}img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;0,900;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}css/site.css">
</head>
<body>
<div class="draft">Staging draft for internal review. Not for distribution. Highlighted text needs input.</div>
"""


def nav(base, current=None):
    items = []
    for k in ORDER:
        L = LEVELS[k]
        cls = ' class="on"' if current == k else ""
        items.append(f'<li><a{cls} href="{base}{L["slug"]}/">{L["name"]}</a></li>')
    home_links = "" if current else ""
    return f"""<header class="nav">
  <div class="wrap">
    <a class="brand" href="{base or './'}"><img src="{base}img/xyz-logo.png" alt="">{BRAND}</a>
    <nav><ul>
      {''.join(items)}
      <li><a href="{base}#record">Track record</a></li>
      <li><a href="{base}#team">Team</a></li>
      <li><a class="btn primary sm" href="{base}#contact">{CTA}</a></li>
    </ul></nav>
  </div>
</header>
"""


def footer(base):
    links = "".join(f'<a href="{base}{LEVELS[k]["slug"]}/">{LEVELS[k]["name"]}</a>' for k in ORDER)
    return f"""<footer>
  <div class="wrap">
    <span>&copy; 2026 {BRAND} &middot; {TAGLINE}</span>
    <span class="links">{links}<a href="{base}#checklist">100-day checklist</a><a href="{base}#contact">Contact</a></span>
    <span style="flex-basis:100%">Information only. Not legal, tax or investment advice. <span class="tbd">[Legal notice: counsel to supply]</span></span>
  </div>
</footer>
"""


SCRIPT = """<script>
  function gateSubmit(e){ e.preventDefault(); var el=document.getElementById('gate-ok'); if(el) el.style.display='block'; return false; }
  function leadSubmit(e){ e.preventDefault(); document.getElementById('formnote').style.display='block'; return false; }
  // Preselect the level in the contact form when arriving from a level page (#contact?level=...)
  (function(){ var m=location.search.match(/level=([^&]+)/); if(!m) return; var s=document.getElementById('f-level'); if(!s) return;
    var v=decodeURIComponent(m[1]); for(var i=0;i<s.options.length;i++){ if(s.options[i].value===v){ s.selectedIndex=i; } } })();
</script>
</body>
</html>
"""


def tiles(founder, idxs=None, base=""):
    rows = RESULTS[founder]
    if idxs is not None:
        rows = [rows[i] for i in idxs]
    cls = " t" if founder == "bart" else ""
    cols = "g5" if len(rows) == 5 else "g4"
    out = [f'<div class="grid {cols}">']
    for k, v, p in rows:
        out.append(f'<div class="tile{cls}"><div class="k">{k}</div><div class="v">{v}</div><p>{p}</p></div>')
    out.append("</div>")
    return "\n".join(out)


def rec_head(founder, base, label):
    F = FOUNDERS[founder]
    return f'<div class="rec-h"><img src="{base}img/{F["img"]}" alt=""><div><b>{label}</b><br><span>{F["name"]}, Founding Partner</span></div></div>'


LEADERSHIP = "<b>Senior leadership across every theme:</b> from a fractional CFO, COO or controller to a full finance team, built around you."
ACROSS = "<b>Across every theme:</b> systems and ERP implementation &middot; tax delivered through trusted partners &middot; technology and AI, built on finance fundamentals"
FOUNDER_LED = "Every engagement is led by a founder, with our PE finance team in reporting, controls and FP&amp;A, and trusted partners for tax and valuation."
PROVIDERS = "<b>We work alongside your existing providers:</b> your administrator, auditors, tax preparers and lenders."


def spectrum(base):
    lv = " + ".join(f'<a class="lv" href="{base}{LEVELS[k]["slug"]}/">{LEVELS[k]["name"]}</a>' for k in ORDER)
    return f"""<div class="levels">At any level, or any combination: {lv}</div>
    <div class="steps5">
      <div class="st s1"><h3>Advisory</h3><p>Targeted consulting on a specific issue or review</p></div>
      <div class="st s2"><h3>Project</h3><p>Defined projects such as valuation, systems or controls documentation</p></div>
      <div class="st s3"><h3>Embedded support</h3><p>Fractional senior or specialist roles inside your team</p></div>
      <div class="st s4"><h3>Managed services</h3><p>We run functions such as reporting, FP&amp;A and close</p></div>
      <div class="st s5"><h3>Full team build</h3><p>We design it, hire it and run it until your team takes over</p></div>
    </div>
    <div class="axis"><span>Light touch</span><span>Full outsourced finance function</span></div>
    <div class="band wash">{PROVIDERS}</div>"""


def offer(base):
    return f"""<section class="offer" id="checklist">
  <div class="wrap">
    <div class="cover-mock">
      <img class="back" src="{base}img/checklist-page2.png" alt="">
      <img src="{base}img/checklist-cover.png" alt="Cover of The First 100 Days finance checklist">
    </div>
    <div>
      <div class="eyebrow" style="color:var(--teal-mid)">Free checklist</div>
      <h2>The First 100 Days: a finance checklist for PE-backed companies</h2>
      <p class="sub">What the PE owner will expect from finance after the deal closes, written by two former CFOs who have sat on both sides of the table.</p>
      <ul class="ticks" style="margin:20px 0 22px">
        <li>30+ actions across three phases, from funds flow to the 18-month roadmap</li>
        <li>Cash, covenants and the first board pack: what has to come first</li>
        <li>The red flags that tell a PE owner finance is falling behind</li>
      </ul>
      <form class="gate" onsubmit="return gateSubmit(event)">
        <input type="email" required placeholder="Work email" aria-label="Work email">
        <button class="btn primary" type="submit">Send me the checklist</button>
      </form>
      <p class="fine">Four pages, PDF. We'll send it to your inbox and the occasional note on PE finance. Unsubscribe anytime.</p>
      <div class="gate-ok" id="gate-ok">Thanks! <a href="{base}downloads/XYZ-100-Day-Finance-Checklist.pdf" target="_blank" rel="noopener">Download the checklist (PDF)</a><br><span style="font-size:13px;color:#C9D0DB">Draft site: the email isn't captured yet. This step needs the same form service as the contact form.</span></div>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- home page
def home():
    b = ""
    doors = []
    for k in ORDER:
        L = LEVELS[k]; F = FOUNDERS[L["founder"]]
        pains = "".join(f"<li><b>{t}:</b> {d[0].lower() + d[1:]}</li>" for t, d in L["pains"])
        cls = "" if L["pc"] else " navy"
        doors.append(f"""<a class="door{cls}" href="{L['slug']}/">
        <div class="lvl">{L['name']}</div>
        <h3>&ldquo;{L['question']}&rdquo;</h3>
        <ul>{pains}</ul>
        <div class="foot"><span>Led by {F['name']}</span><span class="more">How we help {L['plural']}</span></div>
      </a>""")

    hdr = "".join(
        f'<div class="th{" pc" if LEVELS[k]["pc"] else ""}"><a href="{LEVELS[k]["slug"]}/">{LEVELS[k]["name"]}</a>'
        + ("<small>We work for management, not around it</small>" if LEVELS[k]["pc"] else "") + "</div>"
        for k in ORDER)
    rows = []
    for i, t in enumerate(THEMES):
        rows.append(f'<div class="rh">{t}</div>' + "".join(
            f'<div class="cell" data-l="{LEVELS[k]["name"]}">{LEVELS[k]["grid"][i]}</div>' for k in ORDER))

    return head(f"{BRAND} | {TAGLINE}",
                "Senior finance leadership, when you need it, for the PE Fund, the PE Firm and the Portfolio Company. Founded by former PE Firm and Portfolio Company CFOs.", b) + nav(b) + f"""
<div class="hero" id="top">
  <div class="wrap">
    <div class="kicker">Finance leadership for private equity</div>
    <h1>Finance Expertise From <em>Both Sides of the Deal</em></h1>
    <p class="lead">A new type of firm offering senior finance leadership, when you need it, for the PE Fund, the PE Firm and the Portfolio Company.</p>
    <p class="founded">Founded by former PE Firm and Portfolio Company CFOs.</p>
    <div class="btns">
      <a class="btn primary" href="#contact">{CTA}</a>
      <a class="btn ghost" href="#who">Find your starting point</a>
    </div>
    <div class="proof">
      <div><b>50+ years</b><span>as senior finance leaders at PE Firms and PE-backed companies</span></div>
      <div><b>$75B+</b><span>AUM today at PE Firms where we built finance teams from scratch</span></div>
      <div><b>Fund, Firm and Portfolio</b><span>one team that knows how the numbers connect</span></div>
    </div>
  </div>
</div>

<div class="exp"><div class="wrap">
  <strong>FOUNDER EXPERIENCE</strong>
  <span>EIG</span><span>Roark Capital</span><span>The Vistria Group</span>
  <span>Portfolio companies of Oaktree, Apollo and Standard General</span>
  <span>Bain &amp; Company</span><span>PwC</span>
</div></div>

<!-- THREE DOORS -->
<section id="who">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Who we help</div>
      <h2>What's getting in the way, at every level</h2>
      <p class="sub">What we've seen from the inside. Pick the question closest to yours.</p>
    </div>
    <div class="grid g3">
      {''.join(doors)}
    </div>
    <div class="band">Across all three: the finance platform isn't built for where the business is going. The result is slower decisions, stretched teams and value left on the table.</div>
  </div>
</section>

<!-- BOTH SIDES -->
<section class="alt" id="why">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Why {BRAND.split()[0]}</div>
      <h2>Most outside support covers one side of PE. We were built to cover both.</h2>
    </div>
    <div class="vs">
      <div class="hd l">Where today's options fall short</div><div></div><div class="hd r">How we're different</div>
      <div class="l"><b>Only one side of PE:</b> most providers know the Fund or the Portfolio Company, not both</div><div class="ar">&rarr;</div>
      <div class="r"><b>Both-sides experience:</b> whichever level you hire us for, we know what the other side needs</div>
      <div class="l"><b>Fund and Firm out of step:</b> the interplay between Fund and Firm systems is often poorly understood</div><div class="ar">&rarr;</div>
      <div class="r"><b>Fund and Firm in step:</b> we have run both, and know how the systems and costs connect</div>
      <div class="l"><b>Hard to build alone:</b> senior PE finance talent is slow and costly to hire, and key-person risk remains</div><div class="ar">&rarr;</div>
      <div class="r"><b>Senior expertise, at the scale you need:</b> from targeted advice to a full finance function</div>
      <div class="l"><b>AI without the fundamentals:</b> sold as the fix, without the accounting, data and controls it depends on</div><div class="ar">&rarr;</div>
      <div class="r"><b>AI on solid foundations:</b> built on classical finance, not a substitute for it</div>
    </div>

    <div class="cycle">
      <h3>When we work on both sides: one connected cycle</h3>
      <p class="cap">Each engagement stands alone. Take both, and the numbers connect end to end.</p>
      <div class="flow">
        <div class="pc">Portfolio Company close</div>
        <div class="pc">KPIs, board pack and owner reporting</div>
        <div class="pe">Portfolio monitoring and valuations</div>
        <div class="pe">Fund and Firm reporting</div>
        <div class="pe">LP reporting and investor relations</div>
      </div>
      <div class="flow-key"><span>Portfolio Company</span><span class="pe">PE Fund and PE Firm</span><span style="font-style:italic">LP and owner requests flow back the other way</span></div>
      <div class="grid g3 pts">
        <div><h4>Set up for the PE owner</h4><p>Portfolio Company KPIs built in the owner's format from day one, so nothing is reworked at quarter-end.</p></div>
        <div><h4>One set of numbers</h4><p>The same figures run from the Portfolio Company ledger to the LP letter, with no re-keying.</p></div>
        <div><h4>Requests anticipated</h4><p>We know what the PE Firm will ask the Portfolio Company for, and the reverse.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- TRACK RECORD -->
<section id="record">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Track record</div>
      <h2>We've sat in your seat</h2>
      <p class="sub">Results across people, process and systems, on both sides of the PE relationship.</p>
    </div>
    {rec_head("pritpal", b, "Inside the PE Fund and Firm")}
    {tiles("pritpal")}
    <div class="rec-gap"></div>
    {rec_head("bart", b, "Inside the Portfolio Company")}
    {tiles("bart")}
  </div>
</section>

<!-- SERVICES -->
<section class="alt" id="services">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Our services</div>
      <h2>Six outcomes, at every level of PE</h2>
      <p class="sub">The same six themes run across the Fund, the Firm and the Portfolio Company. Choose a level for the detail.</p>
    </div>
    <div class="lead-line-top">{LEADERSHIP}</div>
    <div class="matrix">
      <div class="corner"></div>{hdr}
      {''.join(rows)}
    </div>
    <div class="band teal" style="margin-top:0">{ACROSS}</div>
  </div>
</section>

<!-- TECH AND AI -->
<section id="ai">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Technology and AI</div>
      <h2>Technology and AI, built on finance fundamentals</h2>
      <p class="sub">AI only works on top of sound accounting, clean data and strong controls.</p>
    </div>
    <div class="ai-grid">
      <table class="way">
        <thead><tr><th>Task</th><th>The usual way</th><th class="ours">Our way</th></tr></thead>
        <tbody>
          <tr><td>Month-end close<small>Portfolio Company</small></td><td>Manual reconciliations in spreadsheets</td><td>Automated reconciliations; we review the exceptions</td></tr>
          <tr><td>Portfolio KPIs<small>PE Fund</small></td><td>Emailed templates, re-keyed by hand</td><td>Direct data feeds, checked on arrival</td></tr>
          <tr><td>LP quarterly report<small>PE Fund</small></td><td>Built by hand each quarter</td><td>Drafted from connected data, every figure tied out and reviewed by us</td></tr>
          <tr><td>Firm reporting: DE, FRE, ENI<small>PE Firm</small></td><td>Pieced together from the GL and Excel</td><td>Built from integrated systems, with Firm and Fund costs split</td></tr>
          <tr><td>Board pack<small>Portfolio Company</small></td><td>Drafted from scratch each month</td><td>AI first draft, finance expert review</td></tr>
        </tbody>
      </table>
      <div class="found">
        <h3>The foundation</h3>
        <p>Classical finance and accounting expertise. We fix, redesign or remove processes first, then use AI to speed up what remains.</p>
        <p>Beyond finance, we help leadership decide where AI pays off across the business, with the business case, data and controls to back it.</p>
        <p>We work within your systems and security policies, alongside your auditors and valuation providers, never in place of them.</p>
      </div>
    </div>
  </div>
</section>

{offer(b)}

<!-- HOW WE ENGAGE -->
<section class="alt" id="how">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">How we engage</div>
      <h2>Come in anywhere along the spectrum</h2>
      <p class="sub">From targeted advice to a full finance function, at any level or combination, scaling as your needs change.</p>
    </div>
    {spectrum(b)}
  </div>
</section>

<!-- TEAM -->
<section id="team">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Founding partners</div>
      <h2>Senior finance leaders who have worked on both sides of the PE relationship</h2>
    </div>
    <div class="grid g2">
      <div class="person">
        <div class="top"><img src="img/pritpal.jpg" alt="Pritpal Aujla"><div><h3>Pritpal Aujla</h3><div class="role">Founding Partner<small>Leads PE Fund and Firm</small></div></div></div>
        <p>A 30-year career in finance, including 20 years as CFO / COO across multiple PE Firms that today manage $75B+, investing globally across sectors and the capital structure. Pritpal started his career as an auditor at PwC.</p>
        <div class="creds">EIG &middot; Roark Capital &middot; The Vistria Group &middot; US CPA and UK Chartered Certified Accountant &middot; Applied Sciences, University of Wolverhampton (UK)</div>
      </div>
      <div class="person">
        <div class="top"><img src="img/bart.jpg" alt="Bart Bruckert"><div><h3>Bart Bruckert</h3><div class="role">Founding Partner<small>Leads Portfolio Company</small></div></div></div>
        <p>A 20+ year career, including 10+ years as a PE-backed CFO or VP Finance / Ops and 8+ years in client service at Bain &amp; Co. and Accenture. Bart brings a deep technology background across ERP, CRM, BI and AI implementation.</p>
        <div class="creds">Portfolio companies of Oaktree, Apollo and Standard General &middot; MBA, Finance, University of Chicago &middot; BS, Computer Science, University of Notre Dame</div>
      </div>
    </div>
    <div class="band wash">{FOUNDER_LED}</div>
  </div>
</section>

<!-- FAQ -->
<section class="alt" id="faq">
  <div class="wrap">
    <div class="head center">
      <div class="eyebrow">Questions we hear</div>
      <h2>Before we talk</h2>
    </div>
    <div class="faq">
      <details open><summary>Are you there for management or for the PE owner?</summary>
        <p>Whoever engages us. At a Portfolio Company we work for management, not around it: we strengthen your team and help it deliver what the owner needs. Each engagement stands alone, with its own team, scope and data. <span class="tbd">[Partners to confirm conflict policy]</span></p></details>
      <details><summary>How is this different from a fund administrator?</summary>
        <p>An administrator processes and records. We lead: we own the reporting, the forecasts and the judgment calls a CFO makes, and we oversee your administrator so the handoffs work. We work alongside your administrator, auditors, tax preparers and lenders, never in place of them.</p></details>
      <details><summary>Are you just two people?</summary>
        <p>{FOUNDER_LED}</p></details>
      <details><summary>How quickly can you start?</summary>
        <p>Senior leaders are ready now. There's no executive search, so most engagements start within weeks of our first discussion, not months.</p></details>
      <details><summary>How do you charge?</summary>
        <p>Ongoing work is a fixed monthly fee. Projects are fixed or capped fees agreed up front. You pay for the capability you need, not a full-time team, and you can scale up or down as needs change.</p></details>
      <details><summary>How do you handle our data and use AI?</summary>
        <p>We work within your systems and security policies, alongside your auditors and valuation providers, never in place of them. We fix the process first, then use AI to speed up what remains, and a finance expert reviews everything that leaves our hands.</p></details>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="contact" id="contact">
  <div class="wrap cgrid">
    <div>
      <div class="rule"></div>
      <h2>Let's talk</h2>
      <p class="sub">The next step is a working session on your most pressing priority, with a founding partner.</p>
      <div class="cperson"><img src="img/pritpal.jpg" alt=""><div><b>Pritpal Aujla</b><span>PE Fund and Firm &middot; <span class="tbd">[email]</span></span></div></div>
      <div class="cperson"><img src="img/bart.jpg" alt=""><div><b>Bart Bruckert</b><span>Portfolio Company &middot; <span class="tbd">[email]</span></span></div></div>
      <div class="qs"><h4>Questions we'll ask you</h4><ul>
        <li>Which of these problems feels most urgent?</li>
        <li>What's working today, and where would you like more support?</li>
        <li>Where would support make the biggest difference: the Fund, the Firm or your Portfolio Companies?</li>
      </ul></div>
    </div>
    <form class="lead" onsubmit="return leadSubmit(event)">
      <div class="row">
        <div><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div>
        <div><label for="f-email">Work email</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
      </div>
      <div class="row">
        <div><label for="f-co">Firm or company</label><input id="f-co" name="company" autocomplete="organization"></div>
        <div><label for="f-level">Where do you need support?</label>
          <select id="f-level" name="level"><option value="fund">PE Fund</option><option value="firm">PE Firm</option><option value="pc">Portfolio Company</option><option value="multi">More than one</option><option value="other">Not sure yet</option></select></div>
      </div>
      <label for="f-msg">Your most pressing priority <span style="font-weight:400;color:var(--slate)">(optional)</span></label>
      <textarea id="f-msg" name="message" placeholder="e.g. LPs are asking for more detail and our quarter-end takes five weeks"></textarea>
      <button class="btn primary" type="submit">{CTA}</button>
      <p class="fine">A founding partner will reply within one business day. We never share your details.</p>
      <p class="formnote" id="formnote">Draft site: the form isn't connected yet. It needs a form service (for example HubSpot, Formspree or Microsoft Forms) before launch.</p>
    </form>
  </div>
</section>
""" + footer(b) + SCRIPT


# ---------------------------------------------------------------- level pages
def level_page(key):
    L = LEVELS[key]; F = FOUNDERS[L["founder"]]; b = "../"
    pains = "".join(f'<div class="pain"><h3>{t}</h3><p>{d}</p></div>' for t, d in L["pains"])
    themes = []
    for i, (q, desc, items) in enumerate(L["themes"]):
        lis = "".join(f"<li>{x}</li>" for x in items)
        themes.append(f'<div class="theme"><div class="n">{i+1:02d}</div><h3>{THEMES[i]}</h3><p class="q">&ldquo;{q}&rdquo;</p><p style="color:var(--slate);font-size:15.5px;margin-bottom:8px">{desc}</p><ul>{lis}</ul></div>')
    stats = "".join(f"<div class=\"stat\"><b>{v}</b><p>{t}</p></div>" for v, t in L["stats"])
    label = "Inside the PE Fund and Firm" if L["founder"] == "pritpal" else "Inside the Portfolio Company"
    others = "".join(
        f'<a class="other" href="{b}{LEVELS[k]["slug"]}/"><div class="lvl">{LEVELS[k]["name"]}</div><h3>&ldquo;{LEVELS[k]["question"]}&rdquo;</h3><p>Led by {FOUNDERS[LEVELS[k]["founder"]]["name"]} <span class="more">See how we help</span></p></a>'
        for k in ORDER if k != key)
    motto = f'<div class="motto">{L["motto"]}</div>' if L.get("motto") else ""
    connect = ("Own Portfolio Companies too? When we work on both sides, KPIs are built in your format from day one, and the same figures run from the Portfolio Company ledger to the LP letter with no re-keying."
               if not L["pc"] else
               "Each engagement stands alone. If your PE owner works with us too, we already know what they will ask for, so reporting is set up in their format from day one and nothing is reworked at quarter-end.")
    checklist = offer(b) if L["pc"] else ""

    return head(f"{L['name']} | {BRAND}", L["lead"], b) + nav(b, key) + f"""
<div class="hero page">
  <div class="wrap">
    <div class="crumb"><a href="{b}">Home</a> &nbsp;/&nbsp; {L['name']}</div>
    <div class="kicker">For the {L['name']}</div>
    <h1>&ldquo;{L['question']}&rdquo;</h1>
    {motto}
    <p class="lead">{L['lead']}</p>
    <div class="btns">
      <a class="btn primary" href="{b}?level={key}#contact">{CTA}</a>
      <a class="btn ghost" href="#themes">See what we do</a>
    </div>
    <div class="leader"><img src="{b}img/{F['img']}" alt="{F['name']}"><div><b>Led by {F['name']}</b>Founding Partner &middot; {F['short']}</div></div>
  </div>
</div>

<section class="tight">
  <div class="wrap">
    <div class="head" style="margin-bottom:30px">
      <div class="eyebrow">What's getting in the way</div>
      <h2>What we've seen from the inside</h2>
    </div>
    <div class="pains">{pains}</div>
  </div>
</section>

<section class="alt" id="themes">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">How we help</div>
      <h2>Six questions every {L['name']} asks, and how we answer them</h2>
    </div>
    <div class="lead-line-top" style="margin-bottom:22px">{LEADERSHIP}</div>
    <div class="themes">{''.join(themes)}</div>
    <div class="band teal">{ACROSS}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Why it matters now</div>
      <h2>{L['stats_head']}</h2>
      <p class="sub">{L['stats_sub']}</p>
    </div>
    <div class="stats3">{stats}</div>
    <p class="src">{L['sources']}</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Track record</div>
      <h2>We've sat in your seat</h2>
    </div>
    {rec_head(L['founder'], b, label)}
    {tiles(L['founder'], L['results'], b)}
    <div class="band wash" style="margin-top:30px">{connect}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">How we engage</div>
      <h2>Start where it suits you, and scale as needs change</h2>
    </div>
    {spectrum(b)}
  </div>
</section>

{checklist}

<div class="cta-band">
  <div class="wrap">
    <div><h2>Your most pressing priority, in one working session</h2><p>Talk it through with {F['name']} and see where we can help.</p></div>
    <a class="btn" href="{b}?level={key}#contact">{CTA}</a>
  </div>
</div>

<section class="tight">
  <div class="wrap">
    <div class="head" style="margin-bottom:24px"><div class="eyebrow">Other levels</div><h2 style="font-size:26px">We work on both sides of the deal</h2></div>
    <div class="others">{others}</div>
  </div>
</section>
""" + footer(b) + SCRIPT


if __name__ == "__main__":
    (ROOT / "index.html").write_text(home())
    for k in ORDER:
        d = ROOT / LEVELS[k]["slug"]; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(level_page(k))
    print("built: index.html,", ", ".join(LEVELS[k]["slug"] + "/index.html" for k in ORDER))
