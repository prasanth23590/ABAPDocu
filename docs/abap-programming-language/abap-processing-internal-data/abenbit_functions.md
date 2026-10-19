---
title: "bchain_func - bit-set"
source_file: abenbit_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing > Byte Chains Functions (bchain_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# bchain_func - bit-set

## Syntax

``` abap
... bit-set( arg ) ...  
```

## Description

The [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) `bit-set` is a [bit function](../../abap-glossary/abenbit_function_glosry.md) that sets individual bits of its result. It expects an integer numeric value as an argument. The argument is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of the type `i`.

- If the argument is positive, the function creates a byte chain in which the bit has the value 1 at the position specified by the argument. All other bits have the value 0. The position is counted from left to right starting with the [most significant bit (MSB)](../../abap-glossary/abenmost_significant_bit_glosry.md).

- If the argument has the value 0, the result is an empty byte chain.

- If the argument is negative, the function creates a byte chain in which all bits up to and including the place specified by the argument have the value 1 and all bits after this position have the value 0.

The length of the result is the minimum number of bytes needed to include the set bits.

The function can be used in all places where a [bit expression](../../abap-glossary/abenbit_expression_glosry.md) can be used, particularly in bit expressions themselves. The same applies to handling the result as to bit expressions. More specifically, during assignment to an inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), the resulting byte chain is handled like a byte string of data type `xstring`, and when passing a generic typed formal parameter, it is handled like a byte field of data type `x`. An empty byte chain defines a generically typed formal parameter as a byte field with a length of 1 and a hexadecimal value of *00*.

## Hints

- The function [`boolx`](../abap-program-flow-logic/abenboole_functions.md) is also a [bit function](../../abap-glossary/abenbit_function_glosry.md) in principle, but due to its properties is handled as a [logical function](../../abap-glossary/abenlogic_function_glosry.md).

- Unlike the statement [`SET BIT`](abapset_bit.md), the result field does not need to be filled first.

- Counting the bits from the [most significant bit (MSB)](../../abap-glossary/abenmost_significant_bit_glosry.md) can be unexpected when working with components that count from the [least significant bit (LSB)](../../abap-glossary/abenleast_significant_bit_glosry.md).

## Executable Example

[Setting Bits](abenbit_func_abexa.md)
