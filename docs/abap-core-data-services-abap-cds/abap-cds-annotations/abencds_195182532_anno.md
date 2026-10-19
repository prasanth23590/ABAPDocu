---
title: "Metadata.layer"
source_file: abencds_195182532_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Metadata"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Metadata.layer

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `Metadata.layer`                                              |
| **Scope**   | `#ANNOTATE`                                                   |
| **Type**    | `Integer`                                                     |
| **Enums**   | `#CORE, #CUSTOMER, #INDUSTRY, #LOCALIZATION, #PARTNER`        |
| **Default** | `-`                                                           |
| **Text**    | `-`                                                           |
| **MDE**     | `X`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Metadata

Defines the handling of metadata of a CDS object.

## layer

Multiple metadata extensions can exist for one CDS type definition. Different metadata extensions can provide different annotation values.

The layer annotation defines the priority of the evaluation of a metadata extension by assigning it to a layer.

## Annotation Values

The enumeration values relate the layer to products or parts/extensions of products.

Values on a higher level overrule values on a lower level.

The \#CUSTOMER layer has the highest priority. The \#CORE layer has the lowest priority.

## Enums

## \#CORE

Relates to the *core* product (ABAP Platform).

## \#LOCALIZATION

Relates to the *localization* of a product (SAP Application Component).

## \#INDUSTRY

Relates to an *industry*-specific extension of a product (SAP Industry Solution)

## \#PARTNER

Relates to a *partner* extension of a product

## \#CUSTOMER

Relates to a *customer* extension of a product
