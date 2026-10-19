---
title: "ABAP CDS - External Entities"
source_file: abencds_external_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - External Entities

A [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md) is defined in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md) in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) using the statement [`DEFINE EXTERNAL ENTITY`](abencds_define_external_entity.md). A CDS external entity is a [persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) that can be used to access data from external database systems within the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). The external systems can be other [SAP HANA](../../abap-glossary/abenhana_database_glosry.md) or non-SAP HANA database systems. The properties of the connection between an external entity and the external system are configured using a [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md). The connection is managed using [SAP HANA Smart Data Access](../../abap-glossary/abensap_hana_sda_glosry.md). [Dynamic external entities](../../abap-glossary/abencds_dynamic_ee_glosry.md) and [static external entities](../../abap-glossary/abencds_static_ee_glosry.md) are available. External entities are read-only by default. They can be defined as [writable](../../abap-glossary/abenwritable_ee_glosry.md) using the addition [`WRITABLE`](abencds_writable_ee.md).

A CDS external entity includes the following:

- The CDS entity

  A CDS external entity is declared as a CDS entity `external_entity` using the statement [`DEFINE EXTERNAL ENTITY`](abencds_define_external_entity.md). As a global data type, the CDS entity represents a structured type with the [elements of the CDS external entity](abencds_ee_elem_list.md) as components and can be used as follows:

  - In ABAP, the CDS entity can be used as a data type and in ABAP SQL read statements. The addition [`PROVIDED BY`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) for specifying a [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) at runtime is mandatory for dynamic external entities, but it is not required for static external entities.

  - Static external entities can be used as a data source for other CDS entities and in [ABAP Managed Database Procedures (AMDP)](../../abap-glossary/abenabap_managed_db_proc_glosry.md). For dynamic external entities, this is not possible.

  - A CDS external entity cannot be used as a data type for definitions of [dictionary objects](../../abap-glossary/abendictionary_object_glosry.md).

    A CDS external entity is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

- A [CDS logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) that maps the external entity to a specific physical external system or database, and to a specific [database schema](../../abap-glossary/abendatabase_schema_glosry.md) in such a remote system. A logical external schema is represented by a transportable [repository object](../../abap-glossary/abenrepository_object_glosry.md) and it must be configured for the connection to work. For more details, see the topic [ABAP CDS - CDS Logical External Schema](abencds_logical_external_schema.md).

Currently, [dynamic external entities](../../abap-glossary/abencds_dynamic_ee_glosry.md) and [static external entities](../../abap-glossary/abencds_static_ee_glosry.md) are available.

- A dynamic external entity does not specify a logical external schema in its data definition, but uses the addition [`PROVIDED AT RUNTIME`](abencds_define_external_entity.md) instead. The logical external schema for a dynamic external entity must be specified as a part of the ABAP SQL `SELECT` statement when the external entity is accessed, using a [`PROVIDED BY`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) clause. Dynamic external entities can only be accessed by ABAP SQL; they cannot be used as a data source for other CDS entities.

- A static external entity specifies a logical external schema in its data definition using the addition `PROVIDED BY logical_external_schema`. Static external entities can be used as data sources in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) `SELECT` statements, in other [CDS entities](../../abap-glossary/abencds_entity_glosry.md), and in [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP).

External entities can be defined as [writable](../../abap-glossary/abenwritable_ee_glosry.md) using the optional addition [`WRITABLE`](abencds_writable_ee.md). Writable external entities allow modifying data on external database systems using the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md) operations. Besides a logical external schema, an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) is required to establish a [service connection](../../abap-glossary/abenservice_connection_glosry.md) and enable the logical external schema for write access.

When accessing [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) external entities, an implicit filtering to the ID contained in the SAP HANA session variable `CDS_CLIENT` is applied. The value of the ID is defined in the logical external schema. External entities are [client-safe](../../abap-glossary/abenclient_safe_glosry.md) by default.

[Table buffering](../../abap-glossary/abentable_buffering_glosry.md) with a [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md) is currently not supported for external entities.

## Hints

- Releasing CDS external entities or logical external schemas as a [released API](../../abap-glossary/abenreleased_api_glosry.md) is not supported.

- Extending a CDS external entity using a [CDS entity extension](../../abap-glossary/abencds_entity_extend_glosry.md) is currently not supported.

## More Information

- [CDS External Entities](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/dc24d9c4a9294dd0b2b3f718a507e80e?version=sap_cross_product_abap) - ABAP Data Models guide (SAP Help Portal)

-
