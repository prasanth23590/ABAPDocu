---
title: "CDS DDL - Selection-Related Case Expression (Restricted Measure)"
source_file: abencds_sel_case_expression_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries > CDS DDL - element_list, Analytical Query > CDS DDL - element, Analytical Query > CDS DDL - case_expr, Analytical Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Selection-Related Case Expression (Restricted Measure)

## Syntax

``` abap
... CASE 
      WHEN cds_cond 
      THEN result 
     [ELSE NULL] 
    END ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Case expression in a CDS analytical projection view that defines a selection. There must be exactly one `WHEN` branch. A regular `ELSE` branch is not allowed. `ELSE NULL` is available (optionally) to explicitly define the null value as result if no matches are found.

The following is allowed as `result` specified after `THEN`:

- A field of a data source specified as [analytical measure](../../abap-glossary/abencds_measure_glosry.md).

- The built-in functions [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md), [`CURRENCY_CONVERSION`](abencds_conv_func_unit_curr_v2.md), and [`UNIT_CONVERSION`](abencds_conv_func_unit_curr_v2.md).

- A numeric [typed literal](abencds_typed_literal_v2.md) of a measure-like data type or the [untyped literal](abencds_untyped_literal_v2.md) 1. A literal is only allowed if the element is annotated with `AnalyticsDetails.query.onCharacteristicStructure: true` and when this annotation is used, a literal is mandatory.

The following rules apply to the condition [`cds_cond`](abencds_conditional_expression_v2.md) specified after `WHEN`:

- All [comparison operators](abencds_cond_expr_comp_v2.md) are supported.

- [`[NOT] BETWEEN`](abencds_cond_expr_betw_v2.md), [`LIKE`](abencds_cond_expr_like_v2.md), and [`IS [NOT] INITIAL`](abencds_cond_expr_initial_v2.md) are supported.

  **Note:** `NOT LIKE` is not supported.

- The [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md) `AND`, `OR`, and `NOT` are allowed. Identical fields must be combined with `OR` and different fields must be combined with `AND`.

  **Note:** A filter condition does not support nested negations. The following is not supported: `AND NOT field_a <> 'B`. The reason is that `NOT` and \<\> are both negations.

- `lhs` expects a field of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). The field must be classified as [analytical dimension field](../../abap-glossary/abencds_dimension_glosry.md).

- `rhs` can be a [parameter](abencds_parameter_list_apv.md), a session variable, or a [typed literal](abencds_typed_literal_v2.md).

- [Path expressions](abencds_element_apv.md) are not supported as operands.
