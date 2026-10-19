---
title: "level-based hierarchy"
source_file: abenlevel_based_hiera_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# level-based hierarchy

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md)

## Definition

An [ABAP SQL hierarchy](abensql_hierarchy_glosry.md) that is generated from a [SQL data source](abensql_data_source_glosry.md) where certain columns define from left to right the [hierarchy levels](abenhierarchy_level_glosry.md) and where each row content of these columns represents a path from a [start node](abenstart_node_glosry.md) to a [leaf node](abenleaf_node_glosry.md) that spans these levels. In a level-based hierarchy, all [leaf nodes](abenleaf_node_glosry.md) have the same level that is the highest level defined in the data source. For each leaf node, a similar set of [ancestor nodes](abenancestor_node_glosry.md) is generated for the lower levels of the data source. In [ABAP SQL](abenabap_sql_glosry.md), the addition [`LEVELS`](../abap-programming-language/abap-database-access/abenselect_hierarchy_gen_level.md) of the [hierarchy generator](abenhierarchy_generator_glosry.md) [`HIERARCHY`](../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) can be used to generate level-based hierarchies.

[***-\>* More about**](../abap-programming-language/abap-database-access/abenselect_hierarchy_gen_level.md)
