---
title: "ObjectModel.semanticKey"
source_file: abencds_969786454-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.semanticKey

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.semanticKey[ ]`                                       |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`                                       |
| **Type**    | `ElementRef`                                                       |
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

## semanticKey

### Short Description

Semantic Key fields can be defined using the annotation `@ObjectModel.semanticKey`, which consists of an array of properties from the entity. The given fields will be displayed in bold and the editing status will be displayed.

### More Information

[Handling Semantic Key Fields](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#handling-semantic-key-fields)
