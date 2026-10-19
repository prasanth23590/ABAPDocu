---
title: "CDS DDL - CDS View Entity, $projection"
source_file: abencds_reusable_expression_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, \$projection

## Syntax

``` abap
... $projection.reuse_exp ...  
```

## Description

`$projection.reuse_exp` reuses expressions defined in the `SELECT` list [`select_list`](abencds_select_list_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) in an operand position of the `SELECT` list of the same CDS view entity.

[Reuse expressions](../../abap-glossary/abencds_reuse_expression_glosry.md) can currently be used in the following operand positions:

- In the `SELECT` list as part of an expression.

- In the `ON` clause of an [CDS association](../../abap-glossary/abencds_association_glosry.md) (as described in topic [CDS DDL - CDS View Entity, `ASSOCIATION`](abencds_simple_association_v2.md).

The reused expression `reuse_exp` can contain the following operands or expressions:

- A [field](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity

- a [literal](abencds_literal_v2.md)

- An [arithmetic expression](abencds_arithmetic_expression_v2.md)

- A [cast expression](abencds_cast_expression_v2.md)

- A [built-in function](abencds_builtin_functions_v2.md)

- A [SQL-based scalar function](abencds_sql_scalar_function.md)

- A [case distinction](abencds_case_expression_v2.md)

- A [path expression](abencds_path_expression_v2.md)

## Restrictions

- Cycles must not occur and result in a syntax check error.

  The following represents a cycle and is not allowed. `... { a + $projection.z as x, 2 * $projection.x as y, b + $projection.y as z } ...`

  Explanation: element x uses z, which in turns uses y, which again uses x.

- Currently, reuse expressions **cannot** be used in the [`WHERE`](abencds_where_clause_v2.md), [`GROUP BY`](abencds_group_by_v2.md), or [`HAVING`](abencds_having_clause_v2.md) clause or within a [filter condition](abencds_path_expression_filter_v2.md).

- [Parameters](abencds_parameter_v2.md), [session variables](abencds_session_variable_v2.md), and [aggregate functions](abencds_aggregate_functions_v2.md) are currently **not** possible as part of the reuse expression. If you try to reuse such an element of the `SELECT` list, an error message occurs.

- If a field is specified as [CDS amount field](../abap-cds-data-types/abencds_amount_field.md) or [CDS quantity field](../abap-cds-data-types/abencds_quantity_field.md) by assigning a currency key or unit key, and if this field is reused in the same view with `$projection`, then the reference information is lost and the field is handled as normal numeric value.

  If a [calculated quantity](../abap-cds-data-types/abencds_calculated_quantity.md) is reused via `$projection`, the reference information is lost, but the characteristic as calculated quantity is kept. The required reference information needs to be assigned to the result.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reuse of expressions in a `SELECT` list.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, expression reuse'

define view entity DEMO_CDS_EXPRESSION_REUSE
  as select from demo_expressions
{

      //field
  key id                                     as field1,
      concat($projection.field1, 'x')        as field_reuse,

      //literal
      abap.char'hallo'                                as lit1,
      concat($projection.lit1, 'x')          as lit_reuse,

      //arithmetic expression
      abap.decfloat34'123.45E6'              as arith,
      $projection.arith * 2                  as arith_reuse,

      //cast expression
      cast(char1 as abap.numc(10))           as cast1,
      coalesce($projection.cast1, numc2)     as cast_reuse,

      //built-in function
      abs(dec1)                              as builtIn,
      cast($projection.builtIn as abap.int4) as builtIn_reuse,

      //case distinction
      case char2
          when 'Anna' then 'X'
          when 'Lisa' then 'Y'
          else '-'
          end                                as case1,
      left($projection.case1, 1)             as case_reuse
}
```
