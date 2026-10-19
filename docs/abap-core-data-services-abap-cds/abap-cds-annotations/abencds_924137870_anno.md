---
title: "EndUserText.label"
source_file: abencds_924137870_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > EndUserText"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EndUserText.label

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)                                                                                                                     |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `EndUserText.label`                                                                                                                                                    |
| **Scope**   | `#ACCESSPOLICY`, `#ASPECT`, `#ELEMENT`, `#ENTITY`, `#ENTITY_ASPECT`, `#ENUM_VALUE`, `#EXTEND_VIEW`, `#PARAMETER`, `#PFCG_MAPPING`, `#ROLE`, `#SERVICE`, `#SIMPLE_TYPE` |
| **Type**    | `String(60)`                                                                                                                                                           |
| **Enums**   | `-`                                                                                                                                                                    |
| **Default** | `-`                                                                                                                                                                    |
| **Text**    | `X`                                                                                                                                                                    |
| **MDE**     | `X`                                                                                                                                                                    |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                                                                          |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## EndUserText

Translatable texts of CDS objects.

ABAP annotations introduced using EndUserText are used to define translatable semantic texts for a CDS object. The value of such an annotation is saved in special tables that have a language key and are translatable. The value specified in the source code should consist of text in the original language of the CDS source code, and it is translated into the required languages. The methods of the class CL_DD_DDL_ANNOTATION_SERVICE read these texts as specified by an input parameter for the language. If no language is passed to the input parameter, the text environment language is used as the default. If no text is found for the language, the secondary language of the AS ABAP is used.

## label

Translatable short text of the CDS object or element.

## Annotation Value

Character string with a maximum of 60 characters.
