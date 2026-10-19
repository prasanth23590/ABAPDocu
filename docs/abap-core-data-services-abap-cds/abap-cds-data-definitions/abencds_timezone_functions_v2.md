---
title: "CDS DDL - CDS View Entity, Time Zone Functions"
source_file: abencds_timezone_functions_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, Special Functions > CDS DDL - CDS View Entity, Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Time Zone Functions

## Syntax

``` abap
... ABAP_SYSTEM_TIMEZONE(clnt,on_error) 
  | ABAP_USER_TIMEZONE(user,clnt,on_error) ...  
```

### Variant

[1. `... ABAP_SYSTEM_TIMEZONE(clnt,on_error)`](abencds_timezone_functions_v2.md#variant-1)

[2. `... ABAP_USER_TIMEZONE(user,clnt,on_error)`](abencds_timezone_functions_v2.md#variant-2)

## Overview

### Description

In a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), these functions return the client-dependent [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) and the user-dependent [user time zone](../../abap-glossary/abenuser_time_zone_glosry.md) of the current AS ABAP. The functions have [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) to which actual parameters must be assigned when called. There are currently no optional parameters. Suitable fields of a [data source](abencds_data_source_v2.md), [literals](abencds_literal_v2.md), [parameters](abencds_parameter_v2.md), [path expressions](abencds_path_expression_v2.md), [built-in functions](abencds_builtin_functions_v2.md), [SQL-based scalar functions](abencds_sql_scalar_function.md), [expressions](abencds_expressions_v2.md), or [reuse expressions](abencds_reusable_expression_v2.md) using `$projection` can all be specified as actual parameters. Only literals can be passed to the parameter `on_error`. If an actual parameter contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function returns a null value.

### Hint

For [user time zone](../../abap-glossary/abenuser_time_zone_glosry.md), there is also the [session variable](abencds_session_variable_v2.md) `user_timezone` available. It returns the same result as the built-in function `ABAP_USER_TIMEZONE`.

## Variant 1

`... ABAP_SYSTEM_TIMEZONE(clnt,on_error)`

### Description

The function `ABAP_SYSTEM_TIMEZONE` returns the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) of the AS ABAP for the [client](../../abap-glossary/abenclient_glosry.md) specified with `clnt`. The actual parameter `clnt` must have the built-in dictionary type [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid [client ID](../../abap-glossary/abenclient_identifier_glosry.md). In [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), only the session variable [`$session.client`](abencds_session_variable_v2.md) can be specified for `clnt`.

The result has the [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) type with a length of 6. If the system time zone cannot be determined, an error is raised.

The actual parameter `on_error` controls error handling. It must have the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 10 and must have one of the following values:

- *FAIL* (an error raises an exception)

- *NULL* (an error returns the null value)

- *INITIAL* (an error returns the initial value)

The values are case-sensitive. Any incorrectly specified values raise an exception.

### Hint

The system time zone returned is the client-dependent content of column `TZONESYS` in DDIC database table `TTZCU`.

## Variant 2

`... ABAP_USER_TIMEZONE(user,clnt,on_error)`

### Description

The function `ABAP_USER_TIMEZONE` returns the [user time zone](../../abap-glossary/abenuser_time_zone_glosry.md) of the AS ABAP for the [ABAP user](../../abap-glossary/abenabap_user_glosry.md) specified with `user` and the [client](../../abap-glossary/abenclient_glosry.md) specified with `clnt`. The actual parameter `user` must have the built-in type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The same applies to the actual parameter `clnt` as to function `ABAP_SYSTEM_TIMEZONE`. The result has the [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) type with a length of 6. If the user time zone cannot be determined, an error is raised.

The actual parameter `on_error` controls error handling and the same applies as in function `ABAP_SYSTEM_TIMEZONE`.

### Hint

For the [current client](../../abap-glossary/abencurrent_client_glosry.md), the returned user time zone corresponds with the content of system field [`sy-zonlo`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md) in ABAP.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `SELECT` statement returns the values for system time zone and user time zone that were read with the `ABAP_SYSTEM_TIMEZONE` and `ABAP_USER_TIMEZONE` functions for the current client and current user. The actual parameters of the functions are supplied with suitable [session variables](../../abap-glossary/abensession_variable_glosry.md). The class `CL_DEMO_CDS_TIMEZONE_FUNC_VE` accesses the view, compares the CDS values with the corresponding ABAP values, and returns the result.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_TIMEZONE_FUNC_VE
  as select from demo_expressions
{
  key id,
      abap_system_timezone( $session.client,'NULL' )      as system_tz,
      abap_user_timezone(   $session.user,$session.client,'NULL' ) 
                                                          as user_tz,
      $session.user_timezone as user_tz_session_var
}
```
