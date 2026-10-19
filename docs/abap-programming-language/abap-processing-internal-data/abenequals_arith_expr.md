---
title: "=, Arithmetic Expression"
source_file: abenequals_arith_expr.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > =, Assignment Operator > =, Assign Calculation Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# =, Arithmetic Expression

## Syntax

``` abap
result = arith_exp.  
```

[`arith_exp`](abapcompute_arith.md)

## Description

If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) [`arith_exp`](abapcompute_arith.md) is specified on the right side of the [assignment operator `=`](abenequals_operator.md), its [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is calculated and assigned to the left side `result`.

The following can be specified for `result`:

- A [variable](../../abap-glossary/abenvariable_glosry.md) that is compatible with the numeric result of the arithmetic expression or to whose type the result can be converted.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The data type of the declared variable `var` is the statically known [calculation type](../../abap-glossary/abencalculation_type_glosry.md), where generically typed field symbols and formal parameters with a [standard type](../../abap-glossary/abenstandard_type_glosry.md) [described here](abenarith_type.md) are involved. In the case of the calculation type `p`, the data type of the declared variable is always `p` with the length 8 without decimal places. Furthermore, if [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md) of type `DECFLOAT16` are involved but no numbers of type `DECFLOAT34`, the data type of the declared variable is not the calculation type `DECFLOAT34` but `DECFLOAT16`.

If an existing variable is specified for `result`, its data type is included in the determination of the [calculation type](abenarith_type.md). If the calculation type is not the data type of `result`, the result is converted to the data type of the result field before the assignment is made.

## Hints

- The fact that the result field is respected when the calculation type is determined is a special property of ABAP that should always be kept in mind.

- The calculation type that is dependent on the data type of the result field is an important difference from an [assignment of data objects](abapmove.md). If data objects are incompatible, the source field is always converted to the data type of the target field. When arithmetic expressions are assigned, their operands can also be converted to the data type of the result field before the calculation.

- The fact that a [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `p` on the right side of an inline declaration produces the data type `p` with length 8 and no decimal places can lead to unexpected results and raise exceptions. It is best to either avoid inline declarations when using the calculation type `p` or to determine the data type by applying the conversion operator [`CONV`](abenconstructor_expression_conv.md) to the arithmetic expression.

- See also [calculation assignments](../../abap-glossary/abencalculation_assignment_glosry.md) with the operators [`+=`](abencalculation_assignments.md), [`-=`](abencalculation_assignments.md), [`*=`](abencalculation_assignments.md) and [`/=`](abencalculation_assignments.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first assignment is an assignment of an arithmetic expression, because of the leading plus/minus sign. The [calculation type](abenarith_type.md) is determined as `i` and `result` is given the value *731036*, the number of days since 01.01.0001. The second assignment, on the other hand, has the same meaning as an [assignment of data objects](abapmove.md) and produces the value *20020704* in `result`.

``` abap
DATA: result TYPE string, 
      date   TYPE d VALUE '20020704'. 
 
result = + date. 
result =   date.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates inline declarations with the calculation type `p`. Assignments of a data object use its data type, but assignments of an arithmetic expression with the calculation type `p`, the data type `p` with length 8 and without decimal places is used. This means that decimal places are lost in the first assignment and that the second assignment produces and overflow and its corresponding exception. The conversion operator `CONV` can be used to avoid these problems.

``` abap
TYPES pack8_3  TYPE p LENGTH 8  DECIMALS 3. 
TYPES pack16   TYPE p LENGTH 16 DECIMALS 0. 
DATA  number1  TYPE pack8_3 VALUE '12345.678'. 
DATA  number2  TYPE pack16 VALUE  '12345678901234567890'. 
 
FINAL(result1) = number1.                    "p, length 8, decimals 3 
FINAL(result2) = number2.                    "p, length 16 
TRY. 
    FINAL(result3) = 1 * number1 ##type.     "p, length 8, decimals 0 
    FINAL(result4) = 1 * number2 ##type.     "p, length 8 ->exception 
  CATCH cx_sy_arithmetic_overflow. 
ENDTRY. 
FINAL(result5) = CONV pack8_3( 1 * number1 ). "p, length 8, decimals 3 
FINAL(result6) = CONV pack16(  1 * number2 ). "p, length 16
```
