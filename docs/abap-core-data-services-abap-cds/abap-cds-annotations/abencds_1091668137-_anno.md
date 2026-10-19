---
title: "ObjectModel.usageType.dataClass"
source_file: abencds_1091668137-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.usageType.dataClass

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)                      |
|-------------|-------------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.usageType.dataClass`                                       |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`                                            |
| **Type**    | `String(30)`                                                            |
| **Enums**   | `#CUSTOMIZING, #MASTER, #META, #MIXED, #ORGANIZATIONAL, #TRANSACTIONAL` |
| **Default** | `#MIXED`                                                                |
| **Text**    | `-`                                                                     |
| **MDE**     | `-`                                                                     |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`           |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## usageType

Defines properties of the data delivered by CDS object.

## dataClass

## Evaluation Engine

Runtime

### Short Description

To support the decision on cache strategies for higher layers and to enable client-side statement routing using these caches, the data class is used. The different data classes correspond to different life time cycles. The annotation dataClass has the following values:

### Enums

### \#TRANSACTIONAL

The view contains data which is written or changed in high volume transactions (also for background processing). Examples are header and items for Sales Order processing or Financial Postings.

### \#MASTER

Master data is read but not written or changed in high volume transactions (also for background processing). It typically drives the business process decisions when business logic is executed. It is also shown to the user as context information and to enable user decisions when these transactions are executed manually. Examples are material, business partner or account.

### \#ORGANIZATIONAL

The data describes the organizational structure of a company and its business processes. It can be seen as a special type of master data. This data is only written or changed when organization changes are implemented at the customer. Examples are sales unit, distribution channel and cost center.

### \#CUSTOMIZING

The data describes how a concrete business process is executed at the customer. It consists typically of content delivered by SAP enriched and extended by the customer. This data is typically even less common changed. Examples are countries, unit of measures, currency.

### \#META

Meta data specifies how the system is configured or describes the technical structure of entities. Typically this is part of shipped content. Changes are done in fixes or upgrades. Examples are DDIC structures, field control, authorization objects.

### \#MIXED

This option is chosen if the CDS view contains data of multiple data classes.
