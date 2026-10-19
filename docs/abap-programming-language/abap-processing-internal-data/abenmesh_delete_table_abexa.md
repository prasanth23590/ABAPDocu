---
title: "Meshes - Deleting Single Lines in Mesh Paths"
source_file: abenmesh_delete_table_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths > DELETE mesh_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Deleting Single Lines in Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how single lines are deleted in mesh paths.

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
CLASS cl_demo_mesh_dlt_table_nmbrs DEFINITION 
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
                   WITH NON-UNIQUE KEY col1 col2 
                   WITH UNIQUE HASHED KEY mkey 
                        COMPONENTS col1 col2 col3, 
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
CLASS cl_demo_mesh_dlt_table_nmbrs IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( 'Initial node1' 
      )->write( mesh-node1 
      )->next_section( 'Initial node2' 
      )->write( mesh-node2 ). 
 
    out->next_section( 'Delete One Line Using ON' ). 
    DELETE TABLE mesh-node1\_node2[ mesh-node1[ 1 ] ]. 
    out->write( mesh-node2 ). 
 
    out->next_section( 'Delete One Line Using ON and WITH KEY' ). 
    DELETE TABLE mesh-node1\_node2[ mesh-node1[ 2 ] ] 
      WITH TABLE KEY mkey COMPONENTS col3 = 23. 
    out->write( mesh-node2 ). 
 
    out->next_section( 'Delete One Line Using ON and FROM wa' ). 
    DELETE TABLE mesh-node1\_node2[ mesh-node1[ 3 ] ] 
      FROM VALUE line2( col3 = 33  ) USING KEY mkey. 
    out->write( mesh-node2 ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    mesh-node1 = VALUE #( 
      FOR j = 1 UNTIL j > 5 
      ( col1 = 10 * j + 1 col2 = 10 * j + 2 ) ). 
    DO lines( mesh-node1 ) TIMES. 
      INSERT VALUE line2( col3 = 3 + sy-index * 10 ) 
             INTO TABLE mesh-node1\_node2[ mesh-node1[ sy-index ] ]. 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Starting from the prefilled mesh nodes `mesh-node1` and `mesh-node2`, single lines from `mesh-node2` are deleted:

- Statement `DELETE TABLE` for deleting a line using the `ON` condition.

  `DELETE TABLE mesh-node1\_node2[ mesh-node1[ 1 ] ].` The line of node `mesh-node2`, identified starting with the first line of node `mesh-node1` using the initial mesh association `\_node2`, is deleted. The `ON` condition covers the primary key used here, which means that no additional key fields need to be specified.

- Statement `DELETE TABLE` for deleting a line using the `ON` condition and with an explicitly specified key field.

  `DELETE TABLE mesh-node1\_node2[ mesh-node1[ 2 ] ] WITH TABLE KEY mkey COMPONENTS col3 = 23.` The line of node `mesh-node2`, identified starting with the second line of node `mesh-node1` using the initial mesh association `\_node2`, is deleted. The `ON` condition does not cover the secondary key `mkey`, which means that the missing key field must be specified using the addition `WITH TABLE KEY`.

- Statement `DELETE TABLE` for deleting a line using the `ON` condition and with a key field from the work area.

  `DELETE TABLE mesh-node1\_node2[ mesh-node1[ 3 ] ] FROM VALUE line2( col3 = 33 ) USING KEY mkey.` The line of node `mesh-node2`, identified starting with the third line of node `mesh-node1` using the initial mesh association `\_node2`, is deleted. The `ON` condition does not cover the secondary key `mkey`, which means that the missing key field must be specified using the addition `FROM wa`.
