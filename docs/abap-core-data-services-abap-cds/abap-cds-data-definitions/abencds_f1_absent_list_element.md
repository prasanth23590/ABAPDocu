---
title: "CDS DDL - DEFINE ABSTRACT ENTITY, element"
source_file: abencds_f1_absent_list_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities > CDS DDL - DEFINE ABSTRACT ENTITY > CDS DDL - DEFINE ABSTRACT ENTITY, element_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY, element

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
    { [KEY] name       : typing } 
  | {       _assoc     : association } 
  | {       _compos    : composition } 
  | {       _to_parent : to_parent_assoc } ...  
```

[`@element_annot1`](abencds_f1_return_list_annotation.md) · [`@element_annot2`](abencds_f1_return_list_annotation.md) · [`typing`](abencds_typing.md) · [`association`](abencds_f1_absent_association.md) · [`composition`](abencds_absent_composition.md) · [`to_parent_assoc`](abencds_absent_to_parent_assoc.md)

### Addition

[1. `... @element_annot`](abencds_f1_absent_list_element.md#addition-1)

[2. `... KEY`](abencds_f1_absent_list_element.md#addition-2)

## Overview

### Description

Specifies an element `name` or defines a CDS association `_assoc`, a CDS to-child association `_compos`, or a CDS-to-parent association `_to_parent` in the [list of elements](abencds_f1_absent_element_list.md) of a [CDS abstract entity](../../abap-glossary/abenabstract_glosry.md). `name` or `_assoc` or `_compos` and `_to_parent` must be used to specify a unique name that complies with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md). Here, the name of a CDS association, a CDS to-child association, or a CDS-to-parent association can start with an underscore `_`, as recommended. The names of the elements and CDS associations, CDS to-child associations, and CDS-to-parent associations are in the same namespace as the parameters of the abstract entity. Furthermore, `name` cannot contain any slash (/) characters and cannot be a reserved name in ABAP Dictionary. The reserved names that cannot be used are specified in the DDIC database table `TRESE`.

- An element `name` defines an element. Elements must be typed with an elementary data type [`typing`](abencds_typing.md). All possible data types and the rules for typing are described in the topic about [`typing`](abencds_typing.md) in CDS. The typing determines the data type of the corresponding component of the structured data type represented by the CDS abstract entity.

- The addition [`association`](abencds_f1_absent_association.md) is used to expose a [CDS association](../../abap-glossary/abencds_association_glosry.md) of the name `_assoc`.

- The addition [`composition`](abencds_absent_composition.md) is used to expose a CDS to-child association with the name `_compos`.

- The addition [`to_parent_assoc`](abencds_absent_to_parent_assoc.md) is used to expose a CDS-to-parent association with the name `_to_parent`.

- The element list must contain at least one element `name`. It is not allowed to specify only an association, to-child association, or to-parent association in the element list.

No component with the name `_assoc`, `_compos`, and `_to_parent` is created in the associated structured data type.

Element names are not case-sensitive. The blanks in the comma-separated list are ignored and can be omitted.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS abstract entity:

``` abap
@EndUserText.label: 'Abstract CDS Entity'
@Metadata.allowExtensions: false
define abstract entity demo_cds_abstract_entity
  {
    key col1 : abap.char(3);
        col2 : abap.int4;
        col3 : abap.string;
        col4 : DEMO_BT_CHAR_TEXT;
  }
```

The class `CL_DEMO_CDS_ABSTRACT_ENTITY` demonstrates the following:

- The structure of the CDS abstract entity can be evaluated using [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) methods.

- The annotations of the CDS abstract entity can be evaluated using the class `CL_DD_DDL_ANNOTATION_SERVICE`.

- The structure of the CDS abstract entity can be used as a data type in the ABAP program.

## Addition 1

`... @element_annot`

### Description

Specifies annotations for the element. The annotations can be specified in front of every element and every CDS association, CDS to-child association, and CDS-to-parent association using [`@element_annot`](abencds_f1_absent_list_annotation.md).

### Hint

Element annotations can be used to annotate the elements and CDS associations, CDS to-child associations, plus CDS-to-parent associations of a CDS abstract entity with semantic properties.

## Addition 2

`... KEY`

### Description

`KEY` is used to define the current element as a key element of the current [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md). Those elements of the [element list](abencds_f1_return_list.md) can be defined as key elements that are placed without gaps at the start of the list.

### Hint

The key elements of a CDS abstract entity can be used to create an abstract data model.
