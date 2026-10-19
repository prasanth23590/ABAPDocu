---
title: "CDS DDL - filter, Transactional Query"
source_file: abencds_pv_assoc_modified.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query > CDS DDL - expose_assoc, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - filter, Transactional Query

## Syntax

``` abap
 ... [[cardinality:] cds_cond ] ...  
```

## Description

Specifies a filter for an association from the projected entity that is exposed or redefined in a CDS projection view. The filter is specified in square brackets \[ \] when the association is exposed in the projection list. The filter can consist of two attributes, namely cardinality and [filter condition](../../abap-glossary/abenfilter_condition_glosry.md).

Example: `_Assoc[exact one to exact one:field1 = 5].`

The rules described in topic [CDS DDL - CDS View Entity, `path_expr`, Cardinality](abencds_path_expr_card_v2.md) apply to the cardinality `cardinality`. Additionally, the following special rules apply:

- A filter can never consist of a new cardinality alone. It must always be combined with a filter condition.

- The cardinality of an association might implicitly be changed when a filter is added. If this is the case, and only in this case, the new cardinality can be specified in square brackets.

The following rules apply to the filter condition `cds_cond`:

- The rules described in topic [CDS DDL - View Entity, `path_expr`, filter](abencds_path_expression_filter_v2.md) apply with one exception: no [join type](../../abap-glossary/abenjoin_type_glosry.md) can be specified for a filter of an exposed association in a CDS projection view.

- The prefix `$projection.` can be used within a filter to access an element from the projection list

  Example: `_Assoc[to exact one:field1 = $projection.field1] as _alias`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS projection view `DEMO_SALES_PV_SO_MODIFY` is a projection of the CDS view `DEMO_SALES_CDS_SO`. It exposes the association `_Items` twice. The first time, all original properties are kept. The second time, the association is modified with a filter. The new alias name `_TopItems` is assigned and by using the keyword `REDIRECTED TO`, the specialization as composition child is lost and the association is projected as a simple CDS association.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_SALES_PV_SO_MODIFY
  provider contract transactional_query
  as projection on
    DEMO_SALES_CDS_SO
    {
      key so_key               as SalesOrderKey,
          id                   as SalesOrderExternalId,
          lifecycle_status     as LifecycleStatus,
          buyer_id             as BuyerId,
          _Buyer.family_name   as BuyerDescription,
          created_by           as CreatedBy,
          last_changed_by      as LastChangedBy,
          _Items:                            
              redirected to composition child DEMO_SALES_PV_MODIFY_1,
          _Items[many to many:posnr <= 3] as _TopItems: 
              redirected to DEMO_SALES_PV_MODIFY_1
    }
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS projection view `DEMO_SALES_PV_SO_PARAM` is a projection of the CDS view `DEMO_SALES_CDS_SO`. It exposes the parameter `my_parameter` that is included in the associated CDS view `DEMO_SALES_CDS_SO_PARAM`. The parameter has to be filled upon exposure.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection View SO'
@Metadata.allowExtensions: true
define root view entity DEMO_SALES_PV_SO_PARAM
  as projection on
    DEMO_SALES_CDS_SO
    {
      key so_key                               as SalesOrderKey,
          id                                   as SalesOrderExternalId,
          lifecycle_status                     as LifecycleStatus,
          buyer_id                             as BuyerId,
          created_by                           as CreatedBy,
          last_changed_by                      as LastChangedBy,
          _Param(P_MyParameter: 'A').my_parameter 
                                               as MyParameter
    }
```
