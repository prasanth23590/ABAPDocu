---
title: "ABAP CDS - View Entities"
source_file: abencds_v2_views.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - View Entities

A [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) is a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) defined using the statement [`DEFINE VIEW ENTITY`](abencds_define_view_entity.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of ABAP Core Data Services (CDS). A CDS view entity can be used to select fields from one or more data sources (database tables or other CDS entities). Additional semantic properties can be added by using annotations. CDS view entities are the successor of [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). They have the same structure and serve the same purpose as [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). Generally spoken, they represent an improved version of *classic* [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

When a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) is activated, a repository object is created. This repository object can be accessed using the name of the CDS view entity. As a global data type, each CDS view entity represents a structured type with the [elements of the CDS view entity](abencds_select_list_entry_v2.md) as components and can be used like any [CDS entity](../../abap-glossary/abencds_entity_glosry.md):

- In ABAP CDS, the CDS entity can be used as a data source of other CDS entities.

- In ABAP programs, the CDS entity can be used as a data type and in ABAP SQL read statements.

- The CDS entity cannot be used as a data type for definitions of [dictionary objects](../../abap-glossary/abendictionary_object_glosry.md).

The name of the CDS entity is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

A CDS view entity is a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md).

The following sections describe client handling and table buffering for CDS view entities. Afterwards, the statement [`DEFINE VIEW ENTITY`](abencds_define_view_entity.md) and all possible additions are described.

- [Client handling](abencds_v2_view_client_handling.md)

- [Table buffering](abencds_v2_view_buffering.md)

- [Creation of a CDS view entity](abencds_define_view_entity.md)

## Hint

The programming of [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) using the DDL of the Core Data Services is one of the tasks included in the implementation of data models and is not usually the responsibility of regular ABAP application programmers. Once created, [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) are used in ABAP programs using ABAP SQL read statements and must be stable enough to allow this.

## More Information

For more information about CDS view entities, see [*CDS View Entities*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/8b3e8e8b8797432abecd7d1fbb6d5c12?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
