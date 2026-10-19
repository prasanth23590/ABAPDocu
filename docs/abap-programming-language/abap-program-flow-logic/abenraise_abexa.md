---
title: "Exceptions, RAISE"
source_file: abenraise_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Examples of Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exceptions, RAISE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the statement `RAISE EXCEPTION`.

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
CLASS cl_demo_raise_exception DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_raise_exception IMPLEMENTATION. 
  METHOD main. 
    DATA: oref     TYPE REF TO cx_demo_constructor, 
          text     TYPE string, 
          position TYPE i. 
    TRY. 
        TRY. 
            RAISE EXCEPTION TYPE cx_demo_constructor 
              EXPORTING 
                my_text = sy-repid. 
          CATCH cx_demo_constructor INTO oref. 
            text = oref->get_text( ). 
            oref->get_source_position( 
              IMPORTING  source_line  = position ). 
            out->write_text( |{ position } { text }| ). 
            RAISE EXCEPTION oref. 
        ENDTRY. 
      CATCH cx_demo_constructor INTO oref. 
        text = oref->get_text( ). 
        oref->get_source_position( 
          IMPORTING source_line  = position ). 
        out->write_text( |{ position } { text }| ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example shows the two variants of the statement `RAISE EXCEPTION`. The first statement raises an exception of the class `CX_DEMO_CONSTRUCTOR` in the inner `TRY` block, creates the relevant object, and passes the current program name to the instance constructor. The inner `CATCH` block handles the exception, produces the exception text as output and raises the exception again without creating a new object. The outer `CATCH` block handles the exception again. The class `CX_DEMO_CONSTRUCTOR` is defined in such a way that the passed program name appears in the exception text. The generated instance constructor ensures this.

The output of the line number in which the exception was raised indicates that, when the existing exception object was reused, its information was changed.
