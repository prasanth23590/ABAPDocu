---
title: "OData.hierarchy.recursiveHierarchy.entity.name"
source_file: abencds_253752354-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > OData"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# OData.hierarchy.recursiveHierarchy.entity.name

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `OData.hierarchy.recursiveHierarchy[ ].entity.name`                |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `EntityRef`                                                        |
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

## hierarchy

### Short Description

The parent-child hierarchy can be defined in two ways. The first is a hierarchy based directly on the master data/dimension entity, for example, employees and managers. In this case, the hierarchy is time dependent if the master data entity is as well. The second is a specific hierarchy view. Here, the recursion can be defined on abstract keys and several hierarchies may exist. With abstract keys, the nodes could be different business entities and it is possible that leaves belong to multiple parent nodes. These features are not available when the hierarchy is defined directly in the master data. In this scenario, the relation between the node and parent node can depend on the time independent of the time dependency of the dimension.

The second is a specific hierarchy view. Here, the recursion can be defined on abstract keys and several hierarchies may exist. With abstract keys, the nodes could be different business entities and it is possible that leaves belong to multiple parent nodes. These features are not available when the hierarchy is defined directly in the master data. In this scenario the relation between the node and parent node can depend on the time independent of the time dependency of the dimension.

### Example

An example for a parent-child hierarchy is the “Employee” master data. A “Manager” is an “Employee” and almost every “Employee” is assigned to a “Manager”.

## recursiveHierarchy

### Parent-Child Relationship

- Hierarchy.parentChild.recurse.child: If the underlying view definition does not contain an association defining the parent-child relationship but only “normal” elements, this annotation has to be used to define the children.

Scope: \#VIEW Type: Array of ElementRef. The element names define the key elements of the "child".

Evaluation Runtime (Engine): Analytic manager

- Hierarchy.parentChild.recurse.parent: If the underlying view definition does not contain an association defining the parent-child relationship but only “normal” elements, this annotation has to be used to define the parents.

Scope: \#VIEW

Type: Array of ElementRef. The element names define the key elements of the "parent".

Evaluation Runtime (Engine): Analytic manager

- Hierarchy.parentChild.recurseBy: Defines the parent-child relationship in a hierarchy based on an existing association from hierarchy node to its parent node in the same view.

Scope: \#VIEW

Type: ElementRef. The name of the parent-child association needs to be specified here.

Evaluation Runtime (Engine): Analytic manager

## entity

### Short Description

You can define metadata on entity level.

## name

### Short Description

User-friendly name of the hierarchy. Only relevant if the view defines one hierarchy only, and Hierarchy.parentChild.directory is not used.

Scope: \#VIEW

Type: String - as a description of the hierarchy.

Evaluation Runtime (Engine): Analytic manager: This name can be exposed in input help for Hierarchy.parentChild.name. The hierarchy is exposed if there isn't a directory label defined. See Hierarchy.parentChild.name.
