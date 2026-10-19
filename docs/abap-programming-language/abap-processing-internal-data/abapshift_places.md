---
title: "SHIFT, places"
source_file: abapshift_places.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Statements for Character String and Byte String Processing > SHIFT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SHIFT, places

## Syntax

``` abap
... {BY num PLACES} | {UP TO substring} ...  
```

### Variant

[1. `... BY num PLACES ...`](abapshift_places.md#variant-1)

[2. `... UP TO substring ...`](abapshift_places.md#variant-2)

## Variant 1

`... BY num PLACES ...`

### Description

The content of `dobj` is shifted to the left or right by the positions specified in `num`, depending on the specification in [`direction`](abapshift_direction.md). `num` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`. If the content of `num` is less than or equal to 0, the content of the data object `dobj` remains unchanged.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `FIND` determines the offset of the word *you* in `text` and shifts its content by this length to the left or right. After the shift, `text` contains *you know* and is eight characters long.

``` abap
DATA: text TYPE string VALUE `I know you know`, 
      off  TYPE i. 
 
FIND 'you' IN text MATCH OFFSET off. 
 
SHIFT text BY off PLACES.
```

## Variant 2

`... UP TO substring ...`

### Description

In the data object `dobj`, the first substring is searched for whose content matches that of `substring`. The search is case-sensitive. Depending on the specification in [`direction`](abapshift_direction.md), the content of the data object `dobj` is shifted to the left or right until the byte string or character string contained in `substring` is left-aligned or right-aligned at the position that is at the beginning or end of the data object `dobj` before the shift.

`substring` expects a character-like or byte-like data object. If `substring` is an empty string, the place in front of the first character or byte is found. There is no shift to the left but a shift by the entire length of `dobj` to the right.

In character string processing, `substring` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md); in data objects, `substring` with a fixed length respects the trailing blanks.

### System Fields

| **`sy-subrc`** | **Meaning**                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------------|
| 0              | The substring in `substring` was found in the data object `dobj` and its content was moved accordingly. |
| 4              | The substring in `substring` was not found in the data object `dobj` and its content remain unchanged.  |

### Hint

For data objects of fixed length, the substring searched for after the shift is either left-aligned at the beginning or right-aligned at the end of the data object, depending on the direction. In the case of strings, the shift makes the data object longer on the right, which means that the substring is not at the right margin after the shift.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example has the same result as the previous example. However, here the search for *you* is not performed in the statement `SHIFT` itself.

``` abap
DATA text TYPE string VALUE `I know you know `. 
 
SHIFT text UP TO 'you'.
```
