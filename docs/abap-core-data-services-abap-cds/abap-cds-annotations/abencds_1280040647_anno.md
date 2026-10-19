---
title: "EnterpriseSearch.model"
source_file: abencds_1280040647_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.model

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.model`                                           |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## EnterpriseSearch

`@EnterpriseSearch` annotations add semantics that is needed to use a view entity as a (CDS-based) search model in the Enterprise Search framework.

## model

**Short Description**

Indicate that the CDS View Entity represents a CDS-based Search Model.

For defining CDS-based Search Models, this CDS annotation is mandatory.

**Use Case**

If you choose this CDS annotation, a new Search Connector is automatically created or an existing one updated when the CDS View Entity is activated in the ABAP Developer Tools (ADT).

You can use this CDS annotation with the values true and false:

- true: The system creates an active Search Connector (or updates an existing one). This Search Connector becomes/remains available for search, but can be deactivated at any time.

- false: The system creates an inactive Search Connector (or updates an existing one). This Search Connector is not available for search, but can be activated at any time.
