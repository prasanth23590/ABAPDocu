---
title: "string_tmpl - Case"
source_file: abenstring_template_case_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl) > string_tmpl - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - Case

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how case is specified for embedded expressions.

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
CLASS cl_demo_str_template_case DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_template_case IMPLEMENTATION. 
  METHOD main. 
    DATA: output  TYPE TABLE OF string, 
          formats TYPE abap_attrdescr_tab, 
          format  LIKE LINE OF formats. 
 
    FIELD-SYMBOLS <case> LIKE cl_abap_format=>c_raw. 
 
    formats = 
      CAST cl_abap_classdescr( 
             cl_abap_classdescr=>describe_by_name( 'CL_ABAP_FORMAT' ) 
             )->attributes. 
    DELETE formats WHERE name NP 'C_*' OR is_constant <> 'X'. 
 
    LOOP AT formats INTO format. 
      ASSIGN cl_abap_format=>(format-name) TO <case>. 
 
      APPEND |{ format-name WIDTH = 20 }| & 
             |{ `UPPER CASE, lower case ` CASE = (<case>) }| 
             TO output. 
    ENDLOOP. 
    out->write( output ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The three possible settings for case in a string template are specified dynamically.
