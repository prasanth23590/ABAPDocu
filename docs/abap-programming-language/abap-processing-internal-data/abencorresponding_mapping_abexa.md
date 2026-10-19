---
title: "Component Operator, Mapping Rule"
source_file: abencorresponding_mapping_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Component Operator, Mapping Rule

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [component operator](abenconstructor_expr_corresponding.md) with explicit mapping rules.

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
CLASS cl_demo_crrspndng_mapping DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: 
      BEGIN OF struct1, 
        a1 TYPE string VALUE `a1_XX`, 
        a2 TYPE string VALUE `a2_XX`, 
        a3 TYPE string VALUE `a3_XX`, 
        a4 TYPE string VALUE `a4_XX`, 
      END OF struct1, 
      BEGIN OF struct2, 
        a1 TYPE string VALUE `a1_YY`, 
        a2 TYPE string VALUE `a2_YY`, 
        b3 TYPE string VALUE `b3_YY`, 
        b4 TYPE string VALUE `b4_YY`, 
      END OF struct2. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_mapping IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `struct1` 
      )->write( struct1 
      )->next_section( `struct2` 
      )->write( struct2 ). 
 
    struct2 = CORRESPONDING #( struct1 ). 
    out->begin_section( 
      `struct2 = CORRESPONDING #( struct1 )` 
     )->write( struct2 ). 
 
    struct2 = CORRESPONDING #( struct1 MAPPING b4 = a3 ). 
    out->begin_section( 
      `struct2 = CORRESPONDING #( struct1 MAPPING b4 = a3 )` 
     )->write( struct2 ). 
 
    struct2 = CORRESPONDING #( struct1 MAPPING b4 = a1 ). 
    out->begin_section( 
      `struct2 = CORRESPONDING #( struct1 MAPPING b4 = a1 )` 
     )->write( struct2 ). 
 
    struct2 = CORRESPONDING #( struct1 EXCEPT a1 ). 
    out->begin_section( 
      `struct2 = CORRESPONDING #( struct1 EXCEPT a1 )` 
     )->write( struct2 ). 
 
    struct2 = CORRESPONDING #( struct1  MAPPING b4 = a3 EXCEPT a1 ). 
    out->begin_section( 
      `struct2 = CORRESPONDING #( struct1 MAPPING b4 = a3 EXCEPT a1 )` 
     )->write( struct2 ). 
 
    struct2 = CORRESPONDING #( struct1  MAPPING b4 = a3 EXCEPT * ). 
    out->begin_section( 
      `struct2 = CORRESPONDING #( struct1 MAPPING b4 = a3 EXCEPT * )` 
     )->write( struct2 ). 
 
    struct2 = CORRESPONDING #( struct1 EXCEPT * ). 
    out->begin_section( 
      `struct2 = CORRESPONDING #( struct1 EXCEPT * )` 
     )->write( struct2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example assigns the [basic form](abencorresponding_constr_arg_type.md) of the result of a constructor expression with the component operator `CORRESPONDING` with the parameter `struct1` to a compatible structure `struct2`. Various [mapping rules](abencorresponding_constr_mapping.md) are demonstrated.

- If no mapping rule is used, the identically named components `a1` and `a2` are assigned and the other components remain initial.

- The mapping rule `MAPPING b4 = a3` also assigns the component `a3` to the component `b4`.

- The mapping rule `MAPPING b4 = a1` assigns the component `a1` twice, to `b4` and to the identically named component `a1`.

- The mapping rule `EXCEPT a1` assigns only the component `a2` to the identically named component, since the component `a1` is excluded.

- In addition to the identically named assignment, the mapping rule `MAPPING b4 = a3 EXCEPT a1` assigns the component `a3` to the component `b4` and `a1` is excluded from the identically named assignment.

- The mapping rule `EXCEPT *` does not assign any components and all components of the result remain initial.
