---
title: "sql_func - Generic Date Functions"
source_file: abensql_gen_date_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Date Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Generic Date Functions

## Syntax

``` abap
... IS_VALID( date|time|utclong ) 
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

### Variant

[1. `... IS_VALID( date|time|utclong )`](abensql_gen_date_func.md#variant-1)

[2. `... EXTRACT_YEAR( date|utclong )`](abensql_gen_date_func.md#variant-2)

[3. `... EXTRACT_MONTH( date|utclong )`](abensql_gen_date_func.md#variant-3)

[4. `... EXTRACT_DAY( date|utclong )`](abensql_gen_date_func.md#variant-4)

[5. `... DAYNAME( date|utclong )`](abensql_gen_date_func.md#variant-5)

[6. `... MONTHNAME( date|utclong )`](abensql_gen_date_func.md#variant-6)

[7. `... WEEKDAY( date|utclong )`](abensql_gen_date_func.md#variant-7)

[8. `... DAYS_BETWEEN( {date1|utclong1},{date2|utclong2} )`](abensql_gen_date_func.md#variant-8)

[9. `... ADD_DAYS( {date|utclong},days )`](abensql_gen_date_func.md#variant-9)

[10. `... ADD_MONTHS( {date|utclong},months )`](abensql_gen_date_func.md#variant-10)

## Overview

### Description

These SQL functions perform operations with arguments of the built-in data types [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 1

`... IS_VALID( date|time|utclong ) ...`

### Description

The generic function `IS_VALID` determines whether the specification `date`, `time`, or `utclong` has a valid format. For more information about the `IS_VALID` function, see [time functions](abensql_time_func.md).

### Hint

The generic function `IS_VALID` applies to [time functions](abensql_time_func.md) and [time stamp functions](abensql_timestamp_func.md) as well.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Applying the generic function to a date column of the DDIC database table `DEMO_EXPRESSIONS`.

``` abap
FINAL(date1) = cl_demo_date_time=>get_utc_date( ). 
 
... 
 
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( 
  id      = 'X' 
  dats1 = date1 ) ). 
 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS dats1 AS date1, 
              is_valid( dats1 ) AS valid1 
       INTO @FINAL(result).
```

## Variant 2

`... EXTRACT_YEAR( date|utclong ) ...`

### Description

The generic function `EXTRACT_YEAR` extracts the year of a date or an UTC time stamp. The actual parameter must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `EXTRACT_YEAR` has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The function returns the value 1 for initial input values. If no valid date is passed as a `DATS` value, the function `EXTRACT_YEAR` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

### Hints

- If the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_YEAR` calls the [HANA function `EXTRACT`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20e1a58475191014a343f6fe96c9846c).

- If the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_YEAR` internally uses the ABAP SQL [`SUBSTRING`](abensql_string_func.md) function and a [`CAST`](abensql_cast.md) expression afterwards. The corresponding rules apply.

## Variant 3

`... EXTRACT_MONTH( date|utclong ) ...`

### Description

The generic function `EXTRACT_MONTH` extracts the month of a date or an UTC time stamp. The actual parameter must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `EXTRACT_MONTH` has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The function returns the value 1 for initial input values. If no valid date is passed as a `DATS` value, the function `EXTRACT_MONTH` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

### Hints

- If the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_MONTH` calls the [HANA function `EXTRACT`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20e1a58475191014a343f6fe96c9846c).

- If the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_MONTH` internally uses the ABAP SQL [`SUBSTRING`](abensql_string_func.md) function and a [`CAST`](abensql_cast.md) expression afterwards. The corresponding rules apply.

## Variant 4

`... EXTRACT_DAY( date|utclong ) ...`

### Description

The generic function `EXTRACT_DAY` extracts the day of a date or an UTC time stamp. The actual parameter must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `EXTRACT_DAY` has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The function returns the value 1 for initial input values. If no valid date is passed as a `DATS` value, the function `EXTRACT_DAY` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

### Hints

- If the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_DAY` calls the [HANA function `EXTRACT`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20e1a58475191014a343f6fe96c9846c).

- If the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used, the function `EXTRACT_DAY` internally uses the ABAP SQL [`SUBSTRING`](abensql_string_func.md) function and a [`CAST`](abensql_cast.md) expression afterwards. The corresponding rules apply.

## Variant 5

`... DAYNAME( date|utclong ) ...`

### Description

The generic function `DAYNAME` returns the name of a day of a date or an UTC time stamp in uppercase letters in English. The actual parameter must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `DAYNAME` has the data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 9. If no valid date is saved in a `DATS` value, the function `DAYNAME` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

## Variant 6

`... MONTHNAME( date|utclong ) ...`

### Description

The generic function `MONTHNAME` returns the name of a month of a date or an UTC time stamp in uppercase letters in English. The actual parameter must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `MONTHNAME` has the data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 9. If no valid date is saved in a `DATS` value, the function `MONTHNAME` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

## Variant 7

`... WEEKDAY( date|utclong ) ...`

### Description

The generic function `WEEKDAY` returns the number of a weekday of a date or an UTC time stamp from 0 to 6. The actual parameter must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result of the function `WEEKDAY` has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If no valid date is saved in a `DATS` value, the function `WEEKDAY` raises a catchable exception of class `CX_SY_OPEN_SQL_DB`.

## Variant 8

`... DAYS_BETWEEN( {date1|utclong1},{date2|utclong2} ) ...`

### Description

The function `DAYS_BETWEEN` calculates the difference between two dates `date1` or `utclong1` and `date2` or `utclong2` in days. The actual parameters must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD` or a valid UTC time stamp in a format like `0001-01-01T00:00:00.0000000`. Any invalid date is initialized and set to the value *00010101* before the calculation. Any invalid UTC time stamp is initialized and set to the value *0001-01-01T00:00:00.0000000* before the calculation.

The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `date2` is greater than `date1`, the result is positive. In the reverse case, it is negative.

### Hint

It is possible to use two different data types for the function `DAYS_BETWEEN` and to calculate the days between these two dates.

## Variant 9

`... ADD_DAYS( {date|utclong},days ) ...`

### Description

The function `ADD_DAYS` adds `days` days to a specified date `date` or UTC time stamp `utclong`.

- The actual parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD`. The actual parameter `utclong` must have the built-in data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid UTC time stamp in a format like `0001-01-01T00:00:00.0000000`. Any invalid date is initialized and set to the value *00010101* before the calculation and any invalid UTC time stamp is initialized and set to the value *0001-01-01T00:00:00.0000000* before the calculation.

- The actual parameter `days` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type of the first actual parameter `days` or `utclong`. If `days` is positive, the number of days is added to `date` or `utclong`. In other cases, the number of days is subtracted. If the calculation produces an invalid date, the function raises a catchable exception of class `CX_SY_OPEN_SQL_DB` if the actual parameter `days` is of data type `DATN` or `UTCLONG`. If the actual parameter `days` is of data type `DATS`, the function returns the initial date.

## Variant 10

`...ADD_MONTHS( {date|utclong},months ) ...`

### Description

The function `ADD_MONTHS` adds `months` months to a specified date `date` or UTC time stamp `utclong`.

- The actual parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD`. The actual parameter `utclong` must have the built-in data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid UTC time stamp in a format like `0001-01-01T00:00:00.0000000`. Any invalid date is initialized and set to the value *00010101* before the calculation and any invalid UTC time stamp is initialized and set to the value *0001-01-01T00:00:00.0000000* before the calculation.

- The actual parameter `months` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type of the first actual parameter `days` or `utclong`. If `months` is positive, the number of months is added to `date` or `utclong`. In other cases, the number of months is subtracted.

The system tries to create a date with the same day in an earlier or later month. If the target month has fewer days than the source month, the last day of the target month is returned. If the calculation produces an invalid date, the function raises a catchable exception of class `CX_SY_OPEN_SQL_DB` if the actual parameter `months` is of data type `DATN` or `UTCLONG`. If the actual parameter `months` is of data type `DATS`, the function returns the initial date.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Applying the generic functions to date and time stamp columns of the DDIC database table `DEMO_EXPRESSIONS`.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( 
  VALUE #( id = 'X' dats1 = cl_demo_date_time=>get_user_date( ) 
                    datn2 = cl_demo_date_time=>get_user_date( ) 
           utcl1 = `2022-01-01T12:14:50` ) ). 
 
SELECT SINGLE dats1, datn2, utcl1, 
              extract_year( dats1 ) AS extract_year, 
              extract_month( datn2 ) AS extract_month, 
              extract_day( utcl1 ) AS extract_day, 
              dayname( dats1 ) AS dayname, 
              monthname( datn1 ) AS monthname, 
              weekday( utcl1 ) AS weekday, 
              days_between( dats1,utcl1 ) AS days_between, 
              add_days( datn2,2 ) AS add_days, 
              add_months( utcl1,4 ) AS add_months 
       FROM demo_expressions 
       INTO @FINAL(result).
```
