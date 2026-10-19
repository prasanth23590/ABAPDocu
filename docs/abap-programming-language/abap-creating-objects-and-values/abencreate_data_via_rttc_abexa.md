---
title: "Creating a Structure Using RTTC"
source_file: abencreate_data_via_rttc_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA > CREATE DATA, HANDLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating a Structure Using RTTC

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a structure is created using [RTTC](../../abap-glossary/abenrun_time_type_creation_glosry.md).

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
CLASS cl_demo_create_data_via_handle DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_create_data_via_handle IMPLEMENTATION. 
  METHOD main. 
 
    DATA: struct_type TYPE REF TO cl_abap_structdescr, 
          dref        TYPE REF TO data, 
          oref        TYPE REF TO cx_sy_struct_creation. 
 
    DATA column1 TYPE c LENGTH 30. 
    DATA column2 TYPE c LENGTH 30. 
 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = column1 
     )->add_field( CHANGING field = column2 
     )->request( ). 
 
    column1 = to_upper( column1 ). 
    column2 = to_upper( column2 ). 
 
    TRY. 
        struct_type = cl_abap_structdescr=>get( 
          VALUE #( 
            ( name = column1 type = cl_abap_elemdescr=>get_c( 40 ) ) 
            ( name = column2 type = cl_abap_elemdescr=>get_i( )    ) 
                 ) 
                                               ). 
        CREATE DATA dref TYPE HANDLE struct_type. 
      CATCH cx_sy_struct_creation INTO oref. 
        out->write( oref->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    dref->(column1) = 'Amount'. 
    dref->(column2) = 11. 
 
    out->write( dref->* ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Dynamic definition of a structure with two components using the `GET` method of the `CL_ABAP_STRUCTDESCR` class. The description of the components of the structure is provided in the internal table `comp_tab`. If no type description object exists for this structure yet, it is created by the `GET` method.

The method `CHECK_TABLE_NAME_STR` of the class `CL_ABAP_DYN_PRG` checks whether the database table specified exists and can be used.
