---
title: "Determining Object Types"
source_file: abenrtti_object_type_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Properties of Data Objects > Runtime Type Services (RTTS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Determining Object Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the dynamic types of objects can be determined at runtime.

## Source Code

``` abap
* CCDEF 
CLASS conv_exc DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS c1 DEFINITION. 
ENDCLASS. 
 
CLASS c2 DEFINITION. 
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
CLASS cl_demo_rtti_object_types DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rtti_object_types IMPLEMENTATION. 
  METHOD main. 
 
    DATA: otype1 TYPE c LENGTH 30 VALUE 'C1', 
          otype2 TYPE c LENGTH 30 VALUE 'C2'. 
 
    DATA: oref1 TYPE REF TO object, 
          oref2 TYPE REF TO object. 
 
    DATA: descr_ref1 TYPE REF TO cl_abap_typedescr, 
          descr_ref2 TYPE REF TO cl_abap_typedescr. 
 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = otype1 
     )->request(   CHANGING field = otype2 ). 
 
    TRY. 
        otype1 = cl_abap_dyn_prg=>check_whitelist_str( 
          EXPORTING 
            val                      = otype1 
            whitelist                =  `C1,C2` ). 
        otype2 = cl_abap_dyn_prg=>check_whitelist_str( 
          EXPORTING 
            val                      = otype2 
            whitelist                =  `C1,C2` ). 
      CATCH cx_abap_not_in_whitelist. 
        out->write( 'Input not allowed' ). 
        RETURN. 
    ENDTRY. 
 
    TRY. 
        CREATE OBJECT: oref1 TYPE (otype1), 
                       oref2 TYPE (otype2). 
 
      CATCH cx_sy_create_object_error. 
        out->write( 'Create object error!' ). 
        RETURN. 
 
      CATCH cx_root. 
        out->write( 'Other error!' ). 
        RETURN. 
    ENDTRY. 
 
    descr_ref1 = cl_abap_typedescr=>describe_by_object_ref( oref1 ). 
    descr_ref2 = cl_abap_typedescr=>describe_by_object_ref( oref2 ). 
 
    TRY. 
        IF descr_ref1 <> descr_ref2. 
          RAISE EXCEPTION TYPE conv_exc. 
        ELSE. 
          oref1 = oref2. 
        ENDIF. 
 
      CATCH conv_exc. 
        out->write( 
          `Assignment from type `   && |\n| && 
          descr_ref2->absolute_name && |\n| && 
          `to `                     && |\n| && 
          descr_ref1->absolute_name && |\n| && 
          `not allowed!` ). 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example is the equivalent of the [executable example](abenrtti_data_type_abexa.md) for data types for object types. Here, the dynamic type of reference variables is determined, namely the [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md) of the class of the referenced object.
