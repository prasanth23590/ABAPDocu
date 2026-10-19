---
title: "Event.context.position"
source_file: abencds_123886785-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Event"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Event.context.position

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Event.context.position`                                           |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Integer`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Event

No KTD found

## context

No KTD found

## position

## Short Description

This annotation is mandatory in the context of dynamic topics in the Advanced Event Mesh (AEM). It provides the exact position of the context attribute within the dynamic topic string to the Enterprise Event Enablement framework.

## Use Case

- Define the the order of the context attributes in events using integer values. Values must be greater than 0 and Every field must have its own individual value.

## Required Annotations

The following annoations must always be used in combination with this annotation for dynamic topics

- `@event.context.attribute`
