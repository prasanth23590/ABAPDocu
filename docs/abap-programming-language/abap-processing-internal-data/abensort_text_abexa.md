---
title: "Sorting Internal Tables Alphabetically"
source_file: abensort_text_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > SORT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Sorting Internal Tables Alphabetically

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the alphabetical sorting of character strings.

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
CLASS cl_demo_int_tbls_sort_text DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_tbls_sort_text IMPLEMENTATION. 
  METHOD main. 
 
    DATA: BEGIN OF line, 
            text(6) TYPE c, 
            xtext   TYPE xstring, 
          END OF line. 
 
    DATA itab LIKE HASHED TABLE OF line WITH UNIQUE KEY text. 
 
    line-text = 'Muller'(001). 
    CONVERT TEXT line-text INTO SORTABLE CODE line-xtext. 
    INSERT line INTO TABLE itab. 
 
    line-text = 'M&#x00F6;ller'(002). 
    CONVERT TEXT line-text INTO SORTABLE CODE line-xtext. 
    INSERT line INTO TABLE itab. 
 
    line-text = 'Moller'(003). 
    CONVERT TEXT line-text INTO SORTABLE CODE line-xtext. 
    INSERT line INTO TABLE itab. 
 
    line-text = 'Miller'(004). 
    CONVERT TEXT line-text INTO SORTABLE CODE line-xtext. 
    INSERT line INTO TABLE itab. 
 
    SORT itab. 
    out->write_data( itab ). 
 
    SORT itab BY xtext. 
    out->write_data( itab ). 
 
    SORT itab AS TEXT. 
    out->write_data( itab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `itab` contains a column of text fields and a column of associated country-specific sortable binary characters that were created in a sortable format using conversions. The table is sorted three times. First, binarily for the key field `text`, then binarily for the `xtext` field, and finally alphabetically for the key field `text`.

In the first sort *M&#x00F6;ller* comes after *Muller*, because the internal representation of '&#x00F6;' comes after the representation for 'u'. Both the other sorts are alphabetical. The binary sort performed on `xtext` has the same result as an alphabetical sort on the field `text`.
