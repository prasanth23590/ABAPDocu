#!/usr/bin/env python3
"""Convert the HTML cache written by tools/fetch.py into the markdown tree.

Step 2 of 2.

    python3 -I tools/convert.py CACHE_DIR OUT_DIR

Layout of OUT_DIR (one markdown file per topic):

    <section>/<file>.md                   section landing pages and their own topics
    <section>/<subsection>/<file>.md      everything below a section
    INDEX.md                              table of contents, three levels deep
    manifest.json                         topic file -> path, title, TOC position

Cross references between topics are rewritten to relative .md links.
Needs: pandoc, beautifulsoup4.
"""
import concurrent.futures as cf
import json
import os
import posixpath
import re
import subprocess
import sys

from bs4 import BeautifulSoup

SOURCE = "https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation"


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60].strip("-") or "topic"


def flatten(nodes, path, out):
    for n in nodes:
        out.append({"title": n.get("t") or "", "file": n.get("u"), "path": path,
                    "has_children": bool(n.get("c"))})
        flatten(n.get("c", []), path + [n.get("t") or ""], out)


def location(entry):
    """Directory (relative to OUT_DIR) a topic lives in."""
    p = [slug(a) for a in entry["path"][1:3]]      # ancestors below the root, two levels
    depth = len(entry["path"])
    if depth == 1 or (depth == 2 and entry["has_children"]):   # sections get their own folder
        p.append(slug(entry["title"]))
    return "/".join(p)


def clean_html(raw):
    soup = BeautifulSoup(raw, "html.parser")
    root = soup.find("main") or soup.body or soup
    for pre in root.find_all("pre"):
        code = pre.find("code")
        if code is None:
            code = soup.new_tag("code")
            code.string = pre.get_text()
            pre.clear()
            pre.append(code)
        code.string = code.get_text().replace("\r", "").rstrip("\n")
        code["class"] = ["language-abap"]
    for t in root.find_all(["script", "style"]):
        t.decompose()
    for t in root.find_all(["div", "span", "article", "section", "main", "figure"]):
        t.unwrap()
    for t in root.find_all(True):                  # attributes only get in the way of gfm
        keep = {k: v for k, v in t.attrs.items()
                if k in ("href", "src", "colspan", "rowspan")
                or (t.name == "img" and k == "alt")
                or (t.name == "code" and k == "class")}
        t.attrs = keep
    return root.decode_contents()


def pandoc(html):
    r = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=html.encode(), capture_output=True, check=True)
    return r.stdout.decode()


LINK = re.compile(r"(?<!\!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)")


def main():
    cache, out = sys.argv[1], sys.argv[2]
    toc = json.load(open(os.path.join(cache, "toc.json")))
    entries = []
    flatten(toc["toc"], [], entries)

    where, manifest = {}, {}
    for e in entries:
        f = e["file"]
        if not f or f in where:
            continue
        d = location(e)
        where[f] = posixpath.join(d, re.sub(r"\.html?$", ".md", f))
        manifest[f] = {"md": where[f], "title": e["title"], "toc_path": e["path"]}
    lower = {}
    for f, p in where.items():
        lower.setdefault(p.lower(), []).append(f)
    clashes = {k: v for k, v in lower.items() if len(v) > 1}
    if clashes:
        raise SystemExit(f"case-insensitive path clashes: {list(clashes.items())[:5]}")

    by_lower = {f.lower(): p for f, p in where.items()}    # some source links differ in case
    stats = {"unmapped_links": 0, "links": 0}

    def render(f):
        raw = open(os.path.join(cache, "html", f), encoding="utf-8").read()
        body = pandoc(clean_html(raw))
        here = posixpath.dirname(where[f])

        def fix(m):
            text, target = m.group(1), m.group(2)
            if re.match(r"[a-z][a-z0-9+.-]*:", target, re.I):
                return m.group(0)                      # external URL
            base, _, frag = target.partition("#")
            stats["links"] += 1
            if base == "" and frag:
                return m.group(0)                      # in-page anchor
            dest = where.get(base) or by_lower.get(base.lower())
            if dest is None:
                stats["unmapped_links"] += 1
                return text                            # not part of this deliverable
            rel = posixpath.relpath(dest, here)
            return f"[{text}]({rel}{'#' + frag if frag else ''})"

        body = LINK.sub(fix, body)
        info = manifest[f]
        head = ["---", f"title: {json.dumps(info['title'], ensure_ascii=False)}",
                f"source_file: {f}",
                "section: " + json.dumps(" > ".join(info["toc_path"][1:]) or info["title"],
                                         ensure_ascii=False),
                f"source: {SOURCE}", "---", ""]
        path = os.path.join(out, where[f])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(head) + body.rstrip() + "\n")

    missing = [f for f in where if not os.path.exists(os.path.join(cache, "html", f))]
    if missing:
        print(f"WARNING: {len(missing)} topics not in cache, skipped", file=sys.stderr)
    todo = [f for f in where if f not in set(missing)]
    with cf.ThreadPoolExecutor(8) as ex:
        list(ex.map(render, todo))

    # INDEX.md: the table of contents, three levels deep
    lines = [f"# {toc['deliverable']['title']} – index", "",
             "Generated from the SAP Help Portal table of contents. Three levels are shown; "
             "each section page lists its own topics.", ""]
    seen = set()
    for e in entries:
        depth = len(e["path"])
        if depth > 3 or not e["file"] or e["file"] in seen or e["file"] not in where:
            continue
        seen.add(e["file"])
        rel = where[e["file"]]
        lines.append(f"{'  ' * max(depth - 1, 0)}- [{e['title']}]({rel})")
    with open(os.path.join(out, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=0, sort_keys=True)
    print(f"wrote {len(todo)} topics; links {stats['links']}, "
          f"unmapped (de-linked) {stats['unmapped_links']}")


if __name__ == "__main__":
    main()
