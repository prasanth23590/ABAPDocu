---
title: "itab - Deleting Duplicate Lines"
source_file: abendelete_dup_lines_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > DELETE itab > DELETE itab, duplicates"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Deleting Duplicate Lines

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how adjacent duplicate lines in internal tables can be deleted.

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
CLASS cl_demo_int_tbls_delete_adjcnt DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_tbls_delete_adjcnt IMPLEMENTATION. 
  METHOD main. 
 
    DATA: BEGIN OF line, 
            col1 TYPE i, 
            col2 TYPE c LENGTH 1, 
          END OF line. 
 
    DATA itab LIKE STANDARD TABLE OF line 
              WITH NON-UNIQUE KEY col2. 
 
    itab = VALUE #( ( col1 = 1 col2 = 'A' ) 
                    ( col1 = 1 col2 = 'A' ) 
                    ( col1 = 1 col2 = 'B' ) 
                    ( col1 = 2 col2 = 'B' ) 
                    ( col1 = 3 col2 = 'B' ) 
                    ( col1 = 4 col2 = 'B' ) 
                    ( col1 = 5 col2 = 'A' ) ). 
 
    FINAL(o) = out->write_data( itab ). 
 
    DELETE ADJACENT DUPLICATES FROM itab COMPARING ALL FIELDS. 
    out->write_data( itab ). 
 
    DELETE ADJACENT DUPLICATES FROM itab COMPARING col1. 
    out->write_data( itab ). 
 
    DELETE ADJACENT DUPLICATES FROM itab. 
    out->write_data( itab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `main` creates and fills a standard table. The first `DELETE` statement deletes the second line since it has the same content as the first line. The second `DELETE` statement deletes the second line from the remaining table since the content of the field `col1` is the same as in the first line. The third `DELETE` statement deletes the third and fourth lines of the remaining table since the content of the key field `col2` is the same as in the second line. Although the content of the key fields for the first and fifth lines is the same, the fifth line is not deleted because it is not adjacent to the first line.
