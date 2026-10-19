---
title: "ObjectModel.supportedCapabilities"
source_file: abencds_684104273-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.supportedCapabilities

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.supportedCapabilities[ ]`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Scope**   | `#ENTITY`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Type**    | `String(60)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Enums**   | `#ANALYTICAL_DIMENSION, #ANALYTICAL_DOCUMENT_STORE, #ANALYTICAL_KPI,#ANALYTICAL_PARENT_CHILD_HIERARCHY_NODE, #ANALYTICAL_PROVIDER, #ANALYTICAL_QUERY, #CDS_MODELING_ASSOCIATION_TARGET, #CDS_MODELING_DATA_SOURCE, #COLLECTIVE_VALUE_HELP, #DATA_STRUCTURE, #DERIVATION_FUNCTION, #ENTERPRISE_SEARCH_PROVIDER, #EXTERNAL_DATA_PROVIDER, #EXTRACTION_DATA_SOURCE, #KEY_USER_COPYING_TEMPLATE, #LANGUAGE_DEPENDENT_TEXT, #ODM_COMPLIANT_PROVIDER, #OUTPUT_EMAIL_DATA_PROVIDER, #OUTPUT_FORM_DATA_PROVIDER, #OUTPUT_PARAMETER_DETERMINATION_DATA_SOURCE, #PARENT_CHILD_HIERARCHY_NODE_PROVIDER, #SEARCHABLE_ENTITY, #SITUATION_ANCHOR, #SITUATION_DATACONTEXT, #SITUATION_TRIGGER, #SQL_DATA_SOURCE, #TRANSACTIONAL_PROVIDER, #UI_PROVIDER_PROJECTION_SOURCE, #UNIT_CONVERION_RATE, #VALUE_HELP_PROVIDER` |
| **Default** | `-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Text**    | `-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **MDE**     | `-`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## supportedCapabilities

### Short Description

This annotations indicates whether or not the UI use case is supported. If supported, then either the creation of UI projections or alternatively the direct consumption in an UI service binding is possible. Otherwise, warnings or errors occur indicating that the UI usage is not supported and might lead to unexpected errors.

### Note

- A secondary object handler must check the suitability of the CDS entity for usage in UI services and will add according messages to the activation log. The list of checks must be aligned.

- As the secondary object handler cannot block the activation, an ATC check is required.

### More Information

[Business Objects](https://help.sap.com/docs/abap-cloud/abap-rap/business-object?version=sap_btp&q=Business%20Object)

[Consume](https://help.sap.com/docs/abap-cloud/abap-rap/consume?version=sap_btp&q=Business%2520Object)

[RAP Extensions](https://help.sap.com/docs/abap-cloud/abap-rap/rap-extensions?version=sap_btp&q=Release)

### Supported Capabilities:

## Enums

## \#SQL_DATA_SOURCE

## \#CDS_MODELING_DATA_SOURCE

## \#CDS_MODELING_ASSOCIATION_TARGET

## \#DATA_STRUCTURE

## \#LANGUAGE_DEPENDENT_TEXT

## \#UNIT_CONVERION_RATE

## \#VALUE_HELP_PROVIDER

## \#COLLECTIVE_VALUE_HELP

## \#EXTRACTION_DATA_SOURCE

## \#DERIVATION_FUNCTION

## \#PARENT_CHILD_HIERARCHY_NODE_PROVIDER

## \#SEARCHABLE_ENTITY

## \#ENTERPRISE_SEARCH_PROVIDER

## \#TRANSACTIONAL_PROVIDER

## \#ANALYTICAL_QUERY

## \#ANALYTICAL_DOCUMENT_STORE

## \#ANALYTICAL_DIMENSION

## \#ANALYTICAL_PROVIDER

## \#ANALYTICAL_PARENT_CHILD_HIERARCHY_NODE

## \#ANALYTICAL_KPI

## \#OUTPUT_FORM_DATA_PROVIDER

## \#OUTPUT_EMAIL_DATA_PROVIDER

## \#OUTPUT_PARAMETER_DETERMINATION_DATA_SOURCE

## \#SITUATION_ANCHOR

## \#SITUATION_TRIGGER

## \#SITUATION_DATACONTEXT

## \#UI_PROVIDER_PROJECTION_SOURCE

## \#KEY_USER_COPYING_TEMPLATE

## \#EXTERNAL_DATA_PROVIDER

## \#ODM_COMPLIANT_PROVIDER
