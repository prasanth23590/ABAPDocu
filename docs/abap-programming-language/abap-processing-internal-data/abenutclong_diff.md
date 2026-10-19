---
title: "ts_func - utclong_diff"
source_file: abenutclong_diff.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamp Fields with Time Stamp Type > Time Stamp Functions (ts_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ts_func - utclong_diff

## Syntax

``` abap
... utclong_diff( high = time_stamp2 
                  low  = time_stamp1 ) ...  
```

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) calculates the time difference between the values of two time stamp fields `time_stamp2` and `time_stamp1`. The return value has the type `decfloat34` and contains the exact difference in seconds rounded to seven decimal places. If the UTC time stamp in `time_stamp2` is later than the UTC time stamp in `time_stamp1`, the result is positive. If the values are identical, the result is 0, otherwise it is negative.

Time stamp fields of the type [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md) containing valid UTC time stamps must be passed to the parameters `high` and `low`. `time_stamp2` and `time_stamp1` are [time-stamp-like expression positions](../../abap-glossary/abentimestamp_like_expr_pos_glosry.md). An initial time stamp is handled like the smallest possible value of a time stamp.

## Hints

- The system class [`CL_ABAP_UTCLONG`](abentimestamp_system_class.md) contains a method `DIFF` with multiple output parameters for days, hours, minutes, and seconds across which the time difference is spread instead of just one return parameter.

- If the function `utclong_diff` is used as an operand of an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md), the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `decfloat34` is produced.

- If the function `utclong_diff` is used as the [right side of an assignment](abenequals_return_values.md) or other operand positions in which the return value is converted, the decimal places are converted in accordance with the general conversion rules for [source field type `decfloat34`](abenconversion_type_decfloat.md), if necessary, and are not cut off. If the decimal places are to be cut off, the built-in function [`trunc`](abennumerical_functions.md) can be applied to the return value.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calculation of the time interval in microseconds of consecutive UTC time stamps from an internal table.

``` abap
DATA time_stamps TYPE TABLE OF utclong WITH EMPTY KEY. 
time_stamps = VALUE #( FOR i = 1 UNTIL i > 11 
                         ( utclong_current( ) ) ). 
cl_demo_output=>write( time_stamps ). 
 
TYPES diffs TYPE TABLE OF decfloat34 WITH EMPTY KEY. 
cl_demo_output=>display( 
  VALUE diffs( FOR _ts IN time_stamps FROM 2 INDEX INTO i 
               ( utclong_diff( 
                  high = _ts 
                  low  = time_stamps[ i - 1 ] ) * 1000000 ) ) ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CONVERSION_NO_DATE_TIME`

- *Cause:* A time stamp specified for `high` or `low` is invalid.

  *Runtime error:* `INVALID_UTCLONG`
