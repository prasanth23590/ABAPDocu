---
title: "ABAP CDS - Table Entities"
source_file: abencds_table_entities.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Table Entities

A [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md) is a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) defined using the statement [`DEFINE TABLE ENTITY`](abencds_define_table_entity.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of ABAP Core Data Services (CDS). A CDS table entity describes a physical [database table](../../abap-glossary/abendatabase_table_glosry.md) on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) connected to the current AS ABAP.

When a CDS table entity is activated, a repository object is created. This repository object can be accessed using the name of the CDS table entity. As a global data type, each CDS table entity represents a structured type with the [elements of the CDS table entity](abencds_select_list_entry_v2.md) as components and can be used like any [CDS entity](../../abap-glossary/abencds_entity_glosry.md):

- In ABAP CDS, the CDS entity can be used as a data source of other CDS entities.

- In ABAP programs, the CDS entity can be used as a data type and in ABAP SQL read and write statements.

- The CDS entity cannot be used as a data type for definitions of [dictionary objects](../../abap-glossary/abendictionary_object_glosry.md).

Additionally, CDS table entities can be used in [ABAP SQL write access](../../abap-programming-language/abap-database-access/abenabap_sql_writing.md), for example, for inserting, modifying, and deleting data on the database. CDS table entities are therefore [writable database objects](../../abap-glossary/abenwritable_db_obj_glosry.md).

The name of the CDS entity is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

A CDS table entity is a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md).

The following sections describe client handling for CDS table entities. Afterwards, the statement [`DEFINE TABLE ENTITY`](abencds_define_table_entity.md) and all possible additions are described.

- [Client handling](abencds_table_entity_client.md)

- [`DEFINE TABLE ENTITY`](abencds_define_table_entity.md)

## Hints

- Access control with [CDS roles](../../abap-glossary/abencds_role_glosry.md) can be defined for table entities using the CDS DCL statement [`DEFINE ROLE`](../abap-cds-access-control/abencds_f1_define_role.md).

- [Metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md) can be attached to a CDS table entity to add further annotations.

- It is currently not possible to extend a CDS table entity.

## More Information

For more information about CDS table entities, see [*CDS Table Entities*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/100ab51935544f18b4f4be9b4abb91e8?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
