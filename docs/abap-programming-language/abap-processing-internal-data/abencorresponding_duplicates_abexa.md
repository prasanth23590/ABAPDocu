---
title: "Component Operator, Handling Duplicates"
source_file: abencorresponding_duplicates_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Component Operator, Handling Duplicates

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [component operator](abenconstructor_expr_corresponding.md) with the addition [`DISCARDING DUPLICATES`](abencorresponding_constr_dupl.md).

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
CLASS cl_demo_crrspndng_duplicates DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_duplicates IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF line, 
        a1 TYPE i, 
        a2 TYPE i, 
      END OF line, 
      ntab1 TYPE STANDARD TABLE OF line WITH EMPTY KEY, 
      ntab2 TYPE SORTED   TABLE OF  line WITH UNIQUE KEY a1, 
      BEGIN OF line1, 
        x1 TYPE i, 
        x2 TYPE ntab1, 
      END OF line1, 
      BEGIN OF line2, 
        y1 TYPE i, 
        y2 TYPE ntab2, 
      END OF line2, 
      itab1 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY, 
      itab2 TYPE SORTED   TABLE OF line2 WITH UNIQUE KEY y1. 
 
    FINAL(itab1) = 
      VALUE itab1( ( x1 = 1 x2 = VALUE #( ( a1 = 1 a2 = 2 ) 
                                          ( a1 = 3 a2 = 4 ) ) ) 
                   ( x1 = 2 x2 = VALUE #( ( a1 = 1 a2 = 2 ) 
                                          ( a1 = 1 a2 = 4 ) ) ) 
                   ( x1 = 1 x2 = VALUE #( ( a1 = 1 a2 = 2 ) 
                                          ( a1 = 3 a2 = 4 ) ) ) ). 
 
    FINAL(itab2) = 
      CORRESPONDING itab2( itab1 DISCARDING DUPLICATES 
                           MAPPING y1 = x1 
                                   y2 = x2 DISCARDING DUPLICATES ). 
 
    LOOP AT itab2 INTO FINAL(wa). 
      out->write( wa-y1 
        )->write( wa-y2 
        )->line( ). 
    ENDLOOP. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The addition `DISCARDING DUPLICATES` is used twice to ignore duplicate lines:

- `DISCARDING DUPLICATES` after `itab1` prevents an exception when inserting the third line of `itab1` in `itab2`.

- In the mapping rule, `DISCARDING DUPLICATES` prevents the exception when the second line of the tabular component `x2` is inserted when inserting the second line of `itab1` in `itab2`.
