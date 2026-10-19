---
title: "CDS DDL - redirected, Transactional Query"
source_file: abencds_pv_assoc_redirected.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query > CDS DDL - expose_assoc, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - redirected, Transactional Query

## Syntax

``` abap
 ... REDIRECTED TO proj_view 
  | REDIRECTED TO COMPOSITION CHILD proj_view 
  | REDIRECTED TO PARENT proj_view  
```

### Variant

[1. `... REDIRECTED TO proj_view`](abencds_pv_assoc_redirected.md#variant-1)

[2. `... REDIRECTED TO COMPOSITION CHILD proj view`](abencds_pv_assoc_redirected.md#variant-2)

[3. `... REDIRECTED TO PARENT proj view`](abencds_pv_assoc_redirected.md#variant-3)

## Overview

### Description

Redirects a [CDS association](../../abap-glossary/abencds_association_glosry.md), a [to-child association](../../abap-glossary/abento_child_association_glosry.md), or a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) in a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) to a new association target. As a prerequisite, the original association target must also have a CDS projection view. Redirection using the keyword `REDIRECTED TO [...]` means to direct an association to a new association target, which is also a CDS projection view, in this way moving the complete data model to the projection layer.

With redirection, a specialized CDS association can lose its specialization and become a simple CDS association. This means that you can redirect a to-child or a CDS to-parent association with the keyword `REDIRECTED TO` and then it is exposed as a simple CDS association. The other way around is not possible - a simple CDS association cannot be specialized. Thus, you cannot use the addition `REDIRECTED TO COMPOSITION CHILD` or `REDIRECTED TO PARENT` to redirect a simple CDS association.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The projection view `DEMO_SALES_PV_SO` is based on the CDS view `DEMO_SALES_CDS_SO`. It replaces the [association targets](../../abap-glossary/abenassociation_target_glosry.md) of the associations with other CDS projection views where required.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection View SO'
@Metadata.allowExtensions: true
define root view entity DEMO_SALES_PV_SO
provider contract transactional_query
  as projection on
    DEMO_SALES_CDS_SO
    {
      key     so_key                           as SalesOrderKey,
              id                               as SalesOrderExternalId,
              lifecycle_status                 as LifecycleStatus,
              @ObjectModel.text.element: ['BuyerDescription']
              buyer_id                         as BuyerId,
              _Buyer.family_name               as BuyerDescription,
              created_by                       as CreatedBy,
              last_changed_by                  as LastChangedBy,
              @ObjectModel.virtualElementCalculatedBy:
                          'ABAP:CL_DEMO_SALES_VIRT_ELEM_EXIT'
      virtual ValidToDate : abap.dats(8),
              _Buyer                                                  
                  : redirected to DEMO_SALES_PV_BUPA,
              _ShipTo                          as _ShipToPartner 
                  : redirected to DEMO_SALES_PV_BUPA,
              DEMO_SALES_CDS_SO.ship_to_id     as ShipToPartner,
              _Items                                                  
                  : redirected to composition child DEMO_SALES_PV_SO_I,
              _Items[to many:posnr <= 3]             as _TopItems      
                  : redirected to DEMO_SALES_PV_SO_I
    }
```

### Executable Example

The executable example [Exposing Associations](../../abap-programming-language/abap-database-access/abenwith_associations_abexa.md) accesses the CDS projection view shown above, reads all fields and returns the result.

## Variant 1

`... REDIRECTED TO proj_view`

### Description

Redirects a [CDS association](../../abap-glossary/abencds_association_glosry.md) exposed in a CDS projection view to a new [association target](../../abap-glossary/abenassociation_target_glosry.md).

The following applies to the redirection of a CDS association:

- Can be used to redirect simple CDS associations, to-child or to-parent associations.

  **Note:** When the keyword `REDIRECTED TO` is used on specialized CDS associations (to-child or to-parent associations), they become non-specialized and are handled as CDS associations. To-child and to-parent associations which are projected in this way never define to-child and to-parent associations in the projection view.

- The target of the redirection `proj_view` must be a projection view based on the original target of the association.

- The target of the redirection `proj_view` can be the CDS projection view `proj_view` itself only if the projected CDS association is a [self association](../../abap-glossary/abenself_association_glosry.md).

- The target of the redirection `REDIRECTED TO` cannot be specified using a [path expression](abencds_proj_view_path_expr.md).

- The CDS projection view `proj_view` can be used multiple times as the redirection target of the projected CDS associations in the CDS projection view `proj_view`. The following syntax is valid:

  `_Assoc1: REDIRECTED TO proj_view, _Assoc2: REDIRECTED TO proj_view`

## Variant 2

`... REDIRECTED TO COMPOSITION CHILD proj_view`

### Description

Redirects a to-child association exposed in a CDS projection view to a new [association target](../../abap-glossary/abenassociation_target_glosry.md). With the addition `REDIRECTED TO COMPOSITION CHILD`, the special characteristics of a to-child association are kept.

The following applies to the redirection of a CDS to-child association:

- The CDS association redirected using the addition `REDIRECTED TO COMPOSITION CHILD` must be a CDS to-child association.

- The target of the redirection `REDIRECTED TO COMPOSITION CHILD` must be the projection of the original target of the association. Therefore, the target cannot be a root projection view.

- The target of the redirection `REDIRECTED TO COMPOSITION CHILD` cannot be specified using a [path expression](abencds_proj_view_path_expr.md).

- The target of `REDIRECTED TO COMPOSITION CHILD` cannot be the CDS projection view `proj_view` itself. A [self association](../../abap-glossary/abenself_association_glosry.md) is not possible.

- The redirection target `proj_view` must project exactly one to-parent association to its composition parent. This to-parent association must exist before the to-child association can be projected in the projection view.

- The redirection target `proj_view` can be used only once in a CDS to-child association and multiple times in CDS associations. This is demonstrated in the following simplified example:

  - This is valid

    `_Assoc1: REDIRECTED TO COMPOSITION CHILD proj_view, _Assoc2: REDIRECTED TO proj_view`

  - This is not valid

    `_Assoc1: REDIRECTED TO COMPOSITION CHILD proj_view, _Assoc2: REDIRECTED TO PARENT|{COMPOSITION CHILD} proj_view`

## Variant 3

`... REDIRECTED TO PARENT proj_view`

### Description

Redirects a [to-parent association](../../abap-glossary/abento_parent_association_glosry.md) in a CDS projection view to a new [association target](../../abap-glossary/abenassociation_target_glosry.md). With the addition `REDIRECTED TO PARENT`, the special characteristics of a CDS to-parent association are kept.

The following applies to the redirection of a CDS to-parent association:

- The CDS association `to_parent_assoc` projected with this syntax must be defined as a CDS to-parent association in the underlying CDS view.

- The target of the redirection `REDIRECTED TO PARENT` should be the projection of the original target of the to-parent association.

- The target of the redirection `REDIRECTED TO PARENT` cannot be specified using a [path expression](abencds_proj_view_path_expr.md).

- The addition `REDIRECTED TO PARENT` can be used no more than once in the definition of a CDS projection view. This means that a CDS projection view can have no more than one parent entity.

- The redirection target cannot be the CDS projection view `proj_view` itself. A [self association](../../abap-glossary/abenself_association_glosry.md) is not possible.

- The redirection target `proj_view` can be used only once in a CDS to-parent association and multiple times in CDS associations. This is demonstrated in the following simplified example:

  - This is valid

    `_Assoc1: REDIRECTED TO PARENT proj_view, _Assoc2: REDIRECTED TO proj_view`

  - This is not valid

    `_Assoc1: REDIRECTED TO PARENT proj_view, _Assoc2: REDIRECTED TO PARENT|{COMPOSITION CHILD} proj_view`
