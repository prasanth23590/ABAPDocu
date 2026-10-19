---
title: "GET BIT"
source_file: abapget_bit.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET BIT

## Syntax

``` abap
GET BIT bitpos OF byte_string INTO val.  
```

## Description

This statement reads the bit at the bit position `bitpos` of the data object `byte_string` and assigns its value to the target field `val`. `val` can be specified as follows:

- An existing variable that expects the data type `i`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of type `i` is declared.

- Expressions with the [`CAST`](abenconstructor_expression_cast.md) and [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) operators and table expressions.

The data object `byte_string` must be byte-like. [Bit](../../abap-glossary/abenbit_expression_glosry.md), [constructor](../../abap-glossary/abenconstructor_expression_glosry.md) and [table](../../abap-glossary/abentable_expression_glosry.md) expressions can be used. `bitpos` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`. The value of `bitpos` must be greater than 0, otherwise uncatchable exceptions are raised. The bit positions in `byte_string` are counted from left to right, starting with the [most significant bit (MSB)](../../abap-glossary/abenmost_significant_bit_glosry.md) of the data object. If the value of `bitpos` is greater than the number of bits in `byte_string`, no bit is read and `sy-subrc` is set to 4.

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------|
| 0              | The value of the bit at position `bitpos` of `byte_string` was placed in the result field `val`. |
| 4              | The value of `bitpos` is greater than the number of bits in `byte_string` and no bit was read.   |

## Hints

- If `byte_string` has the [deep](../../abap-glossary/abendeep_glosry.md) type `xstring`, a bit is read from the referenced byte string, not from the reference.

- The reading of single bits is especially intended for evaluating the results of [bit expressions](abapcompute_bit.md).

- Counting the bits from the [most significant bit (MSB)](../../abap-glossary/abenmost_significant_bit_glosry.md) can have unexpected results when working with components that count from the [least significant bit (LSB)](../../abap-glossary/abenleast_significant_bit_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The hexadecimal value *1B* is assigned to the data object `hex` and its bits are read from front to back. The output is *00011011*, which corresponds to the binary representation of decimal 27 or hexadecimal *1B*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA hex TYPE xstring VALUE `1B`. 
FINAL(len) = xstrlen( hex ) * 8. 
DATA output TYPE string. 
 
WHILE sy-index <= len. 
  GET BIT sy-index OF hex INTO FINAL(res). 
  output &&= res. 
ENDWHILE. 
out->write_text( output ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Hexadecimal values are assigned to data objects and included in an internal table which is looped across. During the loop, the bits are read from front to back. Finally, the result is added to the internal table which shows the hexadecimal and binary values. The `GET BIT` statement demonstrates a table expression following `OF`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: BEGIN OF struc, 
         hex_value TYPE xstring, 
         bin       TYPE string, 
       END OF struc. 
 
DATA: hex1   TYPE xstring VALUE `1B`, 
      hex2   TYPE xstring VALUE `1C`, 
      hex3   TYPE xstring VALUE `1D`, 
      output TYPE string, 
      itab   TYPE TABLE OF struc. 
 
FINAL(len) = xstrlen( hex2 ) * 8. 
itab = VALUE #( ( hex_value = hex1 ) 
                ( hex_value = hex2 ) 
                ( hex_value = hex3 ) ). 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
  WHILE sy-index <= len. 
    GET BIT sy-index OF itab[ sy-tabix ]-hex_value INTO FINAL(res). 
    output &&= res. 
  ENDWHILE. 
 
  itab[ sy-tabix ]-bin = output. 
  CLEAR output. 
ENDLOOP. 
 
out->write( itab ). 
 
out->display( ).
```
