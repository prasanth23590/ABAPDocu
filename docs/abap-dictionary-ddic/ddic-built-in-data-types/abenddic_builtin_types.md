---
title: "DDIC - Overview of All Built-In Dictionary Types"
source_file: abenddic_builtin_types.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Overview of All Built-In Dictionary Types

The following tables show the built-in types in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) and their fundamental technical properties. For each built-in data type in ABAP Dictionary, the last column specifies the [built-in ABAP type](../../abap-glossary/abenbuiltin_abap_type_glosry.md) to which the built-in dictionary type is mapped when used as type reference in an ABAP program. Most built-in dictionary types are assigned an initial value. These initial values are applied, for example, when database fields are [initialized](../ddic-database-tables/abenddic_database_tables_init.md), and in the ABAP SQL condition [`IS INITIAL`](../../abap-programming-language/abap-database-access/abenwhere_logexp_initial.md). The initial value of ABAP Dictionary types is not used for data objects declared in ABAP programs when referring to these types. Here, the initial value of the mapped [built-in ABAP types](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) is used.

## General Types

Built-in dictionary data types without special semantic properties.

### Numeric Types

| **Type**     | **Valid Places `m`** | **Decimal Places `n`** | **Initial Value** | **Meaning**                                                                                           | **ABAP Type**                                                                   |
|--------------|----------------------|------------------------|-------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `INT1`       | 3                    | \-                     | 0                 | 1-byte integer, 0 to 255                                                                              | [`b`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                           |
| `INT2`       | 5                    | \-                     | 0                 | 2-byte integer, -32,768 to 32,767                                                                     | [`s`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                           |
| `INT4`       | 10                   | \-                     | 0                 | 4-byte integer, -2,147,483,648 to +2,147,483,647                                                      | [`i`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                           |
| `INT8`       | 19                   | \-                     | 0                 | 8-byte integer, -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807                              | [`int8`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                        |
| `DEC`        | 1-31                 | 0-`m`, maximum 14      | 0                 | Packed number in [BCD](../../abap-glossary/abenbcd_glosry.md) format                                                    | [`p`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), length `m DIV 2 + 1`, decimal places `n` |
| `DECFLOAT16` | 16                   | \-                     | 0                 | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md)                                             | [`decfloat16`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                  |
| `DF16_DEC`   | 1-15                 | 0-`m`, maximum 14      | 0                 | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) stored in [BCD](../../abap-glossary/abenbcd_glosry.md) format | [`decfloat16`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                  |
| `DF16_RAW`   | 16                   | \-                     | 0                 | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) stored in binary format                     | [`decfloat16`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                  |
| `DECFLOAT34` | 34                   | \-                     | 0                 | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md)                                             | [`decfloat34`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                  |
| `DF34_DEC`   | 1-31                 | 0-`m`, maximum 14      | 0                 | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) stored in [BCD](../../abap-glossary/abenbcd_glosry.md) format | [`decfloat34`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                  |
| `DF34_RAW`   | 34                   | \-                     | 0                 | [Decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) stored in binary format                     | [`decfloat34`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                  |
| `FLTP`       | 16                   | 16                     | 0                 | [Binary floating point number](../../abap-glossary/abenbinfloat_glosry.md)                                              | [`f`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md)                                           |

See [Integers, Packed Numbers, Binary Floating Point Numbers](abenddic_builtin_types_int_pack.md) and [Decimal Floating Point Numbers](abenddic_decimal_floating_point.md).

### Character-Like Types

| **Type**  | **Valid Places `m`**                      | **Initial Value** | **Meaning**                                     | **ABAP Type**                                       |
|-----------|-------------------------------------------|-------------------|-------------------------------------------------|-----------------------------------------------------|
| `CHAR`    | 1-30000, maximum of 1333 for table fields | `m` blanks        | String                                          | [`c`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), length `m` |
| `LCHR`    | 256-32000                                 | None              | Long character string                           | [`c`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), length `m` |
| `SSTRING` | 1-1333                                    | Empty string      | Character string                                | [`string`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md)        |
| `STRING`  | 256-...                                   | Empty string      | Character string ([CLOB](../../abap-glossary/abenclob_glosry.md)) | [`string`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md)        |

See [Character-Like Types and Byte-Like Types](abenddic_character_byte_types.md).

### Byte-Like Types

| **Type**    | **Valid Places `m`**                    | **Initial Value** | **Meaning**                                | **ABAP Type**                                  |
|-------------|-----------------------------------------|-------------------|--------------------------------------------|------------------------------------------------|
| `RAW`       | 1-32000 maximum of 255 for table fields | None              | Byte string                                | [`x`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md), length `m` |
| `LRAW`      | 256-32000                               | None              | Long byte string                           | [`x`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md), length `m` |
| `RAWSTRING` | 256-...                                 | Empty string      | Byte string ([BLOB](../../abap-glossary/abenblob_glosry.md)) | [`xstring`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md)       |

See [Character-Like Types and Byte-Like Types](abenddic_character_byte_types.md).

## Special Types

Built-in data types with special semantic properties.

### Date Fields, Time Fields, and Time Stamp Fields

| **Type**  | **Valid Places `m`** | **Initial Value** | **Meaning**                                                                                         | **ABAP Type**                                     |
|-----------|----------------------|-------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `DATN`    | 8                    | 0                 | Date in internal format of database                                                                 | [`d`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md)           |
| `DATS`    | 8                    | 00000000          | Date in the format `YYYYMMDD`                                                                       | [`d`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md)           |
| `TIMN`    | 6                    | 0                 | Time in internal format of database                                                                 | [`t`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md)           |
| `TIMS`    | 6                    | 000000            | Time in the format `HHMMSS`                                                                         | [`t`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md)           |
| `ACCP`    | 6                    | 6 blanks          | Posting period in the format `YYYYMM`                                                               | [`n`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), length 6 |
| `UTCLONG` | 27                   | Empty             | UTC time stamp according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) (exact to 100 ns) | [`utclong`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md)     |

See [Date Fields, Time Fields, and Time Stamp Fields](abenddic_date_time_types.md).

### Character-Like Types with Special Semantics

| **Type** | **Valid Places `m`** | **Initial Value** | **Meaning**                                  | **ABAP Type**                                       |
|----------|----------------------|-------------------|----------------------------------------------|-----------------------------------------------------|
| `NUMC`   | 1-255                | `m` zeros         | [Numeric text](../../abap-glossary/abennumeric_text_glosry.md) | [`n`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), length `m` |
| `CLNT`   | 3                    | 000               | Client                                       | `c`, length 3                                       |
| `LANG`   | 1                    | Blank             | Language key                                 | `c`, length 1                                       |

See [Special Character-Like Types](abenddic_special_character_types.md).

### Currency Fields and Quantity Fields

| **Type** | **Valid Places `m`** | **Decimal Places `n`** | **Initial Value** | **Meaning**                                                                                             | **ABAP Type**                                                                   |
|----------|----------------------|------------------------|-------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| `CURR`   | 1-31                 | 1-`m`, maximum 14      | 0                 | [Currency field](../../abap-glossary/abencurrency_field_glosry.md) in [BCD](../../abap-glossary/abenbcd_glosry.md) format                   | [`p`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), length `m DIV 2 + 1`, decimal places `n` |
| `CUKY`   | 5                    | \-                     | 5 blanks          | [Currency key](../../abap-glossary/abencurrency_key_glosry.md) for [currency fields](../../abap-glossary/abenddic_currency_field_glosry.md) | `c`, length 5                                                                   |
| `QUAN`   | 1-31                 | 0-`m`, maximum 14      | 0                 | [Quantity field](../../abap-glossary/abenddic_quantity_glosry.md) in [BCD](../../abap-glossary/abenbcd_glosry.md) format                    | [`p`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), length `m DIV 2 + 1`, decimal places `n` |
| `UNIT`   | 2-3                  | \-                     | 2 or 3 blanks     | [Unit key](../../abap-glossary/abenunit_glosry.md) of a [quantity field](../../abap-glossary/abenddic_quantity_glosry.md)                   | [`c`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), length `m`                             |

See [Currency Fields](abenddic_currency_field.md) and [Quantity Fields](abenddic_quantity_field.md).

### Geodata Types

| **Type**    | **Valid Places `m`** | **Initial Value** | **Meaning**                           | **ABAP Type**                               |
|-------------|----------------------|-------------------|---------------------------------------|---------------------------------------------|
| `GEOM_EWKB` | \-                   | Empty string      | Geometric data in EWKB representation | [`xstring`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) |

See [Geodata Types](abenddic_geo_data.md).
