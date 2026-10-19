---
title: "Meshes - Table Builds Using Mesh Paths"
source_file: abenmesh_build_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths > INSERT mesh_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Table Builds Using Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a table is built using a mesh path.

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
CLASS cl_demo_mesh_insrt_bld_table DEFINITION 
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
                WITH NON-UNIQUE KEY col1, 
      BEGIN OF line2, 
        col1 TYPE i, 
        col2 TYPE i, 
      END OF line2, 
      t_itab2 TYPE SORTED TABLE OF line2 
                WITH NON-UNIQUE KEY col1 col2, 
      BEGIN OF MESH t_mesh, 
        node1 TYPE t_itab1 
                ASSOCIATION _node2 TO node2 ON col1 = col1, 
        node2 TYPE t_itab2, 
      END OF MESH t_mesh. 
    DATA 
      mesh TYPE t_mesh. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_mesh_insrt_bld_table IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( 'node1' 
      )->write( mesh-node1 ). 
 
    out->next_section( 
      'Building node2 from node1\_node2' ). 
    DO lines( mesh-node1 ) TIMES. 
      INSERT VALUE line2( col2 = 20 + sy-index ) INTO TABLE 
        mesh-node1\_node2[ mesh-node1[ sy-index ] ]. 
    ENDDO. 
    out->write( mesh-node2 ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    mesh-node1 = VALUE #( 
      ( col1 = 11  ) 
      ( col1 = 12  ) 
      ( col1 = 13  ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The empty mesh node `mesh-node2` is built from the filled node `mesh-node1` using the statement `INSERT`. To do this, all lines from `mesh-node1` are used as the source of the initial mesh association `\_node2` of the mesh path in a `DO` loop and a line is inserted in `mesh-node2` for each line from `mesh-node1`. The value of the column `col1` is taken from `mesh-node1` and a new value for the column `col2` is created.
