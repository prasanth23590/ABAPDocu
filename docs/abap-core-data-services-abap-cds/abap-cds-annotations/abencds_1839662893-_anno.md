---
title: "API.element.releaseState"
source_file: abencds_1839662893-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > API"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# API.element.releaseState

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `API.element.releaseState`                                    |
| **Scope**   | `#ELEMENT`                                                    |
| **Type**    | `String(30)`                                                  |
| **Enums**   | `#DECOMMISSIONED, #DEPRECATED`                                |
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

## releaseState

Defines the deviating release state of an element in a released CDS object. It overrides the release state of the CDS object for individual elements.

## Enums

## \#DEPRECATED

The element is deprecated and thus should no longer be used.

If accessed, the element produces a syntax check warning in restricted ABAP language versions.

Together with this release state, a successor for the deprecated element must be specified using annotation @API.element.successor.

## \#DECOMMISSIONED

The element is decommissioned and thus is no longer available for productive use.

Together with this release state, a successor for the decommissioned element must be specified using annotation @API.element.successor.

## Further Information

### Hint

In the ABAP language versions [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) and [ABAP for Key Users](../../abap-glossary/abenabap_for_key_users_glosry.md), accessing an element forbidden using `@API.element.releaseState:#DEPRECATED` in an ABAP program or CDS entity produces a syntax check warning. An element proposed by `@API.element.successor` should be used instead.
