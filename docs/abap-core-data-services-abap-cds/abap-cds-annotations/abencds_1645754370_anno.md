---
title: "Consumption.filter.defaultHierarchyNode.node.element"
source_file: abencds_1645754370_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.filter.defaultHierarchyNode.node.element

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.filter.defaultHierarchyNode.node[ ].element`          |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `ElementRef`                                                       |
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

## defaultHierarchyNode

### Short Description

This annotation allows to specify a default value for a hierarchy node filter of a view element.

### Use Case

The default is either proposed to the end user or implicitly set by the consumption framework of the view in case the end user does not explicitly specify a different value. A hierarchy node is seen as a list of elements, which are the semantic elements in the corresponding view with `@ObjectModel.dataCategory`:#HIERARCHY.

### Required Annotations

This annotation must be used in combination with selectionType:#HIERARCHY_NODE

### Related Links

Usage in Scenario: \[Using Aggregation Data in SAP Fiori Apps(https://help.sap.com/viewer/923180ddb98240829d935862025004d6/Cloud/en-US/84f3dc9e036f4feb9eef3470b629d193.html)\]\](https://help.sap.com/viewer/923180ddb98240829d935862025004d6/Cloud/en-US/84f3dc9e036f4feb9eef3470b629d193.html)\]

## node

### Short Description

With node, each part can be set to a constant separately.

## element

References the element in the hierarchy node view.
