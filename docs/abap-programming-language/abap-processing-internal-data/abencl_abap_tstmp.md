---
title: "System Class for Time Stamps in Packed Numbers"
source_file: abencl_abap_tstmp.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamps in Packed Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Class for Time Stamps in Packed Numbers

The class `CL_ABAP_TSTMP` is used to calculate and convert UTC [time stamps in packed numbers](abentime_stamps_packed.md). Important methods include:

- The methods `ADD`, `SUBTRACTSECS`, `ADD_TO_SHORT`, `ADD_TO_SHORT_TRUNC`, `SUBTRACTSECS_TO_SHORT` and `SUBTRACTSECS_TO_SHORT_TRUNC` add or subtract seconds from UTC time stamps and avoid invalid values. `ADD_TO_SHORT` and `ADD_TO_SHORT_TRUNC` round commercially. `SUBTRACTSECS_TO_SHORT` and `SUBTRACTSECS_TO_SHORT_TRUNC` round down.

- The method `TD_SUBTRACT` calculates the difference between two UTC time stamps.

- The methods `MOVE_TO_SHORT` and `MOVE_TO_SHORT_TRUNC` convert the long form of UTC time stamps to the short form, avoiding invalid values. `MOVE_TO_SHORT` rounds commercially. `MOVE_TO_SHORT_TRUNC` rounds down.

- The methods `MOVE` and `MOVE_TRUNC` convert the long form of UTC time stamps to the short form and vice versa, avoiding invalid values. `MOVE` rounds commercially. `MOVE_TRUNC` rounds down.

- The method `NORMALIZE` normalizes UTC time stamps. Invalid time stamps are converted into valid UTC time stamps according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md).

- The methods `UTCLONG2TSTMP`, `UTCLONG2TSTMP_SHORT`, and `TSTMP2UTCLONG` convert the content of time stamp fields to representation in packed numbers and vice versa.

## Hints

- Conversions between time stamp fields and packed numbers are necessary if time stamp fields are used in new programs, but existing repositories or interfaces need to be accessed at the same time.

- The methods `MOVE`, `MOVE_TO_SHORT`, `ADD_TO_SHORT` and `SUBTRACTSECS_TO_SHORT` can be used for converting long time stamps to short time stamps. These methods avoid invalid values but round the fractional seconds of long time stamps commercially. That might be unexpected. In order to preserve the integer part of a long time stamp it must be rounded down. For that the methods `MOVE_TRUNC`, `MOVE_TO_SHORT_TRUNC`, `ADD_TO_SHORT_TRUNC` and `SUBTRACTSECS_TO_SHORT_TRUNC` can be used. See also executable example [Rounding Time Stamps in Packed Numbers](abenround_time_stamp_abexa.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a one hour earlier UTC time stamp by subtracting 3600 seconds.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
GET TIME STAMP FIELD FINAL(ts1). 
 
FINAL(ts2) = cl_abap_tstmp=>subtractsecs( tstmp = ts1 
                                          secs  = 3600 ). 
 
out->write( |{ ts1 TIMESTAMP = ISO 
                       }\n{ ts2 TIMESTAMP = ISO }| ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of a time stamp field to time stamps in packed numbers. In formatting using string templates, the formatting option [`TIMESTAMP`](abapcompute_string_format_options.md) must be specified for the packed numbers to define a representation as time stamps.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(ts) = utclong_current( ). 
 
out->write( 
  |{ ts }\n{ 
     cl_abap_tstmp=>utclong2tstmp( ts ) TIMESTAMP = ISO }\n{ 
     cl_abap_tstmp=>utclong2tstmp_short( ts ) TIMESTAMP = ISO }| ). 
 
out->display( ).
```
