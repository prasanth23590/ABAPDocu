---
title: "CDS DDL - DEFINE VIEW ENTITY AS PROJECTION ON, Transactional Query"
source_file: abencds_define_view_as_projection.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE VIEW ENTITY AS PROJECTION ON, Transactional Query

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@proj_view_annot1] 
[@proj_view_annot2] 
... 
DEFINE [ROOT] VIEW ENTITY projection_view 
   [PROVIDER CONTRACT TRANSACTIONAL_QUERY] 
    AS PROJECTION ON cds_entity [AS alias_name] 
   [aspect binding] 
   [association1 association2 ...] 
   [redefined_assoc1 redefined_assoc2 ...] 
      { projection_list } 
   [WHERE cds_cond]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@proj_view_annot1`](abencds_proj_view_annotations.md) · [`@proj_view_annot2`](abencds_proj_view_annotations.md) · [`PROVIDER CONTRACT TRANSACTIONAL_QUERY`](abencds_pv_provider_contract.md) · [`aspect binding`](abencds_bind_aspect.md) · [`association1`](abencds_proj_view_association.md) · [`association2`](abencds_proj_view_association.md) · [`redefined_assoc1`](abencds_proj_view_redefined_assoc.md) · [`redefined_assoc2`](abencds_proj_view_association.md) · [`projection_list`](abencds_proj_view_element_list.md) · [`WHERE`](abencds_proj_view_cond_expr.md)

### Addition

[1. `... ROOT`](abencds_define_view_as_projection.md#addition-1)

[2. `... AS alias_name`](abencds_define_view_as_projection.md#addition-2)

## Overview

### Description

Defines a [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) with the name `projection_view` in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). A CDS projection view is a direct projection of an underlying [CDS entity](../../abap-glossary/abencds_entity_glosry.md) `cds_entity` (called [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md)) and exposes a subset of the elements of the projected entity, which are defined in the projection list [`projection_list`](abencds_proj_view_element_list.md).

The projected entity `cds_entity` can be either a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md), or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). No other CDS entities or data sources are allowed as projected entity. Path expressions are not allowed for specifying the projected entity. One CDS entity can be used as basis for multiple CDS projection views.

The name of the CDS projection view `projection_view` is defined after the `DEFINE VIEW ENTITY` statement. The usual rules for ABAP Dictionary views apply to this name and it is not case-sensitive (it is transformed internally into uppercase letters). It can have a maximum of 30 characters and is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The name of the DDL source and of the CDS entity must be identical.

## Prerequisites

A CDS transactional query that uses the addition [`PROVIDER CONTRACT TRANSACTIONAL_QUERY`](abencds_pv_provider_contract.md) must be part of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). That means that the view must either be a root entity itself, or it must be part of a composition tree and reach a root entity via a composition.

**Components**

- Header annotations specified before the statement `DEFINE VIEW ENTITY` are not inherited from the projected entity. It is possible, but not mandatory, to specify [entity annotations](abencds_f1_entity_annotations.md) `@entity_annot` or [projection view annotations](abencds_proj_view_annotations.md) `@proj_view_annot` as header annotations.

- The [provider contract](abencds_pv_provider_contract.md) specifies the scenario in which the projection view is used. It is recommended that a provider contract is always specified. Otherwise, no runtime-specific syntax checks are applied. See the [topic about provider contracts](abencds_pv_provider_contract.md) for further details.

- It is possible to add new, local, read-only associations `association1, association2` to a projection view after the view definition with `DEFINE VIEW ENTITY AS PROJECTION ON`. The same rules apply as to [associations in CDS view entities](abencds_association_v2.md). The main difference is that read-only associations in projection views can only be exposed but they cannot be used in [path expressions](abencds_path_expression_v2.md) to expose elements from new associations. Details on new local associations in CDS projection views can be found in topic [`CDS DDL - projection_view, ASSOCIATION`](abencds_proj_view_association.md).

- The projection list [`projection_list`](abencds_proj_view_element_list.md) can consist of elements of the projected entity, path expressions, exposed associations, and [virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md).

- Optionally, the number of rows included in the result set can be further restricted by the addition [`WHERE`](abencds_proj_view_cond_expr.md).

### Hints

- [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) defined for a CDS transactional query must be defined symmetrically to the [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) for the projected entity. All behavior of the access control of the projected entity must be inherited.

- For an overview of all possible data sources of all available CDS entities, see [Data Source Matrix](abencds_data_source_matrix.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS transactional query `DEMO_SALES_PV_BUPA` is a projection of the existing CDS view `DEMO_SALES_CDS_BUPA`. The result set contains only rows where the last name of the business partner starts with *P*.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection View for BuPa'
define root view entity DEMO_SALES_PV_BUPA
provider contract transactional_query
  as projection on
    DEMO_SALES_CDS_BUPA
    {
      key id          as BusinessPartnerID,
          given_name  as GivenName,
          middle_name as MiddleName,
          family_name as FamilyName
    }
  where $projection.familyname like 'P%'
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS transactional query `DEMO_SALES_PV_SO_I_SL` is a projection of the existing CDS view `DEMO_SALES_CDS_SO_I_SL`. It exposes a subset of the elements of the projected entity as well as an association.

A provider contract is not specified, since the provider contract is specified only once in the root entity of a CDS composition tree and all child entities automatically inherit this provider contract. In this case, the root entity is `DEMO_SALES_PV_SO` and it specifies the business object as transactional query.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection View SO Item Schedule Line'
@Metadata.allowExtensions: true
define view entity DEMO_SALES_PV_SO_I_SL
  as projection on
    DEMO_SALES_CDS_SO_I_SL
    {
      key schedule_line_key as ScheduleLineKey,
          parent_key        as SalesOrderItemKey,
          _SalesOrderItem : redirected to parent DEMO_SALES_PV_SO_I
    }
```

## Addition 1

`... ROOT`

### Description

The keyword `ROOT` specifies that the projection view is the [root entity](../../abap-glossary/abenroot_entity_glosry.md) of a [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md). The projection view must always reflect the position of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) in the composition tree: if the projected entity is a [root entity](../../abap-glossary/abenroot_entity_glosry.md), the projection view must be a root as well. If the projected entity is not a root, the projection view cannot be a root. In this case, the projected entity must contain a [to-parent association](../../abap-glossary/abento_parent_association_glosry.md).

**Note:** If a CDS projection view is defined as transactional query using the addition [`PROVIDER CONTRACT TRANSACTIONAL_QUERY`](abencds_pv_provider_contract.md), then the view must either be a root entity itself, or it must be part of a composition tree and reach a root entity via an association.

## Addition 2

`... AS alias_name`

### Description

Defines the name `alias_name` as [alias name](../../abap-glossary/abenalias_glosry.md) of the projected entity. The alias name can have a maximum of 30 characters. If no name is defined explicitly using `AS`, then the original name of the data source is used.
