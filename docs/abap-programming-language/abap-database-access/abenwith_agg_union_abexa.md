---
title: "WITH, Aggregation for Join Set"
source_file: abenwith_agg_union_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, Aggregation for Join Set

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how to use [`WITH`](abapwith.md) for an aggregation.

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
CLASS cl_demo_select_union_sum_cte DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_union_sum_cte IMPLEMENTATION. 
  METHOD main. 
    DATA carrid TYPE sflight-carrid VALUE 'AA'. 
    cl_demo_input=>new( )->request( CHANGING field = carrid ). 
 
    WITH +agg AS ( 
      SELECT carrid, 
             connid, 
             CAST( '00000000' AS DATS ) AS fldate, 
             SUM( seatsocc ) AS seatsocc 
             FROM sflight 
             WHERE carrid = @( to_upper( carrid ) ) 
             GROUP BY carrid, connid ) 
      SELECT ' ' AS mark, carrid, connid, fldate, seatsocc 
             FROM sflight 
             WHERE carrid = @( to_upper( carrid ) ) 
             UNION SELECT 'X' AS mark, 
                          carrid, connid, fldate, seatsocc 
                          FROM +agg 
             ORDER BY carrid, connid, mark, fldate, seatsocc 
             INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example has the same result as the executable example for a [union with a global temporary table](abenselect_union_sum_gtt_abexa.md). The source code is almost identical. Here the global temporary table `demo_sflight_agg` has been replaced by a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) `+agg` and both `SELECT` statements are part of a `WITH` statement.
