---
title: "sql_exp - sql_func"
source_file: abensql_builtin_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_func

## Syntax

``` abap
... sql_func( ... sql_exp ... ) ...  
```

[`sql_func( ... sql_exp ... )`](abenabap_sql_builtin_functions.md)

## Description

Calls a [built-in function](abenabap_sql_builtin_functions.md) in ABAP SQL. The result is the return value of the function with the associated dictionary type. As a rule, the arguments of the built-in functions cover one or more SQL expressions.

## Hints

- Specifying a built-in function always means specifying an [SQL expression](abapsql_expr.md). Built-in functions can only be called in operand positions for which SQL expressions are possible.

- [Certain SQL expressions](abensql_engine_expr.md) can be calculated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). If any other SQL expressions are used, [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is bypassed and internal tables accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the built-in functions [`CONCAT`](abensql_string_func.md), [`CONCAT_WITH_SPACE`](abensql_string_func.md), and [`LOWER`](abensql_string_func.md) in a [`SELECT` list](abapselect_list.md).

``` abap
SELECT FROM   spfli 
       FIELDS CONCAT( CONCAT( LOWER( carrid ), '_' ), 
                              LOWER( CAST( connid AS CHAR ) ) ) AS key, 
              CONCAT_WITH_SPACE( CONCAT( cityfrom, 
                                 ',' ), cityto, 1 ) AS cities 
       WHERE carrid = '...' 
       INTO TABLE @FINAL(result).
```

## Executable Examples

- [SQL expressions, arithmetic calculations](abensql_expr_arith_abexa.md)

- [String functions](abensql_string_func_abexa.md)

- [SQL Expressions, Coalesce Function](abensql_expr_coalesce_abexa.md)
