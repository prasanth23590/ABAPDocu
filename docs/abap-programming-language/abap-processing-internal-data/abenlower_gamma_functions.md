---
title: "num_func - gamma_lower"
source_file: abenlower_gamma_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - gamma_lower

## Syntax

``` abap
... gamma_lower( arg = expr limit = expr [ inverse = const_abap_bool   normalized = const_abap_bool ] )  
```

## Description

`gamma_lower` is the [Built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) lower incomplete gamma function. The incomplete gamma functions are important in statistics. For example, they serve as the cumulative distribution function of the gamma or chi-squared distribution. For statistical applications, the normalized version of the lower incomplete gamma function is used.

The lower incomplete gamma function is defined as an integral from zero to a variable upper limit. Therefore, it expects a [floating point number](../../abap-glossary/abenfloating_point_number_glosry.md) as an argument (`arg`) and a floating point number as an integration limit (`lim`). The argument of a lower incomplete gamma function must be a single data object outside an arithmetic expression. It can also be an arithmetic expression itself within an arithmetic expression. The values for `arg` must be positive real numbers; the values for `limit` must be real numbers equal or higher than zero.

The following parameters are optional:

- `normalized`: If set to `abap_true,` the regularized lower incomplete gamma function is calculated as follows:

  `gamma_lower( normalized = abap_true ) = gamma_lower( normalized = abap_false ) / gamma(arg).`

- `inverse`: If set to `abap_true`, the inverse of the lower incomplete gamma function is calculated using the limit as argument.

  If `inverse` is set to `abap_true`, `normalized` must also be set to `abap_true`. If parameter `inverse` is set to `abap_true`, the value of `limit` must be in the half-open range between 0 and 1 (excluding 1).

The function is overloaded, so that the return value can have the type `decfloat34` or `f`.

The following applies to the [floating point arithmetic](../../abap-glossary/abenfloating_point_arith_glosry.md) in which a floating point function is calculated, and to the data type of the return value:

- If the argument has the type `decfloat16` or `decfloat34`, a floating point function is calculated in decimal floating point arithmetic and the return value has the type `decfloat34`.

- If a floating point function is used in an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) whose [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is `decfloat34`, or that contains a [numeric expression](../../abap-glossary/abennumerical_expression_glosry.md) of type `decfloat34` as an argument, it also calculates a return value with the type `decfloat34` and the argument is first converted to the data type `decfloat34`, if necessary.

- In all other cases, floating point functions use binary floating point arithmetic to calculate a return value with type `f` and the argument is first converted to the data type `f`, if necessary.

The following catchable exceptions can be raised during function calculation:

- If `arg` cannot be converted to a numeric value, the exception `CX_SY_CONVERSION_NO_NUMBER` can be raised.

- If the values of `arg` or `limit` are outside the domain of the function, a catchable exception of the class `CX_SY_ARG_OUT_OF_DOMAIN` is raised (runtime error `COMPUTE_GAMMA_LOWER_DOMAIN`).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example illustrates the use of the `gamma_lower` function and its inverse.

``` abap
DATA: 
 arg1 TYPE decfloat34 VALUE '10.1', 
 lim1 TYPE decfloat34 VALUE '15.11', 
 arg2 TYPE decfloat34 VALUE '-10.1', 
 lim2 TYPE decfloat34 VALUE '0.5'. 
 
"Lower incomplete gamma function 
DATA(gamma_low1) = gamma_lower( arg = arg1 limit = lim1 ). 
 
"Exception caught at negative value 
TRY. 
  DATA(gamma_low2) = gamma_lower( arg = arg2 limit = lim1 ). 
  CATCH cx_sy_arg_out_of_domain. 
ENDTRY. 
 
"Inverse lower incomplete gamma function 
DATA(gamma_low3) = 
gamma_lower( arg = arg1 limit = lim2 
      normalized = abap_true inverse = abap_true ).
```
