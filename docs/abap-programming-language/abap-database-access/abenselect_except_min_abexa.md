---
title: "SELECT, Difference with Aggregate Expression"
source_file: abenselect_except_min_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > UNION, INTERSECT, EXCEPT > EXCEPT, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Difference with Aggregate Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a difference is created across a table using an aggregate expression.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_select_except_min DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_except_min IMPLEMENTATION. 
  METHOD main. 
    DATA carrid TYPE sflight-carrid VALUE 'AA'. 
    cl_demo_input=>new( )->request( CHANGING field = carrid ). 
 
    SELECT carrid, connid, seatsocc 
           FROM sflight 
           WHERE carrid = @( to_upper( carrid ) ) 
           EXCEPT SELECT carrid, 
                        connid, 
                        MIN( seatsocc ) AS seatsocc 
                        FROM sflight 
                        WHERE carrid = @( to_upper( carrid ) ) 
                        GROUP BY carrid, connid 
           ORDER BY carrid, connid, seatsocc 
           INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[`EXCEPT`](abapunion.md) is used to create the difference of the result sets of two `SELECT` statements for the same DDIC database table. The first `SELECT` statement reads all flights for a carrier and the second `SELECT` statement aggregates the flights by connection, adding the minimum number of occupied seats. The entire result contains only the non-aggregated rows as they are only available in the first result set.
