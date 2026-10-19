---
title: "&&=, Calculation Assignment"
source_file: abencalculation_assignment_string.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - &&"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# &&=, Calculation Assignment

## Syntax

``` abap
lhs &&= rhs.  
```

## Description

[Calculation assignment](../../abap-glossary/abencalculation_assignment_glosry.md) with the concatenation assignment operator `&&=`.

This assignment has the same effect as the following [assignment of a string expression](abenequals_string_expr.md):

lhs = [`lhs && rhs`](abenstring_operators.md).

The result of the expression `rhs` is concatenated with the content of `lhs` and the result is assigned to `lhs`.

The following applies to the operands `lhs` and `rhs`:

- `lhs` is a [result position](../../abap-glossary/abenresult_position_glosry.md) and the following can be specified if they are character-like:

  - [Variables](../../abap-glossary/abenvariable_glosry.md)

  - [Writable expressions](../../abap-glossary/abenwritable_expression_glosry.md)

- `rhs` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) and the following can be specified if they are character-like:

  - [Data objects](../../abap-glossary/abennumeric_data_object_glosry.md)

  - [Constructor expressions](../../abap-glossary/abenconstructor_glosry.md)

  - [String expressions](../../abap-glossary/abenstring_expression_glosry.md)

  - [Table expressions](../../abap-glossary/abentable_expression_glosry.md)

  - [Functions](../../abap-glossary/abenfunction_glosry.md)

    Type inference with the character `#` is not currently possible in constructor expressions. No [numeric expressions](../../abap-glossary/abennumerical_expression_glosry.md) and [bit expressions](../../abap-glossary/abenbit_expression_glosry.md) can be specified.

## Hints

- No [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) are possible for `lhs`.

- Calculation assignments can currently only be specified as standalone statements and after `NEXT` in the reduction operator [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md). They are not possible in other expressions.

- See also the [addition assignment operator](../../abap-glossary/abenadd_assignment_op_glosry.md) ([`+=`](abencalculation_assignments.md)), the [subtraction assignment operator](../../abap-glossary/abensub_assignment_op_glosry.md) ([`-=`](abencalculation_assignments.md)), the [multiplication assignment operator](../../abap-glossary/abenmult_assignment_op_glosry.md) ([`*=`](abencalculation_assignments.md)), and the [division assignment operator](../../abap-glossary/abendiv_assignment_op_glosry.md) ([`/=`](abencalculation_assignments.md)).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the calculation assignments, the variable `text` has the value *1, 2, 3, 4, 5, 6, 7, 8, 9, 10,*.

``` abap
DATA text TYPE string. 
DO 10 TIMES. 
  text &&= |{ sy-index }, |. 
ENDDO.
```
