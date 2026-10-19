---
title: "Consumption.cacheSettings.usage"
source_file: abencds_66994189_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.cacheSettings.usage

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.cacheSettings.usage`                                  |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#CLIENT_CONTROLLED, #MANDATORY, #NOT_ALLOWED`                     |
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

## cacheSettings

### Short Description

The cacheSettings annotation and the subsequent annotations control the usage of the HANA cache. In the context of the Analytical Manger (independent of access via INA or OData), the annotations can be used in a CDS Cube and an Analytical Query view. The annotation from the CDS Cube is inherited to the Analytical Query view, but can be overwritten by the Annotations in the Analytical Query View. "refreshForbidden" can only be used in Cubes and is forbidden on query level.

## usage

## Enums

## \#MANDATORY

The cache can neither be bypassed, nor be refreshed. If a cache is available, it must be used.

### Note

It might occur that in an active/active scenario, the cache only exists on the replica-node, but for technical reasons, the active-node is used. This should be set if not reading from the cache should be avoided as much as possible (performance). The user can't trigger a refresh of the cache.

## \#NOT_ALLOWED

The cache has to be bypassed in order to get current data. This can be set if the query should always show the most recent data for application reasons.

## \#CLIENT_CONTROLLED

In the context of the Analytical Manager used via the INA protocol, standard requests should use the cache (if available). If it is a "refresh" request, the cache will be rebuilt before reading data. This is the default behaviour, if the annotation is not set. In the context of ODATA (SADL and Analytical Manager), The cache usage is specified in the app-descriptor and transferred at runtime through the HTTP-header.
