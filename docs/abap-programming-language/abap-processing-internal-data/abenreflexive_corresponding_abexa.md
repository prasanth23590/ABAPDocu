---
title: "Reflexive Component Assignments"
source_file: abenreflexive_corresponding_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Reflexive Component Assignments

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates assignments between components of a structure.

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
CLASS cl_demo_crrspndng_reflexive DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_reflexive IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF t_str1, 
             a1 TYPE i, 
             a2 TYPE i, 
             a3 TYPE i, 
             a4 TYPE i, 
           END OF t_str1. 
 
    TYPES: BEGIN OF t_str2, 
             b1 TYPE i, 
             b2 TYPE i, 
             a1 TYPE i, 
             a2 TYPE i, 
           END OF t_str2. 
 
    TYPES: BEGIN OF t_str3, 
             a4 TYPE i, 
             a3 TYPE i, 
             a1 TYPE i, 
             a2 TYPE i, 
           END OF t_str3. 
 
    out->begin_section( 'Reflexive Component Assignments' ). 
 
    DATA(str1) = VALUE t_str1( a1 = 1 a2 = 2 a3 = 3 a4 = 4 ). 
    FINAL(back) = str1. 
    out->write( str1 ). 
 
    out->begin_section( 'MOVE-CORRESPONDING' ). 
 
    FIELD-SYMBOLS <fs2> TYPE t_str2. 
    ASSIGN str1 TO <fs2> CASTING. 
    MOVE-CORRESPONDING str1 TO <fs2>. 
    out->write( str1 ). 
 
    str1 = back. 
    ASSIGN str1 TO <fs2> CASTING. 
    MOVE-CORRESPONDING <fs2> TO str1. 
    out->write( str1 ). 
 
    str1 = back. 
    FIELD-SYMBOLS <fs3> TYPE t_str3. 
    ASSIGN str1 TO <fs3> CASTING. 
    MOVE-CORRESPONDING str1 TO <fs3>. 
    out->write( str1 ). 
 
    str1 = back. 
    ASSIGN str1 TO <fs3> CASTING. 
    MOVE-CORRESPONDING <fs3> TO str1. 
    out->write( str1 ). 
 
    out->next_section( 'CORRESPONDING' ). 
 
    str1 = back. 
    str1 = CORRESPONDING #( 
             str1 MAPPING a1 = a4 a2 = a3 a3 = a1 a4 = a2 ) ##operator. 
    out->write( str1 ). 
 
    str1 = back. 
    str1 = CORRESPONDING #( 
             str1 MAPPING a1 = a3 a2 = a4 a3 = a2 a4 = a1 ) ##operator. 
    out->write( str1 ). 
 
    out->next_section( 'CL_ABAP_CORRESPONDING' ). 
 
    str1 = back. 
    cl_abap_corresponding=>create( 
        source      = str1 
        destination = str1 
        mapping     = VALUE cl_abap_corresponding=>mapping_table( 
          ( level = 0 kind = 1 srcname = 'a4' dstname = 'a1' ) 
          ( level = 0 kind = 1 srcname = 'a3' dstname = 'a2' ) 
          ( level = 0 kind = 1 srcname = 'a1' dstname = 'a3' ) 
          ( level = 0 kind = 1 srcname = 'a2' dstname = 'a4' ) ) 
        )->execute( EXPORTING source      = str1 
                    CHANGING  destination = str1 ). 
    out->write( str1 ). 
 
    str1 = back. 
    cl_abap_corresponding=>create( 
        source      = str1 
        destination = str1 
        mapping     = VALUE cl_abap_corresponding=>mapping_table( 
          ( level = 0 kind = 1 srcname = 'a3' dstname = 'a1' ) 
          ( level = 0 kind = 1 srcname = 'a4' dstname = 'a2' ) 
          ( level = 0 kind = 1 srcname = 'a2' dstname = 'a3' ) 
          ( level = 0 kind = 1 srcname = 'a1' dstname = 'a4' ) ) 
        )->execute( EXPORTING source      = str1 
                    CHANGING  destination = str1 ). 
    out->write( str1 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example summarizes different ways of making assignments of components in the same structure:

- In the case of the statement, [`MOVE-CORRESPONDING`](abapmove-corresponding.md) this can be done using [castings](../../abap-glossary/abencast_casting_glosry.md) with differently typed field symbols:

  - There is no overlapping of source components and target components between the type `t_str1` of the structure `str1` and the type `t_str2` of the field symbol `fs2`. In assignments of the structure to the field symbol that points to the structure, the content of the columns `a1` and `a2` is copied to the columns `a3` and `a4` because these columns have the names `a1` and `a2` in the field symbol. In assignments from the field symbol to the structure, however, the content of the columns `a3` and `a4` is copied to the columns `a1` and `a2`.

  - Identically named components overlap between the type `t_str1` of the structure `str1` and the type `t_str3` of the field symbol `fs3`. In assignments of the structure to the field symbol that points to the structure, the components are evaluated in an undefined order and the previously assigned current content of the components is used. Assignments from the field symbol to the structure produce yet another result.

    If performed at all, reflexive assignments between the components of a structure using `MOVE-CORRESPONDING` should be free of overlaps.

- In the case of the basic form of the constructor operator [`CORRESPONDING`](abencorresponding_constr_arg_type.md), a temporary copy of the structure is created as a target object and assignment is made to this copy. The two mapping rules reflect the expectations of the two preceding `MOVE-CORRESPONDING` statements and produce the expected result.

- The method `EXECUTE` of the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) is called using the same mapping rules as the two preceding constructor operators `CORRESPONDING`. No temporary copy of the structure is created as a target object, which means that the result is again the same as in the examples for `MOVE-CORRESPONDING`. In the case of dynamic mappings using `CL_ABAP_CORRESPONDING`, the source and target component should also be free of overlap.
