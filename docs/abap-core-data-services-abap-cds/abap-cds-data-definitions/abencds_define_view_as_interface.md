---
title: "CDS DDL - DEFINE VIEW ENTITY AS PROJECTION ON, Transactional Interface"
source_file: abencds_define_view_as_interface.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Interface"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE VIEW ENTITY AS PROJECTION ON, Transactional Interface

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@proj_view_annot1] 
[@proj_view_annot2] 
... 
DEFINE [ROOT] VIEW ENTITY projection_view 
  PROVIDER CONTRACT TRANSACTIONAL_INTERFACE 
    AS PROJECTION ON cds_entity [AS alias_name] 
   [aspect binding] 
      { projection_list } 
   [WHERE cds_cond]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@proj_view_annot1`](abencds_proj_view_annotations.md) · [`@proj_view_annot2`](abencds_proj_view_annotations.md) · [`PROVIDER CONTRACT TRANSACTIONAL_INTERFACE`](abencds_pv_provider_contract.md) · [`aspect binding`](abencds_bind_aspect.md) · [`projection_list`](abencds_element_list_interface.md) · [`WHERE`](abencds_interface_cond_expr.md)

### Addition

[1. `... ROOT`](abencds_define_view_as_interface.md#addition-1)

[2. `... AS alias_name`](abencds_define_view_as_interface.md#addition-2)

## Overview

### Description

Defines a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) with the name `projection_view` in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md).

The projected entity `cds_entity` can be either a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The projected entity must be part of a RAP BO: It must either be a root entity or contain a to-parent association. No other CDS entities or data sources are allowed as projected entity. Path expressions are not allowed for specifying the projected entity. One CDS entity can be used as basis for multiple CDS projection views.

The name of the CDS projection view `projection_view` is defined after the `DEFINE VIEW ENTITY` statement. The usual rules for ABAP Dictionary views apply to this name and it is not case-sensitive (it is transformed internally into uppercase letters). It can have a maximum of 30 characters and is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The name of the DDL source and of the CDS entity must be identical.

## Prerequisites

A [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) that uses the addition [`PROVIDER CONTRACT TRANSACTIONAL_INTERFACE`](abencds_pv_provider_contract.md) must be part of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). That means that the view must either be a [root entity](../../abap-glossary/abenroot_entity_glosry.md) itself, or it must be part of a [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) and reach a root entity via a [CDS composition](../../abap-glossary/abencds_composition_glosry.md).

**Components**

- Header annotations specified before the statement `DEFINE VIEW ENTITY` are not inherited from the projected entity. It is possible, but not mandatory, to specify [entity annotations](abencds_f1_entity_annotations.md) `@entity_annot` or [projection view annotations](abencds_proj_view_annotations.md) `@proj_view_annot` as header annotations.

- The [provider contract](abencds_pv_provider_contract.md) must be set to `TRANSACTIONAL_INTERFACE`.

- The projection list [`projection_list`](abencds_element_list_interface.md) defines the elements exposed as part of the interface.

- Optionally, the number of rows included in the result set can be further restricted by the addition [`WHERE`](abencds_interface_cond_expr.md).

**Release Contracts**

- A transactional interface can be released for [Contract C0](../../abap-glossary/abenc0_contract_glosry.md).

- A transactional interface should be released for [Contract C1](../../abap-glossary/abenc1_contract_glosry.md).

- A transactional interface should not be released for [Contract C2](../../abap-glossary/abenc2_contract_glosry.md).

## Restrictions

- A transactional interface cannot define new associations.

- No further clauses are possible. `WHERE`, `UNION`, and `GROUP BY` are not supported.

### Hints

- [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) defined for a CDS transactional interface must be defined symmetrically to the [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) for the projected entity. The behavior of the access control of the projected entity must be inherited.

- For an overview of all possible data sources of all available CDS entities, see [Data Source Matrix](abencds_data_source_matrix.md).

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

`... ROOT`

### Description

The keyword `ROOT` specifies that the transactional interface is the [root entity](../../abap-glossary/abenroot_entity_glosry.md) of a [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md). The transactional interface must always reflect the position of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) in the composition tree: if the projected entity is a [root entity](../../abap-glossary/abenroot_entity_glosry.md), the transactional interface must be a root as well. If the projected entity is not a root, the projection view cannot be a root. In this case, the projected entity must contain a [to-parent association](../../abap-glossary/abento_parent_association_glosry.md).

**Note:** A transactional interface must always either be a root entity itself, or it must be part of a composition tree and reach a root entity via an association.

## Addition 2

`... AS alias_name`

### Description

Defines the name `alias_name` as [alias name](../../abap-glossary/abenalias_glosry.md) of the projected entity. The alias name can have a maximum of 30 characters. If no name is defined explicitly using `AS`, then the original name of the data source is used.
