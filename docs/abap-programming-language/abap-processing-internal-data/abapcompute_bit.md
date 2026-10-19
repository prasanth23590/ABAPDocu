---
title: "Bit Expressions (bit_exp)"
source_file: abapcompute_bit.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Bit Expressions (bit_exp)

## Syntax

``` abap
... [BIT-NOT] operand1 
    [{BIT-AND|BIT-OR|BIT-XOR} [BIT-NOT] operand2 
    [{BIT-AND|BIT-OR|BIT-XOR} [BIT-NOT] operand3 
    ...  ]] ...  
```

[`BIT-NOT`](abenbit_operators.md) · [`BIT-AND|BIT-OR|BIT-XOR`](abenbit_operators.md) · [`BIT-NOT`](abenbit_operators.md) · [`BIT-AND|BIT-OR|BIT-XOR`](abenbit_operators.md) · [`BIT-NOT`](abenbit_operators.md)

## Description

A bit expression formulates a binary calculation. The operands must be byte-like, that is, of type `x` or `xstring`. The result of a bit expression is a byte chain in the [calculation length](abenbitexp_length.md) assigned to the bit expression. During assignment to an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), the byte chain is handled as a byte string of data type `xstring`, and when passing a generic typed formal parameter, it is handled as a byte field of data type `x`.

In a bit expression `bit_exp`, an operand `operand1` can be combined with one or more operands `operand2`, `operand3`, ... using [bit operators](abenbit_operators.md) `BIT-AND`, `BIT-OR`, or `BIT-XOR`. [Brackets](abenbit_brackets.md) are possible. Bit expressions can occur in read positions of [certain statements](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md), in particular on the right side of an [assignment](abenequals_bit_expr.md) with the [assignment operator `=`](abenequals_operator.md).

The operand positions `operand` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md), which means byte-like data objects, [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) with byte-like return values, or parenthesized bit expressions can be specified. The bit operators `BIT-AND`, `BIT-OR`, and `BIT-XOR` combine two adjacent operands. When the expression is evaluated, a byte-like value is calculated and combined with the next adjacent operand. The priority of the combination depends on the operators that are used. If functional methods are used, the same applies as described for [arithmetic expressions](abapcompute_arith.md).

The [bit operator](abenbit_operators.md) `BIT-NOT` can be specified one or more times in front of an operand to negate the value of the operand. If `BIT-NOT` is specified an even number of times, the operand remains unchanged. An odd number negates the operand.

If [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) are specified as operands, they are executed from left to right and from inside to outside before the remainder of the expression is evaluated. The return values are buffered to be used in the corresponding operand positions.

If [constructor expressions](../abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) are specified as operands of bit expressions, their data type is not determined by the bit expression. The `#` character can be specified for the data type of the constructor expression only if the type can be determined from the constructor expression itself.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Bit sequences are an efficient way of mapping bit sequences. If a set contains n elements, the existence of an element i in n can be represented by a 1 at the position of i in a byte-like field. The statement [`SET BIT`](abapset_bit.md), for example, can be used to add an element to the set. The operators `BIT-AND`, `BIT-OR`, and `BIT-XOR` can then be used to calculate the intersection, the union, and the symmetric difference of different sets.

In the following example, the attributes of person groups are represented in the fields `p1`, `p2`, `p3` of the type `x`. The bit operator `BIT-AND` is then used to determine which attributes are shared by all people. The result shows that only the eighth attribute is shared.

``` abap
DATA: 
  p1  TYPE x LENGTH 1 VALUE '5B',     "01011011 
  p2  TYPE x LENGTH 1 VALUE '13',     "00010011 
  p3  TYPE x LENGTH 1 VALUE 'A5'.     "10100101 
 
FINAL(res) = p1 BIT-AND p2 BIT-AND p3. "00000001
```
