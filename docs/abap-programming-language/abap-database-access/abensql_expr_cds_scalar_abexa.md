---
title: "sql_exp - CDS Scalar Function"
source_file: abensql_expr_cds_scalar_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - cds_scalar_func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - CDS Scalar Function

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of a [SQL-based scalar function](abensql_cds_scalar_func.md) in ABAP SQL.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Executable demo of ABAP Docu</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_cds_scalar_function DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_scalar_function IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( VALUE #( 
     ( id = 'X' num1 = 100 num2 = 200 ) ) ). 
 
    SELECT FROM demo_expressions 
    FIELDS id, 
           num1, 
           num2, 
           CAST( demo_cds_scalar_ratio( portion = num1, total = num2 ) 
                 AS DEC ) AS percentage 
           WHERE id = 'X' 
    INTO TABLE @FINAL(result). 
 
    out->write( result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The SQL-based scalar function `DEMO_CDS_SCALAR_RATIO` calculates the percentage of two input parameters.

``` abap
define scalar function DEMO_CDS_SCALAR_RATIO 
  with parameters 
    portion: numeric 
      with reference type [ #CUKY, #UNIT, #CALC, #NONE ], 
    total  : type of portion 
      with reference type of portion 
  returns abap.decfloat34 
    with reference type #NONE;
```

It is implemented as follows:

``` abap
METHOD execute BY DATABASE FUNCTION 
               FOR HDB 
               LANGUAGE SQLSCRIPT 
               OPTIONS READ-ONLY. 
  result = portion / total * 100; 
ENDMETHOD.
```

In the above example class, it is used in the `SELECT` list of a query.
