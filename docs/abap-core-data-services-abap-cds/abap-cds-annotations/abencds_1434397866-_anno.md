---
title: "EnterpriseSearch.navigation.intentBased.semanticObject"
source_file: abencds_1434397866-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.navigation.intentBased.semanticObject

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.navigation.intentBased.semanticObject`           |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(120)`                                                      |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## EnterpriseSearch

`@EnterpriseSearch` annotations add semantics that is needed to use a view entity as a (CDS-based) search model in the Enterprise Search framework.

## navigation

Marks a field to be used for navigation if a field is annotated to be a standard response field.

The type of navigation is specified by the respective subannotation.

## intentBased

**Short Description**

Enable intent-based navigation on field level.

The usage of this CDS annotation is optional. You may define a CDS-based Search Model without this CDS annotation.

**Use Case**

If a view field has been marked as a standard response field and additionally this view field has been enabled for intent-based navigation, the field is treated as a link. In this case, the content of the view field is displayed by default as part of the search result item, and you can navigate further based on the semantic object by clicking the displayed field content.

In addition, the CDS View Entity itself must have a semantic object name. To do this, annotate the CDS View Entity with `@Consumption.semanticObject`. As another prerequisite, via the SAP Fiori Launchpad Designer a catalog with target mappings has to be created. (Intent-based navigation is a concept of SAP Fiori. An intent is a combination of a semantic object and an action.)

If you do not have access to the SAP Fiori Launchpad Designer app, you cannot use intent-based navigation for your CDS-based Search Model. In this case, you should not use the annotation described here.

## semanticObject

Contains the name of the semantic object that is used for intent-based navigation.
