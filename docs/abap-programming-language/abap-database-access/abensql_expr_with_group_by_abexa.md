---
title: "SELECT, GROUP BY for SQL Expressions"
source_file: abensql_expr_with_group_by_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, GROUP BY for SQL Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates non elementary [SQL expressions](abapsql_expr.md) combined with the addition [`GROUP BY`](abapgroupby_clause.md).

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
CLASS cl_demo_sql_expr_with_group_by DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_with_group_by IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( VALUE #( 
      ( id = 1 num1 = 1 num2 = 1 ) 
      ( id = 2 num1 = 2 num2 = 4 ) 
      ( id = 3 num1 = 3 num2 = 2 ) 
      ( id = 4 num1 = 3 num2 = 2 ) 
      ( id = 5 num1 = 5 num2 = 1 ) 
      ( id = 6 num1 = 1 num2 = 1 ) 
      ( id = 7 num1 = 1 num2 = 1 ) ) ). 
 
    out->begin_section( `GROUP BY num1, num2` ). 
    SELECT num1 + num2 AS sum, COUNT( * ) AS count 
           FROM demo_expressions 
           GROUP BY num1, num2 
           ORDER BY sum 
           INTO TABLE @FINAL(result1). 
    out->write( result1 ). 
 
    out->next_section( `GROUP BY num1 + num2` ). 
    SELECT num1 + num2 AS sum, COUNT( * ) AS count 
           FROM demo_expressions 
           GROUP BY num1 + num2 
           ORDER BY sum 
           INTO TABLE @FINAL(result2). 
    out->write( result2 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An [arithmetic expression](abensql_arith.md) after `SELECT` adds the values of the columns `NUM1` and `NUM2` and passes the total to the result set as `SUM`. The [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md) `count( * )` counts the rows of a group. `NUM1` and `NUM2` must be specified for the grouping after `GROUP BY`.

- The first `SELECT` statement specifies `NUM1` and `NUM2` as individual columns after `GROUP BY`. The rows are grouped by these columns. Distinct values in these columns produce separate groups, even if the total is the same.

- The second `SELECT` statement specifies `NUM1` and `NUM2` in an SQL expression after `GROUP BY`. The rows are grouped by the result of the expression.
