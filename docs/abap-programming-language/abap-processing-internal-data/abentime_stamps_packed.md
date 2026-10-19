---
title: "Time Stamps in Packed Numbers"
source_file: abentime_stamps_packed.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Time Stamps in Packed Numbers

In this format, [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) are represented using packed numbers of the type [`p`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md).

- [Representation of Time Stamps in Packed Numbers](abentime_stamps_packed.md#representation-of-time-stamps-in-packed-numbers)

- [Accessing Time Stamps in Packed Numbers](abentime_stamps_packed.md#accessing-time-stamps-in-packed-numbers)

- [Notes on Handling Time Stamps in Packed Numbers](abentime_stamps_packed.md#notes-on-handling-time-stamps-in-packed-numbers)

- [Examples for Time Stamps in Packed Numbers](abentime_stamps_packed.md#examples-for-time-stamps-in-packed-numbers)

## Representation of Time Stamps in Packed Numbers

There is a short form and a long form.

- In the short form, an UTC time stamp is represented precisely to the second using a packed number with length 8 without decimal places, and the ABAP Dictionary type `TIMESTAMP`. The digits of the packed number show the time stamp in the format *yyyymmddhhmmss*, where *yyyy* is the year, *mm* is the month, *dd* is the day, *hh* is the hour, *mm* are the minutes, and *ss* are the seconds.

- In the long form, an UTC time stamp is represented precisely to 100 ns using a packed number with length 11 and seven decimal places, and the ABAP Dictionary type `TIMESTAMPL` The digits of the packed number show the time stamp in the format *yyyymmddhhmmss.sssssss*, where, in addition to the short form, the seven decimal places *sssssss* are the fractions of a second. The maximum time resolution that can be achieved depends on the operating system of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md) and can be less.

In its integer part, a valid UTC time stamp must contain valid dates and times:

- For the date, only the values 01 to 9999 for the year, 01 to 12 for the month, and 01 to 31 for the day are valid.

- For the time, only the values 00 to 23 for the hours, and 00 to 59 for the minutes and seconds are valid.

- The date and time must represent a point in time that is valid in the Gregorian calendar.

Each valid value is handled as an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) that represents a unique time in [UTC](../../abap-glossary/abenutc_glosry.md) reference time. In accordance with the POSIX standard, [leap seconds](../../abap-glossary/abenleap_second_glosry.md) are not supported, that is, each day has exactly 86400 seconds.

### Hints

- An initial packed number with the value 0 does not contain a valid time stamp.

- The method `NORMALIZE` of class `CL_ABAP_TSTMP` can be used to convert invalid values in time stamps to valid values.

## Accessing Time Stamps in Packed Numbers

Only a few statements recognize that packed numbers of the types `TIMESTAMP` and `TIMESTAMPL` are UTC time stamps. All other statements interpret the content of these data types as numbers and, with the exception of direct comparisons, are not suitable for handling time stamps. The statements for handling time stamps in packed numbers are as follows:

- [`GET TIME STAMP`](abapget_time-stamp.md) creates a current UTC time stamp.

- [`CONVERT TIME STAMP`](abapconvert_time-stamp.md) converts an UTC time stamp to a local date and a local time.

- [`CONVERT INTO TIME STAMP`](abapconvert_date_time-stamp.md) converts a local date and a local time to an UTC time stamp.

Furthermore, UTC time stamps in packed numbers are handled specifically in the following output formats:

- Use of the options [`TIMESTAMP`](abapcompute_string_format_options.md) and [`TIMEZONE`](abapcompute_string_format_options.md) for [embedded expressions](abenstring_templates_expressions.md) in [string templates](abenstring_templates.md)

- Use of the addition `TIME ZONE` of the statement `WRITE [TO]`.

- The domains `XSDDATETIME_Z` and `XSDDATETIME_LONG_Z` support the serialization and deserialization of UTC time stamps in packed numbers in [asXML](../abap-data-interchange-formats/abenabap_xslt_asxml_schema.md) and [asJSON](../abap-data-interchange-formats/abenabap_asjson_schema.md).

The system class [`CL_ABAP_TSTMP`](abencl_abap_tstmp.md) provides methods for adding, subtracting, converting, and comparing UTC time stamps in packed numbers.

### Hint

Special [time stamp functions](../../abap-glossary/abenabap_cds_glosry.md) can be used in ABAP SQL and the CDS DDL of the ABAP CDS for processing UTC time stamps stored as packed numbers in database tables.

## Notes on Handling Time Stamps in Packed Numbers

UTC time stamps in packed numbers are only interpreted as such if they are accessed by the statements, methods, and functions listed above. When being assigned or converted, they behave like packed numbers of the type `p`, which means they are not suitable for direct calculations. Comparisons produce a meaningful result only when two UTC time stamps are compared with each other. In programs for which the program property [Fixed Point Arithmetic](../../abap-glossary/abenfixed_point_arithmetic_glosry.md) is not set, the corresponding rules applying to the data type `p` should be respected. In particular, direct comparisons of UTC time stamps in the long form with the short form produce a meaningful result only when the program property *fixed point arithmetic* is set. Otherwise, the system class `CL_ABAP_TSTMP` must be used for comparisons as well.

An UTC time stamp in its short form is the integer part of a time stamp in its long form. When simply assigning time stamps in the long form to time stamps in the short form, the [`p` to `p`](abenconversion_type_p.md) conversion rule applies and hence commercial rounding takes place. Therefore, unwanted rounding effects might occur that can even lead to invalid values, e.g. when seconds are rounded to 60. To avoid unwanted rounding effects, the following should be done instead of assignments:

- In order to avoid invalid values, the methods `MOVE_TO_SHORT` and `MOVE` of the system class [`CL_ABAP_TSTMP`](abencl_abap_tstmp.md) can be used. But these methods also round commercially.

- In order to achieve the same integer part, the UTC time stamp in the long form must be rounded down. This can be achieved by using the built-in function [`round`](abendec_floating_point_functions.md) with an appropriate mode or [`trunc`](abennumerical_functions.md).

See also the executable example [Rounding Time Stamps in Packed Numbers](abenround_time_stamp_abexa.md).

When UTC time stamps in packed numbers are used in operand positions that are not specifically intended for them, no warnings are given by the syntax check, not even in [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md).

## Examples for Time Stamps in Packed Numbers

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Direct comparison of UTC time stamps in packed numbers with the same data type.

``` abap
GET TIME STAMP FIELD FINAL(ts2). 
WAIT UP TO 1 SECONDS. 
GET TIME STAMP FIELD FINAL(ts1). 
 
ASSERT ts2 < ts1.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of an UTC time stamp in a packed number to a date and a time field, and determination of the daylight saving time marker.

``` abap
GET TIME STAMP FIELD FINAL(ts). 
 
CONVERT TIME STAMP ts TIME ZONE 
        cl_demo_date_time=>get_user_time_zone( ) 
        INTO DATE FINAL(date) TIME FINAL(time) 
        DAYLIGHT SAVING TIME FINAL(dst). 
 
cl_demo_output=>display( |{ date }\n{ 
                            time }\n{ 
                            dst } | ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Formatting of an UTC time stamp in a packed number in a string template in a type-friendly way.

``` abap
GET TIME STAMP FIELD FINAL(ts). 
 
cl_demo_output=>display( |{ ts TIMESTAMP = ISO } | ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serialization of an UTC time stamp in a packed number by using a special domain.

``` abap
DATA ts TYPE xsddatetime_z. 
GET TIME STAMP FIELD ts. 
 
CALL TRANSFORMATION id SOURCE ts = ts 
                       RESULT XML FINAL(xml). 
cl_demo_output=>display_xml( xml ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calculation of the difference between two UTC time stamps in packed numbers using the class `CL_ABAP_TSTMP`.

``` abap
DATA: ts1 TYPE timestampl, 
      ts2 TYPE timestampl. 
 
GET TIME STAMP FIELD ts2. 
WAIT UP TO 1 SECONDS. 
GET TIME STAMP FIELD ts1. 
 
FINAL(seconds) = cl_abap_tstmp=>subtract( 
    EXPORTING 
      tstmp1 = ts1 
      tstmp2 = ts2 ). 
 
cl_demo_output=>display( seconds ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Direct calculation using UTC time stamps in packed numbers. If, for example, `ts1` has the value *20161004130733*, adding 3600 s in `ts2` produces the value *20161004140733*. Since the time stamps are interpreted as numbers of type `p` in the calculation, the result is `10000`, which would generally be unexpected.

``` abap
GET TIME STAMP FIELD FINAL(ts1). 
 
FINAL(ts2) = cl_abap_tstmp=>add( tstmp = ts1 
                                secs  = 3600 ). 
 
cl_demo_output=>display( ts2 - ts1 ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Incorrect calculation using UTC time stamps in packed numbers. The assumption here is that time stamps are interpreted as a number of seconds in calculations. This is not the case here. The result does not meet expectations and is generally not a valid time stamp. For example, the invalid value *20161004315506* is calculated from `20161004131906`.

``` abap
GET TIME STAMP FIELD DATA(ts). 
 
ts = ts + 86400 * 2 + 3600 * 3. 
 
cl_demo_output=>display( ts ).
```
