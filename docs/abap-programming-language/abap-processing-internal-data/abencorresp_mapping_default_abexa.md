---
title: "CORRESPONDING Operator Using the Additions MAPPING and DEFAULT"
source_file: abencorresp_mapping_default_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CORRESPONDING Operator Using the Additions MAPPING and DEFAULT

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the `CORRESPONDING` operator and the additions `MAPPING` and `DEFAULT`.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">CORRESPONDING operator with MAPPING and 
"! DEFAULT additions</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_corr_op_map_default DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_corr_op_map_default IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Demo: CORRESPONDING operator` && 
    ` using the additions MAPPING and DEFAULT` ). 
 
    "Creating structures 
    DATA: BEGIN OF struc1, 
            id1 TYPE i, 
            a   TYPE string, 
            b   TYPE string, 
            c   TYPE i, 
            d   TYPE string, 
            e   TYPE i, 
          END OF struc1. 
 
    DATA: BEGIN OF struc2, 
            id2 TYPE i, 
            a   TYPE string, 
            b   TYPE string, 
            c   TYPE i, 
            d   TYPE string, 
            z   TYPE i, 
          END OF struc2. 
 
    "Creating internal table 
    DATA itab1 LIKE TABLE OF struc1 WITH EMPTY KEY. 
 
    "Filling structure 
    struc1 = VALUE #( id1 = 1 a = `a`  b = `b` c = 2 d = `c` e = 3 ). 
 
    "1) Assignment using CORRESPONDING (DEFAULT only) 
    "- Component a is not specified; it is mapped anyway 
    "  due to the identical name and not being explicitly specified 
    "  for mapping 
    "- The other components demonstrate various expressions 
    "  in combination with the DEFAULT addition 
    "- Component d: Since the table is initial, there would be 
    "  a shortdump if there was not the DEFAULT addition specified 
    "  as part of the expression with the VALUE operator 
    struc2 = CORRESPONDING #( 
      struc1 MAPPING id2 = id1 
                     b = DEFAULT `ha` && `llo` 
                     c = DEFAULT 1 + 5 
                     d = DEFAULT VALUE #( itab1[ 1 ]-d DEFAULT `hi` ) 
                     z = DEFAULT cl_abap_random_int=>create( 
                                        seed = cl_abap_random=>seed( ) 
                                        min  = 1 
                                        max = 100 )->get_next( ) ). 
 
    out->write( struc2 ). 
 
    "2) Assignment using CORRESPONDING (DEFAULT preceded by source 
    "   component on the right-hand side) 
    "- Component a is not specified; it is mapped anyway 
    "  due to the identical name and not being explicitly specified 
    "  for mapping 
    "- The other components demonstrate various expressions 
    "  in combination with the DEFAULT addition 
    "- Component b: The value of component b in the source is initial. 
    "  Hence, the result of the expression is assigned. 
    "- Component c: The value of component c in the source is not 
    "  initial. Hence, the value of c is assigned. 
    "- Component d: Not initial. Value of d is assigned. 
    "- Component e: Initial. Result of the expression is assigned. 
 
    "Filling structure 
    struc1 = VALUE #( id1 = 1 a = `a` b = `` c = 2 d = `c` e = 0 ). 
 
    struc2 = CORRESPONDING #( 
      struc1 MAPPING id2 = id1 
                     b = b DEFAULT `ha` && `llo` 
                     c = c DEFAULT 1 + 5 
                     d = d DEFAULT VALUE #( itab1[ 1 ]-d DEFAULT `hi` ) 
                     z = e DEFAULT cl_abap_random_int=>create( 
                                        seed = cl_abap_random=>seed( ) 
                                        min  = 1 
                                        max = 100 )->get_next( ) ). 
 
    out->write( struc2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example covers assignments with the `CORRESPONDING` operator demonstrating expressions following the `DEFAULT` addition.

Check the comments in the source code for more information.
