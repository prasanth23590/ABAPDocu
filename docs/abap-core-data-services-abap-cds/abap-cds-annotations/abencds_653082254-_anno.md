---
title: "Semantics.quantity.unitOfMeasure"
source_file: abencds_653082254-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Semantics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Semantics.quantity.unitOfMeasure

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `Semantics.quantity.unitOfMeasure`                            |
| **Scope**   | `#ELEMENT`                                                    |
| **Type**    | `ElementRef`                                                  |
| **Enums**   | `-`                                                           |
| **Default** | `-`                                                           |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Semantics

Semantic annotations complement the concept of semantic data types, while semantic data types always introduce specific behavior in the provider/core infrastructure (through dedicated operations or conversion functions).

Semantic annotations allow the standardizing of semantics that only have an impact on the consumption side (such as currency code representation together with the amount).

Evaluation Runtime (Engine): Interpreted by the RAP runtime engine (SADL): Translates CDS annotations into the corresponding OData annotations.

## quantity

Element is defined as a CDS quantity field.

## unitOfMeasure

### Short Description

Tags an element that contains a measured quantity.

Scope: \[ELEMENT, PARAMETER\]

### Evaluation Runtime (Engine)

Interpreted by the RAP runtime engine (SADL). Translates CDS annotations into the corresponding OData annotations.Unit of measurement key for a CDS quantity field.

In CDS view entities, this annotation can also be used to assign a calculated unit to a CDS calculated quantity.

### Value

elem_name: Name of an element defined as an unit of measurement key that references a unit of measure related to a measured quantity.

### Note

In a CDS view entity, mandatory for all elements of data type abap.quan and for all calculated quantities. Possible for CDS quantity fields of other data types. Optional in all other CDS entities.

## Further Information

- `Semantics.quantity.unitOfMeasure` must point to an element **in the same view** which contains the unit key. This rule applies to all CDS entities except for CDS DDIC-based views (obsolete). In CDS DDIC-based views, the unit key can also be a field from one of the data sources.

- The annotation `Semantics.unitOfMeasure` declares a field as a unit key. In CDS DDIC-based views (obsolete), these unit key fields are automatically and implicitly assigned to all unit fields that have no other assignment. The assignment order is as follows:

  - If there is a direct and local unit key assignment, this assignment is considered.

  - If there is no direct and local assignment, it is checked whether there is any inherited unit key that can be derived from one of the data sources.

  - If there is no inherited or derived unit key, then the local unit key field is assigned automatically and implicitly, even if it is not specified explicitly.

- The API `CL_DD_DDL_ANNOTATION_SERVICE` can derive the annotation `Semantics.quantity.unitofMeasure` from DDIC database tables only if the name of the referred unit key field is not changed in a CDS view entity. If a CDS view entity selecting from a database table uses an alias name for a unit key field, then the annotation cannot be evaluated by this API.
