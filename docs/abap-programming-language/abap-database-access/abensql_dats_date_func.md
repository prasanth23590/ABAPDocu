---
title: "sql_func - Functions for DATS"
source_file: abensql_dats_date_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Date Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Functions for DATS

## Syntax

``` abap
... DATS_IS_VALID( date ) 
  | DATS_DAYS_BETWEEN( date1,date2 ) 
  | DATS_ADD_DAYS( date,days ) 
  | DATS_ADD_MONTHS( date,months ) ...  
```

### Variant

[1. `... DATS_IS_VALID( date )`](abensql_dats_date_func.md#variant-1)

[2. `... DATS_DAYS_BETWEEN( date1,date2 )`](abensql_dats_date_func.md#variant-2)

[3. `... DATS_ADD_DAYS( date,days )`](abensql_dats_date_func.md#variant-3)

[4. `... DATS_ADD_MONTHS( date,months )`](abensql_dats_date_func.md#variant-4)

## Overview

### Description

These SQL functions perform operations on dates with arguments of the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 1

`... DATS_IS_VALID( date )`

### Description

The function `DATS_IS_VALID` determines whether `date` contains a valid date in the format `YYYYMMDD`. The actual parameter must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid date produces the value 1 and all other input values (including the null value) produce the value 0.

### Hint

The value *00010101* is a valid date here but the value *00000000* is not.

## Variant 2

`... DATS_DAYS_BETWEEN( date1,date2 )`

### Description

The function `DATS_DAYS_BETWEEN` calculates the difference between two dates `date1` and `date2` in days. The actual parameters must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. Any invalid date is initialized and set to the value *00010101* before the calculation. The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `date2` is greater than `date1`, the result is positive. In the reverse case, it is negative.

### Hint

Before the difference is calculated, the specified dates are converted to integers like in ABAP, and the corresponding [rules](../abap-processing-internal-data/abenconversion_type_d.md) apply.

## Variant 3

`... DATS_ADD_DAYS( date,days )`

### Description

The function `DATS_ADD_DAYS` adds `days` days to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. Any invalid date is initialized and set to the value *00010101* before the calculation.

- The actual parameter `days` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `days` is positive, the number of days is added to `date`. In other cases, the number of days is subtracted. If the calculation produces an invalid date, the initial value is reset.

### Hint

For the calculation, the specified date is [converted](../abap-processing-internal-data/abenconversion_type_d.md) to an integer like in ABAP, and the result is [converted](../abap-processing-internal-data/abenconversion_type_ibs.md) to a date again while the corresponding rules apply.

## Variant 4

`... DATS_ADD_MONTHS( date,months )`

### Description

The function `DATS_ADD_MONTHS` adds `months` months to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. Any invalid date is initialized and set to the value *00010101* before the calculation.

- The actual parameter `months` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `months` is positive, the number of months is added to `date`. In other cases, the number of months is subtracted.

The system tries to create a date with the same day in an earlier or later month. If the target month has fewer days than the source month, the last day of the target month is returned. If the calculation produces an invalid date, an error occurs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Applying the date functions to date columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_SQL_DATE_FUNCTIONS` executes this access to the table and displays the result.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( 
  VALUE #( id = 'X' dats1 = cl_demo_date_time=>get_user_date( ) 
                    dats2 = cl_demo_date_time=>get_user_date( ) + 100 
           datn1 = cl_demo_date_time=>get_user_date( ) + 5 
           datn2 = cl_demo_date_time=>get_user_date( ) + 200 ) ). 
 
SELECT SINGLE dats1, dats2, 
              dats_is_valid( dats1 ) AS valid, 
              dats_days_between( dats1, dats2 ) AS days_between, 
              dats_add_days( dats1,100 ) AS add_days, 
              dats_add_months( dats1,-1 ) AS add_month, 
              datn1, datn2, 
              datn_days_between( datn1, datn2 ) AS datn_between, 
              datn_add_days( datn1,1 ) AS datn_add_days, 
              datn_add_months( datn1,1 ) AS datn_add_month 
       FROM demo_expressions 
       INTO @FINAL(result).
```
