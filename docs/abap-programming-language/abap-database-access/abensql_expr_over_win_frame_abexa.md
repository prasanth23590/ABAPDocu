---
title: "sql_win - Window Frame Specification"
source_file: abensql_expr_over_win_frame_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_win > sql_win - Examples of Window Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_win - Window Frame Specification

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how different [window functions](../../abap-glossary/abenwindow_function_glosry.md) are applied to frames inside a window.

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
CLASS cl_demo_select_ovr_win_frm_spe DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_ovr_win_frm_spe IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_update.                            "#EC CI_NOWHERE 
    INSERT demo_update FROM TABLE @( 
        VALUE #( ( id = 'A' col1 = '3' col2 = '7' ) 
                 ( id = 'B' col1 = '5' col2 = '5' ) 
                 ( id = 'C' col1 = '4' col2 = '5' ) 
                 ( id = 'D' col1 = '1' col2 = '1' ) 
                 ( id = 'E' col1 = '927' ) 
         ) ). 
 
    SELECT id, col1, col2, 
       COUNT( * ) OVER( ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING 
                                    AND CURRENT ROW ) 
                                    AS count, 
       COUNT( * ) OVER( ORDER BY id ROWS BETWEEN CURRENT ROW 
                                    AND UNBOUNDED FOLLOWING ) 
                                    AS count_reverse, 
       AVG( col1 ) OVER( ORDER BY id ROWS BETWEEN 1 PRECEDING 
                                     AND 1 FOLLOWING ) 
                                     AS average, 
       SUM( col1 ) OVER( ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING 
                                     AND CURRENT ROW ) 
                                     AS accumulate 
       FROM demo_update 
       INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

- `count` sorts the rows by the column `ID` and counts the number of rows from the first row of the window to the current row. The result is the same as that returned by the [`ROW_NUMBER( )`](abensql_win_func.md) function.

- `count_reverse` sorts the rows by the column `ID` and counts the number of rows from the current row to the last row of the window. The result is reverse numbering.

- `average` sorts the rows by the column `ID` and calculates the rolling averages of a subset of rows from column `COL1`. The subset consists of the current row plus one preceding and one following row. With this function, it is possible, for example, to calculate the 3-day-average temperature for every day from a list of temperature data.

- `accumulate` sorts the rows by the column `ID` and accumulates the values from the first row of the window up to the current row, thus computing the running total of column `COL1`.
