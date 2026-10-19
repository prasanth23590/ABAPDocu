---
title: "sql_exp - Constant in SELECT List"
source_file: abensql_expr_literal_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_elem"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - Constant in SELECT List

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates one way to use a constant value in the `SELECT` list.

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
CLASS cl_demo_sql_expr_literal DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_literal IMPLEMENTATION. 
  METHOD main. 
    DATA carrier TYPE scarr-carrid. 
    cl_demo_input=>new( )->request( CHANGING field = carrier ). 
 
    SELECT SINGLE @abap_true 
           FROM scarr 
           WHERE carrid = @carrier 
           INTO @FINAL(exists). 
    IF exists = abap_true. 
      out->write( 
        |Carrier { carrier } exists in SCARR| ). 
    ELSE. 
      out->write( 
        |Carrier { carrier } does not exist in SCARR| ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

It is to be determined whether a row exists for a `WHERE` condition, regardless of the content of the row. A constant is specified to make specifying a column of the database and transporting it unnecessary. The target object `exists` is created using an inline declaration.
