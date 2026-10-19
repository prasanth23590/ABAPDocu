---
title: "ObjectModel.collectiveValueHelp.for.element"
source_file: abencds_91716332-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.collectiveValueHelp.for.element

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.collectiveValueHelp.for.element`                      |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `ElementRef`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## collectiveValueHelp

### Short Description

For SAP GUI-based applications you can define a collective search help that combines several elementary search helps. You can choose one of several alternative search paths and retrieve input values from multiple sources/tables in a single dialog. In Fiori UI, this is also possible via a collective value help using an abstract entity comprising a list of assigned elementary search helps and potential mappings of the bound field names.

### Use Case

The collective value help shall be annotated with `@ObjectModel.collectiveValueHelp.for.element` pointing to the field, for which the collective value help is defined.

### More Information

[Collection Value Help](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#collective-value-help)

## for

No KTD found

## element

No KTD found
