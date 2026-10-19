---
title: "Consumption.derivation.resultHierarchyNode.nodeTypeElement"
source_file: abencds_2076986893_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.derivation.resultHierarchyNode.nodeTypeElement

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.derivation.resultHierarchyNode.nodeTypeElement`       |
| **Scope**   | `#ELEMENT`, `#PARAMETER`                                           |
| **Type**    | `String(30)`                                                       |
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

## derivation

### Short Description

You can use this annotation and the related derivation annotations to define the specific behavior which is related to the consumption of CDS content using domain-specific frameworks. This metadata makes no assumptions on the concrete consumption technology/infrastructure but is applicable across multiple consumption technologies.

The annotation can be used to derive a default value for a parameter or a filter default value for an element automatically at runtime by selecting one or more rows from a given lookup entity.

The derivation assigns a default value to a parameter if no value has been provided for it by the consumer at runtime (for example, when it is annotated with ‘`@Consumption.hidden`: true’). The derivation will be ignored if a fixed default value is specified for the parameter via ‘`@Consumption.defaultValue`’.

The derivation also adds a default filter for an element if no filter has been provided by the consumer at runtime (for example, when it is annotated with ‘`@Consumption.filter.hidden`: true’). The derivation will be ignored, if a fixed filter default value is specified for the parameter via ‘`@Consumption.filter.defaultValue`’.

An empty derivation of a hidden and mandatory parameter/filter will lead to a runtime error.

## resultHierarchyNode

### Short Description

The resultHierachyNode annotation contains elements of the lookupEntity, which provide the hierarchy nodes. It can only be used in combination with ‘Consumption.filter.selectionType: \#HIERARCHY_NODE’. A hierarchy node is seen as list of elements, which are the semantic elements of the corresponding view with ‘`@ObjectModel.dataCategory`: \#HIERARCHY’.

Mapping describes the mapping of the elements in the hierarchy view and the elements in the lookup entity. NodeTypeElement is the name of the element in the lookup entity which returns the type of the node. The type of the node is the element name (in the hierarchy view) which is filled in a row of the resultset. If the value of field NodeTypeElement in the result of the lookup is initial, the row represents a leaf.

## nodeTypeElement

No KTD found
