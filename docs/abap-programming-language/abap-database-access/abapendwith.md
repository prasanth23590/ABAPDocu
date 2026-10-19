---
title: "ENDWITH"
source_file: abapendwith.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ENDWITH

## Syntax

``` abap
ENDWITH.   
```

## Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `ENDWITH` closes a loop started using [`WITH`](abapwith.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows a `WITH` statement, whose main query creates a tabular result set. Since the data is written into work area `wa` rather than to an internal table, a `SELECT` loop is opened, which must be closed with `ENDWITH`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
WITH 
  +carriers AS ( SELECT FROM scarr 
                        FIELDS carrid, carrname ) 
  SELECT FROM spfli AS s 
           INNER JOIN +carriers AS c 
             ON s~carrid = c~carrid 
         FIELDS c~carrname, s~connid 
         WHERE s~carrid = 'UA' 
         INTO @FINAL(wa) 
         UP TO 10 ROWS. 
  out->write( wa ). 
ENDWITH. 
 
out->display( ).
```
