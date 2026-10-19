---
title: "CDS DDL - CDS View Entity, AVG, AS"
source_file: abencds_avg_as_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, aggr_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, AVG, AS

## Syntax

``` abap
... AVG( [DISTINCT] arg AS dtype ) ...  
```

## Description

Aggregate expression [`AVG`](abencds_aggregate_functions_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) specifying the data type `dtype`. The data type determines the result type in which the average value is returned.

The same can be specified for `arg` as for all [aggregate expressions](abencds_aggregate_functions_v2.md). The data type of `arg` must be numeric and have one of the types [`INT1`, `INT2`, `INT4`, `INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The data type `dtype` can have the built-in numeric type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The data type `dtype` can be specified as follows:

- Using a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) with an appropriate data type.

- Using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) with an appropriate data type.

- Directly as a [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary.

The following table shows the syntax for specifying built-in data types:

| **dtype**                         | **Dictionary Type**                                                                          |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| `abap.dec(len,decimals)`          | [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and `decimals` decimal places         |
| `abap.curr(len,decimals)`         | [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and `decimals` decimal places        |
| `abap.quan(len,decimals)`         | [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` with `decimals` decimal places       |
| `abap.decfloat16[(len,decimals)]` | [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` with `decimals` decimal places |
| `abap.decfloat34[(len,decimals)]` | [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` with `decimals` decimal places |
| `abap.fltp[(16,16)]`              | [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                        |

The value range of the data type `dtype` must cover the value range of the type of `arg`:

- If `arg` is an integer type, a type `dtype` of type `DEC` or `QUAN` must have at least as many integer digits as is required by the value range of the respective integer type, that is, 3 for `INT1`, 5 for `INT2`, 10 for `INT4`, and 19 for `INT8`. There is no restriction on the number of decimal places.

- If `arg` has type `DEC` or `QUAN`, then `dtype` of type `DEC` or `QUAN` must have at least as many integer digits and decimal places.

- If `arg` has the data type `DECFLOAT16`, then `dtype` must be `DECFLOAT16` or `DECFLOAT34`. If `arg` has the data type `DECFLOAT34`, then the target data type `dtype` must also be `DECFLOAT34`.

- If `arg` has type `FLTP`, this type must also be specified for `dtype`.

- If `arg` has type `CURR`, this type must also be specified for `dtype` and the number of decimal places must match exactly.

- If `arg` has any other type except `CURR` and `dtype` is specified as `CURR`, then `dtype` must have exactly two decimal places.

If the average value cannot be represented exactly in the data type `dtype`, the result is rounded commercially.

If `arg` is assigned a currency key using the annotation [`Semantics.amount.currencyCode`](abencds_f1_element_annotation.md), then the result field must also be assigned a currency key using the same annotation.

If `arg` is assigned a unit of measurement key using the annotation [`Semantics.quantity.unitofMeasure`](abencds_f1_element_annotation.md), then the result field must also be assigned a unit of measurement key using the same annotation.

## Hints

- The addition `AS` to `AVG` bridges the gap for average values where `FLTP` cannot be cast to other numeric data types with [`CAST`](abencds_cast_expression_v2.md).

- Since average values usually have decimal places, integer types are not supported for `dtype`. If necessary, the type `DEC` can be used without decimal places.

- An aggregate expression `AVG` with the addition `AS dtype` can be used in accordance with this type in a [`CAST`](abencds_cast_expression_v2.md) expression.

- The actual calculation of the average value (determined by the involved data types) is platform-dependent. This can produce underflows, overflows, and exceptions during the calculation. To prevent exceptions, the total of the values for which the average value is being calculated should be within the value range of `dtype`. For further details on the calculation on SAP HANA Platform, see the [SAP HANA SQL Reference Guide](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity demonstrates different uses of the aggregate expression `AVG`. The class `CL_DEMO_CDS_AVG_VE` accesses the view. The average value is calculated with and without addition `DISTINCT` and is returned in various types. A built-in numeric function is used as operand to demonstrate the nesting of built-in functions.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity Demo_Cds_Avg_Ve
  as select from demo_expressions
  {
    avg(          num1 as abap.dec(10,0) ) as avg_dec0,
    avg( distinct num1 as abap.dec(10,0) ) as avg_dec0_distinct,
    avg(          num1 as abap.dec(12,2) ) as avg_dec2,
    avg( distinct num1 as abap.dec(12,2) ) as avg_dec2_distinct,
    avg(          abs(num1)
                       as abap.dec(12,2))  as avg_numeric_func
  }
```
