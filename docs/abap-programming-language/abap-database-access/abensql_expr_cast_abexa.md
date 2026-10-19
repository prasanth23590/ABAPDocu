---
title: "sql_exp - Cast Expression"
source_file: abensql_expr_cast_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_cast"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - Cast Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [cast expressions](abensql_cast.md) in ABAP SQL.

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
CLASS cl_demo_sql_expr_cast DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_cast IMPLEMENTATION. 
  METHOD main. 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM @( VALUE #( 
             id   = 'X' 
             num1 = 111 
             numlong1 = '123456789' 
             dec3 = '123.456' 
             dats2 = cl_demo_date_time=>get_system_date( ) ) ). 
 
    SELECT SINGLE 
           FROM demo_expressions 
           FIELDS CAST( num1     AS CHAR( 20 ) ) AS col1, 
                  CAST( numlong1 AS CHAR( 20 ) ) AS col2, 
                  CAST( dec3     AS CHAR( 20 ) ) AS col3, 
                  CAST( dats2    AS CHAR( 20 ) ) AS col4 
           WHERE id = 'X' 
           INTO @FINAL(result). 
 
    DATA(text)  = ``. 
    DO. 
      ASSIGN result-(sy-index) TO FIELD-SYMBOL(<col>). 
      IF sy-subrc = 0. 
        text = text && <col> && `, `. 
      ELSE. 
        EXIT. 
      ENDIF. 
    ENDDO. 
    CONDENSE text. 
    SHIFT text RIGHT DELETING TRAILING `,`. 
    out->write( text ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Transforms numeric columns and a date field from a DDIC database table to columns of the type `CHAR`, which makes it possible to process them as character strings in the ABAP class.
