---
title: "CDS DDL - PROVIDER CONTRACT"
source_file: abencds_pv_provider_contract.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - PROVIDER CONTRACT

## Syntax

``` abap
... PROVIDER CONTRACT { TRANSACTIONAL_QUERY 
                      | TRANSACTIONAL_INTERFACE 
                      | ANALYTICAL_QUERY } ...   
  | { } ...  
```

### Alternative

[1. `... PROVIDER CONTRACT`](abencds_pv_provider_contract.md#alternative-1)

[2. `... { }`](abencds_pv_provider_contract.md#alternative-2)

## Overview

### Description

A [CDS provider contract](../../abap-glossary/abencds_provider_contract_glosry.md) specifies the scenario in which a CDS projection view is used. The scenario determines in which runtime a CDS projection view is executed and which features are available. It is recommended that the provider contract is always specified to ensure that the appropriate, runtime-specific syntax checks are applied.

It is also possible, but not recommended, to leave out the provider contract. Projection views without provider contract are handled similarly to transactional projection views, but there are some minor differences in the syntax checks applied.

## Alternative 1

`... PROVIDER CONTRACT ...`

### Addition

[1. `... TRANSACTIONAL_QUERY`](abencds_pv_provider_contract.md#addition-1)

[2. `... TRANSACTIONAL_INTERFACE`](abencds_pv_provider_contract.md#addition-2)

[3. `... ANALYTICAL_QUERY`](abencds_pv_provider_contract.md#addition-3)

### Description

Currently, the following provider contracts are available:

- `TRANSACTIONAL_QUERY`

- `TRANSACTIONAL_INTERFACE`

- `ANALYTICAL_QUERY`

[Child entities](../../abap-glossary/abenchild_entity_glosry.md) within a [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) inherit their parents' provider contract and the specification of a provider contract for a child entity is not allowed. As soon as a projection view contains a [to-parent association](../../abap-glossary/abento_parent_association_glosry.md) or a [redirection](abencds_pv_assoc_redirected.md) to a parent entity, a provider contract must not be set.

### Hint

Further provider contracts are planned to be released in the near future.

## Addition 1

`... TRANSACTIONAL_QUERY`

### Description

Specifies a CDS projection view as [transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md). Transactional queries are intended for modelling the projection layer of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). A transactional projection view must always be part of a business object. That means it must either be a [root entity](../../abap-glossary/abenroot_entity_glosry.md) itself, or it must be part of a composition tree that contains a root entity.

The feature set focuses on specializing the [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) of the underlying business object.

The runtime for transactional queries is mainly the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md), but also the [RAP transactional engine](../../abap-glossary/abenrap_transac_engine_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS projection view defines the provider contract `TRANSACTIONAL_QUERY`.

``` abap
@EndUserText.label: 'CDS projection view, REDEFINED ASSOC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_CDS_PV_PARENT
  provider contract transactional_query
  as projection on DEMO_CDS_VIEW_PARENT

    redefine association _child
      redirected to composition child DEMO_CDS_PV_CHILD

{
  key Id,
      Int1,
      /* Associations */
      _child.Int1 as field_exposure
      }
```

Its child entity derives the provider contract from the parent entity. It does not specify a separate provider contract:

``` abap
@EndUserText.label: 'CDS projection view, REDEFINED ASSOC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_PV_CHILD
  as projection on DEMO_CDS_VIEW_CHILD

    redefine association _to_parent 
      redirected to parent DEMO_CDS_PV_PARENT

{
  key Id,
      Int1,
      /* Associations */
      _to_parent
}
```

## Addition 2

`... TRANSACTIONAL_INTERFACE`

### Description

Specifies a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md). CDS transactional interfaces serve as stable public interface layer in a CDS data model. They are typically used in the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md) to provide the basis for a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md). CDS transactional interfaces have a restricted feature set. They only support projecting elements and associations from the projected entity. It is recommended that [release contracts](../../abap-glossary/abenrelease_contract_glosry.md) [C1](../../abap-glossary/abenc1_contract_glosry.md) and, optionally, also [C0](../../abap-glossary/abenc1_contract_glosry.md) are added.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS transactional interface is based on the CDS view entity `DEMO_CDS_PURCH_DOC_M`. The to-child association is redirected to the CDS transactional interface of the child entity. Both parent and child entity are release for system-internal use (C1 Contract).

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

## Addition 3

`... ANALYTICAL_QUERY`

### Description

[CDS analytical projection views](../../abap-glossary/abencds_analytical_pv_glosry.md) are intended for modelling analytical queries within a CDS data model. An analytical projection view must always be part of an analytical object and the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) must be an [analytical cube view](../../abap-glossary/abencds_analytical_cube_glosry.md) or an [analytical dimension view](../../abap-glossary/abencds_anal_dim_view_glosry.md). The feature set is restricted to the capabilities of the runtime of the analytical engine. The runtime for analytical queries are analytical engines, such as [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md) or Online Analytical Processing (OLAP).

See also: [CDS Projection View, Analytical Queries](abencds_analytical_query_apv.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS projection view defines the provider contract `ANALYTICAL_QUERY`.

``` abap
@EndUserText.label: 'CDS projection view, analytical query'
@AccessControl.authorizationCheck: #NOT_ALLOWED
define transient view entity DEMO_ANALYTICAL_QUERY
  provider contract analytical_query
  with parameters
    p_targetCurrency : abap.cuky
  as projection on DEMO_CDS_CUBE_VIEW
{

          //ROWS
          @AnalyticsDetails.query.axis: #FREE
          so_key                       as SalesOrderKey,

          @AnalyticsDetails.query.axis: #ROWS
          lifecycle_status             as LifecycleStatus,

          //COLUMNS
          @AnalyticsDetails.query.axis: #COLUMNS
          quantity_sum                 as QuantitySum,

          uom_sum                      as UnitOfQuantity,

          @ObjectModel.text.element: ['CurrencyDescription']
          currency_sum                 as CurrencyOfAmount,
          _Currency._Text.CurrencyName as CurrencyDescription : localized,

          //typed literal
          @Aggregation.default: #FORMULA
          abap.decfloat34'0.05'        as Discount,


          //Formula to define a calculated quantity
          @Aggregation.default: #FORMULA
          @Semantics.quantity.unitOfMeasure: 'AmPerQuanUnit'
          curr_to_decfloat_amount( amount_sum ) /
          $projection.QuantitySum      as AmountPerQuantity,

          //virtual element to define a calculated unit
  virtual AmPerQuanUnit  : dd_cds_calculated_unit,

  virtual targetCurrency : abap.cuky,

          //parameter used in currency conversion
          @Aggregation.default: #FORMULA
          @Semantics.amount.currencyCode: 'targetCurrency'
          currency_conversion(
            amount => curr_to_decfloat_amount( amount_sum ),
            source_currency => currency_sum,
            target_currency => $parameters.p_targetCurrency,
            exchange_rate_date => created_on
          )                            as convertedAmount


}
```

## Alternative 2

`... { }`

### Description

It is possible, but not recommended, to leave out the provider contract. The default provider contract, if no provider contract is set explicitly, is `TRANSACTIONAL_QUERY`. The same features are available as for transactional queries and a projection view without provider contract can be used in the same scenarios. However, there are some minor differences in the syntax checks applied. The differences are listed in topic [CDS projection view, no contract](abencds_pv_no_contract.md).
