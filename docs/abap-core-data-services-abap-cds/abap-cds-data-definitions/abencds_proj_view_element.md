---
title: "CDS DDL - proj_element, Transactional Query"
source_file: abencds_proj_view_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - proj_element, Transactional Query

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
    {[KEY]    {proj_element      [AS alias]} 
            | {expose_assoc      [AS alias]} 
            | {path_expr.element [AS alias][: LOCALIZED]} 
            | {cast_expr          AS alias}} 
   |{[VIRTUAL  elem_name : typing]}  
```

[`@element_annot1`](abencds_element_annotations_v2.md) · [`@element_annot2`](abencds_element_annotations_v2.md) · [`expose_assoc`](abencds_proj_view_expose_assoc.md) · [`path_expr`](abencds_proj_view_path_expr.md) · [`LOCALIZED`](abencds_localized.md) · [`cast_expr`](abencds_cast_expression_v2.md) · [`typing`](abencds_typing.md)

### Addition

[1. `... KEY`](abencds_proj_view_element.md#addition-1)

[2. `... AS alias`](abencds_proj_view_element.md#addition-2)

[3. `... LOCALIZED`](abencds_proj_view_element.md#addition-3)

[4. `... VIRTUAL`](abencds_proj_view_element.md#addition-4)

## Overview

### Description

Defines which elements of the projected entity are part of the CDS projection view. Only elements from the projected entity can be specified as projected element.

- The rules for [propagation of element annotations in CDS projection views](abencds_element_annotations_pv.md) apply.

- `proj_element` exposes an element from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). `AS` can be used to define an alternative element name `alias`.

  **Note:** In transactional projection views, an element from the projected entity can be exposed multiple times with different alias names.

- [`expose_assoc`](abencds_proj_view_expose_assoc.md) exposes a [CDS association](../../abap-glossary/abencds_association_glosry.md), a [to-child association](../../abap-glossary/abento_child_association_glosry.md), or a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). Exposed associations can be redirected to a new target when the [association target](../../abap-glossary/abenassociation_target_glosry.md) is also projected. The keyword `REDIRECTED TO` is introduced in topic [CDS DDL - `CDS Projection View, expose_assoc`](abencds_proj_view_expose_assoc.md).

  All elements included in the `ON` clause of an exposed [CDS association](../../abap-glossary/abencds_association_glosry.md) must also be included in the projection list of the CDS projection view.

- [`path_expr`](abencds_proj_view_path_expr.md).element exposes an element of an association target of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). If no alternative element name `alias` is defined, the element name is defined by the name of the element named by the path expression. The keyword [`LOCALIZED`](abencds_localized.md) can be used to define [CDS localized fields](../../abap-glossary/abencds_localized_field_glosry.md). All associations that are part of the path expression must be filtered to 1. For details, see the topic about [path expressions in CDS projection views](abencds_proj_view_path_expr.md).

- Cast expressions [`cast_expr`](abencds_cast_expression_v2.md) are available in a reduced way:

  - The target data type can be specified as [CDS user-defined type](../../abap-glossary/abencds_user_defined_type_glosry.md) or as [DDIC data element](../../abap-glossary/abendata_element_glosry.md). Specifying a built-in ABAP Dictionary data type is not possible.

  - The addition `PRESERVING TYPE` is mandatory and must be used.

    That means that type conversions are not supported in CDS projection views and cast expressions can only be used to derive semantic information.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS projection view `DEMO_SALES_PV_SO_I_LIST` is a projection of the CDS view `DEMO_SALES_CDS_SO_I`. It contains details about a sales order item.

``` abap
@EndUserText.label: 'Projection View Sales Order Item List'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_PV_SO_I_LIST
provider contract transactional_query
  as projection on
    DEMO_SALES_CDS_SO_I
    {
      key so_item_key                   as SalesOrderItemKey,
          _SalesOrder.id                as SalesOrderId,
          posnr                         as PositionNumber,
          @ObjectModel.text.element: ['MaterialName']
          material                      as MaterialId,
          _Material._Text.material_name as MaterialName : localized,
          @Semantics.amount.currencyCode: 'Currency'
          gross_amount                  as GrossAmount,
          currency                      as Currency,
          @Semantics.quantity.unitOfMeasure: 'Unit'
          quantity                      as Quantity,
          unit                          as Unit
    }
```

## Addition 1

`... KEY`

### Description

The keyword `KEY` is used to define the current element as a key element of the [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md). A CDS projection view must define exactly the same key elements in the same order as key elements as the underlying projected entity.

**Caution**

The key elements of a CDS entity do not define unique lines in its result with regard to the key. An application or framework accessing a CDS entity must expect duplicate entries for the key fields in the result set. If the lines of a result set should be unique in respect to a set of key elements, it is the task of the application or framework that provides the CDS entity to define them appropriately and to document the view accordingly.

## Addition 2

`... AS alias`

### Description

Defines an alternative element name for the projected element. The alternative element name replaces the actual name of the element from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). The view field is created under the alternative element name in the CDS projection view. Accordingly, the alternative element name must comply with the general syntax rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md).

## Addition 3

`... LOCALIZED`

### Description

Defines a [CDS localized field](../../abap-glossary/abencds_localized_field_glosry.md) in the projection list of a CDS projection view. Localized fields are text fields for which translations in different languages are maintained. The keyword `LOCALIZED` causes automatic and implicit filtering to the current system language. For further details, see the topic [CDS DDL - `LOCALIZED`](abencds_localized.md).

## Addition 4

`... VIRTUAL`

### Description

Defines a [virtual element](../../abap-glossary/abencds_virtual_element_glosry.md) in the [projection list](abencds_proj_view_element_list.md) of a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md). Virtual elements are read-only elements of a CDS projection view which are not part of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). For further details, see topic [CDS DDL - `VIRTUAL`](abencds_proj_view_virtual_element.md).
