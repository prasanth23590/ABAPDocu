---
title: "Statements for Character String and Byte String Processing"
source_file: abenstring_processing_statements.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Statements for Character String and Byte String Processing

The following table shows the key words for character and byte string processing and the processing supported by these statements.

| **Keyword**                             | **Character String Processing** | **Byte String Processing** |
|-----------------------------------------|---------------------------------|----------------------------|
| [`CONCATENATE`](abapconcatenate.md)   | X                               | X                          |
| [`FIND`](abapfind.md)                 | X                               | X                          |
| [`REPLACE`](abapreplace.md)           | X                               | X                          |
| [`SHIFT`](abapshift.md)               | X                               | X                          |
| [`SPLIT`](abapsplit.md)               | X                               | X                          |
| [`CONDENSE`](abapcondense.md)         | X                               | \-                         |
| [`CONVERT TEXT`](abapconvert_text.md) | X                               | \-                         |
| [`OVERLAY`](abapoverlay.md)           | X                               | \-                         |
| [`TRANSLATE`](abaptranslate.md)       | X                               | \-                         |
| `WRITE TO`                              | X                               | \-                         |
|                                         |                                 |                            |
| [`SET BIT`](abapset_bit.md)           | \-                              | X                          |
| [`GET BIT`](abapget_bit.md)           | \-                              | X                          |

There is a strict split between character string processing and byte string processing. Each of the key words in the table that supports both character string and byte string processing has the optional addition

`... IN {CHARACTER|BYTE} MODE ...`

This addition determines which processing is used. If this addition is not specified, character string processing is performed in these statements.

## Hints

- In most cases, [expressions and functions for character string processing](abenstring_processing_expr_func.md) can be used instead of the above statements for character string processing. These have the advantage that expressions can be specified for all operands, which is only possible to a very limited extent in the above statements.
