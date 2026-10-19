---
title: "sql_exp - Arithmetic Calculations"
source_file: abensql_expr_arith_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_arith"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - Arithmetic Calculations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates arithmetic calculations in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_expr_arith DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_arith IMPLEMENTATION. 
  METHOD main. 
    FINAL(rnd) = cl_abap_random_int=>create( 
      seed = CONV i( 
        cl_demo_date_time=>get_user_time( ) ) 
        min = 1 max = 100 ). 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( VALUE #( 
      FOR i = 0 UNTIL i > 9 
      ( id = |{ i }| 
        num1 = rnd->get_next( ) 
        num2 = rnd->get_next( ) ) ) ). 
 
    FINAL(offset) = 10000. 
    SELECT id, num1, num2, 
           CAST( num1 AS D34N ) / CAST( num2 AS D34N ) AS ratio, 
           div( num1, num2 ) AS div, 
           division( num1, num2, 2 ) AS division, 
           mod( num1, num2 ) AS mod, 
           @offset + abs( num1 - num2 ) AS sum 
           FROM demo_expressions 
           ORDER BY sum DESCENDING 
           INTO TABLE @FINAL(results). 
 
    out->write( results ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Calculations are made and functions called in a list of columns specified after `SELECT`.

- To perform [floating point division](abensql_arith.md) with integer columns, these columns are converted to the type `DECFLOAT34` using a [`cast`](abensql_cast.md) expression.

- Integer divisions with the functions [`DIV`](abensql_arith_func.md), [`MOD`](abensql_arith_func.md), and [`DIVISION`](abensql_arith_func.md) do not require this conversion.

- A [host variable](abenabap_sql_host_variables.md) is added to the absolute value of a difference between column values.

Using the alias names defined after `AS`, the results are assigned to identically named columns of an internal table `results` declared inline. The result of the final calculation is used as a sort criterion.
