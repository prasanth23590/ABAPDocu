---
title: "string_tmpl - Alignments and Padding"
source_file: abenstring_template_align_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl) > string_tmpl - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - Alignments and Padding

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how to specify an alignment and how to pad embedded expressions.

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
CLASS cl_demo_str_template_align_pad DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_template_align_pad IMPLEMENTATION. 
  METHOD main. 
 
    DATA pad TYPE c LENGTH 1. 
    cl_demo_input=>new( )->request( CHANGING field = pad ). 
 
    out->write( 
          |{ 'Left'   WIDTH = 20 ALIGN = LEFT   PAD = pad }<---| 
      )->write( 
         |{ 'Center' WIDTH = 20 ALIGN = CENTER PAD = pad }<---| 
      )->write( 
         |{ 'Right'  WIDTH = 20 ALIGN = RIGHT  PAD = pad }<---| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The alignment of three string templates is declared statically. The character used to pad the superfluous places can be entered using an input field.
