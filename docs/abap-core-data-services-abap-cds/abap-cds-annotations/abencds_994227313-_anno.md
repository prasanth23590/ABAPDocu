---
title: "DataIntegration.deltaReplication.intended"
source_file: abencds_994227313-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > DataIntegration"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DataIntegration.deltaReplication.intended

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `DataIntegration.deltaReplication.intended`                        |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
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

## intended

The annotation DataIntegration.deltaReplication.intended enables delta replication of CDS views by means of SQL Service Definitions and SQL Service Bindings.

## Constraints

The annotation DataIntegration.deltaReplication.intended describes only the intention of the author of the CDS view. You need to ensure that the CDS view is suitable for delta replication.

Delta replication is supported if the CDS view selects data from one table and from additional fields of tables which are added using LEFT OUTER TO ONE JOIN or equivalent joins. The key of the CDS view must be identical to the key of the main table, thus fields may be renamed.

Delta replication is not supported if the CDS view contains the following features:

- UNION

- GROUP BY

- ABAP Managed Database Procedures (AMDP)

- Joins with non-key fields in the right part of the ON condition

- INNER JOIN if the join cannot be interpreted as composition relation. If a key field of an INNER JOIN connects to a non-key field on the other side, then this is not a composition anymore.

- Complex WHERE conditions, because WHERE conditions typically convert a LEFT OUTER JOIN to an INNER JOIN. Examples for complex WHERE conditions are:

  - Two atomic conditions on different columns combined with OR

  - Two atomic conditions on the same column combined with AND

  - IS NULL and LIKE predicates

  - ...

- CDS views that cannot be enabled for delta replications in the FROM clause (view on view)

- CDS view having more than 16 key fields

If a view has the annotation `@DataIntegration.deltaReplication.intended`: true but delta replication cannot be supported, then delta replication is automatically disabled. Warning messages are shown in the problems view of ABAP Development Tools (ADT). These warnings are shown as error messages in the Service Definition and activation of the Service Definition is not possible.

## Examples

## Single Table

The following is an example of a simple CDS view based on one table.

``` abap
@DataIntegration.deltaReplication.intended: true

@EndUserText.label: 'Carrier'

define view entity zsb_carrid as select from scarr

{

  key carrid as Carrid,

  carrname as Carrname,

  currcode as Currcode,

  url as Url

}
```

## INNER JOIN between header and item table

The following example outlines source code of a CDS view that is based on two tables that use the annotation. As a foreign key relationship exists between tables SCARR and SPFLI, the INNER JOIN will be accepted.

``` abap
@DataIntegration.deltaReplication.intended: true

@EndUserText.label: 'Connections'

define view entity zsb_ConnID as select from spfli as co

inner join scarr as ca on ca.carrid = co.carrid

{

  key co.carrid as Carrid,

  key co.connid as Connid,

  ca.carrname as Carrname,

  ca.currcode as Currcode,

  co.countryfr as Countryfr,

  co.cityfrom as Cityfrom,

  co.airpfrom as Airpfrom,

  co.countryto as Countryto,

  co.cityto as Cityto,

  co.airpto as Airpto,

  co.fltime as Fltime,

  co.deptime as Deptime,

  co.arrtime as Arrtime,

  co.distance as Distance,

  co.distid as Distid,

  co.fltype as Fltype,

  co.period as Period

}
```
