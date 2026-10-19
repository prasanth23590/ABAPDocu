---
title: "ABAP CDS - Data Definitions"
source_file: abencds_entities.html
section: "ABAP Core Data Services (ABAP CDS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Data Definitions

CDS data definitions are written in the CDS data definition language ([CDS DDL](../../abap-glossary/abencds_ddl_glosry.md)) of [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md). CDS data definitions can be used to define [CDS entities](../../abap-glossary/abencds_entity_glosry.md), [CDS DDL aspects](abencds_ddl_aspect_glosry.md), [CDS functions](../../abap-glossary/abencds_function_glosry.md), [CDS types](../../abap-glossary/abencds_type_glosry.md), or [CDS DDIC-based entities](../../abap-glossary/abencds_ddic_based_entity_glosry.md):

- [CDS table entities](../../abap-glossary/abencds_table_entity_glosry.md)

- [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md)

- [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md)

- [CDS DDL aspects](abencds_ddl_aspect_glosry.md)

- [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md)

- [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md)

- [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md)

- [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md)

- [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md)

- [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

- [CDS user-defined types](../../abap-glossary/abencds_user_defined_type_glosry.md)

- [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md)

A [CDS entity](../../abap-glossary/abencds_entity_glosry.md) is a structured object in ABAP CDS. When DDL source code with a CDS data definition is activated, the CDS entity is created in form of a metadata representation in system tables. The CDS entities themselves are not transported. Instead they are created after the transport of a DDL source code when this code is activated in the target system. Each CDS entity is defined in a separate piece of [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md). In the development tools, CDS entities are only visible as CDS definitions in their DDL source code. The ABAP runtime framework and other frameworks access the internal metadata of CDS entities. For example, the ABAP runtime framework recognizes a CDS entity as a [global type](../../abap-glossary/abenglobal_type_glosry.md) or as a potential data source of ABAP SQL statements. The name of a CDS must be unique accordingly.

A [CDS entity](../../abap-glossary/abencds_entity_glosry.md) represents the following type properties (or signature) as a global data type:

- Metadata defined using [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md)

- A structured type defined using an element list

- Optional parameter interface defined using input parameters

- Optional [CDS associations](../../abap-glossary/abencds_association_glosry.md) exposed in the element list

There are [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md) and [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md):

- For [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md), an artifact is created on the database and they can be used as data sources in other CDS entities.

- For CDS transient entities, no artifact is created on the database and they cannot be used in read access in ABAP SQL and ABAP CDS.

- Both transient and persistent entities can be specified after the `TYPE` addition to reference its structure type and its components in ABAP programs. The components of the structured type are, as usual, specified using the structure component selector `cds_entity-comp`. [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md) can be accessed in ABAP SQL read statements or [AMDP](../../abap-glossary/abenamdp_glosry.md)

A [CDS entity](../../abap-glossary/abencds_entity_glosry.md) cannot be used as a data type in ABAP Dictionary. It cannot, for example, be used as a type of a substructure, as an include structure, or as the row type of a table type.

The following sections describe the possible CDS objects and the associated DDL statements:

- [CDS table entities](abencds_table_entities.md)

- [CDS view entities](abencds_v2_views.md)

- [CDS projection views](abencds_proj_views.md)

- [CDS aspects](abencds_aspects.md)

- [CDS table functions](abencds_table_functions.md)

- [CDS external entities](abencds_external_entity.md)

- [CDS hierarchies](abencds_hierarchies.md)

- [CDS custom entities](abencds_custom_entities.md)

- [CDS abstract entities](abencds_abstract_entities.md)

- [CDS DDIC-based entities](../abap-cds-obsolete-language-elements/abencds_ddic_entity.md)

- [ABAP CDS - Type Definitions](abencds_tdl.md)

- [ABAP CDS - Function Definitions](abencds_fdl.md)

A further section describes the problems that can arise due to [cyclical dependencies](abencds_cycle_problems.md) between CDS entities.

## Hints

- CDS entities are in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

- If a CDS role is defined for a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) using the [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) statement [`DEFINE ROLE`](../abap-cds-access-control/abencds_f1_define_role.md), implicit access control is applied when the CDS entity is accessed in ABAP SQL. Only that data can be accessed that meets the [access conditions](../../abap-glossary/abenaccess_condition_glosry.md). Access control can be switched off using the value `#NOT_ALLOWED` for the annotation `@AccessControl.authorizationCheck` and using the addition [`WITH PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in the [`FROM`](../../abap-programming-language/abap-database-access/abapfrom_clause.md) clause of an ABAP SQL query.

- When a CDS entity is used as a data source in another CDS entity, its [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) defined in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) is not considered when the wrapping entity is accessed. CDS access control only applies to the entry level entities accessed by ABAP SQL.

- Once a piece of DDL source code has been activated, its name or names is/are stable and cannot be modified. The same applies to the DDL source code of a [CDS entity extension](../../abap-glossary/abencds_entity_extend_glosry.md) (and, if available, its [DDIC append view](../../abap-glossary/abenddic_append_view_glosry.md)).

- The DDL source code of a data definition for a CDS entity is edited in a different editor than the [DDLA source code](../../abap-glossary/abenddla_source_code_glosry.md) of a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md), the [DDLX source code](../../abap-glossary/abenddlx_source_code_glosry.md) of a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md), and the [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) of a [CDS role](../../abap-glossary/abencds_role_glosry.md) for [CDS access control](../../abap-glossary/abencds_access_control_glosry.md). The [ADT](../../abap-glossary/abenadt_glosry.md) documentation describes how the different types of source code are created.

- A structure type defined using a CDS entity exists alongside the [DDIC structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) in ABAP Dictionary.
