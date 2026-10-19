---
title: "OData.applySupportedForAggregation"
source_file: abencds_626623472_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > OData"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# OData.applySupportedForAggregation

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `OData.applySupportedForAggregation`                               |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `String(12)`                                                       |
| **Enums**   | `#FULL, #NONE, #RESTRICTED`                                        |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## OData

Capture OData-related aspects to expose data gained from a CDS entity in an OData service.

### Scope and Definition

Annotation OData

{

`@Scope`:\[#ELEMENT\]

etag : Boolean default true;

`@Scope`:\[#ENTITY\]

entitySet

{

``` abap
   name : String(30);
```

};

entityType

{

``` abap
  name : String(128);
```

};

action: array of {

``` abap
  name      : String(128);

  localName : String(30);
```

};

property

{

``` abap
  name : String(128);
```

};

`@Scope`:\[#SERVICE\]

schema

{

``` abap
  name : String(128);
```

};

## applySupportedForAggregation

## Short Description

The @OData.applySupportedForAggregation annotation specifies the level of analytical capabilities supported in OData V4 services, reflected in the \$metadata. It defines whether full, restricted, or no analytical capabilities are available for aggregation.

## Use Case

This annotation is used in scenarios where CDS views need to fulfill specific criteria for complex OData V4 requests with \$apply. It helps expose the allowed aggregations for each measure in analytical tables, guiding developers to mark entities appropriately based on their aggregation needs.

- `#FULL` is not allowed with unmanaged queries.

- `#RESTRICTED` is not allowed with managed queries.

- `#FULL` and `#RESTRICTED` are not allowed with certain query features like filter derivations, ranked search, and hierarchies.

### Enums

### \#FULL

All V4 analytical capabilities implemented for managed queries are available, including transformations such as CONCAT. These available capabilities are part of \$metadata. This option is exclusively available for managed queries.

### \#RESTRICTED

Only a limited set of ODATA V4 analytical capabilities is available, and the CONCAT transformation is not included. The available capabilities are part of \$metadata. This option can be used for unmanaged queries that implement aggregation features.

### \#NONE

No analytical capabilities are annotated in \$metadata.NONE is the default behavior in case of absence of the applySupportedForAggregation annotation.
