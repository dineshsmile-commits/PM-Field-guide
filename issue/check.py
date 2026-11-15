import json, sys, datetime
from urllib.parse import urlparse
from pathlib import Path
base = Path(__file__).resolve().parent
cands = json.loads((base/"candidates.json").read_text())
allow = json.loads((base/"allowlist.json").read_text())
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).date()
earliest = today - datetime.timedelta(days=14)
seen = {}
out = []
for c in cands:
    r = []
    sec = c.get("section")
    key = "craft" if sec == "craft" else c.get("industry")
    url = c.get("url") or ""
    p = urlparse(url)
    host = (p.hostname or "").lower()
    doms = allow.get(key or "", [])
    if p.scheme != "https":
        r.append("url not https")
    if not doms:
        r.append(f"unknown section/industry: {key}")
    elif not any(host == d or host.endswith("." + d) for d in doms):
        r.append(f"host {host} not in allowlist for {key}")
    try:
        d = datetime.date.fromisoformat(c.get("published", ""))
        if d > today: r.append("published in future")
        elif d < earliest: r.append(f"published {d} older than 15-day window")
    except Exception:
        r.append("published not a valid date")
    for f in ("title", "url", "summary", "takeaway"):
        if not str(c.get(f) or "").strip():
            r.append(f"empty {f}")
    if url and url in seen:
        r.append(f"duplicate url (also {seen[url]})")
    seen.setdefault(url, c.get("id"))
    out.append({**c, "pass": not r, "reasons": r})
(base/"checked.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
n = sum(o["pass"] for o in out)
print(f"{n} passed, {len(out)-n} failed, {len(out)} total (window {earliest}..{today})")
sys.exit(0)
