---
title: "sql_win - Window Expressions"
source_file: abensql_expr_over_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_win > sql_win - Examples of Window Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_win - Window Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates simple [window expressions](abapselect_over.md).

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
CLASS cl_demo_select_over DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_over IMPLEMENTATION. 
  METHOD main. 
 
    SELECT char1 && '_' && char2 AS group, 
           num1, 
           COUNT(*)      OVER( PARTITION BY char1, char2 ) AS cnt, 
           ROW_NUMBER( ) OVER( PARTITION BY char1, char2 ) AS rnum, 
           MIN( num1 )   OVER( PARTITION BY char1, char2 ) AS min, 
           MAX( num1 )   OVER( PARTITION BY char1, char2 ) AS max, 
           SUM( num1 )   OVER( PARTITION BY char1, char2 ) AS sum, 
           division( 100 * num1, 
                     SUM( num1 ) OVER( PARTITION BY char1, char2 ), 
                     2 ) AS perc 
           FROM demo_expressions 
           ORDER BY group 
           INTO TABLE @FINAL(windowed). 
 
    out->write( windowed ). 
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

The example demonstrates how different [window functions](abensql_win_func.md) are applied to windows of a result set of a query defined using [`PARTITION BY`](abapselect_over.md). The content of the columns `CHAR1` and `CHAR2` is used as a window criterion. All rows that have identical content in these columns form a window. The result of a window function for a row is determined from all rows of the window this row is a part of. The final column `perc` demonstrates how a window function can be used as arguments of an SQL expression and hence produce row-dependent results, in this case the percentage of the value of the column `NUM1` as part of the entire window.
