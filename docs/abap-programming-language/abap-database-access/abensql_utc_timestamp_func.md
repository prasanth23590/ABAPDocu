---
title: "sql_func - Functions for UTCLONG"
source_file: abensql_utc_timestamp_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions > sql_func - Time Stamp Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Functions for UTCLONG

## Syntax

``` abap
... UTCL_CURRENT( ) 
  | UTCL_ADD_SECONDS( utclong,seconds ) 
  | UTCL_SECONDS_BETWEEN( utclong1,utclong2 ) ...  
```

### Variant

[1. `... UTCL_CURRENT( )`](abensql_utc_timestamp_func.md#variant-1)

[2. `... UTCL_ADD_SECONDS( utclong,seconds )`](abensql_utc_timestamp_func.md#variant-2)

[3. `... UTCL_SECONDS_BETWEEN( utclong1,utclong2 )`](abensql_utc_timestamp_func.md#variant-3)

## Overview

### Description

These SQL functions perform operations with arguments of the built-in data type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 1

`... UTCL_CURRENT( )`

### Description

This function generates an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) from the [system time](../../abap-glossary/abensystem_time_glosry.md) and the [system date](../../abap-glossary/abensystem_date_glosry.md) of AS ABAP. The return value has the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

All columns of a query have the same time stamp.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Selects column `CARRID` from table `SCARR` and returns a time stamp for each row. The time stamp is generated only once for the query and, therefore, all rows have the same time stamp.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT carrid, utcl_current( ) AS time_stamp 
  FROM scarr 
  INTO TABLE @FINAL(result). 
 
out->display( result ).
```

## Variant 2

`... UTCL_ADD_SECONDS( utclong,seconds )`

### Description

The function `UTCL_ADD_SECONDS` adds `seconds` seconds to a time stamp `utclong`. It has two [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md). The actual parameter for the formal parameter `utclong` must have the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a [valid time stamp](../abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSSMMMUUUN`. An invalid time stamp produces the initial value. The actual parameter for the formal parameter `seconds` must have either the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or the data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places. Any negative values are subtracted. If the result is invalid, a catchable exception of class `CX_SY_OPEN_SQL_DB` is raised.

The result is of type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

## Variant 3

`... UTCL_SECONDS_BETWEEN( utclong1,utclong2 )`

### Description

The function `UTCL_SECONDS_BETWEEN` calculates the difference between two specified time stamps `utcl1` and `utcl2` in seconds. It has two [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md). The actual parameters for the formal parameters `utcl1` and `utcl2` must have the built-in dictionary type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and contain a [valid time stamp](../abap-processing-internal-data/abentime_stamps_packed.md) in the format `YYYYMMDDHHMMSSMMMUUUN`. Any invalid time stamps produce an error. If `utcl2` is greater than `utcl1`, the result is positive. If the values are identical, the result is 0. In all other cases, the result is negative.

The result is of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places.
