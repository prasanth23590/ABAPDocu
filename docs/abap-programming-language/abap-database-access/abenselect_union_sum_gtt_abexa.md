---
title: "SELECT, Union with Global Temporary Table"
source_file: abenselect_union_sum_gtt_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > UNION, INTERSECT, EXCEPT > UNION, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Union with Global Temporary Table

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a union across a table and a global temporary table (GTT).

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
CLASS cl_demo_select_union_sum_gtt DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_union_sum_gtt IMPLEMENTATION. 
  METHOD main. 
 
    DATA carrid TYPE sflight-carrid VALUE 'AA'. 
    cl_demo_input=>new( )->request( CHANGING field = carrid ). 
 
    INSERT demo_sflight_agg FROM ( 
    SELECT carrid, 
           connid, 
           CAST( '00000000' AS DATS ) AS fldate, 
           SUM( seatsocc ) AS seatsocc 
           FROM sflight 
           WHERE carrid = @( to_upper( carrid ) ) 
           GROUP BY carrid, connid ). 
 
    SELECT ' ' AS mark, carrid, connid, fldate, seatsocc 
           FROM sflight 
           WHERE carrid = @( to_upper( carrid ) ) 
           UNION SELECT 'X' AS mark, 
                        carrid, connid, fldate, seatsocc 
                        FROM demo_sflight_agg 
           ORDER BY carrid, connid, mark, fldate, seatsocc 
           INTO TABLE @FINAL(result). 
 
    DELETE FROM demo_sflight_agg. 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example has the same result as the executable example for a [union with aggregate expression](abenselect_union_sum_abexa.md). Here, however, the `SELECT` statement is split into two ABAP SQL statements for demonstration purposes:

- The aggregation is performed in the [subquery](../../abap-glossary/abensubquery_glosry.md) of an [`INSERT`](abapinsert_dbtab.md) statement whose result set is written to a [global temporary table (GTT)](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md).

- [`UNION`](abapunion.md) is used to create the union of the result set of a `SELECT` statement on the table `SFLIGHT` and a `SELECT` statement on the GTT.

The GTT must be cleared explicitly before the end of the execution to prevent the runtime error `COMMIT_GTT_ERROR` in the next implicit database commit.

## Hint

See also the corresponding executable [example](abenwith_agg_union_abexa.md) for [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md).
