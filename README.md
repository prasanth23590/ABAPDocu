# ABAP Keyword Documentation (ABAP Cloud) as Markdown

An offline, searchable, diff-able copy of SAP's **ABAP Keyword Documentation for ABAP Cloud**, converted from the
[SAP Help Portal](https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation)
into plain Markdown, one file per topic.

|                         |                                                                 |
| ----------------------- | --------------------------------------------------------------- |
| Topics                  | 4,963 Markdown files (about 34 MB)                              |
| Language                | English (`en-US`)                                               |
| Edition                 | `latest` as published on SAP Help Portal on 2026-10-19          |
| Scope                   | ABAP Cloud / language version *ABAP for Cloud Development*      |
| Cross references        | ~60,000 links between topics, rewritten to relative `.md` links |

> **Copyright.** The documentation text is © SAP SE and its affiliates. This repository only mirrors it in
> a different format for convenient reading and searching. Check SAP's terms of use for the Help Portal
> before redistributing it. Only the scripts in `tools/` are original work.

## What this documentation covers

It describes the syntax and semantics of the programming languages SAP provides on an Application Server ABAP,
**restricted to what is allowed in ABAP Cloud**. That is a subset of classic ABAP: obsolete and
non-released statements are not part of the *ABAP for Cloud Development* language version.

## Where to find things

Start at [`docs/INDEX.md`](docs/INDEX.md), a three-level table of contents, or go straight to a section:

| Folder under `docs/` | Topics | What is in it |
| --- | ---: | --- |
| [`abap-programming-language/`](docs/abap-programming-language) | 1,666 | **The ABAP language itself**: syntax elements, program structure, ABAP Objects, data types and data objects, built-in functions and constructor expressions, operands, declarations, calling and exiting program units, program flow logic (`IF`, `LOOP`, `CASE`, exceptions), internal tables and strings, **ABAP SQL** (`SELECT`, `INSERT`, `UPDATE`, `MODIFY`, `DELETE`), data clusters, data interchange formats (XML/JSON, Simple Transformations), text repositories, language environment, enhancements, authorizations, security notes, and the list of obsolete language elements. |
| [`abap-core-data-services-abap-cds/`](docs/abap-core-data-services-abap-cds) | 1,316 | **ABAP CDS**: CDS DDL (data definitions, views, view entities, projections, associations, expressions, built-in functions), CDS DCL (access control), annotations (one page per annotation), service definitions, data types, null values, tuning objects and system entities. |
| [`abap-rap-business-objects/`](docs/abap-rap-business-objects) | 384 | **RAP (ABAP RESTful Application Programming Model)**: business services, behavior definitions (BDL), and ABAP EML (`MODIFY ENTITIES`, `READ ENTITIES`, `COMMIT ENTITIES`) for providing and consuming RAP business objects. |
| [`abap-dictionary-ddic/`](docs/abap-dictionary-ddic) | 97 | **ABAP Dictionary**: data elements, structures, table types, database tables, tuning objects, built-in dictionary types and functions, activation, and the dictionary objects available for cloud development. |
| [`abap-apis/`](docs/abap-apis) | 15 | **Language versions and released APIs**: release contracts and the rules for building robust programs on released APIs. |
| [`abap-release-news/`](docs/abap-release-news) | 57 | **What is new per ABAP release**: 7.6x, 7.7x, 7.8x, 7.9x, 9.1x and 9.2x. |
| [`abap-glossary/`](docs/abap-glossary) | 1,425 | **Glossary**: ABAP terms and the domain glossaries (technology, DDIC, CDS, language, RAP, ABAP SQL). Most links in the other sections point here. |
| [`abap-syntax-conventions/`](docs/abap-syntax-conventions) | 1 | How to read the syntax notation (`[ ]`, `\|`, `{ }`, `...`). |
| [`abap-cloud-documentation-landscape/`](docs/abap-cloud-documentation-landscape) | 1 | Overview of the ABAP Cloud documentation set. |
| [`docs/abenabap.md`](docs/abenabap.md) | 1 | The landing page of the whole documentation. |

Quick starts:

- `SELECT`: [`docs/abap-programming-language/abap-database-access/abapselect.md`](docs/abap-programming-language/abap-database-access/abapselect.md)
- CDS view entities and RAP behavior definitions live in the CDS and RAP folders above.
- To look up a keyword, search for its topic name, for example `grep -ril "LOOP AT" docs`, or use the file-name
  convention below.

## How the files are organised

```
docs/
├── INDEX.md                  table of contents (3 levels)
├── manifest.json             source file -> repo path, title, position in the SAP table of contents
├── abenabap.md               documentation landing page
└── <section>/                one folder per top-level section (see table above)
    ├── <topic>.md            the section's own landing page and topics
    └── <subsection>/         e.g. abap-database-access/, abap-cds-annotations/ ...
        └── <topic>.md
```

- **File names are SAP's own topic ids.** SAP names them `abap<keyword>.html` (statements, for example `abapselect`)
  and `aben<topic>.html` (concepts and glossary terms), and the files keep that name with an `.md` extension.
  If you know the id from a Help Portal URL or a link, it is the file name.
- **Folders follow the SAP table of contents** to two levels below the root; deeper topics sit next to their
  parent's siblings in the subsection folder.
- **Every file starts with front matter** recording its origin:

  ```yaml
  ---
  title: "SELECT"
  source_file: abapselect.html
  section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL"
  source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
  ---
  ```

- **Code** is in fenced ```` ```abap ```` blocks. **Links** between topics are relative `.md` links, so
  they work on GitHub and in any Markdown viewer.

## Known limitations of the conversion

- This is an automated HTML-to-Markdown conversion. Wording is unchanged, but layout details (colour, italic
  syntax-diagram markup, collapsible sections, some figures) are simplified. The Help Portal remains the
  authoritative, fully formatted version.
- Complex tables are kept as HTML tables inside the Markdown, because GitHub-flavoured Markdown cannot express them.
- About 85 links (out of ~60,000) point to material outside this deliverable and are kept as plain text. About 40 links
  whose text contains unbalanced square brackets, such as `[CONVERT KEY OF bdef`, were not rewritten
  and still end in `.html`.
- In-page `#anchors` are kept as in the source. Some may not match the heading ids GitHub generates.
- It is a snapshot. The Help Portal is updated continuously. Re-run the export to refresh it.

## Regenerating the export

The two scripts in [`tools/`](tools) rebuild `docs/` from the Help Portal. They need Python 3.9+,
[`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) and [`pandoc`](https://pandoc.org/).

```bash
# 1. download the table of contents and the raw HTML of every topic (about 15 minutes, resumable)
python3 tools/fetch.py /path/to/cache --workers 8

# 2. convert the cached HTML into docs/
rm -rf docs
python3 -I tools/convert.py /path/to/cache docs
```

`fetch.py` uses the JSON endpoints behind the Help Portal web app (`deliverableMetadata` and `pagecontent`), because
the portal itself is a JavaScript app that returns no content to a plain HTTP request. It is polite (8 parallel requests, retries
with backoff) but is not an official API, so it may break if SAP changes the portal.
