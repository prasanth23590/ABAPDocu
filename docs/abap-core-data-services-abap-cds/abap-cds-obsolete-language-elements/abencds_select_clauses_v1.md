---
title: "CDS DDL - DDIC-Based View, SELECT, clauses"
source_file: abencds_select_clauses_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, clauses

## Syntax

``` abap
... [WHERE cds_cond] 
    [GROUP BY field1, field2, ...] 
    [HAVING cds_cond] 
    [UNION [ALL] SELECT ...] ...  
```

[`WHERE cds_cond`](abencds_where_clause_v1.md) · [`GROUP BY field1, field2, ...`](abencds_group_by_v1.md) · [`HAVING cds_cond`](abencds_having_clause_v1.md) · [`UNION [ALL] SELECT ...`](abencds_union_v1.md)

## Description

The optional clauses of the [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) have the following semantics:

- The [`WHERE` clause](abencds_where_clause_v1.md) restricts the rows in the result set when the CDS view is accessed.

- The [`GROUP BY` clause](abencds_group_by_v1.md) groups rows in the result set when the CDS view is accessed. It is applied after rows are selected using the `WHERE` clause.

- The [`HAVING` clause](abencds_having_clause_v1.md) restricts the result set further after a `GROUP BY` clause. Here, [aggregate expressions](abencds_aggregate_functions_v1.md) can be specified in the condition.

- [`UNION`](abencds_union_v1.md) can be used to create the union of the result sets from two `SELECT` statements.

## Hint

CDS views do not support `ORDER BY` for the following reasons:

- Historic reason: Some database platforms that support ABAP CDS do not support `ORDER BY` in views.

- Undefined behavior may occur when `ORDER BY` is used in multiple views within a view stack.

- Undefined behavior may occur in complex views that, for example, join multiple data sources and use an `ORDER BY` clause.
