---
title: "regex - Search for a Regular Expression"
source_file: abenregex_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - System Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - Search for a Regular Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how to search for a regular expression.

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
CLASS cl_demo_find_regex DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_find_regex IMPLEMENTATION. 
  METHOD main. 
    DATA regobj TYPE REF TO cl_abap_regex. 
 
    DATA(regex)    = `\b.at\b`. 
    DATA(text)     = `Cathy's cat with the hat sat on Matt's mat.`. 
    DATA standard TYPE cl_abap_regex=>regex_standard. 
    standard = cl_abap_regex=>c_regex_standard-pcre. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = text 
      )->add_field( CHANGING field = regex 
      )->add_field( CHANGING field = standard 
      )->request( ). 
 
    CASE standard. 
      WHEN cl_abap_regex=>c_regex_standard-pcre. 
        regobj = cl_abap_regex=>create_pcre( regex ). 
      WHEN cl_abap_regex=>c_regex_standard-xpath2. 
        regobj = cl_abap_regex=>create_xpath2( regex ). 
      WHEN cl_abap_regex=>c_regex_standard-xsd. 
        regobj = cl_abap_regex=>create_xsd( regex ). 
      WHEN cl_abap_regex=>c_regex_standard-posix. 
        regobj = cl_abap_regex=>create_posix( regex ) ##regex_posix. 
    ENDCASE. 
 
    FIND REGEX regobj IN text. 
 
    IF sy-subrc = 0. 
      REPLACE REGEX regobj IN text 
              WITH  `<font color="#FF0000"><b>$0</b></font>`. 
      out->write_html( 
        `<html><body>` && text && `</body></html>` ). 
    ELSE. 
      out->write( `Not found` ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example allows a text, a regular expression, and the syntax of the regular expression to be entered. The class searches the text line `text` for the first match of the search pattern defined in the regular expression and highlights this section in the result display. The search is case-sensitive. For searching the statement [`FIND`](abapfind.md) is used, while for marking the result, the statement [`REPLACE`](abapreplace.md) is used where the operator `$0` serves as a placeholder for the match in the replacement text.
