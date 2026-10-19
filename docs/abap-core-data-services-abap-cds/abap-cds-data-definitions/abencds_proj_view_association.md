---
title: "CDS DDL - ASSOCIATION, Transactional Query"
source_file: abencds_proj_view_association.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - ASSOCIATION, Transactional Query

## Syntax

``` abap
 ... ASSOCIATION [cardinality] [TO] target [AS _assoc] ON cds_cond 
                [ WITH DEFAULT FILTER cds_cond ] ...  
```

[`cardinality`](abencds_cardinality_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md)

## Description

Defines a [CDS association](../../abap-glossary/abencds_association_glosry.md) with the name `_assoc` in a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md). Possible association targets and rules are the same as for [associations in CDS view entities](abencds_association_v2.md), but there are further restrictions. The main difference is that the newly defined associations can only be exposed, but they cannot be used in [path expressions](../../abap-glossary/abenpath_expression_glosry.md) to include elements from the [association target](../../abap-glossary/abenassociation_target_glosry.md). The purpose of defining new associations is to model new relationships which can be interpreted by consumer frameworks, such as the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md). However, no additional [joins](../../abap-glossary/abenjoin_glosry.md) should be generated on CDS level by denormalizing fields from new association targets into the CDS projection view. Only regular associations can be defined in a CDS projection view. Specialized associations of type [to-child](../../abap-glossary/abento_child_association_glosry.md) or [to-parent](../../abap-glossary/abento_parent_association_glosry.md) are not supported.

All elements included in the `ON` clause of an exposed [CDS association](../../abap-glossary/abencds_association_glosry.md) must also be included in the projection list of the CDS projection view.

Syntax rules

- New associations in CDS projection views are defined in exactly the same way as associations in CDS view entities. The same rules apply to the [cardinality specification](abencds_cardinality_v2.md), `AS _assoc`, `WITH DEFAULT FILTER`, and the `ON` condition. See topic [`CDS DDL - CDS View Entity, ASSOCIATION`](abencds_simple_association_v2.md).

Possible association targets:

- Same as for CDS view entities, see topic [CDS View Entity, `ASSOCIATION`](abencds_simple_association_v2.md) or [Data Source Matrix](abencds_data_source_matrix.md).

Exposure in the projection list

- The newly defined association can be exposed, but exposure is not mandatory, as it can also be done in [CDS view entity extensions](../../abap-glossary/abencds_view_entity_extend_glosry.md) later on.

- An alias name `alias` can be assigned to the exposed association.

- It is possible to enhance a locally defined association with an additional filter when exposing it in the projection list. Two kinds of attributes can be added in square brackets as filter: [cardinality](../../abap-glossary/abencardinality_glosry.md) and [filter condition](../../abap-glossary/abenfilter_condition_glosry.md). It is not possible to specify [join type](../../abap-glossary/abenjoin_type_glosry.md) characteristics in the filter. The details are described in topic [CDS DDL - CDS Projection View, filter](abencds_pv_assoc_modified.md).

  When exposing a CDS association with a filter, an alternative element name `alias` using `AS` is mandatory. Here's an example: `_toAssoc[to exact one:field='1'] as filteredAssoc`

- A CDS association can be exposed multiple times with various alternative element names. This makes it possible to use different filter conditions.

- An exposed CDS association is part of the projection list. It is not, however, part of the result set, nor a component of the type defined in ABAP with respect to the CDS projection view.

Usage

- No fields must be selected from locally defined associations. [Path expressions](../../abap-glossary/abenpath_expression_glosry.md) are not supported.

Client dependency

- A CDS projection view that is based on a client-independent CDS view must not contain an association to a client-dependent target view. Client dependency must not be changed by introducing a new association. This also applies to [CDS DDIC-based view extensions](../../abap-glossary/abencds_view_extend_glosry.md) later on, as this may lead to incompatibilities.

## Restrictions

- Redirection of a newly defined association with the keyword [`REDIRECTED TO`](abencds_proj_view_expose_assoc.md) is not possible.

- To-child or to-parent associations cannot be defined.

## Hint

For an overview of all possible association targets of all CDS entities that can define associations, see [Data Source Matrix](abencds_data_source_matrix.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS projection view `DEMO_SALES_PV_SO_ASSOC` is a projection of the CDS view entity `DEMO_SALES_CDS_SO`. It defines associations to a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md) and a CDS DDIC-based view (obsolete). These associations are exposed in the element list, but no fields are picked from the associations via a path expression.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection View SO'
define root view entity DEMO_SALES_PV_SO_ASSOC
  provider contract transactional_query
  as projection on DEMO_SALES_CDS_SO

  association of many to one DEMO_SALES_SO_CUSTOM_ANALYTICS 
    as _SalesOrderCustomData   
    on _SalesOrderCustomData.SalesOrderKey = $projection.SalesOrderKey

  association of many to one DEMO_SALES_CDS_VIEW_ANALYTICS  
    as _SalesOrderAnalyticData 
    on _SalesOrderAnalyticData.SalesOrderKey = $projection.SalesOrderKey
{
  key so_key             as SalesOrderKey,
      id                 as SalesOrderExternalId,
      lifecycle_status   as LifecycleStatus,
      buyer_id           as BuyerId,
      _Buyer.family_name as BuyerDescription,
      created_by         as CreatedBy,
      last_changed_by    as LastChangedBy,
      _SalesOrderAnalyticData,
      _SalesOrderCustomData
}
```
