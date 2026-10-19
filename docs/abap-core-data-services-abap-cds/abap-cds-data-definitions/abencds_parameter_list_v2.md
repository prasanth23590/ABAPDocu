---
title: "CDS DDL - CDS View Entity, parameter_list"
source_file: abencds_parameter_list_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, parameter_list

## Syntax

``` abap
... WITH PARAMETERS parameter1, parameter2, ...  
```

[`parameter1`](abencds_f1_param.md) · [`parameter2`](abencds_f1_param.md)

## Description

Defines [CDS parameters](../../abap-glossary/abencds_parameter_glosry.md) [`parameter1`](abencds_f1_param.md), [`parameter2`](abencds_f1_param.md), ... as input parameters of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) in a comma-separated list.

An input parameter called `pname` can be accessed using the syntax `$parameters.pname`.

A parameter must be typed with an elementary data type. All data types listed in topic [`Typing`](abencds_typing.md) are allowed, except for `abap.accp`, `abap.geom_ewkb`, and `abap.rawstring`.

It can be used as an operand in the following places in the [`SELECT`](abencds_select_statement_v2.md) statement of the view entity:

- [Element](abencds_select_list_entry_v2.md) in the [`SELECT` list](abencds_select_list_v2.md). An [alias name](../../abap-glossary/abenalias_glosry.md) is mandatory.

- Operand of an [arithmetic expression](abencds_arithmetic_expression_v2.md). The parameter can have any of the numeric data types that are supported in arithmetic expressions in `SELECT` statements (see [here](abencds_arithmetic_expression_v2.md)).

- Operand of an [aggregate expression](abencds_aggregate_functions_v2.md). The parameter can have any of the data types that are supported in aggregate expressions in `SELECT` statements.

- Operand of a [case distinction](abencds_case_expression_v2.md).

- Operand of a [cast expression](abencds_cast_expression_v2.md).

- Operand of a [built-in function](abencds_builtin_functions_v2.md), as long as it has a suitable data type.

- Right side of an expression [`cds_cond`](abencds_conditional_expression_v2.md) in a [`WHERE`](abencds_where_clause_v2.md) clause or [`HAVING` clause](abencds_having_clause_v2.md)

- Right side of an expression [`cds_cond`](abencds_conditional_expression_v2.md) in an `ON` condition in an [ABAP join](abencds_joined_data_source_v2.md) or a [CDS association](abencds_association_v2.md)

- Right side of an expression [`cds_cond`](abencds_conditional_expression_v2.md) in a [filter condition](abencds_path_expression_filter_v2.md) of a [path expression](abencds_path_expression_v2.md)

- Right side of an expression [`cds_cond`](abencds_conditional_expression_v2.md) in the [default filter condition](abencds_simple_association_v2.md) of a [CDS association](abencds_association_v2.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity has a list of three input parameters used in the [`WHERE` clause](abencds_where_clause_v2.md) of the `SELECT` statement. For information about passing actual parameters in a `SELECT` statement in ABAP, see the executable example [`SELECT`, CDS View Entity with Input Parameters](../../abap-programming-language/abap-database-access/abenselect_cds_para_abexa.md).

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'View Entity with Input Parameters'
define view entity Demo_Cds_Param_View_Entity 
   with parameters
    p_distance_l :s_distance,
    p_distance_u :s_distance,
    p_unit       :s_distid
  as select from
    spfli
    {
      key carrid,
      key connid,
          cityfrom,
          cityto,
          distance,
          distid          
    }
    where
          distid   =       $parameters.p_unit
      and distance between $parameters.p_distance_l 
                       and $parameters.p_distance_u;        
```
