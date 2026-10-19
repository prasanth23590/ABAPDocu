---
title: "SELECT, Dynamic ORDER BY Clause"
source_file: abendynamic_order_by_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, ORDER BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Dynamic ORDER BY Clause

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how sorting is specified dynamically for `SELECT`.

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
CLASS cl_demo_select_dynamic_ordr_by DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_dynamic_ordr_by IMPLEMENTATION. 
  METHOD main. 
    TYPES flag TYPE c LENGTH 1. 
    DATA: flag_tab  TYPE TABLE OF flag WITH EMPTY KEY, 
          order_by  TYPE string, 
          spfli_tab TYPE TABLE OF spfli WITH EMPTY KEY. 
 
    "Input screen for columns 
    FINAL(components) = CAST cl_abap_structdescr( 
      cl_abap_typedescr=>describe_by_name( 'SPFLI' ) )->components. 
    FINAL(in) = cl_demo_input=>new( ). 
    LOOP AT components FROM 2 ASSIGNING FIELD-SYMBOL(<component>). 
      APPEND INITIAL LINE TO flag_tab ASSIGNING FIELD-SYMBOL(<flag>). 
      in->add_field( 
        EXPORTING text = CONV string( <component>-name ) 
        CHANGING  field =  <flag> ). 
    ENDLOOP. 
    in->request( ). 
 
    "Create ORDER BY clause 
    LOOP AT components FROM 2 ASSIGNING <component>. 
      FINAL(idx) = sy-tabix. 
      FINAL(flag) = flag_tab[ idx - 1 ]. 
      order_by &&= 
        COND string( WHEN to_upper( flag ) = `X` OR 
                          to_upper( flag ) = `A` 
                            THEN |, { <component>-name } ASCENDING| 
                     WHEN to_upper( flag ) = `D` 
                            THEN |, { <component>-name } DESCENDING| 
                     ELSE `` ). 
    ENDLOOP. 
    SHIFT order_by BY 2 PLACES LEFT. 
 
    "Database access 
    TRY. 
        SELECT * 
               FROM spfli 
               ORDER BY (order_by) 
               INTO TABLE @spfli_tab. 
      CATCH cx_sy_dynamic_osql_error INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
        RETURN. 
    ENDTRY. 
    out->write( spfli_tab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) is used to create input fields for all columns of the table `SPFLI` except for the client column. The values *X* or *A* for ascending sorts and `D` for descending sorts can be entered in these columns. A dynamic `ORDER BY` clause is generated from the input as a character string and used in a `SELECT` statement.
