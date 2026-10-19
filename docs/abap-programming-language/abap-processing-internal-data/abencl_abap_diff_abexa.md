---
title: "itab - Using CL_ABAP_DIFF"
source_file: abencl_abap_diff_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - System Classes > itab - System Class CL_ABAP_DIFF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Using CL_ABAP_DIFF

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates class `CL_ABAP_DIFF`.

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
CLASS cl_demo_itab_diff DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
 
  PRIVATE SECTION. 
    METHODS diff 
      IMPORTING 
        !itab1 TYPE INDEX TABLE 
        !itab2 TYPE INDEX TABLE 
        update TYPE abap_bool OPTIONAL. 
    METHODS diff_with_line_ref 
      IMPORTING 
        !itab1 TYPE INDEX TABLE 
        !itab2 TYPE INDEX TABLE 
        update TYPE abap_bool OPTIONAL. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_itab_diff IMPLEMENTATION. 
  METHOD main. 
 
    DATA: 
      itab1 TYPE TABLE OF i, 
      itab2 TYPE TABLE OF string, 
      itab3 TYPE TABLE OF i, 
      BEGIN OF line, 
        col1 TYPE i, 
        col2 LIKE itab1, 
      END OF line, 
      itab4 LIKE TABLE OF line, 
      itab5 LIKE TABLE OF line. 
 
    out->next_section( `Incompatible Type, Same Values` ). 
    itab1 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
    itab2 = VALUE #( ( `1` ) ( `2` ) ( `3` ) ). 
    diff( itab1 = itab1 
          itab2 = itab2 ). 
 
    out->next_section( `Compatible Type, Same Values` ). 
    itab1 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
    itab3 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
    diff( itab1 = itab1 
          itab2 = itab3 ). 
 
    out->next_section( `Compatible Type, Different Values` ). 
    itab1 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
    itab3 = VALUE #( ( 1 ) ( 4 ) ( 3 ) ). 
    diff( itab1 = itab1 
          itab2 = itab3 ). 
    diff( itab1 = itab1 
          itab2 = itab3 update = 'X' ). 
    diff_with_line_ref( itab1 = itab1 
                        itab2 = itab3 ). 
    diff_with_line_ref( itab1 = itab1 
                        itab2 = itab3 update = 'X' ). 
 
    out->next_section( `Nested Type, Same Values` ). 
    itab4 = VALUE #( 
      ( col1 = 1 col2 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ) ) 
      ( col1 = 2 col2 = VALUE #( ( 4 ) ( 5 ) ( 6 ) ) ) ). 
    itab5 = itab4. 
    diff( itab1 = itab4 
          itab2 = itab5 ). 
    out->next_section( `Nested Type, Different Values` ). 
    itab4 = VALUE #( 
      ( col1 = 1 col2 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ) ) 
      ( col1 = 2 col2 = VALUE #( ( 4 ) ( 5 ) ( 6 ) ) ) ). 
    itab5[ 1 ]-col2[ 3 ] = 10. 
    diff( itab1 = itab4 
          itab2 = itab5 ). 
    diff( itab1 = itab4 
          itab2 = itab5 update = 'X' ). 
    diff_with_line_ref( itab1 = itab4 
                        itab2 = itab5 ). 
    diff_with_line_ref( itab1 = itab4 
                        itab2 = itab5 update = 'X' ). 
 
  ENDMETHOD. 
  METHOD diff. 
    DATA flag_identical TYPE abap_boolean. 
    FINAL(diff) = cl_abap_diff=>create( 
      output_mode = COND #( 
        WHEN update IS NOT INITIAL 
             THEN cl_abap_diff=>s_output-generate_update ) ). 
    TRY. 
        DATA(diff_result) =  diff->diff( 
           EXPORTING 
             target         = itab1 
             source         = itab2 
        IMPORTING 
          flag_identical = flag_identical ). 
        IF flag_identical IS NOT INITIAL. 
          out->write_data( flag_identical ). 
        ELSE. 
          out->write( diff_result ). 
        ENDIF. 
      CATCH cx_abap_diff INTO DATA(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD diff_with_line_ref. 
    DATA flag_identical TYPE abap_boolean. 
    FINAL(diff) = cl_abap_diff=>create( 
      output_mode = COND #( 
        WHEN update IS NOT INITIAL 
             THEN cl_abap_diff=>s_output-generate_update ) ). 
    TRY. 
        DATA(diff_with_line_ref_result) =  diff->diff_with_line_ref( 
           EXPORTING 
             target         = itab1 
             source         = itab2 
        IMPORTING 
          flag_identical = flag_identical ). 
        IF flag_identical IS NOT INITIAL. 
          out->write_data( flag_identical ). 
        ELSE. 
          out->write( diff_with_line_ref_result ). 
        ENDIF. 
      CATCH cx_abap_diff INTO DATA(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Some internal tables are filled with values and compared with methods `DIFF` and `DIFF_WITH_LINE_REF` of class `CL_ABAP_DIFF`. The results are shown for insert/delete as well as for insert/delete/update modes.
