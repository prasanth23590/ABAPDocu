---
title: "sql_exp - Simple CASE"
source_file: abensql_expr_case_string_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_case > sql_exp - sql_simple_case"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - Simple CASE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates simple case distinctions in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_expr_case_string DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_case_string IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( VALUE #( 
      ( id = 'x' char1 = 'aaaaa' char2 = 'bbbbb' ) 
      ( id = 'y' char1 = 'xxxxx' char2 = 'yyyyy' ) 
      ( id = 'z' char1 = 'mmmmm' char2 = 'nnnnn' ) ) ). 
 
    FINAL(else) = 'fffff'. 
    SELECT id, char1, char2, 
           CASE char1 
             WHEN 'aaaaa' THEN ( char1 && char2 ) 
             WHEN 'xxxxx' THEN ( char2 && char1 ) 
             ELSE @else 
           END AS text 
           FROM demo_expressions 
           INTO TABLE @FINAL(results). 
 
    out->write( results ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In a list of columns specified after `SELECT`, [`CASE`](abensql_simple_case.md) is used to make a simple case distinction for the content of a column. The result is a character string that is concatenated from column content or taken from a [host variable](abenabap_sql_host_variables.md). Using the alias name defined after `AS`, the result is assigned to the identically named column in an internal table declared inline, `results`.
