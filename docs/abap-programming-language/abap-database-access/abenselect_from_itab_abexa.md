---
title: "SELECT, Internal Table as Data Source of a Query"
source_file: abenselect_from_itab_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM @itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Internal Table as Data Source of a Query

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how an internal table is accessed using an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md).

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
CLASS cl_demo_select_from_itab DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_from_itab IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF struct, 
        key1 TYPE c LENGTH 1, 
        key2 TYPE c LENGTH 1, 
        num1 TYPE i, 
        num2 TYPE i, 
      END OF struct, 
      itab TYPE SORTED TABLE OF struct 
                WITH NON-UNIQUE KEY key1 key2. 
 
    FINAL(rnd) = cl_abap_random_int=>create( 
      seed = CONV i( 
        cl_demo_date_time=>get_user_time( ) ) min = 1 max = 5 ). 
 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    FINAL(itab) = VALUE itab( 
      FOR i = 1 UNTIL i > 100 
        LET off1 = rnd->get_next( ) - 1 
            off2 = rnd->get_next( ) - 1 IN 
            ( key1 = abcde+off1(1) 
              key2 = abcde+off2(1) 
              num1 = rnd->get_next( ) 
              num2 = rnd->get_next( ) ) ). 
    out->write( itab ). 
 
    SELECT FROM @itab AS itab 
           FIELDS key1, 
                  key2, 
                  SUM( num1 ) AS sum1, 
                  SUM( num2 ) AS sum2, 
                  SUM( num1 + num2 ) AS sum 
           GROUP BY key1, key2 
           ORDER BY key1, key2 
           INTO TABLE @FINAL(result) ##itab_db_select. 
    out->write( result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An internal table is filled with random values and is used as a [data source](abapselect_itab.md) of a [`SELECT`](abapselect.md) statement. Aggregate expressions, an SQL expression, `GROUP BY`, and `ORDER BY` are all used when doing this. The statement cannot be processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) since it does not meet the corresponding [restrictions](abensql_engine_restr.md). The pragma `##itab_db_select` is used to hide the associated syntax check warning.
