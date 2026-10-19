---
title: "itab - Table Comprehensions, Basic Properties"
source_file: abentable_cmprhnsns_simple_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Comprehensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Comprehensions, Basic Properties

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the basic properties of [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md).

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
CLASS cl_demo_table_comprh_elmntry DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF line1, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
        col4 TYPE i, 
      END OF line1, 
      itab1 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY 
                                         WITH UNIQUE SORTED KEY 
                                              key COMPONENTS col1, 
      BEGIN OF line2, 
        col1 TYPE i, 
        col2 TYPE i, 
      END OF line2, 
      itab2 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY, 
      itab3 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY, 
      itab4 TYPE STANDARD TABLE OF line2 WITH EMPTY KEY, 
      itab5 TYPE STANDARD TABLE OF i     WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_table_comprh_elmntry IMPLEMENTATION. 
  METHOD main. 
 
    FINAL(itab1) = VALUE itab1( 
      FOR j = 41 THEN j - 10 UNTIL j < 10 
      ( col1 = j col2 = j + 1 col3 = j + 2 col4 = j + 3 ) ). 
    out->write( itab1 ). 
 
    FINAL(itab2) = VALUE itab2( 
      FOR wa IN itab1 WHERE ( col1 < 30 ) ##PRIMKEY[KEY] 
        ( wa ) ). 
    out->write( itab2 ). 
 
    FINAL(itab3) = VALUE itab3( 
      FOR wa IN itab1 INDEX INTO idx WHERE ( col1 = 21 ) ##PRIMKEY[key] 
        ( LINES OF itab1 FROM idx ) ). 
    out->write( itab3 ). 
 
    FINAL(itab4) = VALUE itab4( 
       FOR wa IN itab1 FROM 2 TO 3 
         ( col1 = wa-col2 col2 = wa-col3 ) ). 
    out->write( itab4 ). 
 
    FINAL(base)  = VALUE itab5( ( 1 ) ( 2 ) ( 3 ) ). 
    FINAL(itab5) = VALUE itab5( 
       BASE base 
       FOR wa IN itab1 USING KEY key 
          ( wa-col1 ) ). 
    out->write( itab5 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

From an internal table `itab1`, the content of new internal tables is created in constructor expressions with one [`FOR` expression](abenfor_in_itab.md) each:

- `itab2` has the same line type as `itab1`. All columns of all lines are assigned that meet a `WHERE` condition.

- `itab3` has the same line type as `itab1`. All lines are assigned that meet a `WHERE` condition from a line.

- `itab4` has fewer columns than `itab1`. Only certain columns of a restricted number of lines are assigned.

- `itab5` has only one column. The addition `BASE` is used to first assign the table `base` and then the first column of `itab1`. This demonstrates the effect of specifying a sorted secondary key for this column.
