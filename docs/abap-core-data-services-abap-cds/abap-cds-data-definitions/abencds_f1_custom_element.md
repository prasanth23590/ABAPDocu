---
title: "CDS DDL - DEFINE CUSTOM ENTITY, element"
source_file: abencds_f1_custom_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY > CDS DDL - DEFINE CUSTOM ENTITY, element_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, element

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
    { [KEY] name      : typing } 
  | {      _assoc     : association } 
  | {      _compos    : composition } 
  | {      _to_parent : to_parent_assoc } ...  
```

[`@element_annot1`](abencds_f1_return_list_annotation.md) · [`@element_annot2`](abencds_f1_return_list_annotation.md) · [`typing`](abencds_typing.md) · [`association`](abencds_f1_custom_association.md) · [`composition`](abencds_f1_custom_composition.md) · [`to_parent_assoc`](abencds_f1_custom_tp_association.md)

### Addition

[1. `... @element_annot`](abencds_f1_custom_element.md#addition-1)

[2. `... KEY`](abencds_f1_custom_element.md#addition-2)

## Overview

### Description

Specifies an element `name` or exposes a CDS association `_assoc`, a to-child association `_compos`, or a CDS-to-parent association `_to_parent` in the [element list](abencds_f1_custom_element_list.md) of a CDS custom entity. At least one element must be defined as a key element.

The element names `name`, `_assoc`, `_compos`, and `_to_parent` must specify a unique name that complies with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md). It is recommended that the name of a CDS association, a CDS to-child association, or a CDS-to-parent association starts with an underscore `_`. The names of the elements are in the same namespace as the parameters of the custom entity. Furthermore, `name` cannot contain any slash (/) characters and cannot be a reserved name in ABAP Dictionary. The reserved names that cannot be used are specified in the DDIC database table `TRESE`.

- An element `name` can optionally be defined as key element using the keyword `KEY` and it must be typed with an elementary data type [`typing`](abencds_typing.md). The typing determines the data type of the corresponding component of the structured data type represented by the CDS custom entity.

- The addition [`association`](abencds_f1_custom_association.md) is used to expose a [CDS association](../../abap-glossary/abencds_association_glosry.md) of the name `_assoc`.

- The addition [`composition`](abencds_f1_custom_composition.md) is used to expose a [to-child association](../../abap-glossary/abento_child_association_glosry.md) with the name `_compos`.

- The addition [`to_parent_assoc`](abencds_f1_custom_tp_association.md) is used to expose a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) with the name `_to_parent`. No component with the name `_assoc`, `_compos`, and `_to_parent` is created in the associated structured data type. Element names are not case-sensitive. The blanks in the semicolon-separated list are ignored and can be omitted.

## Addition 1

`... @element_annot`

### Description

Specifies annotations for an element. The annotations can be specified in front of every element using [`@element_annot`](abencds_f1_absent_list_annotation.md). Element annotations can be used to annotate the elements and CDS associations, CDS to-child associations, and CDS to-parent associations of a CDS custom entity with semantic properties.

## Addition 2

`... KEY`

### Description

`KEY` is used to define the current element as a key element of the current CDS custom entity. Those elements of the [element list](abencds_f1_custom_element_list.md) can be defined as key elements that are placed without gaps at the start of the list. At least the first element **must** be a key element.

**Caution**

The key elements of a CDS entity do not define unique lines in its result with regard to the key. An application or framework accessing a CDS entity must expect duplicate entries for the key fields in the result set. If the lines of a result set should be unique in respect to a set of key elements, it is the task of the application or framework that provides the CDS entity to define them appropriately and to document the view accordingly.
