---
title: "CDS DDL - DEFINE TRANSIENT VIEW ENTITY AS PROJECTION ON, Analytical Query"
source_file: abencds_define_view_as_analytical.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TRANSIENT VIEW ENTITY AS PROJECTION ON, Analytical Query

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
 @AccessControl.authorizationCheck: #NOT_ALLOWED 
[@proj_view_annot1] 
... 
DEFINE TRANSIENT VIEW ENTITY analytical_query 
   PROVIDER CONTRACT ANALYTICAL_QUERY 
   [parameter_list] 
    AS PROJECTION ON cds_entity [AS alias_name] 
   [aspect binding] 
      { element_list } 
   [WHERE cds_cond]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@AccessControl.authorizationCheck: #NOT_ALLOWED`](abencds_proj_view_annotations.md) · [`@proj_view_annot1`](abencds_proj_view_annotations.md) · [`PROVIDER CONTRACT ANALYTICAL_QUERY`](abencds_pv_provider_contract.md) · [`parameter_list`](abencds_parameter_list_apv.md) · [`aspect binding`](abencds_bind_aspect.md) · [`element_list`](abencds_element_list_apv.md) · [`WHERE`](abencds_where_apv.md)

## Description

Defines a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md) with the name `analytical_query` in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). A CDS analytical projection view defines an analytical query in its [`element_list`](abencds_element_list_apv.md).

The [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) `cds_entity` can be an [analytical cube view](../../abap-glossary/abencds_analytical_cube_glosry.md) or an [analytical dimension view](../../abap-glossary/abencds_anal_dim_view_glosry.md). One base view can serve as a basis for multiple analytical projection views.

The name of the CDS analytical projection view `analytical_query` is defined after the `DEFINE TRANSIENT VIEW ENTITY` statement. It must comply with the [naming rules for ABAP CDS](../abap-cds-syntax/abencds_general_syntax_rules.md) with one specialization: It can have a maximum of 28 characters (instead of 30 characters), because the analytical engine automatically adds the prefix *2C* during further processing.

## Prerequisites

- The header annotation [`@AccessControl.authorizationCheck`](abencds_proj_view_annotations.md) must be specified with the value `#NOT_ALLOWED`. Analytical queries cannot be accessed using [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and therefore, no [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) can be specified. Instead, the CDS access control of the projected entity is applied.

- The projected entity must be one of the following:

  - An [analytical cube view](../../abap-glossary/abencds_analytical_cube_glosry.md), annotated with the framework-specific annotation [`@Analytics.dataCategory: #CUBE`](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

  - An [analytical dimension view](../../abap-glossary/abencds_anal_dim_view_glosry.md) annotated with the framework-specific annotation [`@Analytics.dataCategory: #DIMENSION`](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

**Components**

- Header annotations specified before the statement `DEFINE TRANSIENT VIEW ENTITY` are not inherited from the projected entity. It is possible, but not mandatory, to specify [entity annotations](abencds_f1_entity_annotations.md) `@entity_annot` or [projection view annotations](abencds_proj_view_annotations.md) `@proj_view_annot` as header annotations.

- The mandatory keyword `TRANSIENT` defines a CDS analytical projection view as transient CDS view entity. That means that only a runtime object on the ABAP server is generated, but no [SQL view](../../abap-glossary/abensql_view_glosry.md) is generated on the HANA database.

- The [provider contract](abencds_pv_provider_contract.md) must be specified with the value `ANALYTICAL_QUERY` to ensure that the appropriate features and syntax checks for analytical queries are applied.

- [`parameter_list`](abencds_parameter_list_apv.md) can be used to assign [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) to the projection view. These input parameters can be specified in operand positions of the view and can be assigned actual parameters when the view is used.

- The optional addition `AS` defines the name `alias_name` as [alias name](../../abap-glossary/abenalias_glosry.md) of the projected entity. The alias name can have a maximum of 30 characters. If no name is defined explicitly using `AS`, then the original name of the data source is used.

- The element list [`element_list`](abencds_element_list_apv.md) defines the components of the analytical query.

- Optionally, the number of rows included in the result set can be further restricted by the addition [`WHERE`](abencds_where_apv.md).

## Restriction

- Defining new associations in the projection layer is not possible.

- Exposing associations is not allowed either.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS analytical projection view `DEMO_ANALYTICAL_QUERY` defines an analytical query. It is based on the cube view `DEMO_CDS_CUBE_VIEW`.

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
