---
title: "Consumption.dynamicLabel.binding.format"
source_file: abencds_1540292092-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.dynamicLabel.binding.format

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.dynamicLabel.binding[ ].format`                       |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#KEY, #KEY_CONCATENATED, #KEY_INTERNAL, #TEXT`                    |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Consumption

Define a specific behavior that relates to the consumption of CDS content through domain-specific frameworks.

### Use Case

Using these annotations, the specific behavior is defined which is related to the consumption of CDS content. This metadata makes no assumptions about the concrete consumption technology/infrastructure, but it is applicable across multiple consumption technologies (e.g. Analytics or OData).

### Note

Annotations belonging to Consumption.filter regulate filtered queries on UIs.

Usually filter values are entered manually by the user on a UI. By using filter annotations, query filters can be influenced.

## dynamicLabel

### Short Description

You can use this annotation instead of the `@EndUserText.label` annotation if the label contains variables which are only available at runtime. The label might contain placeholders which can be bound to parameters. At runtime, the placeholders will be replaces with the value of bound parameter.

## binding

No KTD found

## format

Defines the format which should be used for replacing the placeholder.

## Enums

## \#KEY

Non concatenated value in external format (e.g. 03.2023 (German formatting) for month) (this is the default, if format is not specified)

## \#KEY_CONCATENATED

Concatenated value in external format (e.g. 1000/4711 for costcenter 4711 which depends on controlling area 1000).

## \#KEY_INTERNAL

ABAP format (e.g. 202303 for month 03.2023). This is useful if binding.offset and -length should be used.

## \#TEXT

Shortest available text (e.g. Mar 2023 for month 03.2023)
