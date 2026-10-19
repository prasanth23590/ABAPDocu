---
title: "SELECT, FROM hierarchy_navigator"
source_file: abenselect_hierarchy_navigators.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM hierarchy_navigator

## Syntax

``` abap
... hierarchy_node_navigator 
  | hierarchy_agg_navigator ...  
```

[`hierarchy_node_navigator`](abenselect_hierarchy_node_navis.md) · [`hierarchy_agg_navigator`](abenselect_hierarchy_agg_navis.md)

## Description

Specifies a [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) as a data source [`data_source`](abapselect_data_source.md) in an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md).

A hierarchy navigator accesses an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) and evaluates it. There are different kinds of hierarchy navigators:

- [Hierarchy node navigators](../../abap-glossary/abenhierarchy_node_navi_glosry.md) [`hierarchy_node_navigator`](abenselect_hierarchy_node_navis.md) select certain hierarchy nodes and their properties.

- [Hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`hierarchy_agg_navigator`](abenselect_hierarchy_node_navis.md) select certain hierarchy nodes and apply additional [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) to them.

The tabular result contains the hierarchy nodes selected by the [hierarchy navigator](../../abap-glossary/abenhierarchy_node_glosry.md). The columns of the tabular result include the additional [hierarchy columns](abenddddl_hierarchy.md) of the SQL hierarchy specified after `SOURCE`, as well as any other hierarchy columns that are specific to the hierarchy navigators where applicable.

The same applies to the additional hierarchy columns as when accessing a SQL hierarchy [`hierarchy`](abenselect_hierarchy.md):

- If `*` or `...~*` is specified in the [`SELECT` list](abapselect_list.md), they are not read and are not part of a structure or internal table created using an inline declaration `@DATA|@FINAL(...)` in the [`INTO` clause](abapinto_clause.md).

- They can, however, be listed explicitly in the `SELECT` list and, like any column in the result set, can be used for columns [`colname`](abenabap_sql_columns.md) specified in the other clauses of the query.

A hierarchy navigator exposes all associations of the SQL hierarchy used implicitly and leaves its [association target](../../abap-glossary/abenassociation_target_glosry.md) unchanged.

## Hints

- Hierarchy navigators do not create any SQL hierarchies:

  - They cannot be specified as a source in hierarchy navigators.

  - They cannot be exposed as a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md).

- On [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md), the result sets of the hierarchy navigators are based on the use of the identically named hierarchy navigation functions. For more information, see the [SAP HANA documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- Since hierarchies generated from the `START WHERE` condition are buffered on the database, it is advisable to use hierarchy navigators to evaluate a SQL hierarchy. For example, finding the descendant nodes of a node with the [hierarchy node navigator](../../abap-glossary/abenhierarchy_node_navi_glosry.md) [`HIERARCHY_DESCENDANTS`](abenselect_hierarchy_node_navis.md) is more efficient than generating a new SQL hierarchy with this node as a root node. Furthermore, the hierarchy navigators add hierarchy columns that are not readily available otherwise.

- Hierarchy functions cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.
