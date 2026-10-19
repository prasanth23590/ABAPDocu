---
title: "CDS DDL - parameter_list, Analytical Query"
source_file: abencds_parameter_list_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - parameter_list, Analytical Query

## Syntax

``` abap
... WITH PARAMETERS parameter1, parameter2, ...  
```

[`parameter1`](abencds_f1_param.md) · [`parameter2`](abencds_f1_param.md)

## Description

Defines [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) [`parameter1`](abencds_f1_param.md), [`parameter2`](abencds_f1_param.md), ... as input parameters of a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md) in a comma-separated list.

An input parameter called `pname` can be accessed using the syntax `$parameters.pname`.

It can be used as an operand in the following places in the [`element_list`](abencds_element_list_apv.md) of the projection view:

- [Element](abencds_element_apv.md) in the [element list](abencds_element_list_apv.md). An [alias name](../../abap-glossary/abenalias_glosry.md) is mandatory.

- Operand of an [arithmetic expression](abencds_arithmetic_expression_v2.md). The parameter can have any of the numeric data types that are supported in arithmetic expressions (see [here](abencds_arithmetic_expression_v2.md)).

- Operand of a [cast expression](abencds_cast_expression_v2.md).

- Operand of a [case expression](abencds_case_expression_apv.md).

- Operand of a [built-in function](abencds_builtin_functions_v2.md), as long as it has a suitable data type.

- Operand of an expression `cds_cond` in a [`WHERE`](abencds_where_apv.md) clause.

**Caution**

Not more than one parameter can be annotated with `@Semantics.businessDate.At`, because the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md) currently supports only one temporal dependency.

**Parameter Passing**

How to pass values to input parameter is described in topic [CDS parameter passing](abencds_select_parameters_v2.md).

## Hint

``` abap
If the underlying projected entity requires parameters, you can pass them on using the following syntax: 
`DEFINE TRANSIENT VIEW ENTITY analytical_query 
  AS PROJECTION ON cds_entity ( parameter : $parameter.param )`
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS analytical projection view `DEMO_CDS_ANALYTIC_PARAMETER` defines an analytical query with an input parameter. The input parameter is used for a currency conversion. The projection view is based on the cube view `DEMO_CDS_CUBE_VIEW`.

``` abap
@EndUserText.label: 'analytical pv, parameter'
@AccessControl.authorizationCheck: #NOT_ALLOWED
define transient view entity DEMO_CDS_ANALYTIC_PARAMETER
  provider contract analytical_query
  with parameters
    p_targetCurrency : abap.cuky
  as projection on DEMO_CDS_CUBE_VIEW
{
  so_key,
  @Aggregation.default: #FORMULA
  @Semantics.amount.currencyCode: 'targetCurrency'
  currency_conversion(
    amount => amount_sum,
    source_currency => currency_sum,
    target_currency => $parameters.p_targetCurrency,
    exchange_rate_date => created_on
  )                            as convertedAmount,

  @Aggregation.default: #FORMULA
  $parameters.p_targetCurrency as targetCurrency
}
```
