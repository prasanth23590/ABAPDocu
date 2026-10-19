---
title: "DataIntegration.deltaReplication.ignoredDataSources"
source_file: abencds_1249954665_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > DataIntegration"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DataIntegration.deltaReplication.ignoredDataSources

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `DataIntegration.deltaReplication.ignoredDataSources[]`            |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `String(30)`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## DataIntegration

No KTD found

## deltaReplication

An initial load of data from ABAP CDS views using the SQL Service is possible without any additional settings. The main purpose of the DataIntegration annotation is to notify the system that a CDS view should be enabled for delta replication. The system could determine this information using the CDS view metadata, but accessing metadata such as catalogue services takes a considerable amount of time.

A CDS view can be enabled for delta replication if it is based on a single table, the so-called main table, plus additional tables joined via LEFT OUTER TO ONE JOIN. Inner joins can be used, but only if the set of key fields of the joined table is a subset of the set of key fields of the main table. The key field of the CDS view and the key field of the main table must match.

## ignoredDataSources

Some views join transactional data with customizing data. Both transactional and customizing data are stored in database tables. The annotation DataIntegration.deltaReplication.ignoredDataSources removes the specified tables from delta calculation.

## Constraints

The annotation DataIntegration.deltaReplication.ignoredDataSources can only be used if the annotation DataIntegration.deltaReplication.intended is set to true. The specified tables must be part of the definition of the CDS view or underlying CDS views.

## Example

In the following example, the annotation is used to ignore a customizing table that not relevant for the replication of delta data.

``` abap
@DataIntegration. deltaReplication:

{ intended: true,

  ignoredDataSources: [ 'TCURC' ]

}

@EndUserText.label: 'Carrier with currency ISO code'

define view entity zsb_carrid as select from scarr

  left outer to one join tcurc on tcurc.waers = scarr.currcode

{

  key scarr.carrid as Carrid,

  scarr.carrname as Carrname,

  scarr.currcode as Currcode,

  tcurc.isocd as CurrISOCode,

  scarr.url as Url

}
```
