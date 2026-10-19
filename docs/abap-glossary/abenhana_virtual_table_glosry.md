---
title: "SAP HANA virtual table"
source_file: abenhana_virtual_table_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SAP HANA virtual table

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

A named, SAP HANA-local proxy object that represents a database object, such as a table or a view, in an external system. A virtual table can be accessed and queried as a normal table or view, allowing you to access data from a remote object in the [SAP HANA database](abenhana_database_glosry.md) as if the data were stored in local tables. The [SAP HANA Smart Data Access](abensap_hana_sda_glosry.md) technology uses virtual tables to communicate with external systems.

For [dynamic external entities](abencds_dynamic_ee_glosry.md), a virtual table is created as a representation of the remote database object to be read. This is done implicitly by the [database interface](abendatabase_interface_glosry.md) of [AS ABAP](abenas_abap_glosry.md) as soon as the external entity is accessed using [ABAP SQL](abenabap_sql_glosry.md) under the precondition that a configured [logical external schema](abencds_logical_schema_glosry.md) is available.
