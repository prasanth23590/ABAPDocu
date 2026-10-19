---
title: "sql_exp - Concatenations"
source_file: abensql_expr_string_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_string"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - Concatenations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how strings are concatenated in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_expr_string DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_string IMPLEMENTATION. 
  METHOD main. 
    SELECT FROM spfli 
           FIELDS concat( concat( carrid,'_' ), connid ) AS key, 
                  'from' && ' ' && cityfrom && 
                  ' to' && ' ' && cityto AS connection 
           INTO TABLE @FINAL(results). 
 
    out->write( results ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In a `SELECT` list, two columns of a result set of a query are created using concatenations of strings.

- The first column `key` cannot be created using the operator [`&&`](abensql_string.md). The column `CONNID` does not have the required data type and [cast expressions](abensql_cast.md) cannot be used either. The built-in function [`CONCAT`](abensql_string_func.md) is used instead.

- The second column `connection` can be constructed from columns and literals using the operator [`&&`](abensql_string.md).
