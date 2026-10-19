---
title: "CDS DDL - DDIC-Based View, Date Functions"
source_file: abencds_date_functions_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, Special Functions > CDS DDL - DDIC-Based View, Date Functions and Time Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Date Functions

## Syntax

``` abap
... DATN_DAYS_BETWEEN(date1,date2) 
  | DATN_ADD_DAYS(date,days) 
  | DATN_ADD_MONTHS(date,months) 
  | DATS_IS_VALID(date) 
  | DATS_DAYS_BETWEEN(date1,date2) 
  | DATS_ADD_DAYS(date,days,on_error) 
  | DATS_ADD_MONTHS(date,months,on_error) ...  
```

### Variant

[1. `... DATN_DAYS_BETWEEN(date1,date2)`](abencds_date_functions_v1.md#variant-1)

[2. `... DATN_ADD_DAYS(date,days)`](abencds_date_functions_v1.md#variant-2)

[3. `... DATN_ADD_MONTHS(date,months)`](abencds_date_functions_v1.md#variant-3)

[4. `... DATS_IS_VALID(date)`](abencds_date_functions_v1.md#variant-4)

[5. `... DATS_DAYS_BETWEEN(date1,date2)`](abencds_date_functions_v1.md#variant-5)

[6. `... DATS_ADD_DAYS(date,days,on_error)`](abencds_date_functions_v1.md#variant-6)

[7. `... DATS_ADD_MONTHS(date,months,on_error)`](abencds_date_functions_v1.md#variant-7)

## Overview

### Description

In a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), these functions execute operations with arguments of the built-in data types [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The functions have [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) to which actual parameters need to be assigned when called. There are currently no optional parameters. Suitable fields of a [data source](abencds_data_source_v1.md), [literals](abencds_literal_v1.md), [parameters](abencds_parameter_v1.md), [path expressions](abencds_path_expression_v1.md), built-in functions, or expressions can all be specified as actual parameters. Only literals can be passed to the parameter `on_error`. If an actual parameter contains the [null value](../../abap-glossary/abennull_value_glosry.md), every function except `DATS_IS_VALID` returns a null value.

### Hint

The session variable [`$session.system_date`](abencds_session_variable_v1.md) is used in a CDS view to provide direct access to the current system date. In addition, special annotation [`@Environment.systemField`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) makes it possible to pass the value of the [ABAP system field](../../abap-glossary/abensystem_field_glosry.md) `sy-datum` to [input parameters](abencds_parameter_list_v1.md).

## Variant 1

`... DATN_DAYS_BETWEEN(date1,date2)`

### Description

The function `DATN_DAYS_BETWEEN` calculates the difference between two specified dates, `date1` and `date2`, in days. The actual parameters must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and must contain a valid date in the format `YYYYMMDD`. The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `date2` is greater than `date1`, the result is positive. In the reverse case, the result is negative. If the result is outside of the range of valid dates, an error occurs.

### Hints

- Empty literals are not possible.

- If an actual parameter is assigned the literal input '00000000', it is set to the initial value and the value *00010101* is used for the calculation.

- The days missing from the Gregorian calendar (from 5.10.1582 to 15.10.1582) are [handled as usual](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) in ABAP.

## Variant 2

`... DATN_ADD_DAYS(date,days)`

### Description

The function `DATN_ADD_DAYS` adds `days` days to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and it must contain a valid date in the format `YYYYMMDD`.

- The actual parameter `days` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `days` is positive, the number of days is added to `date`. In other cases, the number of days is subtracted. If the calculation produces an invalid date, an error occurs.

### Hints

- Literals are not possible for parameter `date`.

- The days missing from the Gregorian calendar (from 5.10.1582 to 15.10.1582) are [handled as usual](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) in ABAP.

## Variant 3

`... DATN_ADD_MONTHS(date,months)`

### Description

The function `DATN_ADD_MONTHS` adds `months` months to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and it must contain a valid date in the format `YYYYMMDD`.

- The actual parameter `months` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The result has the data type [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `months` is positive, the number of months is added to `date`. In other cases, the number of months is subtracted.

An attempt is made to create a date with the same day in an earlier or later month. If the target month has fewer days than the source month, the last day of the target month is returned. If the calculation produces an invalid date, an error occurs.

### Hints

- Literals are not possible for parameter `date`.

- The days missing from the Gregorian calendar (from 5.10.1582 to 15.10.1582) are [handled as usual](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) in ABAP.

## Variant 4

`... DATS_IS_VALID(date)`

### Description

The function `DATS_IS_VALID` determines whether `date` contains a valid date in the format `YYYYMMDD`. The actual parameter must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). A valid date produces the value 1 and all other input values (including the null value) produce the value 0.

### Hint

The value *00010101* is a valid date but the value *00000000* is not.

## Variant 5

`... DATS_DAYS_BETWEEN(date1,date2)`

### Description

The function `DATS_DAYS_BETWEEN` calculates the difference between two specified dates, `date1` and `date2`, in days. The actual parameters must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. Any invalid dates specified are initialized or set to the value *00010101* before the calculation. The result has the data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `date2` is greater than `date1`, the result is positive. In the reverse case, it is negative.

### Hint

Before the difference is calculated, the specified dates are converted to integers, like in ABAP, and the corresponding [rules](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) apply.

## Variant 6

`... DATS_ADD_DAYS(date,days,on_error)`

### Description

The function `DATS_ADD_DAYS` adds `days` days to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. Any invalid date specified is initialized or set to the value *00010101* before the calculation.

- The actual parameter `days` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- The actual parameter `on_error` must have the built-in data type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 10 and must have one of the following values:

  - *FAIL* (an error raises an exception)

  - *NULL* (an error returns the null value)

  - *INITIAL* (an error returns the initial value)

  - *UNCHANGED* (an error returns the unmodified value of `date`)

The values are case-sensitive. Any incorrectly specified values raise an exception.

The result has the data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `days` is positive, the number of days is added to `date`. In other cases, the number of days is subtracted. If the calculation produces an invalid date, the error is handled as specified in `on_error`.

### Hint

For the calculation, the specified date is [converted](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_d.md) to an integer, like in ABAP, and the result is [converted](../../abap-programming-language/abap-processing-internal-data/abenconversion_type_ibs.md) to a date again while applying the corresponding rules.

## Variant 7

`... DATS_ADD_MONTHS(date,months,on_error)`

### Description

The function `DATS_ADD_MONTHS` adds `months` months to a specified date `date`.

- The actual parameter `date` must have the built-in data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and should contain a valid date in the format `YYYYMMDD`. Any invalid date specified is initialized or set to the value *00010101* before the calculation.

- The actual parameter `months` must have the built-in data type [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- The same applies to the actual parameter `on_error` as to `DATS_ADD_DAYS`.

The result has the data type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). If `months` is positive, the number of months is added to `date`. In other cases, the number of months is subtracted.

An attempt is made to create a date with the same day in an earlier or later month. If the maximum day possible in a month is exceeded, the greatest possible day is used. If the calculation produces an otherwise invalid date, the error is handled as specified in `on_error`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view applies date functions in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_DATE_FUNCTIONS` uses `SELECT` to access the view. The columns `DATN1`, `DATN2`, `DATS1` and `DATS2` in the database table and the actual parameters for the input parameters of the view can be given any values. In the case of `DATS_ADD_DAYS` and `DATS_ADD_MONTHS`, invalid values or values that produce invalid results are handled as specified in the view.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_DATFNC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_date_functions
  with parameters
    p_days   :abap.int4,
    p_months :abap.int4
  as select from demo_expressions
{
  key id,
      dats1                                   as date1,
      dats_is_valid(dats1)                    as valid1,
      dats2                                   as date2,
      dats_is_valid(dats2)                    as valid2,
      dats_days_between(dats1,dats2)          as difference,
      dats_add_days(dats1,:p_days,'INITIAL')  as day1,
      dats_add_months(dats2,:p_months,'FAIL') as day2,
      datn1                                   as date3,
      datn2                                   as date4,
      datn_days_between( datn1, datn2 )       as days_between,
      datn_add_days( datn1,:p_days )          as add_days,
      datn_add_months( datn1,1 )              as add_month
}
```
