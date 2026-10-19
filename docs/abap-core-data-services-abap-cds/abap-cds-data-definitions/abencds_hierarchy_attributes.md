---
title: "CDS DDL - Hierarchy Attributes"
source_file: abencds_hierarchy_attributes.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies > CDS DDL - DEFINE HIERARCHY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Hierarchy Attributes

A [hierarchy attribute](../../abap-glossary/abenhierarchy_attribute_glosry.md) contains hierarchy-specific information about a row in a tabular result set of a database hierarchy function. The following table shows the name and meaning of the potential hierarchy attributes.

| **Name**         | **Data Type** | **Meaning**                                                                          |
|------------------|---------------|--------------------------------------------------------------------------------------|
| `HIERARCHY_RANK` | `INT8`        | Sequential number granted as a unique hierarchy node ID when a hierarchy is created. |

\|`HIERARCHY_TREE_SIZE`\|`INT8`\|Number of [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) of the hierarchy node, including the hierarchy node itself.\|

\|`HIERARCHY_PARENT_RANK`\|`INT8`\|0 for [root nodes](../../abap-glossary/abenroot_node_glosry.md), otherwise the `HIERARCHY_RANK` ID of the [parent node](../../abap-glossary/abenchild_node_glosry.md).\| \|`HIERARCHY_LEVEL`\|`INT4`\|[Hierarchy level](../../abap-glossary/abenhierarchy_level_glosry.md) of the hierarchy node. Always 1 for [root nodes](../../abap-glossary/abenroot_node_glosry.md). For their [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md), the distance from the root node plus one.\| \|`HIERARCHY_IS_CYCLE`\|`INT1`\|Flag indicating whether the hierarchy node is part of (1) or is not part of (0) a [node cycle](../../abap-glossary/abennode_cycle_glosry.md).\| \|`HIERARCHY_IS_ORPHAN`\|`INT1`\|Flag indicating whether the hierarchy node is (1) or is not (0) an [orphan node](../../abap-glossary/abenorphan_node_glosry.md).\| \|`NODE_ID`\|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): `SSTRING`, length 1333

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): Refer to [`SELECT`, `FROM HIERARCHY`, `LEVELS`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_gen_level.md). \|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): Internal character-like key of the hierarchy node that concatenates the values of all [association target](../../abap-glossary/abenassociation_target_glosry.md) fields of the associated [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) specified in the `ON` conditions. If there is only one comparison in the `ON` condition, no concatenation is required, and the data type is the data type of the specified field of the [association target](../../abap-glossary/abenassociation_target_glosry.md).

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): The content of the level column that defines the current hierarchy level.\| \|`PARENT_ID`\|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): `SSTRING`, length 1333

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): Refer to [`SELECT`, `FROM HIERARCHY`, `LEVELS`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_gen_level.md).\|For a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md): Internal character-like key of the hierarchy node that concatenates the values of all [association source](../../abap-glossary/abenassociation_source_glosry.md) fields of the associated [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) specified in the `ON` conditions. If there is only one comparison in the `ON` condition, no concatenation is required, and the data type is the data type of the specified field of the [association source](../../abap-glossary/abenassociation_source_glosry.md).

For a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) (only in ABAP SQL): The content of the level column that defines the hierarchy level f the preceding parent node.\| \|`VALID_FROM`, `VALID_UNTIL`

\|`DATS`, `TIMESTAMP`, `TIMESTAMPL`\| These attributes exist only for [temporal SQL hierarchies](../../abap-glossary/abentemporal_hierarchy_glosry.md). They contain the limits of the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of the current [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) of a [temporal SQL hierarchy](../../abap-glossary/abentemporal_hierarchy_glosry.md).\|

In the definition of a CDS hierarchy using [`DEFINE HIERARCHY`](abencds_f1_define_hierarchy.md), the hierarchy attributes can be included in the [element list](abencds_f1_hiera_element_list.md) by specifying their names explicitly after a prefix [`$node.`](abencds_f1_hiera_element.md). This makes them components of the structured type represented by the CDS hierarchy with respect to ABAP.

## Hint

In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the hierarchy attributes occur as additional [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) in the result set of an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) access. More specifically, this is also the case when a CDS hierarchy is accessed. In ABAP SQL this means that there are two different ways of accessing a hierarchy attribute specified in the element list of a CDS hierarchy. See the example class `CL_DEMO_HRRCHY_TREE_HIER_ATTR`.
