---
title: "sql_func - Functions for DATN"
source_file: abensql_datn_date_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Date Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Functions for DATN

## Syntax

``` abap
... DATN_DAYS_BETWEEN( date1,date2 ) 
  | DATN_ADD_DAYS( date,days ) 
  | DATN_ADD_MONTHS( date,months ) ...  
```

### Variant

[1. `... DATN_DAYS_BETWEEN( date1,date2 )`](abensql_datn_date_func.md#variant-1)

[2. `... DATN_ADD_DAYS( date,days )`](abensql_datn_date_func.md#variant-2)

[3. `... DATN_ADD_MONTHS( date,months )`](abensql_datn_date_func.md#variant-3)

## Overview

### Description

These SQL functions perform operations on dates with arguments of the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 1

`... DATN_DAYS_BETWEEN( date1,date2 )`

### Description

The function `DATN_DAYS_BETWEEN` calculates the difference between two specified dates `date1` and `date2` in days. The actual parameters must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD`. The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `date2` is greater than `date1`, the result is positive. Otherwise, the result is negative. If the result is outside of the range of valid dates, an error occurs.

## Variant 2

`... DATN_ADD_DAYS( date,days )`

### Description

The function `DATN_ADD_DAYS` adds `days` days to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD`.

- The actual parameter `days` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `days` is positive, the number of days is added to `date`. In other cases, the number of days is subtracted. If the calculation produces an invalid date, an error occurs.

## Variant 3

`... DATN_ADD_MONTHS( date,months )`

### Description

The function `DATN_ADD_MONTHS` adds `months` months to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and it must contain a valid date in the format `YYYYMMDD`.

- The actual parameter `months` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `months` is positive, the number of months is added to `date`. In other cases, the number of months is subtracted.

The system tries to create a date with the same day in an earlier or later month. If the target month has fewer days than the source month, the last day of the target month is returned. If the calculation produces an invalid date, an error occurs.
