---
title: "CDS DDL - CDS View Entity, Time Stamp Functions"
source_file: abencds_timestamp_functions_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, Special Functions > CDS DDL - CDS View Entity, Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Time Stamp Functions

## Syntax

``` abap
... UTCL_CURRENT() 
  | UTCL_ADD_SECONDS(utcl,seconds) 
  | UTCL_SECONDS_BETWEEN(utcl1,utcl2) 
  | TSTMP_IS_VALID(tstmp) 
  | TSTMP_CURRENT_UTCTIMESTAMP() 
  | TSTMP_SECONDS_BETWEEN(tstmp1,tstmp2,on_error) 
  | TSTMP_ADD_SECONDS(tstmp,seconds,on_error) ...  
```

### Variant

[1. `... UTCL_CURRENT()`](abencds_timestamp_functions_v2.md#variant-1)

[2. `... UTCL_ADD_SECONDS(utcl,seconds)`](abencds_timestamp_functions_v2.md#variant-2)

[3. `... UTCL_SECONDS_BETWEEN(utcl1,utcl2)`](abencds_timestamp_functions_v2.md#variant-3)

[4. `... TSTMP_IS_VALID(tstmp)`](abencds_timestamp_functions_v2.md#variant-4)

[5. `... TSTMP_CURRENT_UTCTIMESTAMP()`](abencds_timestamp_functions_v2.md#variant-5)

[6. `... TSTMP_SECONDS_BETWEEN(tstmp1,tstmp2,on_error)`](abencds_timestamp_functions_v2.md#variant-6)

[7. `... TSTMP_ADD_SECONDS(tstmp,seconds,on_error)`](abencds_timestamp_functions_v2.md#variant-7)

## Overview

### Description

In a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), these functions perform operations on [time stamps](../../abap-glossary/abentime_stamp_glosry.md). The values of time stamps are handled as [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md).

With the exception of `UTCL_CURRENT` and `TSTMP_CURRENT_UTCTIMESTAMP`, these functions have [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) to which arguments must be assigned when called. There are currently no optional parameters. Suitable fields of a [data source](abencds_data_source_v2.md), [literals](abencds_literal_v2.md), [parameters](abencds_parameter_v2.md), [path expressions](abencds_path_expression_v2.md), [built-in functions](abencds_builtin_functions_v2.md), [SQL-based scalar functions](abencds_sql_scalar_function.md), [expressions](abencds_expressions_v2.md), or [reuse expressions](abencds_reusable_expression_v2.md) using `$projection` can all be specified as arguments. Only literals can be passed to the parameter `on_error`. If an argument contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function except `TSTMP_IS_VALID` returns a null value.

### Hints

- While the time stamp functions starting with `UTCL` process data that is stored as real time stamp on the database, the functions starting with `TSTMP` process time stamps on the database that are stored [as a packed number](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the ABAP-specific format in DDIC database tables. These `TSTMP` time stamps are interpreted as regular numeric values in ABAP and in other types of access.

- [Conversion functions](abencds_date_time_conversions_v2.md) make it possible to transform a time stamp to date fields and time fields and to transform date fields and time fields to a time stamp.

## Variant 1

`... UTCL_CURRENT()`

### Description

This function generates a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) from the [system time](../../abap-glossary/abensystem_time_glosry.md) and the [system date](../../abap-glossary/abensystem_date_glosry.md) of AS ABAP in accordance with [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md). The return value has the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 2

`... UTCL_ADD_SECONDS(utcl,seconds)`

### Description

The function `UTCL_ADD_SECONDS` adds `seconds` seconds to a time stamp `utclong`. It has two [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md). The argument for the formal parameter `utclong` must have the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a valid [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md). An invalid time stamp produces an error. The argument for the formal parameter `seconds` must have either the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or the data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places. Any negative values are subtracted. If the result is invalid, an error occurs.

The result is of type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

### Hints

- If the positional parameter `utclong` is empty, it is set to its initial value.

- The days missing from the Gregorian calendar (from 5.10.1582 to 15.10.1582) are [handled as usual](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) in ABAP.

## Variant 3

`... UTCL_SECONDS_BETWEEN(utcl1,utcl2)`

### Description

The function `UTCL_SECONDS_BETWEEN` calculates the difference between two specified time stamps, `utcl1` and `utcl2`, in seconds. It has two [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md). The arguments for the formal parameters `utcl1` and `utcl2` must have the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a valid [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md). Any invalid time stamps produce an error. If `utcl2` is greater than `utcl1`, the result is positive. If the values are identical, the result is 0. In all other cases, the result is negative.

The result is of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places.

### Hints

- If an argument is empty, then this parameter is set to its initial value.

- The days missing from the Gregorian calendar (from 5.10.1582 to 15.10.1582) are [handled as usual](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) in ABAP.

## Variant 4

`... TSTMP_IS_VALID(tstmp)`

### Description

The function `TSTMP_IS_VALID` determines whether an argument `tstmp` contains a [valid time stamp](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. The argument must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places. The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid time stamp produces the value 1 and all other input values (including the null value) produce the value 0.

## Variant 5

`... TSTMP_CURRENT_UTCTIMESTAMP()`

### Description

The function `TSTMP_CURRENT_UTCTIMESTAMP` returns a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) in accordance with the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard. The result has the data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places.

### Hints

- The UTC time stamp is created from the clock on the database server. The [system date](../../abap-glossary/abensystem_date_glosry.md) and the [system time](../../abap-glossary/abensystem_time_glosry.md) in AS ABAP from which its time stamp is created using [`GET TIME STAMP`](../../abap-programming-language/abap-processing-internal-data/abapget_time-stamp.md) are [synchronized](../../abap-programming-language/abap-processing-internal-data/abensystem_user_time_zones.md) with the database server clock.

- If the function `TSTMP_CURRENT_UTCTIMESTAMP` is used more than once within a view, it cannot be guaranteed that the every call within a database access produces the same result. Later calls can produce later time stamps.

## Variant 6

`... TSTMP_SECONDS_BETWEEN(tstmp1,tstmp2,on_error)`

### Description

The function `TSTMP_SECONDS_BETWEEN` calculates the difference between two specified time stamps, `tstmp1` and `tstmp2`, in seconds. The argument must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places and contain [valid time stamps](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. Any invalid time stamps produce an error. If `tstmp2` is greater than `tstmp1`, the result is positive. In the reverse case, it is negative.

The result is of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places.

The argument `on_error` controls error handling. It must have the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 10 and must have one of the following values:

- *FAIL* (an error raises an exception)

- *NULL* (an error returns the null value)

- *INITIAL* (an error returns the initial value)

The values are case-sensitive. Any incorrectly specified values raise an exception.

## Variant 7

`... TSTMP_ADD_SECONDS(tstmp,seconds,on_error)`

### Description

The function `TSTMP_ADD_SECONDS` adds `seconds` seconds to a time stamp `tstmp`. The argument `tstmp` must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places and contain a valid [time stamp](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. An invalid time stamp produces an error. The argument `seconds` must also have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places. Any negative values are subtracted. If the result is invalid, an error occurs.

The argument `on_error` controls error handling. The same applies as to the function `TSTMP_SECONDS_BETWEEN`. The additional value *UNCHANGED* can be used to specify that an error caused the unchanged value of `tstmp` to be returned.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity applies time stamp functions in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_TIMESTAMP_FUNC_VE` uses `SELECT` to access the view. The column `NUM1` of the DDIC database table is given a value that is added to a time stamp in the column `TIMESTAMP1` as seconds. The difference is found between this sum and a time stamp retrieved on the database by the function `TSTMP_CURRENT_UTCTIMESTAMP`. A delay, `wait`, can be integrated between the time stamp in the ABAP program and the time stamp created on the database.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_TIMESTAMP_FUNC_VE
  with parameters
    p_seconds :abap.int4
  as select from demo_expressions
{
  key id,
      utcl_current()                                as utcl_timestamp,
      utcl_add_seconds(
        abap.utcl'2020-01-02 00:00:02.2222333',
        $parameters.p_seconds)                      as add_seconds,
      utcl_seconds_between(utcl1,utcl2)             as seconds_between,
      timestamp1                                    as timestamp1,
      tstmp_is_valid(abap.dec'202001022306050')     as valid1,
      tstmp_seconds_between(
        tstmp_current_utctimestamp(),
        tstmp_add_seconds(
          timestamp1,
          abap.dec'123456789123456',
          'FAIL'),
       'FAIL')                                      as difference
}
```
