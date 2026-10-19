---
title: "Checking Elementary Data Objects"
source_file: abenmove_exact_elementary.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments > Lossless Assignments, Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Checking Elementary Data Objects

In conversions between incompatible [elementary data objects](../../abap-glossary/abenelementary_data_object_glosry.md), the operator [`EXACT`](abenconstructor_expression_exact.md) ensures that no values are lost. Regardless of the value of the operand, the operator `EXACT` generally does not allow conversions between data objects with the following data types, for which the values are always lost when the [conversion rules](abenconversion_elementary.md) are applied.

- From `x`, `xstring` to `n`, `d`, `t`, and vice versa.

- From `x`, `xstring` to all [numeric data types](../../abap-glossary/abennumeric_data_type_glosry.md), and vice versa.

- From `d` and `t` to `b` and `s`

Conversions from `d` to `t` and vice versa, and most conversions for UTC time stamps of the type `utclong` are prohibited regardless of the operator `EXACT`. Other conversions that are not allowed are conversions in which byte-like fields are converted directly or as an interim result to the data type `i` and vice versa.

If the compiler detects a forbidden conversion a syntax error occurs. If a forbidden conversion is detected at runtime, an exception of the class `CX_SY_CONVERSION_EXACT_NOT_SUP` is raised. The same applies to types for which conversions are allowed, but for which a loss of values can be identified regardless of the content, for example, if a conversion is made to fields that are too short.

If allowed conversions are made between incompatible elementary data objects, the operator `EXACT` checks the content of the operand at runtime as follows:

- [Valid Values for Lossless Assignments](abenmove_exact_elementary_valid.md)

- [Suitable Values for Lossless Assignments](abenmove_exact_elementary_fit.md)

If the elementary data types for which no conversion is required are [compatible](../../abap-glossary/abencompatible_glosry.md), no checks are performed, and no exceptions are raised.

## Hints

- When the operator `EXACT` is used, a catchable exception is always raised at runtime when a forbidden conversions is made, in particular, when an attempt is made to convert between `d` and `t`. In all other cases, an attempted conversion of this type raises an uncatchable exception.

- If an operand contains an invalid or inappropriate value, this is assigned to its return value, even if the operator `EXACT` is used.

## Executable Example

[Lossless Assignment](abenmove_exact_abexa.md).
