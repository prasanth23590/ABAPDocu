---
title: "sql_func - Date/Time Conversions"
source_file: abensql_date_time_conversions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Date/Time Conversions

## Syntax

``` abap
... TSTMP_TO_DATS( tstmp    = tstmp, 
                   tzone    = tzone[, 
                   on_error = on_error] ) 
  | TSTMP_TO_TIMS( tstmp    = tstmp, 
                   tzone    = tzone[, 
                   on_error = on_error] ) 
  | TSTMP_TO_DST(  tstmp    = tstmp, 
                   tzone    = tzone[, 
                   on_error = on_error] ) 
  | DATS_TIMS_TO_TSTMP( date     = date, 
                        time     = time, 
                        tzone    = tzone[, 
                        on_error = on_error] ) 
  | TSTMPL_TO_UTCL( tstmpl = tstmpl[, 
                    on_error = on_error],[ 
                    on_initial = on_initial] ) 
  | TSTMPL_FROM_UTCL( utcl = utcl[, 
                      on_null = on_null] ) 
  | DATS_TO_DATN( dats = dats[, 
                  on_error = on_error],[ 
                  on_initial = on_initial] ) 
  | DATS_FROM_DATN( datn = datn[, 
                    on_null = on_null] ) 
  | TIMS_TO_TIMN( tims = tims[, 
                  on_error = on_error] ) 
  | TIMS_FROM_TIMN( timn = timn[, 
                    on_null = on_null] )...  
```

### Variant

[1. `... TSTMP_TO_DATS( ... )`](abensql_date_time_conversions.md#variant-1)

[2. `... TSTMP_TO_TIMS( ... )`](abensql_date_time_conversions.md#variant-2)

[3. `... TSTMP_TO_DST( ... )`](abensql_date_time_conversions.md#variant-3)

[4. `... DATS_TIMS_TO_TSTMP( ... )`](abensql_date_time_conversions.md#variant-4)

[5. `... TSTMPL_TO_UTCL( ... )`](abensql_date_time_conversions.md#variant-5)

[6. `... TSTMPL_FROM_UTCL( ... )`](abensql_date_time_conversions.md#variant-6)

[7. `... DATS_TO_DATN( ... )`](abensql_date_time_conversions.md#variant-7)

[8. `... DATS_FROM_DATN( ... )`](abensql_date_time_conversions.md#variant-8)

[9. `... TIMS_TO_TIMN( ... )`](abensql_date_time_conversions.md#variant-9)

[10. `... TIMS_FROM_TIMN( ... )`](abensql_date_time_conversions.md#variant-10)

## Overview

### Description

The SQL functions described in variants 1 to 4 convert [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard into dates or times, and vice versa. The SQL functions described in variants 5 to 10 convert UTC time stamps, dates, and times between different types.

The arguments of the functions are specified as a comma-separated list in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis. The functions have [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md). Optional parameters can be assigned actual parameters when called. Non-optional parameters must be assigned actual parameters.

[SQL expressions](abapsql_expr.md), in particular individual columns, type-compliant literals, SQL functions, host variables or host expressions can be specified as actual parameters.

The conversions follow the ABAP-specific [rules for time zones](../abap-processing-internal-data/abentime_zone_rules.md). The associated DDIC database tables must be filled correctly.

### Hints

- The functions described in Variants 5 to 10 have [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md) and all of them have exactly one required parameter. When calling only the required parameter, then it can be handled like a [positional parameter](../../abap-glossary/abenpositional_parameter_glosry.md), that means it can be called without the formal parameter name.

- These functions move the functions of the ABAP statements [`CONVERT TIME STAMP`](../abap-processing-internal-data/abapconvert_time-stamp.md) and [`CONVERT INTO TIME STAMP`](../abap-processing-internal-data/abapconvert_date_time-stamp.md) to the database.

## Variant 1

`... TSTMP_TO_DATS( ... )`

### Description

The function `TSTMP_TO_DATS` extracts the local date for the time zone specified in `tzone` from an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard in the argument `tstmp`.

The actual parameter for the formal parameter `tstmp` must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places and contain a [valid UTC time stamp](../abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. `tzone` expects an actual parameter of the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 6, either initial or containing a valid [time zone](../../abap-glossary/abentime_zone_glosry.md). If an initial time zone is specified, no time shift is calculated. Another optional parameter `client` must not be used in ABAP for Cloud Development.

The return value has the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The optional parameter `on_error` affects how errors are handled. The parameter for `on_error` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` from the class `SQL_TSTMP_TO_DATS` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_TSTMP_TO_DATS=>FAIL`, an error raises an exception (default)

- `SQL_TSTMP_TO_DATS=>SET_TO_NULL`, an error returns the null value

## Variant 2

`... TSTMP_TO_TIMS( ... )`

### Description

The function `TSTMP_TO_TIMS` extracts the local time for the time zone specified in `tzone` from an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard in the argument `tstmp`.

The same applies to the parameters `tstmp`, `tzone`, and `on_error` as to the function `TSTMP_TO_DATS`. Here, the class of the enumerated type of `on_error` is `SQL_TSTMP_TO_TIMS`. Another optional parameter `client` must not be used in ABAP for Cloud Development.

The return value has the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 3

`... TSTMP_TO_DST( ... )`

### Description

The function `TSTMP_TO_DST` extracts the daylight saving time marker for the time zone specified in `tzone` from an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard in the argument `tstmp`. This is *X* if the time stamp for the time zone is in the daylight saving time, otherwise it is initial.

The same applies to the parameters `tstmp`, `tzone`, and `on_error` as to the function `TSTMP_TO_DATS`. Here, the class of the enumerated type of `on_error` is `SQL_TSTMP_TO_DST`. Another optional parameter `client` must not be used in ABAP for Cloud Development.

The return value has the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 1.

## Variant 4

`... DATS_TIMS_TO_TSTMP( ... )`

### Description

The function `DATS_TIMS_TO_TSTMP` constructs an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard from a local date specified in `date` and a local time specified in `time` in the time zone specified in `tzone`. The daylight saving time is respected implicitly.

The actual parameter for the formal parameter `date` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date. The actual parameter for the formal parameter `time` must have the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid time. The same applies to the parameters `tzone`, and `on_error` as to the function `TSTMP_TO_DATS`. Here, the class of the enumerated type of `on_error` is `SQL_DATS_TIMS_TO_TSTMP`. Another optional parameter `client` must not be used in ABAP for Cloud Development.

The return value has the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and represents an ABAP-specific UTC [time stamp in a packed number](../abap-processing-internal-data/abentime_stamps_packed.md).

## Variant 5

`... TSTMPL_TO_UTCL( ... )`

### Description

The function `TSTMPL_TO_UTCL` converts an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard `tstmpl` from the ABAP Dictionary type `TIMESTAMPL` to the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The actual parameter for the formal parameter `tstmpl` must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places and contain a [valid UTC time stamp](../abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSSMMMUUUN`.

The optional parameter `on_error` affects how errors are handled:

The parameter for `on_error` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` from the class `SQL_TSTMPL_TO_UTCL` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_TSTMPL_TO_UTCL=>C_ON_ERROR-FAIL`, an error raises an exception (default)

- `SQL_TSTMPL_TO_UTCL=>C_ON_ERROR-SET_TO_NULL`, an error returns the null value)

- `SQL_TSTMPL_TO_UTCL=>C_ON_ERROR-SET_TO_INITIAL`, an error returns the initial value

The optional parameter `on_initial` affects how arguments with initial values are handled:

The parameter for `on_initial` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_INITIAL` from the class `SQL_TSTMPL_FROM_UTCL` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_TSTMPL_FROM_UTCL=>C_ON_INITIAL-FAIL`, an initial value raises an exception

- `SQL_TSTMPL_FROM_UTCL=>C_ON_INITIAL-SET_TO_NULL`, an initial value returns the null value

- `SQL_TSTMPL_FROM_UTCL=>C_ON_INITIAL-SET_TO_INITIAL`, an initial value returns the initial value (default)

## Variant 6

`... TSTMPL_FROM_UTCL( ... )`

### Description

The function `TSTMPL_FROM_UTCL` converts an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard `utcl` from the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the ABAP Dictionary type `TIMESTAMPL`. It is the counterpart to variant 5.

The actual parameter for the formal parameter `utcl` must have the built-in data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid UTC time stamp.

The optional parameter `on_null` affects how null values as arguments are handled. The parameter for `on_null` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_NULL` from the class `SQL_TSTMPL_FROM_UTCL` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_TSTMPL_FROM_UTCL=>C_ON_NULL-FAIL`, a null value raises an exception

- `SQL_TSTMPL_FROM_UTCL=>C_ON_NULL-SET_TO_NULL`, a null value returns the null value

- `SQL_TSTMPL_FROM_UTCL=>C_ON_NULL-SET_TO_INITIAL`, a null value returns the initial value (default)

## Variant 7

`... DATS_TO_DATN( ... )`

### Description

The function `DATS_TO_DATN` converts a date `dats` from the built-in ABAP Dictionary data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the built-in ABAP Dictionary type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The actual parameter for the formal parameter `dats` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. The same applies to the actual parameters `on_error` and `on_initial` as to the function `TSTMPL_TO_UTCL` (Variant 5, see above). Here, the class of the enumerated type of `on_error` and `on_initial` is `SQL_DATS_TO_DATN`.

### Hint

The same effect of the function `DATS_TO_DATN` can be achieved by [casting](abensql_cast.md).

## Variant 8

`... DATS_FROM_DATN( ... )`

### Description

The function `DATS_FROM_DATN` converts a date `date` from the built-in ABAP Dictionary data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the built-in ABAP Dictionary type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). It is the counterpart to Variant 7.

The actual parameter for the formal parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD`. The same applies to the actual parameter `on_null`, as to the function `TSTMPL_FROM_UTCL` (Variant 6, see above). Here, the class of the enumerated type of `on_null` is `SQL_DATS_FROM_DATN`.

### Hint

The same effect of the function `DATS_FROM_DATN` can be achieved by [casting](abensql_cast.md).

## Variant 9

`... TIMS_TO_TIMN( ... )`

### Description

The function `TIMS_TO_TIMN` converts a time `tims` from the ABAP Dictionary type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the ABAP Dictionary type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The actual parameter for the formal parameter `tims` must have the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a valid time in the format `HHMMSS`. The same applies to the actual parameter `on_error` as to the function `TSTMP_TO_DATS` (Variant 1, see above). Here, the class of the enumerated type of `on_error` is `SQL_TIMS_TO_TIMN`.

### Hint

The same effect of the function `TIMS_TO_TIMN` can be achieved by [casting](abensql_cast.md).

## Variant 10

`... TIMS_FROM_TIMN( ... )`

### Description

The function `TIMS_FROM_TIMN` converts a time `time` from the ABAP Dictionary type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the ABAP Dictionary type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). It is the counterpart to variant 9.

The actual parameter for the formal parameter `time` must have the built-in data type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a valid time in the format `HHMMSS`. The same applies to the actual parameter `on_null` as to the function `TSTMPL_FROM_UTCL` (Variant 6, see above). Here, the class of the enumerated type of `on_null` is `SQL_TIMS_FROM_TIMN`.

### Hint

The same effect of the function `TIMS_FROM_TIMN` can be achieved by [casting](abensql_cast.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Extracts date, time, and daylight saving time flag of the current UTC time stamp using the conversion functions `TSTMP_TO_DATS`, `TSTMP_TO_TIMS`, and `TSTMP_TO_DST`. The values of the columns `DATS1` and `TIMS1` of the DDIC database table `DEMO_EXPRESSIONS` are combined into a time stamp by the conversion function `DATS_TIMS_TO_TSTMP`. The conversion functions `TSTMPL_TO_UTCL` and `TSTMPL_FROM_UTCL` convert time stamps between `TIMESTAMPL` and [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) format. The conversion functions `DATS_TO_DATN` and `DATS_FROM_DATN` convert dates between [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The conversion functions `TIMS_TO_TIMN` and `TIMS_FROM_TIMN` convert times between [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The class `CL_DEMO_SQL_DATE_TIME` executes the statement and displays the result.

``` abap
DATA ts TYPE timestampl. 
GET TIME STAMP FIELD ts. 
 
FINAL(utc) = utclong_current( ). 
 
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( 
  VALUE #( id = 'X' 
           dats1 = cl_demo_date_time=>get_user_date( ) 
           tims1 = cl_demo_date_time=>get_user_time( ) 
           timestampl1 = ts 
           utcl1 = utclong_current( ) ) ). 
 
DATA tzone TYPE timezone. 
CALL FUNCTION 'GET_SYSTEM_TIMEZONE' 
  IMPORTING 
    timezone = tzone. 
 
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS 
         tstmp_current_utctimestamp( ) 
             AS tstmp, 
         tstmp_to_dats( 
           tstmp    = tstmp_current_utctimestamp( ), 
           tzone    = @tzone, 
           on_error = @sql_tstmp_to_dats=>set_to_null ) 
             AS dat, 
         tstmp_to_tims( 
           tstmp    = tstmp_current_utctimestamp( ), 
           tzone    = @tzone, 
           on_error = @sql_tstmp_to_tims=>set_to_null ) 
             AS tim, 
         tstmp_to_dst( 
           tstmp    = tstmp_current_utctimestamp( ), 
           tzone    = @tzone, 
           on_error = @sql_tstmp_to_dst=>set_to_null ) 
             AS dst, 
           dats_tims_to_tstmp( 
             date     = dats1, 
             time     = tims1, 
             tzone    = @tzone, 
             on_error = @sql_dats_tims_to_tstmp=>set_to_null ) 
               AS dat_tim, 
         tstmpl_to_utcl( 
           tstmpl    = timestampl1, 
           on_error = @sql_tstmpl_to_utcl=>c_on_error-set_to_null, 
           on_initial = 
           @sql_tstmpl_to_utcl=>c_on_initial-set_to_initial ) 
             AS utcl, 
         tstmpl_from_utcl( 
           utcl = utcl1, 
           on_null = @sql_tstmpl_from_utcl=>c_on_null-set_to_null ) 
             AS from_utcl 
       INTO @FINAL(result).
```
