---
title: "ObjectModel.virtualElementCalculatedBy"
source_file: abencds_1555784333_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.virtualElementCalculatedBy

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `ObjectModel.virtualElementCalculatedBy`           |
| **Scope**   | `#ELEMENT`                                         |
| **Type**    | `String(255)`                                      |
| **Enums**   | `-`                                                |
| **Default** | `-`                                                |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## virtualElementCalculatedBy

## Evaluation Engine

Runtime

### Short Description

References the calculation class for the annotated virtual element.

### Use Case

The query framework is left during runtime to retreive the values for the virtual element in the calculation class.

To reference the calculation class, ABAP: must be added to the string reference.
