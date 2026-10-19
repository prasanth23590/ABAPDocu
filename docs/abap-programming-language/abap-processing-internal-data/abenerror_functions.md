---
title: "num_func - erf, erfc, erf_inv, erfc_inv"
source_file: abenerror_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - erf, erfc, erf_inv, erfc_inv

## Syntax

``` abap
... erf( arg ) ... 
... erfc( arg ) ... 
... erf_inv( arg ) ... 
... erfc_inv( arg ) ...  
```

## Description

[Built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) arithmetic functions for calculating the error function, complementary error function, and their inverses. These functions are typically used in statistics and probability theory. The functions expect a numeric value as single argument (`arg`), which can be a single data object outside an arithmetic expression or an arithmetic expression itself. They are overloaded functions, returning values of types `f` or `decfloat34`. `arg` is implicitly converted to `f` or `decfloat34`.

| **Function** | **Meaning**                                                                          | **Definition Range**                                         |
|--------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `erf`        | (Gauss) error function, which is the probability function of the normal distribution | All real numbers                                             |
| `erfc`       | Complementary error function                                                         | All real numbers; defined as `erfc( arg ) = 1 - erf( arg ).` |
| `erf_inv`    | Inverse error function                                                               | -1 \< `arg` \< 1                                             |
| `erfc_inv`   | Inverse complementary error function                                                 | 0 \< `arg` \< 2                                              |

The following applies to the [floating point arithmetic](../../abap-glossary/abenfloating_point_arith_glosry.md) in which a floating point function is calculated, and to the data type of the return value:

- If the argument has the type `decfloat16` or `decfloat34`, a floating point function is calculated in decimal floating point arithmetic and the return value has the type `decfloat34`.

- If a floating point function is used in an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) whose [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is `decfloat34`, or that contains a [numeric expression](../../abap-glossary/abennumerical_expression_glosry.md) of type `decfloat34` as an argument, it also calculates a return value with the type `decfloat34` and the argument is first converted to the data type `decfloat34`, if necessary.

- In all other cases, floating point functions use binary floating point arithmetic to calculate a return value with type `f` and the argument is first converted to the data type `f`, if necessary.

## Hints

- If `arg` cannot be converted to a numeric value, the exception `CX_SY_CONVERSION_NO_NUMBER` is raised.

- If `arg` is outside of the definition range, the exception `CX_SY_ARG_OUT_OF_DOMAIN` is raised.

- When the poles are used as arguments for `erf_inv` or `erfc_inv`, for example, `erf_inv( 1&#x00A0;)`, then the exception `CX_SY_ARITHMETIC_OVERFLOW` is raised.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates a loop that performs calculations using error functions in each iteration. It constructs a value table by adding calculation results or exceptions raised.

``` abap
TYPES: BEGIN OF erf_struc, 
             value    TYPE string, 
             erf      TYPE string, 
             erfc     TYPE string, 
             erf_inv  TYPE string, 
             erfc_inv TYPE string, 
           END OF erf_struc, 
           erf_tab_type TYPE TABLE OF erf_struc WITH EMPTY KEY. 
 
    DATA(num) = CONV decfloat34( '-2.5' ). 
    DATA(max) = CONV decfloat34( '2.5' ). 
    DATA erf_tab TYPE erf_tab_type. 
    DATA err type ref to cx_root. 
    WHILE num <= max. 
 
      APPEND VALUE #( value = num ) 
       TO erf_tab REFERENCE INTO DATA(erf_ref). 
 
      TRY. 
          DATA(erf) = erf( num ). 
          erf_ref->erf = erf. 
        CATCH cx_sy_arithmetic_overflow 
              cx_sy_arg_out_of_domain INTO err. 
          erf_ref->erf = |Exception { 
          cl_abap_typedescr=>describe_by_object_ref( 
          err )->get_relative_name( ) } raised|. 
      ENDTRY. 
 
      TRY. 
          DATA(erfc) = erfc( num ). 
          erf_ref->erfc = erfc. 
        CATCH cx_sy_arithmetic_overflow 
              cx_sy_arg_out_of_domain INTO err. 
          erf_ref->erfc = |Exception { 
            cl_abap_typedescr=>describe_by_object_ref( 
            err )->get_relative_name( ) } raised|. 
      ENDTRY. 
 
      TRY. 
          DATA(erf_inv) = erf_inv( num ). 
          erf_ref->erf_inv = erf_inv. 
        CATCH cx_sy_arithmetic_overflow 
              cx_sy_arg_out_of_domain INTO err. 
          erf_ref->erf_inv = |Exception { 
          cl_abap_typedescr=>describe_by_object_ref( 
          err )->get_relative_name( ) } raised|. 
      ENDTRY. 
 
      TRY. 
          DATA(erfc_inv) = erfc_inv( num ). 
          erf_ref->erfc_inv = erfc_inv. 
        CATCH cx_sy_arithmetic_overflow 
              cx_sy_arg_out_of_domain INTO err. 
          erf_ref->erfc_inv = |Exception { 
          cl_abap_typedescr=>describe_by_object_ref( 
          err )->get_relative_name( ) } raised|. 
      ENDTRY. 
 
      num += CONV decfloat34( '0.1' ). 
 
    ENDWHILE. 
 
    FINAL(out) = cl_demo_output=>new( ). 
    out->write( erf_tab ). 
    out->display( ).
```
