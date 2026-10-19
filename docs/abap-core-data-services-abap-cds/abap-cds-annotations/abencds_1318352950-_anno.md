---
title: "API.element.decommissioningPlannedForYearMonth"
source_file: abencds_1318352950-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > API"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# API.element.decommissioningPlannedForYearMonth

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `API.element.decommissioningPlannedForYearMonth`              |
| **Scope**   | `#ELEMENT`                                                    |
| **Type**    | `String(7)`                                                   |
| **Enums**   | `-`                                                           |
| **Default** | `-`                                                           |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## API

Specify

- the usability of an *annotation* in CDS objects defined in a restricted ABAP language version or

- deviating release state settings for an *element* in a released CDS entity in a restricted ABAP language version.

## element

Specify deviating release state settings for an *element* in a released CDS object.

This is required only if the release state of the element deviates from the release state of the CDS object.

## decommissioningPlannedForYearMonth

Defines the earliest point in time when the element release state change from \#DEPRECATED to \#DECOMMISSIONED will take effect for your customers, given as month of a year. This annotation is used in combination with the annotation @API.element.releaseState: \#DEPRECATED to schedule the change to \#DECOMMISSIONED.

## Annotation Value

Month of the year of the planned release state change to \#DECOMMISSIONED in the ISO format YYYY-MM, e.g. 2024-08 for August 2024
