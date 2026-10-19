---
title: "num_func - ipow"
source_file: abenpower_function.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - ipow

## Syntax

``` abap
... ipow( base = arg exp = n ) ...  
```

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) raises the argument `arg` passed to `base` to the exponent `n` passed to `exp`. The arguments `arg` and `n` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md). Any [numeric data object](../../abap-glossary/abennumeric_data_object_glosry.md) can be specified for `arg`. `n` expects the type `i` and exponents of other types are [converted](abenconversion_elementary.md) to `i`. If the argument `arg` has the value 0, the value of the exponent `n` must be greater than or equal to 0.

The function `ipow` is overloaded in such a way that the return value can have different numeric types.

- Outside of an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md), the data type of the argument `arg` determines the data type of the return value.

- Within an arithmetic expression, the argument `arg` contributes to the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of the entire expression and the function is calculated using the calculation type.

- If the argument `arg` is a [numeric expression](../../abap-glossary/abennumerical_expression_glosry.md), `ipow` works like an arithmetic operator and the function is handled in its operand position like an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md).

This function can be specified in [general](../../abap-glossary/abengeneral_expr_position_glosry.md) and [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md). The calculation type is determined from the argument `arg` in the same way as with the other [numeric functions](abennumerical_functions.md). The argument `n` does not have any effect on the data type of the return value.

## Hints

- The power function `ipow` can replace [`arg ** n`](abenarith_operators.md) calculations, if the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `f` is to be avoided. This makes sense if the type `f` is not precise enough.

- In many cases, the power function `ipow` has better performance than using the arithmetic operator [`**`](abenarith_operators.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The results are `1.4399999999999999` for `**` and `1.4400` for `ipow`. The result of `ipow` is more precise.

``` abap
cl_demo_output=>display( |**:   { '1.2' ** 2 } \n| && 
                         |ipow: { ipow( base = '1.2' exp = 2 ) }| ).
```

## Executable Example

[Power Function `ipow`](abenipow_function_abexa.md)
