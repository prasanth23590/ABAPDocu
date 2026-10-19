---
title: "SELECT, WHERE"
source_file: abapwhere.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, WHERE

## Syntax

``` abap
... WHERE sql_cond ...  
```

[`sql_cond`](abenasql_cond.md)

## Description

The addition `WHERE` restricts the number of rows that are included in the result set by the statement `SELECT` of a [query](../../abap-glossary/abenasql_query_glosry.md) by using a logical expression [`sql_cond`](abenabap_sql_stmt_logexp.md). A row is only included in the result set if the logical expression is true.

Except for columns of type `STRING`, `RAWSTRING`, or `GEOM_EWKB`, or `LCHR` and `LRAW`, all columns of the [data sources](abapselect_data_source.md) specified after [`FROM`](abapfrom_clause.md) can usually be evaluated in the `WHERE` condition of a [query](../../abap-glossary/abenasql_query_glosry.md). Special rules apply to some logical expressions. The columns do not necessarily have to be a part of the result set.

[Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies to the `WHERE` clause. The [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent data source cannot be used as an operand in the `WHERE` condition.

## Hints

- If the data source is accessed using generic [table buffering](../../abap-glossary/abentable_buffering_glosry.md), the buffered area must be specified completely in the `WHERE` condition, otherwise buffering is bypassed.

- If the data sources are accessed using single record buffering, the conditions combined using `AND` in the `WHERE` condition must be specified for all key fields of the primary key, otherwise buffering is bypassed.

- For frequently used `SELECT` statements with an identical `WHERE` condition, it can be useful to create an [index](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_index.md). In `WHERE` conditions, the fields of the index should be expressed as equality comparisons and combined using the `AND` operator. All the fields of an index that are behind a field, for which a comparison other than `=` or `EQ` is specified in the `WHERE` clause, cannot be used for searching in the index.

- It is currently not possible to use [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) as operands in a `WHERE` condition. This is only possible in the [`HAVING`](abaphaving_clause.md) clause.

- If one of the columns involved in the logical expression [`sql_cond`](abenabap_sql_stmt_logexp.md) contains the [null value](../../abap-glossary/abennull_value_glosry.md), its result is unknown, and no row is included in the result set.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of all objects in the ABAP keyword documentation from the table `DOKIL` using a suitable `WHERE` condition. Messages of the code inspector regarding the bypassing of the table buffer are suppressed using [pseudo comments](../../abap-glossary/abenpseudo_comment_glosry.md).

``` abap
SELECT FROM dokil 
       FIELDS object, langu 
       WHERE  id = 'SD'  AND 
              typ = 'E'  AND 
                   ( object LIKE 'ABAP%'    OR 
                     object LIKE 'ABEN%'    OR 
                     object LIKE 'DYNP%'  ) AND 
                     ( langu = 'D' OR langu = 'E' ) "#EC CI_GENBUFF 
      ORDER BY object, langu                        "#EC CI_BYPASS 
      INTO TABLE @FINAL(dokil_tab).
```

## Executable Examples

- [Host Expressions in the `WHERE` Condition](abenhost_expr_in_where_cond_abexa.md)

- [SQL Expressions in the `WHERE` Condition](abensql_expr_in_where_cond_abexa.md)
