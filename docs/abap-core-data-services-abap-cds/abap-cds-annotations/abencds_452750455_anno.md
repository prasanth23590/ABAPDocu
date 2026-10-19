---
title: "OData.action.localName"
source_file: abencds_452750455_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > OData"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# OData.action.localName

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `OData.action[ ].localName`                                        |
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

## action

## Evaluation Engine

Runtime

### Short Description

Denotes the external name of an action for an arbitrary OData service. The annotation maps the localName to the external OData name.

### localName

Value: String(30)

Denotes the action name for mapping to the OData action name (name).
