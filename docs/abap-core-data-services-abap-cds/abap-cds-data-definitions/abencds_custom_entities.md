---
title: "ABAP CDS - Custom Entities"
source_file: abencds_custom_entities.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Custom Entities

A [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md) is defined in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md) using the statement [`DEFINE CUSTOM ENTITY`](abencds_f1_define_custom_entity.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of the [ABAP Core Data Services (CDS)](../abencds.md). The name of the CDS custom entity must match the name of the DDL source code.

Purpose and use cases:

CDS custom entities allow developers to implement their own data provision using ABAP. Data retrieval is implemented via an ABAP class and performed at runtime. On CDS level, only an interface is defined, while the implementation of the logic is encapsulated in the application server artifact. Custom entities are used if data access cannot be done via means of [SQL](../../abap-glossary/abensql_glosry.md) and the available CDS feature set and other CDS entity types. For example, custom entities can be used when

- data is stored in non-relational storage, for example in a [BLOB](../../abap-glossary/abenblob_glosry.md).

- data is stored in SAP liveCache and access is done via ABAP APIs.

- data cannot be computed by means of CDS due to additional application-server-side logic.

- a data model can be defined via CDS views, but the [DCL](../../abap-glossary/abendcl_glosry.md) feature set is not sufficient to define the necessary authorizations.

Data retrieval is also possible using an http client.

In the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md), custom entities are used as a data model basis for [RAP unmanaged queries](../../abap-glossary/abenrap_unmanged_query_glosry.md).

A CDS custom entity represents all type properties of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md):

- Metadata defined using [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md)

- A structured type defined using an [element list](abencds_f1_custom_element_list.md)

- Optionally, a parameter interface defined using [input parameters](abencds_f1_custom_parameter_list.md)

- Any [CDS associations](../../abap-glossary/abencds_association_glosry.md), [CDS to-child associations](../../abap-glossary/abento_child_association_glosry.md), or [CDS to-parent associations](../../abap-glossary/abento_parent_association_glosry.md) exposed in the element list.

A CDS custom entity is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md).

A CDS custom entity can be used as follows:

- ABAP CDS

  - A CDS custom entity can be specified as the [association target](../../abap-glossary/abenassociation_target_glosry.md) of a [CDS association](../../abap-glossary/abencds_association_glosry.md), [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md), or [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md). A CDS association, CDS to-child association, or CDS to-parent association of this type can be [exposed](abencds_f1_custom_element.md) only and cannot be created as an instance of a join expression. Such associations can only be followed in Fiori OData scenarios where the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md) (not SQL) is used to execute the query.

  - Since no SQL artifact is generated for CDS custom entities and the query is implemented in ABAP, a CDS custom entity cannot be used as a data source of `SELECT` statements or used by SQL path expressions in other [CDS entities](../../abap-glossary/abencds_entity_glosry.md).

- ABAP Programs

  - The structured type of the CDS custom entity is known in ABAP programs. Like the type of any CDS entity, it can be used after the addition `TYPE`.

  - A CDS custom entity cannot be used as a data source of [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statements or used by [path expressions](../../abap-programming-language/abap-database-access/abenabap_sql_path.md) in ABAP SQL.

- Frameworks

  - In the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md), custom entities are used as a data model basis for [RAP unmanaged queries](../../abap-glossary/abenrap_unmanged_query_glosry.md). The ABAP query is in this case executed by a framework such as the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md).

  - The [annotations](../../abap-glossary/abencds_annotation_glosry.md) of a CDS custom entity can be evaluated using the methods of the class `CL_DD_DDL_ANNOTATION_SERVICE`.

  - The parameters and the CDS associations of CDS custom entities can be evaluated by frameworks such as the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md).

An instance of a CDS custom entity is not created as a database object and [client handling](../../abap-glossary/abenclient_handling_glosry.md) is not defined. Custom entities are [client-safe](../../abap-glossary/abenclient_safe_glosry.md) by default.

## Hints

- Custom entities can be nodes in RAP business objects, for example root, parent and/or child nodes using `ROOT` and composition relationships.

## More Information

- Development guide for the ABAP RESTful Application Programming model, section [Query](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/511a134f89614e77a2231d0af5b924f8?version=sap_cross_product_abap).

- ABAP Data Models guide, section about [CDS custom entities](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/0d1e361dedc04116ba335470f3adf408?version=sap_cross_product_abap).
