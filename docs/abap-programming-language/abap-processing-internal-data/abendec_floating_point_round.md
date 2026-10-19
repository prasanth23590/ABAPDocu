---
title: "num_func - round"
source_file: abendec_floating_point_round.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - round, rescale"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - round

## Syntax

``` abap
... round( val = arg {dec = n}|{prec = n} [mode = m] ) ...  
```

## Description

The rounding function `round` can be implemented in [operand positions](../abap-operands/abenoperands_expressions.md) using the syntax above. This function rounds a decimal floating point number specified as an argument for the parameter `val`. A data object specified for `arg` is converted to the data type `decfloat34` before the function is executed, if necessary.

Either the parameter `dec` or the parameter `prec` must be given a value, and rounding must be to either a particular number of decimal places or to a [precision](../../abap-glossary/abenprecision_glosry.md):

- If the parameter `dec` is given a value, the input value is rounded to the number of decimal places specified in `n` and returned. `n` expects data objects of the type `i` whose value must not be less than -6144. If a negative value is specified, the corresponding pre-decimal place is rounded.

- If the parameter `prec` is given a value, the value entered is rounded to the [precision](../../abap-glossary/abenprecision_glosry.md) specified in `n` and returned. `n` expects data objects of the type `i` whose value must be greater than 0.

A rounding can reduce [scaling](../../abap-glossary/abenscale_glosry.md) and [precision](../../abap-glossary/abenprecision_glosry.md) but cannot increase them. If `dec` is specified, the mantissa of the return value does not contain any zeros after the place where the rounding applies. If `prec` is specified, the input value is returned unchanged if the specified precision is greater than or equal to the input value.

The optional parameter `mode` determines the rounding type. For `m` it is only possible to specify values that exist as `ROUND_...` constants in class `CL_ABAP_MATH`. The following table shows the possible rounding rules. If `mode` is not given a value, commercial rounding is used.

| **Constant**      | **Rounding rule**                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ROUND_HALF_UP`   | The value is rounded to the nearest rounded value. If the value falls exactly halfway between two rounded values, it is rounded away from zero (commercial rounding).                 |
| `ROUND_HALF_DOWN` | The value is rounded to the nearest rounded value. If the value falls exactly halfway between two round values, it is rounded towards zero.                                           |
| `ROUND_HALF_EVEN` | The value is rounded to the nearest rounded value. If the value falls exactly halfway between two rounded values, it is rounded to the value whose rightmost digit is an even number. |
| `ROUND_UP`        | The value is rounded away from zero or towards the greater absolute value.                                                                                                            |
| `ROUND_DOWN`      | The value is rounded towards zero or towards the lesser absolute value.                                                                                                               |
| `ROUND_CEILING`   | The value is rounded towards positive infinity or towards the greater value.                                                                                                          |
| `ROUND_FLOOR`     | The value is rounded towards negative infinity or towards the lower value.                                                                                                            |

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following tables show the results of commercial rounding of the decimal floating point number `1234.56789` (scaling 5, precision 9) with different values for `dec` and `prec`. The shown results shown are created by executing the class `CL_DEMO_ROUND_AND_RESCALE`.

| **`dec`** | **Result**   | **Scaling** | **Precision** |
|-----------|--------------|-------------|---------------|
| `-5`      | `0E+5`       | `-5`        | `1`           |
| `-4`      | `0E+4`       | `-4`        | `1`           |
| `-3`      | `1E+3`       | `-3`        | `1`           |
| `-2`      | `1.2E+3`     | `-2`        | `2`           |
| `-1`      | `1.23E+3`    | `-1`        | `3`           |
| `0`       | `1235`       | `0`         | `4`           |
| `1`       | `1234.6`     | `1`         | `5`           |
| `2`       | `1234.57`    | `2`         | `6`           |
| `3`       | `1234.568`   | `3`         | `7`           |
| `4`       | `1234.5679`  | `4`         | `8`           |
| `5`       | `1234.56789` | `5`         | `9`           |
| `6`       | `1234.56789` | `5`         | `9`           |
| `prec`    | **Result**   | **Scaling** | **Precision** |
| `1`       | `1E+3`       | `-3`        | `1`           |
| `2`       | `1.2E+3`     | `-2`        | `2`           |
| `3`       | `1.23E+3`    | `-1`        | `3`           |
| `4`       | `1235`       | `0`         | `4`           |
| `5`       | `1234.6`     | `1`         | `5`           |
| `6`       | `1234.57`    | `2`         | `6`           |
| `7`       | `1234.568`   | `3`         | `7`           |
| `8`       | `1234.5679`  | `4`         | `8`           |
| `9`       | `1234.56789` | `5`         | `9`           |
| `10`      | `1234.56789` | `5`         | `9`           |

## Executable Example

[Rounding Function `round`](abenround_function_abexa.md)
