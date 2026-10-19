---
title: "Table Buffering - Full Buffering"
source_file: abenbuffer_complete_buffering.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering > Table Buffering - Buffering Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering - Full Buffering

When a row is read, all rows in the table or view are loaded to the [table buffer](../../abap-glossary/abentable_buffer_glosry.md). The buffered table or view is either entirely in the buffer or not at all. In the buffer, the buffered data records are sorted by the key of the table or view. Optimized access requires that the left-aligned part of the primary key or of the fields of a secondary index be as large as possible. If not, the buffer is scanned linearly.

If full buffering is switched on in a client-dependent table or view, generic buffering using the client column as a generic key is performed internally.

## Hints

- In a fully buffered table or view, access to nonexistent data is very fast (see [Buffer Management](abenbuffer_memory.md)).

- For fully buffered tables or views, [restrictions](abensql_engine_restr.md) that cause [bypassing](abenbuffer_restrictions.md) the buffer come from the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) only.

- Full buffering should be used for small amounts of data, such as customizing tables. For larger amounts of data, full buffering is worthwhile only if large quantities of data are read frequently. Writes on fully buffered tables should be performed only rarely.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The table `T005` is fully buffered since it is small and accessed often by reads.
