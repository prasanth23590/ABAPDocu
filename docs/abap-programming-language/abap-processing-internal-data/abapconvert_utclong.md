---
title: "CONVERT UTCLONG"
source_file: abapconvert_utclong.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamp Fields with Time Stamp Type > Conversion Statements for Time Stamp Fields"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONVERT UTCLONG

## Syntax

``` abap
CONVERT UTCLONG time_stamp 
        INTO [DATE dat] 
             [TIME tim [FRACTIONAL SECONDS fs]] 
             [DAYLIGHT SAVING TIME dst] 
             TIME ZONE tz.  
```

## Description

This statement handles the [time stamp](../../abap-glossary/abentime_stamp_glosry.md) contained in a [time stamp field](../../abap-glossary/abentimestamp_field_glosry.md) `time_stamp` as an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) and converts it to the local date and local time of the time zone specified in `tz` assigning the result to the variables `dat`, `tim`, and `dst`. At least one of the additions `DATE`, `TIME`, or `DAYLIGHT SAVING TIME` must be specified. The conversion is performed in accordance with the [rules for time zones](abentime_zone_rules.md).

`time_stamp` is a [time-stamp-like expression position](../../abap-glossary/abentimestamp_like_expr_pos_glosry.md) and `tz` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

- The operand `time_stamp` must be of the type [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), which contains a valid time stamp. If `time_stamp` does not contain a valid time stamp, a catchable exception of the class `CX_SY_CONVERSION_NO_DATE_TIME` is raised.

- The operand `tz` must be character-like and contain a [time zone](../../abap-glossary/abentime_zone_glosry.md) from the DDIC database table `TTZZ`.

  - If `tz` is initial, the UTC time stamp is not converted to a different time zone. The local date and time in the target fields correspond to the UTC reference time.

  - If the specified time zone is not found in the DDIC database table `TTZZ`, a catchable exception of the class `CX_SY_CONVERSION_NO_DATE_TIME` is raised, unless the time stamp is initial.

  - If the [rule set](abentime_zone_rules.md) for the specified time zone is incomplete, an uncatchable exception is raised.

- The local date is assigned to `dat` as a return value of the data type `d`. The following can be specified for `dat`:

  - An existing variable of type `d`.

  - An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of data type `d` is declared.

- The local time without the fractions of seconds is assigned to `tim` as a return value of data type `t`. The following can be specified for `tim`:

  - An existing variable of type `t`.

  - An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of data type `t` is declared.

- The fractions of seconds are assigned to `fs` as a return value of the data type `decfloat34`. The following can be specified for `fs`:

  - An existing variable of the type `decfloat34`.

  - An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of data type `decfloat34` is declared.

- If the time stamp in `time_stamp` for the time zone specified in `tz` is in daylight saving time, `dst` is given the value *X*. Otherwise it is given the value blank. The following can be specified for `dst`:

  - An existing variable of the type `c` with length 1

  - An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of data type `c` with length 1 is declared.

Regardless of the time zone specified, an initial time stamp generates type-dependent [initial values](../../abap-glossary/abeninitial_value_glosry.md) in all target fields. If the time stamp has the minimum value *0001-01-01T00:00:00.0000000* or is in the last possible second *9999-12-31T23:59:59.fffffff* no time shift is calculated. A time stamp whose value is greater than or equal to the last second or is between *9999-12-31 23:59:59.0000000* and *9999-12-31 23:59:59.9999999* is handled like the maximum value *9999-12-31 23:59:59.9999999*.

If `time_stamp` contains a valid value but results in an invalid date in combination with a valid time zone in `tz`, a catchable exception of the class `CX_SY_CONVERSION_NO_DATE_TIME` is raised.

## Hints

- A current UTC time stamp can be created with the built-in function [`utclong_current`](abenutclong_current.md).

- The return value for the daylight saving time in `dst` can be used to distinguish duplicate local time specifications that occur when UTC time stamps are converted into local time within the double hour in the switch between daylight saving and standard time.

- Usually, an invalid date and the associated exception can be created from a valid time stamp only by combining the first valid day with time zones west of UTC or the last valid day with time zones east of UTC.

- An initial time zone `tz` only corresponds to `UTC` if the tables of the [rules for time zones](abentime_zone_rules.md) are filled correctly for the time zone UTC.

- The statement `CONVERT INTO UTCLONG` does not set the return value `sy-subrc`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For the time zone *EST* in the DDIC database table `TTZZ`, a shift of -5 hours from the UTC reference time is entered in the DDIC database table `TTZR`. In the DDIC database table `TTZDV`, the end of daylight saving time is defined as the first Sunday in November at 02:00 using the key *USA*. In 2019, the first Sunday is November 03. With these settings in the rule set, the two conversions below both result in the same local time of *01:30:00*. The first conversion shows that the time is still in daylight saving time.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
CONVERT UTCLONG CONV utclong( '2019-11-03 05:30:00' ) 
        INTO DATE DATA(dat) 
             TIME DATA(tim) 
             DAYLIGHT SAVING TIME DATA(dst) 
             TIME ZONE 'EST'. 
out->write( |{ dat DATE = ISO } { 
               tim TIME = ISO } { dst }| ). 
 
CONVERT UTCLONG CONV utclong( '2019-11-03 06:30:00' ) 
        INTO DATE dat 
             TIME tim 
             DAYLIGHT SAVING TIME dst 
             TIME ZONE 'EST'. 
out->write( |{ dat DATE = ISO } { 
               tim TIME = ISO } { dst }| ). 
 
out->display( ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CONVERSION_NO_DATE_TIME`

- *Cause:* Invalid time zone in `tz`.

  *Runtime error:* `INVALID_TIME_ZONE`

- *Cause:* An invalid date would be generated.

  *Runtime error:* `LOCAL_TIMESTAMP_OUT_OF_RANGE`

- *Cause:* The specified time stamp is invalid.

  *Runtime error:* `INVALID_UTCLONG`
