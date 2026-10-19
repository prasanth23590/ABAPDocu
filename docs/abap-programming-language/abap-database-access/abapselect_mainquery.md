---
title: "SELECT, mainquery_clauses"
source_file: abapselect_mainquery.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, mainquery_clauses

## Syntax

``` abap
... [SINGLE [FOR UPDATE]] 
    { FROM source 
      FIELDS select_clause } 
  | { select_clause 
      FROM source } 
    [[FOR ALL ENTRIES IN itab] 
      WHERE sql_cond] 
    [GROUP BY group] [HAVING group_cond] 
    [ORDER BY sort_key] 
    [db_hints]  ...  
```

[`SINGLE [FOR UPDATE]`](abapselect_single.md) · [`FROM`](abapfrom_clause.md) · [`FIELDS`](abapfields_clause.md) · [`select_clause`](abapselect_clause.md) · [`select_clause`](abapselect_clause.md) · [`FROM`](abapfrom_clause.md) · [`FOR ALL ENTRIES IN`](abenwhere_all_entries.md) · [`WHERE`](abapwhere.md) · [`GROUP BY`](abapgroupby_clause.md) · [`HAVING`](abaphaving_clause.md) · [`ORDER BY`](abaporderby_clause.md) · [`db_hints`](abenabap_sql_db_hints.md)

## Description

Possible [clauses and additions](abenselect_clauses.md) of a [main query](../../abap-glossary/abenmainquery_glosry.md) represented by a standalone [`SELECT`](abapselect.md) statement. The clauses and additions define the result set of the `SELECT` statement:

- Rows of the result set

  - Multirow result set

    If `SINGLE` is not specified and if [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) are not exclusively specified in the [`SELECT` list](abapselect_list.md) of the `SELECT` clause [`select_clause`](abapselect_clause.md), the result set is multirow or tabular by default. All database rows that are selected by the remaining additions of the statement `SELECT` are included in the result set. If the addition [`ORDER BY`](abaporderby_clause.md) is not used, the order of the rows in the result set is not defined and can be different if the same statement `SELECT` is executed multiple times. A data object specified after [`INTO`](abapinto_clause.md) can be an internal table and the addition [`APPENDING`](abapinto_clause.md) can be used. If no internal table is specified after `INTO` or `APPENDING`, the statement `SELECT` for multirow result sets initiates a loop that must be closed using `ENDSELECT`.

  - Single row result set

    The optional addition [`SINGLE`](abapselect_single.md) defines a single-row result set that can be protected against parallel changes by another program. When using `SINGLE`, it is not possible to specify an internal table as the target object, and the addition `SINGLE` cannot be combined with all additions of the `SELECT` statement.

- Columns of the result set

  The `SELECT` clause [`select_clause`](abapselect_clause.md) defines the structure of the result set. It consists mainly of a [`SELECT` list](abapselect_list.md) that defines the columns of the result set. Optionally, duplicate rows can be excluded.

- Data Sources

  The [`FROM`](abapfrom_clause.md) clause specifies [data sources](abapselect_data_source.md) `source` from which data is read. These can either be data sources in the database accessed by the current query or they can be [internal tables](abapselect_itab.md). Data sources in the database must be defined in the ABAP Dictionary.

- Conditions

  The result set can be restricted using the [`WHERE`](abapwhere.md) clause. The optional addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md) can be used to compare the content of a column on the database with a component with all rows of a structured internal table `itab`.

- Grouping

  The [`GROUP BY`](abapgroupby_clause.md) clause merges multiple database rows into one row of the result set. The [`HAVING`](abaphaving_clause.md) clause restricts the merged rows.

- Database Hints

  [`db_hints`](abenabap_sql_db_hints.md) can be used to specify [database hints](../../abap-glossary/abendatabase_hint_glosry.md).

- Sorting

  The [`ORDER BY`](abaporderby_clause.md) clause sorts the result set. If `ORDER BY` is not specified, the order of the rows in the result set is undefined.

The `SELECT` clause [`select_clause`](abapselect_clause.md) can be specified before or after the [`FROM` clause](abapfrom_clause.md). After the `FROM` clause, the `SELECT` clause must be prefixed with the addition `FIELDS`.

## Hints

- Although the `WHERE` condition is optional, it should always be specified for performance reasons. In most cases, the result should already be restricted by the database system and not only on the application server.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

[`SELECT`](abapselect.md) statement with all possible clauses.

``` abap
SELECT FROM sflight 
       FIELDS carrid, 
              connid, 
              SUM( seatsocc ) AS seatsocc 
       WHERE carrid = 'LH' 
       GROUP BY carrid, connid 
       HAVING SUM( seatsocc ) > 1000 
       ORDER BY carrid, connid 
       INTO TABLE @FINAL(result).
```
