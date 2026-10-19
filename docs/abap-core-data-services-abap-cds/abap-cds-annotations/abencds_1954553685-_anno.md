---
title: "Semantics.currencyCode"
source_file: abencds_1954553685-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Semantics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Semantics.currencyCode

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `Semantics.currencyCode`                                      |
| **Scope**   | `#ELEMENT`                                                    |
| **Type**    | `Boolean`                                                     |
| **Enums**   | `-`                                                           |
| **Default** | `true`                                                        |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Semantics

Semantic annotations complement the concept of semantic data types, while semantic data types always introduce specific behavior in the provider/core infrastructure (through dedicated operations or conversion functions).

Semantic annotations allow the standardizing of semantics that only have an impact on the consumption side (such as currency code representation together with the amount).

Evaluation Runtime (Engine): Interpreted by the RAP runtime engine (SADL): Translates CDS annotations into the corresponding OData annotations.

## currencyCode

### Short Description

Tags a field containing a currency code

This can be either an ISO codeInformation published on non-SAP site or an SAP currency code (data type CUKY).

Scope: \[ELEMENT, PARAMETER\]

### Evaluation Runtime (Engine)

Interpreted by the RAP runtime engine (SADL). Translates CDS annotations into the corresponding OData annotations.
