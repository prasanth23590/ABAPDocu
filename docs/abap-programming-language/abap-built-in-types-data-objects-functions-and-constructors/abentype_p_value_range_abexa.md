---
title: "Value Ranges of Packed Numbers"
source_file: abentype_p_value_range_abexa.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Types > Built-In ABAP Types > Built-In Numeric Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Value Ranges of Packed Numbers

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the value ranges of packed numbers with different lengths and decimal places.

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
CLASS cl_demo_type_p_value_range DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_type_p_value_range IMPLEMENTATION. 
  METHOD main. 
    DATA:length   TYPE i VALUE 2, 
         decimals TYPE i VALUE 2. 
    cl_demo_input=>new( 
     )->add_field( EXPORTING text  = `Length` 
                   CHANGING  field = length 
     )->request(   EXPORTING text  = `Decimals` 
                   CHANGING  field = decimals ). 
 
    DATA dref TYPE REF TO data. 
    TRY. 
        IF decimals > 2 * length - 1. 
          RAISE EXCEPTION TYPE cx_sy_create_data_error. 
        ENDIF. 
        CREATE DATA dref TYPE p LENGTH length DECIMALS decimals. 
      CATCH cx_sy_create_data_error. 
        out->write( 'Wrong input values ...' ). 
        RETURN. 
    ENDTRY. 
 
    FINAL(lower) 
      = cl_abap_exceptional_values=>get_min_value( dref->* ). 
    IF lower IS NOT INITIAL. 
      ASSIGN lower->* TO FIELD-SYMBOL(<lower>). 
      out->write_data( <lower> ). 
    ENDIF. 
 
    ASSERT <lower> =  CONV decfloat34( 
     ( ipow( base = -10 exp = 2 * length - 1 ) + 1 ) / 
       ipow( base  = 10 exp = decimals ) ). 
 
    FINAL(upper) 
       = cl_abap_exceptional_values=>get_max_value( dref->* ). 
    IF upper IS NOT INITIAL. 
      ASSIGN upper->* TO FIELD-SYMBOL(<upper>). 
      out->write_data( <upper> ). 
    ENDIF. 
 
    ASSERT <upper> = CONV decfloat34( 
     ( ipow( base = +10 exp = 2 * length - 1 ) - 1 ) / 
       ipow( base  = 10 exp = decimals ) ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The value range of a packed number with the length `length` and `decimals` decimal places is one of the following according to the formula in this [table](abenbuiltin_types_numeric.md)):

`( -10^(2xlength-1) +1 ) / ( 10^decimals )`

to

`( +10^(2xlength-1) -1 ) / ( 10^decimals )`

The method creates a packed number with a length and decimal places that can be entered from outside. The minimum and maximum values of the number are determined using methods of the system class `CL_ABAP_EXCEPTIONAL_VALUES` and compared with self-calculated values.
