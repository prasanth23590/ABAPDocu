---
title: "CDS DDL - DDIC-Based View, Date/Time Conversions"
source_file: abencds_date_time_conversions_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, Special Functions > CDS DDL - DDIC-Based View, Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Date/Time Conversions

## Syntax

``` abap
... TSTMP_TO_DATS(tstmp,tzone,clnt,on_error) 
  | TSTMP_TO_TIMS(tstmp,tzone,clnt,on_error) 
  | TSTMP_TO_DST(tstmp,tzone,clnt,on_error) 
  | DATS_TIMS_TO_TSTMP(date,time,tzone,clnt,on_error) 
  | TSTMPL_TO_UTCL(tstmpl,on_error,on_initial) 
  | TSTMPL_FROM_UTCL(utcl,on_null) 
  | DATS_TO_DATN(dats,on_error,on_initial) 
  | DATS_FROM_DATN(date,on_null) 
  | TIMS_TO_TIMN(tims,on_error) 
  | TIMS_FROM_TIMN(time,on_null) ...  
```

### Variant

[1. `... TSTMP_TO_DATS(tstmp,tzone,clnt,on_error)`](abencds_date_time_conversions_v1.md#variant-1)

[2. `... TSTMP_TO_TIMS(tstmp,tzone,clnt,on_error)`](abencds_date_time_conversions_v1.md#variant-2)

[3. `... TSTMP_TO_DST(tstmp,tzone,clnt,on_error)`](abencds_date_time_conversions_v1.md#variant-3)

[4. `... DATS_TIMS_TO_TSTMP(date,time,tzone,clnt,on_error)`](abencds_date_time_conversions_v1.md#variant-4)

[5. `... TSTMPL_TO_UTCL(tstmpl,on_error,on_initial)`](abencds_date_time_conversions_v1.md#variant-5)

[6. `... TSTMPL_FROM_UTCL(utcl,on_null)`](abencds_date_time_conversions_v1.md#variant-6)

[7. `... DATS_TO_DATN(dats,on_error,on_initial)`](abencds_date_time_conversions_v1.md#variant-7)

[8. `... DATS_FROM_DATN(date,on_null)`](abencds_date_time_conversions_v1.md#variant-8)

[9. `... TIMS_TO_TIMN(tims,on_error)`](abencds_date_time_conversions_v1.md#variant-9)

[10. `... TIMS_FROM_TIMN(time,on_null)`](abencds_date_time_conversions_v1.md#variant-10)

## Overview

### Description

In a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), these functions perform conversions between date, time, and time stamp formats.

The functions have [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) to which arguments need to be assigned when called. There are currently no optional parameters. Suitable fields of a [data source](abencds_data_source_v1.md), [literals](abencds_literal_v1.md), [parameters](abencds_parameter_v1.md), [path expressions](abencds_path_expression_v1.md), built-in functions, or expressions can all be specified as arguments. Only literals can be passed to the parameters `on_error`, `on_initial`, and `on_null`. If an argument contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function returns a null value.

The values of time stamps are handled as [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md). The conversions follow the ABAP-specific [rules for time zones](../../abap-programming-language/abap-processing-internal-data/abentime_zone_rules.md). The associated DDIC database tables must be filled correctly.

### Hints

- These functions move the functions of the ABAP statements [`CONVERT TIME STAMP`](../../abap-programming-language/abap-processing-internal-data/abapconvert_time-stamp.md) and [`CONVERT INTO TIME STAMP`](../../abap-programming-language/abap-processing-internal-data/abapconvert_date_time-stamp.md) to the database.

- Literals in date and time conversion functions:

  - In functions 1 to 3, the parameter `tstmp` cannot be specified as literal. This is only possible indirectly, by using a cast expression. For example, this can be specified for `tstmp`:

    `cast('20200102122334' as abap.dec(15,0))`

  - In functions 5 and 6, the parameter `tstmpl` cannot be specified as literal. Casting isn't possible either.

  - In functions 7 and 8, the parameters `dats` and `datn` can be specified as character literals.

  - In functions 9 and 10, the parameters `tims` and `timn` can be specified as character literals.

## Variant 1

`... TSTMP_TO_DATS(tstmp,tzone,clnt,on_error)`

### Description

The function `TSTMP_TO_DATS` extracts the local date for the time zone specified in `tzone` from a time stamp in the argument `tstmp`. The value of the time stamp is handled as an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md).

The argument `tstmp` must contain a [valid time stamp](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in a packed number format. There are two options:

- It can have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places in the format `YYYYMMDDHHMMSS`.

- It can have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places in the format `YYYYMMDDHHMMSS.SSSSSSS`.

`tzone` expects an argument of the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 6, either initial or containing a valid [time zone](../../abap-glossary/abentime_zone_glosry.md). If an initial time zone is specified, no time shift is calculated. The argument `clnt` must have the built-in dictionary type [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid [client ID](../../abap-glossary/abenclient_identifier_glosry.md). This client ID is used in the evaluation of the system tables of the [rules for time zones](../../abap-programming-language/abap-processing-internal-data/abentime_zone_rules.md). In [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), only the session variable [`$session.client`](../abap-cds-data-definitions/abencds_session_variable_v2.md) can be specified for `clnt`. The return value has the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The argument `on_error` controls error handling. It must have the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 10 and must have one of the following values:

- *FAIL* (an error raises an exception)

- *NULL* (an error returns the null value)

- *INITIAL* (an error returns the initial value)

The pattern is case-sensitive. Any incorrectly specified values raise an exception.

## Variant 2

`... TSTMP_TO_TIMS(tstmp,tzone,clnt,on_error)`

### Description

The function `TSTMP_TO_TIMS` extracts the local time for the time zone specified in `tzone` from a time stamp in the argument `tstmp`. The value of the time stamp is handled as an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md).

The same applies to the arguments `tstmp`, `tzone`, `clnt`, and `on_error` as to the function `TSTMP_TO_DATS`. The return value has the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 3

`... TSTMP_TO_DST(tstmp,tzone,clnt,on_error)`

### Description

The function `TSTMP_TO_DST` extracts the daylight saving time marker for the time zone specified in `tzone` from a time stamp in the argument `tstmp`. The value of the time stamp is handled as an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md).

The result is *X* if the time stamp for the time zone is in the daylight saving time, otherwise it is initial.

The same applies to the arguments `tstmp`, `tzone`, `clnt`, and `on_error` as to the function `TSTMP_TO_DATS`. The return value has the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 1.

## Variant 4

`... DATS_TIMS_TO_TSTMP(date,time,tzone,clnt,on_error)`

### Description

The function `DATS_TIMS_TO_TSTMP` constructs an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) from a local date specified in `date` and a local time specified in `time` in the time zone specified in `tzone`. The daylight saving time is respected implicitly.

The argument `date` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date. The argument `time` must have the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid time. The same applies to the arguments `tzone`, `clnt`, and `on_error` as to the function `TSTMP_TO_DATS`.

The return value has the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and represents an ABAP-specific [time stamp in a packed number](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md).

## Variant 5

`... TSTMPL_TO_UTCL(tstmpl,on_error,on_initial)`

### Description

The function `TSTMPL_TO_UTCL` converts a time stamp `tstmpl` from the ABAP Dictionary type `TIMESTAMPL` to the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The argument for the formal parameter `tstmpl` must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places and contain a [valid time stamp](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSSMMMUUUN`.

The same applies to the argument `on_error` as to the function `TSTMP_TO_DATS`.

The argument `on_initial` defines the way arguments with initial values are handled. It must have the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 10 and must have one of the following values:

- *FAIL* (an initial value raises an exception)

- *NULL* (an initial value returns the null value)

- *INITIAL* (an initial value returns the initial value)

The pattern is case-sensitive. Any incorrectly specified values raise an exception.

### Hint

The function `TSTMPL_TO_UTCL` is a purely technical type conversion and does not involve any time zone calculations.

## Variant 6

`... TSTMPL_FROM_UTCL(tstmpl,on_null)`

### Description

The function `TSTMPL_FROM_UTCL` converts a time stamp `utcl` from the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the ABAP Dictionary type `TIMESTAMPL`. It is the counterpart to variant 5.

The argument for the formal parameter `utcl` must have the built-in data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and it should contain a valid time stamp.

The argument `on_null` defines the way null values as arguments are handled. It must have the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 10 and must have one of the following values:

- *FAIL* (a null value raises an exception)

- *NULL* (a null value returns the null value)

- *INITIAL* (a null value returns the initial value)

The pattern is case-sensitive. Any incorrectly specified values raise an exception.

If the parameter `utcl` is initial, 0 is returned.

### Hint

The function `TSTMPL_FROM_UTCL` is a purely technical type conversion and does not involve any time zone calculations.

## Variant 7

`... DATS_TO_DATN(dats,on_error,on_initial)`

### Description

The function `DATS_TO_DATN` converts a date `dats` from the built-in ABAP Dictionary data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the built-in ABAP Dictionary type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The argument for the formal parameter `dats` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. The same applies to the arguments `on_error` and `on_initial` as to the function `TSTMPL_TO_UTCL` (variant 5, see above).

### Hint

[`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is a newer dictionary type which represents a real date type in a database. [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), by contrast, is an older dictionary type. It is instantiated on a database as a character-like field. [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not interchangeable and a conversion is necessary to use certain functions.

## Variant 8

`... DATS_FROM_DATN(date,on_null)`

### Description

The function `DATS_FROM_DATN` converts a date `date` from the built-in ABAP Dictionary data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the built-in ABAP Dictionary type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). It is the counterpart to variant 7.

The argument for the formal parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD`. The same applies to the actual parameter `on_null` as to the function `TSTMPL_FROM_UTCL` (variant 6, see above).

### Hint

[`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is a newer dictionary type which represents a real date type in a database. [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), by contrast, is an older dictionary type. It is instantiated on a database as a character-like field. [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not interchangeable and to use certain functions, a conversion is necessary.

## Variant 9

`... TIMS_TO_TIMN(tims,on_error)`

### Description

The function `TIMS_TO_TIMN` converts a time `tims` from the ABAP Dictionary type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the ABAP Dictionary type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The argument for the formal parameter `tims` must have the built-in data type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a valid time in the format `HHMMSS`. The same applies to the argument `on_error` as to the function `TSTMP_TO_DATS` (variant 1, see above).

### Hint

[`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is a newer dictionary type which represents a real date type in a database. [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), by contrast, is an older dictionary type. It is instantiated on a database as a character-like field. [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not interchangeable and to use certain functions, a conversion is necessary.

## Variant 10

`... TIMS_FROM_TIMN(time,on_null)`

### Description

The function `TIMS_FROM_TIMN` converts a time `time` from the ABAP Dictionary type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to the ABAP Dictionary type [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). It is the counterpart to variant 9.

The argument for the formal parameter `time` must have the built-in data type [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a valid time in the format `HHMMSS`. The same applies to the argument `on_null` as to the function `TSTMPL_FROM_UTCL` (variant 6, see above).

### Hint

[`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is a newer dictionary type which represents a real date type in a database. [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), by contrast, is an older dictionary type. It is instantiated on a database as a character-like field. [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not interchangeable and to use certain functions, a conversion is necessary.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following CDS view, the date, the time, and the daylight saving time marker of the current UTC time stamp are extracted using the conversion functions `TSTMP_TO_DATS`, `TSTMP_TO_TIMS`, and `TSTMP_TO_DST`. The values of the columns `DATS1` and `TIMS1` of the DDIC database table `DEMO_EXPRESSIONS` are combined into a time stamp by the conversion function `DATS_TIMS_TO_TSTMP`. The conversion functions described in variants 5 to 10 convert time stamps, dates, and times between different types. The class `CL_DEMO_CDS_DATE_TIME` accesses the view and displays the result.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_DATIM'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_date_time
  with parameters
    p_tstmpl :abap_channels_timestamp_long
  as select from demo_expressions
{
  tstmp_current_utctimestamp()                   as tstmp,
  tstmp_to_dats( tstmp_current_utctimestamp(),
                 abap_system_timezone( $session.client,'NULL' ),
                 $session.client,
                 'NULL' )                        as dat,
  tstmp_to_tims( tstmp_current_utctimestamp(),
                 abap_system_timezone( $session.client,'NULL' ),
                 $session.client,
                 'NULL' )                        as tim,
  tstmp_to_dst( tstmp_current_utctimestamp(),
                abap_system_timezone( $session.client,'NULL' ),
                $session.client,
                'NULL' )                         as dst,
  dats_tims_to_tstmp( dats1,
                      tims1,
                      abap_system_timezone( $session.client,'NULL' ),
                      $session.client,
                     'NULL' )                    as dat_tim,
  tstmpl_to_utcl( :p_tstmpl, 'FAIL', 'INITIAL' ) as to_utcl,
  tstmpl_from_utcl( utcl_current( ), 'NULL' )    as from_utcl,
  dats_to_datn( dats1, 'INITIAL', 'INITIAL' )    as to_datn,
  dats_from_datn( datn1, 'INITIAL' )             as from_datn,
  tims_to_timn( tims1, 'NULL')                   as to_timn,
  tims_from_timn( timn1, 'INITIAL' )             as from_timn
}
```
