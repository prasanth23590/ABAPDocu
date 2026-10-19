---
title: "Strings"
source_file: abenstring.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Strings

Strings are [elementary data objects](../../abap-glossary/abenelementary_data_object_glosry.md) of variable length. There are [text strings](../../abap-glossary/abentext_string_glosry.md) and [byte strings](../../abap-glossary/abenbyte_string_glosry.md). Like [internal tables](../../abap-glossary/abeninternal_table_glosry.md), strings are [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md).

The corresponding built-in ABAP types are `string` and `xstring`. These are the dynamic equivalent of the data types `c` and `x`, which define text fields or byte fields of fixed length.

- Text strings and text fields contain [character strings](../../abap-glossary/abencharacter_string_glosry.md). Their common generic type is `csequence`.

- Byte strings and byte fields contain [byte strings](../../abap-glossary/abenbyte_chain_glosry.md). Their common generic type is `xsequence`.

Unlike a text field or byte field, the length of a string is not defined statically, but is variable and adapts to the current content of the data object at runtime. For this, dynamic memory management is used internally (see [Memory Management for Deep Data Objects](abenmemory_consumption.md)). The initial value of a string is the empty string with length 0. If there is an assignment between strings with the same type, [sharing](../../abap-glossary/abensharing_glosry.md) takes place. If an operation with a [string](../../abap-glossary/abenstring_glosry.md) exceeds its maximum size, an exception of the class `CX_SY_STRING_SIZE_TOO_LARGE` occurs and can be handled.

In contrast to text fields, trailing blanks are considered in text strings. There is a special [text string literal](../../abap-glossary/abentext_string_literal_glosry.md) for text strings. As for byte fields, there is no special [literal](../../abap-glossary/abenabap_literal_glosry.md) for byte strings in general ABAP but there is a [typed literal](../../abap-glossary/abentyped_literal_glosry.md) in ABAP SQL and ABAP CDS.

Strings are [deep](../../abap-glossary/abendeep_glosry.md) data types. A structure that contains a string is a [deep structure](../../abap-glossary/abendeep_structure_glosry.md) and cannot be used as a character-like field like a [flat structure](../../abap-glossary/abenflat_structure_glosry.md).

Strings can be stored in [data clusters](../../abap-glossary/abendata_cluster_glosry.md) like internal tables. In the ABAP Dictionary, there are the built-in data types [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) for strings that can also be the types of table fields in database tables, whereby certain [restrictions](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_character_byte_types.md) need to be considered.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declaration of a text string `carrier_list` for adding a comma-separated list of character-like data.

``` abap
SELECT carrid 
       FROM scarr 
       INTO TABLE @FINAL(carrier_tab). 
CONCATENATE LINES OF carrier_tab INTO FINAL(carrier_list) 
            SEPARATED BY `,  `. 
 
cl_demo_output=>display( carrier_list ).
```
