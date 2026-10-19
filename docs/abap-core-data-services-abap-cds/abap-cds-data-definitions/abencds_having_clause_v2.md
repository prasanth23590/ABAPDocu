---
title: "CDS DDL - CDS View Entity, SELECT, HAVING"
source_file: abencds_having_clause_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, HAVING

## Syntax

``` abap
... HAVING cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Defines a `HAVING` condition for the result set of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) after a [`GROUP BY` clause](abencds_group_by_v2.md) is evaluated. A `HAVING` condition can only be specified together with `GROUP BY`. The `HAVING` condition removes all rows from the result set that do not meet the condition `cds_cond` specified after `HAVING`.

If the view entity makes use of multiple [data sources](abencds_data_source_v2.md) by using join expressions, then all fields listed after `HAVING` must be prefixed with the name of their data source separated by a period (.). The prefix is required in all cases, even if the field names are unique.

The following rules apply to the condition specified after `HAVING`:

- As relational operators, comparison operators, `LIKE`, and `IS [NOT] NULL` can be used. `BETWEEN` and `IS INITIAL` are not supported.

- The Boolean operators `NOT`, `AND`, and `OR` are allowed.

- `lhs` can be a [field](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md), a [path expression](abencds_path_expression_v2.md), an [aggregate expression](abencds_aggregate_functions_v2.md), a [case expression](abencds_case_expression_v2.md), or an [arithmetic expression](abencds_arithmetic_expression_v2.md).

- `rhs` can be an [element](abencds_select_list_entry_v2.md) of the [`SELECT` list](abencds_select_list_v2.md), an [aggregate expression](abencds_aggregate_functions_v2.md), a [literal](abencds_literal_v2.md), a [parameter](abencds_parameter_v2.md), a path expression, a [case expression](abencds_case_expression_v2.md), or an [arithmetic expression](abencds_arithmetic_expression_v2.md).

  **Exception:** when using the operator `LIKE`, then `rhs` must be a character literal.

- A field of a data source can be specified using a path expression [`path_expr`](abencds_path_expression_v2.md).element, as long as the CDS associations of the expression do not have any [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) as [association targets](../../abap-glossary/abenassociation_target_glosry.md) and all associations traversed have the cardinality to-one:

  - The [cardinality](../../abap-glossary/abencardinality_glosry.md) of the contained [CDS associations](../../abap-glossary/abencds_association_glosry.md) is to-one.

  - The path expression contains the [cardinality specification](abencds_path_expr_card_v2.md) attribute to-one.

    `element` can be used to specify an element of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the last CDS association of the path.

- Other expressions and function calls are not allowed.

## Hint

[Aggregate expressions](abencds_aggregate_functions_v2.md) can be specified in the `HAVING` condition, which is not possible in the [`WHERE` condition](abencds_where_clause_v2.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

When accessed, the CDS view entity `DEMO_CDS_VIEW_ENTITY_HAVING` returns details about all flights that have a maximal seats capacity of more than 500 seats.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_VIEW_ENTITY_HAVING
  as select from sflight
  {
    concat_with_space(carrid, connid, 1) as ID,
    count(*)                             as col_count,
    seatsmax
  }
  group by
    carrid,
    connid,
    seatsmax
  having
    seatsmax > abap.int2'500'
```
