---
title: "ABAP CDS - CDS Logical External Schema"
source_file: abencds_logical_external_schema.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - External Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - CDS Logical External Schema

A [CDS logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) is a transportable [repository object](../../abap-glossary/abenrepository_object_glosry.md) that is defined in a form-based tool in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). It maps one or more [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md) to a specific physical external system or database, and to a specific [database schema](../../abap-glossary/abendatabase_schema_glosry.md) in such a remote system. A logical external schema must be created, activated, and configured to enable a remote connection. A logical external schema can have one or more configurations. Each configuration refers to exactly one client. A logical external schema configuration triggers the creation of an [SAP HANA remote source](../../abap-glossary/abensap_hana_remote_source_glosry.md) ad hoc at runtime when an external entity with a specific logical external schema is accessed. The configuration specifies the connection details required by the [SAP HANA remote source](../../abap-glossary/abensap_hana_remote_source_glosry.md) to connect to an external system.

A logical external schema can be bound to one or more external entities. For dynamic external entities, the binding is done using the addition [`PROVIDED BY`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in ABAP SQL when accessing the external entity. Static external entities specify a logical external schema in their data definition using the addition [`PROVIDED BY logical_external_schema`](abencds_define_external_entity.md).

A logical external schema can have one or more configurations, one per client.

In [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), a logical external schema must be included as an outbound service in a communication scenario in addition to the configuration.

## Hints

- In [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), the configuration of a logical external schema is done in the `Communication Arrangement` SAP Fiori application.

- You can create, activate, and transport an external entity and a logical external schema without any configuration. However, data transfer only works if there is a valid configuration.
