---
title: "Consumption.cacheSettings.refreshForbidden"
source_file: abencds_1540815607_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.cacheSettings.refreshForbidden

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.cacheSettings.refreshForbidden`                       |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
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

## cacheSettings

### Short Description

The cacheSettings annotation and the subsequent annotations control the usage of the HANA cache. In the context of the Analytical Manger (independent of access via INA or OData), the annotations can be used in a CDS Cube and an Analytical Query view. The annotation from the CDS Cube is inherited to the Analytical Query view, but can be overwritten by the Annotations in the Analytical Query View. "refreshForbidden" can only be used in Cubes and is forbidden on query level.

## refreshForbidden

If this annotation is set to true, the cache can't be refreshed with any request from the user. If the user sends a "refresh-request", data is read from cache without updating the cache and a warning is raised.
