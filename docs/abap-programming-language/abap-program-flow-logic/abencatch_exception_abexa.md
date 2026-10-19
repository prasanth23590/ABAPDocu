---
title: "Exceptions, CATCH"
source_file: abencatch_exception_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Examples of Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exceptions, CATCH

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how class-based exceptions are caught.

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
CLASS cl_demo_catch_exception DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS lcx_exception DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS exc_demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA: in TYPE REF TO if_demo_input, 
    out TYPE REF TO if_demo_output. 
    CLASS-DATA dref TYPE REF TO data. 
    CLASS-DATA: resumable TYPE abap_bool VALUE abap_false, 
    before_unwind TYPE abap_bool VALUE abap_false, 
    resume TYPE abap_bool VALUE abap_false. 
    CLASS-METHODS: main IMPORTING out TYPE REF TO if_demo_output, 
    meth1 RAISING lcx_exception, 
    meth2 RAISING RESUMABLE(lcx_exception). 
ENDCLASS. 
 
CLASS exc_demo IMPLEMENTATION. 
  METHOD main. 
    exc_demo=>out = out. 
    in = cl_demo_input=>new( ). 
    in->add_field( EXPORTING as_checkbox = 'X' 
    text = 'RAISE RESUMABLE' 
    CHANGING field = resumable 
    )->add_field( EXPORTING as_checkbox = 'X' 
    text = 'CATCH BEFORE UNWIND' 
    CHANGING field = before_unwind 
    )->add_field( EXPORTING as_checkbox = 'X' 
    text = 'RESUME' 
    CHANGING field = resume 
    )->request( ). 
    DATA exc TYPE REF TO lcx_exception. 
    IF before_unwind = abap_false. 
      TRY. 
          out->write( 'Trying method call' ). 
          IF resumable = abap_false. 
            exc_demo=>meth1( ). 
          ELSEIF resumable = abap_true. 
            exc_demo=>meth2( ). 
          ENDIF. 
        CATCH lcx_exception. 
          IF dref IS BOUND. 
            out->write( 'Context of method available' ). 
          ELSE. 
            out->write( 'Context of method not available' ). 
          ENDIF. 
      ENDTRY. 
      out->write( 'Continue after main TRY block' ). 
    ELSEIF before_unwind = abap_true. 
      TRY. 
          out->write( 'Trying method call' ). 
          IF resumable = abap_false. 
            exc_demo=>meth1( ). 
          ELSEIF resumable = abap_true. 
            exc_demo=>meth2( ). 
          ENDIF. 
        CATCH BEFORE UNWIND lcx_exception INTO exc. 
          IF dref IS BOUND. 
            out->write( 'Context of method available' ). 
          ELSE. 
            out->write( 'Context of method not available' ). 
          ENDIF. 
          IF resume = abap_true. 
            IF exc->is_resumable = abap_true. 
              RESUME. 
            ELSE. 
              out->write( 'Resumption not possible' ). 
            ENDIF. 
          ENDIF. 
      ENDTRY. 
      out->write( 'Continue after main TRY block' ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD meth1. 
    DATA loc TYPE i. 
    dref = REF #( loc ). 
    TRY. 
        out->write( 'Raising non-resumable exception' ). 
        RAISE EXCEPTION TYPE lcx_exception ##STMNT_EXIT. 
        out->write( 'Never executed' ). 
      CLEANUP. 
        out->write( 'Cleanup in method' ). 
    ENDTRY. 
    out->write( 'Continue after TRY block in method' ). 
  ENDMETHOD. 
  METHOD meth2. 
    DATA loc TYPE i. 
    dref = REF #( loc ). 
    TRY. 
        out->write( 'Raising resumable exception' ). 
        RAISE RESUMABLE EXCEPTION TYPE lcx_exception. 
        out->write( 'Resuming method' ). 
      CLEANUP. 
        out->write( 'Cleanup in method' ). 
    ENDTRY. 
    out->write( 'Continue after TRY block in method' ). 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_catch_exception IMPLEMENTATION. 
  METHOD main. 
    exc_demo=>main( out ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `meth1` raises a non-resumable exception and the method `meth2` raises a resumable exception that is handled in the `TRY` control structures of the method `main` using `CATCH`.

- If handled without `BEFORE UNWIND`, the `CLEANUP` block is executed in both cases before handling and the context of the called method does not exist during handling.

- If handled with `BEFORE UNWIND`, the context of the called method exists in both cases during handling and the `CLEANUP` block is executed after handling.

- If a resumable exception is raised, the statement `RESUME` can be executed during handling, which ensures that processing in the called method is continued without its `CLEANUP` block being executed.
