---
title: "sql_win - Window Expressions with Sort"
source_file: abensql_expr_over_order_by_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_win > sql_win - Examples of Window Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_win - Window Expressions with Sort

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [window expressions](abapselect_over.md) with a sort.

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
CLASS cl_demo_select_over_order_by DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_over_order_by IMPLEMENTATION. 
  METHOD main. 
 
    SELECT char1, char2, 
           num1, 
           COUNT(*)      OVER( PARTITION BY char1 ) AS cnt, 
           ROW_NUMBER( ) OVER( PARTITION BY char1 ) AS rnum, 
           '-'                                      AS rank, 
           '-'                                      AS schlank, 
           MAX( num1 )   OVER( PARTITION BY char1 ) AS max, 
           MIN( num1 )   OVER( PARTITION BY char1 ) AS min, 
           SUM( num1 )   OVER( PARTITION BY char1 ) AS sum, 
           division( 100 * num1, 
                     SUM( num1 ) OVER( PARTITION BY char1 ), 
                     2 ) AS perc 
           FROM demo_expressions 
           ORDER BY char1, char2 
           INTO TABLE @FINAL(windowed_no_order). 
    out->write( windowed_no_order ). 
 
    SELECT char1, char2, 
           num1, 
           COUNT(*)      OVER( PARTITION BY char1 
                               ORDER BY char2 ) AS cnt, 
           ROW_NUMBER( ) OVER( PARTITION BY char1 
                               ORDER BY char2 ) AS rnum, 
           RANK( )       OVER( PARTITION BY char1 
                               ORDER BY char2 ) AS rank, 
           DENSE_RANK( ) OVER( PARTITION BY char1 
                               ORDER BY char2 ) AS schlank, 
           MAX( num1 )   OVER( PARTITION BY char1 
                               ORDER BY char2 ) AS max, 
           MIN( num1 )   OVER( PARTITION BY char1 
                               ORDER BY char2 ) AS min, 
           SUM( num1 )   OVER( PARTITION BY char1 
                               ORDER BY char2 ) AS sum, 
           division( 100 * num1, 
                     SUM( num1 ) OVER( PARTITION BY char1 
                                       ORDER BY char2 ), 
                     2 ) AS perc 
           FROM demo_expressions 
           ORDER BY char1, char2 
           INTO TABLE @FINAL(windowed_order_ascending). 
    out->write( windowed_order_ascending ). 
 
    SELECT char1, char2, 
           num1, 
           COUNT(*)      OVER( PARTITION BY char1 
                               ORDER BY char2 DESCENDING ) AS cnt, 
           ROW_NUMBER( ) OVER( PARTITION BY char1 
                               ORDER BY char2 DESCENDING ) AS rnum, 
           RANK( )       OVER( PARTITION BY char1 
                               ORDER BY char2 DESCENDING ) AS rank, 
           DENSE_RANK( ) OVER( PARTITION BY char1 
                               ORDER BY char2 DESCENDING ) AS schlank, 
           MAX( num1 )   OVER( PARTITION BY char1 
                               ORDER BY char2 DESCENDING ) AS max, 
           MIN( num1 )   OVER( PARTITION BY char1 
                               ORDER BY char2 DESCENDING ) AS min, 
           SUM( num1 )   OVER( PARTITION BY char1 
                               ORDER BY char2 DESCENDING ) AS sum, 
           division( 100 * num1, 
                     SUM( num1 ) OVER( PARTITION BY char1 
                                 ORDER BY char2 DESCENDING ), 
                     2 ) AS perc 
           FROM demo_expressions 
           ORDER BY char1 DESCENDING, char2 DESCENDING 
           INTO TABLE @FINAL(windowed_order_descending). 
    out->write( windowed_order_descending ). 
 
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

The example compares `SELECT` statements with identical [window expressions](abapselect_over.md) with and without the addition `ORDER BY` specified after `OVER`. The use of the [ranking functions](../../abap-glossary/abenranking_function_glosry.md) [`RANK`](abensql_win_func.md) and [`DENSE_RANK`](abensql_win_func.md) is only possible in combination with this addition.

- If the addition `ORDER BY` is not specified after `OVER`, the window functions are executed in an undefined order for all rows of the windows defined by the content of the column `CHAR1`:

  - The aggregate functions `COUNT`, `MAX`, `MIN`, and `SUM` evaluate all rows of a window.

  - The ranking function `ROW_NUMBER` assigns a sequential row number within each window, which matches the undefined order of processing.

- When the addition `ORDER BY` is specified after `OVER` the window functions within the window are executed once in ascending order and once in descending order, with respect to the content of the column `CHAR2`. Only the rows of a frame are respected:

  - Within a window, that is, all rows with identical content in the column `CHAR1`, the aggregate functions `COUNT`, `MAX`, `MIN`, and `SUM` evaluate only those rows that have identical content in `CHAR2` or that precede it in the sort.

  - The ranking function `ROW_NUMBER` assigns the row number in accordance with the sort order. The order is then only undefined in rows with identical content in the column `CHAR2`. The ranking functions `RANK` and `DENSE_RANK` return the rank with respect to the sort order within the current window. Here, identical content in the column `CHAR2` has the same rank.

The addition `ORDER BY` of the `SELECT` statement is used only to highlight the output. It does not modify the results for the individual rows.
