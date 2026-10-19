---
title: "CDS DDL - DDIC-Based View, AVG, AS"
source_file: abencds_avg_as_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, aggr_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, AVG, AS

## Syntax

``` abap
... AVG( [DISTINCT] arg AS dtype ) ...  
```

## Description

Aggregate expression [`AVG`](abencds_aggregate_functions_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) with a data type `dtype` specified. The data type determines the result type in which the average value is returned.

The same can be specified for the `arg` as for all [aggregate expressions](abencds_aggregate_functions_v1.md) with one exception; [`CASE`](abencds_case_expression_v1.md) cannot be specified. The data type of `arg` must be numeric and have one of the types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). `arg` can also have data type [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), but with this data type, the addition `AS` is mandatory.

The data type `dtype` can have the built-in numeric type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT16`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DECFLOAT34`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The data type `FLTP`, however, can only be specified for operands of type `FLTP`. The data type `dtype` can be specified as follows:

- Using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) with a allowed type.

- Directly as a [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary.

The following table shows the syntax for specifying built-in data types:

| **dtype**                 | **Dictionary Type**                                                                    |
|---------------------------|----------------------------------------------------------------------------------------|
| `abap.dec(len,decimals)`  | [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and `decimals` decimal places   |
| `abap.curr(len,decimals)` | [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and `decimals` decimal places  |
| `abap.quan(len,decimals)` | [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` with `decimals` decimal places |
| `abap.fltp[(16,16)]`      | [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                  |

The value range of the data type `dtype` must cover the value range of the operand type:

- If `arg` is an integer type, a type `dtype` of type `DEC`, `CURR`, `QUAN` must have at least as many integer digits as is required by the value range of the respective integer type, that is, 3 for `INT1`, 5 for `INT2`, 10 for `INT4`, and 19 for `INT8`. There is no restriction on the number of decimal places.

- If `arg` has type `DEC`, `CURR`, `QUAN`, a type `dtype` of type `DEC`, `CURR`, `QUAN` must have at least as many integer digits and decimal places.

- If `arg` has type `FLTP`, this type must also be specified for `dtype`.

If the average value cannot be represented exactly in the data type `dtype`, the result is rounded commercially.

## Hints

- The addition `AS` to `AVG` bridges the gap for average values where `FLTP` cannot be cast to other numeric data types with [`CAST`](abencds_cast_expression_v1.md).

- Since average values usually have decimal places, integer types are not supported for `dtype`. If necessary, the type `DEC` can be used without decimal places.

- An aggregate expression `AVG` with the addition `AS dtype` can be used in accordance with this type in a [`CAST`](abencds_cast_expression_v1.md) expression.

- The actual calculation of the average value (determined by the involved data types) is platform-dependent. This can produce underflows, overflows, and exceptions during the calculation. To prevent exceptions, the total of the values for which the average value is being calculated should be within the value range of `dtype`. For further details on the calculation on SAP HANA Platform, see the [SAP HANA SQL Reference Guide](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- If `FLTP` is specified explicitly for operands of type `FLTP`, this ensures that the result of `AVG` actually has this type at each operand position, which cannot be guaranteed otherwise.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view demonstrates different uses of the aggregate expression `AVG`. The class `CL_DEMO_CDS_AVG` accesses the view. The average value is calculated with and without addition `DISTINCT` and is returned in various types.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSAVG'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view Demo_Cds_Avg
  as select from
    demo_expressions
    {
      avg(          num1                   ) as avg_no_type,
      avg( distinct num1                   ) as avg_no_type_distinct,
      avg(          num1 as abap.dec(10,0) ) as avg_dec0,
      avg( distinct num1 as abap.dec(10,0) ) as avg_dec0_distinct,
      avg(          num1 as abap.dec(12,2) ) as avg_dec2,
      avg( distinct num1 as abap.dec(12,2) ) as avg_dec2_distinct
    }     
```
