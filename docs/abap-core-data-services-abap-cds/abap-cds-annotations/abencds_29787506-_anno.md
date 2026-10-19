---
title: "EnterpriseSearch.nls.valueEnumeration.entityBased.textElement"
source_file: abencds_29787506-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.nls.valueEnumeration.entityBased.textElement

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.nls.valueEnumeration.entityBased.textElement`    |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `ElementRef`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
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

## entityBased

Indicates that the enumerated values are derived from a CDS view/view entity or a database table.

The entity must contain fields (elements) for language, enumerated value and text.

The elements for enumerated value and text are specified by **codeElement** and **textElement**.

The element that contains the language is determined automatically:

- CDS views/view entities must have a key field that is annotated with `@Semantics.language`: true.

- In database tables there must be a key field with data type LANG.

## textElement

Specify the field (element) of the entity that contains the corresponding text of the value in the code field.
