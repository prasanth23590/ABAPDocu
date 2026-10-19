---
title: "CDS DDL - CDS View Entity, SELECT, clauses"
source_file: abencds_select_clauses_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, clauses

## Syntax

``` abap
... [WHERE cds_cond] 
    [GROUP BY field1, field2, ...] 
    [HAVING cds_cond] 
    [EXCEPT SELECT ...]   
    [INTERSECT SELECT ...]   
    [UNION [ALL] SELECT ...]   ...  
```

[`WHERE cds_cond`](abencds_where_clause_v2.md) · [`GROUP BY field1, field2, ...`](abencds_group_by_v2.md) · [`HAVING cds_cond`](abencds_having_clause_v2.md) · [`EXCEPT SELECT ...] `](abencds_except_v2.html) · [`INTERSECT SELECT ...] `](abencds_intersect_v2.html) · [`UNION [ALL] SELECT ...] `](abencds_union_v2.html)

## Description

The optional clauses of the [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) have the following semantics:

- The [`WHERE` clause](abencds_where_clause_v2.md) restricts the rows in the result set when the CDS view entity is accessed.

- The [`GROUP BY` clause](abencds_group_by_v2.md) groups rows in the result set when the CDS view entity is accessed. It is applied after rows are selected using the `WHERE` clause.

- The [`HAVING` clause](abencds_having_clause_v2.md) restricts the result set further after a `GROUP BY` clause. [Aggregate expressions](abencds_aggregate_functions_v2.md) are possible after `HAVING`.

- [`EXCEPT`](abencds_except_v2.md), [`INTERSECT`](abencds_intersect_v2.md), and [`UNION`](abencds_union_v2.md) are [`set operators`](../../abap-glossary/abencds_set_operators_glosry.md). They can be used to merge the result sets of multiple `SELECT` statements into a single result set.

## Hint

CDS view entities do not support `ORDER BY` for the following reasons:

- Historic reason: Some database platforms that support ABAP CDS do not support `ORDER BY` in views.

- Undefined behavior may occur when `ORDER BY` is used in multiple views within a view stack.

- Undefined behavior may occur in complex views that, for example, join multiple data sources and use an `ORDER BY` clause.
