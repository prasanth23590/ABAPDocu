---
title: "SUBTRACT, MULTIPLY, DIVIDE"
source_file: abapsubtract_multiply_divide.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Calculation Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SUBTRACT, MULTIPLY, DIVIDE

## Obsolete, deprecated Syntax

``` abap
SUBTRACT dobj1 FROM dobj2.   
MULTIPLY dobj2 BY   dobj1.   
DIVIDE   dobj2 BY   dobj1.  
```

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Description

These statements have the same effect as the statements

[`dobj2 -= dobj1.`](../abap-processing-internal-data/abencalculation_assignments.md)

[`dobj2 *= dobj1.`](../abap-processing-internal-data/abencalculation_assignments.md)

[`dobj2 /= dobj1.`](../abap-processing-internal-data/abencalculation_assignments.md)

that are the same as

[`dobj2 = dobj2 - dobj1.`](../abap-processing-internal-data/abenequals_arith_expr.md) [`dobj2 = dobj2 * dobj1.`](../abap-processing-internal-data/abenequals_arith_expr.md) [`dobj2 = dobj2 / dobj1.`](../abap-processing-internal-data/abenequals_arith_expr.md)

The content of `dobj2`

- has the content of `dobj1` subtracted,

- or is multiplied by the content of `dobj1`,

- or is divided by the content of `dobj1`,

and the result is assigned to `dobj2`. The data objects `dobj1` and `dobj2` must be numeric. Only data objects can be specified and no calls or other expressions. The [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is determined as for an [arithmetic expression](../abap-processing-internal-data/abapcompute_arith.md).

Division by the value 0 is undefined and raises a catchable exception. The only situation where division by 0 does not raise an exception is if the dividend is also 0. Here, the result is set to 0.

## Hint

The statements shown here have been fully replaced by [calculation assignments](../../abap-glossary/abencalculation_assignment_glosry.md) with the operators [`-=`](../abap-processing-internal-data/abencalculation_assignments.md), [`*=`](../abap-processing-internal-data/abencalculation_assignments.md), and [`/=`](../abap-processing-internal-data/abencalculation_assignments.md) in which the operands can also be specified as expressions.

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

`CX_SY_ZERODIVIDE`

- *Cause:* Division by 0 (type `p`)

  *Runtime error:* `BCD_ZERODIVIDE`

- *Cause:* Division by 0 (type `f`)

  *Runtime error:* `COMPUTE_FLOAT_ZERODIVIDE`

- *Cause:* Division by 0 (type `i`)

  *Runtime error:* `COMPUTE_INT_ZERODIVIDE`
