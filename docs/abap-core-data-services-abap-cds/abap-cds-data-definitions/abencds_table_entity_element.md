---
title: "CDS DDL - CDS Table Entity, element"
source_file: abencds_table_entity_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities > CDS DDL - DEFINE TABLE ENTITY > CDS DDL - CDS Table Entity, element_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Table Entity, element

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
    { [KEY] name      : typing [NULL]; } 
  | {      _assoc     : association; } 
  | {      _compos    : composition; } 
  | {      _to_parent : association to parent; }  
```

[`@element_annot1`](abencds_element_annotations_v2.md) · [`@element_annot2`](abencds_element_annotations_v2.md) · [`typing`](abencds_typing.md) · [`association`](abencds_table_entity_assoc.md) · [`composition`](abencds_table_entity_compos.md) · [`association to parent`](abencds_table_entity_to_parent.md)

### Addition

[1. `... @element_annot ...`](abencds_table_entity_element.md#addition-1)

[2. `... KEY`](abencds_table_entity_element.md#addition-2)

[3. `... NULL`](abencds_table_entity_element.md#addition-3)

## Overview

### Description

Defines an element of a [`element list`](abencds_table_entity_element_list.md) of a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md). The following elements are possible:

- [`@element_annot1`](abencds_f1_element_annotation.md), [`@element_annot2`](abencds_f1_element_annotation.md), ... define annotations for an element or an association of a table entity. All element annotations described in the topic [CDS DDL - `element_annot`](abencds_f1_element_annotation.md) can be used.

- `name`: Defines a single field in the element list of a table entity. A field can optionally be defined as key element using the keyword `KEY` and it must be typed with an elementary data type or an enumerated type as described in the topic [`typing`](abencds_typing.md). The optional addition `NULL` is available to define that a column may contain null values.

  Note that the addition `NULL` is not available for key fields.

- The addition [`association`](abencds_table_entity_assoc.md) is used to define and expose a [CDS association](../../abap-glossary/abencds_association_glosry.md) of the name `_assoc`.

- The addition [`composition`](abencds_table_entity_compos.md) is used to define and expose a [to-child association](../../abap-glossary/abento_child_association_glosry.md) with the name `_compos`.

- The addition [`association to parent`](abencds_table_entity_to_parent.md) is used to define and expose a [to-parent association](../../abap-glossary/abento_parent_association_glosry.md) with the name `_to_parent`.

No component with the name `_assoc`, `_compos`, and `_to_parent` is created in the associated structured data type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code shows the different options for typing for a CDS table entity:

- The fields `KEY_ELEMENT` and `COL1` are typed using [CDS built-in types](../../abap-glossary/abencds_built_in_type_glosry.md).

- The field `COL2` is typed using a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md).

- The field `COL3` is typed using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md).

- The field `COL4` is typed using a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md).

``` abap
@ClientHandling.type: #CLIENT_INDEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS table entity, client independent'
define table entity DEMO_CDS_TE_CLIENT_IND
{
  key key_element : abap.char(1);

      @EndUserText.label: 'This field is nullable'
      col1        : abap.char(3) null;
      
      @EndUserText.label: 'This field uses a CDS simple type'
      col2        : demo_simple_type;

      @EndUserText.label: 'This field uses a data element'
      col3        : demo_bt_inheritance;

      @EndUserText.label: 'This field uses a CDS enum type'
      col4        : DEMO_CDS_ENUM_WEEKDAY;

      _assoc      : association of many to many DEMO_CDS_TE_ASSOC 
      on $projection.key_element = _assoc.col3;

}
```

## Addition 1

`... @element_annot ...`

### Description

Specifies annotations for the element. The annotations must be specified before the element using ` @element_annot`. All possible element annotations are listed in topic [element annotations](abencds_f1_element_annotation.md).

## Addition 2

`... KEY`

### Description

The keyword `KEY` is used to define the current element as a [key field](../../abap-glossary/abenkey_field_glosry.md) of the current CDS table entity. All key elements must be placed without gaps at the start of the `element` list. The fields flagged as key fields become the [primary key](../../abap-glossary/abenprimary_key_glosry.md) of the table entity. If a table entity is defined as client-dependent, the client field is implicitly added to the primary key as its first field.

A table entity without any to-child or to-parent association can be defined without any key fields. A table entity without a primary key has limitations during write access using ABAP SQL.

If the table entity defines any to-child or to-parent association, then it must contain at least one key field at the start of the element list.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS table entity `DEMO_CDS_TE_NOKEY` does not define a primary key.

``` abap
@ClientHandling.type: #CLIENT_DEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS table entity without key fields'
define table entity DEMO_CDS_TE_NOKEY
{
  col1 : abap.int4;
  col2 : abap.char(2);
  col3 : abap.int4;

}
```

Therefore, multiple identical data records can be inserted using ABAP SQL `INSERT`.

``` abap
DELETE FROM demo_cds_te_nokey. 
INSERT demo_cds_te_nokey FROM TABLE @( VALUE #( 
   ( col1 = 1 col2 = 'A' col3 = 1 ) 
   ( col1 = 1 col2 = 'A' col3 = 1 ) 
   ( col1 = 1 col2 = 'A' col3 = 1 ) ) ). 
 
SELECT * FROM demo_cds_te_nokey INTO TABLE @FINAL(result).
```

## Addition 3

`... NULL`

### Description

Defines that a column may contain [null values](../../abap-glossary/abennull_value_glosry.md). A null value on the database is an undefined value.

Per default, the fields of a table entity are created as `NOT NULL` on the database. For example, `field : abap.int4` is created on the SAP HANA database as

`"FIELD" INTEGER DEFAULT 0 NOT NULL`

For fields that are not nullable, the type-specific default value is inserted implicitly.

Fields with the data type `abap.string` and `abap.rawstring` must be defined as `NULL`, as they do not have any default value on the SAP HANA database.

## Restriction

Key fields defined using the keyword `KEY` cannot be defined as `NULL`.
