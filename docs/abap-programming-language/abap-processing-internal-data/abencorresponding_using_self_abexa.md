---
title: "Component Operator, Reflexive Assignment"
source_file: abencorresponding_using_self_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Component Operator, Reflexive Assignment

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [component operator](abenconstructor_expr_corresponding.md) with `FROM USING` for a single table.

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
CLASS cl_demo_crrspndng_using_self DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF struct, 
        node   TYPE string, 
        parent TYPE string, 
        text   TYPE string, 
      END OF struct. 
    DATA 
      itab TYPE HASHED TABLE OF struct 
           WITH UNIQUE KEY node. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_using_self IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `itab` 
      )->write( itab ). 
 
 
    itab = CORRESPONDING #( 
              itab FROM itab 
                   USING node = parent ) ##operator. 
    out->next_section( 
      `itab = CORRESPONDING #( itab FROM itab USING node = parent )` 
      )->write( itab ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    itab = VALUE #( 
      ( node = `0` parent = `-`  text = `node0`  ) 
      ( node = `1` parent = `0`  text = `node1` ) 
      ( node = `2` parent = `1`  text = `node2` ) 
      ( node = `3` parent = `1`  text = `node3` ) 
      ( node = `4` parent = `3`  text = `node4` ) 
      ( node = `5` parent = `3`  text = `node5` ) 
      ( node = `6` parent = `1`  text = `node6` ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Using the component operator `CORRESPONDING` in the [variant with lookup table](abencorresponding_constr_using.md), the example relates an internal table `itab` in a component expression to itself and assigns the result to the same table. This requires a temporary copy of the table to be created, which raises a warning from the syntax check. This warning can be hidden using the pragma `##operator`.

The table contains a hierarchical tree structure in which nodes of the column `node` are assigned to a parent node using the column `parent`. This relationship is specified after `USING`, which finds the parent node for every line. The assignment of the identically named component `text` ensures that every line in this column is given the content of its direct parent node.

For further examples of reflexive assignments, see the executable example [Reflexive Component Assignments](abenreflexive_corresponding_abexa.md).
