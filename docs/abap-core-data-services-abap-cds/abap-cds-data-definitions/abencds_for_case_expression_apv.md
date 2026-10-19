---
title: "CDS DDL - Formula-Related Case Expression"
source_file: abencds_for_case_expression_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries > CDS DDL - element_list, Analytical Query > CDS DDL - element, Analytical Query > CDS DDL - case_expr, Analytical Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Formula-Related Case Expression

## Syntax

``` abap
... 
@Aggregation.default: #FORMULA 
  CASE 
    WHEN cds_cond 
    THEN result1 
    ELSE {result2 | NULL} 
  END ...  
```

## Description

Formula-related case expression in the element list of an CDS analytical projection view. The case distinction evaluates the condition [`cds_cond`](abencds_conditional_expression_v2.md) and returns either the operand `result1` specified after `THEN`, or the operand `result2` specified after `ELSE`. `result2` can also be the null value. `ELSE NULL` is available to explicitly define the null value as result if no matches are found.

There must be exactly one `WHEN` branch, one `THEN` branch, and one `ELSE` branch. The annotation `@Aggregation.default: #FORMULA` is mandatory for formula-related case expressions.

`result1` and `result2` must be specified as a field of a data source with a data type valid for [analytical measures](../../abap-glossary/abencds_measure_glosry.md), numeric [typed literals](abencds_typed_literal_v2.md) (except for data type `NUMC`), or numeric [parameters](abencds_f1_param.md) (except for data type `NUMC`).

The following rules apply to the condition specified after `WHEN`:

- All [comparison operators](abencds_cond_expr_comp_v2.md) except for \<\> are supported.

- [`IS INITIAL`](abencds_cond_expr_initial_v2.md) is supported. [`BETWEEN`](abencds_cond_expr_betw_v2.md), [`LIKE`](abencds_cond_expr_like_v2.md), and [`IS NULL`](abencds_cond_expr_null_v2.md) are not allowed.

- The [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md) `AND` and `OR` are allowed.

- `lhs` expects either a field of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) classified as an analytical measure, a [built-in function](abencds_builtin_functions_v2.md), or an input parameter.

- `rhs` can be a field of a data source specified as [analytical measure](../../abap-glossary/abencds_measure_glosry.md), a built-in function, a [parameter](abencds_parameter_list_apv.md), a session variable, or a [typed literal](abencds_typed_literal_v2.md) of one of the following data types: `DEC`, `DECFLOAT16`, `DECFLOAT34`, `FLTP`, `DF16_DEC`, `DF34_DEC`, `DF16_RAW`, `DF34_RAW`, `INT1`, `INT2`, `INT4`, `INT8`, `DATS`, `DATN`, `TIMN`, `TIMS`.

- [Path expressions](abencds_element_apv.md) are not supported as operands.
