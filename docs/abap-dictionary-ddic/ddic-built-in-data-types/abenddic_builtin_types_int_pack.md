---
title: "DDIC - Integers, Packed Numbers, Binary Floating Point Numbers"
source_file: abenddic_builtin_types_int_pack.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - General Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Integers, Packed Numbers, Binary Floating Point Numbers

The following dictionary data types are available to describe numeric types, except for decimal floating point numbers:

- [`INT1`](abenddic_builtin_types.md), [`INT2`](abenddic_builtin_types.md), [`INT4`](abenddic_builtin_types.md), [`INT8`](abenddic_builtin_types.md) for [integer numbers](../../abap-glossary/abeninteger_number_glosry.md)

  These types describe general 1-byte, 2-byte, 4-byte, and 8-byte integers. The dictionary types `INT1` and `INT2` are assigned to the ABAP types [`b`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and [`s`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). These ABAP types cannot be specified either statically or dynamically in ABAP statements. They can only be used in ABAP programs by reference to the built-in dictionary types `INT1` and `INT2`.

- [`DEC`](abenddic_builtin_types.md) for [packed numbers](../../abap-glossary/abenpacked_number_glosry.md)

  This type describes general packed numbers in [BCD format](../../abap-glossary/abenbcd_glosry.md). When used, a length and the number of decimal places must be added to the type. The number of decimal places must be less than or equal to the length and cannot exceed 14.

- [`FLTP`](abenddic_builtin_types.md) for [binary floating point numbers](../../abap-glossary/abenbinfloat_glosry.md)

  This type describes general binary floating point numbers. Table fields of this type cannot be used as [key fields](../ddic-database-tables/abenddic_database_tables_key.md) of DDIC database tables.

## Hints

- When defining data types based on the built-in type `DEC`, an odd number of places should be used. These values are stored in [BCD](../../abap-glossary/abenbcd_glosry.md) format, for which in ABAP (data type `p`), only an odd number of digits is possible, since a half byte is used for the sign. If a data type `DEC` has an even number of characters, the length of the associated ABAP type `p` is rounded up and hence contains the next highest odd number of places. This can cause overflows and exceptions when writing to DDIC database tables. The same applies to the built-in types `CURR`, `DF34_DEC`, `DF16_DEC`, and `QUAN`, which are handled technically like the type `DEC`,

- If the built-in dictionary types `INT1`, `INT2`, `INT4`, and `INT8` are [used](abenddic_builtin_type_usage.md) for typing, the number of places must usually be specified explicitly as 2, 5, 10, and 19. If the type `FLTP` is used, 16 places and the same number of decimal places must be specified. However, the specified number of places does not have any effect on the data types. By default, they describe platform-dependent integers or binary floating point numbers and occupy 1, 2, 4, or 8 bytes.

  - In the case of integer types, the specified places express the possible decimal places without sign.

  - In the case of binary floating point numbers, 16 expresses the approximate precision of the IEEE-754 (double precision) standard.

    The specified places are saved in the metadata of a user-defined type and are evaluated, if necessary, by special frameworks.
