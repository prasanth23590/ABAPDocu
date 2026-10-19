---
title: "itab - Table Comprehensions, Local Helper Fields"
source_file: abentable_cmprhnsns_locals_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Comprehensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Comprehensions, Local Helper Fields

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how local helper fields are used in [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md).

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
CLASS cl_demo_table_comprh_locals DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_table_comprh_locals IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      array TYPE STANDARD TABLE OF i WITH EMPTY KEY, 
      BEGIN OF line, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
      END OF line, 
      itab TYPE STANDARD TABLE OF line WITH EMPTY KEY. 
 
    CONSTANTS factor TYPE i VALUE 1000. 
 
    FINAL(array) = VALUE array( 
      ( 3 ) ( 5 ) ( 7 ) ( 9 ) ). 
 
    FINAL(itab) = VALUE itab( 
      FOR x IN array INDEX INTO idx 
         LET off = factor * idx IN 
        ( col1 = x col2 = x * x col3 = x + off ) ). 
 
    out->write( itab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

From a single column table `array`, a three-column table `itab` is created whose column content is calculated from the respective line content in `array`. The local helper fields in this example are the work area `x` of the [`FOR` expression](abenfor_in_itab.md) and the helper field `off` defined in a [`LET` expression](../abap-declarations/abaplet.md).
