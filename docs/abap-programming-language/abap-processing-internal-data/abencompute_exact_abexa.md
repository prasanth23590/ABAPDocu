---
title: "arith_exp - Lossless Calculations"
source_file: abencompute_exact_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Arithmetic Expressions (arith_exp) > arith_exp - Lossless Calculations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# arith_exp - Lossless Calculations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates [lossless calculations](../../abap-glossary/abenlossless_calculation_glosry.md) and the exceptions raised when roundings occur.

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
CLASS cl_demo_compute_exact DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: 
      BEGIN OF o, 
        div     TYPE string, 
        result1 TYPE string, 
        flag1   TYPE string, 
        result2 TYPE string, 
        flag2   TYPE string, 
      END OF o, 
      output LIKE TABLE OF o. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_compute_exact IMPLEMENTATION. 
  METHOD main. 
    DATA: number TYPE i VALUE 3, 
          result TYPE decfloat34, 
          exc    TYPE REF TO  cx_sy_conversion_rounding. 
 
    cl_demo_input=>new( )->request( CHANGING field = number ). 
 
    out->begin_section( 
      |{ number } / div vs. { number } * ( 1 / div )| ). 
 
    DO 100 TIMES. 
      APPEND INITIAL LINE TO output. 
      output[ sy-index ]-div = sy-index. 
      TRY. 
          result = EXACT #( number / sy-index ). 
          output[ sy-index ]-result1 = result. 
          output[ sy-index ]-flag1   = `X`. 
        CATCH cx_sy_conversion_rounding INTO exc. 
          output[ sy-index ]-result1 = exc->value. 
          output[ sy-index ]-flag1   = ` `. 
      ENDTRY. 
      TRY. 
          result = EXACT #( number * ( 1 / sy-index ) ). 
          output[ sy-index ]-result2 = result. 
          output[ sy-index ]-flag2   = `X`. 
        CATCH cx_sy_conversion_rounding INTO exc. 
          output[ sy-index ]-result2 = exc->value. 
          output[ sy-index ]-flag2   = ` `. 
      ENDTRY. 
    ENDDO. 
    out->write( output ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The lossless operator [`EXACT`](abenconstructor_expression_exact.md) is used to perform the following calculations and to assign the result to a data object with the type `decfloat34`:

`result = number / sy-index`

`result = number * ( 1 / sy-index )`

If rounding is not needed, the result `result` is produced. If roundings are needed, the associated exception `CX_SY_CONVERSION_ROUNDING` is caught, and its attribute `VALUE` is displayed. The results of lossless calculations are flagged in the display.

This example demonstrates how the structure of an arithmetic expression can affect the result of a lossless calculation. For example, the division of the number `number` by itself is always a lossless calculation. Multiplying `number` by `1 / number`, however, raises an exception when a rounding occurs in the division.

The following two expressions are further examples of the affect the structure has on an arithmetic expression:

`result = number * 1 / sy-index`

`result = 1 / sy-index * number`

The first expression has an effect like `number / sy-index` and the second like `number * ( 1 / sy-index )`.
