---
title: "Conversion of Integer Numbers to Bytes"
source_file: abenconversion_int_to_hex_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Elementary Data Objects > Numeric Source Fields > Source Field Type i, int8, (b, s)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion of Integer Numbers to Bytes

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the conversion of integers into byte fields and byte strings.

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
CLASS cl_demo_int_to_hex DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF line, 
        int1 TYPE c LENGTH 60, 
        int2 TYPE c LENGTH 60, 
        int4 TYPE c LENGTH 60, 
        int8 TYPE c LENGTH 60, 
      END OF line. 
    DATA output TYPE TABLE OF line. 
    METHODS write_output IMPORTING VALUE(idx) TYPE i 
                                   VALUE(col) TYPE i 
                                   text       TYPE clike. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_to_hex IMPLEMENTATION. 
  METHOD main. 
    DATA: int1 TYPE int1, 
          int2 TYPE int2, 
          int4 TYPE int4, 
          int8 TYPE int8, 
          xstr TYPE xstring, 
          xfld TYPE x LENGTH 8. 
    out->begin_section( 
      `Conversion of Integers to Byte Fields and Byte Strings` ). 
    DO 9 TIMES. 
      int1 = ipow( base = 2 exp = sy-index - 1 ) - 1 . 
      xstr = int1. 
      xfld = int1. 
      write_output( 
        idx = sy-index 
        col = 1 
        text = |{ int1 WIDTH = 4 ALIGN = RIGHT } { 
                  xfld ALIGN = LEFT } { xstr ALIGN = LEFT }| ). 
    ENDDO. 
    DO 15 TIMES. 
      int2 = - ipow( base = 2 exp = 16 - sy-index ) + 1 . 
      xstr = int2. 
      xfld = int2. 
      write_output( 
        idx = sy-index 
        col = 2 
        text = |{ int2 WIDTH = 7 ALIGN = RIGHT } { 
                  xfld ALIGN = LEFT } { xstr ALIGN = LEFT }| ). 
    ENDDO. 
    DO 16 TIMES. 
      int2 = ipow( base = 2 exp = sy-index - 1 ) - 1 . 
      xstr = int2. 
      xfld = int2. 
      write_output( 
        idx = sy-index + 15 
        col = 2 
        text = |{ int2 WIDTH = 7 ALIGN = RIGHT } { 
                  xfld ALIGN = LEFT } { xstr ALIGN = LEFT }| ). 
    ENDDO. 
    DO 31 TIMES. 
      int4 = - CONV decfloat34( 
                 ipow( base = 2 exp = 32 - sy-index ) ) + 1 . 
      xstr = int4. 
      xfld = int4. 
      write_output( 
        idx = sy-index 
        col = 3 
        text = |{ int4 WIDTH = 12 ALIGN = RIGHT } { 
                  xfld ALIGN = LEFT } { xstr ALIGN = LEFT }| ). 
    ENDDO. 
    DO 32 TIMES. 
      int4 = CONV decfloat34( 
               ipow( base = 2 exp = sy-index - 1 )  ) - 1 . 
      xstr = int4. 
      xfld = int4. 
      write_output( 
        idx = sy-index + 31 
        col = 3 
        text = |{ int4 WIDTH = 12 ALIGN = RIGHT } { 
                  xfld ALIGN = LEFT } { xstr ALIGN = LEFT }| ). 
    ENDDO. 
    DO 63 TIMES. 
      int8 = - CONV decfloat34( 
                 ipow( base = 2 exp = 64 - sy-index ) ) + 1 . 
      xstr = int8. 
      xfld = int8. 
      write_output( 
        idx = sy-index 
        col = 4 
        text = |{ int8 WIDTH = 21 ALIGN = RIGHT } { 
                  xfld ALIGN = LEFT } { xstr ALIGN = LEFT }| ). 
    ENDDO. 
    DO 64 TIMES. 
      int8 = CONV decfloat34( 
                ipow( base = 2 exp = sy-index - 1 ) ) - 1 . 
      xstr = int8. 
      xfld = int8. 
      write_output( 
        idx = sy-index + 63 
        col = 4 
        text = |{ int8 WIDTH = 21 ALIGN = RIGHT } { 
                  xfld ALIGN = LEFT } { xstr ALIGN = LEFT }| ). 
    ENDDO. 
    out->write( output ). 
  ENDMETHOD. 
  METHOD write_output. 
    ASSIGN output[ idx ] TO FIELD-SYMBOL(<line>). 
    IF sy-subrc <> 0. 
      DO. 
        APPEND INITIAL LINE TO output ASSIGNING <line>. 
        IF sy-tabix = idx. 
          EXIT. 
        ENDIF. 
      ENDDO. 
    ENDIF. 
    ASSIGN <line>-(col) TO FIELD-SYMBOL(<col>). 
    <col> = text. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class assigns numbers of the data types `b`, `s`, and `i` and `int8`, which cover the entire value range, to byte fields with the lengths 1, 2, 4, and 8 as well as to a byte string and displays them.

To calculate the numbers with powers of two, the use of the [calculation type](abenarith_type.md) `decfloat34` is forced in some cases to avoid overflows when assigning the results of the function [`ipow`](abenipow_function_abexa.md) to interim results of the calculation type `i` or `int8`.

This example highlights the different lengths that can result from these assignments to byte strings. It also shows that, in the case of assignments of the type `s` to `x`, a field length of 4 bytes instead of only 2 bytes is required for negative numbers.
