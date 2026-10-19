---
title: "ABAP Core Data Services (ABAP CDS)"
source_file: abencds.html
section: "ABAP Core Data Services (ABAP CDS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Core Data Services (ABAP CDS)

The ABAP Core Data Services (ABAP CDS) are the implementation of the general [CDS](../abap-glossary/abencds_glosry.md) concept for AS ABAP. ABAP CDS makes it possible to define semantic data models on the [standard database](../abap-glossary/abenstandard_db_glosry.md) of an AS ABAP and support [ABAP RAP](../abap-glossary/abenabap_rap_glosry.md) using behavior models.

- The entities of the data models defined in ABAP CDS provide enhanced access functions compared to previous DDIC database tables and DDIC views defined in [ABAP Dictionary](../abap-dictionary-ddic/abenabap_dictionary.md), thus enabling the optimization of ABAP SQL-based applications. This is particularly the case if an AS ABAP uses an [SAP HANA database](../abap-glossary/abenhana_database_glosry.md), since its in-memory characteristics can be used optimally.

- [ABAP RAP](../abap-glossary/abenabap_rap_glosry.md) is based both on the data models defined in ABAP CDS and on [RAP behavior definitions](../abap-glossary/abencds_behavior_definition_glosry.md), which model behavior.

The data models are defined in the form of [CDS objects](../abap-glossary/abencds_object_glosry.md) using the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md), [CDS SDL](../abap-glossary/abencds_sdl_glosry.md), and [CDS DCL](../abap-glossary/abencds_dcl_glosry.md) provided by ABAP CDS in the [syntax of ABAP CDS](abap-cds-syntax/abencds_syntax.md) in [CDS source code](../abap-glossary/abencds_source_code_glosry.md). [CDS annotations](../abap-glossary/abencds_annotation_glosry.md) can be used to define metadata for CDS objects.

Data exchange between ABAP CDS data models and data models on different platforms is possible using [CDS schema notation](../abap-glossary/abencds_schema_notation_glosry.md) (CSN). CSN is a data format for data exchange between data models and it can be used, for example, to exchange metadata between [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md) and SAP Analytics Cloud (SAC).

- [CDS Annotations](abap-cds-annotations/abencds_annotations.md)

  A CDS annotation adds metadata to a CDS object. Annotations can be specified in [DDL source code](../abap-glossary/abenddl_source_code_glosry.md), [SDL source code](../abap-glossary/abensdl_source_code_glosry.md), and [DCL source code](../abap-glossary/abenddl_source_code_glosry.md) and outsourced to [metadata extensions](../abap-glossary/abencds_metadata_extension_glosry.md). [Annotation definitions](../abap-glossary/abencds_anno_definition_glosry.md) can be used to create an annotation itself as a CDS object. An annotation definition prescribes how an annotation is used.

- [CDS Data Definitions](abap-cds-data-definitions/abencds_entities.md)

  CDS data definitions are created using the [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) of the ABAP CDS in [DDL source code](../abap-glossary/abenddl_source_code_glosry.md). They define the following [CDS entities](../abap-glossary/abencds_entity_glosry.md) that can be accessed as a data type in ABAP programs and as a data source in reading ABAP SQL statements.

  - [CDS Table Entities](abap-cds-data-definitions/abencds_table_entities.md)

    [CDS table entities](../abap-glossary/abencds_table_entity_glosry.md) that define database tables in ABAP CDS.

  - [CDS View Entities](abap-cds-data-definitions/abencds_v2_views.md)

    [CDS entities](../abap-glossary/abencds_entity_glosry.md) that use SQL to access other data sources and can be enriched semantically using annotations.

  - [CDS Projection Views](abap-cds-data-definitions/abencds_proj_views.md)

    Special [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md) that are based on a another CDS view entity (called [CDS projected entity](../abap-glossary/abencds_pv_projected_entity_glosry.md)). CDS projection views adapt a CDS data model for service-specific use cases.

  - [ABAP CDS - Aspects](abap-cds-data-definitions/abencds_aspects.md)

    [CDS objects](../abap-glossary/abencds_object_glosry.md) that can be used to define reusable elements and calculations centrally to be reused across various [CDS entities](../abap-glossary/abencds_entity_glosry.md).

  - [CDS Table Functions](abap-cds-data-definitions/abencds_table_functions.md)

    [CDS entities](../abap-glossary/abencds_entity_glosry.md) that are implemented in [AMDP functions](../abap-glossary/abenamdp_function_glosry.md) and return a tabular result set.

  - [CDS External Entities](abap-cds-data-definitions/abencds_external_entity.md)

    [CDS entities](../abap-glossary/abencds_entity_glosry.md) that can be used to access data from external database systems within the AS ABAP.

  - [CDS Hierarchies](abap-cds-data-definitions/abencds_hierarchies.md)

    [CDS entities](../abap-glossary/abencds_entity_glosry.md) that create an [ABAP SQL hierarchy](../abap-glossary/abensql_hierarchy_glosry.md) from a data source.

  - [CDS Custom Entities](abap-cds-data-definitions/abencds_custom_entities.md)

    [CDS entities](../abap-glossary/abencds_entity_glosry.md) for data models whose runtime is implemented manually.

  - [CDS Abstract Entities](abap-cds-data-definitions/abencds_abstract_entities.md)

    [CDS entities](../abap-glossary/abencds_entity_glosry.md) that describe only type properties and for which no database objects are instantiated.

  - [CDS DDIC-based views (obsolete)](abap-cds-obsolete-language-elements/abencds_v1_views.md)

    [CDS entities](../abap-glossary/abencds_entity_glosry.md) that use SQL to access other data sources and can be enriched semantically using annotations. These entities are technically based on [dictionary objects](../abap-glossary/abendictionary_object_glosry.md) and were superseded from release 7.81 on by [CDS view entities](../abap-glossary/abencds_v2_view_glosry.md), which are no longer based on dictionary objects. The [CDS DDL](../abap-glossary/abencds_ddl_glosry.md) in ABAP CDS also contains language elements for enhancing CDS entities.

- [CDS Type Definitions](abap-cds-data-definitions/abencds_tdl.md)

  CDS type definitions define data types natively in ABAP CDS. They can be enhanced with [CDS annotations](../abap-glossary/abencds_annotation_glosry.md) and they can be used for typing, casting, and as operands of expressions in [CDS entities](../abap-glossary/abencds_entity_glosry.md) and in the [ABAP language](../abap-glossary/abenabala_glosry.md).

  - [CDS Simple Types](abap-cds-data-definitions/abencds_simple_types.md)

    [CDS user-defined type](../abap-glossary/abencds_user_defined_type_glosry.md) that defines an [elementary data type](../abap-glossary/abenelementary_data_type_glosry.md).

  - [CDS Enumerated Types](abap-cds-data-definitions/abencds_enumeration_types.md)

    [CDS user-defined type](../abap-glossary/abencds_user_defined_type_glosry.md) that defines an [enumerated type](../abap-glossary/abenenum_type_glosry.md).

- [CDS Function Definitions](abap-cds-data-definitions/abencds_fdl.md)

  [CDS function definitions](../abap-glossary/abencds_function_definition_glosry.md) allow the definition of user-defined [CDS functions](../abap-glossary/abencds_function_glosry.md) that encapsulate algorithms in reusable code that can be used in operand positions of [CDS entities](../abap-glossary/abencds_entity_glosry.md). There is currently only one type of CDS function definition:

  - [CDS Scalar Functions](abap-cds-data-definitions/abencds_scalar_functions.md)

    [CDS function definitions](../abap-glossary/abencds_function_definition_glosry.md) that are implemented in [AMDP functions](../abap-glossary/abenamdp_function_glosry.md) and return a scalar result.

- [CDS Tuning Objects](abap-cds-tuning-objects/abencds_tuning_objects.md)

  [ABAP tuning objects](../abap-glossary/abenabap_tuning_object_glosry.md) for CDS objects to define technical settings and tunings that can be transported separately.

- [CDS Access Control](abap-cds-access-control/abencds_access_control.md)

  [CDS access control](../abap-glossary/abencds_access_control_glosry.md) is based on [CDS roles](../abap-glossary/abencds_role_glosry.md) that are defined in [CDS DCL](../abap-glossary/abencds_dcl_glosry.md) in [DCL source code](../abap-glossary/abendcl_source_code_glosry.md). When [CDS SQL entities](../abap-glossary/abencds_sql_entity_glosry.md) that are assigned a CDS role are accessed, additional [access conditions](../abap-glossary/abenaccess_condition_glosry.md) are evaluated by default.

- [CDS System Entities](abap-cds-system-entities/abencds_system_entities.md)

  [CDS system entities](../abap-glossary/abencds_system_entity_glosry.md) are predefined CDS entities for common usage in ABAP CDS and ABAP SQL.

## More Information

For further details on ABAP Core Data Services, check the [*ABAP Data Models*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/977a051cea1c4059be2500dcbf2d3d7d?version=sap_cross_product_abap) development guide on SAP Help Portal.

## Hints

- [CDS objects](../abap-glossary/abencds_object_glosry.md) are transported using the [CDS source code](../abap-glossary/abencds_source_code_glosry.md). The actual objects, like the [CDS entities](../abap-glossary/abencds_entity_glosry.md) that are defined using a [CDS data definition](../abap-glossary/abencds_data_definition_glosry.md) in [DDL source code](../abap-glossary/abenddl_source_code_glosry.md), are created after the transport by being activated in the target system.

- [CDS source code](../abap-glossary/abencds_source_code_glosry.md) can only be programmed in the Eclipse-based [ABAP development tools for Eclipse](../abap-glossary/abenadt_glosry.md). There are different editors for the Data Definition Language (DDL), the Service Definition Language (SDL), and the Data Control Language (DCL). The ADT documentation describes how these editors are used.
