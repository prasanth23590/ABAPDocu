---
title: "Table Buffering - Generic Buffering"
source_file: abenbuffer_generic_buffering.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering > Table Buffering - Buffering Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering - Generic Buffering

When a read is performed on a row, all rows are loaded into the table buffer that match this row in a left-aligned part of the primary key. The number of respected key fields is specified in the definition and is always less than the total number of key fields. These key fields form the generic key.

The individual generic areas are handled like standalone tables or views whose primary key is the generic key and that are fully buffered.

If a fully specified generic key is used to access an unbuffered row through ABAP SQL, an attempt is made to load the area. If the row is not found, this is noted in the buffer and the database is not accessed again the next time a row is accessed using a fully specified generic key.

## Hints

- In a generically buffered table or view, access to nonexistent data is very fast (see [Buffer Management](abenbuffer_memory.md)).

- When using generic buffering, any ABAP SQL statements must respect the generic key to prevent them from [bypassing](abenbuffer_restrictions.md) table buffering.

- Generic buffering should be used if usually only certain areas of the table or view are required. These areas should not be too small, to prevent too many of them from being created and overloading buffer management. They should also not be too big, to prevent too much data from being loaded. [Full buffering](abenbuffer_complete_buffering.md) may also be more efficient in some cases. Accordingly, the generic key must not cover too many or too few fields.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

One good application of generic buffering is language-dependent data that has the language code field as a generic key.
