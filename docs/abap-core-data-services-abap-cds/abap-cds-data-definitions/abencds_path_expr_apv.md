---
title: "CDS DDL - path_expr, Analytical Query"
source_file: abencds_path_expr_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries > CDS DDL - element_list, Analytical Query > CDS DDL - element, Analytical Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - path_expr, Analytical Query

## Syntax

``` abap
... [source.]_assoc1[parameters][filter] ...  
```

[`parameters`](abencds_select_parameters_v2.md) · [`filter`](abencds_pv_assoc_modified.md)

## Description

A [path expression](../../abap-glossary/abenpath_expression_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) is a sequence of CDS associations separated by periods (.) whose names are specified using `assoc1, assoc2,` and so on.

In analytical projection views, path expressions are only supported in the following scenarios:

- Language dependencies implemented using the keyword [`LOCALIZED`](abencds_localized.md).

- Temporal dependencies implemented in the following format:

  ` [to one:date_from <= $parameter.key_date && date_to >= $parameter.key_date]` **Note:** `key_date` can be a [parameter](abencds_f1_param.md), a [session variable](abencds_session_variable_v2.md), or a [literal](abencds_literal_v2.md). It must be typed with [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). It must be annotated with `@Semantics.businessDate`.

## Hint

Fields included via path expressions can be texts, display attributes, or texts belonging to display attributes. In an [analytical cube view](../../abap-glossary/abencds_analytical_cube_glosry.md), such fields can be text or foreign key associations. In an [analytical dimension view](../../abap-glossary/abencds_anal_dim_view_glosry.md), these fields can be text associations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS analytical projection view `DEMO_ANALYTICAL_QUERY` defines an analytical query. It is based on the cube view `DEMO_CDS_CUBE_VIEW`. It contains a path expression to a localized text element `CurrencyDescription`.

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
