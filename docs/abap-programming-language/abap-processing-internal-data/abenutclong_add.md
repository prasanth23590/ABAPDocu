---
title: "ts_func - utclong_add"
source_file: abenutclong_add.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamp Fields with Time Stamp Type > Time Stamp Functions (ts_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ts_func - utclong_add

## Syntax

``` abap
... utclong_add( val  = time_stamp [days = days] 
                                   [hours = hours] 
                                   [minutes = minutes] 
                                   [seconds = seconds] ) ...  
```

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) adds the values passed to the optional parameters to an UTC [time stamp](../../abap-glossary/abentime_stamp_glosry.md) specified after `val`. The type of the return value is [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md).

A time stamp field of the type `utclong` that contains a valid UTC time stamp must be passed to the parameter `val`. `time_stamp` is a [time-stamp-like expression position](../../abap-glossary/abentimestamp_like_expr_pos_glosry.md). An initial time stamp is handled like the smallest possible value of a time stamp.

The values to be added are passed in the following parameters, of which at least one must be specified:

- `days` expects a number of days as a number of the type `i`.

- `hours` expects a number of hours as a number of the type `i`.

- `minutes` expects a number of minutes as a number of the type `int8`.

- `seconds` expects a number of seconds as a number of the type `decfloat34`.

Each parameter can be passed data objects that can be converted to the expected type. Positive and negative numbers can be passed. These are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md). Internally, the passed values are transformed to the corresponding number of seconds, whereby the value passed to `seconds` is rounded to seven decimal places. First, the days, hours, and minutes, and then seconds are added to or subtracted from the value of the UTC time stamp. If an invalid UTC time stamp value is produced by one of the intermediate steps, a catchable exception of the class `CX_SY_ARITHMETIC_OVERFLOW` is raised.

## Hints

- `utclong_subtract` is not available, since its function is achieved by passing negative numbers to the parameter `utclong_add`.

- There are no parameters for years and months, since they do not correspond to a fixed number of seconds.

- The result of the function `utclong_add` is never the initial value of an UTC time stamp. It is either a valid time stamp value or an exception is raised.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the function `utclong_add` works. The corresponding number of seconds is subtracted from a time stamp field `ts_new`, which itself is produced by adding days, hours, and minutes. The statement [`ASSERT`](../abap-program-maintenance/abapassert.md) demonstrates how this produces the original time stamp again.

``` abap
FINAL(ts) = utclong_current( ). 
 
FINAL(ts_new) = 
  utclong_add( val     = ts 
               days    = 1000 
               hours   = 100 
               minutes = 10 ). 
 
ASSERT ts = 
  utclong_add( val     = ts_new 
               seconds = - ( 1000 * 86400 + 100 * 3600 + 10 * 60 ) ). 
 
cl_demo_output=>display( |{ ts }\n{ ts_new }| ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the initial value is handled by `utclong_add`. One second is added to a time stamp `ts_ini` passed as an initial value and one second is subtracted from the result in `ts_1`. The result `ts_0` is the smallest valid time stamp value and not the initial value.

``` abap
FINAL(o) = cl_demo_output=>new( ). 
 
DATA ts_ini TYPE utclong. 
 
IF ts_ini IS INITIAL. 
  o->write( 'ts_ini is initial' ). 
ENDIF. 
o->write( ts_ini ). 
 
FINAL(ts_1) = 
  utclong_add( val     = ts_ini 
               seconds = 1 ). 
 
o->write( ts_1 ). 
 
FINAL(ts_0) = 
  utclong_add( val     = ts_1 
               seconds = -1 ). 
 
IF ts_0 IS NOT INITIAL AND 
   ts_0 <> ts_ini. 
  o->write( 'ts_0 is neither initial nor equal to ts_ini' ). 
ENDIF. 
o->write( ts_0 ). 
 
o->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows how missing days due to the switch from the Julian to the Gregorian calendar are handled by `utclong_add`. Adding 100 ns to the time stamp *1582-10-04 23:59:59.9999999* produces the time stamp *1582-10-15T00:00:00.0000000*.

``` abap
FINAL(ts) = conv utclong( '1582-10-04 23:59:59,9999999' ). 
 
FINAL(ts_new) = 
  utclong_add( val     = ts 
               seconds    = '0.0000001' ). 
 
cl_demo_output=>display( |{ ts }\n{ ts_new }| ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CONVERSION_NO_DATE_TIME`

- *Cause:* The time stamp specified for `val` is invalid.

  *Runtime error:* `INVALID_UTCLONG`

`CX_SY_CONVERSION_ERROR`

- *Cause:* A passed parameter cannot be converted to the expected type.

  *Runtime error:* `CONVT_OVERFLOW`, `BCD_OVERFLOW`

`CX_SY_ARITHMETIC_OVERFLOW`

- *Cause:* The parameters passed produce an invalid time stamp.

  *Runtime error:* `UTCLONG_ADD_OVERFLOW`
