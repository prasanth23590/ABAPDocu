---
title: "SELECT, Assignment Rules"
source_file: abenselect_into_conversion.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, INTO, APPENDING"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Assignment Rules

The following assignment rules apply to assignments of the result fields of the result set of a standalone [`SELECT`](abapselect.md), [`WITH`](abapwith.md), or `FETCH` statement to the target fields defined in the [`INTO`](abapinto_clause.md) clause.

- [Prerequisites](abenselect_into_conversion.md#prerequisites)

- [Rules](abenselect_into_conversion.md#rules)

## Prerequisites

The following table shows the prerequisites for assigning individual columns of the result set to individual data objects, that is, for all forms of the `SELECT` statement, except when all columns in a work area `wa` are read with `*` and `CORRESPONDING FIELDS` is not specified at the same time. The table shows which data types of the result set can be assigned to which ABAP data types.

| **Data Type of Column in Result Set**                         | **ABAP Data Type**                |
|---------------------------------------------------------------|-----------------------------------|
| `CHAR`, `CLNT`, `CUKY`, `LANG`, `SSTRING`, `STRING`, `UNIT`   | `c`, `string`                     |
| `ACCP`, `NUMC`                                                | `c`, `n`                          |
| `LCHR`                                                        | `c`                               |
| `RAW`, `RAWSTRING`, `GEOM_EWKB`                               | `x`, `xstring`                    |
| `LRAW`                                                        | `x`                               |
| `DF16_DEC`                                                    | `decfloat16`, `decfloat34`        |
| `DECFLOAT16`, `DF16_RAW`, `DF16_SCL` (obsolete)               | `decfloat16`                      |
| `DECFLOAT34`, `DF34_DEC`, `DF34_RAW`, `DF34_SCL` (obsolete)   | `decfloat34`                      |
| `CURR`, `DEC`, `INT1`, `INT2`, `INT4`, `INT8`, `PREC`, `QUAN` | (`b`, `s`,) `i`, `int8`, `p`, `f` |
| `FLTP`                                                        | `f`                               |
| `DATN`, `DATS`                                                | `d`                               |
| `TIMN`, `TIMS`                                                | `t`                               |
| `UTCLONG`                                                     | `utclong`                         |

### Hints

- Fields of the types `STRING` and `RAWSTRING` ([LOBs](../../abap-glossary/abenlob_glosry.md)) from the result set can be assigned to reference variables for [LOB handles](abenselect_into_lob_handles.md) as well as to strings. The static type of these reference variables must be one of the system classes or one of the system interfaces that support [streaming and locators](abenstreams_locators.md) for ABAP SQL.

- Fields cannot be assigned to [enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md), even if their [base type](../../abap-glossary/abenbase_type_glosry.md) would be an allowed ABAP type.

## Rules

The assignments are made according to the following rules:

- If the target field is of data type `c` or `x`, the content of the result field is inserted left-aligned into the target field. If the target field is too short, the result is truncated to the right. If the target field is too long, spaces or hexadecimal 0 are filled to the right.

- If the target field is of data type `string` or `xstring`, the content of the result field is inserted left-aligned into the target field. In result fields of the type `STRING`, the trailing blanks are transferred. The target field has the same length as the result field.

- If the target field is of data type `n`, the content of the result field is inserted right-aligned into the target field. If necessary, it is padded with zeros on the left. If the target field is too short, the result is truncated to the left.

- If the target field has a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md), the value of the result field is converted to this data type and the [value range](../../abap-glossary/abenvalue_range_glosry.md) of the target field must be large enough. Here, any surplus decimal places in result fields of the type `CURR`, `DEC`, or `QUAN` (numbers in the [BCD](../../abap-glossary/abenbcd_glosry.md) format) are cut off.

- If the result field contains a [null value](../../abap-glossary/abennull_value_glosry.md), a type-dependent initial value is assigned to the target field.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The variable `result1` is given the value 1. Any surplus decimal places are cut off. The built-in SQL function [`ROUND`](abensql_arith_func.md) can be used to perform roundings like in [conversions](../abap-processing-internal-data/abenconversion_rules.md) in ABAP. `result2` is given the value 2.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( id   = 'X' 
                                         dec2 = '1.9999999999' ) ). 
 
DATA result1 TYPE i. 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS dec2 
       WHERE id = 'X' 
       INTO (@result1). 
 
DATA result2 TYPE i. 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS ROUND( dec2,0 ) AS dec2 
       WHERE id = 'X' 
       INTO (@result2).
```
