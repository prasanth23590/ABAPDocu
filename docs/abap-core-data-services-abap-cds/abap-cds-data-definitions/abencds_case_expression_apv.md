---
title: "CDS DDL - case_expr, Analytical Query"
source_file: abencds_case_expression_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Analytical Queries > CDS DDL - element_list, Analytical Query > CDS DDL - element, Analytical Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - case_expr, Analytical Query

## Syntax Forms

**[Selection-Related Case Expression (Restricted Measure)](abencds_sel_case_expression_apv.md)**

``` abap
1. ... CASE 
        WHEN cds_cond 
        THEN result 
       [ELSE NULL] 
      END ...
```

**[Formula-Related Case Expression](abencds_for_case_expression_apv.md)**

``` abap
2.  @Aggregation.default: #FORMULA 
   CASE 
     WHEN cds_cond 
     THEN result1 
     ELSE {result2 | NULL} 
   END ...
```

[`cds_cond`](abencds_conditional_expression_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md)

## Description

[Case distinction](../../abap-glossary/abencase_distinction_glosry.md) in the [element list](abencds_element_list_apv.md) of an analytical query. Either a selection-related case expression (restricted measure) or a formula-related case expression.

- In a selection-related case expression (restricted measure), the field in the `WHEN` clause must be an [analytical dimension field](../../abap-glossary/abencds_dimension_glosry.md).

- In a formula-related case expression, the field in the `WHEN` clause must be an [analytical measure field](../../abap-glossary/abencds_measure_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS analytical projection view `DEMO_CDS_ANALYTIC_CASE` defines an analytical query. It is based on the cube view `DEMO_CDS_CUBE_VIEW`. The projection view defines one selection-related case expression and one formula-related case expression.

``` abap
@AccessControl.authorizationCheck: #NOT_ALLOWED
define transient view entity DEMO_CDS_ANALYTIC_CASE
  provider contract analytical_query
  as projection on DEMO_CDS_CUBE_VIEW
{
  so_key,

  currency_sum,

  //selection-related case expression
  @Semantics.amount.currencyCode: 'currency_sum'
  case when lifecycle_status between 'A' and 'B'
  then amount_sum else null end as QuantityAB,

  ////formula-related case expression
  @Aggregation.default: #FORMULA
  //  case
  //  when created_on = $session.system_date
  //  then abap.int8'200'
  //  else abap.int8'700'
  //  end                 as formula_demo

  case
  when amount_sum is initial
  then abap.int8'200'
  else abap.int8'700'
  end                           as formula_demo
}
where
  created_on = $session.system_date
```
