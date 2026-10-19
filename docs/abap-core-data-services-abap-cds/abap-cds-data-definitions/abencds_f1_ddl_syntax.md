---
title: "ABAP CDS - DDL for Data Definitions"
source_file: abencds_f1_ddl_syntax.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - DDL for Data Definitions

The [CDS data definitions](../../abap-glossary/abencds_data_definition_glosry.md) in ABAP CDS are created using the data definition language [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) in [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md). The CDS DDL follows the [general CDS syntax rules for ABAP CDS](../abap-cds-syntax/abencds_general_syntax_rules.md) and comprises the following statements for the definition and extension of [CDS entities](../../abap-glossary/abencds_entity_glosry.md) and [CDS DDIC-based entities](../../abap-glossary/abencds_ddic_based_entity_glosry.md):

- Statements for [CDS entities](abencds_view_entity.md):

  - [`DEFINE TABLE ENTITY`](abencds_define_table_entity.md)

  - [`DEFINE VIEW ENTITY`](abencds_define_view_entity.md)

  - [`DEFINE VIEW ENTITY AS PROJECTION ON`](abencds_define_view_as_projection.md)

  - [`DEFINE TABLE FUNCTION`](abencds_f1_define_table_function.md)

  - [`DEFINE EXTERNAL ENTITY`](abencds_define_external_entity.md)

  - [`DEFINE HIERARCHY`](abencds_f1_define_hierarchy.md)

  - [`DEFINE CUSTOM ENTITY`](abencds_f1_define_custom_entity.md)

  - [`DEFINE ABSTRACT ENTITY`](abencds_f1_define_abstract_entity.md)

- Statements for [CDS aspects](abencds_ddl_aspect_glosry.md):

  - [`DEFINE ASPECT`](abencds_define_aspect.md)

- Statements for [CDS DDIC-based entities](../abap-cds-obsolete-language-elements/abencds_ddic_entity.md):

  - [`DEFINE VIEW`](../abap-cds-obsolete-language-elements/abencds_define_view_v1.md)

- Language elements that can be used in various CDS entities:

  - [Entity annotations](abencds_f1_entity_annotations.md)

  - [Input parameters](abencds_f1_param.md)

  - [Typing](abencds_typing.md)

  - [Element annotations](abencds_f1_element_annotation.md)

- Statements for [CDS type definitions](abencds_tdl.md):

  - [`DEFINE TYPE [ENUM]`](abencds_define_type.md)

- Statements for [CDS function definitions](abencds_fdl.md):

  - [`DEFINE SCALAR FUNCTION`](abencds_define_scalar_function.md)

- Statements for [CDS entity extensions](abencds_view_extension.md):

  - [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md)

  - [`EXTEND ABSTRACT ENTITY`](abencds_extend_abstract_entity.md)

  - [`EXTEND CUSTOM ENTITY`](abencds_extend_custom_entity.md)

  - [`EXTEND VIEW`](abencds_extend_view.md)

## Hint

The [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of data definitions has its own editor in [ADT](../../abap-glossary/abenadt_glosry.md), which is documented there. This editor can also be used to display the actual SQL statement generated from the CDS DDL source on the database.
