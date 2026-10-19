---
title: "sql_func - Coalesce Function"
source_file: abensql_expr_coalesce_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - Coalesce Function"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Coalesce Function

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the coalesce function in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_expr_coalesce DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: wa1 TYPE demo_join1, 
          wa2 TYPE demo_join2. 
    DATA BEGIN OF wa. 
    INCLUDE STRUCTURE wa1 AS wa1 RENAMING WITH SUFFIX 1. 
    INCLUDE STRUCTURE wa2 AS wa2 RENAMING WITH SUFFIX 2. 
    DATA END OF wa. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_coalesce IMPLEMENTATION. 
  METHOD main. 
    DATA itab LIKE TABLE OF wa WITH EMPTY KEY. 
    out->begin_section( `OUTER JOIN with Coalesce` ). 
    SELECT t1~a AS a1, t1~b AS b1, t1~c AS c1, t1~d AS d1, 
           coalesce( t2~d, '--' ) AS d2, 
           coalesce( t2~e, '--' ) AS e2, 
           coalesce( t2~f, '--' ) AS f2, 
           coalesce( t2~g, '--' ) AS g2, 
           coalesce( t2~h, '--' ) AS h2 
       FROM demo_join1 AS t1 
         LEFT OUTER JOIN demo_join2 AS t2 ON t2~d = t1~d 
       ORDER BY t1~d 
       INTO CORRESPONDING FIELDS OF TABLE @itab. 
    out->write( itab ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    DELETE FROM demo_join1.                             "#EC CI_NOWHERE 
    INSERT demo_join1 FROM TABLE @( VALUE #( 
      ( a = 'a1' b = 'b1' c = 'c1'  d = 'uu' ) 
      ( a = 'a2' b = 'b2' c = 'c2'  d = 'uu' ) 
      ( a = 'a3' b = 'b3' c = 'c3'  d = 'vv' ) 
      ( a = 'a4' b = 'b4' c = 'c4'  d = 'ww' ) ) ). 
    DELETE FROM demo_join2.                             "#EC CI_NOWHERE 
    INSERT demo_join2 FROM TABLE @( VALUE #( 
      ( d = 'uu' e = 'e1' f = 'f1'  g = 'g1'  h = 'h1' ) 
      ( d = 'ww' e = 'e2' f = 'f2'  g = 'g2'  h = 'h2' ) 
      ( d = 'xx' e = 'e3' f = 'f3'  g = 'g3'  h = 'h3' ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example is an excerpt from the executable example for [joins](abenjoins_abexa.md). Here, the function [`COALESCE`](abensql_coalesce.md) is used to replace null values produced by an outer join with a different value.
