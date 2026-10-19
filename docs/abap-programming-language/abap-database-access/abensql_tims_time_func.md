---
title: "sql_func - Functions for TIMS"
source_file: abensql_tims_time_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Functions for TIMS

## Syntax

``` abap
... TIMS_IS_VALID( time ) ...  
```

## Description

This SQL function performs operations with arguments of the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The function `TIMS_IS_VALID` determines whether the specification `time` contains a valid time in the format `HHMMSS`. The actual parameter must have the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid time and the initial value produce the value 1 and all other input values (including the null value) produce the value 0.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Applying the time function to a time column of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_SQL_TIME_FUNCTIONS` executes this access to the table and displays the result.

``` abap
FINAL(time1) = cl_demo_date_time=>get_user_time( ). 
 
... 
 
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( 
  id      = 'X' 
  tims1 = time1 ) ). 
 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS tims1 AS time1, 
              tims_is_valid( tims1 ) AS valid1 
       INTO @FINAL(result).
```
