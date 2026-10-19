---
title: "EnterpriseSearch.nls.valueEnumeration.standard"
source_file: abencds_2086819586-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.nls.valueEnumeration.standard

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.nls.valueEnumeration.standard`                   |
| **Scope**   | `#ELEMENT`                                                         |
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

## nls

### Short Description

This annotation can be used to enable Enterprise Search for Natural Language Search (NLS) based on GenAI technology. The information is needed to generate the required GenAI prompts.

### Use Case

The `@EntepriseSearch.nls` CDS annotations are used to enrich CDS-based Search Models with information that is required for GenAI prompt generation in the context of Natural Language Search.

## valueEnumeration

Indicate that the natural language search should consider an enumeration of values for the annotated field.

The subannotations specify the source of the values.

## standard

Indicate that the enumeration of values is based on the corresponding type of the view field.
