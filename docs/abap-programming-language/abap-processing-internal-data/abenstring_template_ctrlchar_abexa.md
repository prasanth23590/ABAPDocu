---
title: "string_tmpl - Control Characters"
source_file: abenstring_template_ctrlchar_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl) > string_tmpl - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - Control Characters

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the formatting of a text using [control characters](../../abap-glossary/abencontrol_character_glosry.md).

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
CLASS cl_demo_str_template_ctrl_char DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_template_ctrl_char IMPLEMENTATION. 
  METHOD main. 
 
    out->write( 
      |First line.\r\ttab\ttab\ttab\n\ttab\ttab\ttab\rLast line.| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A string template with literal text and control character is output using the class `CL_DEMO_OUTPUT`. The text output is formatted with line feeds and tabulators.

## Hint

Note that the output shown here is not a direct display of the character string but an HTML representation displayed in a browser. In the HTML representation, the control characters are replaced by normal characters suitable for HTML.
