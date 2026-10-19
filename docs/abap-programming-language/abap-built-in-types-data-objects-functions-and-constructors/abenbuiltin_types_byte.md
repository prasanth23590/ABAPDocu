---
title: "Built-In Byte-Like Types"
source_file: abenbuiltin_types_byte.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Types > Built-In ABAP Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Byte-Like Types

The data objects of the byte-like data types are used to store byte strings.

**Properties**

| **Type**  | **Length**         | **Standard Length** | **Meaning**                                          | **Data Object**                            |
|-----------|--------------------|---------------------|------------------------------------------------------|--------------------------------------------|
| `x`       | 1 to 524,287 bytes | 1 byte              | [Byte field type](../../abap-glossary/abenbyte_field_type_glosry.md)   | [Byte field](../../abap-glossary/abenbyte_field_glosry.md)   |
| `xstring` | Variable           |                     | [Byte string type](../../abap-glossary/abenbyte_string_type_glosry.md) | [Byte string](../../abap-glossary/abenbyte_string_glosry.md) |

**Value Ranges and Initial Values**

| **Type**  | **Value Range**                         | **Initial Value**          |
|-----------|-----------------------------------------|----------------------------|
| `x`       | Any byte values, hexadecimal 00 to `FF` | Hexadecimal 00             |
| `xstring` | As for type `x`                         | Empty string with length 0 |

## Hints

- The byte-like data types are used for [byte string processing](../abap-processing-internal-data/abenabap_data_string.md).

- For more about strings, see [Strings](../abap-data-types-and-data-objects/abenstring.md).

- The type `x`, for which a length interval is specified in the second column of the first table, is [generic](abenbuilt_in_types_generic.md), which means that the length is not part of the type description. The entry in the column `Standard Length` specifies the length used in declarations of data objects when using types with generic lengths, if no explicit length is specified in the corresponding statement.

- The system class `CL_ABAP_ELEMDESCR` contains a constant `TYPE_X_MAX_LENGTH` for the maximum length of the type `x`.

- The [maximum size](../abap-data-types-and-data-objects/abenmemory_consumption_2.md) of strings must be respected. If an operation with a string exceeds its maximum size, an exception of class `CX_SY_STRING_SIZE_TOO_LARGE` is raised and can be handled.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a byte string of the built-in ABAP type `xstring` for the result of a functional method. This declaration could also be made [inline](../abap-declarations/abeninline_declarations.md) on the left side of the assignment.

``` abap
DATA hex TYPE xstring. 
hex =  cl_abap_conv_codepage=>create_out(  )->convert( `...` ).
```
