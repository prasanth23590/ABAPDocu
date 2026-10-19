---
title: "Meshes - Reflexive Associations in Mesh Paths"
source_file: abenmesh_for_reflex_sngl_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths > Meshes - Result of Mesh Paths > Meshes - Example of Results of Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Reflexive Associations in Mesh Paths

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the results of reflexive mesh associations in mesh paths.

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
CLASS cl_demo_mesh_rflxv_assoc_sngl DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF line, 
        id        TYPE i, 
        parent_id TYPE i, 
        name      TYPE string, 
      END OF line, 
      t_itab TYPE SORTED TABLE OF line WITH UNIQUE KEY id 
             WITH NON-UNIQUE SORTED KEY by_parent COMPONENTS parent_id, 
      BEGIN OF MESH t_mesh, 
        node TYPE t_itab 
             ASSOCIATION _node TO node ON parent_id = id 
                         USING KEY by_parent, 
      END OF MESH t_mesh. 
    DATA 
      mesh TYPE t_mesh. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_mesh_rflxv_assoc_sngl IMPLEMENTATION. 
  METHOD main. 
    DATA(id) = 1. 
    cl_demo_input=>new( )->request( CHANGING field = id ). 
 
    out->begin_section( 'node' 
      )->write( mesh-node ). 
 
    IF line_exists( mesh-node[ id = id ] ). 
      out->next_section( '\_node' 
        )->write( VALUE t_itab( 
           FOR <node> IN mesh-node\_node[ mesh-node[ id = id ] ] 
              ( <node> ) ) ). 
 
      out->next_section( '\_node+' 
        )->write( VALUE t_itab( 
           FOR <node> IN mesh-node\_node+[ mesh-node[ id = id ] ] 
              ( <node> ) ) ). 
 
      out->next_section( '\_node*' 
        )->write( VALUE t_itab( 
           FOR <node> IN mesh-node\_node*[ mesh-node[ id = id ] ] 
              ( <node> ) ) ) ##PRIMKEY[BY_PARENT]. 
    ELSE. 
      out->write( `Enter a valid ID ...` ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    mesh-node = VALUE t_itab( 
        ( id = 1  parent_id = 0 name = 'AA'          ) 
        ( id = 2  parent_id = 1 name = 'AA-AA'       ) 
        ( id = 3  parent_id = 2 name = 'AA-AA-AA'    ) 
        ( id = 4  parent_id = 2 name = 'AA-AA-BB'    ) 
        ( id = 5  parent_id = 1 name = 'AA-BB'       ) 
        ( id = 6  parent_id = 5 name = 'AA-BB-AA'    ) 
        ( id = 7  parent_id = 6 name = 'AA-BB-AA-AA' ) 
        ( id = 8  parent_id = 6 name = 'AA-BB-AA-BB' ) 
        ( id = 9  parent_id = 5 name = 'AA-BB-BB'    ) 
        ( id = 10 parent_id = 9 name = 'AA-BB-BB-AA' ) 
        ( id = 11 parent_id = 1 name = 'AA-CC'       ) 
        ( id = 12 parent_id = 0 name = 'BB'          ) 
        ( id = 13 parent_id = 0 name = 'CC'          ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In a reflexive mesh association (self-association), the source and target nodes are the same. A reflexive mesh association implements semantic relationships between the lines of a mesh node. This example shows the result sets of reflexive mesh associations for an internal table in which a hierarchical tree structure is stored.

- Simple reflexive mesh association

  `mesh-node\_node[ mesh-node[ id = id ] ]` The result set includes all lines in which, in accordance with the `ON` condition, the column `parent_id` is the same as the column `id` of the source. In the tree hierarchy, these are the direct subnodes of the line described using `source`.

- Transitive mesh association with `+`

  `mesh-node\_node+[ mesh-node[ id = id ] ]` The result set also includes all further lines for which, based on the first result set, the `ON` condition is met. In the tree hierarchy, these are all subnodes of the line described using `source`.

- Transitive mesh association with `*`

  `mesh-node\_node*[ mesh-node[ id = id ] ]` The result set also includes the line described by `source`.
