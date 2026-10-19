---
title: "API.element.successor"
source_file: abencds_1922632877-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > API"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# API.element.successor

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `API.element.successor`                                       |
| **Scope**   | `#ELEMENT`                                                    |
| **Type**    | `ElementRef`                                                  |
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

## successor

Defines the name of the successor element which should be used instead of a deprecated or decommissioned element.

## Annotation Value

Name of an element of the type ElementRef.
