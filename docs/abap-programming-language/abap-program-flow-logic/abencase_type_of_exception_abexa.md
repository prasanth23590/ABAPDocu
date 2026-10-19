---
title: "Case Distinction CASE TYPE OF for Exceptions"
source_file: abencase_type_of_exception_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Control Structures > Branches > CASE TYPE OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Case Distinction CASE TYPE OF for Exceptions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the case distinction [`CASE TYPE OF`](abapcase_type.md) for exception classes.

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
CLASS cl_demo_case_type_of_exception DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS my_sqrt IMPORTING num TYPE any 
                    RAISING   cx_dynamic_check. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_case_type_of_exception IMPLEMENTATION. 
  METHOD main. 
    DATA number TYPE string VALUE -1. 
    cl_demo_input=>new( )->request( CHANGING field = number ). 
    TRY. 
        my_sqrt( number ). 
      CATCH cx_root INTO FINAL(exc). 
        CASE TYPE OF exc. 
          WHEN TYPE cx_sy_arithmetic_error. 
            out->write( 'Arithmetic error' ). 
          WHEN TYPE cx_sy_conversion_error. 
            out->write( 'Conversion error' ). 
          WHEN OTHERS. 
            out->write( 'Other error' ). 
        ENDCASE. 
    ENDTRY. 
  ENDMETHOD. 
  METHOD my_sqrt. 
    FINAL(sqrt) = sqrt( CONV decfloat34( num ) ). 
    out->write( sqrt ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Non-specific exceptions of the superclass `CX_DYNAMIC_CHECK` can be propagated from a method `my_sqrt`. The actual exception class is determined in the calling method using the case distinction [`CASE TYPE OF`](abapcase_type.md).
