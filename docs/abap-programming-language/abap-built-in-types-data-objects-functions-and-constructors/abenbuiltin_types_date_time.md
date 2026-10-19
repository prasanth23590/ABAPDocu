---
title: "Built-In Date Types, Time Types, and Time Stamp Types"
source_file: abenbuiltin_types_date_time.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Types > Built-In ABAP Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Date Types, Time Types, and Time Stamp Types

The data objects of the date types, time types, and time stamp types are used to store calendar dates, times, and UTC time stamps.

**Attributes**

| **Type**  | **Length**   | **Standard Length** | **Meaning**                                       | **Data Object**                                     |
|-----------|--------------|---------------------|---------------------------------------------------|-----------------------------------------------------|
| `d`       | 8 characters |                     | [Date type](../../abap-glossary/abendate_type_glosry.md)            | [Date field](../../abap-glossary/abendate_field_glosry.md)            |
| `t`       | 6 characters |                     | [Time type](../../abap-glossary/abentime_type_glosry.md)            | [Time field](../../abap-glossary/abentime_field_glosry.md)            |
| `utclong` | 8 byte       |                     | [Time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) | [Time stamp field](../../abap-glossary/abentimestamp_field_glosry.md) |

**Value Ranges and Initial Values**

| **Type**  | **Value Range**                                                                                                                                                                                                                                                                                                                                                                            | **Initial Value**         |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| `d`       | Any eight Unicode characters that can be encoded in [UCS-2](../../abap-glossary/abenucs2_glosry.md); valid values are only digits that are valid as dates in accordance with the calendar rules in the format *yyyymmdd*: *yyyy* (year): 0001 to 9999, *mm* (month): 01 to 12, *dd* (day): 01 to 31                                                                                                          | *00000000*                |
| `t`       | Any six Unicode characters that can be encoded in [UCS-2](../../abap-glossary/abenucs2_glosry.md); valid values are only digits that are valid as times in accordance with the 24-hour clock range in the format *hhmmss*. *hh* (hours): 00 to 23, *mm* (minutes): 00 to 59, *ss* (seconds): 00 to 59.                                                                                                       | *000000*                  |
| `utclong` | Internal 8-byte integer representation of an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) exact to 100 nanoseconds, in ISO-8601 notation between *0001-01-01T00:00:00.0000000* and *9999-12-31T23:59:59.9999999*. There are 3,155,380,704,000,000,000 real values and one special [initial value](../abap-processing-internal-data/abenutclong.md). | [empty](../abap-processing-internal-data/abenutclong.md) |

## Hints

- Date types and time types `d` and `t`

  - The date types and time types are used to handle calendar date and time values. For more information on how to use them and their special handling, see [Date Fields and Time Fields](../abap-processing-internal-data/abencharacter_date_time.md).

  - From a technical perspective, the data types `d` and `t` are flat character-like types. The content of their data objects is stored according to the current [system code page](../../abap-glossary/abensystem_codepage_glosry.md).

  - As character-like data types, data objects of the data types `d` and `t` can be used like text fields of the type `c`. This applies in particular to structures with components of the types `d` and `t`.

  - The generic type [`clike`](abenbuilt_in_types_generic.md) also includes the types `d` and `t`.

  - Data objects of the types `d` and `t` behave like character-like objects in character-like operand positions and numeric in numeric operand positions.

  - The data types `d` and `t` are the built-in ABAP types that correspond to the special types [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_date_time_types.md), [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_date_time_types.md), and [`TIMS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_date_time_types.md), [`TIMN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_date_time_types.md) of the ABAP Dictionary.

  - The valid values of the data types `d` and `t` are a subset of their value range. ABAP statements that work with data objects of these types are only guaranteed to function correctly for operands with valid values.

- Time stamp type `utclong`

  - The time stamp type `utclong` represented internally by integer numbers replaces the [time stamps](../abap-processing-internal-data/abentime_stamps_packed.md) represented by packed numbers as the type for real [time stamp fields](../abap-processing-internal-data/abenutclong.md).

  - The data type `utclong` is the built-in ABAP type that corresponds to the special type [`UTCLONG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_date_time_types.md) in ABAP Dictionary.

  - The system class [`CL_ABAP_UTCLONG`](../abap-processing-internal-data/abentimestamp_system_class.md) for UTC time stamps in time stamp fields contains the minimum and maximum values of the type `utclong` as attributes.

  - Invalid values in time stamps, that is integer numbers outside of the string of valid values of [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md), can be created using [casting](../../abap-glossary/abencast_casting_glosry.md).

  - There is no UTC time stamp for the days missing due to the switch from the Julian to the Gregorian calendar. The time stamp *1582-10-04T23:59:59.9999999* is followed by the time stamp *1582-10-15T00:00:00.0000000*.

  - The [initial value](../abap-processing-internal-data/abenutclong.md) of `utclong` is a special value "empty", that is internally by integer number 0.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of date fields and time fields of the built-in ABAP types `d` and `t` and examples for their use. The declarations are made with the statement [`DATA`](../abap-declarations/abapdata.md) and using the declaration operator [`DATA`](../abap-declarations/abendata_inline.md).

``` abap
DATA: tomorrow  TYPE d, 
      next_hour TYPE t. 
 
FINAL(today) = cl_demo_date_time=>get_user_date( ). 
FINAL(now)   = cl_demo_date_time=>get_user_time( ). 
 
tomorrow  = today + 1. 
next_hour = ( now + 3600 ) / 3600 * 3600.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an UTC time stamp of the type `utclong` with the built-in function [`utclong_current`](../abap-processing-internal-data/abenutclong_current.md) and its conversion to date and time fields.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(ts) = utclong_current( ). 
 
FINAL(time_zone) = cl_demo_date_time=>get_user_time_zone( ). 
CONVERT UTCLONG ts 
        INTO DATE FINAL(dat) TIME FINAL(tim) 
        TIME ZONE time_zone. 
 
out->write( 
  |{ ts }\n| && 
  |{ dat }\n| && 
  |{ tim }|  ). 
 
out->display( ).
```
