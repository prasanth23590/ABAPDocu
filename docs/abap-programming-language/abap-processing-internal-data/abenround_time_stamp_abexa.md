---
title: "Rounding Time Stamps in Packed Numbers"
source_file: abenround_time_stamp_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamps in Packed Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Rounding Time Stamps in Packed Numbers

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates different rounding behaviors for UTC time stamps stored in packed numbers.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_round_time_stamp DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_round_time_stamp IMPLEMENTATION. 
  METHOD main. 
 
    DATA ts_pack     TYPE timestamp. 
    DATA ts_packlong TYPE timestampl. 
    DATA ts_utclong  TYPE utclong. 
 
    DATA(frac) = 0. 
    WHILE frac < '0.5'. 
      GET TIME STAMP FIELD ts_packlong. 
      GET TIME STAMP FIELD ts_pack. 
      ts_utclong = utclong_current( ). 
 
      DATA utclong_2_short TYPE timestamp. 
      utclong_2_short = 
        cl_abap_tstmp=>utclong2tstmp_short( ts_utclong ). 
 
      DATA assigned_to_short TYPE timestamp. 
      assigned_to_short =  ts_packlong ##type. 
 
      DATA moved_to_short TYPE timestamp. 
      moved_to_short = cl_abap_tstmp=>move_to_short( ts_packlong ). 
 
      DATA moved_to_short_trunc TYPE timestamp. 
      moved_to_short_trunc = cl_abap_tstmp=>move_to_short_trunc( 
                                                      ts_packlong ). 
 
      DATA moved TYPE timestamp. 
      cl_abap_tstmp=>move( EXPORTING tstmp_src = ts_packlong 
                           IMPORTING tstmp_tgt = moved ). 
 
      DATA moved_trunc TYPE timestamp. 
      cl_abap_tstmp=>move_trunc( EXPORTING tstmp_src = ts_packlong 
                                 IMPORTING tstmp_tgt = moved_trunc ). 
 
      DATA ts_pack_round_half_up TYPE timestamp. 
      ts_pack_round_half_up = round( val = ts_packlong dec = 0 ). 
 
      DATA ts_pack_round_down TYPE timestamp. 
      ts_pack_round_down = round( val = ts_packlong dec = 0 
                                  mode =  cl_abap_math=>round_down ). 
 
      DATA ts_pack_trunc TYPE timestamp. 
      ts_pack_trunc = trunc( ts_packlong ). 
 
      frac = frac( ts_packlong ). 
    ENDWHILE. 
 
    out->write( |Short packed time stamp:            { 
         ts_pack TIMESTAMP = ISO }| 
     )->write( |Long packed time stamp:             { 
         ts_packlong TIMESTAMP = ISO }| 
     )->write( |UTCLONG time stamp:                 { 
         ts_utclong TIMESTAMP = ISO }| 
     )->line( 
     )->write( |CL_ABAP_TSTMP=>UTCLONG2TSTMP_SHORT: { 
         utclong_2_short TIMESTAMP = ISO }| 
     )->write( |Assignment with conversion:         { 
         assigned_to_short TIMESTAMP = ISO }| 
     )->write( |CL_ABAP_TSTMP=>MOVE_TO_SHORT:       { 
         moved_to_short TIMESTAMP = ISO }| 
     )->write( |CL_ABAP_TSTMP=>MOVE_TO_SHORT_TRUNC: { 
         moved_to_short_trunc TIMESTAMP = ISO }| 
     )->write( |CL_ABAP_TSTMP=>MOVE:                { 
         moved TIMESTAMP = ISO }| 
     )->write( |CL_ABAP_TSTMP=>MOVE_TRUNC:          { 
         moved_trunc TIMESTAMP = ISO }| 
     )->write( |ROUND half up:                      { 
         ts_pack_round_half_up TIMESTAMP = ISO }| 
     )->write( |ROUND down:                         { 
         ts_pack_round_down TIMESTAMP = ISO }| 
     )->write( |TRUNC:                              { 
         ts_pack_trunc TIMESTAMP = ISO }| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A short packed number UTC time stamp of type `TIMESTAMP`, a long packed number UTC time stamp of type `TIMESTAMPL` and an UTC time stamp in a time stamp field of type `utclong` are created at almost the same point in time.

The example shows the different rounding behaviors when time stamps with fractional seconds are converted to time stamps of type `TIMESTAMP` without fractional seconds:

- Using method `UTCLONG2TSTMP_SHORT` of class `CL_ABAP_TSTMP` to convert a time stamp field rounds down.

- Using a simple assignment involving the conversion rule [from `p` to `p`](abenconversion_type_p.md) rounds half up (commercial rounding).

- Using method `MOVE_TO_SHORT` of class `CL_ABAP_TSTMP` to convert a long time stamp stored as a packed number field rounds half up (commercial rounding).

- Using method `MOVE_TO_SHORT_TRUNC` of class `CL_ABAP_TSTMP` to convert a long time stamp stored as a packed number field rounds down.

- Using method `MOVE` of class `CL_ABAP_TSTMP` to convert a long time stamp stored as a packed number field rounds half up (commercial rounding).

- Using method `MOVE_TRUNC` of class `CL_ABAP_TSTMP` to convert a long time stamp stored as a packed number field rounds down.

- Using built-in function [`round`](abendec_floating_point_functions.md) without specifying `mode` for a long time stamp stored as a packed number field rounds half up (commercial rounding).

- Using built-in function [`round`](abendec_floating_point_functions.md) and specifying the appropriate mode `mode` for a long time stamp stored as a packed number field rounds down.

- Using built-in function [`trunc`](abennumerical_functions.md) for a long time stamp stored as a packed number field rounds down.

Since only rounding down a long time stamp stored as a packed number gives the same result as the statement [`GET TIME STAMP`](abapget_time-stamp.md) and if that is the expected behavior, the methods with suffix `_TRUNC` from `CL_ABAP_TSTMP` or the built-in function [`round`](abendec_floating_point_functions.md) with an appropriate mode or [`trunc`](abennumerical_functions.md) should be used instead of the other methods.
