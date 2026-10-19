---
title: "Semantics.amount.currencyCode"
source_file: abencds_689127610-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Semantics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Semantics.amount.currencyCode

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `Semantics.amount.currencyCode`                               |
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

## amount

Element is defined as a currency field.

## currencyCode

### Short Description

The annotated field contains a monetary amount, and the corresponding currency code is contained in the referenced field.

## Annotation Value

elem_name: Name of an element defined as a currency key.

## Note

In a CDS view entity, the annotation is mandatory for all elements of data type abap.curr and possible for CDS amount fields of other data types. Optional in all other CDS entities.

## Further Information

- `Semantics.amount.currencyCode` must point to an element **in the same view** which contains the currency key. This rule applies to all CDS entities except for CDS DDIC-based views (obsolete). In CDS DDIC-based views, the currency key can also be a field from one of the data sources.

- The annotation `Semantics.currencyCode` declares a field as currency key. In CDS DDIC-based views (obsolete), these currency key fields are automatically and implicitly assigned to all currency fields that have no other assignment. The assignment order is as follows:

  - If there is a direct and local currency key assignment, this assignment is considered.

  - If there is no direct and local assignment, it is checked whether there is any inherited currency key that can be derived from one of the data sources.

  - If there is no inherited or derived currency key, then the local currency key field is assigned automatically and implicitly, even if it is not specified explicitly.

- The API `CL_DD_DDL_ANNOTATION_SERVICE` can derive the annotation `Semantics.amount.currencyCode` from DDIC database tables only if the name of the referred currency key field is not changed in a CDS view entity. If a CDS view entity selecting from a database table uses an alias name for a currency key field, then the annotation cannot be evaluated by this API.
