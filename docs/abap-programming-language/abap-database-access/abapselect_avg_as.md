---
title: "sql_agg - AVG, AS"
source_file: abapselect_avg_as.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_agg > sql_agg - agg_func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_agg - AVG, AS

## Syntax

``` abap
... AVG( [DISTINCT] col AS dtype ) ...  
```

[`col`](abenabap_sql_columns.md)

## Description

Aggregate function [`AVG`](abensql_agg_func.md) in ABAP SQL with a data type `dtype` specified. The data type determines the result type in which the average value is returned. The data type of `col` must be numeric and have one of the types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The addition `AS` cannot yet be used for all types for [decimal floating point numbers](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_decimal_floating_point.md).

The data type `dtype` can have the built-in numeric type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The data type `FLTP`, however, can only be specified for operands of type `FLTP`. The data type `dtype` can be specified as follows:

- `DEC( len,decimals )`

- `CURR( len,decimals )`

- `QUAN( len,decimals )`

- `D16N` for `DECFLOAT16`

- `D34N` for `DECFLOAT34`

- `FLTP`

Length and decimal places must be specified with `len` and `decimals`. [Literals](abenabap_sql_literals.md) or [host constants](abenabap_sql_host_variables.md) of the [ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) `b`, `s`, `i`, or `int8` can be specified for `len` and `decimals`. The value range of the data type `dtype` should cover the value range of the operand type:

- If `col` is an integer type, a type `dtype` of type `DEC`, `CURR`, `QUAN` must have at least as many integer digits as is required by the value range of the respective integer type, that is, 3 for `INT1`, 5 for `INT2`, 10 for `INT4`, and 19 for `INT8`. There is no restriction on the number of decimal places.

- If `col` has type `DEC`, `CURR`, `QUAN`, a type `dtype` of type `DEC`, `CURR`, `QUAN` must have at least as many integer digits and decimal places.

The data types `DECFLOAT16` and `DECFLOAT34` can be used for all allowed data types of `col`. If the average value cannot be represented exactly in the data type `dtype`, the result is rounded commercially for decimal types.

**Note:** The usage of smaller result types (e.g. less digits) is possible, but not recommended. Overflows during execution may occur.

## Hints

- The addition `AS` to `AVG` bridges the gap for average values where the default result type `FLTP` cannot be cast to other numeric data types with [`CAST`](abensql_cast.md).

- Since average values usually have decimal places, integer types are not supported for `dtype`. If necessary, the type `DEC` can be used without decimal places.

- An aggregate expression `AVG` cannot be applied to operands with the data type `INT8` without using the addition `AS`. The addition `AS` can also be used to form average values for columns with data type `INT8`. However, for the types [`DF16_...`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF34_...`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), `AVG` is only possible without the addition `AS`.

- The actual calculation of the average value depending on the involved data types is platform dependent. This can lead to platform-dependent underflows, overflows and corresponding exceptions during the calculation. To prevent exceptions, the total of the values for which the average value is calculated should be within the value range of `dtype`.

- If `AS FLTP` is specified explicitly for operands of type `FLTP`, this ensures that the result of `AVG` has this type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Application of the aggregate function `AVG` to a column of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_SQL_AVG` implements this access to the table and can be executed to show the result.

``` abap
SELECT 
  FROM demo_expressions 
  FIELDS 
    AVG(          num1                ) AS avg_no_type, 
    AVG( DISTINCT num1                ) AS avg_no_type_distinct, 
    AVG(          num1 AS DEC( 10,0 ) ) AS avg_dec0, 
    AVG( DISTINCT num1 AS DEC( 10,0 ) ) AS avg_dec0_distinct, 
    AVG(          num1 AS DEC( 14,4 ) ) AS avg_dec4, 
    AVG( DISTINCT num1 AS DEC( 14,4 ) ) AS avg_dec4_distinct 
  INTO @FINAL(result).
```
