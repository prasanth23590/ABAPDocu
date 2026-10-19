---
title: "CDS DDL - WHERE, Analytical Query"
source_file: abencds_where_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - WHERE, Analytical Query

## Syntax

``` abap
... WHERE cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Defines a `WHERE` condition for the result set of a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md). When the CDS projection view is accessed, the result set contains only the data from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) `cds_entity` that meets the condition [`cds_cond`](abencds_conditional_expression_v2.md) specified after `WHERE`.

The condition is either a single [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) `rel_expr` or an expression constructed from the [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md) `AND`, `OR`, and `NOT`.

In CDS analytical projection views, the following rules apply to the operands and syntax of the `WHERE` condition:

- [Comparison operators](abencds_cond_expr_comp_v2.md) are allowed.

- [`BETWEEN`](abencds_cond_expr_betw_v2.md), [`LIKE`](abencds_cond_expr_like_v2.md), and [`INITIAL`](abencds_cond_expr_initial_v2.md) are allowed as relational operators.

- The Boolean operators `AND`, `OR`, and `NOT` are supported. Identical fields must be combined with `OR` and different fields must be combined with `AND`.

  **Note:** A filter condition does not support nested negations. The following is not supported: `AND NOT field_a <> 'B`. The reason is that `NOT` and \<\> are both negations.

- `lhs` must be a field of the projected entity specified as [analytical dimension field](../../abap-glossary/abencds_dimension_glosry.md).

- `rhs` can be a [CDS literal](../../abap-glossary/abencds_literal_glosry.md), a session variable (currently, only `$session.system_date` and `$session.user_date` are supported), or a parameter. When using the operator `LIKE`, `rhs` must be a character literal.

- [Path expressions](abencds_path_expr_apv.md) `path_expr` are not allowed as operands in a `WHERE` condition.
