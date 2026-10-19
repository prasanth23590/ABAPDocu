---
title: "Consumption.filter.hierarchyBinding.type"
source_file: abencds_1575871936-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.filter.hierarchyBinding.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.filter.hierarchyBinding[ ].type`                      |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(12)`                                                       |
| **Enums**   | `#CONSTANT, #ELEMENT, #PARAMETER, #SYSTEM_FIELD, #USER_INPUT`      |
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

## hierarchyBinding

### Short Description

This annotation determines how the key element is filled.

## type

## Enums

## \#ELEMENT

Name of an element, which has a unique filter. At runtime, the filter value is used for this hierarchy component.

## \#PARAMETER

Parameter name.

## \#CONSTANT

Constant.

## \#USER_INPUT

USER_INPUT is optional. It will be requested at runtime of the analytic query. It can contain a name. USER_INPUT with the same name will be provided with the same user input at runtime. The variable is placed in the list of all values in accordance with Consumption.filter.hierarchyBinding.variableSequence.

## \#SYSTEM_FIELD

System field.
