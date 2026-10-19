---
title: "ENDSELECT"
source_file: abapendselect.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ENDSELECT

## Syntax

``` abap
ENDSELECT.   
```

## Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `ENDSELECT` closes a loop started using [`SELECT`](abapselect.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` loop. The [`INTO` clause](abapinto_clause.md) used here cannot be written to a tabular result, which means that in multirow result sets, a loop is opened that must be closed using `ENDSELECT`.

``` abap
SELECT carrid, connid, SUM( seatsocc ) AS seatsocc 
       FROM sflight 
       GROUP BY carrid, connid 
       ORDER BY carrid, connid 
       INTO (@FINAL(carrid),@FINAL(connid),@FINAL(seatsocc)). 
  ... 
ENDSELECT.
```
