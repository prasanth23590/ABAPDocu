---
title: "SELECT, FROM hierarchy_descendants_aggregate"
source_file: abenselect_hierarchy_desc_agg.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy_navigator > SELECT, FROM hierarchy_aggregate_navigator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM hierarchy_descendants_aggregate

## Syntax

``` abap
... HIERARCHY_DESCENDANTS_AGGREGATE( 
      SOURCE hierarchy [AS tabalias] 
     [JOIN data_source [AS tabalias] ON sql_cond] 
      MEASURES agg_func1 AS alias1[, 
               agg_func2 AS alias2[, 
               ...]] 
     [WHERE sql_cond] 
     [WITH SUBTOTAL] 
     [WITH BALANCE] 
     [WITH NOT MATCHED] 
     [WITH TOTAL] ) ...  
```

[`hierarchy`](abenselect_hierarchy.md) · [`data_source`](abapselect_data_source.md) · [`sql_cond`](abenabap_sql_expr_logexp.md) · [`sql_cond`](abenabap_sql_expr_logexp.md)

### Addition

[1. `... JOIN data_source [AS tabalias]`](abenselect_hierarchy_desc_agg.md#addition-1)

[2. `... WHERE sql_cond`](abenselect_hierarchy_desc_agg.md#addition-2)

[3. `... WITH SUBTOTAL`](abenselect_hierarchy_desc_agg.md#addition-3)

[4. `... WITH BALANCE`](abenselect_hierarchy_desc_agg.md#addition-4)

[5. `... WITH NOT MATCHED`](abenselect_hierarchy_desc_agg.md#addition-5)

[6. `... WITH TOTAL`](abenselect_hierarchy_desc_agg.md#addition-6)

## Overview

### Description

Specifies the [hierarchy aggregate navigator](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) `HIERARCHY_DESCENDANTS_AGGREGATE` as a data source [`data_source`](abapselect_data_source.md) in an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md). It accesses the [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md) specified after `SOURCE` and evaluates it. After the SQL hierarchy, `AS` can be used to specify an alias name for it that is valid within the parentheses and must be used in positions in which the SQL hierarchy is addressed.

The hierarchy navigator `HIERARCHY_DESCENDANTS_AGGREGATE` returns a tabular result consisting of the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of the SQL hierarchy [`hierarchy`](abenselect_hierarchy.md) specified after `SOURCE` that meet the optional `WHERE` condition. If no `WHERE` condition is specified, these are all the hierarchy nodes. For each node of the result, the aggregate functions specified after `MEASURES` are applied to the row set resulting from the node and all its [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md). The result of each aggregate function is stored in the current node as the content of a separate column.

A comma-separated list of [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) `agg_func1`, `agg_func2`, ... must be specified after `MEASURES`. At least one aggregate function must be specified. Each aggregate function must be assigned an alias name `alias1`, `alias2`, ... The arguments of the aggregate functions can be individual columns [`col`](abenabap_sql_columns.md) of the SQL hierarchy `hierarchy` including its [hierarchy columns](abenddddl_hierarchy.md) or a data source `data_source` specified after `JOIN`. The [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~` can or must be used to prefix the columns with the name of the SQL hierarchy or data source. The following aggregate functions are possible:

- If `JOIN` is not specified, the arguments `col` can be columns of the SQL hierarchy and the following aggregate functions can be used:

  [`AVG( col )`](abensql_agg_func.md),

  [`MIN( col )`](abensql_agg_func.md),

  [`MAX( col )`](abensql_agg_func.md),

  [`SUM( col )`](abensql_agg_func.md),

  [`COUNT( [DISTINCT] col )`](abensql_agg_func.md),

  [`COUNT( * )`](abensql_agg_func.md), [`COUNT(*)`](abensql_agg_func.md) The addition `DISTINCT` is only possible for `COUNT`.

- If `JOIN` is specified, the arguments `col` can be columns of the SQL hierarchy and the data source after `data_source` and the following aggregate functions can be used:

  [`MIN( col )`](abensql_agg_func.md),

  [`MAX( col )`](abensql_agg_func.md),

  [`SUM( col )`](abensql_agg_func.md),

  [`COUNT( [DISTINCT] col )`](abensql_agg_func.md) The addition `DISTINCT` is only possible for `COUNT` and for columns of the SQL hierarchy.

The aggregate functions work as described in the [general description](abensql_agg_func.md), except that only columns `col` are allowed as arguments and that the result of the function `COUNT` is `INT8`. For each aggregate function, a column with the alias name defined by `AS` is added to the tabular result of the hierarchy navigator. This column contains the result of the aggregate function in every row. These columns are not [hierarchy columns](abenddddl_hierarchy.md). If `*` or `...~*` is specified in the [`SELECT` list](abapselect_list.md), they are read like a column of the SQL hierarchy specified as a source and are part of a structure or internal table created using an inline declaration `@DATA|@FINAL(...)` in the [`INTO` clause](abapinto_clause.md).

In addition to the [hierarchy columns](abenddddl_hierarchy.md) of the SQL hierarchy specified after `SOURCE`, the result set contains a further hierarchy column `HIERARCHY_AGGREGATE_TYPE` with the type `INT1`. In the rows of the result set created by the optional `WITH` additions, this column contains an indicator for the addition to be created, otherwise it contains the numeric value 0.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the hierarchy navigator `HIERARCHY_DESCENDANTS_AGGREGATE` in the class `CL_DEMO_HIERARCHY_AGGREGATE`, where the [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) `DEMO_CDS_PARENT_CHILD_AGG` is specified as a source. The `WHERE` condition evaluates the [hierarchy column](abenddddl_hierarchy.md) `HIERARCHY_LEVEL` and only nodes with a maximum hierarchy level of 2 are added to the result set. The aggregate functions, however, respect all descendant nodes regardless of their hierarchy level. When executed, `CL_DEMO_HIERARCHY_AGGREGATE` demonstrates how this hierarchy navigator works.

``` abap
FINAL(level) = 2. 
 
SELECT agg~* 
       FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
              SOURCE demo_cds_parent_child_agg( p_id = 'A' ) 
              MEASURES AVG( num ) AS avg, 
                       MIN( num ) AS min, 
                       MAX( num ) AS max, 
                       SUM( num ) AS sum, 
                       COUNT( * ) AS cnt 
              WHERE hierarchy_level <= @level ) AS agg 
       INTO TABLE @FINAL(cds_hierarchy_desc_aggregate).
```

## Addition 1

`... JOIN data_source [AS tabalias]`

### Description

The optional addition `JOIN` can be used to join an additional data source [`data_source`](abapselect_data_source.md) with the SQL hierarchy specified after `SOURCE`. The same applies to `data_source` as to every data source of a query, except that path expressions [`sql_path`](abenabap_sql_path.md) are not possible. After the data source, `AS` can be used to specify an alias name for it that is valid within parentheses and must be used in positions in which the data source is addressed.

The result set of the SQL hierarchy is joined with the result set of the data source `data_source` in accordance with [`LEFT OUTER JOIN`](abapselect_join.md) rules. The rules for conditions [`sql_cond` in expressions](abenabap_sql_expr_logexp.md) apply to the `ON` condition. Columns of the data source can be used as arguments of those aggregate functions after `MEASURES` for which their data type is suitable. However, they are not part of the tabular result of the hierarchy navigator as additional columns.

For every node of the original SQL hierarchy that meets the `WHERE` condition, the aggregate functions specified after `MEASURES` are applied to every [descendant node](../../abap-glossary/abendescendant_node_glosry.md) in the result set of the join according to the [parent-child relationship](../../abap-glossary/abenpcr_glosry.md).

### Hints

- The addition `JOIN` does not modify the number of rows in the result set of the hierarchy navigator `HIERARCHY_DESCENDANTS_AGGREGATE`. If, however, the result set of the join contains more descendant nodes for a node than in the original SQL hierarchy, all these nodes are respected by the aggregate functions. Any start nodes in a calculation that occur more than once are also all respected multiple times.

- If there are [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) in [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) for a data source specified by `JOIN` and these are not switched off using [`WITH PRIVILEGED ACCESS`](abapselect_data_source.md), these conditions are applied before the join is made.

### Executable Example

[Hierarchy Navigator `HIERARCHY_DESCENDANTS_AGGREGATE`](abenhier_desc_agg_abexa.md)

## Addition 2

`... WHERE sql_cond`

### Description

The `WHERE` condition selects those nodes of the SQL hierarchy specified after `SOURCE` that are added to the result set of the hierarchy navigator. Columns of the SQL hierarchy, including the additional [hierarchy columns](abenddddl_hierarchy.md), can be used in the condition [`sql_cond`](abenabap_sql_expr_logexp.md).

### Hints

- The `WHERE` condition does not restrict the descendant nodes of the selected nodes. It is used only to select those nodes for which the aggregate function is calculated.

- The columns of a data source joined using `JOIN` cannot be used after `WHERE`.

## Addition 3

`... WITH SUBTOTAL`

## Addition 4

`... WITH BALANCE`

## Addition 5

`... WITH NOT MATCHED`

## Addition 6

`... WITH TOTAL`

### Description

Each of the optional `WITH` additions, which can be specified in any order, adds exactly one row to the tabular result of the hierarchy aggregate navigator `HIERARCHY_DESCENDANTS_AGGREGATE`. In the new row, all columns, including the [hierarchy columns](abenddddl_hierarchy.md), contain the [null value](../../abap-glossary/abennull_value_glosry.md), except columns created using the addition `MEASURES` and the hierarchy column `HIERARCHY_AGGREGATE_TYPE`. The special hierarchy column `HIERARCHY_AGGREGATE_TYPE` uses the following values to indicate which `WITH` addition added the row:

| **WITH Addition** | **`HIERARCHY_AGGREGATE_TYPE`** |
|-------------------|--------------------------------|
| `SUBTOTAL`        | 1                              |
| `BALANCE`         | 2                              |
| `NOT MATCHED`     | 3                              |
| `TOTAL`           | 4                              |

In the rows not created by `WITH`, the hierarchy column `HIERARCHY_AGGREGATE_TYPE` contains the numeric value 0. The columns created by the addition `MEASURES` contain the results of their aggregate functions for the hierarchy nodes created as follows by the `WITH` addition:

- `WITH SUBTOTAL`

  The aggregate functions evaluate all hierarchy nodes that meet the `WHERE` condition of the hierarchy navigator.

- `WITH BALANCE`

  The aggregate functions evaluate all hierarchy nodes that do not meet the `WHERE` condition of the hierarchy navigator.

- `WITH NOT MATCHED`

  This addition can only be specified together with the `JOIN` addition. The aggregate functions evaluate all rows of the data source `data_source` specified after `JOIN` for which the `ON` condition of the join is not met.

- `WITH TOTAL`

  The aggregate functions evaluate all hierarchy nodes plus the rows of a data source `data_source` specified after `JOIN` that do not meet the `ON` condition.

### Executable Example

[Hierarchy Navigator `HIERARCHY_DESCENDANTS_AGGREGATE` with `WITH`](abenhier_desc_agg_with_abexa.md)
