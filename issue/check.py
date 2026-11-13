import json, sys, datetime
from urllib.parse import urlparse
from pathlib import Path
base = Path(__file__).resolve().parent
allow = json.loads((base/"allowlist.json").read_text())
cands = json.loads((base/"candidates.json").read_text())
today = datetime.date.today()
earliest = today - datetime.timedelta(days=15)
seen = set(); out = []
for c in cands:
    r = []
    sec = c.get("section"); key = "craft" if sec == "craft" else c.get("industry")
    url = c.get("url") or ""
    p = urlparse(url)
    host = (p.hostname or "").lower()
    doms = allow.get(key)
    if p.scheme != "https": r.append("not https")
    if not doms: r.append(f"unknown section/industry: {key}")
    elif not any(host == d or host.endswith("." + d) for d in doms): r.append(f"host {host} not allowed for {key}")
    try:
        d = datetime.date.fromisoformat(c.get("published",""))
        if d > today: r.append("date in future")
        elif d < earliest: r.append(f"date {d} older than {earliest}")
    except Exception: r.append("bad date")
    for f in ("title","url","summary","takeaway"):
        if not str(c.get(f) or "").strip(): r.append(f"empty {f}")
    if url in seen: r.append("duplicate url")
    seen.add(url)
    out.append({**c, "pass": not r, "reasons": r})
(base/"checked.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(f"{sum(o['pass'] for o in out)} passed, {sum(not o['pass'] for o in out)} failed of {len(out)}")
sys.exit(0)
