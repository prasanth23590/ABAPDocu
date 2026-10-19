---
title: "sql_func - Coalesce Function"
source_file: abensql_coalesce.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Coalesce Function

## Syntax

``` abap
... COALESCE( sql_exp1, sql_exp2, ..., sql_expn ) ...  
```

## Description

Calls the [coalesce function](../../abap-glossary/abencoalesce_glosry.md) as an [SQL expression](abapsql_expr.md) or operand of an expression in ABAP SQL. The coalesce function can have a comma-separated list with at least two but no more than 255 arguments `sql_exp1`, `sql_exp2`, ..., `sql_expn`. This function returns the value of the first argument that does not have the [null value](../../abap-glossary/abennull_value_glosry.md). If every argument has the null value, the value of the last argument `sql_expn` is returned. A blank must be placed after the opening parenthesis and in front of the closing parenthesis.

The arguments can be any [SQL expressions](abapsql_expr.md) of all dictionary types except `ACCP`, `LCHR`, `LRAW`, `PREC`, `RAWSTRING`, `STRING`, and `GEOM_EWKB`. The data types of the arguments must either be the same or the data type of one argument must be able to fully represent the value of the other data types. The result has the dictionary type of the argument with the largest value range.

## Hints

- The coalesce function can be used to assign a target object a user-defined value or the result of an expression when null values are read. The type-dependent initial value is assigned by default.

- A maximum of ten coalesce functions can be nested.

- A coalesce function is a short form of the following [complex case distinction](abensql_searched_case.md):

  `CASE WHEN sql_exp1 IS NOT NULL THEN sql_exp1 WHEN sql_exp2 IS NOT NULL THEN sql_exp2 ... ELSE sql_expn END`

- The coalesce function can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table with [`FROM @itab`](abapselect_itab.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first four [`CASE` expressions](abensql_simple_case.md) return the null value, since no `WHEN` condition is met and no `ELSE` is specified. The result of the fifth `CASE` expression is not a null value and is returned by `COALESCE`.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( id = 'X' ) ). 
 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS coalesce( CASE id WHEN 'A'  THEN 'a' END, 
                        CASE id WHEN 'B'  THEN 'b' END, 
                        CASE id WHEN 'C'  THEN 'c' END, 
                        CASE id WHEN NULL THEN 'd' END, 
                        CASE id WHEN 'X'  THEN 'x' END  ) AS coalesced 
       INTO @FINAL(result).
```

## Executable Example

[SQL Expressions, Coalesce Function](abensql_expr_coalesce_abexa.md)
