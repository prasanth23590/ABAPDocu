---
title: "num_func - binomial"
source_file: abenbinomial_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - factorial, binomial"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - binomial

## Syntax

``` abap
... binomial( n = i k = j ) ...  
```

## Description

The `binomial` function represents the number of possible `k` element subsets of a set with `n` elements, thus calculating the binomial coefficient. `i` and `j` represent 4-byte integer values or data objects convertible to type `i`, passed as arguments. They can be positive or negative.

The function is overloaded so that the return value can have the types `f` and `decfloat34`.

The calculation pattern may be expressed as `i! / ( j! * ( i - j )! )`. For example, the binomial coefficient of 10 (argument for `n`) and 2 (argument for `k`) is 45.

The following special cases apply:

- Positive argument for `n`:

  - `binomial( n = 0 k = any_value )` yields 0

  - `binomial( n = i k = j )` yields 0 if j \< 0 or j \> i

- Negative argument for `n`:

  - `binomial( n = i k = j )` computes `-1 ^ j * binomial( n = -i + j - 1 k = j )` if i \< 0 and j \>= 0

  - `binomial( n = i k = j )` computes `-1 ^ ( i - j ) * binomial( n = -j - 1 k = i - j )` if i \< 0 and j \<= i

  - `binomial( n = i k = j )` yields 0 if i \< 0 and j \> i and j \< 0

## Hints

- The order of the argument specification is not fixed.

- Rounding may occur. If the result fits to the types `i` or `int8`, it is assigned accurately. Otherwise, it is rounded to the last digit following the [rules](abenarith_type.md) for the types `f`, `decfloat16`, or `decfloat34`.

- Besides precision and potential overflows, using the function has a performance advantage over manual calculation.

- In arithmetic operations involving the function and other operands, the resulting type is determined by the operand with the largest value range.

- The function performs the calculation internally without computing the factorial individually, but rather uses the mathematical beta function. This allows for the function to determine the binomial coefficient even if the result is very large. The example `DATA(calc_bin_coeff) = CONV decfloat34( binomial( n = 20000000 k = 1298 ) ).` yields `2.796321303970816355690410266166715E+5997`.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

- If the argument produces a result too large for the types `f`, `decfloat16`, or `decfloat34`, the `CX_SY_ARITHMETIC_OVERFLOW` exception occurs.

- If the argument cannot be converted to type `i`, the `CX_SY_CONVERSION_NO_NUMBER` exception is raised.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example computes the binomial coefficient of various integer values passed as arguments.

``` abap
TYPES: BEGIN OF bin_coeff_struc, 
         n             TYPE i, 
         k             TYPE i, 
         result        TYPE string, 
         result_simple TYPE string, 
       END OF bin_coeff_struc. 
DATA bin_coeff_table TYPE TABLE OF bin_coeff_struc WITH EMPTY KEY. 
DATA n_value TYPE i VALUE 21. 
DATA k_value TYPE i VALUE 11. 
DO 10 TIMES. 
  n_value -= 1. 
  k_value -= 1. 
  DATA(binomial_coefficient) = binomial( n = n_value k = k_value ). 
  APPEND VALUE #( 
    n             = n_value 
    k             = k_value 
    result        = binomial_coefficient 
    result_simple = |{ binomial_coefficient STYLE = SIMPLE }| 
  ) TO bin_coeff_table. 
ENDDO. 
 
cl_demo_output=>new( )->display( bin_coeff_table ).
```

## Executable Example

[`num_func` - `factorial` and `binomial` Functions](abenfactorial_binomial_abexa.md)
