---
title: "itab - Deleting Lines Using the Index"
source_file: abendelete_line_idx_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > DELETE itab > DELETE itab, itab_line > DELETE itab, index"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Deleting Lines Using the Index

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how lines can be deleted from internal tables using the index.

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
CLASS cl_demo_int_tbls_delete_ind_1 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_tbls_delete_ind_1 IMPLEMENTATION. 
  METHOD main. 
 
    DATA itab TYPE SORTED TABLE OF i WITH UNIQUE KEY table_line. 
 
    FIELD-SYMBOLS <line> LIKE LINE OF itab. 
 
    itab = VALUE #( FOR j = 1 UNTIL j > 5 ( j ) ). 
 
    DELETE itab INDEX: 2, 3, 4. 
 
    out->write( |sy-subrc: { sy-subrc }| ). 
 
    LOOP AT itab ASSIGNING <line>. 
      out->write( |{ sy-tabix } { <line> }| ). 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A sorted table `itab` is filled with five lines. Then an attempt is made to delete the lines with the indexes 2, 3, and 4 using a chained statement. However, after the deletion of each individual line, the index of each subsequent line is lowered by 1. As a result, the second delete operation deletes the line that had the index 4 first. The third deletion fails because the table now has only 4 lines.

To actually delete the lines 2 to 4, the addition [`FROM TO`](abapdelete_itab_lines.md) of the statement `DELETE` is used.
