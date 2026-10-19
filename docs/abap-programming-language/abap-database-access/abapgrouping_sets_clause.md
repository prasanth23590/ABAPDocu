---
title: "SELECT, GROUP BY, grouping_sets"
source_file: abapgrouping_sets_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, GROUP BY, grouping_sets

## Syntax

``` abap
... GROUPING SETS ( ( { } 
                    | { sql_exp1, sql_exp2, ... } ), 
                    ( { } 
                    | { sql_exp1, sql_exp2, ... } ), ... ) ...  
```

[`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md)

## Description

`GROUPING SETS` is an addition of the `GROUP BY` clause that allows the definition of multiple grouping sets under a `GROUP BY` clause. The grouping sets are aggregated separately and grouped in a result set.

The [`GROUP BY`](abapgroupby_clause.md) addition `GROUPING SETS` consists of a comma-separated list of grouping sets enclosed in parentheses. Each grouping set is itself parenthesized and is specified as follows:

- **As an empty grouping set `( )`**

  An empty grouping set represents an [aggregation](../../abap-glossary/abenaggregate_expression_glosry.md) across the entire [data source](abapselect_data_source.md). It is used, for example, to calculate a [total sum](abapselect_aggregate.md).

- **As a comma-separated list `( sql_exp1, sql_exp2, ... )`**

  A comma-separated list consisting of SQL expressions `sql_exp1, sql_exp2, ...` that defines the set of expressions to be aggregated.

Each grouping is viewed as a separate `GROUP BY` list and is evaluated as such. Here, the [SQL expressions](abapsql_expr.md) `sql_exp1, sql_exp2, ...` outside of the grouping set are also respected. The following two examples demonstrate this:

`GROUP BY sql_exp1, GROUPING SETS ( ( sql_exp2 ), ( sql_exp3, sql_exp4 ) )`

`GROUP BY GROUPING SETS ( ( sql_exp1, sql_exp2 ), (sql_exp1, sql_exp3, sql_exp4 ) )`

The results of the two `GROUP BY` clauses are equivalent and are the same as two [`SELECT`](abapselect.md) statements joined using [`UNION ALL`](abapunion.md). The following two `GROUP BY` lists are used here:

1.  `sql_exp1, sql_exp2`

2.  `sql_exp1, sql_exp3, sql_exp4`

The addition `GROUPING SETS` has an advantage over a `UNION` clause grouping because the `SELECT` clause only needs to be specified once. It is also potentially easier for the database to optimize a statement with the addition `GROUPING SETS` than its `UNION` equivalent.

****Rules****

- All columns used in the addition `GROUPING SETS` must be specified in the [`SELECT` list](abapselect_list.md).

- The expressions specified in `GROUPING SETS` cannot have the [data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `RAWSTRING`, `STRING`, or `GEOM_EWKB`.

- The result rows, plus the SQL expressions, can be in any order in the comma-separated list and the order does not affect the result of the aggregation. If the results of the aggregation need to be sorted in a specific way, an [`ORDER BY`](abaporderby_clause.md) clause must be specified. The `ORDER BY` addition `PRIMARY KEY` is allowed.

- The expressions that are part of the aggregation contain the null values as placeholders in the corresponding results.

****Tips****

The grouping function [`GROUPING`](abengrouping_function.md) can be used to check whether a specific column in the result set was aggregated or not.

## Hints

- The `GROUP BY` addition `GROUPING SETS` cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For Lufthansa flights, the following example calculates the sum of the maximum available seats depending on the plane type (column `planetype`) and the connection (column `connid`) Two grouping sets are defined, which contain either the plane type or the connection.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT FROM sflight 
       FIELDS carrid, 
              connid, 
              planetype, 
              SUM( seatsmax ) AS sum_seatsmax 
              WHERE carrid = 'LH' 
       GROUP BY GROUPING SETS ( ( carrid, planetype ), 
                                ( carrid, connid ), 
                                ( ) ) 
       ORDER BY connid, planetype 
       INTO TABLE @FINAL(result_grouping_sets). 
 
 out->write( result_grouping_sets ). 
 
out->display( ).
```

## Executable Example

See [`SELECT`, Grouping Sets](abenselect_grouping_sets_abexa.md)
