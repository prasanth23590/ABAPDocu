---
title: "Component Operator, Lookup Table"
source_file: abencorresponding_using_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Component Operator, Lookup Table

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [component operator](abenconstructor_expr_corresponding.md) with `FROM ... USING`.

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
CLASS cl_demo_crrspndng_using DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF struct1, 
        a1 TYPE string, 
        a2 TYPE string, 
        b1 TYPE string, 
        b2 TYPE string, 
        c1 TYPE string, 
        c2 TYPE string, 
      END OF struct1, 
      BEGIN OF struct2, 
        a1 TYPE string, 
        a2 TYPE string, 
        b1 TYPE string, 
        b2 TYPE string, 
        c1 TYPE string, 
        d2 TYPE string, 
      END OF struct2, 
      BEGIN OF struct3, 
        u1 TYPE string, 
        u2 TYPE string, 
        v1 TYPE string, 
        v2 TYPE string, 
        w1 TYPE string, 
        w2 TYPE string, 
      END OF struct3. 
    DATA: 
      itab       TYPE STANDARD TABLE OF struct1, 
      lookup_tab TYPE STANDARD TABLE OF struct2 
                 WITH NON-UNIQUE SORTED KEY mkey COMPONENTS b1 b2, 
      jtab       TYPE STANDARD TABLE OF struct3. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_using IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `itab` 
      )->write( itab ). 
 
    out->next_section( 
      `lookup_tab` 
      )->write( lookup_tab ). 
 
    itab = CORRESPONDING #( 
              itab FROM lookup_tab 
                   USING KEY mkey b1 = a1 b2 = a2 ). 
    out->next_section( 
      `itab = CORRESPONDING #( itab FROM lookup_tab USING ... )` 
      )->write( itab ). 
 
    itab = CORRESPONDING #( 
              itab FROM lookup_tab 
                   USING KEY mkey b1 = a1 b2 = a2 
                   MAPPING a1 = a1 a2 = a2 b1 = b1 b2 = b2 c2 = d2 ). 
    out->next_section( 
    `itab = CORRESPONDING #( itab FROM lookup_tab ` && 
                                 `USING ... MAPPING ... )` 
      )->write( itab ). 
 
    jtab = CORRESPONDING #( 
             itab FROM lookup_tab 
                  USING KEY mkey b1 = a1 b2 = a2 ) ##operator. 
    out->next_section( 
      `jtab = CORRESPONDING #( itab FROM lookup_tab USING ... )` 
      )->write( jtab ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    itab = VALUE #( 
          ( a1 = `id1_1` a2 = `id2_1` 
            b1 = `000`   b2 = `000` 
            c1 = `000`   c2 = `000` ) 
          ( a1 = `id1_2` a2 = `id2_2` 
            b1 = `000`   b2 = `000` 
            c1 = `000`   c2 = `000` ) 
          ( a1 = `id1_3` a2 = `id2_3` 
            b1 = `000`   b2 = `000` 
            c1 = `000`   c2 = `000` ) ). 
    lookup_tab = VALUE #( 
      ( a1 = `a_11`  a2 = `a_12` 
        b1 = `id1_1` b2 = `id2_1` 
        c1 = `c_11`  d2 = `d_12` ) 
      ( a1 = `a_21`  a2 = `a_22` 
        b1 = `id1_3` b2 = `id2_3` 
        c1 = `c_21`  d2 = `d_22` ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example joins two internal tables `itab` and `itab2` in a constructor expression with the component operator `CORRESPONDING` in the [variant with lookup table](abencorresponding_constr_using.md).

- The first assignment specifies the condition `b1 = a1 b2 = a2` without a mapping rule after `USING`. In the `lookup_tab`, a line is found for the first and third line of `itab` and its identically named components are assigned to the corresponding line of `itab`, where `b1` and `b2` from `lookup_tab` and `a1` and `a2` from `itab` are ignored. The only identically named component remaining is `c1`. All other components keep their previous value from `itab`. The second line is transferred unchanged from `itab1`.

- In the second assignment, the default handling is overridden by specifying a mapping rule `a1 = a1 a2 = a2 b1 = b1 b2 = b2 c2 = d2`, where a mapping relationship for all components that were ignored until now is listed. Accordingly, the content of all components in the first and third line of `itab` are modified.

- Finally, the third assignment demonstrates the assignment of the expression to an internal table `jtab` that does not have the type of `itab` but is compatible with it. The result of the expression is completely assigned to `jtab`. The pragma `##operator` hides the syntax check warning stating that a temporary copy of `itab` needs to be created.
