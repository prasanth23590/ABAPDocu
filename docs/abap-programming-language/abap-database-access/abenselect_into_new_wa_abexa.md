---
title: "SELECT, Create Structure as Target Area"
source_file: abenselect_into_new_wa_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, INTO, APPENDING > SELECT, INTO target"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Create Structure as Target Area

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the creation of an structure as a target area of the statement `SELECT`.

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
CLASS cl_demo_select_into_new_wa DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_into_new_wa IMPLEMENTATION. 
  METHOD main. 
    DATA: dbtab TYPE tabname VALUE 'SPFLI', 
          rows  TYPE i VALUE 100. 
 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = dbtab 
      )->add_field( CHANGING field = rows )->request( ). 
    IF rows < 1 OR rows > 1000. 
      out->write( 'Enter rows between 1 and 1000' ). 
      RETURN. 
    ENDIF. 
 
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
        SELECT * 
               FROM (dbtab) 
               INTO NEW @FINAL(row) 
               UP TO @rows ROWS. 
          out->write( row->* ). 
        ENDSELECT. 
      CATCH cx_sy_open_sql_db. 
        out->write( 'Error in ABAP SQL' ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Creates a work area that matches any DDIC database table in the `INTO` clause and reads the first rows `rows` of the DDIC database table into this work area using a [`SELECT`](abapselect.md) loop.

The method `CHECK_TABLE_NAME_STR` of the class `CL_ABAP_DYN_PRG` checks whether the DDIC database table specified exists and can be used.

See also the [executable example](../abap-creating-objects-and-values/abencreate_structured_data_abexa.md) for `CREATE DATA` with explicit creation of the structure.
