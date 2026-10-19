---
title: "ABAP CDS - Built-In Data Types"
source_file: abencds_overview_builtin_types.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Built-In Data Types

The [built-in data types](../../abap-glossary/abencds_built_in_type_glosry.md) of ABAP CDS are based on the [built-in dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and the same rules apply as for the corresponding built-in dictionary types. The built-in data types in ABAP CDS are written with the domain prefix `abap`, a period (*.*), and the name of the data type.

The following table lists all available built-in CDS data types and the corresponding dictionary type they can be mapped to. The third column indicates whether a data type can be used for [typing](../abap-cds-data-definitions/abencds_typing.md) of a [CDS element](../../abap-glossary/abencds_element_glosry.md). The fourth column indicates whether a data type can be used for [typing](../abap-cds-data-definitions/abencds_typing.md) of a [CDS parameter](../../abap-glossary/abencds_parameter_glosry.md). The fifth column indicates whether a data type can be used in a [cast expression](../abap-cds-data-definitions/abencds_cast_expression_v2.md).

| **Notation**         | **Built-In Data Type in ABAP Dictionary**                                             | **Element Typing** | **Parameter Typing** | **Cast Target** |
|----------------------|---------------------------------------------------------------------------------------|--------------------|----------------------|-----------------|
| `abap.char( len )`   | [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len`                               | x                  | x                    | x               |
| `abap.clnt[(3)]`     | [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.cuky[(5)]`     | [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.curr(len,dec)` | [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and with `dec` decimal places | x                  | x                    | x               |
| `abap.d16n[(16)]`    | [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                           | x                  | x                    | x               |
| `abap.d34n[(34)]`    | [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                           | x                  | x                    | x               |
| `abap.datn[(8)]`     | [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.dats[(8)]`     | [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.dec(len,dec)`  | [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and with `dec` decimal places  | x                  | x                    | x               |
| `abap.fltp[(16,16)]` | [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.geom_ewkb`     | [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                            | x                  | \-                   | \-              |
| `abap.int1[(3)]`     | [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.int2[(5)]`     | [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.int4[(10)]`    | [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.int8[(19)]`    | [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.lang[(1)]`     | [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.numc( len )`   | [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len`                               | x                  | x                    | x               |
| `abap.quan(len,dec)` | [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and with `dec` decimal places | x                  | x                    | x               |
| `abap.raw(len)`      | [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len`                                | x                  | x                    | \-              |
| `abap.rawstring`     | [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                            | x                  | \-                   | \-              |
| `abap.sstring(len)`  | [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len`                            | x                  | x                    | x               |
| `abap.string`        | [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                               | x                  | \-                   | \-              |
| `abap.timn[(6)]`     | [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.tims[(6)]`     | [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                 | x                  | x                    | x               |
| `abap.unit[(2\|3)]`  | [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `2` or `3` (standard length)        | x                  | x                    | x               |
| `abap.utcl[(27)]`    | [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                              | x                  | x                    | x               |

`len` and `dec` must be used to specify values for the length and decimal places of the respective generic types. The values specified here in parentheses must be within the value ranges allowed by ABAP Dictionary. For data types with fixed lengths and decimal places, it is possible, but not mandatory to specify the predefined value for length and decimal places. The exception in this regard is `abap.accp`: this type has the predefined length of 6, which must always be specified in parentheses.

In [CDS simple types](../../abap-glossary/abencds_simple_type_glosry.md), all of the data types listed above can be used for [typing](../abap-cds-data-definitions/abencds_define_simple_type.md) except for `abap.accp` and `abap.fltp`. The data type `abap.accp` is deprecated. Instead of `abap.fltp`, a [decimal floating point number type](../../abap-glossary/abendecfloat_type_glosry.md) can be used.

In [CDS table entities](../../abap-glossary/abencds_table_entity_glosry.md), all of the data types listed above can be used for typing except for `abap.accp`, `abap.clnt`, `abap.dats`, `abap.tims`, and `abap.geom_ewkb`.
