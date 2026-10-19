---
title: "CDS SDL - service_annot"
source_file: abencds_define_service_annos.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Service Definitions > ABAP CDS - SDL for Service Definitions > CDS SDL - DEFINE SERVICE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS SDL - service_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a service definition annotation in the definition of a [service definition](../../abap-glossary/abencds_service_definition_glosry.md) in front of the statement [`DEFINE SERVICE`](abensrvd_define_service.md).

The character `@` must be placed directly in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#SERVICE`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.extensibility.extensible`](../abap-cds-annotations/abencds_1159849682_anno.md)

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)
