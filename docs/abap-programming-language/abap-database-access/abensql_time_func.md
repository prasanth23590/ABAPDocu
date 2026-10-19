---
title: "sql_func - Time Functions"
source_file: abensql_time_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Time Functions

## Syntax Forms

**[Generic Time Functions](abensql_gen_time_func.md)**

``` abap
1. ... IS_VALID( date|time|utclong ) 
    | EXTRACT_HOUR( time|utclong ) 
    | EXTRACT_MINUTE( time|utclong ) 
    | EXTRACT_SECOND( time|utclong ) ...
```

**[Functions for `TIMS`](abensql_tims_time_func.md)**

``` abap
2. ... TIMS_IS_VALID( time ) ...
```

## Description

These SQL functions perform operations on times with arguments of the built-in data types [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The first set covers generic functions and the second set covers one function depending on the data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The arguments of the functions are specified in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis. [SQL expressions](abapsql_expr.md) of matching data types can be specified as actual parameters. If an actual parameter contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function except `IS_VALID` and `TIMS_IS_VALID` returns a null value. `IS_VALID` and `TIMS_IS_VALID` return the value 0.
