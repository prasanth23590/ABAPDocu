---
title: "num_func - factorial and binomial Functions"
source_file: abenfactorial_binomial_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - factorial and binomial Functions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the functions [`factorial`](abenbinomial_functions.md) and [`binomial`](abenfactorial_functions.md).

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
CLASS cl_demo_factorial_binomial DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS: get_bin_coeff_w_arithm_op 
      IMPORTING 
        n             TYPE i 
        k             TYPE i 
      RETURNING 
        VALUE(result) TYPE string. 
    METHODS: get_factorial_w_arithm_op 
      IMPORTING 
        number        TYPE i 
      RETURNING 
        VALUE(result) TYPE decfloat34. 
    METHODS: get_bin_coeff_w_cl_abap_bigint 
      IMPORTING 
        n             TYPE i 
        k             TYPE i 
      RETURNING 
        VALUE(result) TYPE string. 
    METHODS: get_factorial_w_cl_abap_bigint 
      IMPORTING 
        number        TYPE i 
      RETURNING 
        VALUE(result) TYPE REF TO cl_abap_bigint. 
    METHODS: get_bin_coeff_w_factorial_func 
      IMPORTING 
        n             TYPE i 
        k             TYPE i 
      RETURNING 
        VALUE(result) TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_factorial_binomial IMPLEMENTATION. 
  METHOD main. 
 
    DATA error TYPE REF TO cx_root. 
 
    "factorial function 
    DATA(factorial_a) = factorial( 5 ). 
    out->write( factorial_a ). 
 
    "Manually calculating the factorial 
    DATA factorial_b TYPE f. 
    factorial_b = 5 * 4 * 3 * 2 * 1. 
    ASSERT factorial_b = factorial_a. 
 
    DATA factorial_c TYPE f VALUE '1'. 
    DO 5 TIMES. 
      factorial_c *= sy-index. 
    ENDDO. 
    ASSERT factorial_c = factorial_a. 
 
    "If the result does not fit into the value range of 
    "f/decfloat34, an exception is raised. 
    TRY. 
        DATA(factorial_e) = factorial( 10000 ). 
        out->write( factorial_e ). 
      CATCH cx_sy_arithmetic_overflow INTO error. 
        out->write( error->get_text( ) ). 
    ENDTRY. 
 
    "The argument is always a non-negative integer value. 
    TRY. 
        DATA(factorial_f) = factorial( -5 ). 
        out->write( factorial_f ). 
      CATCH cx_sy_arg_out_of_domain INTO error. 
        out->write( error->get_text( ) ). 
    ENDTRY. 
 
    TRY. 
        DATA(factorial_g) = factorial( '#' ). 
        out->write( factorial_g ). 
      CATCH cx_sy_conversion_no_number INTO error. 
        out->write( error->get_text( ) ). 
    ENDTRY. 
 
    "Calculating the factorial of 0 - 20 
    TYPES: BEGIN OF factorial_struc, 
             n             TYPE i, 
             result        TYPE string, 
             result_simple TYPE string, 
           END OF factorial_struc. 
    DATA factorial_table TYPE TABLE OF factorial_struc WITH EMPTY KEY. 
    DATA counter TYPE i. 
    DO 21 TIMES. 
      DATA(factorial_result) = factorial( counter ). 
      APPEND VALUE #( 
        n             = counter 
        result        = factorial_result 
        result_simple = |{ factorial_result STYLE = SIMPLE }| 
      ) TO factorial_table. 
      counter += 1. 
    ENDDO. 
 
    out->write( factorial_table ). 
 
********************************************************************** 
 
    "binomial function 
    DATA(binomial_coefficient_a) = binomial( n = 5 k = 3 ). 
 
    out->write( binomial_coefficient_a ). 
 
    "Manually calculating the binomial coefficient 
    DATA(factorial_n) = 5 * 4 * 3 * 2 * 1. 
    DATA(factorial_k) = 3 * 2 * 1. 
    DATA(n_minus_k) = 5 - 3. 
    DATA factorial_nk TYPE i VALUE 1. 
    DO n_minus_k TIMES. 
      factorial_nk *= sy-index. 
    ENDDO. 
    DATA(binomial_coefficient_b) = 
      CONV f( factorial_n / ( factorial_k * factorial_nk ) ). 
    ASSERT binomial_coefficient_b = binomial_coefficient_a. 
 
    "Using the factorial function 
    DATA(binomial_coefficient_c) = 
      factorial( 5 ) / ( factorial( 3 ) * factorial( 5 - 3 ) ). 
    ASSERT binomial_coefficient_c = binomial_coefficient_a. 
 
    "Note the pitfalls when calculating manually, and dealing with 
    "very large results. Rounding effects in intermediate calculation 
    "results may cause imprecise final results. This is reflected in 
    "the results not calculated using the binomial function. 
    "Furthermore, special cases apply when using the binomail function 
    "and dealing with particular integer arguments. 
 
    TYPES: BEGIN OF numbers, 
             n                              TYPE i, 
             k                              TYPE i, 
             result_binomial_function       TYPE string, 
             result_binomial_function_simpl TYPE string, 
             result_calc_w_factorial_func   TYPE string, 
             result_calc_w_cl_abap_bigint   TYPE string, 
             result_calc_w_arithm_op        TYPE string, 
           END OF numbers, 
           tab_numbers TYPE TABLE OF numbers WITH EMPTY KEY. 
 
    DATA(itab) = VALUE tab_numbers( 
      ( n = 10 k = 2 ) 
      ( n = 5 k = 3 ) 
      ( n = 211 k = 4 ) 
      ( n = 15 k = 6 ) 
      ( n = 6 k = 4 ) 
      ( n = 3 k = 0 ) 
      ( n = 123 k = 45 ) 
      ( n = 654 k = 32 ) 
 
      "Special cases when using the binomial function with 
      "positive n values 
      "binomial( n = 0 k = arbitrary ) = 0 
      ( n = 0 k = 1 ) 
      "binomial( n = n k = n ) = 0 (if k < 0 or k > n) 
      ( n = 5 k = -2 ) 
      ( n = 3 k = 4 ) 
 
      "Special cases when using the binomial function with 
      "negative n values 
      "binomial( n = n k = n ) = 
      "(-1)^k * binomial( n = -n + k - 1 k = k ) if n < 0 and k >= 0 
      ( n = -5 k = 2 ) 
      "binomial( n = n k = n ) = 
      "(-1)^(n-k) * binomial( n = -k - 1 k = n - k ) if n < 0 and 
      "k <= n 
      ( n = -5 k = -8 ) 
      "binomial( n = n k = k ) = 0 if n < 0 and k > n and k < 0 
      ( n = -5 k = -3 ) 
       ). 
 
    LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
      <fs>-result_binomial_function = binomial( n = <fs>-n 
                                                k = <fs>-k ). 
      <fs>-result_binomial_function_simpl = 
        |{ binomial( n = <fs>-n k = <fs>-k ) STYLE = SIMPLE }|. 
      <fs>-result_calc_w_factorial_func = 
        get_bin_coeff_w_factorial_func( n = <fs>-n k = <fs>-k ). 
      <fs>-result_calc_w_cl_abap_bigint = 
        get_bin_coeff_w_cl_abap_bigint( n = <fs>-n k = <fs>-k ). 
      <fs>-result_calc_w_arithm_op = 
        get_bin_coeff_w_arithm_op( n = <fs>-n k = <fs>-k ). 
    ENDLOOP. 
 
    out->write( itab ). 
  ENDMETHOD. 
  METHOD get_bin_coeff_w_arithm_op. 
    TRY. 
        DATA(factor_n)  = get_factorial_w_arithm_op( n ). 
        DATA(factor_k)  = get_factorial_w_arithm_op( k ). 
        DATA(factor_nk) = get_factorial_w_arithm_op( n - k ). 
        result = factor_n / ( factor_k * factor_nk ). 
      CATCH cx_root INTO DATA(error). 
        result = error->get_text( ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD get_bin_coeff_w_cl_abap_bigint. 
    TRY. 
        DATA(factor_n)  = get_factorial_w_cl_abap_bigint( n ). 
        DATA(factor_k)  = get_factorial_w_cl_abap_bigint( k ). 
        DATA(factor_nk) = get_factorial_w_cl_abap_bigint( n - k ). 
        DATA(div) = factor_k->mul( factor_nk ). 
        result = factor_n->div_to_df34( div ). 
      CATCH cx_root INTO DATA(error). 
        result = error->get_text( ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD get_bin_coeff_w_factorial_func. 
    TRY. 
        result = 
          factorial( n ) / ( factorial( k ) * factorial( n - k ) ). 
      CATCH cx_root INTO DATA(error). 
        result = error->get_text( ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD get_factorial_w_arithm_op. 
    result = '1'. 
    DO number TIMES. 
      result = result * sy-index. 
    ENDDO. 
  ENDMETHOD. 
  METHOD get_factorial_w_cl_abap_bigint. 
    result = cl_abap_bigint=>factory_from_int4( 1 ). 
    DO number TIMES. 
      result = result->mul_int4( sy-index ). 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example includes:

- Various computations of the factorial, including the retrieval of the target's type for some examples

- Exception raising in case of improper arguments

- Various computations of the binomial coefficient, including manually computations

  - The manual computations of the binomial coefficient include various ways such as regular arithmetic operations, the use of the `fractional` function, the use of the `CL_ABAP_BIGINT` system class. The results demonstrate that the manual computation can be accurate for simple, fairly low integer arguments, but not for larger integer arguments, also due to rounding effects. It is recommended that you always use the `binomial` function.
