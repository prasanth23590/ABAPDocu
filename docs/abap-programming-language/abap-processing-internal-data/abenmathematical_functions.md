---
title: "Numeric Functions (num_func)"
source_file: abenmathematical_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Numeric Functions (num_func)

Numeric functions are a type of [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md). The main argument of a numeric function must represent a numeric value. The data type of the return value is determined either by the argument of the function (overloaded functions) or by the function.

Outside of an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md), the main argument of a numeric function must be a single numeric data object. Within an arithmetic expression, the following are possible as main arguments of a numeric function:

- [Numeric data object](../../abap-glossary/abennumeric_data_object_glosry.md)

- [Arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md)

- [Built-in function](../../abap-glossary/abenbuiltin_function_glosry.md)

- [Functional method](../../abap-glossary/abenfunctional_method_glosry.md)

The following functions are available:

| **Function**                                     | **Meaning**                                                                          |
|--------------------------------------------------|--------------------------------------------------------------------------------------|
| [`abs`](abennumerical_functions.md)            | Absolute value                                                                       |
| [`acos`](abenfloating_point_functions.md)      | Arccosine                                                                            |
| [`asin`](abenfloating_point_functions.md)      | Arcsine                                                                              |
| [`atan`](abenfloating_point_functions.md)      | Arctangent                                                                           |
| [`binomial`](abenbinomial_functions.md)        | Computes the binomial coefficient                                                    |
| [`ceil`](abennumerical_functions.md)           | Smallest integer not less than the argument                                          |
| [`cos`](abenfloating_point_functions.md)       | Cosine                                                                               |
| [`cosh`](abenfloating_point_functions.md)      | Hyperbolic cosine                                                                    |
| [`erf`](abenerror_functions.md)                | (Gauss) error function, which is the probability function of the normal distribution |
| [`erfc`](abenerror_functions.md)               | Complementary error function                                                         |
| [`erf_inv`](abenerror_functions.md)            | Inverse error function                                                               |
| [`erfc_inv`](abenerror_functions.md)           | Inverse complementary error function                                                 |
| [`exp`](abenfloating_point_functions.md)       | Exponential function for base e                                                      |
| [`factorial`](abenfactorial_functions.md)      | Computes the factorial                                                               |
| [`floor`](abennumerical_functions.md)          | Largest integer not greater than an argument                                         |
| [`frac`](abennumerical_functions.md)           | Value of decimal places of an argument                                               |
| [`gamma`](abengamma_functions.md)              | Gamma function                                                                       |
| [`gamma_lower`](abenlower_gamma_functions.md)  | Lower incomplete gamma function                                                      |
| [`ipow`](abenpower_function.md)                | Power function                                                                       |
| [`log`](abenfloating_point_functions.md)       | Natural logarithm                                                                    |
| [`log10`](abenfloating_point_functions.md)     | Logarithm to base 10                                                                 |
| [`log_gamma`](abengamma_functions.md)          | Log gamma function                                                                   |
| [`nmax`](abennmax_nmin_functions.md)           | Returns the value of the largest of the passed arguments                             |
| [`nmin`](abennmax_nmin_functions.md)           | Returns the value of the smallest of the passed arguments                            |
| [`rescale`](abendec_floating_point_rescale.md) | Rescaling function                                                                   |
| [`round`](abendec_floating_point_round.md)     | Rounding function                                                                    |
| [`sign`](abennumerical_functions.md)           | Sign of an argument                                                                  |
| [`sin`](abenfloating_point_functions.md)       | Sine                                                                                 |
| [`sinh`](abenfloating_point_functions.md)      | Hyperbolic sine                                                                      |
| [`sqrt`](abenfloating_point_functions.md)      | Square root                                                                          |
| [`tan`](abenfloating_point_functions.md)       | Tangent                                                                              |
| [`tanh`](abenfloating_point_functions.md)      | Hyperbolic tangent                                                                   |
| [`trunc`](abennumerical_functions.md)          | Value of the integer part of an argument                                             |

**Catchable Exceptions**

The catchable exceptions that can be raised during the calculation of a numeric function are subclasses of the classes CX_SY_ARITHMETIC_ERROR and CX_SY_CONVERSION_ERROR.
