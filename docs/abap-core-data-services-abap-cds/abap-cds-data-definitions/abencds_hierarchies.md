---
title: "ABAP CDS - Hierarchies"
source_file: abencds_hierarchies.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Hierarchies

A CDS hierarchy is defined in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md) in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) using the statement [`DEFINE HIERARCHY`](abencds_f1_define_hierarchy.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of the [ABAP Core Data Services (CDS)](../abencds.md). The name of the CDS hierarchy must match the name of the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md).

A CDS hierarchy represents an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) ([parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md)) created when the CDS hierarchy is accessed. CDS hierarchies can currently only be used when the [standard database](../../abap-glossary/abenstandard_db_glosry.md) is a [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). When a CDS hierarchy is activated, a view with the same name is created as an [ABAP-managed database object](../../abap-glossary/abenabap_managed_db_object_glosry.md) on the database. This view accesses a hierarchy generator function such as [`HIERARCHY`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/2969da89b87f4abd85fd0b5f9f5bc395).

A CDS hierarchy is declared as a CDS entity `hierarchy` using the statement [`DEFINE HIERARCHY`](abencds_f1_define_hierarchy.md). As a global data type, the CDS entity represents a structured type with the [elements of the CDS hierarchy](abencds_f1_hiera_element_list.md) as components and can be used like any [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

- In ABAP CDS, the CDS entity can be used as a data source of other CDS entities.

- In ABAP, the CDS entity can be used as a data type and in ABAP SQL read statements.

- The CDS entity cannot be used as a data type for definitions of [dictionary objects](../../abap-glossary/abendictionary_object_glosry.md).

A CDS hierarchy is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

A CDS hierarchy is a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md).

When using CDS hierarchies, the handling of the special [hierarchy attributes](../../abap-glossary/abenhierarchy_attribute_glosry.md) is of special importance. These attributes occur as part of the result set of the hierarchy function on the database:

- The hierarchy attributes can be accessed explicitly as follows:

  - The prefix [`$node.`](abencds_f1_hiera_element.md) can be used to list them in the [element list](abencds_f1_hiera_element_list.md) of the CDS hierarchy and grant them an alias name. They are then applied like a regular element of the CDS hierarchy.

  - When a ABAP SQL query is applied to a CDS hierarchy, they are handled as additional [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md), regardless of their element list, and their names can be used in explicitly specified columns

    This makes it possible to specify a hierarchy attribute in the element list of the CDS hierarchy in two different ways in an ABAP SQL query, either by using the name of the element or by using the name of the hierarchy column.

- When CDS hierarchies are used, the hierarchy attributes are not respected implicitly in the following cases:

  - When used as a data source of other CDS entities.

  - When used as a data type.

  - When used as a data source in [ABAP SQL](../../abap-programming-language/abap-database-access/abenabap_sql.md), if `*` or `...~*` is specified in the [`SELECT`](../../abap-programming-language/abap-database-access/abapselect_list.md) list.

    In these cases, only the explicit elements of the [element list](abencds_f1_hiera_element_list.md) are respected. These can, however, represent hierarchy attributes.

CDS hierarchies can be released as stable APIs under the [C1 release contract for system internal use](../../abap-glossary/abenc1_contract_glosry.md).

## Hints

- For a CDS hierarchy, no repository object is created in ABAP Dictionary.

- A hierarchy attribute does not become part of a structured data type created by a CDS hierarchy until it is listed explicitly in the element list of the CDS hierarchy.

- For information about client handling of CDS hierarchies, see [Client Handling in CDS Hierarchies](abencds_hiera_client_handling.md).

- CDS hierarchies cannot be processed by the [ABAP SQL in-memory engine](../../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md). An ABAP SQL statement that accesses a CDS hierarchy bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](../../abap-programming-language/abap-database-access/abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## More Information

For more information about CDS hierarchies, see [*CDS Hierarchies*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/b3232b0a219d4f7098b47de3c3710509?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
