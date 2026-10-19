---
title: "num_func - abs, sign, ceil, floor, trunc, frac"
source_file: abennumerical_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - abs, sign, ceil, floor, trunc, frac

## Syntax

``` abap
... num_func( arg ) ...  
```

## Description

General [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) numeric functions with exactly one unnamed parameter for an argument with any numeric data type. These functions are overloaded with the effect that the return value can have different numeric types. The argument of a general numeric function must be a single data object outside an arithmetic expression, and can itself be a numeric expression within an arithmetic expression.

The following table shows the general numeric functions and how they work.

| **Function num_func** | **Return Value**                                                                                                                   |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `abs`                 | Absolute value of argument `arg`                                                                                                   |
| `sign`                | Sign of argument `arg`: -1, if the value of `arg` is negative; 0, if the value of `arg` is 0; 1, if the value of `arg` is positive |
| `ceil`                | Smallest integer that is not less than the value of the argument `arg`                                                             |
| `floor`               | Largest integer that is not greater than the value of the argument `arg`                                                           |
| `trunc`               | Value of the integer part of the argument `arg`; negative if `arg` is negative                                                     |
| `frac`                | Value of the [decimal places](../../abap-glossary/abendecimal_place_glosry.md) of the argument `arg`; negative if `arg` is negative                  |

The following applies to the data type of the return value:

- Outside of an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md), the data type of the argument determines the data type of the return value.

- Within an arithmetic expression, the argument of the function contributes to the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of the entire expression and the function is calculated using the calculation type. If the argument itself is an arithmetic expression, its operands contribute to the entire calculation type and the argument is also calculated with this type.

- If the argument `arg` is a [numeric expression](../../abap-glossary/abennumerical_expression_glosry.md), the function works like an arithmetic operator and it is handled in its operand position like an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md).

If the argument of a numeric function outside of an arithmetic expression does not have a numeric data type `i`, `int8`, `p`, `decfloat16`, `decfloat34`, or `f`, its data type determines the type of return value as follows:

- `d` and `t` give` i`

- `c`, `n` and `string` give` p`

- `x` and `xstring` give`i`

- `utclong` is not allowed

Before the calculation of the function, the argument is [converted](abenconversion_rules.md) to the corresponding type.

## Hints

- The time stamp type `utclong` cannot be converted implicitly to a numeric type, and therefore cannot be specified directly as an argument.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following assertion should always be correct.

``` abap
DATA pack TYPE p LENGTH 8 DECIMALS 4 VALUE '-1234.5678'. 
cl_demo_input=>request( CHANGING field = pack ). 
 
ASSERT pack  = trunc( pack ) + frac( pack ).
```

## Executable Example

[Numeric Functions](abenmath_func_abexa.md)
