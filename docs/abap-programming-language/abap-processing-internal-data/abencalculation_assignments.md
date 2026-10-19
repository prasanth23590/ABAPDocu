---
title: "+=, -=, *=, /=, Calculation Assignments"
source_file: abencalculation_assignments.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# +=, -=, \*=, /=, Calculation Assignments

## Syntax

``` abap
lhs += 
  | -= 
  | *= 
  | /= rhs.  
```

## Description

[Calculation assignment](../../abap-glossary/abencalculation_assignment_glosry.md) with one of the following [calculation assignment operators](../../abap-glossary/abencalc_assignment_op_glosry.md):

- addition assignment operator `+=`

- subtraction assignment operator `-=`

- multiplication assignment operator `*=`

- division assignment operator `/=`

As long as no [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md) using the character `#` for type inference are used as `rhs`, these assignments have the same effect as the following [assignments of arithmetic expressions](abenequals_arith_expr.md):

``` abap
lhs = `lhs + ( rhs )`. 
lhs = `lhs - ( rhs )`. 
lhs = `lhs * ( rhs )`. 
lhs = `lhs / ( rhs )`.
```

The content of `lhs`

- gets the result of the parenthesized expression `rhs` added to it,

- or has the result of the parenthesized expression `rhs` subtracted from it,

- or is multiplied by the result of the parenthesized expression `rhs`,

- or is divided by the result of the parenthesized expression `rhs`,

and the result is assigned to `lhs`. The [calculation type](../../abap-glossary/abencalculation_type_glosry.md) is [determined](abenarith_type.md) accordingly.

The following applies to the operands `lhs` and `rhs`:

- `lhs` is a [result position](../../abap-glossary/abenresult_position_glosry.md) and the following can be specified:

  - numeric [variables](../../abap-glossary/abenvariable_glosry.md)

  - numeric [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md)

- `rhs` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) and the following can be specified:

  - numeric [data objects](../../abap-glossary/abennumeric_data_object_glosry.md)

  - numeric [constructor expressions](../../abap-glossary/abenconstructor_glosry.md)

  - numeric [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md)

  - numeric [table expressions](../../abap-glossary/abentable_expression_glosry.md)

  - numeric [functions](../../abap-glossary/abenfunction_glosry.md)

    [Character-like expressions](../../abap-glossary/abencharlike_expression_glosry.md) and [bit expressions](../../abap-glossary/abenbit_expression_glosry.md) cannot be specified.

Division by the value 0 is undefined and raises a catchable exception. The only situation where division by 0 does not raise an exception is if the dividend is also 0. Here, the result is set to 0.

**Caution**

If `rhs` is a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) using the character `#` for type inference, the type is not derived as in the respective arithmetic expression but as in an assignment of `rhs` to `lhs`.

## Hints

- Apart from data objects, calculation assignments also allow expressions in the operand positions. This makes them more powerful than the statements [`ADD`](../abap-obsolete-language-elements/abapadd.md), [`SUBTRACT`](../abap-obsolete-language-elements/abapsubtract_multiply_divide.md), [`MULTIPLY`](../abap-obsolete-language-elements/abapsubtract_multiply_divide.md), [`DIVIDE`](../abap-obsolete-language-elements/abapsubtract_multiply_divide.md), and also makes them obsolete.

- No [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) are possible for `lhs`.

- Calculation assignments can currently only be specified as standalone statements. They are not possible in other expressions, such as after `NEXT` in the reduction operator [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md).

- See also the [concatenation assignment operator](../../abap-glossary/abenconcat_assignment_op_glosry.md) ([`&&=`](abencalculation_assignment_string.md)).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The variable `n` has the value *1.50* after the calculation assignments.

``` abap
DATA n TYPE p DECIMALS 2. 
 
n += 1. 
n += 1. 
n += 1. 
n += 1. 
n -= 2. 
n *= 3. 
n /= 4.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The calculation assignment gives a different result than the respective arithmetic expression because of different type inference for the constructor expression.

- In the calculation assignment, the type `i` is taken from the left hand side of the assignment. The result of the constructor expression is converted from `c` to `i` and the value *0,5* is rounded up to *1*. The calculated value is `2`

- In the arithmetic expression, the rules for its [calculation type](abenarith_type.md) are followed. The type of the constructor expression is taken from the expression itself, that is type `c` of operand `txt`. This type is handled as type `p` and thus determines the calculation type. The calculated value is `1`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(txt) = '0.5'. 
 
DATA(num) = 2. 
"# takes type i from num, expression is rounded up to 1 
num *= COND #( WHEN 1 = 1 THEN txt ). "2 
out->write( num ). 
 
num = 2. 
"# takes type c from txt, expression is converted to calculation type p 
num  = num * COND #( WHEN 1 = 1 THEN txt ). "1 
out->write( num ). 
 
out->display( ).
```
