---
title: "CONVERT TIME STAMP"
source_file: abapconvert_time-stamp.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamps in Packed Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONVERT TIME STAMP

## Syntax

``` abap
CONVERT TIME STAMP time_stamp TIME ZONE tz   
        INTO [DATE dat]   
             [TIME tim] [DAYLIGHT SAVING TIME dst].  
```

## Description

This statement interprets the content of a packed number `time_stamp` as a [time stamp](abentime_stamps_packed.md) that represents an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) and converts it to the local date and the local time in the time zone specified in `tz` assigning the result to the variables `dat`, `tim`, and `dst`. At least one of the additions `DATE` or `TIME` must be specified. The conversion is performed in accordance with the [rules for time zones](abentime_zone_rules.md).

`time_stamp` and `tz` are [functional operand positions](../../abap-glossary/abenfunctional_position_glosry.md).

- The operand `time_stamp` must have the type `TIMESTAMP` or `TIMESTAMPL` from the ABAP Dictionary, in accordance with the ABAP type `p` with length 8 or `p` with length 11 and seven decimal places. Depending on the data type, the content is interpreted either as a time stamp in the [short form](abentime_stamps_packed.md) or as a time stamp in the [long form](abentime_stamps_packed.md). No other data types can be specified. If `time_stamp` does not contain a valid time stamp, the content of `dat` and `tim` is not changed, and `sy-subrc` is set to 12.

- The operand `tz` must be character-like and contain a [time zone](../../abap-glossary/abentime_zone_glosry.md) from the DDIC database table `TTZZ`.

  - If `tz` is initial, the UTC time stamp is not converted to a different time zone. The local date and time in the target fields match the UTC reference time. In this case, `sy-subrc` is set to 4.

  - If the specified time zone is not found in the DDIC database table `TTZZ`, the content of `dat` and `tim` is not changed and `sy-subrc` is set to 8.

  - If the [rule set](abentime_zone_rules.md) for the specified time zone is incomplete, an uncatchable exception is raised.

- The local date is assigned to `dat` as a return value of the data type `d`. The following can be specified for `dat`:

  - An existing variable to which the return value can be [converted](abenconversion_type_d.md).

  - An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of data type `d` is declared.

- The local time is assigned to `tim` as a return value of data type `t`. If the time stamp in `time_stamp` is in the [long form](abentime_stamps_packed.md), the fractions of seconds in the decimal places are ignored. The following can be specified for `tim`:

  - An existing variable to which the return value can be [converted](abenconversion_type_t.md).

  - An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of data type `t` is declared.

- If the time stamp in `time_stamp` for the time zone specified in `tz` is in daylight saving time, `dst` is given the value *X*. Otherwise it is given the value blank. The following can be specified for `dst`:

  - An existing variable of the type `c` with length 1

  - An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of data type `c` with length 1 is declared.

When time stamps are converted for the days between 5.10.1582 and 14.10.1582 that do not actually exist due to the switch from the Julian calendar to the Gregorian calendar, this returns the same results as the conversion for the days from 15.10.1582 to 24.10.1582, which do exist.

If `time_stamp` contains a valid value but produces an invalid date when combined with a valid time zone in `tz`, `dat` and `tim` are not modified and `sy-subrc` is set to 12.

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                                  |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | Time stamp was converted into the local time of the specified time zone and assigned to the target fields.                                   |
| 4              | Time stamp was assigned to the target fields without conversion into a local time.                                                           |
| 8              | Time stamp could not be converted because the specified time zone is not in the DDIC database table `TTZZ`.                                  |
| 12             | Time stamp could not be converted since `time_stamp` contains an invalid value or produces an invalid date when combined with the time zone. |

## Hints

- A current UTC time stamp can be created using the statement [`GET TIME STAMP`](abapget_time-stamp.md).

- It is now possible to use the return value for the daylight saving time in `dst` to distinguish duplicate local time specifications that can occur when UTC time stamps are converted into local time during the double hour in the switch from daylight saving to standard time.

- Usually, an invalid date can be created from a valid time stamp only by combining the first valid day with time zones west of UTC or the last valid day with time zones east of UTC.

- An initial packed number with the value 0 is not a valid time stamp and produces the value 12 in `sy-subrc`.

- An initial time zone `tz` corresponds to `UTC` only if the tables of the [rules for time zones](abentime_zone_rules.md) are filled correctly for the time zone UTC.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example for `CONVERT TIME STAMP` for time stamps in packed numbers functions in exactly the same way as the example for [`CONVERT UTCLONG`](abapconvert_utclong.md) for time stamps in time stamp fields.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
CONVERT TIME STAMP CONV timestamp( '20191103' && '053000' ) 
        TIME ZONE 'EST' 
        INTO DATE DATA(dat) TIME DATA(tim) 
        DAYLIGHT SAVING TIME DATA(dst). 
out->write( |{ dat DATE = ISO } { 
               tim TIME = ISO } { dst }| ). 
 
CONVERT TIME STAMP CONV timestamp( '20191103' && '063000' ) 
        TIME ZONE 'EST' 
        INTO DATE dat TIME tim 
        DAYLIGHT SAVING TIME dst. 
out->write( |{ dat DATE = ISO } { 
               tim TIME = ISO } { dst }| ). 
 
out->display( ).
```
