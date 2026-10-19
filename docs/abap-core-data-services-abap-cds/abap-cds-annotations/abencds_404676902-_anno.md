---
title: "Semantics.nullValueIndicatorFor"
source_file: abencds_404676902-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Semantics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Semantics.nullValueIndicatorFor

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Semantics.nullValueIndicatorFor`                                  |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `ElementRef`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Semantics

Semantic annotations complement the concept of semantic data types, while semantic data types always introduce specific behavior in the provider/core infrastructure (through dedicated operations or conversion functions).

Semantic annotations allow the standardizing of semantics that only have an impact on the consumption side (such as currency code representation together with the amount).

Evaluation Runtime (Engine): Interpreted by the RAP runtime engine (SADL): Translates CDS annotations into the corresponding OData annotations.

## nullValueIndicatorFor

### Short Description

You can use this annotation when your associated entity (QuickView entity) has a key that is non-UUID and a referential constraint for the association does not get generated automatically. To do so, a property needs to act as a null value indicator for the QuickView property, similar to a value control property.

### More Information

[QuickView with non-UUID key - NullValueIndicator](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#quickview-with-non-uuid-key---nullvalueindicator)
