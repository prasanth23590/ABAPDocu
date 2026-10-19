---
title: "UNION, INTERSECT, EXCEPT"
source_file: abapunion.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UNION, INTERSECT, EXCEPT

## Syntax Forms

**`UNION`, `INTERSECT`, and `EXCEPT` in Main Queries**

``` abap
1. [WITH ...] 
  SELECT query_clauses 
    {UNION [ALL|DISTINCT]} 
  | {INTERSECT [DISTINCT]} 
  | {EXCEPT [DISTINCT]} 
     [(] SELECT query_clauses [)] 
    [{UNION [ALL|DISTINCT]} 
   | {INTERSECT [DISTINCT]} 
   | {EXCEPT [DISTINCT]} 
    ...] 
        [ORDER BY sort_key] 
         INTO|APPENDING target 
        [OPTIONS ...]. 
  ... 
 
  [ENDSELECT|ENDWITH.] 
 
 
2. OPEN CURSOR ... FOR 
    [WITH ...] 
    SELECT query_clauses 
     {UNION [ALL|DISTINCT]} 
   | {INTERSECT [DISTINCT]} 
   | {EXCEPT [DISTINCT]} 
       [(] SELECT query_clauses [)] 
      [{UNION [ALL|DISTINCT]} 
     | {INTERSECT [DISTINCT]} 
     | {EXCEPT [DISTINCT]} 
      ...] 
          [ORDER BY sort_key] 
          [OPTIONS ...].
```

**`UNION`, `INTERSECT`, and `EXCEPT` in Subqueries**

``` abap
3. ... ( SELECT query_clauses 
          {UNION [ALL|DISTINCT]} 
        | {INTERSECT [DISTINCT]} 
        | {EXCEPT [DISTINCT]} 
           [(] SELECT query_clauses [)] 
          [{UNION [ALL|DISTINCT]} 
         | {INTERSECT [DISTINCT]} 
         | {EXCEPT [DISTINCT]} 
          ...] ) ...
```

[`WITH ...`](abapwith.md) · [`query_clauses`](abapunion_clause.md) · [`query_clauses`](abapunion_clause.md) · [`ORDER BY`](abaporderby_clause.md) · [`INTO|APPENDING`](abapinto_clause.md) · [`OPTIONS ...`](abapselect_options.md) · [`ENDSELECT`](abapendselect.md) · [`ENDWITH`](abapendwith.md) · [`WITH ...`](abapwith.md) · [`query_clauses`](abapunion_clause.md) · [`query_clauses`](abapunion_clause.md) · [`ORDER BY`](abaporderby_clause.md) · [`OPTIONS ...`](abapselect_options.md) · [`query_clauses`](abapunion_clause.md) · [`query_clauses`](abapunion_clause.md)

### Variant

[1. `... UNION ...`](abapunion.md#variant-1)

[2. `... INTERSECT ...`](abapunion.md#variant-2)

[3. `... EXCEPT ...`](abapunion.md#variant-3)

### Addition

[`... ALL|DISTINCT`](abapunion.md#addition)

## Overview

### Description

The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) `UNION`, `INTERSECT`, and `EXCEPT` merge the result sets of multiple queries into a single result set. The syntax forms show where `UNION`, `INTERSECT`, and `EXCEPT` can be used:

1.  For creating the result set of the [main query](../../abap-glossary/abenmainquery_glosry.md) of a standalone statement, which is introduced using [`WITH`](abapwith.md) or [`SELECT`](abapselect.md).

2.  For creating the result set of the [main query](../../abap-glossary/abenmainquery_glosry.md) after `OPEN CURSOR`.

3.  For creating the result set of a parenthesized [subquery](../../abap-glossary/abensubquery_glosry.md) in a [relational expression](abenabap_sql_stmt_logexp.md), the definition of a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) after [`WITH`](abapwith.md), or an [`INSERT`](abapinsert_dbtab.md) statement.

In all syntax forms, it is possible to specify the same [clauses and additions](abenselect_clauses.md), specifically [`query_clauses`](abapunion_clause.md), for `SELECT` statements of queries in front of and after `UNION`, `INTERSECT`, or `EXCEPT` for defining result sets. A query on the right side of `UNION`, `INTERSECT`, or `EXCEPT` can be enclosed in parentheses `( )`. A pair of parentheses can include multiple unions, intersections, or differences. The queries joined with `UNION`, `INTERSECT`, or `EXCEPT` are evaluated from left to right. Specific statements can be prioritized using parentheses.

In the case of a standalone [`SELECT`](abapselect.md) or [`WITH`](abapwith.md) statement and after `OPEN CURSOR`, the [`ORDER BY`](abaporderby_clause.md) and the additions [`OPTIONS`](abapselect_options.md) after the last query or after the position of the last closing bracket are listed and affect the merged result set. In the case of standalone statements, the [`INTO`](abapinto_clause.md) clause is to be listed as the last clause and in front of the additions [`OPTIONS`](abapselect_options.md). The following special features apply to standalone statements with set operators:

- `ORDER BY` clause

  - The addition [`ORDER BY PRIMARY KEY`](abaporderby_clause.md) is not allowed.

  - Columns of the merged result set specified after [`ORDER BY`](abaporderby_clause.md) must occur with the same name in all relevant `SELECT` statements. The names must be specified directly and cannot be specified with the [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~` after a column name.

- `INTO` clause

  - If the addition `CORRESPONDING` or an inline declaration `@DATA|@FINAL(...)` is used in the [`INTO`](abapinto_clause.md) clause, the column names of all result sets defined in the [`query_clauses`](abapunion_clause.md) from left to right must match.

  - The merged result set is always multirow. When assigning to a non-table target area, that is, a `SELECT` statement without the addition [`INTO|APPENDING ... TABLE`](abapinto_clause.md), a loop to be terminated with [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md) is always opened.

- Restricting the result set

  - The additions [`UP TO`](abapselect_up_to_offset.md) and [`OFFSET`](abapselect_up_to_offset.md) are not currently allowed with `UNION`, `INTERSECT`, and `EXCEPT`.

  - Since the result set is tabular, [`SINGLE`](abapselect_single.md) cannot be used.

### Hints

- Prioritizations using parentheses are particularly applicable when handling duplicate rows using `DISTINCT`.

- `UNION`, `INTERSECT`, or `EXCEPT` cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

- The maximum number of different `SELECT` statements that can be joined using `UNION`, `INTERSECT`, or `EXCEPT` depends on the database system. If this number is exceeded, an exception is raised when the program is executed.

## Variant 1

`... UNION ...`

### Description

The ABAP SQL set operator `UNION` merges the result sets of two [queries](../../abap-glossary/abenasql_query_glosry.md). The rows of the result set of the query after `UNION` are inserted into the result set of the query in front of `UNION`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creates the union of one row from the DDIC database table `SCARR` with multiple rows from the DDIC database table `SPFLI`. Those columns that do not exist in the other table are replaced by literals. Here, a [`CAST`](abensql_cast.md) is required for the column `CONNID`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT FROM scarr 
       FIELDS carrname, 
              CAST( '-' AS CHAR( 4 ) ) AS connid, 
              '-' AS cityfrom, 
              '-' AS cityto 
       WHERE carrid = 'LH' 
  UNION 
    SELECT FROM spfli 
           FIELDS '-' AS carrname, 
                  CAST( connid AS CHAR( 4 ) ) AS connid, 
                  cityfrom, 
                  cityto 
           WHERE carrid = 'LH' 
   ORDER BY carrname DESCENDING, connid, cityfrom, cityto 
   INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Executable Examples

[`UNION` - Examples](abenunion_abexas.md)

## Variant 2

`... INTERSECT ...`

### Description

The ABAP SQL set operator `INTERSECT` returns all distinct rows of the result set of the query in front of `INTERSECT` that are also present in the result set of the query after `INTERSECT`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creates the intersect of multiple rows from a joined table with multiple rows from the DDIC database table `SCARR`.

``` abap
SELECT spfli~carrid, scarr~carrname 
  FROM spfli 
    INNER JOIN scarr ON scarr~carrid = spfli~carrid 
  INTERSECT 
    SELECT carrid, carrname 
      FROM scarr 
  ORDER BY carrid ASCENDING, carrname 
  INTO TABLE @FINAL(result).
```

## Executable Examples

[`INTERSECT` - Examples](abenintersect_abexas.md)

## Variant 3

`... EXCEPT ...`

### Description

The ABAP SQL set operator `EXCEPT` returns all distinct rows of the result set of the query in front of `EXCEPT` that are not present in the result set of the query after `EXCEPT`.

### Hints

- ABAP SQL does not support the alternative syntax `MINUS` that is available for the SAP HANA database.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Selects all airline codes and airline names from the DDIC database table `SCARR` that do not exist in the DDIC database table `SPFLI`.

``` abap
SELECT carrid, carrname 
  FROM scarr 
    EXCEPT 
      SELECT spfli~carrid, scarr~carrname 
        FROM spfli 
          INNER JOIN scarr ON scarr~carrid = spfli~carrid 
  ORDER BY carrid ASCENDING, carrname 
  INTO TABLE @FINAL(result).
```

## Executable Examples

[`EXCEPT` - Examples](abenexcept_abexas.md)

## Addition

`... ALL|DISTINCT`

### Description

The additions `ALL` and `DISTINCT` control how duplicate rows are handled. `DISTINCT` is the default here:

- If the addition `ALL` is specified, all rows from the result set of the right `SELECT` statement are inserted into the existing result set.

- If the addition `DISTINCT` is specified or if neither of the two additions is specified, the behavior is as follows:

  - First, all rows of the result set of the right `SELECT` statement are inserted into the existing result set.

  - Then all rows that occur more than once are deleted except for one. For determining the duplicate rows, all columns of the result set are respected.

### Hints

- The default behavior or the addition `DISTINCT` is always applied to the entire existing result set of the left side. The addition `DISTINCT` also removes any duplicate rows produced by the addition `ALL` of preceding `UNION` additions.

- The ABAP SQL set operator `UNION` can be used together with the addition `ALL` or `DISTINCT`.

- The ABAP SQL set operators `INTERSECT` and `EXCEPT` can be used together with the addition `DISTINCT`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The DDIC database table `DEMO_EXPRESSIONS` is filled with one row and the union of the table with itself is created. Using the addition `DISTINCT`, the result set contains one row and using the addition `ALL` it contains two rows.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( id = 'X' num1 = 111 ) ). 
 
SELECT id, num1 
       FROM demo_expressions 
  UNION DISTINCT 
      SELECT id, num1 
      FROM demo_expressions 
  INTO TABLE @FINAL(result1). 
 
SELECT id, num1 
       FROM demo_expressions 
  UNION ALL 
      SELECT id, num1 
      FROM demo_expressions 
  INTO TABLE @FINAL(result2). 
 
ASSERT lines( result1 ) = 1. 
ASSERT lines( result2 ) = 2.
```
