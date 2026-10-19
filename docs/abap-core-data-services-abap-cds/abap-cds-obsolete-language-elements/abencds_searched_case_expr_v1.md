---
title: "CDS DDL - DDIC-Based View, searched_case_expr"
source_file: abencds_searched_case_expr_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, case_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, searched_case_expr

## Syntax

``` abap
... CASE WHEN cds_cond1 THEN result1 
        [WHEN cds_cond2 THEN result2] 
        [WHEN cds_cond3 THEN result3] 
          ... 
        [ELSE resultn] 
    END ...  
```

[`cds_cond1`](abencds_conditional_expression_v1.md) · [`cds_cond2`](abencds_conditional_expression_v1.md) · [`cds_cond3`](abencds_conditional_expression_v1.md)

## Description

Complex [case distinction](abencds_case_expression_v1.md) (searched case) in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The case distinction evaluates the conditions [`cds_cond1`](abencds_conditional_expression_v1.md), [`cds_cond2`](abencds_conditional_expression_v1.md), ... and returns the operand `result` as the result after the first `THEN` for which the condition is true. If none of the conditions are true, the `result` specified after `ELSE` is selected. If `ELSE` is not specified, the result is the [null value](../../abap-glossary/abennull_value_glosry.md). For the operands, [general](abencds_cond_expr_operands_v1.md) and [special rules](abencds_cond_expr_case_v1.md) apply when specifying the conditions. The same applies to `result1`, `result2`, ... as to [simple case distinction](abencds_simple_case_expression_v1.md).

## Hints

- The SQL standard specifies the result of a case distinction, but not the order in which the operands are evaluated. Potentially, the result may even be evaluated before the associated condition. This means that any expressions specified as operands must have no side effects and must not be dependent on each other.

- On the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), operands are evaluated in parallel for reasons of optimization. The order in which the operands are evaluated is undefined. If an exception is raised when an operand is evaluated, the entire case distinction is canceled. In this case, it does not matter which conditions apply and the order in which they are listed. For this reason, it is advisable not to use any exceptions in expressions specified as operands. For more information, see the [HANA-specific SQL documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view has a complex case distinction in the `SELECT` list.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_SCASE'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_searched_case
  as select from
    spfli
    {
      key carrid,
      key connid,
          distance,
          distid,
          case
            when distance >= 2000 then 'long-haul flight'
            when distance >= 1000 and
                 distance <  2000 then 'medium-haul flight'
            when distance <  1000 then 'short-haul flight'
                                  else 'error'
          end as flight_type
    }
    where
      distid = 'MI'
```

The class `CL_DEMO_CDS_SEARCHED_CASE` uses [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) to access the view and shows the result.
