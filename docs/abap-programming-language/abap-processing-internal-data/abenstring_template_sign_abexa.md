---
title: "string_tmpl - Sign"
source_file: abenstring_template_sign_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl) > string_tmpl - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - Sign

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how the plus/minus sign format is specified for embedded expressions.

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
CLASS cl_demo_str_template_sign DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_template_sign IMPLEMENTATION. 
  METHOD main. 
    DATA: num1    TYPE i VALUE -10, 
          num2    TYPE i VALUE +10, 
          results TYPE TABLE OF string, 
          formats TYPE abap_attrdescr_tab, 
          format  LIKE LINE OF formats. 
 
    FIELD-SYMBOLS <sign> LIKE cl_abap_format=>s_left. 
 
    formats = 
      CAST cl_abap_classdescr( 
             cl_abap_classdescr=>describe_by_name( 'CL_ABAP_FORMAT' ) 
             )->attributes. 
    DELETE formats WHERE name NP 'S_*' OR is_constant <> 'X'. 
 
    LOOP AT formats INTO format. 
      ASSIGN cl_abap_format=>(format-name) TO <sign>. 
      APPEND |{ format-name WIDTH = 16 }  | & 
             |"{ num1 SIGN = (<sign>) }"  | & 
             |"{ num2 SIGN = (<sign>) }"  | TO results. 
    ENDLOOP. 
    out->write( results ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The six possible settings for the case of a string template are specified dynamically.
