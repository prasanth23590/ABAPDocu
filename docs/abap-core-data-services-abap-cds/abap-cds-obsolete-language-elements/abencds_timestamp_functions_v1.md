---
title: "CDS DDL - DDIC-Based View, Time Stamp Functions"
source_file: abencds_timestamp_functions_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, Special Functions > CDS DDL - DDIC-Based View, Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Time Stamp Functions

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

[1. `... UTCL_CURRENT()`](abencds_timestamp_functions_v1.md#variant-1)

[2. `... UTCL_ADD_SECONDS(utcl,seconds)`](abencds_timestamp_functions_v1.md#variant-2)

[3. `... UTCL_SECONDS_BETWEEN(utcl1,utcl2)`](abencds_timestamp_functions_v1.md#variant-3)

[4. `... TSTMP_IS_VALID(tstmp)`](abencds_timestamp_functions_v1.md#variant-4)

[5. `... TSTMP_CURRENT_UTCTIMESTAMP()`](abencds_timestamp_functions_v1.md#variant-5)

[6. `... TSTMP_SECONDS_BETWEEN(tstmp1,tstmp2,on_error)`](abencds_timestamp_functions_v1.md#variant-6)

[7. `... TSTMP_ADD_SECONDS(tstmp,seconds,on_error)`](abencds_timestamp_functions_v1.md#variant-7)

## Overview

### Description

In a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), these functions perform operations on time stamps. The values of time stamps are handled as [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md).

With the exception of `UTCL_CURRENT` and `TSTMP_CURRENT_UTCTIMESTAMP`, these functions have [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) to which arguments must be assigned when called. There are currently no optional parameters. Suitable fields of a [data source](abencds_data_source_v1.md), [literals](abencds_literal_v1.md), [parameters](abencds_parameter_v1.md), [path expressions](abencds_path_expression_v1.md), built-in functions, or expressions can all be specified as arguments. Only literals can be passed to the parameter `on_error`. If an argument contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function except `TSTMP_IS_VALID` returns a null value.

### Hints

- While the time stamp functions starting with `UTCL` process data that is stored as real time stamp on the database, the functions starting with `TSTMP` process time stamps on the database that are stored [as a packed number](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the ABAP-specific format in DDIC database tables. As in ABAP, other types of access to these fields interpret these time stamps as regular numeric values.

- [Conversion functions](abencds_date_time_conversions_v1.md) make it possible to transform a time stamp to date fields and time fields and to transform date fields and time fields to a time stamp.

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

- The argument `utcl` can be any of the operands listed above in section **Effect**, including a literal. A literal can be specified in the following format: `'0001-01-01 00:00:02.0000000'`

- If the positional parameter `utclong` is empty, it is set to its initial value.

- The days missing from the Gregorian calendar (from 5.10.1582 to 15.10.1582) are [handled as usual](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) in ABAP.

## Variant 3

`... UTCL_SECONDS_BETWEEN(utcl1,utcl2)`

### Description

The function `UTCL_SECONDS_BETWEEN` calculates the difference between two specified time stamps, `utcl1` and `utcl2`, in seconds. It has two [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md). The arguments for the formal parameters `utcl1` and `utcl2` must have the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a valid [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md). Any invalid time stamps produce an error. If `utcl2` is greater than `utcl1`, the result is positive. If the values are identical, the result is 0. In all other cases, the result is negative.

The result is of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places.

### Hints

- The argument `utcl` can be any of the operands listed above in section **Effect**, including a literal. A literal can be specified in the following format: `'0001-01-01 00:00:02.0000000'`

- If an argument is empty, then this parameter is set to its initial value.

- The days missing from the Gregorian calendar (from 5.10.1582 to 15.10.1582) are [handled as usual](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) in ABAP.

## Variant 4

`... TSTMP_IS_VALID(tstmp)`

### Description

The function `TSTMP_IS_VALID` determines whether an argument `tstmp` contains a [valid time stamp](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. The argument must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places. The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid time stamp produces the value 1 and all other input values (including the null value) produce the value 0.

### Hint

The argument `tstmp` cannot be specified as literal. This is only possible indirectly by using a cast expression. For example, this is valid syntax:

`tstmp_is_valid(cast(20200102334455 as abap.dec(15,0)) as demo`

## Variant 5

`... TSTMP_CURRENT_UTCTIMESTAMP()`

### Description

The function `TSTMP_CURRENT_UTCTIMESTAMP` returns a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) in accordance with the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard. The result has the data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places.

### Hints

- The UTC time stamp is created from the clock on the database server. The [system date](../../abap-glossary/abensystem_date_glosry.md) and the [system time](../../abap-glossary/abensystem_time_glosry.md) in AS ABAP from which its time stamp is created using [`GET TIME STAMP`](../../abap-programming-language/abap-processing-internal-data/abapget_time-stamp.md) are [synchronized](../../abap-programming-language/abap-processing-internal-data/abensystem_user_time_zones.md) with the database server clock.

- If the function `TSTMP_CURRENT_UTCTIMESTAMP` is used more thane once within a view, it cannot be guaranteed that the every call within a database access produces the same result. Hence, later calls can produce later time stamps.

## Variant 6

`... TSTMP_SECONDS_BETWEEN(tstmp1,tstmp2,on_error)`

### Description

The function `TSTMP_SECONDS_BETWEEN` calculates the difference between two specified time stamps, `tstmp1` and `tstmp2` in seconds. The argument must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places and contain [valid time stamps](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. Any invalid time stamps produce an error. If `tstmp2` is greater than `tstmp1`, the result is positive. In the reverse case, it is negative.

The result is of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places.

The argument `on_error` controls error handling. It must have the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 10 and must have one of the following values:

- *FAIL* (an error raises an exception)

- *NULL* (an error returns the null value)

- *INITIAL* (an error returns the initial value)

The values are case-sensitive. Any incorrectly specified values raise an exception.

### Hint

`tstmp1` and `tstmp2` cannot be specified as literals. This is only possible indirectly by using a cast expression. For example, this is valid syntax:

`tstmp_seconds_between(cast(20200102122345 as abap.dec(15,0)),cast(20200401161034 as abap.dec(15,0)), 'FAIL') as demo`

## Variant 7

`... TSTMP_ADD_SECONDS(tstmp,seconds,on_error)`

### Description

The function `TSTMP_ADD_SECONDS` adds `seconds` seconds to a time stamp `tstmp`. The argument `tstmp` must have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places and contain a valid [time stamp](../../abap-programming-language/abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSS`. An invalid time stamp produces an error. The argument `seconds` must also have the built-in data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and no decimal places. Any negative values are subtracted. If the result is invalid, an error occurs.

The argument `on_error` controls error handling. The same applies as to the function `TSTMP_SECONDS_BETWEEN`. The additional value *UNCHANGED* can be used to specify that an error caused the unchanged value of `tstmp` to be returned.

### Hint

`tstmp` and `seconds` cannot be specified as literals. This is only possible indirectly by using cast expressions. For example, this is valid syntax:

`tstmp_add_seconds(cast(20200102122345 as abap.dec(15,0)),cast(5 as abap.dec(15,0)), 'FAIL') as demo`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view applies time stamp functions in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_TIMESTAMP_FNCTNS` uses `SELECT` to access the view. A current [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) time stamp is generated, seconds are added to a [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) time stamp and the difference in seconds between two [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) time stamps is calculated. The column `NUM1` of the DDIC database table is given a value that is added to a time stamp in the column `TIMESTAMP1` as seconds. The difference is found between this sum and a time stamp retrieved on the database by the function `TSTMP_CURRENT_UTCTIMESTAMP`. A delay, `wait`, can be integrated between the time stamp in the ABAP program and the time stamp created on the database.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_TSFNC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_timestamp_functions
  with parameters
    p_seconds :abap.int4
  as select from demo_expressions
{
  key id,
      utcl_current()                     as utcl_timestamp,
      utcl_add_seconds(utcl2,:p_seconds) as add_seconds,
      utcl_seconds_between(utcl1,utcl2)  as seconds_between,
      timestamp1                         as timestamp1,
      tstmp_is_valid(timestamp1)         as valid1,
      tstmp_seconds_between(
        tstmp_current_utctimestamp(),
        tstmp_add_seconds(
          timestamp1,
          cast( num1 as abap.dec(15,0) ),
          'FAIL'),
       'FAIL')                           as difference
}
```
