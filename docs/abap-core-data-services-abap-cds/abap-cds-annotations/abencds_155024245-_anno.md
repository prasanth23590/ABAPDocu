---
title: "ObjectModel.text.association"
source_file: abencds_155024245-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.text.association

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.text.association`                                     |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `AssociationRef`                                                   |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## text

No KTD found

## association

## Evaluation Engine

Runtime

### Short Description

Defines the associated view, which provides textual descriptions for the annotated field.

SADL - Enriches the OData entity type of the view with the textual description of the target view applying an automated language filtering. The name of the auto-generated text property will be composed out of the annotated field name and the constant suffix \_Text. This OData property is mapped onto the first text field of the associated target CDS view annotated with `@Semantics.text`:true.

Analytic Manager - Uses the associated view as TEXT view for annotated field.
