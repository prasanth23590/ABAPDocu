---
title: "sql_win - Window Functions LEAD and LAG"
source_file: abensql_expr_over_lead_lag_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_win > sql_win - Examples of Window Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_win - Window Functions LEAD and LAG

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [window expressions](abapselect_over.md) with the [window functions](../../abap-glossary/abenwindow_function_glosry.md) [`LEAD`](abensql_win_func.md) and [`LAG`](abensql_win_func.md).

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
CLASS cl_demo_select_over_lead_lag DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_over_lead_lag IMPLEMENTATION. 
  METHOD main. 
 
    SELECT char1, char2, 
           num1, 
           ROW_NUMBER( ) 
             OVER( PARTITION BY char1 ORDER BY char2 ) 
               AS rnum, 
           LEAD( CAST( num1 AS CHAR( 11 ) ), 1, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 ) 
               AS lead1, 
           LAG( CAST( num1 AS CHAR( 11 ) ), 1, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 ) 
               AS lag1, 
           LEAD( CAST( num1 AS CHAR( 11 ) ), 2, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 ) 
               AS lead2, 
           LAG( CAST( num1 AS CHAR( 11 ) ), 2, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 ) 
               AS lag2, 
           LEAD( CAST( num1 AS CHAR( 11 ) ), 10, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 ) 
               AS lead10, 
           LAG( CAST( num1 AS CHAR( 11 ) ), 10, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 ) 
               AS lag10 
           FROM demo_expressions 
           ORDER BY char1, char2                        "#EC CI_NOWHERE 
           INTO TABLE @FINAL(windowed_order_ascending) ##no_text. 
    out->write( windowed_order_ascending ). 
 
    SELECT char1, char2, 
           num1, 
           ROW_NUMBER( ) 
             OVER( PARTITION BY char1 ORDER BY char2 DESCENDING ) 
               AS rnum, 
           LEAD( CAST( num1 AS CHAR( 11 ) ), 1, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 DESCENDING ) 
               AS lead1, 
           LAG( CAST( num1 AS CHAR( 11 ) ), 1, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 DESCENDING ) 
               AS lag1, 
           LEAD( CAST( num1 AS CHAR( 11 ) ), 2, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 DESCENDING ) 
               AS lead2, 
           LAG( CAST( num1 AS CHAR( 11 ) ), 2, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 DESCENDING ) 
               AS lag2, 
           LEAD( CAST( num1 AS CHAR( 11 ) ), 10, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 DESCENDING ) 
               AS lead10, 
           LAG( CAST( num1 AS CHAR( 11 ) ), 10, 'Nope' ) 
             OVER( PARTITION BY char1 ORDER BY char2 DESCENDING ) 
               AS lag10 
           FROM demo_expressions 
           ORDER BY char1, char2                        "#EC CI_NOWHERE 
           INTO TABLE @FINAL(windowed_order_descending) ##no_text. 
    out->write( windowed_order_descending ). 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    TYPES tab_type TYPE STANDARD TABLE OF 
                   demo_expressions WITH EMPTY KEY. 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    DELETE FROM demo_expressions.                      "#EC CI_NOWHERE. 
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

The example shows results of the window functions [`LEAD`](abensql_win_func.md) and [`LAG`](abensql_win_func.md) to which all three possible arguments are passed. Like in the executable example, the windows are determined for [window expressions with sorting](abensql_expr_over_order_by_abexa.md).

- The first argument determines the result as a character-like representation of the column `NUM1` of the row determined by the second argument.

- The second argument determines the rows to be evaluated using differently sized distances.

- The third argument is a literal returned instead of the null value if the row to be evaluated is not in the current window.
