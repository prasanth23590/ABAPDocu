---
title: "SET BIT"
source_file: abapset_bit.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET BIT

## Syntax

``` abap
SET BIT bitpos OF byte_string [TO val].  
```

## Description

This statement sets the bit at bit position `bitpos` of the `byte_string` to 1 or, if specified, to the value of data object `val`. The other bits in `byte_string` remain unchanged. `byte_string` is a [result position](../../abap-glossary/abenresult_position_glosry.md), that is, either a variable or a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) can be specified.

The data object `byte_string` must be byte-like, whereas `bitpos` and `val` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`. The value of `bitpos` must be greater than 0 and `val` must be either 0 or 1, otherwise an uncatchable exception is raised. The bit positions in `byte_string` are counted from left to right starting with the [most significant bit (MSB)](../../abap-glossary/abenmost_significant_bit_glosry.md) of the data object. If the value of `bitpos` is greater than the number of bits in `byte_string`, no replacement is made and `sy-subrc` is set to 4.

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| 0              | A bit of the data object `byte_string` was set at position `bitpos`.                          |
| 4              | The value of `bitpos` is greater than the number of bits in `byte_string` and no bit was set. |

## Hints

- If `byte_string` has the [deep](../../abap-glossary/abendeep_glosry.md) type `xstring`, a bit is set in the referenced byte string, not in the reference.

- Setting single bits is intended in particular for preparing operators in [bit expressions](abapcompute_bit.md).

- The built-in function [`bit-set`](abenbit_functions.md) can also be used to set an individual bit.

- Counting the bits from the [most significant bit (MSB)](../../abap-glossary/abenmost_significant_bit_glosry.md) can have unexpected results when working with components that count from the [least significant bit (LSB)](../../abap-glossary/abenleast_significant_bit_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the data object `hex` with eight bits, the bit is set to the value 1 at the position determined by the loop counter `sy-index`, with all other bits set to 0. The output is *80 40 20 10 08 04 02 01*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA hex    TYPE x LENGTH 1. 
DATA output TYPE string. 
DO 8 TIMES. 
  CLEAR hex. 
  SET BIT sy-index OF hex. 
  output &&= |{ hex } |. 
ENDDO. 
out->write( output ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, single bits are set in the lines of an internal table, where a [table expression](../../abap-glossary/abentable_expression_glosry.md) is used as a [writable expression](../../abap-glossary/abenwritable_expression_glosry.md) in `SET BIT`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  hex     TYPE x LENGTH 1, 
  hex_tab TYPE STANDARD TABLE OF hex WITH EMPTY KEY. 
 
DATA(hex_tab) = VALUE hex_tab( FOR i = 1 UNTIL i > 8 ( ) ). 
 
DO 8 TIMES. 
  SET BIT sy-index OF hex_tab[ sy-index ]. 
ENDDO. 
 
out->write( hex_tab ). 
 
out->display( ).
```
