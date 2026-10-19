---
title: "Mapping of Dictionary to ABAP Types"
source_file: abapmapping_ddic_abap.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Mapping of Dictionary to ABAP Types

As outlined in [DDIC - Overview of All Built-In Dictionary Types](abenddic_builtin_types.md), built-in dictionary types are mapped to built-in ABAP types. However, there is no one-to-one relationship between elementary dictionary types and ABAP types. Multiple dictionary types can map to the same ABAP type. For example, the dictionary types `DF34_RAW`, `DF34_DEC`, and `DECFLOAT34` all map to the ABAP type `decfloat34`. A standard mapping exists between elementary dictionary types and ABAP types, where ABAP types are mapped to a specific dictionary type. Only these types are considered compatible. Strict compatibility checks are enforced in certain contexts, such as with [generic structures](../../abap-programming-language/abap-declarations/abapany_structure.md).

Standard mapping of dictionary to ABAP types:

| **ABAP Type** | **Dictionary Type** |
|---------------|---------------------|
| `c`           | `CHAR`              |
| `p`           | `DEC`               |
| `d`           | `DATS`              |
| `t`           | `TIMS`              |
| `x`           | `RAW`               |
| `n`           | `NUMC`              |
| `f`           | `FLTP`              |
| `b`           | `INT1`              |
| `s`           | `INT2`              |
| `i`           | `INT4`              |
| `int8`        | `INT8`              |
| `string`      | `STRING`            |
| `xstring`     | `RAWSTRING`         |
| `decfloat16`  | `DF16_RAW`          |
| `decfloat34`  | `DF34_RAW`          |
| `utclong`     | `UTCLONG`           |

**Note:** Strict compatibility checks are realized, for example, in the context of date and time types. This is especially relevant for date and time functions used in ABAP SQL `SELECT` statements. These functions work with `TIMN` and `DATN` types, not with `TIMS` and `DATS` (which represent the type `CHAR` with length 6 and 8 respectively). Likewise, calculation operations can be performed with the `DECFLOAT34` type, not, for example, with `DF34_RAW` (which represents the type `RAW` with length 16).
