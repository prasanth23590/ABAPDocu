---
title: "DDIC - Decimal Floating Point Numbers"
source_file: abenddic_decimal_floating_point.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - General Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Decimal Floating Point Numbers

In [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md), a maximum of 16 or 34 places exactly are returned in the mantissa depending on the data type.

- [Handling in ABAP Dictionary](abenddic_decimal_floating_point.md#handling-in-abap-dictionary)

  - [Decimal Floating Point Types](abenddic_decimal_floating_point.md#decimal-floating-point-types)

  - [Replacement Types](abenddic_decimal_floating_point.md#replacement-types)

- [Handling in ABAP Programs](abenddic_decimal_floating_point.md#handling-in-abap-programs)

## Handling in ABAP Dictionary

In ABAP Dictionary, the following data types are available for decimal floating numbers.

### Decimal Floating Point Types

The following built-in ABAP Dictionary data types represent real floating point types of a database:

- [`DECFLOAT16`](abenddic_builtin_types.md) for 16-digit numbers.

- [`DECFLOAT34`](abenddic_builtin_types.md) for 34-digit numbers.

They can be used, without restrictions, as numeric data types in appropriate expressions. They are currently only supported by [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md).

### Replacement Types

The following built-in data types in ABAP Dictionary are used as replacements for real decimal floating point types:

- [`DF16_DEC`](abenddic_builtin_types.md) and [`DF16_RAW`](abenddic_builtin_types.md) for 16-digit numbers.

- [`DF34_DEC`](abenddic_builtin_types.md) and [`DF34_RAW`](abenddic_builtin_types.md) for 34-digit numbers.

These types can be used as replacements on database systems that do not support decimal floating point types. They are mainly used to save decimal floating point numbers from ABAP programs and can be used in a limited way as numeric data types in appropriate expressions:

- `DF16_DEC` and `DF34_DEC`

  In database fields of this type, decimal floating point numbers are stored as a packed number (type [`DEC`](abenddic_builtin_types_int_pack.md)). The length and the number of decimal places must be specified when defining a data type in ABAP Dictionary. For this type, restricted operations can be performed on the database:

  - No operands of these types can be used in [arithmetic SQL expressions](../../abap-programming-language/abap-database-access/abensql_arith.md) or [numeric SQL functions](../../abap-programming-language/abap-database-access/abensql_arith_func.md).

  - Columns, but no SQL expressions of these types, can be used as operands in the [aggregate functions](../../abap-programming-language/abap-database-access/abapselect_aggregate.md) except for `STRING_AGG`.

  - In the statement [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md), operations with these types are possible with [`SET` `+` and `-`](../../abap-programming-language/abap-database-access/abapupdate_set_expression.md).

  - Database fields with these types can be processed in [AMDP](../../abap-glossary/abenamdp_glosry.md).

  - When there is a write to the database, the system implicitly rounds off to the number of decimal places and decimal overflows can occur.

- `DF16_RAW` and `DF34_RAW`

  In database fields of this type, decimal floating point numbers are stored as binary (in `RAW` format). The length is set to 16 or 34 places. Values can be sorted, compared, and used in indexes. For this type, no calculations can be performed on the database. This is an SAP-specific format, which means that the corresponding fields also cannot be processed in [AMDP](../../abap-glossary/abenamdp_glosry.md). The scaling is lost when writing to the database.

### Hints

- If possible, the types `DECFLOAT16` and `DECFLOAT34` should be used.

- If it is necessary to work with the replacement types, the intended use case determines which type is to be used:

  - The types `DF16_DEC` and `DF34_DEC` can be used for calculations on the database, but their value ranges are smaller than those of real decimal floating point numbers.

  - The types `DF16_RAW` and `DF34_RAW` cover the whole value range, but are not recognized as numbers by the databases.

- As in the [general packed numbers](abenddic_builtin_types_int_pack.md), the number of places in the replacement types `DF16_DEC` and `DF34_DEC` should be odd.

- In [ABAP CDS](../../abap-core-data-services-abap-cds/abencds.md) it is not usually possible to execute expressions for the replacement types.

## Handling in ABAP Programs

The ABAP types that correspond to the 16- or 34-digit decimal floating numbers in ABAP Dictionary are `decfloat16` and `decfloat34`. They are handled internally according to the IEEE-754-2008 standard, and are supported by all ABAP operations. There is restricted support for floating point numbers with replacement types in [SQL expressions](../../abap-programming-language/abap-database-access/abapsql_expr.md). In [arithmetic SQL expressions](../../abap-programming-language/abap-database-access/abensql_arith.md), only those decimal floating point numbers are supported that are based on the decimal floating point types.

The addition `STYLE` after `WRITE [TO]` and the formatting option [`STYLE`](../../abap-programming-language/abap-processing-internal-data/abapcompute_string_format_options.md) in [embedded expressions](../../abap-programming-language/abap-processing-internal-data/abenstring_templates_expressions.md) are available for the formatting of decimal floating numbers in programs. These overwrite the output style defined in ABAP Dictionary. When the addition `CURRENCY` is used after `WRITE [TO]` for a decimal floating number defined in the ABAP Dictionary, it must be defined with the output style *Sign right*, otherwise an exception occurs.
