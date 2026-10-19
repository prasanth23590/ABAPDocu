---
title: "Character Strings and Byte Chains"
source_file: abenstring_processing_strings.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Character String and Byte String Processing, Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Character Strings and Byte Chains

- [Character Strings](abenstring_processing_strings.md#character-strings)

- [Byte Chains](abenstring_processing_strings.md#byte-chains)

## Character Strings

Character-like data objects contain character strings. A character-like data object either has a character-like data type `c`, `n`, or `string`, a date/time type `d` or `t`, or it is a [flat structure](../../abap-glossary/abenflat_structure_glosry.md) with exclusively character-like components.

ABAP supports the character format [UCS-2](../../abap-glossary/abenucs2_glosry.md) and a character always occupies two bytes. This ensures that all characters of the system code page [UTF-16](../../abap-glossary/abenutf16_glosry.md) are handled correctly, except those in the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md). These occupy four bytes and hence are handled as two characters by ABAP, which can produce unexpected results if character strings are truncated or individual characters are compared in character sets.

## Byte Chains

Byte-like data objects contain byte chains (or byte sequences). A byte-like data object always has the byte-like data type `x` or `xstring`.

### Hints

- When working with [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md) of type `string` and `xstring`, their [maximum size](../abap-data-types-and-data-objects/abenmemory_consumption_2.md) must not be exceeded. If an operation with a string exceeds its maximum size, an exception of class `CX_SY_STRING_SIZE_TOO_LARGE` occurs and can be handled.

- When [accessing substrings](../abap-operands/abenoffset_length.md) of strings, it should always be checked if the specified substring lies within the current length of the string.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A byte string of type `xstring` contains a byte chain, which is decoded in accordance with codepage UTF-8 into a text in a text string of type `string`.

``` abap
DATA hex  TYPE xstring VALUE '48656C6C6F20576F726C64'. 
DATA text TYPE string. 
 
text = cl_abap_conv_codepage=>create_in( )->convert( hex ). 
 
cl_demo_output=>display( text ).
```
