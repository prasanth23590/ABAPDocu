---
title: "Lossless Assignments"
source_file: abenlossless_move.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Lossless Assignments

In a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md), the assigned content is checked to see whether the assignment is lossless before [converting](../../abap-glossary/abenconversion_glosry.md) it to an incompatible target object. Lossless assignments can be performed using the

- [lossless operator `EXACT`](abenconstructor_expression_exact.md), in which the operand is converted to a result of the specified type using the

- [rules for lossless assignments.](abapmove_exact.md)

This makes it possible to use lossless assignments in all operand positions in which [`EXACT`](abenconstructor_expression_exact.md) can be specified.

A lossless assignment in the true sense of the word is the following use of a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) with [`EXACT`](abenconstructor_expression_exact.md) as the right side of an [assignment](abenequals_operator.md):

## Syntax

``` abap
destination = EXACT   #( source ).  
```

[`EXACT `](abenconstructor_expression_exact.md)

## Description

In this case, `source` is converted to the data type of `destination` and checked accordingly.

## Hints

- If the operand of the operator [`EXACT`](abenconstructor_expression_exact.md) is an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md), a [lossless calculation](../../abap-glossary/abenlossless_calculation_glosry.md) is performed instead of a lossless assignment.

- When assigning structures component by component using [`MOVE-CORRESPONDING`](abapmove-corresponding.md), there is an addition `EXACT` for lossless assignments.
