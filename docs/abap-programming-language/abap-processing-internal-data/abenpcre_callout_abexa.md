---
title: "regex - PCRE Regular Expression with Callouts"
source_file: abenpcre_callout_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Regular Expressions (regex) > regex - System Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# regex - PCRE Regular Expression with Callouts

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how to call an ABAP method from a PCRE regular expression.

## Source Code

``` abap
* CCDEF 
CLASS o DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA out TYPE REF TO if_demo_output. 
ENDCLASS. 
 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_pcre_callout DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS handle_regex DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES if_abap_matcher_callout. 
ENDCLASS. 
 
CLASS handle_regex IMPLEMENTATION. 
  METHOD if_abap_matcher_callout~callout. 
    o=>out->write( 
    |{ callout_num } { callout_string }| ). 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_pcre_callout IMPLEMENTATION. 
  METHOD main. 
    o=>out = out. 
 
    FINAL(regex) = cl_abap_regex=>create_pcre( 
      pattern = `a(?C1)b(?C2)c(?C3)d(?C"D")e(?C"E")` ). 
 
    FINAL(matcher) = regex->create_matcher( text = `abcde` ). 
 
    FINAL(handler) = NEW handle_regex( ). 
    matcher->set_callout( handler ). 
    matcher->match( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

An object-oriented representation of a PCRE regular expression is created from class [`CL_ABAP_REGEX`](abenregex_system_classes.md). The regular expression contains the [special characters](abenregex_pcre_syntax_specials.md) `(?C...)` for callouts. The first three callouts pass numeric data, the other two pass string data.

A local class `handle_regex` implements the interface `IF_ABAP_MATCHER_CALLOUT` and an instance of that class is set as the callout handler. When the regular expression is matched, the interface method `CALLOUT` is called for each callout position and can access the passed parameter.
