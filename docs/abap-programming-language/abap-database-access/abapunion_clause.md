---
title: "UNION, INTERSECT, EXCEPT, query_clauses"
source_file: abapunion_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > UNION, INTERSECT, EXCEPT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UNION, INTERSECT, EXCEPT, query_clauses

## Syntax

``` abap
... { FROM source 
      FIELDS select_clause } 
  | { select_clause 
      FROM source } 
      [WHERE sql_cond] 
      [GROUP BY group] [HAVING group_cond] 
      [ORDER BY [UP TO n ROWS [OFFSET o]]] 
      [db_hints]  ...  
```

[`FROM`](abapfrom_clause.md) · [`FIELDS`](abapfields_clause.md) · [`select_clause`](abapselect_clause.md) · [`select_clause`](abapselect_clause.md) · [`FROM`](abapfrom_clause.md) · [`WHERE`](abapwhere.md) · [`sql_cond`](abenabap_sql_stmt_logexp.md) · [`GROUP BY`](abapgroupby_clause.md) · [`HAVING`](abaphaving_clause.md) · [`ORDER BY`](abaporderby_clause.md) · [`[UP TO n ROWS [OFFSET o]]`](abapselect_up_to_offset.html) · [`db_hints`](abenabap_sql_db_hints.md)

## Description

Possible [clauses and additions](abenselect_clauses.md) of [queries](../../abap-glossary/abenasql_query_glosry.md) whose result sets are joined using [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md). The result set of `SELECT` statements joined using `UNION`, `INTERSECT`, or `EXCEPT` is tabular and the [target area](abapinto_clause.md) must be used appropriately.

The following special conditions apply to clauses and additions of the `SELECT` statements joined using `UNION`, `INTERSECT`, or `EXCEPT`:

- The [`SELECT` list](abapselect_list.md) must consist of a list of specified columns [`col_spec`](abapselect_clause_col_spec.md) as [SQL expressions](abapsql_expr.md). `*` and `data_source~*` cannot be specified.

- All [`SELECT` lists](abapselect_list.md) of `SELECT` statements grouped using `UNION`, `INTERSECT`, or `EXCEPT` must have the same number of elements.

- The columns assigned to each other must have the same type properties with respect to [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), length, and number of digits after the decimal point, with the following exceptions:

  - Numeric types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) can create a column. The resulting column has the data type with the greatest value range.

  - Numeric types [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) can have different lengths but must have the same number of decimal places. The resulting column has the data type with the greatest length. The corresponding special types [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are handled here like [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

  - The numeric types [`DF16_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DF34_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are handled like the numbers of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) as they are stored, and the rule above applies with respect to lengths and decimal places.

  - Character-like types [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) can have different lengths. The resulting column has the data type with the greatest length. The corresponding special types [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are handled here like [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

    All other types must be exactly the same. This applies specifically to [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), where the lengths must match. The different categories of [strings](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_character_byte_types.md) cannot be combined either.

- The addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md) is not allowed in the [`WHERE`](abapwhere.md) conditions of the `SELECT` statements involved.

- An [`ORDER BY`](abaporderby_clause.md) clause cannot be specified for individual result sets. Instead, `ORDER BY` can be applied to the union, intersection, or difference result set of main queries.

The number of `SELECT` statements that can be joined using `UNION`, `INTERSECT`, or `EXCEPT` is not limited by a fixed value.

## Hints

- If required, the column names of the individual result sets can be modified using alias names after `AS`.

- If the column names of the result sets are not identical, the column names are used from the result set of the `SELECT` statement on the left of `UNION`, `INTERSECT`, or `EXCEPT`. In this type of case, the names are usually not visible, except for subqueries in the [`WITH`](abapwith.md) statement.

- The numeric types [`DF16_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DF34_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) can only be used together in a column if their decimal places match.

- SQL expressions, host expressions, and host variables can be used to synchronize the columns of the result set of the `SELECT` statements involved.

- Each of the joined `SELECT` statements has its own [client handling](../../abap-glossary/abenclient_handling_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creates the union set of three [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) on the same DDIC database table in a subquery of a [`WITH`](abapwith.md) statement. The union set is selected in a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md), which makes it possible to use a single `WHERE` condition for the entire result set in the main query of the `WITH` statement. If the union set were created in a main query, every single `SINGLE` statement would have to contain the same `WHERE` condition or `HAVING` condition.

``` abap
WITH +aggregates AS ( 
  SELECT FROM sflight 
         FIELDS carrid, 
                connid, 
                'MAX' AS function, 
                MAX( CAST( seatsocc AS DEC( 31,2 ) ) ) AS agg 
         GROUP BY carrid, connid 
    UNION 
      SELECT FROM sflight 
             FIELDS carrid, 
                    connid, 
                    'MIN' AS function, 
                    MIN( CAST( seatsocc AS DEC( 31,2 ) ) ) AS agg 
             GROUP BY carrid, connid 
        UNION 
          SELECT FROM sflight 
                 FIELDS carrid, 
                 connid, 'AVG' AS function, 
                 AVG( seatsocc AS DEC( 31,2 ) ) AS agg 
                 GROUP BY carrid, connid ) 
  SELECT * 
         FROM +aggregates 
         WHERE carrid = 'LH' AND connid = '0400' 
         INTO TABLE @FINAL(result).
```

## Executable Examples

- `UNION`

  - [Union of Different Tables](abenselect_union_abexa.md)

  - [Union with Aggregate Expression](abenselect_union_sum_abexa.md)

  - [Union with Global Temporary Table](abenselect_union_sum_gtt_abexa.md)

  - Union for Building a Ranges Table

  - [Union of CDS View Entity with Input Parameters](abenselect_union_cds_para_abexa.md)

- `INTERSECT`

  - [Intersection of Multiple Tables](abenselect_intersect_abexa.md)

  - [Intersection with Aggregate Expression](abenselect_intersect_max_abexa.md)

  - [Intersection with Global Temporary Table](abenselect_intersect_max_gtt_abexa.md)

  - [Intersection of CDS View Entity with Input Parameters](abenselect_inter_cds_para_abexa.md)

- `EXCEPT`

  - [Difference of Multiple Tables](abenselect_except_abexa.md)

  - [Difference with Aggregate Expression](abenselect_except_min_abexa.md)

  - [Difference with Global Temporary Table](abenselect_except_min_gtt_abexa.md)

  - [Difference of CDS View Entity with Input Parameters](abenselect_except_cds_para_abexa.md)
