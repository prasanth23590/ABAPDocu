---
title: "sql_func - Time Zone Functions"
source_file: abensql_timezone_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Time Zone Functions

## Syntax

``` abap
... ABAP_SYSTEM_TIMEZONE( [on_error = on_error] ) 
  | ABAP_USER_TIMEZONE( [user     = user ][, 
                         on_error = on_error] ) ...  
```

### Variant

[1. `... ABAP_SYSTEM_TIMEZONE( ... )`](abensql_timezone_func.md#variant-1)

[2. `... ABAP_USER_TIMEZONE( ... )`](abensql_timezone_func.md#variant-2)

## Overview

### Description

These SQL functions return the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) and the user-dependent [user time zone](../../abap-glossary/abenuser_time_zone_glosry.md) of the current AS ABAP.

The arguments of the functions are specified as a comma-separated list in parentheses. A blank must be placed after the opening parenthesis and in front of the closing parenthesis. The functions have optional [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md) to which actual parameters can be assigned when called.

[SQL expressions](abapsql_expr.md), in particular individual columns, literals, SQL functions, host variables or host expressions can be specified as actual parameters. Only [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) of specific classes can be passed to the parameter `on_error`. If an actual parameter contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function returns a null value.

## Variant 1

`... ABAP_SYSTEM_TIMEZONE( ... )`

### Description

The function `ABAP_SYSTEM_TIMEZONE` returns the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) of the AS ABAP. Another optional parameter `client` must not be used in ABAP for Cloud Development.

The result has the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 6. If the system time zone cannot be detected, an error occurs.

The optional parameter `on_error` affects how errors are handled. The parameter for `on_error` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` from the class `SQL_ABAP_SYSTEM_TIMEZONE` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_ABAP_SYSTEM_TIMEZONE=>FAIL`, an error raises an exception (default)

- `SQL_ABAP_SYSTEM_TIMEZONE=>SET_TO_NULL`, an error returns the null value

## Variant 2

`... ABAP_USER_TIMEZONE( ... )`

### Description

The function `ABAP_USER_TIMEZONE` returns the [user time zone](../../abap-glossary/abenuser_time_zone_glosry.md) of AS ABAP for the [user name](../../abap-glossary/abenuser_name_glosry.md) passed to `user`.

The actual parameter for the optional formal parameter `user` must have the built-in type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 12. The default value is the user name of the current [ABAP user](../../abap-glossary/abenabap_user_glosry.md). Another optional parameter `client` must not be used in ABAP for Cloud Development.

The result has the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 6. If the user time zone cannot be detected, an error occurs.

The optional parameter `on_error` affects how errors are handled. The actual parameter for `on_error` must be an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `ON_ERROR` from the class `SQL_ABAP_USER_TIMEZONE` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

- `SQL_ABAP_USER_TIMEZONE=>FAIL`, an error raises an exception (default)

- `SQL_ABAP_USER_TIMEZONE=>SET_TO_NULL`, an error returns the null value

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `SELECT` statement returns the values for system time zone and user time zone that were read with the `ABAP_SYSTEM_TIMEZONE` and `ABAP_USER_TIMEZONE` functions for the current user. The class `CL_DEMO_SQL_TIMEZONE_FUNCTIONS` executes the statement and displays the result.

``` abap
SELECT SINGLE 
       FROM demo_expressions 
       FIELDS 
         abap_system_timezone( 
           on_error = @sql_abap_system_timezone=>set_to_null ) 
             AS system_tz, 
         abap_user_timezone( 
           user     = @sy-uname, 
           on_error = @sql_abap_user_timezone=>set_to_null ) 
             AS user_tz 
       INTO @FINAL(result).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The [example for date/time conversions](abensql_date_time_conversions.md) uses the function `ABAP_SYSTEM_TIMEZONE` without parameters being specified explicitly.
