---
title: "Meshes - Forward Associations in Mesh Paths"
source_file: abenmesh_for_forward_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths > Meshes - Result of Mesh Paths > Meshes - Example of Results of Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Forward Associations in Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the results of forward associations in mesh paths.

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
CLASS cl_demo_mesh_forward_assoc DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF line1, 
        col1 TYPE i, 
      END OF line1, 
      t_itab1 TYPE SORTED TABLE OF line1 
                   WITH UNIQUE KEY col1, 
      BEGIN OF line2, 
        col1 TYPE i, 
        col2 TYPE i, 
      END OF line2, 
      t_itab2 TYPE SORTED TABLE OF line2 
                   WITH UNIQUE KEY col1 col2, 
      BEGIN OF line3, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
      END OF line3, 
      t_itab3 TYPE SORTED TABLE OF line3 
                   WITH UNIQUE KEY col1 col2 col3, 
      BEGIN OF MESH t_mesh, 
        node1 TYPE t_itab1 
             ASSOCIATION _node2 TO node2 ON col1 = col1, 
        node2 TYPE t_itab2 
             ASSOCIATION _node3 TO node3 ON col1 = col1 
                                        AND col2 = col2, 
        node3 TYPE t_itab3, 
      END OF MESH t_mesh. 
    DATA 
      mesh TYPE t_mesh. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_mesh_forward_assoc IMPLEMENTATION. 
  METHOD main. 
    DATA(idx) = 1. 
    cl_demo_input=>new( )->request( CHANGING field = idx ). 
 
    out->begin_section( 'node1' 
      )->write( mesh-node1 
      )->next_section( 'node2' 
      )->write( mesh-node2 
      )->next_section( 'node3' 
      )->write( mesh-node3 ). 
 
    IF line_exists( mesh-node1[ idx ] ). 
      out->next_section( 'node1\_node2' 
        )->write( VALUE t_itab2( 
           FOR <node2> IN 
             mesh-node1\_node2[ mesh-node1[ idx ] ] 
             ( <node2> ) ) ). 
 
      out->next_section( 'node1\_node2\_node3' 
        )->write( VALUE t_itab3( 
           FOR <node3> IN 
             mesh-node1\_node2[ mesh-node1[ idx ] ]\_node3[ ] 
             ( <node3> ) ) ). 
    ELSE. 
      out->write( `Enter a valid index for node1 ...` ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    mesh-node1 = VALUE t_itab1( 
       ( col1 = 1 ) 
       ( col1 = 2 ) 
       ( col1 = 3 ) ). 
    mesh-node2 = VALUE t_itab2( 
      ( col1 = 1  col2 = 11 ) 
      ( col1 = 1  col2 = 12 ) 
      ( col1 = 2  col2 = 21 ) 
      ( col1 = 2  col2 = 22 ) 
      ( col1 = 3  col2 = 31 ) 
      ( col1 = 3  col2 = 32 ) ). 
    mesh-node3 = VALUE t_itab3( 
      ( col1 = 1  col2 = 11 col3 = 111 ) 
      ( col1 = 1  col2 = 11 col3 = 112 ) 
      ( col1 = 1  col2 = 12 col3 = 121 ) 
      ( col1 = 1  col2 = 12 col3 = 122 ) 
      ( col1 = 2  col2 = 21 col3 = 211 ) 
      ( col1 = 2  col2 = 21 col3 = 212 ) 
      ( col1 = 2  col2 = 22 col3 = 221 ) 
      ( col1 = 2  col2 = 22 col3 = 222 ) 
      ( col1 = 3  col2 = 31 col3 = 311 ) 
      ( col1 = 3  col2 = 31 col3 = 312 ) 
      ( col1 = 3  col2 = 32 col3 = 321 ) 
      ( col1 = 3  col2 = 32 col3 = 322 ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[Table comprehensions](abenmesh_for.md) are used to construct and return internal tables that are described using forward associations in the mesh nodes `mesh-node2` and `mesh-node3`.
