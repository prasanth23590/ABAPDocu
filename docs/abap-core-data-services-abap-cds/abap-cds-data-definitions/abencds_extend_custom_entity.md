---
title: "CDS DDL - EXTEND CUSTOM ENTITY"
source_file: abencds_extend_custom_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entity Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - EXTEND CUSTOM ENTITY

## Syntax

``` abap
 
EXTEND CUSTOM ENTITY CustomEntity WITH 
  { ElementListExtension }  
```

## Description

Extends an existing [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md) `CustomEntity` using a [CDS custom entity extension](../../abap-glossary/abencds_cus_entity_extend_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). An existing CDS custom entity can have one or more CDS custom entity extensions.

## Prerequisite

As a prerequisite, the extended entity must allow extensions. Extensions are allowed by default or can be explicitly allowed with the annotation [`AbapCatalog.extensibility.extensible`](abencds_f1_entity_annotations.md) with the value `true`. If the value `false` is specified, extensions are not allowed.

**Components of a Custom Entity Extension**

Custom entity extensions can make additions to the original entity, but they cannot modify, overwrite, or delete elements from the original entity. A custom entity extension can specify only features that are possible within custom entities, but with some limitations. The following can be specified in a custom entity extension:

- New elements. These new elements are defined as described in topic [`DEFINE CUSTOM ENTITY`, Element](abencds_f1_custom_element.md). Those elements can have [element annotations](abencds_f1_custom_element_anno.md). New key elements are not possible.

- New associations `_assoc1`, `_assoc2` can be defined in the CDS custom entity extension. The same rules apply that are described in topic [`DEFINE CUSTOM ENTITY`, association](abencds_f1_custom_association.md).

- New [to-child associations](../../abap-glossary/abento_child_association_glosry.md) `_compos1`, `_compos2` can be defined in the CDS custom entity extension under the condition that the composition target is also defined as composition child and has the required to-parent association. The composition target is the extended custom entity, not the extension itself. The same rules apply that are described in topic [`DEFINE CUSTOM ENTITY`, Composition](abencds_f1_custom_composition.md).

- Each appended element must have a unique name.

Elements that are added to a custom entity by an extension change the custom entity signature. The ABAP class that implements the CDS custom entity can access the original and the extension fields.

## Restrictions

- CDS custom entity extensions themselves cannot be extended.

- It is not possible to specify new [input parameters](abencds_f1_custom_parameter_list.md) in a custom entity extension.

- [CDS to-parent associations](../../abap-glossary/abento_parent_association_glosry.md) must not be defined in a custom entity extension.

- No addition `ROOT` can be specified in the statement `EXTEND CUSTOM ENTITY` to transform a regular entity to a [root entity](../../abap-glossary/abenroot_entity_glosry.md).

- An appended element cannot be defined as a `KEY` element.

- In a custom entity extension, [header annotations](abencds_f1_entity_annotations.md) are not supported. That means that no annotations are allowed in front of the statement `EXTEND CUSTOM ENTITY`.

## Hint

As stated above, a custom entity extension changes the custom entity signature of the ABAP class that implements the custom entity. To use the extension elements, the following options exist:

- If the implementing ABAP class selects data from data sources, such as CDS entities or DDIC database tables, these data sources can also be extended. The custom entity extension fields can be passed to the extension fields of the data source with `MOVE-CORRESPONDING`.

- If a customer wants to process the extension fields in the custom entity implementation, this can be enabled via BAdIs provided by the owner of the custom entity.
