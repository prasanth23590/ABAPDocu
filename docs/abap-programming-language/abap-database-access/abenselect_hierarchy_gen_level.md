---
title: "SELECT, FROM HIERARCHY, LEVELS"
source_file: abenselect_hierarchy_gen_level.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy > SELECT, FROM HIERARCHY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM HIERARCHY, LEVELS

## Syntax

``` abap
... HIERARCHY( SOURCE data_source [AS tabalias] 
               LEVELS ( col1, col2, ... ) 
              [SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING][, 
                                 field2 [ASCENDING|DESCENDING], ...]] 
              [CACHE ON|OFF|FORCE],... 
              [RETAIN NULLS @policy] ) ...  
```

[`data_source`](abapselect_data_source.md) · [`[AS tabalias]`](abapfrom_clause.md) · [`col1`](abenabap_sql_columns.md) · [`col2`](abenabap_sql_columns.md)

### Addition

[1. `... SOURCE data_source [AS tabalias]`](abenselect_hierarchy_gen_level.md#addition-1)

[2. `... LEVELS ( col1, col2, ... )`](abenselect_hierarchy_gen_level.md#addition-2)

[3. `... SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING], ...`](abenselect_hierarchy_gen_level.md#addition-3)

[4. `... CACHE ON|OFF|FORCE,...`](abenselect_hierarchy_gen_level.md#addition-4)

[5. `... RETAIN NULLS @policy`](abenselect_hierarchy_gen_level.md#addition-5)

## Overview

### Description

In this variant of the hierarchy generator `HIERARCHY`, a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md), is generated based on a set of columns of a data source that define the levels of the hierarchy. The row content of these level columns is interpreted as the nodes of a path from a [root](../../abap-glossary/abenroot_node_glosry.md) to a [leaf node](../../abap-glossary/abenleaf_node_glosry.md) that spans all levels. In the resulting hierarchy, all leaf nodes have the same level that is the highest level of the hierarchy.

The following needs to be specified:

- A data source [`data_source`](abapselect_data_source.md) must be specified after `SOURCE`.

- After `LEVELS` the columns of the data source must be listed that define the levels of the level-based hierarchy.

From these specifications, a SQL hierarchy is generated as follows:

- Each column specified after `LEVELS` defines a [hierarchy level](../../abap-glossary/abenhierarchy_level_glosry.md) of the resulting level-based hierarchy. The level numbering depends on the order of these columns in the data source.

  - The leftmost column defines [root nodes](../../abap-glossary/abenroot_node_glosry.md) of level 1.

  - The rightmost column defines [leaf nodes](../../abap-glossary/abenleaf_node_glosry.md) of the highest level.

  - The columns in between define [child nodes](../../abap-glossary/abenchild_node_glosry.md) that make up a path from the root to the leave node.

- The rows of the [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) are constructed as follows:

  - Each row of the data results in a node of the highest level.

  - For each preceding level one row is inserted into the hierarchy with its respective level in such a way that there are no duplicates in the level columns.

  - The root nodes represent the set of unique values of the leftmost column.

- The columns of the SQL hierarchy are composed of the columns of the source specified after `SOURCE` and additional [hierarchy columns](abenddddl_hierarchy.md). The columns of the data source are filled as follows:

  - In the row of the highest level, all columns of the data source are filled with the data from the data source.

  - In the rows of lower levels, only the column that defines the level and the columns of lower levels are filled with the data from the data source. All other columns are filled with the [null value](../../abap-glossary/abennull_value_glosry.md).

- The [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) are filled in each row with their [corresponding values](abenddddl_hierarchy.md).

- In addition to the general [hierarchy columns](abenddddl_hierarchy.md), a level-based hierarchy has an additional column `HIERARCHY_LEVEL_NAME` with the type `SSTRING` and length 256 that contains the uppercase name of the level column that defines the current hierarchy level.

- The hierarchy columns `NODE_ID` and `PARENT_ID` have a different meaning than for a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md):

  - `NODE_ID` contains the content of the level column that defines the current hierarchy level.

  - `PARENT_ID` contains the content of the level column that defines the hierarchy level of the preceding parent node.

    The data type of columns `NODE_ID` and `PARENT_ID` are inferred as follows:

  - If all level columns have the same type `INT1`, `INT2`, `INT4`, `INT8`, `FLTP`, `D16N`, `D34N`, `TIMN`, `DATN`, or `UTCL`, the type of the hierarchy columns is the same as the type of the level columns.

  - In all other cases the hierarchy columns have type `SSTRING` and length 1333.

### Hints

- The order of the additions is fixed. They must be specified as shown here.

- In the [relational data model](../../abap-glossary/abenrelational_data_model_glosry.md), hierarchical data stored in [relational databases](../../abap-glossary/abenrelational_database_glosry.md) are a common phenomenon, where the key fields are mapped to hierarchy levels.

- Transforming hierarchical data from relational databases into SQL hierarchies makes the hierarchy attributes available and enables the usage of [hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md) for these data (refer to the executable example [ABAP SQL - Level-based Hierarchy of Flight Data](abensheet_abap_sql_lev_hiera_abexa.md)).

- Additions as `MULTIPLE PARENTS`, `ORPHANS` or `CYCLES` that are necessary for [parent-child-based hierarchies](../../abap-glossary/abenpc_based_hiera_glosry.md), are not needed for level-based hierarchies. By their definition, multiple parents, orphans and cycles cannot appear in level-based hierarchies.

- The [hierarchy edges](../../abap-glossary/abenhierarchy_edge_glosry.md) between neighboring nodes of a path in a level-based hierarchies are also parent-child-relations, even if they are not defined as such. There is a parent-child relation between the [hierarchy columns](abenddddl_hierarchy.md) `HIERARCHY_PARENT_RANK` and `HIERARCHY_RANK` (refer to [ABAP SQL - Parent-child-based Hierarchy vs. Level-based Hierarchy](abenabap_sql_pc_lev_hiera_abexa.md)).

- The generation of a level-based hierarchy can be compared to the [group level processing](../../abap-glossary/abengroup_level_processing_glosry.md) of internal tables (refer to the executable example [ABAP SQL - Level-based Hierarchy vs. Grouping](abenabap_sql_lev_hiera_grp_abexa.md)).

- On the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), the hierarchy generator function [`HIERARCHY_LEVELED`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/2969da89b87f4abd85fd0b5f9f5bc395) is used to create the level-based hierarchy.

## Addition 1

`... SOURCE data_source [AS tabalias]`

### Description

After `SOURCE`, any single data source [`data_source`](abapselect_data_source.md) that can be used in the `FROM` clause can be specified.

### Hints

- The data source can also be another SQL hierarchy.

- In order to give meaningful results, the data source should contain appropriate data.

## Addition 2

`... LEVELS ( col1, col2, ... )`

### Description

The addition `LEVELS` lists the level columns [`col1`](abenabap_sql_columns.md), [`col2`](abenabap_sql_columns.md), ... of the data source [`data_source`](abapselect_data_source.md) that define the levels of the [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md). The level columns are specified by their name optionally preceded by the name of the data source (`data_source~` or `tabalias~`). Only columns of the data source `data_source` can be specified and each column can be specified only once. The order in which the columns are listed does not matter but the hierarchy level is determined by the order of the columns in the data source. Columns of the data types [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) cannot be specified. Either all or none of the level columns can have the data type [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`LRAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

### Hint

Only columns of the data source can be specified after `LEVELS`. [Literals](abenabap_sql_literals.md), [host variables](abenabap_sql_host_variables.md), [host expressions](abenabap_sql_host_expressions.md), [SQL expressions](abapsql_expr.md), and [SQL path expressions](abenabap_sql_path.md) are not possible.

## Addition 3

`... SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING], ...`

### Description

This addition has the same functionality as the addition [`SIBLINGS`](abenselect_hierarchy_gen_assoc.md) for [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md). Here, fields of the data source `data_source` can be specified.

## Addition 4

`... CACHE ON|OFF|FORCE`

### Description

This addition has the same functionality as the addition [`CACHE`](abenselect_hierarchy_gen_assoc.md) for [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Generation of a level-based hierarchy from an internal table `level_tab`. The columns `col1`, `col2`, `col3` are used as level columns. The result contains columns from the data source as well as hierarchy columns. The hierarchy columns `HIERARCHY_RANK` and `HIERARCHY_PARENT_RANK` show a parent-child relationship.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF level_struc, 
    col1 TYPE i, 
    col2 TYPE i, 
    col3 TYPE i, 
    data TYPE c LENGTH 1, 
  END OF level_struc, 
  level_tab TYPE TABLE OF level_struc WITH EMPTY KEY. 
 
 
DATA(level_tab) = VALUE level_tab( 
  ( col1 = 1 col2 = 11 col3 = 111 data = `A` ) 
  ( col1 = 1 col2 = 11 col3 = 112 data = `B` ) 
  ( col1 = 1 col2 = 11 col3 = 113 data = `C` ) 
  ( col1 = 1 col2 = 12 col3 = 121 data = `D` ) 
  ( col1 = 1 col2 = 12 col3 = 122 data = `E` ) 
  ( col1 = 1 col2 = 12 col3 = 123 data = `F` ) 
  ( col1 = 2 col2 = 21 col3 = 211 data = `G` ) 
  ( col1 = 2 col2 = 21 col3 = 212 data = `H` ) 
  ( col1 = 2 col2 = 21 col3 = 213 data = `I` ) 
  ( col1 = 2 col2 = 22 col3 = 221 data = `J` ) 
  ( col1 = 2 col2 = 22 col3 = 222 data = `K` ) 
  ( col1 = 2 col2 = 22 col3 = 223 data = `L` ) 
  ). 
 
out->write( level_tab ). 
 
SELECT FROM HIERARCHY( 
              SOURCE @level_tab AS lt 
              LEVELS ( lt~col1, lt~col2, lt~col3 ) 
              SIBLINGS ORDER BY lt~col1, lt~col2, lt~col3 ) 
       FIELDS hierarchy_rank, 
              hierarchy_parent_rank, 
              col1, col2, col3, data, 
              node_id, 
              parent_id, 
              hierarchy_level_name, 
              hierarchy_level, 
              hierarchy_tree_size 
       INTO TABLE @DATA(result) ##ITAB_DB_SELECT. 
 
out->write( result ). 
 
out->display( ).
```

## Addition 5

`... RETAIN NULLS @policy`

### Description

`Policy` must have type `SQL_HIERARCHY_RETAIN_NULLS`. This is an [enumerated type](../../abap-glossary/abencds_enum_type_glosry.md). By default, the value of `policy` is `none`. Therefore, if one level column of a row of the data source contains the [null value](../../abap-glossary/abennull_value_glosry.md), the row is not included in the SQL hierarchy.

If the value is set to `not_trailing`, the null value is handled like a normal value in all but the last level. If there is a null in the last level, the row will still be ignored (= the trailing null).

## Executable Examples

- [ABAP SQL - Level-based Hierarchy of Flight Data](abensheet_abap_sql_lev_hiera_abexa.md)

- [ABAP SQL - Level-based Hierarchy vs. Grouping](abenabap_sql_lev_hiera_grp_abexa.md)

- [ABAP SQL - Parent-child-based Hierarchy vs. Level-based Hierarchy](abenabap_sql_pc_lev_hiera_abexa.md)
