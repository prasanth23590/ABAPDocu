---
title: "CDS DDL - CDS View Entity, cds_cond, Comparable Types"
source_file: abencds_cond_expr_types_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, cds_cond > CDS DDL - CDS View Entity, cds_cond, Comparison Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, cds_cond, Comparable Types

The following tables show which [built-in data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary can be compared with each other in a [condition](abencds_conditional_expression_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

- [Comparisons with Fields of Data Sources](abencds_cond_expr_types_v2.md#comparisons-with-fields-of-data-sources)

- [Comparisons with Parameters](abencds_cond_expr_types_v2.md#comparisons-with-parameters)

- [Comparisons with Literals](abencds_cond_expr_types_v2.md#comparisons-with-literals)

- [Comparisons with CDS Amount Fields and CDS Quantity Fields](abencds_cond_expr_types_v2.md#comparisons-with-cds-amount-fields-and-cds-quantity-fields)

## Comparisons with Fields of Data Sources

The following table shows the possible combinations of data source fields on the left side (`lhs`) with data source fields on the right side (`rhs`) of comparisons.

| **lhs/rhs**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`CLNT`** | **`LANG`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCLONG`** | **`ACCP`** | **`UNIT`** | **`CUKY`** | **`RAW`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------------|------------------|------------|------------|---------------|------------|------------|------------|------------|------------|------------|------------|---------------|------------|------------|------------|-----------|
| **`INT1`**       | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT2`**       | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT4`**       | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT8`**       | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DEC`**        | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CURR`**       | \-         | \-         | \-         | \-         | \-        | d          | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`QUAN`**       | a          | a          | a          | \-         | a         | \-         | a          | a                | a                | a          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`FLTP`**       | x          | x          | x          | x          | x         | \-         | a          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CHAR`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | m          | l          | x          | x          | x          | \-         | \-         | \-            | x          | x          | x          | \-        |
| **`SSTRING`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-            | x          | x          | x          | \-        |
| **`NUMC`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | m          | \-            | l          | l          | \-         | l          | l          | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CLNT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | l          | \-            | l          | x          | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`LANG`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DATS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | \-            | l          | \-         | \-         | x          | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`TIMS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | \-            | l          | \-         | \-         | \-         | x          | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DATN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-            | \-         | \-         | \-         | \-        |
| **`TIMN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-            | \-         | \-         | \-         | \-        |
| **`UTCLONG`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x             | \-         | \-         | \-         | \-        |
| **`ACCP`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | x          | \-         | \-         | \-        |
| **`UNIT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | x          | \-         | \-        |
| **`CUKY`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | x          | \-        |
| **`RAW`**        | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | l         |

- There are no restrictions for combinations using *x*.

- In combinations using *l*, the lengths of the compared columns must match exactly.

- For combinations using *m*, the length is relevant: the field of type `NUMC` can have the same lengths or fewer characters than the field of type `CHAR`. If the field of type `NUMC` is longer than the field of type `CHAR`, a syntax error occurs.

- For combinations using *d*, the number of decimal places must match exactly.

  - **Note:** Operands of data type `CURR` can be cast to data type `DECFLOAT34` using the conversion function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) to avoid length requirements.

- For combinations using *a*, both operands must be specified as [ABAP CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md) by adding a reference to a [unit of measurement key](../../abap-glossary/abenunit_glosry.md) using the annotation [`@Semantics.quantity.unitOfMeasure`](abencds_f1_element_annotation.md). Otherwise, a syntax check warning occurs.

  - **Note:** You can use the conversion function [`GET_NUMERIC_VALUE`](abencds_conv_func_unit_curr_v2.md) to turn quantity fields into regular fields of data type `DECFLOAT34`.

## Comparisons with Parameters

The following table shows the possible combinations of data source fields on the left side (`lhs`) with parameters on the right side (`rhs`) of comparisons.

| **lhs/rhs**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`CLNT`** | **`LANG`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCLONG`** | **`ACCP`** | **`UNIT`** | **`CUKY`** | **`RAW`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------------|------------------|------------|------------|---------------|------------|------------|------------|------------|------------|------------|------------|---------------|------------|------------|------------|-----------|
| **`INT1`**       | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT2`**       | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT4`**       | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT8`**       | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DEC`**        | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CURR`**       | \-         | \-         | \-         | \-         | \-        | d          | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`QUAN`**       | \-         | \-         | \-         | \-         | \-        | \-         | x          | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`FLTP`**       | x          | x          | x          | x          | x         | \-         | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CHAR`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | m          | l          | x          | x          | x          | \-         | \-         | \-            | \-         | x          | x          | \-        |
| **`SSTRING`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-            | \-         | x          | x          | \-        |
| **`NUMC`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | m          | \-            | l          | l          | \-         | l          | l          | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CLNT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | l          | \-            | l          | x          | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`LANG`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DATS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | \-            | l          | \-         | \-         | x          | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`TIMS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | \-            | l          | \-         | \-         | \-         | x          | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DATN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | x          | \-         | \-            | \-         | \-         | \-         | \-        |
| **`TIMN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | x          | \-            | \-         | \-         | \-         | \-        |
| **`UTCLONG`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | x             | \-         | \-         | \-         | \-        |
| **`ACCP`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`UNIT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | x          | \-         | \-        |
| **`CUKY`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | \-         | \-         |            | \-         | \-         | --            | \-         | \-         | x          | \-        |
| **`RAW`**        | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | l         |

- There are no restrictions for combinations using *x*.

- In combinations using *l*, the lengths of the compared operands must match exactly.

- For combinations using *m*, the length is relevant: the field of type `NUMC` can have the same lengths or less characters than the field of type `CHAR`. If the field of type `NUMC` is longer than the field of type `CHAR`, a syntax error occurs.

- For combinations using *d*, the number of decimal places must match exactly.

  - **Note:** Operands of data type `CURR` can be cast to data type `DECFLOAT34` using the conversion function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) to avoid this length requirement.

## Comparisons with Literals

The following table shows the possible combinations of data source fields on the left side (`lhs`) with literals on the right side (`rhs`) of comparisons. The literals can be [typed](abencds_typed_literal_v2.md) or [untyped](abencds_untyped_literal_v2.md). It is recommended that only typed literals are used, because they offer more data types. With typed literals, the data types shown in the table are possible.

| **lhs/rhs**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`FLTP`** | **`CHAR`** | **`NUMC`** | **`RAW`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCL`** | **`DECFLOAT16`** | **`DECFLOAT34`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------|------------|------------|-----------|------------|------------|------------|------------|------------|------------------|------------------|
| **`INT1`**       | y          | y          | y          | y          | y         | \-         | y          | y          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | y                | y                |
| **`INT2`**       | x          | y          | y          | y          | y         | \-         | y          | y          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | y                | y                |
| **`INT4`**       | x          | x          | y          | y          | y         | \-         | y          | y          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | y                | y                |
| **`INT8`**       | x          | x          | x          | y          | y         | \-         | y          | y          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | y                | y                |
| **`DEC`**        | x          | x          | x          | x          | d         | \-         | d          | d          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | m                | m                |
| **`CURR`**       | m          | m          | m          | m          | d         | d          | d          | d          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | m                | m                |
| **`QUAN`**       | m          | m          | m          | m          | d         | \-         | d          | d          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | m                | m                |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | \-         | x          | x          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | x                | x                |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | \-         | x          | x          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | x                | x                |
| **`FLTP`**       | x          | x          | x          | x          | x         | \-         | x          | x          | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | x                | x                |
| **`CHAR`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | m          | m          | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`SSTRING`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | m          | \-         | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`NUMC`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | l          | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`CLNT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | l          | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`LANG`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | l          | l          | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`DATS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | l          | \-        | x          | \-         | \-         | \-         | \-         | \-               | \-               |
| **`TIMS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | l          | \-        | \-         | x          | \-         | \-         | \-         | \-               | \-               |
| **`DATN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | \-        | \-         | \-         | x          | \-         | \-         | \-               | \-               |
| **`TIMN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | x          | \-         | \-               | \-               |
| **`UTCL`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | x          | \-               | \-               |
| **`ACCP`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | l          | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`UNIT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | m          | \-         | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`CUKY`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | m          | \-         | \-        | \-         | \-         | \-         | \-         | \-         | \-               | \-               |
| **`RAW`**        | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-         | \-         | \-         | l         | \-         | \-         | \-         | \-         | \-         | \-               | \-               |

- There are no restrictions for combinations using *x*.

- For combinations using *y*, the literal value must be within the value range of the respective type. That means:

  - For a comparison with `INT1`, the literal value must be between 0 and 255.

  - For a comparison with `INT2`, the literal value must be between -32,768 and +32,767.

  - For a comparison with `INT4`, the literal value must be between -2,147,483,648 and +2,147,483,647.

  - For a comparison with `INT8`, the literal value must be between -9,223,372,036,854,775,808 and +9,223,372,036,854,775,807.

- For combinations using *m*, the length of the literal cannot be greater than the column.

- For combinations using *d*, the length of the literal and the number of decimal places cannot be greater than the length and number for the column.

- For combinations using *l*, the length of the literal must be equal to the length of the column.

- If the literal on the right side (`rhs`) is of data type `CURR`, it must have exactly two decimal places. Since the number of decimal places of `rhs` and `lhs` must match exactly, `lhs` must also have exactly two decimal places. The conversion functions [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) and [`GET_NUMERIC_VALUE`](abencds_conv_func_unit_curr_v2.md) can be used to avoid this length requirement.

## Comparisons with CDS Amount Fields and CDS Quantity Fields

If one of the operands `lhs` or `rhs` of a comparison is a [CDS amount field](../../abap-glossary/abencds_amount_field_glosry.md), a [CDS quantity field](../../abap-glossary/abencds_quantity_glosry.md), or a [CDS calculated quantity](../../abap-glossary/abencds_calculated_quantity_glosry.md), special rules apply:

- Both operands `lhs` and `rhs` must have the same reference type. Both must be either amounts, or quantities, or calculated quantities. Comparing operands with references of different types ([currency key](../../abap-glossary/abencurrency_key_glosry.md), [unit key](../../abap-glossary/abenunit_glosry.md), or [calculated unit](../../abap-glossary/abencds_calculated_unit_glosry.md)) results in a syntax check warning.

- An operand of type `CURR` can only be compared with another operand of type `CURR`. The number of decimal places of both operands must match exactly.

  - **Exception:** If `lhs` has data type `CURR` and `rhs` is specified as literal, the following data types are possible for `rhs`: `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `CURR`, `QUAN`, `FLTP`, `DECFLOAT16`, `DECFLOAT34`.

- Two conversion functions are available to circumvent limitations:

  - [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) converts an amount field of type `CURR` to an amount field of type `DECFLOAT34`.

  - [`GET_NUMERIC_VALUE`](abencds_conv_func_unit_curr_v2.md) convert amounts and quantities into regular fields.

    In the [`ON` condition of a CDS association](abencds_simple_association_v2.md), these two conversion functions are not available, since functions in general are not supported in the `ON` condition of a CDS association.

The following table shows the possible combinations of operands in comparisons. `Number` refers to an operand of a numeric data type without reference annotation that turns it into an amount or quantity field.

<table>
<thead>
<tr class="header">
<th><strong>Type of Operand</strong></th>
<th><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>amount, number</td>
<td><p>syntax check warning</p>
<p><strong>Exception:</strong>: If <code class="ph codeph">number</code> is specified as literal, no syntax check warning occurs.</p></td>
</tr>
<tr class="even">
<td>amount, amount</td>
<td>OK. Elements of data type <code class="ph codeph">CURR</code> must have exactly the same number of decimal places.</td>
</tr>
<tr class="odd">
<td>quantity, number</td>
<td><p>syntax check warning</p>
<p><strong>Exception:</strong> If <code class="ph codeph">number</code> is specified as literal, no syntax check warning occurs.</p></td>
</tr>
<tr class="even">
<td>quantity, quantity</td>
<td>OK</td>
</tr>
<tr class="odd">
<td>amount, quantity</td>
<td>syntax check warning</td>
</tr>
<tr class="even">
<td>amount, calculated quantity</td>
<td>syntax check warning</td>
</tr>
<tr class="odd">
<td>quantity, calculated quantity</td>
<td>syntax check warning</td>
</tr>
<tr class="even">
<td>calculated quantity, number</td>
<td><p>syntax check warning</p>
<p><strong>Exception:</strong> If <code class="ph codeph">number</code> is specified as literal, no syntax check warning occurs.</p></td>
</tr>
<tr class="odd">
<td>calculated quantity, calculated quantity</td>
<td>OK</td>
</tr>
</tbody>
</table>

Undesirable comparisons of operands with references of different types result in a syntax check warning. There is no syntax check error to ensure downward compatibility.

The exception that amounts, quantities, and calculated quantities can be compared with a number if the number is specified as literal is in place to ensure downward compatibility.
