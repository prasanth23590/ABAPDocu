---
title: "OData.entitySet.name"
source_file: abencds_814310721-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > OData"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# OData.entitySet.name

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `OData.entitySet.name`                                             |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `String(30)`                                                       |
| **Enums**   | `-`                                                                |
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

## entitySet

## Evaluation Engine

Runtime

### Short Description

Denotes the external name of the entity set for an arbitrary OData service.This annotation can't be used for services exposed with SEGW.

### name

Value: String (30)

#### Note

You can also define the name of the entity set in the service definition by using an alias: expose /DMO/C_Travel_U as Travel. The name of the alias in the service definition will be used even if you use the annotation in the CDS view.
