---
title: "CDS DDL - CDS View Entity, SELECT, GROUP BY"
source_file: abencds_group_by_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, GROUP BY

## Syntax

``` abap
... GROUP BY field1, field2, ... 
             path_expr1, path_expr2, ...  
```

[`path_expr1`](abencds_path_expression_v2.md) · [`path_expr2`](abencds_path_expression_v2.md)

## Description

Groups those rows in the result set of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) that have the same content in the elements specified by the fields `field1`, `field2, ...` or [path expressions](abencds_path_expression_v2.md) `path_expr1`, `path_expr2` ... as a single row. The fields must be specified using the same names as the fields in the data source [`data_source`](abencds_data_source_v2.md). The use of alias names defined in the current CDS view entity with [`AS`](abencds_select_list_entry_v2.md) is not allowed.

If the view entity makes use of multiple [data sources](abencds_data_source_v2.md) by using join expressions, then all fields listed after `GROUP BY` must be prefixed with the name of their data source separated by a period (.). The prefix is required in all cases, even if the field names are unique.

The `GROUP BY` clause is mandatory if the `SELECT` list contains any aggregate expressions. All elements that are **not** defined using an aggregate expression must be listed after `GROUP BY`.

After `GROUP BY`, only [fields](abencds_field_v2.md) or [path expressions](abencds_path_expression_v2.md) that are listed in the `SELECT` list can be specified. Other [elementary operands](abencds_operands_v2.md) or [expressions](abencds_expressions_v2.md) cannot be specified after `GROUP BY`.

When the CDS view entity is accessed, the results of the aggregate expressions are calculated from the values of the grouped rows. Several rows are condensed into one row and the result of the calculation is one field of the result set.

The fields specified after `GROUP BY` can have any [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) except for `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

## Hint

A [`WHERE` condition](abencds_where_clause_v2.md) is evaluated **before** the rows are combined using `GROUP BY`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

When the CDS view entity `DEMO_CDS_VIEW_ENTITY_GROUP_BY` shown below is accessed, all flights that have the same carrier ID and connection ID are condensed into one row. The number of rows and the average occupation is calculated for each group. The fields `carrid` and `connid`, which are used in the string function `concat_with_space` in the `SELECT` list, must be listed after `GROUP BY`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@AbapCatalog.viewEnhancementCategory: [#PROJECTION_LIST, #GROUP_BY]
define view entity DEMO_CDS_VIEW_ENTITY_GROUP_BY
  as select from sflight
{
  concat_with_space(carrid, connid, 1) as ID,
  count(*)                             as col_count,
  avg( seatsocc as abap.dec( 20, 2 ))  as col_avg
}
group by
  carrid,
  connid
```
