---
title: "Determining Data Types"
source_file: abenrtti_data_type_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Properties of Data Objects > Runtime Type Services (RTTS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Determining Data Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the properties of data types can be determined at runtime.

## Source Code

``` abap
* CCDEF 
CLASS conv_exc DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_rtti_data_types DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rtti_data_types IMPLEMENTATION. 
  METHOD main. 
 
    DATA: type1 TYPE c LENGTH 30 VALUE 'SCARR', 
          type2 TYPE c LENGTH 30 VALUE 'SPFLI'. 
 
    DATA: dref1 TYPE REF TO data, 
          dref2 TYPE REF TO data. 
 
    DATA: descr_ref1 TYPE REF TO cl_abap_typedescr, 
          descr_ref2 TYPE REF TO cl_abap_typedescr. 
 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = type1 
     )->request(   CHANGING field = type2 ). 
 
    TRY. 
        CREATE DATA: dref1 TYPE (type1), 
                     dref2 TYPE (type2). 
 
      CATCH cx_sy_create_data_error. 
        out->write( 'Create data error!' ). 
        RETURN. 
    ENDTRY. 
 
    descr_ref1 = cl_abap_typedescr=>describe_by_data( dref1->* ). 
    descr_ref2 = cl_abap_typedescr=>describe_by_data( dref2->* ). 
 
    TRY. 
        IF descr_ref1 <> descr_ref2. 
          RAISE EXCEPTION TYPE conv_exc. 
        ELSE. 
          dref2->* = dref1->*. 
        ENDIF. 
      CATCH conv_exc. 
        out->write( 
          `Assignment from type `    && 
          descr_ref2->absolute_name  && 
          ` to `                     && 
          descr_ref1->absolute_name  && 
          ` not allowed!` ). 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example expands on the executable example for `DESCRIBE FIELD` to the correct check of any data type.

When complex types, such as `SCARR` and `SPFLI`, are entered in the input fields, the RTTI determines the full [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md).
