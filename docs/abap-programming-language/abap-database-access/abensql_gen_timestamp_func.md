---
title: "sql_func - Generic Time Stamp Functions"
source_file: abensql_gen_timestamp_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Time Stamp Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Generic Time Stamp Functions

## Syntax

``` abap
... IS_VALID( date|time|utclong ) 
  | EXTRACT_YEAR( date|utclong ) 
  | EXTRACT_MONTH( date|utclong ) 
  | EXTRACT_DAY( date|utclong ) 
  | EXTRACT_HOUR( time|utclong ) 
  | EXTRACT_MINUTE( time|utclong ) 
  | EXTRACT_SECOND( time|utclong ) 
  | DAYNAME( date|utclong ) 
  | MONTHNAME( date|utclong ) 
  | WEEKDAY( date|utclong ) 
  | DAYS_BETWEEN( {date1|utclong1},{date2|utclong2} ) 
  | ADD_DAYS( {date|utclong},days ) 
  | ADD_MONTHS( {date|utclong},months ) ...  
```

## Description

These SQL functions perform operations with arguments of the built-in data types [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The generic functions are documented in [date functions](abensql_date_func.md) and [time functions](abensql_time_func.md).
