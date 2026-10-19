---
title: "Consumption.valueHelpDefault.fetchValues"
source_file: abencds_884538153-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.valueHelpDefault.fetchValues

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.valueHelpDefault.fetchValues`                         |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `String(30)`                                                       |
| **Enums**   | `#AUTOMATICALLY_WHEN_DISPLAYED, #ON_EXPLICIT_REQUEST`              |
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

## valueHelpDefault

This annotation can be used on action importing parameters to define default values for the action consumption via UI consumption. The specified value in the annotation is then displayed as default value when executing the action on the UI.

## fetchValues

### Short Description

This annotation defines whether the values of the value help provider view are automatically retrieved without setting a filter when invoking the value help, or whether they must be explicitly requested.

The annotation must be used in the value help provider entity.

## Enums

## \#AUTOMATICALLY_WHEN_DISPLAYED

(default in OData V4)

## \#ON_EXPLICIT_REQUEST

(default in OData V2)
