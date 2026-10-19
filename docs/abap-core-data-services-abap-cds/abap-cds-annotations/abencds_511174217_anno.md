---
title: "ObjectModel.filter.enabled"
source_file: abencds_511174217_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.filter.enabled

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.filter.enabled`                                       |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## filter

No KTD found

## enabled

## Evaluation Engine Runtime

SADL

### Short Description

Sets the OData annotation for filterable or non-filterable elements according to the annotation value true or false.

The annotation overrules element default settings regarding filter enablement for the element.

### Use Case

If the annotated CDS view is exposed in an OData service, the non-filterable properties are marked with an OData annotation in the OData metadata. The default of being filterable is not shown in the metadata.
