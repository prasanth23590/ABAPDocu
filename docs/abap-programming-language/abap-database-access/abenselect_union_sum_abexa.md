---
title: "SELECT, Union with Aggregate Expression"
source_file: abenselect_union_sum_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > UNION, INTERSECT, EXCEPT > UNION, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Union with Aggregate Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a union is created across a table using an aggregate expression.

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
CLASS cl_demo_select_union_sum DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_union_sum IMPLEMENTATION. 
  METHOD main. 
    DATA carrid TYPE sflight-carrid VALUE 'AA'. 
    cl_demo_input=>new( )->request( CHANGING field = carrid ). 
 
    SELECT ' ' AS mark, carrid, connid, fldate, seatsocc 
           FROM sflight 
           WHERE carrid = @( to_upper( carrid ) ) 
           UNION SELECT 'X' AS mark, 
                        carrid, 
                        connid, 
                        "@( CONV d( '00000000' ) ) AS fldate, 
                        CAST( '00000000' AS DATS ) AS fldate, 
                        SUM( seatsocc ) AS seatsocc 
                        FROM sflight 
                        WHERE carrid = @( to_upper( carrid ) ) 
                        GROUP BY carrid, connid 
           ORDER BY carrid, connid, mark, fldate, seatsocc 
           INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[`UNION`](abapunion.md) is used to create the union of the result sets of two `SELECT` statements for the same DDIC database table. The first `SELECT` statement reads all flights for a carrier and the second `SELECT` statement aggregates the flights by connection, adding the number of occupied seats. A [`CAST` expression](abensql_cast.md) is used to insert a column for the flight date `fldate` from the first result set with a suitable data type in the second result set. A comment indicates how this is also possible using a [host expression](abenabap_sql_host_expressions.md) in this case. A further column `mark` is filled with literals to make realistic sorts possible. The entire result contains the aggregated rows located below the associated rows of the first result set and are flagged with *X*.
