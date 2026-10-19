---
title: "Component Operator, Nested Mapping Rule"
source_file: abencorresponding_deep_mapp_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Component Operator, Nested Mapping Rule

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [component operator](abenconstructor_expr_corresponding.md) with a nested mapping rule.

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
CLASS cl_demo_crrspndng_deep_mapp DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      BEGIN OF struct1, 
        a1   TYPE string VALUE `a1_XX`, 
        a2   TYPE string VALUE `a2_XX`, 
        BEGIN OF istruct, 
          a1 TYPE string VALUE `a1_YY`, 
          a2 TYPE string VALUE `a2_YY`, 
        END OF istruct, 
        itab LIKE STANDARD TABLE OF struct1-istruct WITH EMPTY KEY, 
      END OF struct1, 
      BEGIN OF struct2, 
        b1   TYPE string, 
        a2   TYPE string, 
        BEGIN OF istruct, 
          b1 TYPE string, 
          a2 TYPE string, 
        END OF istruct, 
        jtab LIKE STANDARD TABLE OF struct2-istruct WITH EMPTY KEY, 
      END OF struct2. 
    TYPES: 
      BEGIN OF o1, 
        a1 LIKE struct1-a1, 
        a2 LIKE struct1-a2, 
      END OF o1, 
      BEGIN OF o2, 
        a1 LIKE struct2-b1, 
        a2 LIKE struct2-a2, 
      END OF o2. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_deep_mapp IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `struct1` 
      )->write( CORRESPONDING o1( struct1 ) 
      )->write( struct1-istruct 
      )->write( struct1-itab ). 
 
    struct2 = CORRESPONDING #( struct1 ). 
    out->next_section( 
      `struct2 = CORRESPONDING #( struct1 )` 
      )->write( CORRESPONDING o2( struct2 ) 
      )->write( struct2-istruct 
      )->write( struct2-jtab ). 
 
    struct2 = CORRESPONDING #( struct1 MAPPING jtab = itab ). 
    out->next_section( 
      `struct2 = CORRESPONDING #( struct1 MAPPING jtab = itab )` 
      )->write( CORRESPONDING o2( struct2 ) 
      )->write( struct2-istruct 
      )->write( struct2-jtab ). 
 
    struct2 = CORRESPONDING #( struct1 MAPPING 
               ( istruct = istruct MAPPING b1 = a1 EXCEPT a2 ) 
               ( jtab = itab MAPPING b1 = a1 ) ). 
    out->next_section( 
      `struct2 = CORRESPONDING #( struct1  MAPPING ( ... ) )` 
      )->write( CORRESPONDING o2( struct2 ) 
      )->write( struct2-istruct 
      )->write( struct2-jtab ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    struct1-itab = VALUE #( 
          ( a1 = `a1_xx` a2 = `a2_xx` ) 
          ( a1 = `a1_yy` a2 = `a2_yy` ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example assigns the [basic form](abencorresponding_constr_arg_type.md) of the result of a constructor expression with the component operator `CORRESPONDING` with the parameter `struct1` to a compatible structure `struct2`. Various [mapping rules](abencorresponding_constr_mapping.md) are demonstrated. The structures contain a substructure and a tabular component.

- If there is not mapping rule, the identically named components `a2` and `istruct` are assigned at the top level. The substructure `istruct` is resolved and the component `a2` is assigned here. The tabular components are not identically named and are not assigned.

- The mapping rule `MAPPING jtab = itab` is also used to assign the tabular component, whereby only the identically named column `a2` is considered.

- The nested mapping rule

  `MAPPING ( istruct = istruct MAPPING b1 = a1 EXCEPT a2 ) ( jtab = itab MAPPING b1 = a1 )` is used to

  - specify a mapping relationship for the components of the substructure `istruct`. Here, `istruct = istruct` must be specified at the top level.

  - define a mapping for the tabular components. Here, a mapping is also nested for their columns.

    In the result, all components are filled except the component `a2` of the substructure that was excluded using `EXCEPT`.
