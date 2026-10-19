#!/usr/bin/env python3
"""Download the ABAP Keyword Documentation (ABAP Cloud) from SAP Help Portal.

Step 1 of 2. Saves the table of contents (toc.json) and the raw HTML of every
topic (html/<file>.html) into a cache directory. tools/convert.py turns the
cache into the markdown tree under docs/.

    python3 tools/fetch.py CACHE_DIR [--workers 8]

Re-running skips topics that are already cached.
"""
import argparse
import concurrent.futures as cf
import json
import os
import sys
import time
import urllib.parse
import urllib.request

BASE = "https://help.sap.com/http.svc"
PRODUCT = "abap-cloud"
DELIVERABLE = "abap-keyword-documentation"


def get_json(url, tries=6):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "abapdocu-export/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # network hiccup, 5xx, truncated body
            if attempt == tries - 1:
                raise
            time.sleep(2 ** attempt)


def walk(nodes, path, out):
    for n in nodes:
        out.append({"title": n.get("t"), "file": n.get("u"), "path": path})
        walk(n.get("c", []), path + [n.get("t")], out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cache")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    html_dir = os.path.join(args.cache, "html")
    os.makedirs(html_dir, exist_ok=True)

    meta = get_json(f"{BASE}/deliverableMetadata?" + urllib.parse.urlencode({
        "deliverable_url": DELIVERABLE, "product_url": PRODUCT,
        "version": "LATEST", "language": "en-US"}))["data"]
    deliv = meta["deliverable"]
    did, build = deliv["id"], deliv["buildNo"]

    def page_url(f, info=0):
        return f"{BASE}/pagecontent?" + urllib.parse.urlencode({
            "deliverableInfo": info, "deliverable_id": did,
            "file_path": f, "buildNo": build})

    # One request with deliverableInfo=1 carries the full table of contents.
    first = get_json(page_url("abenabap.html", info=1))["data"]
    toc = first["deliverable"]["fullToc"]
    entries = []
    walk(toc, [], entries)
    with open(os.path.join(args.cache, "toc.json"), "w") as f:
        json.dump({"deliverable": {k: first["deliverable"][k] for k in
                                   ("title", "shortdesc", "version", "languageCode")},
                   "deliverable_id": did, "build": build, "toc": toc}, f)

    files = list(dict.fromkeys(e["file"] for e in entries if e["file"]))
    todo = [f for f in files if not os.path.exists(os.path.join(html_dir, f))]
    print(f"{len(entries)} toc entries, {len(files)} unique files, {len(todo)} to download",
          flush=True)

    failed = []

    def grab(f):
        d = get_json(page_url(f))["data"]
        cur = d["currentPage"]["u"]
        if cur != f:  # server fell back to the landing page: topic not found
            raise RuntimeError(f"fell back to {cur}")
        tmp = os.path.join(html_dir, f + ".part")
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(d["body"])
        os.replace(tmp, os.path.join(html_dir, f))

    done = 0
    with cf.ThreadPoolExecutor(args.workers) as ex:
        futs = {ex.submit(grab, f): f for f in todo}
        for fut in cf.as_completed(futs):
            f = futs[fut]
            done += 1
            try:
                fut.result()
            except Exception as e:
                failed.append((f, str(e)))
            if done % 250 == 0:
                print(f"  {done}/{len(todo)} (failed so far: {len(failed)})", flush=True)

    with open(os.path.join(args.cache, "failed.json"), "w") as fh:
        json.dump(failed, fh, indent=1)
    print(f"done; {len(failed)} failed", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
