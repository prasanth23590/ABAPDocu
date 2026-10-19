---
title: "sql_agg - Aggregate Function ALLOW_PRECISION_LOSS"
source_file: abensql_expr_aggr_prec_loss_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_agg > sql_agg - Examples of Aggregate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_agg - Aggregate Function ALLOW_PRECISION_LOSS

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [aggregate function](abensql_agg_func.md) `ALLOW_PRECISION_LOSS`.

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
CLASS cl_demo_allow_precision_loss DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_allow_precision_loss IMPLEMENTATION. 
  METHOD main. 
 
    TYPES result_type TYPE p LENGTH 6 DECIMALS 2. 
    DATA: allow_precision_loss_result TYPE result_type, 
          normal_sum_result           TYPE result_type. 
 
    DELETE FROM demo_expressions.                       "#EC CI_NOWHERE 
    INSERT demo_expressions FROM TABLE @( 
      VALUE #( ( id = 'X' dec2 = '2.119999' ) 
               ( id = 'Y' dec2 = '2.118888' ) 
               ( id = 'A' dec2 = '1.13999' ) 
               ( id = 'Z' dec2 = '2.668888' ) 
      ) ). 
 
    SELECT SUM( CAST( dec2 AS DEC( 10,2 ) ) ) AS sum1 
    FROM demo_expressions INTO @normal_sum_result. 
 
    SELECT allow_precision_loss( SUM( CAST( dec2 AS DEC( 10,2 ) ) ) ) 
           AS sum1 
    FROM demo_expressions INTO @allow_precision_loss_result. 
 
    out->write_data( allow_precision_loss_result ). 
    out->write_data( normal_sum_result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Sums up decimal values with five or more decimal places and converts them to a decimal number with two decimal places. The result of the aggregate expression differs when using `ALLOW_PRECISION_LOSS`.

In this example, `ALLOW_PRECISION_LOSS` first sums up all decimals and then converts them, which is why it performs fewer operations. Without `ALLOW_PRECISION_LOSS`, each decimal is converted individually and then added up.
