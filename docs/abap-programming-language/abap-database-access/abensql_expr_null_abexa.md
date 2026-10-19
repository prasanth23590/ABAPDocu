---
title: "sql_exp - Null Expression"
source_file: abensql_expr_null_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_null"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - Null Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [null expressions](abensql_null.md) in ABAP SQL.

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
CLASS cl_demo_sql_expr_null DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_expr_null IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: BEGIN OF result, 
             carrid   TYPE scarr-carrid, 
             distid   TYPE spfli-distid, 
             distance TYPE string, 
             null     TYPE string, 
           END OF result. 
 
    DATA result TYPE TABLE OF result 
                WITH NON-UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
    SELECT FROM scarr 
             LEFT OUTER JOIN spfli 
               ON scarr~carrid = spfli~carrid 
           FIELDS scarr~carrid, 
                  distid, 
                  CASE distid 
                     WHEN 'MI' THEN 'Miles' 
                     WHEN 'KM' THEN 'Kilometers' 
                     ELSE NULL 
                  END AS distance, 
                  CASE distid 
                     WHEN 'MI' THEN NULL 
                     WHEN NULL THEN 'Kilometers' 
                     ELSE NULL 
                  END AS null 
           ORDER BY scarr~carrid 
           INTO TABLE @result. 
 
    DELETE ADJACENT DUPLICATES FROM result. 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the `SELECT` list, two [simple case distinctions](abensql_simple_case.md) are made which both explicitly specify the null expression `NULL` after `ELSE`.

- The column `distance` returns the result of all matches and if there is no match returns the null value.

- The column `null` returns an unknown result for the first comparison, which is true, and the null value for the second comparison, which is not true.

The [null value](../../abap-glossary/abennull_value_glosry.md) is converted to the type-dependent [initial value](../../abap-glossary/abeninitial_value_glosry.md) in both cases when passed to the result table.
