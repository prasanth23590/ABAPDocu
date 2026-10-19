---
title: "Meshes - Changing Single Lines in Mesh Paths"
source_file: abenmesh_modify_table_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths > MODIFY mesh_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Changing Single Lines in Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how single lines are changed in mesh paths.

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
CLASS cl_demo_mesh_modify_tble_nmbrs DEFINITION 
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
                   WITH NON-UNIQUE KEY col1 
                   WITH UNIQUE HASHED KEY mkey 
                        COMPONENTS col1 col2, 
      BEGIN OF MESH t_mesh, 
        node1 TYPE t_itab1 
        ASSOCIATION _node2_1 TO node2 ON col1 = col1 
                                     AND col2 = col2 
        ASSOCIATION _node2_2 TO node2 ON col1 = col1, 
        node2 TYPE t_itab2, 
      END OF MESH t_mesh. 
    DATA 
      mesh TYPE t_mesh. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_mesh_modify_tble_nmbrs IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( 'Initial node1' 
      )->write( mesh-node1 
      )->next_section( 'Initial node2' 
      )->write( mesh-node2 ). 
 
    out->next_section( 'Modify One Line Using ON' ). 
    MODIFY TABLE mesh-node1\_node2_1[ mesh-node1[ 1 ] ] 
      FROM VALUE line2( col2 = 111 col3 = 222 ) 
                 TRANSPORTING col2 col3. 
    out->write( mesh-node2 ). 
 
    out->next_section( 'Modify One Line Using ON and FROM wa' ). 
    MODIFY TABLE mesh-node1\_node2_2[ mesh-node1[ 2 ] ] 
      FROM VALUE line2( col2 = 22 col3 = 333 ) 
                 USING KEY mkey TRANSPORTING col3. 
    out->write( mesh-node2 ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    mesh-node1 = VALUE #( 
      FOR j = 11 THEN j + 10 WHILE j < 30 
          ( col1 = j col2 = j + 1  ) ). 
    DO lines( mesh-node1 ) TIMES. 
      INSERT VALUE line2( col3 = 3 + sy-index * 10 ) 
        INTO TABLE mesh-node1\_node2_1[ mesh-node1[ sy-index ] ]. 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Starting from the filled mesh nodes `mesh-node1` and `mesh-node2`, single lines from `mesh-node2` are changed:

- Statement `MODIFY TABLE` for changing a line using the `ON` condition.

  `MODIFY TABLE mesh-node1\_node2_1[ mesh-node1[ 1 ] ] FROM VALUE line2( col2 = 111 col3 = 222 ) TRANSPORTING col2 col3.` The `ON` condition of the mesh association `_node2_1` covers the primary table key of the node `node2` and is used to identify the line that needs to be modified.

- Statement `MODIFY TABLE` for changing a line using the `ON` condition and with a key field from the work area.

  `MODIFY TABLE mesh-node1\_node2_2[ mesh-node1[ 2 ] ] FROM VALUE line2( col2 = 22 col3 = 333 ) USING KEY mkey TRANSPORTING col3.` The `ON` condition of the mesh association `_node2_2` does not cover the table key `mkey` and the missing information is taken from column `col2` of the work area after `FROM`.
