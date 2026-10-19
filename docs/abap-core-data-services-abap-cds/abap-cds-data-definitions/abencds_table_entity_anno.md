---
title: "CDS DDL - CDS Table Entity, table_entity_annot"
source_file: abencds_table_entity_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities > CDS DDL - DEFINE TABLE ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Table Entity, table_entity_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a table entity annotation in the definition of a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md) in front of the statement [`DEFINE TABLE ENTITY`](abencds_define_table_entity.md).

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.amdp.allowedForWrite`](../abap-cds-annotations/abencds_368297892_anno.md)

  - [`AbapCatalog.deliveryClass`](../abap-cds-annotations/abencds_61840010-_anno.md)

  - [`AbapCatalog.entityBuffer.definitionAllowed`](../abap-cds-annotations/abencds_2036691489-_anno.md)

- AccessControl Annotations

  - [`AccessControl.authorizationCheck`](../abap-cds-annotations/abencds_1180334353_anno.md)

- ClientHandling Annotations

  - [`ClientHandling.type`](../abap-cds-annotations/abencds_613831553_anno.md)

## Hints

- Alongside the function annotations shown here, the globally valid [entity annotations](abencds_f1_entity_annotations.md) can also be specified for a table entity.

- The annotations `AccessControl` and `ObjectModel` have further [framework-specific subannotations](../abap-cds-annotations/abencds_annotations_frmwrk.md).

- Special rules for [Client Handling in CDS Table Entities](abencds_table_entity_client.md):

  - For the annotation `ClientHandling.type` only the enumeration values `#CLIENT_DEPENDENT` and `#CLIENT_INDEPENDENT` can be specified in table entity definitions. Especially, `#INHERITED` cannot be used.
