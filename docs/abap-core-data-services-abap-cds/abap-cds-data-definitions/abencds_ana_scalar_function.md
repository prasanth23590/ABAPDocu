---
title: "ABAP CDS - Analytical Scalar Functions"
source_file: abencds_ana_scalar_function.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions > ABAP CDS - Scalar Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Analytical Scalar Functions

[Analytical scalar functions](../../abap-glossary/abencds_ana_scalar_glosry.md) are [scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md) that are evaluated by an analytical runtime environment.

They can be specified in the [element list](abencds_select_list_entry_v2.md) of [analytical projection views](../../abap-glossary/abencds_analytical_pv_glosry.md).

Analytical scalar functions are delivered by SAP. They can only be defined and implemented internally by SAP. They are available for internal and external use in [CDS analytical queries](../../abap-glossary/abencds_analytic_query_glosry.md).

**SAP-Delivered Analytical Scalar Functions**

The following analytical scalar functions are delivered by SAP. They are released under the [C1 contract for system-internal use](../../abap-glossary/abenc1_contract_glosry.md). The function documentation is available in [Knowledge Transfer Documents](../../abap-glossary/abenktd_glosry.md) and can be accessed by clicking F2 in your IDE.

- `CALENDAR_OPERATION`

- `CALENDAR_SHIFT`

- `COLUMN_TOTAL`

- `CURRENT_TOTAL`

- `DEVIATION_RATIO`

- `EXPONENTIAL`

- `FISCAL_CALENDAR_OPERATION`

- `FISCAL_CALENDAR_SHIFT`

- `GET_CELL_REFERENCE_VALUE`

- `GRAND_TOTAL`

- `HRY_NODE_SIGN_VALUE`

- `LN`

- `LOG`

- `POWER`

- `RATIO_OF`

- `ROW_TOTAL`

- `SQRT`

## Restrictions

Analytical scalar functions cannot be used as operands in ABAP SQL.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the use of an analytical scalar function provided by SAP.

- The projected entity `DEMO_CDS_CUBE_VIEW` is a cube view.

- The provider contract is set to `ANALYTICAL_QUERY`.

- The analytical scalar function `RATIO_OF` is used in the element list to calculate the ratio of the final value of the field `amount_sum` compared to the original value. The final value subtracts a discount from the original value and adds taxes.

``` abap
@EndUserText.label: 'Analytical scalar function'
@AccessControl.authorizationCheck: #NOT_ALLOWED
define transient view entity DEMO_CDS_USE_ANA_SCALAR
  provider contract analytical_query
  as projection on DEMO_CDS_CUBE_VIEW
{
          @AnalyticsDetails.query.axis: #FREE
          so_key                as SalesOrderKey,

          @AnalyticsDetails.query.axis: #ROWS
          lifecycle_status      as LifecycleStatus,

          @AnalyticsDetails.query.axis: #ROWS
          created_on            as SellingDate,

          @AnalyticsDetails.query.axis: #COLUMNS
          amount_sum            as AmountSum,

          @AnalyticsDetails.query.axis: #COLUMNS
          $projection.AmountSum as DuplicatedAmountSum,

          @AnalyticsDetails.query.hidden: true
          currency_sum          as CurrencyOfAmount,

          @AnalyticsDetails.query.axis: #COLUMNS
          quantity_sum          as QuantitySum,

          @AnalyticsDetails.query.hidden: true
          uom_sum               as UnitOfQuantity,

          @Aggregation.default: #FORMULA
          abap.decfloat34'0.05' as Discount,

          @Aggregation.default: #FORMULA
          abap.decfloat34'1.19' as Tax,

          @Semantics.quantity.unitOfMeasure: 'AmPerQuanUnit'
          @Aggregation.default: #FORMULA
          curr_to_decfloat_amount( amount_sum )
                                     / $projection.QuantitySum
                                as AmountPerQuantity,

  virtual AmPerQuanUnit : abap.char(3),

          @Semantics.amount.currencyCode: 'CurrencyOfAmount'
          @Aggregation.default: #FORMULA
          curr_to_decfloat_amount( amount_sum )
            - ( curr_to_decfloat_amount( amount_sum )
            * $projection.Discount )
                                as AmountSumDiscounted,

          @Semantics.amount.currencyCode: 'CurrencyOfAmount'
          @Aggregation.default: #FORMULA
          $projection.AmountSumDiscounted * $projection.Tax
                                as AmountSumDiscountedTaxed,

          @Aggregation.default: #FORMULA
          ratio_of(
            portion => ( get_numeric_value( amount_sum )
                          - get_numeric_value( amount_sum )
                          * $projection.Discount ) * $projection.Tax,
            total   => get_numeric_value( amount_sum ) )
                                as AmountRatioFinalToOriginal
}
```
