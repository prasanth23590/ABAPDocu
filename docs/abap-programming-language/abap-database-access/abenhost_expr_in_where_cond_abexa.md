---
title: "Host Expressions, Use in the WHERE Condition"
source_file: abenhost_expr_in_where_cond_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Operands sql_elem > ABAP SQL - @( expr )"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Host Expressions, Use in the WHERE Condition

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [host expressions](abenabap_sql_host_expressions.md) on the right side of a [relational expression](abenabap_sql_stmt_logexp.md) of a [`WHERE`](abapwhere.md) condition.

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
CLASS cl_demo_select_where_tab_exp DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    DATA carriers TYPE HASHED TABLE OF scarr 
              WITH UNIQUE KEY carrid 
              WITH NON-UNIQUE SORTED KEY name COMPONENTS carrname. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_where_tab_exp IMPLEMENTATION. 
  METHOD main. 
    DATA name TYPE scarr-carrname VALUE 'United Airlines'. 
    cl_demo_input=>new( )->request( CHANGING field = name ). 
 
    SELECT carrid, connid, cityfrom, cityto 
           FROM spfli 
           WHERE carrid = 
             @( VALUE spfli-carrid( carriers[ KEY name 
                                              carrname = name ]-carrid 
                                              OPTIONAL ) ) 
           INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    SELECT * 
           FROM scarr 
           INTO TABLE @carriers. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A table expression is evaluated as a host expression on the right side of an [SQL condition](abenabap_sql_stmt_logexp.md). The result is used for the comparison with the column specified on the left side.
