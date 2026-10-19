---
title: "sql_win - Window Expressions with Grouping"
source_file: abensql_expr_over_group_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_win > sql_win - Examples of Window Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_win - Window Expressions with Grouping

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [window expressions](abapselect_over.md) for a grouped result set.

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
CLASS cl_demo_select_over_group DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_over_group IMPLEMENTATION. 
  METHOD main. 
 
    SELECT char1 && '_' && char2 AS group, 
           COUNT(*)                   AS cnt, 
           AVG( num1 AS DEC( 12,2 ) ) AS avg, 
           CORR_SPEARMAN( num1,num2 ) AS corr, 
           SUM( num1 )                AS sum, 
           COUNT(*)           OVER( PARTITION BY char1 ) AS win_cnt, 
           COUNT( DISTINCT num1 ) 
                              OVER( PARTITION BY char1 ) 
                              AS win_cnt_dist, 
           ROW_NUMBER( )      OVER( PARTITION BY char1 ) AS win_num, 
           MIN( AVG( num1 AS DEC( 12,2 ) ) ) 
                              OVER( PARTITION BY char1 ) AS win_min, 
           MAX( AVG( num1 AS DEC( 12,2 ) ) ) 
                              OVER( PARTITION BY char1 ) AS win_max, 
           SUM( SUM( num1 ) ) OVER( PARTITION BY char1 ) AS win_sum, 
           VAR( CAST( num1 AS FLTP ) ) 
                              OVER( PARTITION BY char1 ) AS var, 
           division( 100 * SUM( num1 ), 
                     SUM( SUM( num1 ) ) OVER( PARTITION BY char1 ), 
                     2 ) AS win_perc 
           FROM demo_expressions 
           GROUP BY char1, char2, num1 
           ORDER BY group 
           INTO TABLE @FINAL(groups_windowed). 
 
    out->write( groups_windowed ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    TYPES tab_type TYPE STANDARD TABLE OF 
                   demo_expressions WITH EMPTY KEY. 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( REDUCE tab_type( 
      LET r1 = cl_abap_random_int=>create( 
                 seed = CONV i( 
                  cl_demo_date_time=>get_user_time( ) ) 
                  min = 1 max = 10 ) 
          r2 = cl_abap_random_int=>create( 
                 seed = CONV i( r1->get_next( ) ) min = 0 max = 1 ) 
          c = `AB` IN 
      INIT t TYPE tab_type 
      FOR i = 0 THEN i + 1 UNTIL i >= 25 
      NEXT t = VALUE #( 
                 BASE t ( id    = abcde+i(1) 
                          num1  = r1->get_next( ) 
                          char1 = substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) && 
                                  substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) 
                          char2 = substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) && 
                                  substring( val = c 
                                             off = r2->get_next( ) 
                                             len = 1 ) ) ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example shows the combination of [window expressions](abapselect_over.md) in the `SELECT` list with a [`GROUP BY`](abapgroupby_clause.md) clause. In this case, [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) used as a [window function](../../abap-glossary/abenwindow_function_glosry.md) can also have aggregate functions as arguments.

The `GROUP BY` clause groups by the columns `CHAR1` and `CHAR2`. In the result set created by this, [`OVER`](abapselect_over.md) is used to define windows whose window criterion is the column `CHAR1`. Aggregate expressions that can be specified as columns in the `SELECT` list due to the `GROUP BY` clause are also used as arguments of window functions.

The aggregate functions used as an argument of window functions would not need to appear as separately specified columns in the `SELECT` list but are shown here anyway to highlight how these values are produced.
