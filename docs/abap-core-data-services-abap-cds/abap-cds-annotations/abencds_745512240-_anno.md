---
title: "Consumption.semanticObjectMapping.additionalBinding.localElement"
source_file: abencds_745512240-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.semanticObjectMapping.additionalBinding.localElement

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)   |
|-------------|----------------------------------------------------------------------|
| **Syntax**  | `Consumption.semanticObjectMapping.additionalBinding[].localElement` |
| **Scope**   | `#ELEMENT`, `#PARAMETER`                                             |
| **Type**    | `ElementRef`                                                         |
| **Enums**   | `-`                                                                  |
| **Default** | `-`                                                                  |
| **Text**    | `-`                                                                  |
| **MDE**     | `X`                                                                  |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`        |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Consumption

Define a specific behavior that relates to the consumption of CDS content through domain-specific frameworks.

### Use Case

Using these annotations, the specific behavior is defined which is related to the consumption of CDS content. This metadata makes no assumptions about the concrete consumption technology/infrastructure, but it is applicable across multiple consumption technologies (e.g. Analytics or OData).

### Note

Annotations belonging to Consumption.filter regulate filtered queries on UIs.

Usually filter values are entered manually by the user on a UI. By using filter annotations, query filters can be influenced.

## semanticObjectMapping

This annotation allows to navigate to other UIs providing a related mapping for the semantic object.

## additionalBinding

No KTD found

## localElement

No KTD found
