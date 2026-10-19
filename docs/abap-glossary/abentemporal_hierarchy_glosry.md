---
title: "temporal SQL hierarchy"
source_file: abentemporal_hierarchy_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# temporal SQL hierarchy

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md)

## Definition

A special [ABAP SQL hierarchy](abensql_hierarchy_glosry.md) that only contains [hierarchy nodes](abenhierarchy_node_glosry.md) that meet certain conditions for time intervals. When the SQL hierarchy is created with the addition [`PERIOD`](../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../abap-programming-language/abap-database-access/abenabap_sql.md) or [`PERIOD`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_hierarchy.md) in [ABAP CDS](abenabap_cds_glosry.md), columns of the [SQL data source](abensql_data_source_glosry.md) of the hierarchy are defined as interval limits of so-called [periods](abenperiod_glosry.md) and a time interval is specified for the [root node set](abenroot_node_set_glosry.md). [Validity intervals](abenvalidity_interval_glosry.md) are determined as intersections of these time intervals. Only nodes with non-empty validity intervals are included in the hierarchy. The validity intervals of [child nodes](abenchild_node_glosry.md) result from their period and the validity interval of the [parent node](abenparent_node_glosry.md).
