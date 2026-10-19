---
title: "GET TIME STAMP"
source_file: abapget_time-stamp.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamps in Packed Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# GET TIME STAMP

## Syntax

``` abap
GET TIME STAMP FIELD time_stamp.  
```

## Description

This statement uses the [system time](../../abap-glossary/abensystem_time_glosry.md) and [system date](../../abap-glossary/abensystem_date_glosry.md) of the AS ABAP to create a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX](../../abap-glossary/abenposix_timestamp_glosry.md) standard and assigns it to the variable `time_stamp` of type `p` as a [time stamp in a packed number](abentime_stamps_packed.md).

The following can be specified for `time_stamp`:

- An existing variable of the data type `TIMESTAMP` or `TIMESTAMPL` from the ABAP Dictionary, in accordance with the ABAP type `p` with length 8 or `p` with length 11 and seven decimal places. Depending on the data type, the time stamp is created either in the [short form](abentime_stamps_packed.md) or in the [long form](abentime_stamps_packed.md).

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of type `TIMESTAMP` is declared.

## Hints

- The precision of the decimal places of the generated time stamp depends on the hardware (processor) of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md). Resolutions in the one-digit or two-digit microsecond range are realistic.

- A time stamp in its short form is the integer part of a time stamp in its long form. In order to create the respective short form from an existing long form time stamp, the value of the long form must be rounded down. This cannot be achieved by a simple assignment because the corresponding [`p` to `p`](abenconversion_type_p.md) conversion rule rounds commercially. Instead, an appropriate function such as [`round`](abendec_floating_point_functions.md) or [`trunc`](abennumerical_functions.md) can be used. Note that the methods `MOVE_TO_SHORT` and `MOVE` of the system class [`CL_ABAP_TSTMP`](abencl_abap_tstmp.md) prevent invalid results but also round commercially. See the executable example [Rounding Time Stamps in Packed Numbers](abenround_time_stamp_abexa.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of two time stamps. An existing variable of the type `TIMESTAMPL` must be used for the long form. An inline declaration can be used for the short form. The time stamps must be formatted specially for the output, since otherwise only numbers of type `p` would be displayed.

``` abap
DATA tsl TYPE timestampl. 
 
GET TIME STAMP FIELD FINAL(ts). 
GET TIME STAMP FIELD tsl. 
 
cl_demo_output=>new( 
  )->write( |{ ts  TIMESTAMP = ISO 
                   TIMEZONE = 'UTC' }| 
  )->write( |{ tsl TIMESTAMP = ISO 
                   TIMEZONE = 'UTC' }| 
  )->display( ).
```
