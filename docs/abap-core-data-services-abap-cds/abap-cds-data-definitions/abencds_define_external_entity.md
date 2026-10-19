---
title: "CDS DDL - DEFINE EXTERNAL ENTITY"
source_file: abencds_define_external_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - External Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE EXTERNAL ENTITY

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@external_entity_annot1] 
[@external_entity_annot2] 
... 
[DEFINE] [WRITABLE] EXTERNAL ENTITY ext_entity_name 
  [EXTERNAL NAME ext_obj_name] 
          element_list 
WITH FEDERATED DATA 
PROVIDED AT RUNTIME | PROVIDED BY logical_external_schema[;]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@external_entity_annot1`](abencds_f1_function_annotations.md) · [`@external_entity_annot2`](abencds_f1_function_annotations.md) · [`WRITABLE`](abencds_writable_ee.md) · [`element_list`](abencds_ee_elem_list.md)

### Addition

[1. `... WRITABLE ...`](abencds_define_external_entity.md#addition-1)

[2. `... WITH FEDERATED DATA`](abencds_define_external_entity.md#addition-2)

[3. `... PROVIDED AT RUNTIME`](abencds_define_external_entity.md#addition-3)

[4. `... PROVIDED BY logical_external_schema`](abencds_define_external_entity.md#addition-4)

## Overview

### Description

Defines a [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md) `ext_entity_name` in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). A CDS external entity can be used to access data from an external system within the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). As a prerequisite, there must be a [data source](../../abap-glossary/abendata_source_glosry.md) in a remote [database schema](../../abap-glossary/abendatabase_schema_glosry.md) of a remote database in a remote system from which the data is retrieved. The name `ext_entity_name` is the name of the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) that is used to access the entity in ABAP. It must conform to the naming conventions for CDS objects that are described in the topic [ABAP CDS - General Syntax Rules](../abap-cds-syntax/abencds_general_syntax_rules.md). The external name ` ext_obj_name` must be the identical to the name of the remote database object. This name is case-sensitive and if it differs from the name of the remote database object, a runtime error occurs when accessing the external entity. `ext_obj_name` does not need to conform to the naming rules for CDS objects. It can be escaped using double quotes. This might be useful, for example, if the name contains characters not supported by ABAP.

- Entity annotations [`@entity_annot`](abencds_f1_entity_annotations.md) and external entity annotations [`@external_entity_annot`](abencds_ee_annotations.md) are used to specify optional [annotations](../../abap-glossary/abencds_annotation_glosry.md) for the CDS external entity.

  **Note:** The following restrictions apply regarding entity annotations: `AbapCatalog.extensibility` annotations are not supported for external entities, because external entities are not extensible. The `Environment.sql.passValueForClient` annotation is also not supported.

- [`element_list`](abencds_ee_elem_list.md) is used to declare the elements of the CDS external entity. These elements must mirror the names and data types of the remote data source elements, and they determine the columns of the result set of the external entity.

- `WITH FEDERATED DATA` is a mandatory addition that declares the [data federation](../../abap-glossary/abendata_federation_glosry.md) approach as the method for the data transfer.

- `PROVIDED AT RUNTIME` declares the external entity as a [dynamic external entity](../../abap-glossary/abencds_dynamic_ee_glosry.md).

- `PROVIDED BY logical_external_schema` declares the external entity as a [static external entity](../../abap-glossary/abencds_static_ee_glosry.md).

The name of a CDS external entity is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

## Addition 1

`... WRITABLE ...`

### Description

The addition [`WRITABLE`](abencds_writable_ee.md) is optional. It defines the external entity as writable. For further details, see the topic [CDS DDL - `DEFINE EXTERNAL ENTITY`, `WRITABLE`](abencds_writable_ee.md).

## Addition 2

`... WITH FEDERATED DATA`

### Description

Mandatory addition that declares the [data federation](../../abap-glossary/abendata_federation_glosry.md) approach as method for the data transfer. This addition is mandatory and there are currently not other options, so it mainly serves a semantic purpose.

## Addition 3

`... PROVIDED AT RUNTIME`

### Description

Addition that declares the external entity as a [dynamic external entity](../../abap-glossary/abencds_dynamic_ee_glosry.md). A dynamic external entity does not specify a [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) in its [data definition](../../abap-glossary/abencds_data_definition_glosry.md). The logical external schema for a dynamic external entity must be provided as a part of the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) `SELECT` statement when accessing the external entity, using a [`PROVIDED BY`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) clause. Dynamic external entities can only be accessed by ABAP SQL; they cannot be used as a data source for other [CDS entities](../../abap-glossary/abencds_entity_glosry.md). The related database artifacts of dynamic external entities, such as the [SAP HANA virtual table](../../abap-glossary/abenhana_virtual_table_glosry.md) and the [SQL view](../../abap-glossary/abensql_view_glosry.md), are generated at runtime when the external entity is accessed for the first time. They are updated at runtime whenever this is required. SQL access works only if the logical external schema has been created, activated, and configured. Otherwise, a runtime error occurs.

### Hint

Accessing a dynamic external entity with [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP) is not possible.

## Addition 4

`... PROVIDED BY logical_external_schema`

### Description

Addition that declares the external entity as a [static external entity](../../abap-glossary/abencds_static_ee_glosry.md). A static external entity is linked with a [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md) in its [data definition](../../abap-glossary/abencds_data_definition_glosry.md). Static external entities can be used as data sources in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) `SELECT` statements, in other [CDS entities](../../abap-glossary/abencds_entity_glosry.md), and in [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP). For static external entities, there is a [SQL view](../../abap-glossary/abensql_view_glosry.md) instantiated on the SAP HANA database. An [SAP HANA virtual table](../../abap-glossary/abenhana_virtual_table_glosry.md) is created after the associated logical external schema has been configured. Accessing a static external entity is possible only if the logical external schema has been created, activated, and configured. Otherwise, a runtime error occurs.
