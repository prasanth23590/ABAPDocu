---
title: "ABAP CDS - Metadata Extensions"
source_file: abencds_meta_data_extensions.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Metadata Extensions

A [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md) (MDE) adds [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md) to a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) that are not specified in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of the [data definition](../../abap-glossary/abencds_data_definition_glosry.md). Currently, CDS metadata extensions can be created for any [CDS entity](../abap-cds-data-definitions/abencds_view_entity.md) except [CDS table functions](../abap-cds-data-definitions/abencds_table_functions.md).

A CDS metadata extension is a [CDS object](../../abap-glossary/abencds_object_glosry.md) that is defined and transported in a separate piece of [DDLX source code](../../abap-glossary/abenddlx_source_code_glosry.md). These pieces of DDLX source code can only be edited in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md).

Alongside the [CDS DDL statements for data definitions](../abap-cds-data-definitions/abencds_f1_ddl_syntax.md), there is a CDS DDL statement for defining metadata extensions in DDLX source code. A prerequisite for extending a CDS entity with metadata extensions is that the annotation `@Metadata.allowExtensions` (with the default value `true`) is specified in the DDL source code of the CDS entity.

A CDS entity can have more than one CDS metadata extension. The following rules determine which metadata extension to use to evaluate the annotations:

- Each metadata extension is assigned to a layer, such as branch, partner, or customer. The layer determines the priority of the evaluation.

For more information, see the following:

- [DDL for Metadata Extensions](abencds_f1_ddlx_syntax.md)

- [Evaluation of Metadata Extensions](abencds_meta_data_extension_eval.md)

## Hints

- The [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) and the activation of a CDS entity are completely independent of any metadata extensions for this entity. For this reason, a metadata extension can only add annotations that are not already evaluated during the activation of the CDS entity.

- Metadata extensions separate the way metadata is specified from the actual data definition. Specifying the annotations that are not required to activate a CDS entity outside the DDL source code of the CDS entity has the following advantages:

  - It greatly improves the readability of the DDL source code of a data definition if it does not have to list all the metadata.

  - The metadata can be specified and transported independently of the data definition.

  - Separating the activation of metadata from the data definition avoids the need for mass activation of dependent repository objects that can occur when activating a data definition.

- When using metadata extensions for [framework-specific annotations](abencds_annotations_frmwrk.md), note the relevant rules. Otherwise error messages can occur during framework-specific checks.

- Layers allow frameworks, partners, and customers to override the metadata of a CDS entity without making modifications.

- Metadata extensions can be connected to the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md), making them switchable.
