---
title: "CDS DDL - projection_list, Transactional Interface"
source_file: abencds_element_list_interface.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Interface > CDS DDL - DEFINE VIEW ENTITY AS PROJECTION ON, Transactional Interface"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - projection_list, Transactional Interface

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
      [KEY]   {proj_element        [AS alias]} 
            | {proj_assoc          [AS alias]} 
            | {cast_expr            AS alias}  
```

[`@element_annot1`](abencds_element_annotations_v2.md) · [`@element_annot2`](abencds_element_annotations_v2.md) · [`proj_assoc`](abencds_proj_view_expose_assoc.md) · [`cast_expr`](abencds_cast_expression_v2.md)

### Addition

[1. `... KEY`](abencds_element_list_interface.md#addition-1)

[2. `... AS alias`](abencds_element_list_interface.md#addition-2)

## Overview

### Description

Defines the elements of a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md). The elements are specified in a comma-separated list in curly brackets { }.

The feature set of a transactional interface is restricted to projecting elements from the underlying projected entity. No new associations, virtual elements, or fields can be defined.

The following elements are supported in the projection list of a transactional interface:

- Element annotations can be specified. The rules for [propagation of element annotations in CDS projection views](abencds_element_annotations_pv.md) apply.

- `proj_element` exposes an element from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). `AS` can be used to define an alternative element name `alias`.

  **Note:** In transactional interfaces, an element from the projected entity can be exposed multiple times with different alias names.

- [`proj_assoc`](abencds_proj_view_expose_assoc.md) exposes a [CDS association](../../abap-glossary/abencds_association_glosry.md), a [to-child association](../../abap-glossary/abento_child_association_glosry.md), or a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). Exposed associations can be redirected to a new target when the [association target](../../abap-glossary/abenassociation_target_glosry.md) is also projected. Read topic [CDS DDL - `CDS Projection View, proj_assoc`](abencds_proj_view_expose_assoc.md) for further details.

  **Note:** Adding additional filter conditions to exposed associations is not supported in CDS transactional interfaces. All elements included in the `ON` clause of an exposed [CDS association](../../abap-glossary/abencds_association_glosry.md) must also be included in the projection list of the CDS projection view.

- Cast expressions [`cast_expr`](abencds_cast_expression_v2.md) are available in a reduced way:

  - The target data type can be specified as [CDS user-defined type](../../abap-glossary/abencds_user_defined_type_glosry.md) or as [DDIC data element](../../abap-glossary/abendata_element_glosry.md). Specifying a built-in ABAP Dictionary data type is not possible.

  - The addition `PRESERVING TYPE` is mandatory and must be used.

    That means that type conversions are not supported in CDS projection views and cast expressions can only be used to derive semantic information.

## Restrictions

In a transactional interface, the following elements are not supported in the projection list: expressions, virtual elements, [CDS localized fields](../../abap-glossary/abencds_localized_field_glosry.md), and parameters.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS transactional interface is based on the CDS view entity `DEMO_CDS_PURCH_DOC_M`. The to-child association is redirected to the CDS transactional interface of the child entity.

Both parent and child entity should be released for system-internal use under the C1 contract.

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_CDS_TRANS_INTERFACE_ROOT
  provider contract transactional_interface
  as projection on DEMO_CDS_PURCH_DOC_M
{
  key PurchaseDocument,
      Description,
      Status,
      Priority,
      /* Associations */
      _PurchaseDocumentItem: 
        redirected to DEMO_CDS_TRANS_INTERFACE_CHILD
}
```

The following CDS transactional interface represents the child entity:

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_TRANS_INTERFACE_CHILD
  provider contract transactional_interface
  as projection on DEMO_CDS_PURCH_DOC_I_M
{
  key PurchaseDocumentItem,
  key PurchaseDocument,
      Description,
      Vendor,
      /* Associations */
      _PurchaseDocument : redirected to DEMO_CDS_TRANS_INTERFACE_ROOT
}
```

## Addition 1

`... KEY`

### Description

The keyword `KEY` is used to define the current element as a key element of the transactional interface. A transactional interface must define exactly the same key elements in the same order as key elements as the underlying projected entity.

**Caution**

The key elements of a CDS entity do not define unique lines in its result with regard to the key. An application or framework accessing a CDS entity must expect duplicate entries for the key fields in the result set. If the lines of a result set should be unique in respect to a set of key elements, it is the task of the application or framework that provides the CDS entity to define them appropriately and to document the view accordingly.

## Addition 2

`... AS alias`

### Description

Defines an alternative element name for the projected element. The alternative element name replaces the actual name of the element from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). The view field is created under the alternative element name in the CDS transactional interface. Accordingly, the alternative element name must comply with the general syntax rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md).
