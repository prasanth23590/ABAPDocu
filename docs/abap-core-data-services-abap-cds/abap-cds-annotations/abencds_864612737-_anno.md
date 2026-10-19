---
title: "Semantics.quantity.unitOfMeasureIsoCode"
source_file: abencds_864612737-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Semantics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Semantics.quantity.unitOfMeasureIsoCode

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Semantics.quantity.unitOfMeasureIsoCode`                          |
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

## quantity

Element is defined as a CDS quantity field.

## unitOfMeasureIsoCode

### Short Description

You can use this annotation to expose not only the language-dependent code of a quantity unit, but also the language-independent ISO code of a unit of measure in external APIs. Using this annotation, you can relate a quantity field to the target field of a language-independent `@Semantics.quantity.unitOfMeasure`.

### Constraints

The following constraints must be kept in mind:

- The target field of `@Semantics.quantity.unitOfMeasureISOCode` shall be type by a data element based on ABAP domain ISOCD_UNIT.

- The target field of `@Semantics.quantity.unitOfMeasureISOCode` shall not be annotated with Semantics.unitOfMeasure: true

- In VDM remote API views (prefix 'A\_') all quantity fields shall be annotated with `@Semantics.quantity.unitOfMeasureISOCode`. The corresponding units must be provided in the view.

Note: This constraint will only be activated for existing A-views after a clean-up A-views has taken place.
