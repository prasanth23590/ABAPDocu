---
title: "cstring_func - escape for HTML"
source_file: abenstring_function_escape_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - escape for HTML

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the string function [`escape`](abenescape_functions.md) for HTML.

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
CLASS cl_demo_escape_html DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_escape_html IMPLEMENTATION. 
  METHOD main. 
    DATA: body     TYPE string, 
          esc_body TYPE string. 
 
    body = `<table border> ` 
        && `<tr><td>11</td><td>12</td></tr> ` 
        && `<tr><td>21</td><td>22</td></tr> ` 
        && `</table>`. 
 
    esc_body = escape( val    = body 
                       format = cl_abap_format=>e_html_text ). 
 
    out->begin_section( 'Original text' 
      )->write_text( body 
 
      )->next_section( 'Original text formatted as HTML' 
      )->write_html( body 
 
      )->next_section( 'Escaped text' 
      )->write_text( esc_body 
 
      )->next_section( 'Escaped text formatted as HTML' 
      )->write_html( esc_body ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class applies the function `escape` to a string used as the body of an HTML file. The string is displayed as a text and as an HTML file both before and after the function is executed.
