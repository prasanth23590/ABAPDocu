---
title: "Consumption.dbHints"
source_file: abencds_710938603-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Consumption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Consumption.dbHints

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Consumption.dbHints[ ]`                                           |
| **Scope**   | `#VIEW`                                                            |
| **Type**    | `String(1298)`                                                     |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Consumption

Define a specific behavior that relates to the consumption of CDS content through domain-specific frameworks.

### Use Case

Using these annotations, the specific behavior is defined which is related to the consumption of CDS content. This metadata makes no assumptions about the concrete consumption technology/infrastructure, but it is applicable across multiple consumption technologies (e.g. Analytics or OData).

### Note

Annotations belonging to Consumption.filter regulate filtered queries on UIs.

Usually filter values are entered manually by the user on a UI. By using filter annotations, query filters can be influenced.

## dbHints

### Short Description

You can use this annotation to pass DB hints to HANA via select statement to optimize execution plans and hence performance. DB hints may be defined statically by using the annotation `@Consumption.dbHint` or programmatically by ABAP classes specified in `@Consumption.dbHintCalculatedBy`. All hints are expected to be merged and used by the consuming framework when it performs a select on the HANA DB.

### Use Case

Set DB hints if you want to improve performance.

## Further Information

### SAP-internal Hint

- The ABAP class `CL_SADL_GW_CDS_DBHINT` lists the database hints that are allowed as values for this annotation.

- The annotation can have one of the two values:

  - `&PREFER_JOIN_WITH_FDA 1&`

  - `&PREFER_JOIN_WITH_FDA 0&`

    These values are [database hints](../../abap-glossary/abendatabase_hint_glosry.md) of the [database interface](../../abap-glossary/abendatabase_interface_glosry.md). They are for internal use only. They can be used to switch off the [fast data access](../../abap-glossary/abenfast_data_access_glosry.md) (FDA) protocol and this can improve performance. The [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md) evaluates these hints.
