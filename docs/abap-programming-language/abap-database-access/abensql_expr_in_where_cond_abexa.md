---
title: "SELECT, SQL Expressions in the WHERE Condition"
source_file: abensql_expr_in_where_cond_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, WHERE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, SQL Expressions in the WHERE Condition

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how [SQL expressions](abapsql_expr.md) are used on the left side of a [`WHERE`](abenabap_sql_stmt_logexp.md) condition.

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
CLASS cl_demo_select_where_exprssn DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS input RETURNING VALUE(free_seats) TYPE i. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_where_exprssn IMPLEMENTATION. 
  METHOD main. 
    SELECT carrid, connid, fldate, seatsmax, seatsocc, 
           seatsmax - seatsocc AS seatsfree 
           FROM sflight 
           WHERE seatsmax - seatsocc > @( input( ) ) 
           INTO TABLE @FINAL(result) 
           UP TO 100 ROWS. 
    out->write( result ). 
  ENDMETHOD. 
  METHOD input. 
    cl_demo_input=>new( )->request( CHANGING field = free_seats ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

On the left side of the [relational expression](abenabap_sql_stmt_logexp.md), the content of two specified columns is subtracted in an [SQL expression](abapsql_expr.md). This calculation is performed on the database. The right side is a functional method call in a [host expression](abenabap_sql_host_expressions.md).
