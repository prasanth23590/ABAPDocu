---
title: "=, Assignment Operator"
source_file: abenequals_operator.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# =, Assignment Operator

## Syntax

``` abap
lhs = rhs.  
```

## Description

An operator `=` that is placed in a statement between a left hand side `lhs` and a right hand side `rhs` acts as an [assignment operator](../../abap-glossary/abenassignment_operator_glosry.md), that assigns the value of the right hand side to the left hand side. If necessary, a [conversion](abenconversion_rules.md) takes place.

The right side `rhs`, which is the source of the assignment, is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md) and can be specified as follows:

- As a single [data object](abapmove.md)

- As a [return value or result](abenequals_return_values.md) of functional methods, built-in functions, or constructor expressions or table expressions

- As a result of [calculation expressions](abenequals_calc_expr.md)

The left side `lhs`, the target of the assignment, is a both a [declaration position](../../abap-glossary/abendeclaration_position_glosry.md) and a [result position](../../abap-glossary/abenresult_position_glosry.md) and can be specified as follows:

- As any data object that can be specified in a [write position](../../abap-glossary/abenwrite_position_glosry.md). The data type of the data object must either be [compatible](../../abap-glossary/abencompatible_glosry.md) with the assigned value or must be convertible to the data type of `lhs` in accordance with one of the [conversion rules](abenconversion_rules.md). If the assigned value does not match the data type of `lhs`, the exceptions described in the conversion rules can occur.

- As an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The data type of the declared variable is determined by the right side and is described for the different `rhs` options. Any variable that is used on the right side cannot be declared on the left side. An identically named data object of a more global context can be used on the right side and is not hidden by the local declaration until after the statement.

- As a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) representing an operand to which the right side can be assigned.

If an exception is raised on the right side, the statement is not executed, and the value of the target field is undefined.

## Hints

- See also [calculation assignments](../../abap-glossary/abencalculation_assignment_glosry.md) with the operators [`+=`](abencalculation_assignments.md), [`-=`](abencalculation_assignments.md), [`*=`](abencalculation_assignments.md), [`/=`](abencalculation_assignments.md), and [`&&=`](abencalculation_assignment_string.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignments of a literal, a constructor expression, and an arithmetic expression to target fields.

``` abap
DATA: o1 TYPE i, 
      o2 TYPE i, 
      r  TYPE i. 
 
o1 = 100. 
o2 = CONV #( '200' ). 
r  = o1 + o2.
```
