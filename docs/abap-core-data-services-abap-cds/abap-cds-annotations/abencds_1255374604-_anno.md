---
title: "ObjectModel.usageType.serviceQuality"
source_file: abencds_1255374604-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.usageType.serviceQuality

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `ObjectModel.usageType.serviceQuality`                        |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`                                  |
| **Type**    | `String(30)`                                                  |
| **Enums**   | `#A, #B, #C, #D, #P, #X`                                      |
| **Default** | `#X`                                                          |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## usageType

Defines properties of the data delivered by CDS object.

## serviceQuality

## Evaluation Engine

Runtime

### Short Description

Specifies the quality of the service with respect to the performance that can be expected by the consumer of the CDS view entity.

A CDS object can be assigned to one quality category, specified by an Enum value.

If the annotation is not specified, the value \#X is used.

### Use Case

There are 6 levels of service quality: 'A', 'B', 'C' and 'D' corresponding to decreasing KPIs. 'A' has the highest requirements and 'D' the lowest. There is one additional level 'X' where no KPIs are specified. This level is used as the default. serviceQuality 'P' is reserved for views that are used to structure the view hierarchy and that don't have any consumer outside of the hierarchy.

### Enums

### \#A

The CDS object can be used for high volume transactions or for background transactions.

### \#B

The CDS object can be used for transactions or for background transactions.

### \#C

The CDS object can be used to query individual objects in transactions.

### \#D

The CDS object can be used for analytical queries.

### \#X

The CDS object is designed for special application cases, such as data migration.

### \#P

The CDS object is used to structure hierarchies of CDS entities and must not be used outside of such a hierarchy.

### Further Information

- Generally, a CDS object in an application should not access more than 100 DDIC database tables and should have a quality category between A and D.

- With the above subannotations of `ObjectModel` it can be documented for a object for which kind of application it is intended and which kind of data are to expected. This information is especially important in regards of performance that can be expected by the consumer of the object. For the quality categories annotated with `ObjectModel.usageType.serviceQuality`, the following rules apply:

  - A CDS object with the quality category A should access no more than three DDIC database tables, must not call any functions, must not aggregate a large number of table rows for direct access, and must not access DDIC database tables with mixed data categories. If the underlying tables are buffered, the CDS object should be buffered too. The runtime for reading a single line with a fully specified key must be less than 1 ms for selecting fields from a field list or 2 ms for selecting all fields with `*`.

  - A CDS object with the quality category B should access no more than five DDIC database tables, must not call any functions, must not aggregate a large number of table rows for direct access, and must not access DDIC database tables with mixed data categories. If the underlying tables are buffered, the CDS object should be buffered too. The runtime for reading a single line with a fully specified key must be less than 2 ms for fields from a field list or 5 ms for selecting all fields with `*`.

  - A CDS object with the quality category C should access no more than 15 DDIC database tables, must not aggregate a large number of table rows for direct access, and must not access DDIC database tables with mixed data categories. The runtime for reading a single line with a fully specified key must be less than 10 ms for fields from a field list or 20 ms for selecting all fields with `*`.

  - A CDS object with the quality category D should access no more than 100 DDIC database tables. The performance should be checked and monitored with realistic data by a test framework.

  - A CDS object with the quality category X can access more than 100 database tables. The performance must be checked and monitored with realistic data by a test framework.

  - A CDS object with the quality category P is not intended for usage in business applications. Performance checks by a test framework are not required.

  - For all quality categories, the subannotations `sizeCategory` and `dataClass` should be specified. Only for quality category P, they do not need to be specified.

    These rules can be checked in the [ABAP Test Cockpit (ATC)](../../abap-glossary/abenatc_glosry.md) by tests delivered by SAP.
