---
title: "CDS DDL - DDIC-Based View, aggr_expr"
source_file: abencds_aggregate_functions_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, aggr_expr

## Syntax

``` abap
... { MAX( [ALL|DISTINCT] arg ) 
    | MIN( [ALL|DISTINCT] arg ) 
    | AVG( [ALL|DISTINCT] arg [AS dtype] ) 
    | SUM( [ALL|DISTINCT] arg ) 
    | COUNT( DISTINCT arg ) 
    | COUNT(*) } ...  
```

[`[AS dtype]`](abencds_avg_as_v1.md)

## Description

Aggregate expression in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). An aggregate expression calculates a single value from an operand `arg` by calling an aggregate function from multiple rows of a result set. The operands can have any [data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) except `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`. The following table shows the possible aggregate functions:

| **Aggregate Function** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Result Type**                                                                                                 |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `MAX`                  | Greatest value of `arg`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Data type of `arg`                                                                                              |
| `MIN`                  | Least value of `arg`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Data type of `arg`                                                                                              |
| `AVG`                  | Average value of `arg` (`arg` must be numeric). Type [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is only supported with addition [`AS dtype`](abencds_avg_as_v1.md). The types [`DF16_...`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF34_...`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) for decimal free floating numbers are not supported. The types [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UTCL`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not supported either. | , [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), platform-dependent interim result or [`dtype`](abencds_avg_as_v1.md) |
| `SUM`                  | Sum of `arg` (`arg` must be numeric). The types [`DF16_...`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DF34_...`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) for decimal free floating numbers are not supported. The types [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UTCL`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not supported either.                                                                                                                            | Data type of `arg`                                                                                              |
| `COUNT`                | If `DISTINCT arg` is specified, the number of distinct values of `arg` is counted; if `*` is specified, the number of rows in the result set is counted.                                                                                                                                                                                                                                                                                                                         | [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)                                                                           |

If `ALL` is used, all rows in the result set are respected, which is the standard setting. If `DISTINCT` is used, only distinct values of `arg` are respected.

The following can be specified for `arg`:

- A [literal](abencds_literal_v1.md)

- A field of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view

- A [path expression](abencds_path_expression_v1.md) that identifies a field of a data source [`data_source`](abencds_data_source_v1.md)

- A case distinction [`CASE`](abencds_case_expression_v1.md) that returns a value

The data type of the result is defined when the CDS view is activated and is determined by the aggregate function and the value range of the data types of the operands. If the result of aggregate function `AVG` is returned in a result set, the result type is `FLTP`. As the interim result in a clause, the result type can be platform-dependent. With addition [`AS dtype`](abencds_avg_as_v1.md), the result type can be defined for every operand position.

Aggregate expressions can be used as [elements](abencds_select_list_entry_v1.md) of a [`SELECT` list](abencds_select_list_v1.md). Here they need an alternative element name defined using `AS` and require a [`GROUP BY` clause](abencds_group_by_v1.md) to be used. Aggregate expressions can be compared with [literals](abencds_literal_v1.md) in a [`HAVING` condition](abencds_having_clause_v1.md).

## Hints

- The aggregate expression `SUM` is calculated on the database. The database platform determines whether an overflow occurs if the result of an aggregate expression exceeds its value range.

  See also:

  - [SAP HANA SQL Reference Guide, `SUM` Function (Aggregate)](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/03958a1eb0ad4950b00dedd8fdda475a)

  - [SAP HANA SQL Reference Guide, Numerical Effects](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/4ee2f261e9c44003807d08ccc2e249ac)

- The names of the aggregate functions `AVG`, `COUNT`, `MAX`, `MIN`, and `SUM` are protected and cannot be used as user-defined names.

- To add aggregate expressions in the `SELECT` list to a CDS view using [`EXTEND VIEW`](../abap-cds-data-definitions/abencds_extend_view.md), the values `#PROJECTION_LIST` and `#GROUP_BY` must be specified with the annotation [`AbapCatalog.viewEnhancementCategory[ ]`](abencds_view_anno_v1.md).

- The result of the aggregate functions `AVG` in data type `FLTP` is platform-dependent.

- When using `count(*)` on a [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) table which has no entries, then no result is returned. The expected behavior would be that a '0' is returned, but instead, the result field remains empty (it also does not contain the [null value](../../abap-glossary/abennull_value_glosry.md)).

  `count(*)` on an empty, [client-independent](../../abap-glossary/abenclient_dependent_glosry.md) table returns '0', as expected.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the `SELECT` list of the CDS view `sales_order`, aggregate expressions calculate the sum, the minimum, and the maximum of the gross amounts of each business partner. Also, the number of requests is determined. An alternative element name is defined for each aggregation. The non-aggregated fields `buyer_guid` and `currency_code` are specified in the `GROUP BY` clause.

``` abap
@AbapCatalog.sqlViewName: 'SALES_ORDER_VW' 
define view sales_order as 
  select from snwd_so 
  { key buyer_guid, 
       @Semantics.currencyCode 
        currency_code, 
       @Semantics.amount.currencyCode: 'currency_code' 
        sum(gross_amount) as sum_gross_amount, 
       @Semantics.amount.currencyCode: 'currency_code' 
        min(gross_amount) as min_gross_amount, 
       @Semantics.amount.currencyCode: 'currency_code' 
        max(gross_amount) as max_gross_amount, 
       @Semantics.amount.currencyCode: 'currency_code' 
        avg(gross_amount) as avg_gross_amount, 
        count(*) as sales_orders_count } 
  group by buyer_guid, currency_code
```
