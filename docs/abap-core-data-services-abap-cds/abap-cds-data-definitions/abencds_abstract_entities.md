---
title: "ABAP CDS - Abstract Entities"
source_file: abencds_abstract_entities.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Abstract Entities

A CDS abstract entity is defined in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md) in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) using the statement [`DEFINE ABSTRACT ENTITY`](abencds_f1_define_abstract_entity.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of the [ABAP Core Data Services (CDS)](../abencds.md).

A CDS abstract entity represents all type properties of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md):

- Metadata defined using [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md)

- A structured type defined using an element list

- Optionally a parameter interface defined using input parameters

- Any [CDS associations](../../abap-glossary/abencds_association_glosry.md) or [CDS compositions](../../abap-glossary/abencds_composition_glosry.md) exposed in the [element list](../abap-cds-obsolete-language-elements/abencds_select_list_association_v1.md)

An instance of a CDS abstract entity is not created as a database object and client handling is not defined. Abstract entities are [client-safe](../../abap-glossary/abenclient_safe_glosry.md) by default. Abstract entities are [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md).

A CDS abstract entity can be used as follows:

- ABAP CDS

  - A CDS abstract entity can be specified as the [association target](../../abap-glossary/abenassociation_target_glosry.md) of a [CDS association](../../abap-glossary/abencds_association_glosry.md), [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md), or [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md). A CDS association, to-child association, or CDS to-parent association of this type can be [exposed](abencds_f1_absent_list_element.md) only and cannot be created as an instance of a join expression.

  - A CDS abstract entity cannot be used as a data source of `SELECT` statements or used by SQL path expressions in other CDS entities, such as [CDS view entities](abencds_v2_views.md) or [DDIC-based CDS views](../abap-cds-obsolete-language-elements/abencds_v1_views.md).

- ABAP Programs

  - The structured type of the CDS abstract entity is known in ABAP programs. Like the type of any CDS entity, it can be used after the addition `TYPE`.

  - A CDS abstract entity cannot be used as a data source of [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statements or used by [path expressions](../../abap-programming-language/abap-database-access/abenabap_sql_path.md) in ABAP SQL.

  - The statement [`ANNOTATE ENTITY`](../abap-cds-annotations/abencds_f1_annotate_view.md) can be used to add [CDS metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md) to the [annotations](../../abap-glossary/abencds_annotation_glosry.md) of a CDS abstract entity.

- Frameworks

  - The [annotations](../../abap-glossary/abencds_annotation_glosry.md) of a CDS abstract entity can be evaluated using the methods of the class `CL_DD_DDL_ANNOTATION_SERVICE`.

  - The parameters and the CDS associations of CDS abstract entities can be evaluated by frameworks such as the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md).

## Hint

CDS abstract entities can be employed in the following cases:

- They can be used as data types whose type properties go beyond the regular [DDIC structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) in the ABAP Dictionary. Examples of this use case can be found in [ABAP RAP](../../abap-glossary/abenabap_rap_glosry.md).

- They can be used as prototype definitions of data models without being created as instances of data objects.

## More Information

For more information about CDS abstract entities, see [CDS Abstract Entities](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/c62faa730f5646b08e19cfb335de0f8a?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
