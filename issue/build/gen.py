import html, json
L="color:#1f5c99;text-decoration:underline;"
SANS="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
SER="Georgia,'Times New Roman',serif"
LBL=f"font-family:{SANS};font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#4f7a52;font-weight:bold;margin:0 0 10px 0;"
P=f"font-family:{SANS};font-size:16px;line-height:1.6;color:#2b2420;margin:0 0 12px 0;"
META=f"font-family:{SANS};font-size:13px;line-height:1.5;color:#6b5d52;margin:0 0 10px 0;"
H3=f"font-family:{SER};font-size:19px;line-height:1.35;color:#2b2420;margin:0 0 6px 0;font-weight:bold;"
G="color:#4f7a52;font-weight:bold;"
def a(t,u): return f'<a href="{u}" style="{L}">{html.escape(t)}</a>'
def card(inner,bg="#ffffff",extra=""):
    return f'<tr><td style="padding:0 0 20px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{bg};border-radius:6px;{extra}"><tr><td style="padding:24px 24px 14px 24px;">{inner}</td></tr></table></td></tr>'
DIV='<div style="border-top:1px solid #eadfd2;margin:16px 0;"></div>'

big = (f'<p style="{LBL}">The big sip</p>'
 f'<h2 style="font-family:{SER};font-size:23px;line-height:1.3;color:#2b2420;margin:0 0 6px 0;">{a("RBI tightens cyber oversight of non-bank payment system operators","https://www.business-standard.com/industry/banking/rbi-consolidates-cyber-security-rules-for-non-bank-payment-system-operators-126110502060_1.html")}</h2>'
 f'<p style="{META}">Business Standard · 5 November 2026</p>'
 f'<p style="{P}"><strong style="{G}">What happened:</strong> On 5 November, RBI issued consolidated Master Directions on Cyber Resilience and Digital Payment Security Controls for non-bank payment system operators, including NPCI, card networks, payment aggregators and wallet issuers. Large and medium operators must comply now; small ones have until 1 April 2028. Operators must get source code for critical third-party apps or use escrow, report incidents within six hours, and apply a 12-hour cooling-off after a customer changes a registered mobile number or email.</p>'
 f'<p style="{P}"><strong style="{G}">Why it matters:</strong> Rules like these land directly in the product: onboarding, account recovery, vendor choice and release cadence. One rulebook replacing six older circulars also makes compliance easier to reason about.</p>'
 f'<p style="{P}"><strong style="{G}">If you were the PM:</strong> Map every flow that touches a number or email change, and decide how to explain the 12-hour wait so it feels like protection. List your critical vendor apps and check the source-code position for each, since that shapes your release process. Then ask what six-hour incident reporting looks like at 2 am.</p>')

sips=[
("Retail &amp; E-commerce","Beauty Brands Go Quick Commerce-First","https://inc42.com/features/beauty-brands-go-quick-commerce-first/","Inc42 · 10 November 2026",
 "Redseer puts beauty sales on India's quick commerce apps at about $1 billion in annualised GMV, growing about 90% a year.",
 "a report cited by Inc42 says generic makeup searches rose 236% on Blinkit and fell 76% on Amazon, so find where your customers now search."),
("Pharma &amp; Life Sciences","FDA approves novel Bayer drug to reduce recurrence of stroke","https://www.statnews.com/2026/11/09/cardiovascular-stroke-recurrence-bayer-drug-fda-approval/","STAT · 9 November 2026",
 "The FDA approved Bayer's Sunharbo, the first of a new drug class, after a trial where 6.2% of patients had a second stroke versus 8.4% on placebo.",
 "53 patients need a year of treatment to prevent one stroke; \"number needed to treat\" is how doctors and payers judge value."),
("Health Sciences &amp; MedTech","The Big Challenge for AI in Healthcare Comes After Approval","https://medcitynews.com/2026/11/the-big-challenge-for-ai-in-healthcare-comes-after-approval/","MedCity News (contributor piece) · 6 November 2026",
 "The author notes roughly 1,450 FDA-authorised AI devices and cites an eye-screening system that gave no result for a quarter of patients because of camera quality and pupil size.",
 "plan post-launch monitoring and change control before launch day."),
("Telecom &amp; Connectivity","Can Jio's stock market debut reset India's telecom pricing?","https://www.lightreading.com/finance/can-jio-s-stock-market-debut-reset-india-s-telecom-pricing-","Light Reading · 30 October 2026",
 "Jio Platforms' $3.2 billion IPO is called India's largest, and media reports say Nomura expects a possible 15% tariff hike in November–December 2026.",
 "after its July 2024 price rise Jio lost around 12.74 million subscribers in three months; every tariff call trades ARPU against churn."),
("Fintech &amp; Banking","ChatGPT's new Wallet lets AI agents shop and check out for you","https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/","TechCrunch · 13 November 2026",
 "OpenAI launched a wallet that lets ChatGPT's shopping agents complete purchases, starting with some US ChatGPT Pro subscribers.",
 "note the trust design: a review screen, Face ID-style approval, and payment tokens that keep card details from the agent and merchant."),
("B2B SaaS &amp; Enterprise","Adobe brings AI agents and new creative tools to Photoshop, Premiere, and Firefly","https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/","TechCrunch · 10 November 2026",
 "At its MAX event, Adobe announced an MCP server that lets chatbots such as ChatGPT, Claude or Gemini use Adobe features.",
 "letting outside assistants call your features buys distribution but loosens control of the experience."),
]
rows=[]
for i,(ind,t,u,m,w,f) in enumerate(sips):
    rows.append(f'<p style="font-family:{SANS};font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#4f7a52;font-weight:bold;margin:0 0 4px 0;">{ind}</p>'
      f'<h3 style="{H3}font-size:17px;">{a(t,u)}</h3><p style="{META}margin-bottom:6px;">{m}</p>'
      f'<p style="{P}margin-bottom:6px;">{html.escape(w)}</p><p style="{P}"><strong style="{G}">For PMs:</strong> {html.escape(f)}</p>')
sipsh=f'<p style="{LBL}">Quick sips from six industries</p>'+DIV.join(rows)

books=[
("I thought bank statements were a Formatting Problem. Then I found out whose loan was riding on one","https://www.mindtheproduct.com/i-thought-bank-statements-were-a-formatting-problem-then-i-found-out-whose-loan-was-riding-on-one/","Amey Farde, Mind the Product · 3 November 2026",
 "Farde, a Staff PM at Intuit, shows how a messy transaction description on a bank statement can sway a small business's loan decision. His team replaced a brittle rulebook with an LLM paired with an embedding model, and underwriters preferred the new descriptions in more than half the cases where outputs disagreed.",
 "pick a \"cosmetic\" bug in a product you use and trace it forward to the real decision it affects."),
("How is AI changing the traditional SaaS and business app model?","https://www.mindtheproduct.com/how-is-ai-changing-the-traditional-saa-s-and-business-app-model/","Lucy Pitticas-Rothwell, Mind the Product · 29 October 2026",
 "She splits a business app into front-end, data and logic layers and sets out five responses to AI, from adding chat inside the app to rebuilding AI-first. A two-axis grid then weighs back-end and data moats against front-end moats such as loyalty and ease of use.",
 "place one work app you use daily on her grid and choose which of the five options you would back."),
]
bk=[]
for t,u,m,d,tr in books:
    bk.append(f'<h3 style="{H3}font-size:17px;">{a(t,u)}</h3><p style="{META}margin-bottom:6px;">{m}</p><p style="{P}margin-bottom:6px;">{html.escape(d)}</p><p style="{P}"><strong style="{G}">Try this:</strong> {html.escape(tr)}</p>')
booksh=f'<p style="{LBL}">From the PM bookshelf</p>'+DIV.join(bk)

fw=(f'<p style="{LBL}">Framework of the fortnight</p><h3 style="{H3}">Kano model, applied to ChatGPT\'s Wallet</h3>'
 f'<p style="{P}">Kano sorts features into basics users expect, performance features where more is better, and delighters nobody asked for. In ChatGPT\'s Wallet, an agent that buys for you is the delighter. The review screen, biometric approval and payment token are basics: nobody praises them, but one failure breaks trust. OpenAI plans spending limits and category controls later. Kano suggests those will soon be basics too, so they deserve priority over more delight. '
 f'{a("Explore Kano and the other frameworks","https://dineshsmile-commits.github.io/PM-Field-guide/#frameworks")}.</p>')

chew=(f'<p style="{LBL}">Something to chew on</p>'
 f'<p style="{P}font-family:{SER};font-size:18px;"><em>"You are the PM for a payment app. RBI\'s rules require a 12-hour cooling-off period after a user changes their registered mobile number or email. How would you implement it without losing users?"</em></p>'
 f'<p style="{P}margin-bottom:6px;">A strong answer covers:</p>'
 f'<ul style="{P}padding-left:20px;margin-top:0;">'
 '<li style="margin-bottom:6px;">The user and the risk: who changes numbers, and how the wait blocks account takeover.</li>'
 '<li style="margin-bottom:6px;">The experience: warn before the change, show a countdown, and say what still works during the wait.</li>'
 '<li style="margin-bottom:6px;">The metrics: drop-off and support tickets against fraud losses, with edge cases checked with compliance.</li></ul>')

pour=(f'<p style="{LBL}">Pour yourself a cup</p>'
 f'<p style="{P}">Welcome to Product Over Chai. This fortnight kept circling one idea: trust. RBI rewrote the security rules for payment apps, an AI assistant started paying on people\'s behalf, and a health writer reminded us that medical AI\'s hard part begins after approval. Inside: one big story, six quick sips, two reads and an interview question.</p>'
 f'<p style="{P}font-style:italic;">Team PM Field Guide</p>')

last=(f'<p style="{LBL}">Last sip</p><p style="{P}">Payment rules, shopping agents and medical AI all said the same thing this fortnight: people trust products that plan for what can go wrong.</p>'
 f'<p style="{P}">Hit reply and tell us what you would like us to cover next.</p>')

mast=(f'<tr><td style="background:#3b2416;border-radius:6px 6px 0 0;padding:28px 24px 24px 24px;text-align:left;">'
 f'<p style="font-family:{SER};font-size:30px;line-height:1.2;color:#fbf6ee;margin:0 0 8px 0;font-weight:bold;">☕ Product Over Chai</p>'
 f'<p style="font-family:{SANS};font-size:14px;line-height:1.5;color:#fbf6ee;margin:0 0 4px 0;">A fortnightly 5-minute read for aspiring PMs · Test issue · 13 November 2026</p>'
 f'<p style="font-family:{SANS};font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:#e6d6c2;margin:0;">by PM Field Guide</p></td></tr>'
 '<tr><td style="height:20px;line-height:20px;font-size:0;">&nbsp;</td></tr>')

foot=(f'<tr><td style="padding:8px 8px 24px 8px;text-align:center;">'
 f'<p style="{META}">Explore the frameworks and industry briefs at PM Field Guide: {a("https://dineshsmile-commits.github.io/PM-Field-guide/","https://dineshsmile-commits.github.io/PM-Field-guide/")}</p>'
 f'<p style="{META}">You\'re receiving Product Over Chai because you registered at PM Field Guide. Reply \'unsubscribe\' to stop.</p>'
 f'<p style="{META}">Every story links to its original source. Summaries are ours.</p></td></tr>')

preview='RBI rewrites payment security rules, ChatGPT gets a wallet, and beauty goes quick commerce-first.'
body=(f'<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{preview}</div>'
 f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f4ece1;"><tr><td align="center" style="padding:24px 12px;">'
 f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;">'
 + mast + card(pour) + card(big,"#eef3ec") + card(sipsh) + card(booksh) + card(fw) + card(chew,"#ffffff","border-left:4px solid #4f7a52;") + card(last) + foot +
 '</table></td></tr></table>')
title="Product Over Chai, Test issue, 13 November 2026"
frag=(f'<title>{title}</title>\n<style>body{{background:#f4ece1;margin:0;}}</style>\n'+body)
open('../issue_test_artifact.html','w').write(frag)
full=(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title></head>'
 f'<body style="margin:0;padding:0;background:#f4ece1;">{body}</body></html>')
open('../issue.html','w').write(full)
