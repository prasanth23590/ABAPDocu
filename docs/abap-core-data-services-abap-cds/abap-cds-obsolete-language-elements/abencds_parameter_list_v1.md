---
title: "CDS DDL - DDIC-Based View, parameter_list"
source_file: abencds_parameter_list_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, parameter_list

## Syntax

``` abap
... WITH PARAMETERS parameter1, parameter2, ...  
```

[`parameter1`](../abap-cds-data-definitions/abencds_f1_param.md) · [`parameter2`](../abap-cds-data-definitions/abencds_f1_param.md)

## Description

Defines [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) [`parameter1`](../abap-cds-data-definitions/abencds_f1_param.md), [`parameter2`](../abap-cds-data-definitions/abencds_f1_param.md), ... as input parameters of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) in a comma-separated list.

An input parameter called `pname` can be used as an operand in the following places in the [`SELECT`](abencds_select_statement_v1.md) statement of the view using the syntax [`:pname`](abencds_parameter_v1.md) or [`$parameters.pname`](abencds_parameter_v1.md):

- [Element](abencds_select_list_entry_v1.md) in the [`SELECT` list](abencds_select_list_v1.md)

- Operand of an [arithmetic expression](abencds_arithmetic_expression_v1.md)

- Operand `operand` directly after `case` in a [case distinction](abencds_case_expression_v1.md)

- [Right side](abencds_cond_expr_where_v1.md) of an expression [`cds_cond`](abencds_conditional_expression_v1.md) in a [`WHERE`](abencds_where_clause_v1.md) clause or [`HAVING` clause](abencds_having_clause_v1.md)

- [Right side](abencds_cond_expr_where_v1.md) of an expression [`cds_cond`](abencds_conditional_expression_v1.md) in an `ON` condition in an [ABAP join](abencds_joined_data_source_v1.md) or a [CDS association](abencds_association_v1.md)

- [Right side](abencds_cond_expr_where_v1.md) of an expression [`cds_cond`](abencds_conditional_expression_v1.md) in a [filter condition](abencds_path_expression_filter_v1.md) of a [path expression](abencds_path_expression_v1.md)

- [Right side](abencds_cond_expr_where_v1.md) of an expression [`cds_cond`](abencds_conditional_expression_v1.md) in the [default filter condition](abencds_association_v1.md) of a [CDS association](abencds_association_v1.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view has a list of three input parameters used in the [`WHERE` clause](abencds_where_clause_v1.md) of the `SELECT` statement. The ABAP class `CL_DEMO_CDS_PARAMETERS` accesses the view and assigns actual parameters to the input parameters.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@Metadata.allowExtensions
@EndUserText.label: 'Demo f&#x00FC;r Parameter-View'
define view entity demo_cds_parameters
  with parameters
    p_distance_l :s_distance,
    p_distance_u :s_distance,
    p_unit       :s_distid
  as select from spfli
{
  key carrid,
  key connid,
      cityfrom,
      cityto,
      distance,
      distid
}
where
      distid   = $parameters.p_unit
  and distance between $parameters.p_distance_l and $parameters.p_distance_u;
```
