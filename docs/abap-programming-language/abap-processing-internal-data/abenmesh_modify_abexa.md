---
title: "Meshes - Changing Multiple Lines in Mesh Paths"
source_file: abenmesh_modify_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths > MODIFY mesh_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Changing Multiple Lines in Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how multiple lines are changed in mesh paths.

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
CLASS cl_demo_mesh_modify_nmbrs DEFINITION 
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
        col2 TYPE i, 
      END OF line1, 
      t_itab1 TYPE SORTED TABLE OF line1 
                   WITH NON-UNIQUE KEY col1 col2, 
      BEGIN OF line2, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
      END OF line2, 
      t_itab2 TYPE SORTED TABLE OF line2 
                   WITH NON-UNIQUE KEY col1 col2, 
      BEGIN OF MESH t_mesh, 
        node1 TYPE t_itab1 
          ASSOCIATION _node2 TO node2 ON col1 = col1 
                                     AND col2 = col2, 
        node2 TYPE t_itab2, 
      END OF MESH t_mesh. 
    DATA 
      mesh TYPE t_mesh. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_mesh_modify_nmbrs IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( 'Initial node1' 
      )->write( mesh-node1 
      )->next_section( 'Initial node2' 
      )->write( mesh-node2 ). 
 
    out->next_section( 'Modify Multiple Lines Using ON' ). 
    MODIFY mesh-node1\_node2[ mesh-node1[ 1 ] ] 
      FROM VALUE line2( col3 = 111 ) TRANSPORTING col3. 
    out->write( mesh-node2 ). 
 
    out->next_section( 'Modify Multiple Lines Using ON and WHERE' ). 
    MODIFY mesh-node1\_node2[ mesh-node1[ 2 ] WHERE col3 > 23 ] 
      FROM VALUE line2( col3 = 222 ) TRANSPORTING col3. 
    out->write( mesh-node2 ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    mesh-node1 = VALUE #( 
      FOR j = 11 THEN j + 10 WHILE j < 30 
          ( col1 = j col2 = j + 1  ) ). 
    DO 3 TIMES. 
      FINAL(idx) = sy-index. 
      DO lines( mesh-node1 ) TIMES. 
        INSERT VALUE line2( col3 = 2 + idx + sy-index * 10 ) 
          INTO TABLE mesh-node1\_node2[ mesh-node1[ sy-index ] ]. 
      ENDDO. 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Starting from the filled mesh nodes `mesh-node1` and `mesh-node2`, multiple lines from `mesh-node2` are changed:

- Statement `MODIFY` for deleting multiple lines using the `ON` condition.

  `MODIFY mesh-node1\_node2[ mesh-node1[ 1 ] ] FROM VALUE line2( col3 = 111 ) TRANSPORTING col3.` All lines of the node `mesh-node2` identified starting with the first line of the node `mesh-node1` using the initial mesh association `\_node2` are changed in the third column.

- Statement `DELETE` for deleting multiple lines using the `ON` condition with an additional `WHERE` condition.

  `MODIFY mesh-node1\_node2[ mesh-node1[ 2 ] WHERE col3 > 23 ] FROM VALUE line2( col3 = 222 ) TRANSPORTING col3.` All lines of the node `mesh-node2` identified starting with the second line of the node `mesh-node1` using the initial mesh association `\_node2` and that meet the additional `WHERE` condition are changed in the third column.
