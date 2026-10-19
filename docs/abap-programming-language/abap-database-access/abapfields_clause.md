---
title: "SELECT, FIELDS"
source_file: abapfields_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FIELDS

## Syntax

``` abap
... FIELDS select_clause ...  
```

[`select_clause`](abapselect_clause.md)

## Description

The addition `FIELDS` must prefix the `SELECT` clause [`select_clause`](abapselect_clause.md) of a [query](../../abap-glossary/abenasql_query_glosry.md), if this clause is listed after the [`FROM` clause](abapfrom_clause.md). If the `SELECT` clause [`select_clause`](abapselect_clause.md) is listed in front of the [`FROM` clause](abapfrom_clause.md), then `FIELDS` must not be specified.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Two equivalent `SELECT` statements and different arrangements of the `SELECT` and `FROM` clauses.

``` abap
SELECT FROM scarr 
       FIELDS carrid, carrname 
       ORDER BY carrid 
       INTO TABLE @FINAL(result1). 
 
SELECT carrid, carrname 
       FROM scarr 
       ORDER BY carrid 
       INTO TABLE @FINAL(result2). 
 
ASSERT result1 = result2.
```
