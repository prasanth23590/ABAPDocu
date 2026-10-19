---
title: "SELECT, hierarchy_ancestors_aggregate"
source_file: abenselect_hierarchy_ancs_agg.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy_navigator > SELECT, FROM hierarchy_aggregate_navigator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, hierarchy_ancestors_aggregate

## Syntax

``` abap
... HIERARCHY_ANCESTORS_AGGREGATE( 
      SOURCE hierarchy [AS tabalias] 
     [START WHERE sql_cond] 
      MEASURES agg_func1 AS alias1[, 
               agg_func2 AS alias2[, 
               ...]] 
     [WHERE sql_cond] ...  
```

[`hierarchy`](abenselect_hierarchy.md) · [`sql_cond`](abenabap_sql_expr_logexp.md) · [`sql_cond`](abenabap_sql_expr_logexp.md)

### Addition

[1. `... START WHERE sql_cond`](abenselect_hierarchy_ancs_agg.md#addition-1)

[2. `... WHERE sql_cond`](abenselect_hierarchy_ancs_agg.md#addition-2)

## Overview

### Description

Specifies the [hierarchy aggregate navigator](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) `HIERARCHY_ANCESTORS_AGGREGATE` as the data source [`data_source`](abapselect_data_source.md) in an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md). It accesses the [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md) specified after `SOURCE` and evaluates it. After the SQL hierarchy, `AS` can be used to specify an alias name for it that is valid within the parentheses and must be used in positions in which the SQL hierarchy is addressed.

The hierarchy navigator `HIERARCHY_ANCESTORS_AGGREGATE` aggregates the values of all [ancestor nodes](../../abap-glossary/abenancestor_node_glosry.md) located between [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) determined using `WHERE` and [start nodes](../../abap-glossary/abenstart_node_glosry.md) determined using `START WHERE`, including the values of the hierarchy nodes and start nodes themselves. A tabular result set is created consisting of all hierarchy nodes that

- meet the `WHERE` condition and

- have an ancestor node, including the hierarchy node itself, that meets the `START WHERE` condition as a start node.

- Here, a separate row is created for each possible path to every start node that occurs under the ancestor nodes. If no `WHERE` condition is specified, this is done for all the hierarchy nodes. If no `START WHERE` condition is specified, the start node is the [ancestor node](../../abap-glossary/abenancestor_node_glosry.md) implicitly with the lowest [hierarchy level](../../abap-glossary/abenhierarchy_level_glosry.md).

For each node of the result, the aggregate functions specified after `MEASURES` are applied to the hierarchy nodes of that path that consists of the node and its ancestor nodes, including the start node. The aggregation is based on the start node, which is significant for the aggregate function `STRING_AGG`. The result of each aggregate function is stored in the current node as the content of a separate column.

A comma-separated list of [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) `agg_func1`, `agg_func2`, ... must be specified after `MEASURES`. At least one aggregate function must be specified. Each aggregate function must be assigned an alias name `alias1`, `alias2`, ... The arguments of the aggregate functions can be individual columns [`col`](abenabap_sql_columns.md) of the SQL hierarchy `hierarchy`, including their [hierarchy columns](abenddddl_hierarchy.md). The [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~` can be used to prefix the columns with the name of the SQL hierarchy. The following aggregate functions can be used:

[`AVG( col )`](abensql_agg_func.md), [`MIN( col )`](abensql_agg_func.md), [`MAX( col )`](abensql_agg_func.md), [`SUM( col )`](abensql_agg_func.md), [`PRODUCT( col )`](abensql_agg_func.md), [`COUNT( [DISTINCT] col )`](abensql_agg_func.md), [`COUNT( * )`](abensql_agg_func.md), [`COUNT(*)`](abensql_agg_func.md), [`STRING_AGG( col[, sep] )`](abensql_agg_func.md)

The addition `DISTINCT` is only possible for `COUNT`. The aggregate function `PRODUCT` can be used in this hierarchy navigator only. The addition `ORDER BY` is not possible in the function `STRING_AGG`.

The aggregate functions work as described in the [general description](abensql_agg_func.md), except that only columns `col` are allowed as arguments and that the result of the function `COUNT` is `INT8` instead of `INT4`. For each aggregate function, a column with the alias name defined by `AS` is added to the tabular result of the hierarchy navigator. This column contains the result of the aggregate function in every row. These columns are not [hierarchy columns](abenddddl_hierarchy.md). If `*` or `...~*` is specified in the [`SELECT` list](abapselect_list.md), they are read like a column of the SQL hierarchy specified as a source and are part of a structure or internal table created using an inline declaration `@DATA|@FINAL(...)` in the [`INTO` clause](abapinto_clause.md).

### Hints

- If the `START WHERE` condition selects multiple start nodes, a separate row is inserted in the result set for each start node for which a path exists to one of the hierarchy nodes selected by the `WHERE` condition. Child nodes with multiple parent nodes can also point to different paths to a start node and hence to multiple rows for a hierarchy node.

- Additional hierarchy columns such as `START_RANK` and `START_ID` as for the [hierarchy node navigators](../../abap-glossary/abenhierarchy_node_navi_glosry.md) are not yet available, which means that the different paths in the result set cannot be distinguished from the content of hierarchy columns. It is currently advisable, therefore, to use the `START WHERE` condition to select exactly one start node only.

- The fact that the start node determined by `START WHERE` is respected in the aggregation may be unexpected behavior and should be respected when formulating the condition. This can be done, for example, by setting a condition for the hierarchy column that determines the parent node and is not set on the key of the node.

### Executable Example

See [Hierarchy Navigator `HIERARCHY_ANCESTORS_AGGREGATE`](abenhier_ancs_agg_abexa.md)

## Addition 1

`... START WHERE sql_cond`

### Description

The `START WHERE` condition selects the start nodes for the paths to be aggregated for the hierarchy nodes selected by the `WHERE` condition. Columns of the SQL hierarchy, including the additional [hierarchy columns](abenddddl_hierarchy.md), can be used in the condition [`sql_cond`](abenabap_sql_expr_logexp.md).

If a selected start node is an ancestor node of a node selected by `WHERE`, the latter is added to the result set.

### Hints

- If multiple start nodes are ancestor nodes of a node selected by `WHERE`, the latter is also added to the result set multiple times.

- If a selected start node is not an ancestor node of a node selected by `WHERE`, the node is ignored.

## Addition 2

`... WHERE sql_cond`

### Description

The `WHERE` condition selects those nodes of the SQL hierarchy specified after `SOURCE` that can be added to the result set of the hierarchy navigator. Columns of the SQL hierarchy, including the additional [hierarchy columns](abenddddl_hierarchy.md), can be used in the condition [`sql_cond`](abenabap_sql_expr_logexp.md).

### Hint

Meeting the `WHERE` condition is by itself not sufficient to add nodes to the result set. An ancestor node must also meet the `START WHERE` in this case.
