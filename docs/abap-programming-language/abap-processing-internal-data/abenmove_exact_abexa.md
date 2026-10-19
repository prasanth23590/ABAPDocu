---
title: "Lossless Assignment"
source_file: abenmove_exact_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments > Lossless Assignments, Rules > Checking Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Lossless Assignment

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the operator [`EXACT`](abenconstructor_expression_exact.md) is used to make lossless assignments.

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
CLASS cl_demo_move_exact DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_move_exact IMPLEMENTATION. 
  METHOD main. 
    DATA: text     TYPE string VALUE `4 Apples + 2 Oranges`, 
          num_text TYPE n LENGTH 8. 
    out->begin_section( text 
      )->begin_section( `Not really exact:` ). 
    num_text = text. 
    out->write_data( num_text 
      )->next_section( `Try to be exact:` ). 
    TRY. 
        num_text = EXACT #( text ). 
        out->write_data( num_text ). 
      CATCH cx_sy_conversion_error INTO FINAL(exc). 
        out->write_text( exc->get_text( ) ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Without the operator `EXACT`, `text` is assigned to `num_text` without the check for validity of the assigned value against the associated [conversion rules](abenconversion_type_string.md), which produces a value that is not very intuitive, *00000042*.

Using the operator `EXACT`, the value that is passed is checked and an exception is raised in the case in question.
