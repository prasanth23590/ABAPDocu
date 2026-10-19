---
title: "Table Buffering - Single Record Buffering"
source_file: abenbuffer_single_buffering.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering > Table Buffering - Buffering Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering - Single Record Buffering

Only those rows are buffered that are actually accessed. This requires less space in the buffer than when using generic or full buffering. On the other hand, more administration work is required and significantly more direct database accesses.

If a [`WHERE`](abapwhere.md) clause is used to access a non-buffered row and this clause specifies equality conditions joined using `AND`, an attempt is made to load this row. If the row is not found, this is noted in the buffer and a fully specified `WHERE` clause is used to avoid a new database access in the next read.

## Hints

- When using single record buffering, any ABAP SQL statements must respect the entire primary key to prevent them from [bypassing](abenbuffer_restrictions.md) table buffering.

- Single record buffering is recommended for large amounts of data from which single rows are often read. For comparatively small amounts of data from which many rows are read, [full buffering](abenbuffer_complete_buffering.md) is usually preferred since this reduces the number of direct database accesses required for loading.

- The use of single record buffering depends on the `WHERE` clause only and not on the use of the addition [`SINGLE`](abapselect_single.md).
