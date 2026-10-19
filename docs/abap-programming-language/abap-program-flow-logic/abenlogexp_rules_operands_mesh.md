---
title: "rel_exp - Comparing Meshes"
source_file: abenlogexp_rules_operands_mesh.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparing Meshes

[Meshes](../abap-processing-internal-data/abenabap_meshes.md) can only be compared with meshes that are fully [compatible](../abap-data-types-and-data-objects/abencompatibility.md). The comparison is performed component by component, as for the corresponding [structure](abenlogexp_rules_operands_struc.md). The rules for [internal tables](abenlogexp_rules_operands_itab.md) also apply to comparing components.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After `mesh1` has been assigned to `mesh2`, both meshes are the same. After increasing the number of lines of component `node2` in `mesh2`, this mesh is greater than `mesh1`.

``` abap
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
  BEGIN OF MESH t_mesh, 
    node1 TYPE t_itab1 
          ASSOCIATION _node2 TO node2 ON col1 = col1, 
    node2 TYPE t_itab2, 
  END OF MESH t_mesh. 
 
DATA: 
  mesh1 TYPE t_mesh, 
  mesh2 TYPE t_mesh. 
 
mesh1-node1 = VALUE t_itab1( 
  ( col1 = 1 ) ). 
mesh1-node2 = VALUE t_itab2( 
  ( col1 = 1 col2 = 11 ) 
  ( col1 = 1 col2 = 12 ) ). 
 
mesh2 = mesh1. 
ASSERT mesh2 = mesh1. 
 
mesh2-node2 = VALUE t_itab2( 
  BASE mesh2-node2 
  ( col1 = 1  col2 = 13 ) ). 
ASSERT mesh2 > mesh1.
```
