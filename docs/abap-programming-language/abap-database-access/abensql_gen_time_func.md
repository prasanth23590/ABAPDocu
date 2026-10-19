---
title: "sql_func - Generic Time Functions"
source_file: abensql_gen_time_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Generic Time Functions

## Syntax

``` abap
... IS_VALID( date|time|utclong ) 
  | EXTRACT_HOUR( time|utclong ) 
  | EXTRACT_MINUTE( time|utclong ) 
  | EXTRACT_SECOND( time|utclong ) ...  
```

### Variant

[1. `... IS_VALID( date|time|utclong ) ...`](abensql_gen_time_func.md#variant-1)

[2. `... EXTRACT_HOUR( time|utclong ) ...`](abensql_gen_time_func.md#variant-2)

[3. `... EXTRACT_MINUTE( time|utclong ) ...`](abensql_gen_time_func.md#variant-3)

[4. `... EXTRACT_SECOND( time|utclong ) ...`](abensql_gen_time_func.md#variant-4)

## Overview

### Description

These SQL functions perform operations with arguments of the built-in data types [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 1

`... IS_VALID( date|time|utclong ) ...`

### Description

The generic function `IS_VALID` determines whether

- the specified date `date` contains a valid date in the format `YYYYMMDD`. The actual parameter must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- the specified time `time` contains a valid time in the format `HHMMSS`. The actual parameter must have the built-in data type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- the specified time stamp `utclong` contains a valid [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard in a format like `0001-01-01T00:00:00.0000000`. The actual parameter must have the built-in data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid time and the initial value (for the data types `TIMN` and `TIMS`) produce the value 1 and all other input values (including the null value) produce the value 0.

### Hint

The generic function `IS_VALID` is also available for [date functions](abensql_date_func.md) and [time stamp functions](abensql_timestamp_func.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Applying the generic function to a time column of the DDIC database table `DEMO_EXPRESSIONS`.

``` abap
FINAL(time1) = cl_demo_date_time=>get_utc_time( ). 
 
... 
 
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( 
  id      = 'X' 
  tims1 = time1 ) ). 
 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS tims1 AS time1, 
              is_valid( tims1 ) AS valid1 
       INTO @FINAL(result).
```

## Variant 2

`... EXTRACT_HOUR( time|utclong ) ...`

### Description

The generic function `EXTRACT_HOUR` extracts the hour of a time or an UTC time stamp. The actual parameter must have the built-in data type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `EXTRACT_HOUR` has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The function returns the value 0 for initial input values. If no valid time is passed as a `TIMS` value, the function `EXTRACT_HOUR` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

### Hints

- If one of the built-in data types [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_HOUR` calls the [HANA function `EXTRACT`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20e1a58475191014a343f6fe96c9846c).

- If the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_HOUR` internally uses the ABAP SQL [`SUBSTRING`](abensql_string_func.md) function and a [`CAST`](abensql_cast.md) expression afterwards. The corresponding rules apply.

## Variant 3

`... EXTRACT_MINUTE( time|utclong ) ...`

### Description

The generic function `EXTRACT_MINUTE` extracts the minute of a time or an UTC time stamp. The actual parameter must have the built-in data type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `EXTRACT_MINUTE` has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The function returns the value 0 for initial input values. If no valid time is passed as a `TIMS` value, the function `EXTRACT_MINUTE` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

### Hints

- If one of the built-in data types [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_MINUTE` calls the [HANA function `EXTRACT`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20e1a58475191014a343f6fe96c9846c).

- If the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_MINUTE` internally uses the ABAP SQL [`SUBSTRING`](abensql_string_func.md) function and a [`CAST`](abensql_cast.md) expression afterwards. The corresponding rules apply.

## Variant 4

`... EXTRACT_SECOND( time|utclong ) ...`

### Description

The generic function `EXTRACT_SECOND` extracts the second of a time or an UTC time stamp. The actual parameter must have the built-in data type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `EXTRACT_SECOND` has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The function returns the value 0 for initial input values. If no valid time is passed as a `TIMS` value, the function `EXTRACT_SECOND` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

### Hints

- If one of the built-in data types [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_SECOND` calls the [HANA function `EXTRACT`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20e1a58475191014a343f6fe96c9846c).

- If the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_SECOND` internally uses the ABAP SQL [`SUBSTRING`](abensql_string_func.md) function and a [`CAST`](abensql_cast.md) expression afterwards. The corresponding rules apply.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Applying the generic functions to time and time stamp columns of the DDIC database table `DEMO_EXPRESSIONS`.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( 
  VALUE #( id = 'X' tims1 = cl_demo_date_time=>get_user_time( ) 
                    timn2 = cl_demo_date_time=>get_user_time( ) 
           utcl1 = `2022-01-01T12:14:50` ) ). 
 
SELECT SINGLE tims1, timn2, utcl1, 
              extract_hour( tims1 ) AS extract_hour, 
              extract_minute( timn2 ) AS extract_minute, 
              extract_second( utcl1 ) AS extract_second 
       FROM demo_expressions 
       INTO @FINAL(result).
```
