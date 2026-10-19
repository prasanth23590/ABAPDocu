---
title: "Built-In Character-Like Types"
source_file: abenbuiltin_types_character.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Types > Built-In ABAP Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Character-Like Types

The data objects of the character-like data types are used to store character strings.

**Properties**

| **Type** | **Length**              | **Standard Length** | **Meaning**                                                        | **Data Object**                                          |
|----------|-------------------------|---------------------|--------------------------------------------------------------------|----------------------------------------------------------|
| `c`      | 1 to 262,143 characters | 1 character         | [Text field type](../../abap-glossary/abentext_field_type_glosry.md)                 | [Text field](../../abap-glossary/abentext_field_glosry.md)                 |
| `n`      | 1 to 262,143 characters | 1 character         | [Numeric text field type](../../abap-glossary/abennumeric_text_field_type_glosry.md) | [Numeric text field](../../abap-glossary/abennumeric_text_field_glosry.md) |
| `string` | Variable                |                     | [Text string type](../../abap-glossary/abentext_string_type_glosry.md)               | [Text string](../../abap-glossary/abentext_string_glosry.md)               |

**Value Ranges and Initial Values**

| **Type** | **Value Range**                                                                                                              | **Initial Value**          |
|----------|------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| `c`      | Any Unicode characters that can be encoded in [UCS-2](../../abap-glossary/abenucs2_glosry.md).                                                 | Blank for every position   |
| `n`      | Any Unicode characters that can be encoded in [UCS-2](../../abap-glossary/abenucs2_glosry.md); valid characters are only the digits *0* to *9* | *0* for every position     |
| `string` | As for type `c`                                                                                                              | Empty string with length 0 |

## Hints

- The character-like data types are mainly used for [string processing](../abap-processing-internal-data/abenabap_data_string.md).

- For more about strings, see [Strings](../abap-data-types-and-data-objects/abenstring.md).

- The data types `c` and `string` are general character-like data types, whereas `n` has special properties. The data type `n` matches the special type [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_special_character_types.md) in ABAP Dictionary.

- Further character-like data types with special properties are the built-in [date types and time types](abenbuiltin_types_date_time.md) that match the corresponding types [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_date_time_types.md) and [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_date_time_types.md) of the ABAP Dictionary. All other special character-like data types in ABAP Dictionary are assigned to the general ABAP types listed here.

- The content of the data objects of character-like data types is stored in the memory according to the current [system code page](../../abap-glossary/abensystem_codepage_glosry.md).

- When specifying lengths for character-like types, note that the length of a character in bytes depends on the character representation used. For the character representation [UCS-2](../../abap-glossary/abenucs2_glosry.md) used by the ABAP programming language, the length of a character is two bytes.

- The types `c` and `n`, for which a length interval is specified in the second column of the first table, are [generic](abenbuilt_in_types_generic.md), which means that the length is not part of the type description. The entries in the column `Standard Length` specify the length that is used in declarations of data objects when using types with generic lengths, if no explicit length is specified in the corresponding statement.

- The system class `CL_ABAP_ELEMDESCR` contains the constants `TYPE_C_MAX_LENGTH` and `TYPE_N_MAX_LENGTH` for the maximum length of the types `c` and `n`.

- The valid values of the data type `n` are a subset of its value range. ABAP statements that work with data objects of this type are only guaranteed to function correctly for operands with valid values.

- The [maximum size](../abap-data-types-and-data-objects/abenmemory_consumption_2.md) of strings must be respected. If an operation with a string exceeds its maximum size, an exception of class `CX_SY_STRING_SIZE_TOO_LARGE` is raised and can be handled.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of character-like data objects with built-in character-like data types. The flag `flag` is limited to one character and the set of characters in the string `html` is variable.

``` abap
DATA: flag TYPE c LENGTH 1, 
      html TYPE string.
```
