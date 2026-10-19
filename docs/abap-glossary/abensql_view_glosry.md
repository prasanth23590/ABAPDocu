---
title: "SQL view"
source_file: abensql_view_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SQL view

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

[ABAP-managed database object](abenabap_managed_db_object_glosry.md) that is generated automatically by the [ABAP Dictionary](abenabap_dictionary_glosry.md) or by [ABAP CDS](abenabap_cds_glosry.md) for [CDS entities](abencds_entity_glosry.md), such as:

- [CDS view entity](abencds_v2_view_glosry.md), the name of the SQL view is the same as the name of the CDS view entity

- [CDS transactional query](abencds_transactional_pv_glosry.md), where the name of the SQL view is the same as the name of the CDS transactional query

- [CDS transactional interface](abencds_trans_interface_glosry.md), where the name of the SQL view is the same as the name of the CDS transactional interface

- [CDS hierarchy](abencds_hierarchy_glosry.md), the name of the SQL view is the same as the name of the CDS hierarchy view

- [CDS DDIC-based view (obsolete)](abencds_v1_view_glosry.md), the name of the SQL view is the same as the name of the respective [CDS-managed DDIC view (obsolete)](abencds_mngdddic_view_glosry.md)

Like all ABAP-managed database objects, an SQL view should mainly be accessed with [ABAP SQL](abenabap_sql_glosry.md) using the names defined in the ABAP Dictionary or in ABAP CDS. For [CDS DDIC-based views (obsolete)](abencds_v1_view_glosry.md), the name of the CDS entity should be used and not the name of the CDS-managed DDIC view (obsolete). When using [AMDP](abenamdp_glosry.md), only the technical name of the SQL view can be used.
