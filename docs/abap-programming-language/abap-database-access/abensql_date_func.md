---
title: "sql_func - Date Functions"
source_file: abensql_date_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Date Functions

## Syntax Forms

**[Generic Date Functions](abensql_gen_date_func.md)**

``` abap
1. ... IS_VALID( date|time|utclong ) 
    | EXTRACT_YEAR( date|utclong ) 
    | EXTRACT_MONTH( date|utclong ) 
    | EXTRACT_DAY( date|utclong ) 
    | DAYNAME( date|utclong ) 
    | MONTHNAME( date|utclong ) 
    | WEEKDAY( date|utclong ) 
    | DAYS_BETWEEN( {date1|utclong1},{date2|utclong2} ) 
    | ADD_DAYS( {date|utclong},days ) 
    | ADD_MONTHS( {date|utclong},months ) ...
```

**[Functions for `DATN`](abensql_datn_date_func.md)**

``` abap
2. ... DATN_DAYS_BETWEEN( date1,date2 ) 
    | DATN_ADD_DAYS( date,days ) 
    | DATN_ADD_MONTHS( date,months ) ...
```

**[Functions for `DATS`](abensql_dats_date_func.md)**

``` abap
3. ... DATS_IS_VALID( date ) 
    | DATS_DAYS_BETWEEN( date1,date2 ) 
    | DATS_ADD_DAYS( date,days ) 
    | DATS_ADD_MONTHS( date,months ) ...
```

## Description

These SQL functions perform operations on dates with arguments of the built-in data types [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The first set covers generic functions, the second set covers a function depending on the data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and the third set covers a function depending on the data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The arguments of the functions are specified as a comma-separated list in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis. [SQL expressions](abapsql_expr.md) of matching data types can be passed as actual parameters. If an actual parameter contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function except `IS_VALID` and `DATS_IS_VALID` returns a null value.
