---
title: "Built-In ABAP Types"
source_file: abenbuilt_in_types_complete.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In ABAP Types

The following types are built-in in every ABAP program:

- [Built-In Numeric Types](abenbuiltin_types_numeric.md)

- [Built-In Character-Like Types](abenbuiltin_types_character.md)

- [Built-In Byte-Like Types](abenbuiltin_types_byte.md)

- [Built-In Date Types, Time Types, and Time Stamp Types](abenbuiltin_types_date_time.md)

All built-in ABAP types from these tables are elementary and are included in the generic type [`simple`](abenbuilt_in_types_generic.md). Apart from the types [`b`](abenbuiltin_types_numeric.md) and [`s`](abenbuiltin_types_numeric.md), the built-in ABAP types can be used to define separate [data types](../../abap-glossary/abendata_type_glosry.md) and [data objects](../../abap-glossary/abendata_object_glosry.md) and for [typing](../../abap-glossary/abentyping_glosry.md).

In addition to the actual built-in ABAP types, there is a predefined data type `cursor` that is global to the program, which currently has the same meaning as the built-in ABAP type [`i`](abenbuiltin_types_numeric.md). It is required when declaring a cursor variable for [database cursor](../../abap-glossary/abendatabase_cursor_glosry.md) handling.

## Hints

- If no explicit [start value](../../abap-glossary/abenstart_value_glosry.md) is specified when creating a data object with one of the built-in ABAP types, the start value is set to the [initial value](../../abap-glossary/abeninitial_value_glosry.md) specified for the relevant type.

- The built-in data types [`string`](abenbuiltin_types_character.md) and [`xstring`](abenbuiltin_types_byte.md) describe data objects of variable length ([dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md)). While the length of data objects of all other elementary data types is fixed for their whole lifetime, the length of text strings and byte strings varies according to their content.
