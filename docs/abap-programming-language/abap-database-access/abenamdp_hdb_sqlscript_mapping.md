---
title: "AMDP - Mapping of ABAP Types to SQLScript"
source_file: abenamdp_hdb_sqlscript_mapping.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods > METHOD, BY DATABASE PROCEDURE, FUNCTION, GRAPH WORKSPACE > AMDP - SQLScript for the SAP HANA Database"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Mapping of ABAP Types to SQLScript

Elementary ABAP types are mapped to the appropriate types in SQLScript as shown in the following tables. The type mapping includes:

- Interface parameters of an AMDP method

- References to ABAP types using the [AMDP macro](../../abap-glossary/abenamdp_macro_glosry.md) [`$ABAP.type`](abenamdp_abap_types.md)

The tables distinguish parameters that reference a type defined in ABAP from those that reference a [built-in type in the ABAP Dictionary](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). No parameters or type references can be defined for SQLScript types that are not listed here.

- [Mapping with Reference to Types Defined in ABAP](abenamdp_hdb_sqlscript_mapping.md#mapping-with-reference-to-types-defined-in-abap)

- [Mapping with Reference to Types Defined in ABAP Dictionary](abenamdp_hdb_sqlscript_mapping.md#mapping-with-reference-to-types-defined-in-abap-dictionary)

## Mapping with Reference to Types Defined in ABAP

**Numeric Types**

| **ABAP Type**                                | **HANA Type**                                        | **Note**                                                                               |
|----------------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------|
| `b`                                          | `SMALLINT`                                           | `SMALLINT` is a two byte integer with sign                                             |
| `s`                                          | `SMALLINT`                                           | `SMALLINT` is a two byte integer with sign                                             |
| `i`                                          | `INTEGER`                                            | \-                                                                                     |
| `int8`                                       | `BIGINT`                                             | \-                                                                                     |
| `p`, length `leng` with `dec` decimal places | `DECIMAL`, length `2len-1` with `dec` decimal places | \-                                                                                     |
| `decfloat16`                                 | `VARBINARY`, length 8                                | Cannot be interpreted as a number in the database and no calculations can be performed |
| `decfloat34`                                 | `VARBINARY`, length 16                               | Cannot be interpreted as a number in the database and no calculations can be performed |
| `f`                                          | `DOUBLE`                                             | \-                                                                                     |

**Character-Like Types**

| **ABAP Type**     | **HANA Type**            | **Note**                                                                                                                                                                      |
|-------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`, length `len` | `NVARCHAR`, length `len` | \-                                                                                                                                                                            |
| `string`          | `NCLOB`                  | Not allowed for input/output parameters                                                                                                                                       |
| `n`, length `len` | `NVARCHAR`, length `len` | A suitable casting to a numeric database type must be performed before calculations can be made in the database. Numeric results must be transformed back to the ABAP format. |

**Byte-Like Types**

| **ABAP Type**     | **HANA Type**             | **Note**                                |
|-------------------|---------------------------|-----------------------------------------|
| `x`, length `len` | `VARBINARY`, length `len` | \-                                      |
| `xstring`         | BLOB                      | Not allowed for input/output parameters |

**Date Types, Time Types, and Time Stamp Types**

| **ABAP Type** | **HANA Type**          | **Note**                                                                                                                                               |
|---------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `d`           | `NVARCHAR`, length `8` | A casting to the `DATE` type of the database must be performed before date calculations can be made. SQLScript offers the built-in function `to_dats`. |
| `t`           | `NVARCHAR`, length `6` | A casting to the `TIME` type of the database must be performed before time calculations can be made. SQLScript offers the built-in function `to_tims`. |
| `utclong`     | `TIMESTAMP`            | \-                                                                                                                                                     |

## Mapping with Reference to Types Defined in ABAP Dictionary

The [built-in types in ABAP Dictionary](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are mapped like the associated ABAP types, with the following exceptions.

| **Dictionary Type**                                 | **HANA Type**                                        | **Note**                                            |
|-----------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|
| `DECFLOAT16`                                        | `SMALLDECIMAL`                                       | Recommended mapping                                 |
| `DECFLOAT34`                                        | `DECIMAL`                                            | Recommended mapping                                 |
| `DF16_DEC`, length `leng` with `dec` decimal places | `DECIMAL`, length `2len-1` with `dec` decimal places | Value range on the database is smaller than in ABAP |
| `DF34_DEC`, length `leng` with `dec` decimal places | `DECIMAL`, length `2len-1` with `dec` decimal places | Value range on the database is smaller than in ABAP |
| `DF16_SCL`                                          | \-                                                   | Obsolete, not supported                             |
| `DF34_SCL`                                          | \-                                                   | Obsolete, not supported                             |
| `DATN`                                              | `DATE`                                               | Recommended mapping                                 |
| `TIMN`                                              | `TIME`                                               | Recommended mapping                                 |
| `GEOM_EWKB`                                         | `ST_GEOMETRY`                                        | Recommended mapping                                 |
| `SSTRING`, length `len`                             | `NVARCHAR`, length `len`                             | \-                                                  |

### Hint

In the recommended mappings, the ABAP type should be defined with reference to the built-in ABAP Dictionary type to define the more suitable HANA type.
