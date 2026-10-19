---
title: "CDS DDL - DEFINE HIERARCHY, hierarchy_annot"
source_file: abencds_f1_hierarchy_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies > CDS DDL - DEFINE HIERARCHY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE HIERARCHY, hierarchy_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a hierarchy annotation in front of the statement [`DEFINE HIERARCHY`](abencds_f1_define_hierarchy.md) in the definition of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md). The character `@` must be placed directly in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#HIERARCHY`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.dataMaintenance`](../abap-cds-annotations/abencds_67699033-_anno.md)

- AccessControl Annotations

  - [`AccessControl.authorizationCheck`](../abap-cds-annotations/abencds_1180334353_anno.md)

## Hints

- Alongside the hierarchy annotations shown here, the globally valid [entity annotations](abencds_f1_entity_annotations.md) can also be specified for a CDS hierarchy.

- Regarding `AccessControl.authorizationCheck`, there are some restrictions that are described under [DCL Restrictions for CDS Hierarchies](../abap-cds-access-control/abencds_f1_dcl_hierarchies.md).
