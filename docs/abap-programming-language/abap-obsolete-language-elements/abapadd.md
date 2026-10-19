---
title: "ADD"
source_file: abapadd.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Calculation Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ADD

## Obsolete, deprecated Syntax

``` abap
ADD dobj1 TO dobj2.  
```

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Description

This statement has the same effect as the statement

[`dobj2 += dobj1.`](../abap-processing-internal-data/abencalculation_assignments.md)

that is the same as

[`dobj2 = dobj2 + dobj1.`](../abap-processing-internal-data/abenequals_arith_expr.md)

The content of `dobj1` is added to the content of `dobj2` and the result is assigned to `dobj2`. The data objects `dobj1` and `dobj2` must be numeric. Only data objects can be specified, no calls or other expressions. The [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is determined as for an [arithmetic expression](../abap-processing-internal-data/abapcompute_arith.md).

## Hint

The statement `ADD` has been fully replaced by the [calculation assignment](../../abap-glossary/abencalculation_assignment_glosry.md) with the operator [`+=`](../abap-processing-internal-data/abencalculation_assignments.md) in which the operands can also be specified as expressions.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ARITHMETIC_OVERFLOW`

- *Cause:* Overflow in arithmetic operation (type `p`)

  *Runtime error:* `BCD_OVERFLOW`

- *Cause:* Integer overflow in addition

  *Runtime error:* `COMPUTE_INT_PLUS_OVERFLOW`

`CX_SY_CONVERSION_OVERFLOW`

- *Cause:* Overflow in arithmetic operation (type `p`, with specified length)

  *Runtime error:* `BCD_FIELD_OVERFLOW`
