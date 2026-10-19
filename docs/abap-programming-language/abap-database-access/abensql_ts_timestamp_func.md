---
title: "sql_func - Functions for TIMESTAMP"
source_file: abensql_ts_timestamp_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Time Stamp Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Functions for TIMESTAMP

## Syntax

``` abap
... TSTMP_IS_VALID( tstmp ) 
  | TSTMP_CURRENT_UTCTIMESTAMP( ) 
  | TSTMP_SECONDS_BETWEEN( tstmp1   = tstmp1, 
                           tstmp2   = tstmp2[, 
                           on_error = on_error] ) 
  | TSTMP_ADD_SECONDS( tstmp    = tstmp, 
                       seconds  = seconds[, 
                       on_error = on_error] ) ...  
```

### Variant

[1. `... TSTMP_IS_VALID( tstmp )`](abensql_ts_timestamp_func.md#variant-1)

[2. `... TSTMP_CURRENT_UTCTIMESTAMP( )`](abensql_ts_timestamp_func.md#variant-2)

[3. `... TSTMP_SECONDS_BETWEEN( ... )`](abensql_ts_timestamp_func.md#variant-3)

[4. `... TSTMP_ADD_SECONDS( ... )`](abensql_ts_timestamp_func.md#variant-4)

## Overview

### Description

These SQL functions perform operations with arguments of the data element [`TIMESTAMP`](../abap-processing-internal-data/abentime_stamps_packed.md).

## Variant 1

`... TSTMP_IS_VALID( tstmp )`

### Description

The function `TSTMP_IS_VALID` determines whether an argument `tstmp` contains a [valid time stamp](../abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. It has one [positional parameter](../../abap-glossary/abenpositional_parameter_glosry.md). The actual parameter must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places. The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid time stamp produces the value 1 and all other input values (including the null value) produce the value 0.

## Variant 2

`... TSTMP_CURRENT_UTCTIMESTAMP( )`

### Description

The function `TSTMP_CURRENT_UTCTIMESTAMP` returns a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) in accordance with the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard. The result has the data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places.

### Hints

- The UTC time stamp is created from the clock on the database server. The [system date](../../abap-glossary/abensystem_date_glosry.md) and the [system time](../../abap-glossary/abensystem_time_glosry.md) in AS ABAP from which its time stamp is created using [`GET TIME STAMP`](../abap-processing-internal-data/abapget_time-stamp.md) are [synchronized](../abap-processing-internal-data/abensystem_user_time_zones.md) with the database server clock.

- If the function `TSTMP_CURRENT_UTCTIMESTAMP` is used more than once within an ABAP SQL statement, it cannot be guaranteed that every call within a database access produces the same result. Hence, later calls can produce later time stamps.

## Variant 3

`... TSTMP_SECONDS_BETWEEN( ... )`

### Description

The function `TSTMP_SECONDS_BETWEEN` calculates the difference between two specified time stamps, `tstmp1` and `tstmp2` in seconds. All parameters are [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md). The actual parameters for the formal parameters `tstmp1` and `tstmp2` must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places and contain [valid time stamps](../abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. Any invalid time stamps produce an error. If `tstmp2` is greater than `tstmp1`, the result is positive. In the reverse case, it is negative.

The optional parameter `on_error` affects how errors are handled. The parameter for `on_error` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` from the class `SQL_TSTMP_SECONDS_BETWEEN` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_TSTMP_SECONDS_BETWEEN=>FAIL`: An error raises an exception (default).

- `SQL_TSTMP_SECONDS_BETWEEN=>SET_TO_NULL`: An error returns the null value.

## Variant 4

`... TSTMP_ADD_SECONDS( ... )`

### Description

The function `TSTMP_ADD_SECONDS` adds `seconds` seconds to a time stamp `tstmp`. All parameters are [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md). The actual parameter for the formal parameter `tstmp` must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places and contain a [valid time stamp](../abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. An invalid time stamp produces an error. The actual parameter for the formal parameter `seconds` must also have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places. Negative values are subtracted. If the result is invalid, an error occurs.

The optional parameter `on_error` affects how errors are handled. The parameter for `on_error` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` from the class `SQL_TSTMP_ADD_SECONDS` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_TSTMP_ADD_SECONDS=>FAIL`: An error raises an exception (default).

- `SQL_TSTMP_ADD_SECONDS=>SET_TO_NULL`: An error returns the null value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Applies the time stamp functions to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_SQL_TIMESTAMP_FUNC` executes this access to the table and displays the result. The column `NUM1` of the DDIC database table is given a value that is added to a time stamp in the column `TIMESTAMP1` as seconds. The difference is calculated between this sum and a time stamp retrieved on the database by the function `TSTMP_CURRENT_UTCTIMESTAMP`. A delay `wait` can be integrated between the time stamp in the ABAP program and the time stamp created on the database. The number of seconds specified as type-compliant literal in the variable `pack` is added to the time stamp `utcl`, which has the type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). Finally, the difference in seconds between two time stamps of type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is calculated. Since `utcl1` is greater than `utcl2`, the result is negative.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(seconds) = 3600. 
cl_demo_input=>add_field( CHANGING field = seconds ). 
DATA(wait) = 1. 
cl_demo_input=>request( CHANGING field = wait ). 
 
GET TIME STAMP FIELD FINAL(timestamp1). 
 
DATA pack TYPE p LENGTH 11 DECIMALS 7 VALUE '123.456'. 
 
FINAL(utcl) = utclong_current( ). 
FINAL(utcl1) = 
  utclong_add( val     = utcl 
               days    = 1000 
               hours   = 100 
               minutes = 10 ). 
 
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( 
  id         = 'X' 
  num1       = seconds 
  timestamp1 = timestamp1 
  utcl1 = utcl1 
  utcl2 = utclong_current( ) ) ). 
WAIT UP TO COND #( WHEN wait > 10 THEN 10 
                   WHEN wait <  0 THEN 0 
                   ELSE wait ) SECONDS. 
 
TRY. 
    SELECT 
      SINGLE 
      FROM demo_expressions 
      FIELDS 
        timestamp1, 
        tstmp_is_valid( 
          timestamp1 ) 
            AS valid1, 
        tstmp_seconds_between( 
          tstmp1 = tstmp_current_utctimestamp( ), 
          tstmp2 = tstmp_add_seconds( 
                     tstmp    = timestamp1, 
                     seconds  = CAST( num1 AS DEC( 15,0 ) ), 
                     on_error = @sql_tstmp_add_seconds=>fail ), 
          on_error = @sql_tstmp_seconds_between=>fail ) 
            AS difference, 
        utcl_add_seconds( utcl2, @pack ) AS add_seconds, 
        utcl_seconds_between( utcl1,utcl2 ) AS seconds_between 
      INTO @FINAL(result). 
    out->display( result ). 
  CATCH cx_sy_open_sql_db INTO FINAL(exc). 
    out->display( exc->get_text( ) ). 
    RETURN. 
ENDTRY.
```
