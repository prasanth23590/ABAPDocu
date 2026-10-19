---
title: "ABAP SQL Hierarchies"
source_file: abensql_hierarchies.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL Hierarchies

An [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) is a tabular set of rows where each row represents one [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) of a [parent-child hierarchy](../../abap-glossary/abenpcr_hierarchy_glosry.md). ABAP SQL hierarchies appear in ABAP as follows:

- As the result set of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md). It is a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) created from a data source using [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) defined by a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md).

- As the result set of the hierarchy generator [`HIERARCHY`](abenselect_hierarchy_generator.md). The hierarchy generator can generate the following hierarchies:

  - A [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) created from a data source using [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) defined by a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md).

  - A [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) that is created from a data source using a set of its columns for defining the [hierarchy levels](../../abap-glossary/abenhierarchy_level_glosry.md).

- As the result set of a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md) in the subsequent queries of the current [`WITH`](abapwith.md) statement.

The columns of an ABAP SQL hierarchy are composed as follows:

- Components of the data source used when the hierarchy is created by a CDS hierarchy or created by the hierarchy generator.

  - In the case of CDS hierarchies and CTE hierarchies, these are exactly the components listed here.

  - In the case of the hierarchy generator `HIERARCHY`, these are all components of the source of the SQL hierarchy.

- Additional [hierarchy columns](abenddddl_hierarchy.md). For each hierarchy node, the hierarchy columns contain its [hierarchy attributes](../../abap-glossary/abenhierarchy_attribute_glosry.md), which describe certain hierarchy-specific properties.

## Hints

- In an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md), the [hierarchy column](../../abap-glossary/abenhierarchy_column_glosry.md) [`HIERARCHY_LEVEL`](abenddddl_hierarchy.md) contains the value of the hierarchy level of a hierarchy node.

- Sibling nodes have the same values in the hierarchy column [`HIERARCHY_PARENT_RANK`](abenddddl_hierarchy.md).

- While each SQL hierarchies is a [parent-child hierarchy](../../abap-glossary/abenpcr_hierarchy_glosry.md), there are differences between [parent-child-based hierarchies](../../abap-glossary/abenpc_based_hiera_glosry.md) and [level-based hierarchies](../../abap-glossary/abenlevel_based_hiera_glosry.md):

  - A [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) is general in a sense that it can represent any parent child hierarchy. There can be [orphan nodes](../../abap-glossary/abenorphan_node_glosry.md), [child nodes](../../abap-glossary/abenchild_node_glosry.md) with multiple [parent nodes](../../abap-glossary/abenparent_node_glosry.md), [node cycles](../../abap-glossary/abennode_cycle_glosry.md) and the path lengths between a [root nodes](../../abap-glossary/abenroot_node_glosry.md) and [leave nodes](../../abap-glossary/abenleaf_node_glosry.md) is not fixed.

  - A [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) is special in a sense that it represents [tree hierarchies](../../abap-glossary/abentree_hierarchy_glosry.md) where no orphans, multiple parents or cycles are possible. The path lengths between root nodes and leaf nodes is defined by the highest level and fixed for the complete SQL hierarchy.

- In a [parent-child hierarchy](../../abap-glossary/abenpcr_hierarchy_glosry.md) created from a data source using [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) defined by a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md):

  - The [root nodes](../../abap-glossary/abenroot_node_glosry.md) are part of the [root node set](../../abap-glossary/abenroot_node_set_glosry.md). The [hierarchy column](../../abap-glossary/abenhierarchy_column_glosry.md) [`HIERARCHY_PARENT_RANK`](abenddddl_hierarchy.md) of a root node of a SQL hierarchy contains the value 0 and the hierarchy column [`HIERARCHY_LEVEL`](abenddddl_hierarchy.md) contains the value 1.

  - The nodes of the root node set are not considered [orphan nodes](../../abap-glossary/abenorphan_node_glosry.md). The hierarchy column [`HIERARCHY_IS_ORPHAN`](abenddddl_hierarchy.md) contains the value 0.

  - In case of a [node cycle](../../abap-glossary/abennode_cycle_glosry.md), the [hierarchy column](../../abap-glossary/abenhierarchy_column_glosry.md) [`HIERARCHY_IS_CYCLE`](abenddddl_hierarchy.md) contains the value 1.
