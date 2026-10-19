---
title: "CDS DDL - DDIC-Based View, cds_cond, Comparable Types"
source_file: abencds_cond_expr_types_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, cds_cond > CDS DDL - DDIC-Based View, cds_cond, Comparison Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cds_cond, Comparable Types

The following tables show which [built-in data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary can be compared with each other in a [condition](abencds_conditional_expression_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- [Comparisons with Fields of Data Sources](abencds_cond_expr_types_v1.md#comparisons-with-fields-of-data-sources)

- [Comparisons with Parameters](abencds_cond_expr_types_v1.md#comparisons-with-parameters)

- [Comparisons with Literals](abencds_cond_expr_types_v1.md#comparisons-with-literals)

## Comparisons with Fields of Data Sources

The following table shows the possible combinations of data source fields [`data_source`](abencds_data_source_v1.md) on the left side (`lhs`) with data source fields on the right side (`rhs`) of [comparisons](abencds_cond_expr_comp_v1.md).

| **lhs/rhs**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`CLNT`** | **`LANG`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCLONG`** | **`ACCP`** | **`UNIT`** | **`CUKY`** | **`RAW`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------------|------------------|------------|------------|---------------|------------|------------|------------|------------|------------|------------|------------|---------------|------------|------------|------------|-----------|
| **`INT1`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT2`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT4`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT8`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DEC`**        | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CURR`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`QUAN`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`FLTP`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CHAR`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | x          | l          | x          | x          | x          | \-         | \-         | \-            | x          | x          | x          | \-        |
| **`SSTRING`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-            | x          | x          | x          | \-        |
| **`NUMC`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | \-            | l          | l          | \-         | l          | l          | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
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

## Comparisons with Parameters

The following table shows the possible combinations of data source fields [`data_source`](abencds_data_source_v1.md) on the left side (`lhs`) with [parameters](abencds_parameter_v1.md) on the right side (`rhs`) of [comparisons](abencds_cond_expr_comp_v1.md).

| **lhs/rhs**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`CLNT`** | **`LANG`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCLONG`** | **`ACCP`** | **`UNIT`** | **`CUKY`** | **`RAW`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------------|------------------|------------|------------|---------------|------------|------------|------------|------------|------------|------------|------------|---------------|------------|------------|------------|-----------|
| **`INT1`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT2`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT4`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`INT8`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DEC`**        | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CURR`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`QUAN`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`FLTP`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
| **`CHAR`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | x          | l          | x          | x          | x          | \-         | \-         | \-            | \-         | x          | x          | \-        |
| **`SSTRING`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | x          | \-         | \-         | \-         | \-         | \-            | \-         | x          | x          | \-        |
| **`NUMC`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | \-            | l          | l          | \-         | l          | l          | \-         | \-         | \-            | \-         | \-         | \-         | \-        |
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

## Comparisons with Literals

The following table shows the possible combinations of data source fields [`data_source`](abencds_data_source_v1.md) on the left side (`lhs`) with [literals](abencds_literal_v1.md) on the right side (`rhs`) of [comparisons](abencds_cond_expr_comp_v1.md). The data types of literals are determined by their content (as described [here](abencds_literal_v1.md)) and only the data types shown in the table are possible.

| **lhs/rhs**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`FLTP`** | **`CHAR`** | **`NUMC`** |
|------------------|------------|------------|------------|------------|------------|------------|------------|
| **`INT1`**       | x          | v          | \-         | \-         | \-         | \-         | \-         |
| **`INT2`**       | x          | x          | v          | \-         | \-         | \-         | \-         |
| **`INT4`**       | x          | x          | x          | v          | \-         | \-         | \-         |
| **`INT8`**       | x          | x          | x          | v          | \-         | \-         | \-         |
| **`DEC`**        | x          | x          | x          | x          | d          | \-         | \-         |
| **`CURR`**       | l          | l          | l          | l          | d          | \-         | \-         |
| **`QUAN`**       | l          | l          | l          | l          | d          | \-         | \-         |
| **`DECFLOAT16`** | x          | x          | x          | x          | \-         | \-         | \-         |
| **`DECFLOAT34`** | x          | x          | x          | x          | \-         | \-         | \-         |
| **`FLTP`**       | \-         | \-         | \-         | \-         | \-         | \-         | \-         |
| **`CHAR`**       | \-         | \-         | \-         | \-         | \-         | m          | m          |
| **`SSTRING`**    | \-         | \-         | \-         | \-         | \-         | m          | \-         |
| **`NUMC`**       | \-         | \-         | \-         | \-         | \-         | \-         | l          |
| **`CLNT`**       | \-         | \-         | \-         | \-         | \-         | \-         | l          |
| **`LANG`**       | \-         | \-         | \-         | \-         | \-         | l          | l          |
| **`DATS`**       | \-         | \-         | \-         | \-         | \-         | \-         | l          |
| **`TIMS`**       | \-         | \-         | \-         | \-         | \-         | \-         | l          |
| **`ACCP`**       | \-         | \-         | \-         | \-         | \-         | \-         | l          |
| **`UNIT`**       | \-         | \-         | \-         | \-         | \-         | m          | \-         |
| **`CUKY`**       | \-         | \-         | \-         | \-         | \-         | m          | \-         |
| **`RAW`**        | \-         | \-         | \-         | \-         | \-         | \-         | \-         |

- There are no restrictions for combinations using *x*.

- For the combination using *v*, the literal value must be within the following value range:

  - Comparison of `INT1`(`lhs`) with `INT2`(`rhs`): between 0 and 999.

  - Comparison of `INT2`(`lhs`) with `INT4`(`rhs`): between -99,999 and +99,999.

  - Comparison of `INT4`(`lhs`) with `INT8`(`rhs`): between -9,999,999,999 and +9,999,999,999.

  - Comparison of `INT8`(`lhs`) with `INT8`(`rhs`): between -9,223,372,036,854,775,808 and +9,223,372,036,854,775,807.

- For combinations using *m*, the length of the literal cannot be greater than the column.

- For combinations using *d*, the length of the literal and the number of decimal places cannot be greater than the length and number for the column.

- For combinations using *l*, the length of the literal must be equal to the length of the column.
