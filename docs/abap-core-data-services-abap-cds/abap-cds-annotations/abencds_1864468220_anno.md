---
title: "Consumption.valueHelpDefinition.entity.element"
source_file: abencds_1864468220_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.valueHelpDefinition.entity.element

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.valueHelpDefinition[ ].entity.element`                |
| **Scope**   | `#ELEMENT`, `#PARAMETER`, `#SIMPLE_TYPE`                           |
| **Type**    | `String(40)`                                                       |
| **Enums**   | `-`                                                                |
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

## valueHelpDefinition

### Short Description

You can use this annotation to enable defining value help support in simple types. This improves modeling consistent value help support for equally typed CDS fields and parameters.

## entity

## Evaluation Engine

Runtime

## Use Case

Defines the binding for the value help to the value help providing entity. It requires specification of the entity and the element providing the value help for the annotated element.

### element

Value: elementRef

Definition: Specifies the element in the entity referenced in name that provides the value help for the annotated element.
