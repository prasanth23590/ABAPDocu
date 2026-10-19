---
title: "num_func - factorial"
source_file: abenfactorial_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - factorial, binomial"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - factorial

## Syntax

``` abap
... factorial( n ) ...  
```

## Description

The `factorial` function calculates the number of permutations of a set with `n` elements. `n` represents a positive integer or a data object convertible to a positive integer. The function is overloaded so that the return value can have the types `f` and `decfloat34`.

In mathematics, the factorial is represented as *n!*. The calculation pattern is: `n! = n * (n - 1) * (n - 2) * (n - 3) * ...`. For example, the factorial of 7 is 5040: `7! = 7 * 6 * 5 * 4 * 3 * 2 * 1.`

## Hints

- Rounding may occur. If the result fits to the types `i` or `int8`, it is assigned accurately. Otherwise, it is rounded to the last digit following the [rules](abenarith_type.md) for the types `f`, `decfloat16`, or `decfloat34`.

- The factorial of 0 is 1.

- The maximum integer values for `n` are: 170 for type `f` as resulting type, 2123 for `decfloat34`.

- In arithmetic operations involving the function and other operands, the resulting type is determined by the operand with the largest value range.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

- The function requires a positive integer or a value convertible to a positive integer. Passing negative integers raises the `CX_SY_ARG_OUT_OF_DOMAIN` exception.

- If the argument produces a result too large for the types `f`, `decfloat16`, or `decfloat34`, the `CX_SY_ARITHMETIC_OVERFLOW` exception occurs.

- If the argument cannot be converted to type `i`, the `CX_SY_CONVERSION_NO_NUMBER` exception is raised.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example computes the factorial of 0 to 20.

``` abap
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
 
cl_demo_output=>new( )->display( factorial_table ).
```

## Executable Example

[`num_func` - `factorial` and `binomial` Functions](abenfactorial_binomial_abexa.md)
