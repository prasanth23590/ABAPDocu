---
title: "DataIntegration.dataProduct.transformTo"
source_file: abencds_1620739584-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > DataIntegration"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DataIntegration.dataProduct.transformTo

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)        |
|-------------|---------------------------------------------------------------------------|
| **Syntax**  | `DataIntegration.dataProduct.transformTo`                                 |
| **Scope**   | `#ELEMENT`                                                                |
| **Type**    | `String(30)`                                                              |
| **Enums**   | `#BOOLEAN, #DATE, #DATETIME, #DECIMAL, #STRING, #TIME, #TIMESTAMP, #UUID` |
| **Default** | `-`                                                                       |
| **Text**    | `-`                                                                       |
| **MDE**     | `-`                                                                       |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`             |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## DataIntegration

No KTD found

## dataProduct

This annotation represents some mandatory attributes of the data product ORD definition.

## transformTo

The ABAP Push Replication Service (APRS) describes the metadata of the exposed entities within an SQL service using CSN. When replicating data into Business Data Cloud (BDC) certain semantic transformations are required, e.g. transforming the ABAP types DATS and TIMS into date and time or the handling of sematic Boolean columns. These type transformations can be controlled via annotation this annotation.

## Enums

## \#DATE

Date values are replicated in ISO format (e.g. 2025-11-28 for Nov 28th 2025). This transformation is used automatically for elements of ABAP type DATS and DATN if no annotation `@DataIntegration.dataProduct.transformTo` is specified. Invalid values (e.g. 'TODAY' in a DATS field) are replicated as empty values (aka NULL).

The date transformation can be enabled explicitly by adding annotation `@DataIntegration.dataProduct.transformTo`: \#DATE at element level. In addition to data types DATS and DATN, this is also possible for elements of ABAP types CHAR or NUMC with a length of 8 characters. This transformation can be disabled using annotation `@DataIntegration.dataProduct.transformTo`: \#STRING.

## \#TIME

Time values are replicated in ISO format (e.g. 12:34:56). This transformation is used automatically for elements of ABAP type TIMS and TIMN if no annotation `@DataIntegration.dataProduct.transformTo` is specified. Invalid values are replicated as empty values (aka NULL).

The time transformation can be enabled explicitly by adding annotation `@DataIntegration.dataProduct.transformTo`: \#TIME at element level. In addition to data type TIMS and TIMN, this is also possible for elements of ABAP types CHAR or NUMC with a length of 6 characters. This transformation can be disabled using annotation `@DataIntegration.dataProduct.transformTo`: \#STRING.

## \#BOOLEAN

The ABAP type system does not have a dedicated technical type for true/false values. These values are typically stored in columns of ABAP type CHAR with length one and fixed values 'X' for true and ' ' for false.

The replication transforms these values into Boolean values 'true' and 'false'. All other values are replicated empty, i.e., as NULL values.

Per default this Transformation is enabled for elements based on ABAP data dictionary domains:

- ABAP_BOOLEAN

- BOOLE

- XFELD

- XSDBOOLEAN

## \#UUID

There are different ways to store universal unique identifiers (UUID) in ABAP. These are the standard domains in the ABAP data dictionary:

- SYSUUID Universal Unique Identifier

- SYSUUID_22 - UUID in compressed form (22 character UUENCODEd)

- SYSUUID_C - UUID in character form

- SYSUUID_C22 - UUID in 22 Characters (Usually Base64 Encoded)

- SYSUUID_C26 - UUID in 26 chars (usually Base 32 encoded)

- SYSUUID_C32 - UUID in 32 Characters (Hexadecimal Encoded)

- SYSUUID_C36 - UUID in 36 chars - encoded according to RFC 4122

- SYSUUID_X16 - UUID in 16 Bytes (Raw Format)

During replcation all formats are transformed to 36 lower case characters according to RFC 4122. Example: '00112233-4455-6677-8899-aabbccddeeff'.

Additonally, this annotation value can be used at elements of ABAP type CHAR with length 32 and elements of ABAP type RAW with length 16.

## \#TIMESTAMP

The following two domains are used to store timestamps:

- TZNTSTMPL - UTC time stamp in long form (YYYYMMDDhhmmss,mmmuuun)

- TZNTSTMPS - UTC Time Stamp in Short Form (YYYYMMDDhhmmss)

The replication transforms the values into ISO format.

It is allowed to use annotation `@DataIntegration.dataProduct.transformTo`: \#TIMESTAMP at elements that use one of the above domains and at elements of ABAP type DEC with length 21 with 7 decimals, length 15 with 0 decimals or length 14 with 0 decimals.

## \#STRING

This annotation value is used to turn off default transformations \#BOOLEAN, \#UUID, \#DATE or \#TIME.

## \#DECIMAL

This annotation value turns off the timestamp or datetime formatting. Annotated columns will be replicated as decimal numbers.

## \#DATETIME

The following domain it used to store timestamps without microseconds:

- TZNTSTMPS - UTC Time Stamp in Short Form (YYYYMMDDhhmmss)

The replication transforms the values into ISO format.

It is allowed to use annotation `@DataIntegration.dataProduct.transformTo`: \#TIMESTAMP at elements that use the above domain and at elements of ABAP type DEC with length 15 or 14 and 0 decimal places.
