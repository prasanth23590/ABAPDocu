---
title: "Creating Elementary Data Objects"
source_file: abencreate_simple_data_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA > CREATE DATA, TYPE abap_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating Elementary Data Objects

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how elementary data objects are created.

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
CLASS cl_demo_create_simple_data DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS create_data IMPORTING 
                          VALUE(typ)  TYPE c 
                          VALUE(len)  TYPE i 
                          VALUE(dec)  TYPE i 
                        RETURNING 
                          VALUE(dref) TYPE REF TO data 
                        RAISING 
                          cx_sy_create_data_error. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_create_simple_data IMPLEMENTATION. 
  METHOD main. 
    DATA dref TYPE REF TO data. 
 
    DATA: type     LENGTH 10 TYPE c, 
          length   TYPE i, 
          decimals TYPE i. 
 
    cl_demo_input=>new( 
      )->add_field( EXPORTING text  = `Built-In ABAP Type` 
                    CHANGING  field = type 
      )->add_field( EXPORTING text  = `Length` 
                    CHANGING  field = length 
      )->request(   EXPORTING text  = `Decimals` 
                    CHANGING  field = decimals ). 
 
    TRY. 
        IF to_lower( type ) = 'p' AND decimals > 2 * length - 1. 
          "Would lead to undefined state for packed number 
          RAISE EXCEPTION TYPE cx_sy_create_data_error. 
        ENDIF. 
        dref = create_data( typ = type 
                            len = length 
                            dec = decimals ). 
 
        FINAL(descr) = CAST cl_abap_datadescr( 
          cl_abap_typedescr=>describe_by_data( dref->* ) ). 
        type = descr->type_kind. 
        length = descr->length. 
        decimals = descr->decimals. 
 
        out->write( |{ type } { length } { decimals }| ). 
      CATCH cx_sy_create_data_error. 
        out->write( |Error creating { type } { 
                                                   length } { 
                                                   decimals }| ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD create_data. 
    TRANSLATE typ TO LOWER CASE. 
    CASE typ. 
      WHEN 'd' OR 'decfloat16' OR 'decfloat34' OR 'f' OR 'i' 
               OR 'string' OR 't' OR 'xstring'. 
        CREATE DATA dref TYPE (typ). 
      WHEN 'c' OR 'n' OR 'x'. 
        CREATE DATA dref TYPE (typ) LENGTH len. 
      WHEN 'p'. 
        CREATE DATA dref TYPE p LENGTH len DECIMALS dec. 
      WHEN OTHERS. 
        RAISE EXCEPTION TYPE cx_sy_create_data_error. 
    ENDCASE. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `create_data` creates all elementary data objects that are possible with the built-in ABAP types, depending on the passed input values.
