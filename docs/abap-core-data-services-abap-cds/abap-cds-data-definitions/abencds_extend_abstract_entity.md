---
title: "CDS DDL - EXTEND ABSTRACT ENTITY"
source_file: abencds_extend_abstract_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entity Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - EXTEND ABSTRACT ENTITY

## Syntax

``` abap
 
EXTEND ABSTRACT ENTITY cds_abstract_entity 
       WITH 
            { element_list_extension }  
```

## Description

Extends an existing [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) `cds_abstract_entity` using a [CDS abstract entity extension](../../abap-glossary/abencds_abs_entity_extend_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). An existing CDS abstract entity can have one or more CDS abstract entity extensions.

## Prerequisite

As a prerequisite for the extension of the CDS abstract entity with the statement `EXTEND ABSTRACT ENTITY`, the base entity must allow extensions. Extensions are allowed per default or can be explicitly allowed with the annotation [`AbapCatalog.extensibility.extensible`](abencds_f1_entity_annotations.md) with the value `true`. If the value `false` is specified, extensions are not allowed.

**Components of an Abstract Entity Extension**

Abstract entity extensions can make additions to the original entity, but they cannot modify, overwrite, or delete elements from the original entity. An abstract entity extension can specify only features that are possible within abstract entities, but with some limitations. The following can be specified in an abstract entity extension:

- New elements. These new elements are defined as described in topic [`DEFINE ABSTRACT ENTITY`, element](abencds_f1_absent_list_element.md). Those elements can have [element annotations](abencds_f1_absent_list_annotation.md). New key elements are not possible.

- New associations `_assoc1`, `_assoc2` can be defined in the CDS abstract entity extension. The same rules apply that are described in topic [`DEFINE ABSTRACT ENTITY`, association](abencds_f1_absent_association.md).

  **Note:** It is **not** allowed to define new [CDS to-parent associations](../../abap-glossary/abento_parent_association_glosry.md) in an abstract entity extension. New [to-child associations](../../abap-glossary/abento_child_association_glosry.md) are allowed under the condition that the composition target is also defined as composition child and has the required to-parent association. The composition target is the extended abstract entity, not the extension itself.

- Each appended element must have a unique name.

## Restrictions

- CDS abstract entity extensions themselves cannot be extended.

- It is not possible to specify new [input parameters](abencds_f1_entity_parameter_list.md) in an abstract entity extension.

- No addition `ROOT` can be specified in the statement `EXTEND ABSTRACT ENTITY` to transform a regular entity to a [root entity](../../abap-glossary/abenroot_entity_glosry.md).

- An appended element cannot be defined as a `KEY` element.

- In an abstract entity extension, [header annotations](abencds_f1_entity_annotations.md) are not supported. That means that no annotations are allowed in front of the statement `EXTEND ABSTRACT ENTITY`.
