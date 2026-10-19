---
title: "Creating Structured Data Objects"
source_file: abencreate_structured_data_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA > CREATE DATA, TYPE, LIKE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating Structured Data Objects

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how structured data objects are created.

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
CLASS cl_demo_create_structured_data DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_create_structured_data IMPLEMENTATION. 
  METHOD main. 
    DATA dref TYPE REF TO data. 
 
    DATA: dbtab TYPE tabname VALUE 'SPFLI', 
          rows  TYPE i VALUE 100. 
 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = dbtab 
      )->add_field( CHANGING field = rows )->request( ). 
 
    dbtab = to_upper( dbtab ). 
    TRY. 
        dbtab = cl_abap_dyn_prg=>check_table_name_str( 
                  val = dbtab 
                  packages = 'SAPBC_DATAMODEL' ). 
      CATCH cx_abap_not_a_table. 
        out->write( 'Database table not found' ). 
        RETURN. 
      CATCH cx_abap_not_in_package. 
        out->write( 
          'Only tables from the flight data model are allowed' ). 
        RETURN. 
    ENDTRY. 
 
    TRY. 
        CREATE DATA dref TYPE (dbtab). 
        SELECT * 
               FROM (dbtab) 
               INTO @dref->* 
               UP TO @rows ROWS. 
          out->write( dref->* ). 
        ENDSELECT. 
      CATCH cx_sy_create_data_error. 
        out->write( 'Error in data creation' ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Creation of a work area that matches any database table and reads the first few rows (`rows`) of the database table into this work area using a [`SELECT`](../abap-database-access/abapselect.md) loop.

The method `CHECK_TABLE_NAME_STR` of the class `CL_ABAP_DYN_PRG` checks whether the entered database table exists and can be used.

See also the [executable example](../abap-database-access/abenselect_into_new_wa_abexa.md) for `SELECT INTO NEW`, where the structure is created implicitly in the `INTO` clause.
