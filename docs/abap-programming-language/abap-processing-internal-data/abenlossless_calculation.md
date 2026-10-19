---
title: "arith_exp - Lossless Calculations"
source_file: abenlossless_calculation.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Arithmetic Expressions (arith_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# arith_exp - Lossless Calculations

A [lossless calculation](../../abap-glossary/abenlossless_calculation_glosry.md) is a calculation of an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) in which no roundings occur. Lossless calculations can be performed using the [lossless operator `EXACT`](abenconstructor_expression_exact.md):

## Syntax

``` abap
... EXACT type( arith_exp ) ...  .
```

## Description

If the operand of the operator `EXACT` is an arithmetic expression, the data type specified by `type` must not be of type `f`. `arith_exp` must be an arithmetic expression simplified as follows:

- The allowed [arithmetic operators](../../abap-glossary/abenarithmetic_operator_glosry.md) are `+`, `-`, `*`, and `/`. The operators `DIV`, `MOD`, and `**` cannot be used.

- The allowed [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md) are `abs`, `sign`, `ceil`, `floor`, `trunc`, `frac`, `round`, and `rescale`. These functions do not raise the exception `CX_SY_CONVERSION_ROUNDING`. No other built-in functions can be specified because their results are not lossless in principle.

- No operands of data type `x` and `xstring` can be specified.

- No [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) can be specified, since the requirement for losslessness cannot be applied to the method execution.

- Operands of the type `f` (binary floating point numbers) are not allowed because they cannot represent every decimal number precisely, due to their internal representation.

The operator `EXACT` ensures that a simplified expression with the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `decfloat34` is calculated and checks whether roundings are performed. If no roundings occur, the result is assigned to the return value. If necessary, the result is converted from `decfloat34` to the data type determined by `type`. If a rounding is required by the calculation, the exception `CX_SY_CONVERSION_ROUNDING` is raised. Rounding can occur when operands are converted to the calculation type, during the calculation, or when the result is converted to the target field.

The exception is raised when the first subexpression that requires a rounding is calculated. If the exception is handled, the exception object in the `VALUE` attribute contains the result of a regular calculation. The attribute `OPERATION` contains the first operation that had to be rounded, whereby conversions are represented by *:=*.

## Hints

- If the operand of the operator `EXACT` is not an arithmetic expression, the operator performs a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md).

- Since the first calculation in lossless calculations that requires rounding raises an exception, the behavior in arithmetic expressions that are mathematically identical but constructed in different ways can be different.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second arithmetic expression raises an exception, since it requires rounding to two decimal places.

``` abap
TYPES pack TYPE p LENGTH 8 DECIMALS 2. 
 
FINAL(result1) = EXACT pack( 1 / 4 ). 
 
FINAL(result2) = EXACT pack( 1 / 3 ).
```

## Executable Example

[Lossless Calculations](abencompute_exact_abexa.md)

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_TYPE_NOT_EXACT`

- *Cause:* Invalid operand type for lossless calculations

  *Runtime error:* `UNCAUGHT_EXCEPTION`

`CX_SY_CONVERSION_ROUNDING`

- *Cause:* Rounding in a lossless calculation

  *Runtime error:* `UNCAUGHT_EXCEPTION`
