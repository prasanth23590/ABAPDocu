---
title: "=, String Expression"
source_file: abenequals_string_expr.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > =, Assignment Operator > =, Assign Calculation Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# =, String Expression

## Syntax

``` abap
result = string_exp.  
```

[`string_exp`](abapcompute_string.md)

## Description

If a [string expression](../../abap-glossary/abenstring_expression_glosry.md) [`string_exp`](abapcompute_string.md) is specified on the right side of the [assignment operator `=`](abenequals_operator.md), its result of type `string` is calculated and assigned to the left side `result`.

The following can be specified for `result`:

- A [variable](../../abap-glossary/abenvariable_glosry.md) that has type `string` or to whose data type the result can be converted.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The data type of the declared variable `var` is `string`.

## Hints

- In the following example, the result `result` is a variable with the type `string`, and strings are appended to this variable on the right side that cannot be recognized as dependent on `result` by the compiler:

  `result = result && dobj1 && dobj2 && ...` `result = |result...{ dobj1 ... }...{ dobj2 ... }...|.` Here, no interim result is created but it is directly appended to the `result`. In all other cases, that is, data types other than `string` or when expressions are appended on the right side, an interim result is created first and then assigned. This optimization improves performance, but it must be ensured that, especially in loops, this improvement is not canceled out by using expressions on the right side, even if they are not dependent on `result`). See also the [Performance Note](abenstring_expr_perfo.md) for string expressions.

- See also [calculation assignment](../../abap-glossary/abencalculation_assignment_glosry.md) with the operator [`**=`](abencalculation_assignment_string.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first assignment declares a target field of the type `string` inline and assigns the chained text *12* to it. The second assignment converts the chained text *12* to the number 12.

``` abap
FINAL(text) = '1' && '2'. 
 
DATA number TYPE i. 
number = 1 && 2.
```
