---
title: "CDS DDL - CDS View Entity, aggr_expr"
source_file: abencds_aggregate_functions_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, aggr_expr

## Syntax

``` abap
... { MAX( [ALL|DISTINCT] arg ) 
    | MIN( [ALL|DISTINCT] arg ) 
    | AVG( [ALL|DISTINCT] arg AS dtype ) 
    | SUM( [ALL|DISTINCT] arg ) 
    | COUNT( DISTINCT arg ) 
    | COUNT(*) } ...  
```

[`AS dtype`](abencds_avg_as_v2.md)

## Description

[Aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). An aggregate expression calculates a single value from multiple rows of the operand `arg`. The operands can have any [data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) except for `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`. The following table shows the possible aggregate functions:

| **Aggregate Function** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Result Type**                                                                                                                              |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `MAX`                  | Returns the greatest value of `arg`                                                                                                                                                                                                                                                                                                                                                                                                                   | Data type of `arg`                                                                                                                           |
| `MIN`                  | Returns the least value of `arg`                                                                                                                                                                                                                                                                                                                                                                                                                      | Data type of `arg`                                                                                                                           |
| `AVG`                  | Average value of `arg`. Must be specified with the addition [`AS dtype`](abencds_avg_as_v2.md). The following data types are supported: [`INT1`, `INT2`, `INT4`, `INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`D16N`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`D34N`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). | Must be specified explicitly after [`AS`](abencds_avg_as_v2.md). Possible data types are `DEC`, `CURR`, `QUAN`, `D16N`,`D34N`, and `FLTP`. |
| `SUM`                  | Sum of `arg`. The following data types are supported: [`INT1`, `INT2`, `INT4`, `INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`D16N`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`D34N`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).                                                                                     | Data type of `arg`                                                                                                                           |
| `COUNT`                | If `DISTINCT arg` is specified, the number of distinct values of `arg` is counted; if `*` is specified, the number of rows in the result set is counted.                                                                                                                                                                                                                                                                                              | [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                                                                        |

If `ALL` is used, all rows in the result set are respected, which is the standard setting. If `DISTINCT` is used, only distinct values of `arg` are respected.

Null values:

- If an argument of an aggregate function has the [null value](../../abap-glossary/abennull_value_glosry.md), it is ignored when the function is evaluated. This also applies to `COUNT` with the addition `DISTINCT`: null values are not considered as a distinct value, and are not counted.

- The result of an aggregate function is a null value only if all the rows in the column in question contain a null value.

- The aggregate function `COUNT` counts rows and never produces the null value.

The following can be specified for `arg`:

- A [literal](abencds_literal_v2.md)

- A field of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity

- A [parameter](abencds_parameter_v2.md)

- A [session variable](abencds_session_variable_v2.md)

- A [path expression](abencds_path_expression_v2.md) that identifies a field of a data source [`data_source`](abencds_data_source_v2.md)

- A case distinction [`CASE`](abencds_case_expression_v2.md) that returns a value

- A cast expression

- Any built-in function that returns a suitable data type

- An [arithmetic expression](abencds_arithmetic_expression_v2.md)

- A [reuse expression](abencds_reusable_expression_v2.md) using `$projection`

The data type of the result is defined when the CDS view entity is activated. It depends on the aggregate function used and the value range of the data types of the operands. The result of aggregate function `AVG` must always be specified with the addition [`AS dtype`](abencds_avg_as_v2.md).

**Amounts and Quantities in Aggregate Expressions**

If the operand arg of an aggregate function is a [CDS amount field](../../abap-glossary/abencds_amount_field_glosry.md), a [CDS quantity field](../../abap-glossary/abencds_quantity_glosry.md), or a [CDS calculated quantity](../../abap-glossary/abencds_calculated_quantity_glosry.md), the result type might require a reference annotation as well. The following table shows the result type depending on the operand type of all available aggregate functions.

| **Aggregate Function**     | **Type of Operand**                   | **Result Type**       |
|----------------------------|---------------------------------------|-----------------------|
| `MAX`, `MIN`, `SUM`, `AVG` | amount                                | amount                |
| `MAX`, `MIN`, `SUM`, `AVG` | quantity                              | quantity              |
| `MAX`, `MIN`, `SUM`, `AVG` | calculated quantity                   | calculated quantity   |
| `COUNT`                    | amount, quantity, calculated quantity | number of type `INT4` |

Operand positions:

- Aggregate expressions can be used as [elements](abencds_select_list_entry_v2.md) of a [`SELECT` list](abencds_select_list_v2.md). There they need an alternative element name defined using `AS` and require a [`GROUP BY` clause](abencds_group_by_v2.md). The [`GROUP BY` clause](abencds_group_by_v2.md) must list all non-aggregated fields from the [`SELECT` list](abencds_select_list_v2.md).

- Aggregate expressions can be compared with [literals](abencds_literal_v2.md) in a [`HAVING` condition](abencds_having_clause_v2.md).

- Aggregate expressions can be used as operands in [built-in functions](abencds_builtin_functions_v2.md), [cast expressions](abencds_cast_expression_v2.md), or [case distinctions](abencds_case_expression_v2.md).

- An aggregate expression can be used in the condition `cds_cond` of a [complex case distinction](abencds_searched_case_expr_v2.md) as the operand `lhs` or as the operand `rhs` if a comparison operator is used as relational operator.

## Hints

- The aggregate expression `SUM` is calculated on the database. The database platform determines whether an overflow occurs if the result of `SUM` exceeds its value range.

  See also:

  - [SAP HANA SQL Reference Guide, `SUM` Function (Aggregate)](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/03958a1eb0ad4950b00dedd8fdda475a)

  - [SAP HANA SQL Reference Guide, Numerical Effects](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/4ee2f261e9c44003807d08ccc2e249ac)

- The names of the aggregate functions `AVG`, `COUNT`, `MAX`, `MIN`, and `SUM` are protected and cannot be used as user-defined names.

- It is possible to add aggregate expressions to the `SELECT` list of a CDS view entity by means of a CDS view entity extension (using [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md)). The following conditions must be met: The extended entity must explicitly allow aggregate expressions and the annotation [`AbapCatalog.viewEnhancementCategory[ ]`](abencds_view_entity_anno.md) must be set to `#PROJECTION_LIST` and `#GROUP_BY`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity demonstrates the usage of the aggregate expressions `AVG`, `SUM`, `MIN`, `MAX`, and `COUNT(*)`. An alternative element name is defined for each aggregation. The class `CL_DEMO_CDS_AGGREGATE_VE` fills the underlying database table, reads the view entity and returns the result.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_AGGREGATE_VE
  as select from demo_expressions
  {
    avg( abs(num1) as abap.dec(12,2)) as average_numeric_func7,
    sum( num1 )                       as sum_num1,
    min( num1 )                       as min_num1,
    max( num1 )                       as max_num1,
    count(*)                          as count1
  }
group by
  id
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Example for counting rows using `COUNT`. Field `count1` returns the result *1*, field `countNull` returns *0*. This demonstrates that `COUNT` with the addition `DISTINCT` ignores null values.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_AGGREGATES_VE
  as select from scarr
{
  count( distinct case carrid when 'LH' then 'LH' end ) as count1,

  count( distinct case carrid when 'XX' then 'LH' end ) as countNull
}
where
  carrid = 'LH'
```

The following code snippet accesses the CDS view entity with ABAP SQL and returns the result.

``` abap
SELECT * FROM demo_cds_aggregates_ve INTO TABLE @FINAL(result).
```
