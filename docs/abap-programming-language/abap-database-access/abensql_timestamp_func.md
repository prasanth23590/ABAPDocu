---
title: "sql_func - Time Stamp Functions"
source_file: abensql_timestamp_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Time Stamp Functions

## Syntax Forms

**[Generic Time Stamp Functions](abensql_gen_timestamp_func.md)**

``` abap
1. ... IS_VALID( date|time|utclong ) 
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

**[Functions for `UTCLONG`](abensql_utc_timestamp_func.md)**

``` abap
2. ... UTCL_CURRENT( ) 
    | UTCL_ADD_SECONDS( utclong,seconds ) 
    | UTCL_SECONDS_BETWEEN( utclong1,utclong2 ) ...
```

**[Functions for `TIMESTAMP`](abensql_ts_timestamp_func.md)**

``` abap
3. ... TSTMP_IS_VALID( tstmp ) 
    | TSTMP_CURRENT_UTCTIMESTAMP( ) 
    | TSTMP_SECONDS_BETWEEN( tstmp1   = tstmp1, 
                             tstmp2   = tstmp2[, 
                             on_error = on_error] ) 
    | TSTMP_ADD_SECONDS( tstmp    = tstmp, 
                         seconds  = seconds[, 
                         on_error = on_error] ) ...
```

## Description

These SQL functions perform operations on time stamps. The values of time stamps are handled as [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md).

The first set covers generic functions, the second set covers functions depending on the built-in data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and the third set covers functions depending on the data element [`TIMESTAMP`](../abap-processing-internal-data/abentime_stamps_packed.md).

The arguments of the functions are specified as a comma-separated list in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis. Optional parameters can be assigned actual parameters when called. Non-optional parameters must be assigned actual parameters.

[SQL expressions](abapsql_expr.md) of matching data types can be specified as actual parameters. Only [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) of specific classes can be passed to the parameter `on_error` for the `TIMESTAMP` functions `TSTMP_SECONDS_BETWEEN` and `TSTMP_ADD_SECONDS`. If an actual parameter contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function except `IS_VALID` and `TSTMP_IS_VALID` returns a null value.
