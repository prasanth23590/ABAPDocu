---
title: "num_func - Rounding Function round"
source_file: abenround_function_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - Rounding Function round

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the rounding function [`round`](abendec_floating_point_functions.md).

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
CLASS cl_demo_round DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: BEGIN OF mode, 
            value LIKE cl_abap_math=>round_half_up, 
            name  TYPE abap_attrdescr-name, 
          END OF mode, 
          modes LIKE SORTED TABLE OF mode 
            WITH UNIQUE KEY name. 
    METHODS get_modes. 
    TYPES: 
      BEGIN OF line, 
        number    TYPE decfloat34, 
        ceiling   TYPE decfloat34, 
        down      TYPE decfloat34, 
        floor     TYPE decfloat34, 
        half_down TYPE decfloat34, 
        half_even TYPE decfloat34, 
        half_up   TYPE decfloat34, 
        up        TYPE decfloat34, 
      END OF line. 
    DATA output TYPE TABLE OF line. 
    METHODS write_output IMPORTING VALUE(idx) TYPE i 
                                   VALUE(col) TYPE i 
                                   text       TYPE clike. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_round IMPLEMENTATION. 
  METHOD main. 
    DATA number TYPE decfloat34. 
    out->begin_section( `Rounding Function` ). 
    get_modes( ). 
    DO 21 TIMES. 
      number = - ( sy-index - 11 ) / 10. 
      write_output( 
        idx = sy-index 
        col = '1' 
        text = |{ number }| ). 
      LOOP AT modes INTO mode. 
        write_output( 
          idx = sy-index 
          col = sy-tabix + 1 
          text = |{ round( val  = number 
                           dec  = 0 
                           mode = mode-value ) }| ). 
      ENDLOOP. 
    ENDDO. 
    out->write( output ). 
  ENDMETHOD. 
  METHOD get_modes. 
    DATA: modes TYPE abap_attrdescr_tab, 
          mode  LIKE LINE OF modes. 
    FIELD-SYMBOLS <mode> LIKE cl_abap_math=>round_half_up. 
    modes = 
      CAST cl_abap_classdescr( 
             cl_abap_classdescr=>describe_by_name( 'CL_ABAP_MATH' ) 
             )->attributes. 
    DELETE modes WHERE name NP 'ROUND_*' OR is_constant <> 'X'. 
    LOOP AT modes INTO mode. 
      ASSIGN cl_abap_math=>(mode-name) TO <mode>. 
      me->mode-value = <mode>. 
      me->mode-name = mode-name. 
      INSERT me->mode INTO TABLE me->modes. 
    ENDLOOP. 
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

For fraction numbers between 1 and -1, the class depicts the effect of all rounding types from the class `CL_ABAP_MATH` in the rounding function [`round`](abendec_floating_point_functions.md). The class reads the possible rounding methods using RTTI and sorts them by name.
