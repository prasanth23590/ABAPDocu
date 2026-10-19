---
title: "sql_win - Window Function NTILE"
source_file: abensql_expr_over_ntile_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_win > sql_win - Examples of Window Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_win - Window Function NTILE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [window expression](abapselect_over.md) with the [window function](../../abap-glossary/abenwindow_function_glosry.md) [`NTILE`](abensql_win_func.md).

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
CLASS cl_demo_select_over_ntile DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_over_ntile IMPLEMENTATION. 
  METHOD main. 
 
    SELECT name, 
           salary, 
           NTILE( 5 ) OVER( ORDER BY salary ) AS ntile 
           FROM demo_employees 
           INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
 
    DELETE FROM demo_employees.                         "#EC CI_NOWHERE 
    INSERT demo_employees FROM TABLE @( 
       VALUE #( ( name = 'Lothar Sudhoff' salary = '1354.00' ) 
       ( name = 'Christa Martin' salary = '3247.00' ) 
       ( name = 'Illya Gueldenpfennig' salary = '7453.00' ) 
       ( name = 'Johannes Legrand' salary = '1468.00' ) 
       ( name = 'Johann Buchholm' salary = '3245.00' ) 
       ( name = 'Holm Trensch' salary = '2324.00' ) 
       ( name = 'Laura Lindwurm' salary = '3247.00' ) 
       ( name = 'Thilo Eichbaum' salary = '5436.00' ) 
       ( name = 'Amelie Babilon' salary = '3485.00' ) 
       ( name = 'Ulla Babilon' salary = '5489.00' ) 
       ( name = 'Anna Picard' salary = '7453.00' ) 
       ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

All employees from the `DEMO_EMPLOYEES` table are sorted by their salary, starting with the lowest, and distributed into five salary groups by the `NTILE` function. The first group, group 1, has one entry more than the other four groups, as the number of employees (11) cannot be distributed equally into the number of buckets (five in this example).
