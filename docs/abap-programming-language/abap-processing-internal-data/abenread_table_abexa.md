---
title: "itab - Output Area"
source_file: abenread_table_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab > READ TABLE, result"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Output Area

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how and where the line content of internal tables is read to.

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
CLASS cl_demo_read_table_result DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_read_table_result IMPLEMENTATION. 
  METHOD main. 
 
    DATA: BEGIN OF line, 
            col1 TYPE i, 
            col2 TYPE i, 
          END OF line. 
 
    DATA itab LIKE SORTED TABLE OF line WITH UNIQUE KEY col1. 
 
    DATA subrc TYPE sy-subrc. 
    DATA tabix TYPE sy-tabix. 
 
    FIELD-SYMBOLS <fs> LIKE LINE OF itab. 
 
    itab = VALUE #( FOR j = 1 UNTIL j > 4 
            ( col1 = j col2 = j ** 2 ) ). 
 
    out->write_data( itab )->line( ). 
 
* INTO line COMPARING 
 
    line-col1 = 2. 
    line-col2 = 3. 
 
    READ TABLE itab FROM line INTO line COMPARING col2. 
    subrc = sy-subrc. 
 
    out->write( |sy-subrc: { subrc }| ). 
    out->write_data( line )->line( ). 
 
* INTO line TRANSPORTING 
 
    CLEAR line. 
 
    READ TABLE itab WITH TABLE KEY col1 = 3 
                    INTO line TRANSPORTING col2. 
    subrc = sy-subrc. 
    tabix = sy-tabix. 
 
    out->write( |sy-subrc: { subrc }| 
      )->write( |sy-tabix: { tabix }| 
      )->write_data( line 
      )->line( ). 
 
* TRANSPORTING NO FIELDS 
 
    READ TABLE itab WITH KEY col2 = 16  TRANSPORTING NO FIELDS. 
    subrc = sy-subrc. 
    tabix = sy-tabix. 
    out->write( |sy-subrc: { subrc }| 
      )->write( |sy-tabix: { tabix }| 
      )->line( ). 
 
* ASSIGNING 
 
    READ TABLE itab WITH TABLE KEY col1 = 2 ASSIGNING <fs>. 
 
    <fs>-col2 = 100. 
 
    out->write_data( itab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Four alternatives for output behavior when reading internal tables are shown. First a sorted table is filled with a list of square numbers.

In the first alternative, the work area `line` that is compatible with the line type is filled with the numbers 2 and 3. The `READ` statement finds the line of the table in which the key field `col1` has the same content as the work area and is copied to the work area. `sy-subrc` is two, since different numbers are found when the field `col2` is compared.

In the second alternative, the `READ` statement reads the line of the table in which the key field `col1` has the value 3. Only the content of `col2` is copied to the work area `line`. `sy-subrc` is zero and `sy-tabix` is three, since `itab` is an index table.

In the third alternative, the `READ` statement is used to search for the lines of the table in which the field `col2` has the value 16. The primary table key is not used. No fields are copied to the work area and no lines are assigned a field symbol. Only system fields are set. `sy-subrc` is zero, since a line was found and `sy-tabix` is four.

In the `READ` statement of the final alternative, the lines of the table are read in which the key field `col1` has the value 2 and are assigned to the field symbol `<fs>`. The component `col2` of `<fs>` is assigned the value 100. This also changes the corresponding table field.
