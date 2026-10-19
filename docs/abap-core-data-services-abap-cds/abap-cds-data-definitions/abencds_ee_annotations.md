---
title: "CDS DDL - DEFINE EXTERNAL ENTITY, external_entity_annot"
source_file: abencds_ee_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - External Entities > CDS DDL - DEFINE EXTERNAL ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE EXTERNAL ENTITY, external_entity_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of a [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md) in front of the statement [`DEFINE EXTERNAL ENTITY`](abencds_define_external_entity.md) as an external entity annotation. The character `@` must be placed in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#EXTERNAL_ENTITY`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AccessControl Annotations

  - [`AccessControl.authorizationCheck`](../abap-cds-annotations/abencds_1180334353_anno.md)

## Hints

- Alongside the external entity annotations shown here, the globally valid [entity annotations](abencds_f1_entity_annotations.md) can also be specified for an external entity.

- The `AccessControl` annotation has further [framework-specific subannotations](../abap-cds-annotations/abencds_annotations_frmwrk.md).
