---
title: "Consumption.filter.defaultValue"
source_file: abencds_467685227-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.filter.defaultValue

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.filter.defaultValue`                                  |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(1024)`                                                     |
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

## filter

### Short Description

A filter should be specified before executing a query on the view. Usually filter values are entered manually by the user on a UI (filter popup) to filter on an element of the underlying view. Filters are not explicitly known by the Core CDS Layer, but only by the clients like Datapreview, MDX, Advanced Analysis for Office, BO Explorer or OData. It is the task of the consumption (framework) to convert the user input into the WHERE clause when accessing the data.

### Note

Filters can only be specified for elements within the projection list. For Filters the following metadata can be defined:

## defaultValue

### Short Description

This annotation can be used on action importing parameters to define default values for the action consumption via UI consumption. The specified value in the annotation is then displayed as default value when executing the action on the UI.

It allows to specify a default value for a filter of a view element. This value is either proposed to the user or implicitly set by the consumer (framework) of the view in case the end user doesn’t explicitly specify a different value. This default value is completely transparent for the CDS runtime meaning that the consumer is responsible to explicitly extend the where condition. The result type of the “default expression” must comply with the data type of the associated element.

### More Information

[Default Values](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#list-report---header-area)
