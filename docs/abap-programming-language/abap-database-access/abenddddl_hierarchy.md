---
title: "Hierarchy Columns"
source_file: abenddddl_hierarchy.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Hierarchy Columns

[Hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) are additional components of the result set when the following data sources are accessed in an ABAP SQL query:

- An [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md)

- A [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) [`hierarchy_navigator`](abenselect_hierarchy_navigators.md)

The hierarchy columns have the same names and contain the values of the [hierarchy attributes](../../abap-glossary/abenhierarchy_attribute_glosry.md) of the data sources above. Using these, they provide information about the SQL [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) in question. The following table shows the name and meaning of each hierarchy column:

| **Name**         | **Data Type** | **Meaning**                                                                          |
|------------------|---------------|--------------------------------------------------------------------------------------|
| `HIERARCHY_RANK` | `INT8`        | Sequential number granted as a unique hierarchy node ID when a hierarchy is created. |

\|`HIERARCHY_TREE_SIZE`\|`INT8`\|Number of [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) of the hierarchy node, including the hierarchy node itself.\|

\|`HIERARCHY_PARENT_RANK`\|`INT8`\|0 for [root nodes](../../abap-glossary/abenroot_node_glosry.md), otherwise the `HIERARCHY_RANK` ID of the [parent node](../../abap-glossary/abenchild_node_glosry.md).\| \|`HIERARCHY_LEVEL`\|`INT4`\|[Hierarchy level](../../abap-glossary/abenhierarchy_level_glosry.md) of the hierarchy node. Always 1 for [root nodes](../../abap-glossary/abenroot_node_glosry.md). For their [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md), the distance from the root node plus one.\| \|`HIERARCHY_IS_CYCLE`\|`INT1`\|Flag indicating whether the hierarchy node is part of (1) or is not part of (0) a [node cycle](../../abap-glossary/abennode_cycle_glosry.md).\| \|`HIERARCHY_IS_ORPHAN`\|`INT1`\|Flag indicating whether the hierarchy node is (1) or is not (0) an [orphan node](../../abap-glossary/abenorphan_node_glosry.md).\| \|`NODE_ID`\|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): `SSTRING`, length 1333

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): Refer to [`SELECT`, `FROM HIERARCHY`, `LEVELS`](abenselect_hierarchy_gen_level.md). \|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): Internal character-like key of the hierarchy node that concatenates the values of all [association target](../../abap-glossary/abenassociation_target_glosry.md) fields of the associated [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) specified in the `ON` conditions. If there is only one comparison in the `ON` condition, no concatenation is required, and the data type is the data type of the specified field of the [association target](../../abap-glossary/abenassociation_target_glosry.md).

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): The content of the level column that defines the current hierarchy level.\| \|`PARENT_ID`\|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): `SSTRING`, length 1333

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): Refer to [`SELECT`, `FROM HIERARCHY`, `LEVELS`](abenselect_hierarchy_gen_level.md).\|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): Internal character-like key of the hierarchy node that concatenates the values of all [association source](../../abap-glossary/abenassociation_source_glosry.md) fields of the associated [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) specified in the `ON` conditions. If there is only one comparison in the `ON` condition, no concatenation is required, and the data type is the data type of the specified field of the [association source](../../abap-glossary/abenassociation_source_glosry.md).

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): The content of the level column that defines the hierarchy level f the preceding parent node.\| \|`VALID_FROM`, `VALID_UNTIL`

\|`DATS`, `TIMESTAMP`, `TIMESTAMPL`\| These attributes exist only for [temporal SQL hierarchies](../../abap-glossary/abentemporal_hierarchy_glosry.md). They contain the limits of the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of the current [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) of a [temporal SQL hierarchy](../../abap-glossary/abentemporal_hierarchy_glosry.md).\|

## Hints

- In addition to the general hierarchy columns shown here, [hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md) have several additional columns.

- Hierarchies generated with [`LEVELS ( ... )`](abenselect_hierarchy_gen_level.md) from level-based hierarchy data have an additional column `HIERARCHY_LEVEL_NAME`.

- The hierarchy columns must be specified explicitly in the [`SELECT`](abapselect_list.md) list before they can be selected.

- The values of some hierarchy columns are usable only if the hierarchy is a tree-like SQL hierarchy in which a hierarchy node does not have multiple parent nodes.

- Using the [`HIERARCHY_COMPOSITE_ID`](abensql_hierarchy_comp_id.md) function, node IDs and parent IDs can be generated.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Explicit access to the hierarchy columns when a CDS hierarchy is specified as a data source in a `SELECT` statement in the class `CL_DEMO_HIERARCHY_PARENT_CHILD`.

``` abap
FINAL(start_id) = 'A '. 
 
SELECT FROM demo_cds_parent_child( p_id = @start_id ) 
       FIELDS id, 
              parent, 
              hierarchy_rank, 
              hierarchy_tree_size, 
              hierarchy_parent_rank, 
              hierarchy_level, 
              hierarchy_is_cycle, 
              hierarchy_is_orphan, 
              node_id, 
              parent_id 
       INTO TABLE @FINAL(cds_result).
```
