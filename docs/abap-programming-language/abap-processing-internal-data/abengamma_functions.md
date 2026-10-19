---
title: "num_func - gamma, log_gamma"
source_file: abengamma_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - gamma, log_gamma

## Syntax

``` abap
... gamma( arg ) ... 
... log_gamma( arg ) ...  
```

## Description

`gamma` and `log_gamma` are the [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) gamma function and log gamma function. The gamma function is the transcendental analog of the factorial, that is, `gamma(m) = (m-1)!`, but it is defined for all real numbers except 0 and negative integers. The log gamma function is defined as `log_gamma( z ) = log( abs ( gamma( z ) )`. Both functions expect a numeric value as single argument (`arg`), which can be a single data object outside an arithmetic expression or an arithmetic expression itself.

| **Function** | **Meaning**        | **Domain**                                                    |
|--------------|--------------------|---------------------------------------------------------------|
| `gamma`      | Gamma function     | All real numbers except 0 and negative integers {-1, -2, ...} |
| `log_gamma`  | Log gamma function | All real numbers except 0 and negative integers {-1, -2, ...} |

The following applies to the [floating point arithmetic](../../abap-glossary/abenfloating_point_arith_glosry.md) in which a floating point function is calculated, and to the data type of the return value:

- If the argument has the type `decfloat16` or `decfloat34`, a floating point function is calculated in decimal floating point arithmetic and the return value has the type `decfloat34`.

- If a floating point function is used in an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) whose [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is `decfloat34`, or that contains a [numeric expression](../../abap-glossary/abennumerical_expression_glosry.md) of type `decfloat34` as an argument, it also calculates a return value with the type `decfloat34` and the argument is first converted to the data type `decfloat34`, if necessary.

- In all other cases, floating point functions use binary floating point arithmetic to calculate a return value with type `f` and the argument is first converted to the data type `f`, if necessary.

The functions are overloaded, returning values of types `f` or `decfloat34`. `arg` is implicitly converted to either `f` or `decfloat34`.

The following catchable exceptions can be raised during function calculation:

- If `arg` cannot be converted to a numeric value, the exception `CX_SY_CONVERSION_NO_NUMBER` is raised.

- The `gamma` and the `log_gamma` functions have poles at 0 and negative integers. Therefore, if the poles are used as arguments for the functions (for example, `gamma( -1&#x00A0;)`), the exception `CX_SY_ARG_OUT_OF_DOMAIN` is raised (runtime error: `COMPUTE_GAMMA_DOMAIN`).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example below demonstrates a simple use of the gamma function, including a catchable exception at the pole -4. It also shows that for non-integers, the gamma function can return `decfloat` values, unlike the factorial function, which only returns integers.

``` abap
DATA: 
  d34n          TYPE decfloat34 VALUE '1.5', 
  pos_integer   TYPE i VALUE '4', 
  neg_integer   TYPE i VALUE '-4', 
  pi            TYPE decfloat34 VALUE '3.14159265358979323846'. 
 
DATA(gamma_result1) = gamma( d34n ). 
DATA(log_gamma_result1) = log_gamma( d34n ). 
 
"Exception caught at pole -4 
TRY. 
  DATA(gamma_result2) = gamma( neg_integer ). 
  DATA(log_gamma_result2) = log_gamma( neg_integer ). 
  CATCH  cx_sy_arg_out_of_domain. 
ENDTRY. 
 
"Comparison to factorial (m-1)! for integers and non-integers 
"Identical for integers > 0 
DATA(factorial_int) = factorial( pos_integer - 1 ). 
DATA(gamma_result3) = gamma( pos_integer ). 
 
DATA(factorial_pi) = factorial( pi - 1 ). 
DATA(gamma_result4) = gamma( pi ).
```
