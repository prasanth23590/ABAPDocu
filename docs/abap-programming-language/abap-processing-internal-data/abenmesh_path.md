---
title: "Meshes - mesh_path"
source_file: abenmesh_path.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - mesh_path

## Syntax

``` abap
... {mesh-|<mesh>-|mesh_ref->}rnode\_associ[ ...]\_assoc1[ ... ]\_assoc2[ ... ] ...  
```

[`\_associ[ ...`](abenmesh_path_assoc.html) · [`]`](abenmesh_path_assoc.md) · [`\_assoc1[ ... ]`](abenmesh_path_assoc.md) · [`\_assoc2[ ... ]`](abenmesh_path_assoc.md)

### Addition

[1. `... {mesh-|<mesh>-|mesh_ref->}rnode`](abenmesh_path.md#addition-1)

[2. `... \_associ[ source [cond] ]`](abenmesh_path.html#addition-2)

[3. `... \_assoc1[ [cond] ]\_assoc2[ [cond] ] ...`](abenmesh_path.html#addition-3)

## Overview

### Description

Specifies a mesh path in [statements and expressions](abenmesh_path_usage.md) used to process meshes. A mesh path is always constructed as follows:

- A root node `rnode` specification

- An initial mesh association `\_associ` specification between a root node and a follow-on node

- Optional further mesh associations `\_assoc1`, `\_assoc2`, ... specifications whose start nodes can be the follow-on nodes of preceding mesh associations.

When specifying a mesh path, it is not significant whether the address nodes of the mesh are internal tables or references to internal tables. When a mesh path is evaluated, references to internal tables are dereferenced automatically. A mesh path describes a set of lines in its final path node as its [result](abenmesh_path_result.md).

### Hint

A mesh path cannot exit a mesh. Each follow-on node is part of the same mesh as the root node. Meshes can, however, be nested by specified a [mesh path expression](abenmesh_path_expression.md) as the source of the initial mesh association.

## Addition 1

`... {mesh-|<mesh>-|mesh_ref->}rnode`

### Description

Root node `rnode` of a mesh path. `rnode` is a node of a [mesh type](../../abap-glossary/abenmesh_type_glosry.md) that must be the start node or target node of a [mesh association](../abap-declarations/abaptypes_mesh_association.md) of the mesh type. The same options are available when specifying the mesh as when addressing regular structure components:

- `mesh-rnode`

  `mesh` is a mesh, that is, a data object of the respective [mesh type](../../abap-glossary/abenmesh_type_glosry.md). The root node is addressed using the structure component selector (`-`).

- `<mesh>-rnode`

  `<mesh>` is a field symbol typed with the mesh type and to which a mesh is assigned. The root node is addressed using the structure component selector (`-`).

- `mesh_ref->rnode`

  `mesh_ref` is a reference variable whose static type is the mesh type and that points to a mesh. The root node is addressed using the object component selector (`->`).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a mesh type `mesh` with internal tables and a mesh type `refmesh` with references to internal tables as components. A data object `mesh` has the type `mesh` and a data object `meshref` points to a data object of type `refmesh`. The root node of the first mesh path is `mesh-node1`. The structure component selector is used here. The root node of the second mesh path is `node1` in the anonymous data object of type `refmesh`, for which the object component selector is used. The references within the mesh are dereferenced implicitly.

``` abap
TYPES: 
  BEGIN OF MESH mesh, 
    node1 TYPE itab1 ASSOCIATION _assoc2 TO node2 ON ... 
    node2 TYPE itab2, 
  END OF MESH mesh, 
  BEGIN OF MESH refmesh, 
    node1 TYPE REF TO itab1 ASSOCIATION _assoc2 TO node2 ON ... 
    node2 TYPE REF TO itab2, 
  END OF MESH refmesh. 
 
DATA(mesh) =    VALUE mesh( ). 
DATA(meshref) = NEW refmesh( VALUE refmesh( ) ). 
 
... mesh-node1\_assoc2[ ... ] ... 
... meshref->node1\_assoc2[ ... ] ...
```

## Addition 2

`... \_associ[ source [cond] ]`

### Description

Initial mesh association of a mesh path. Each mesh path has an initial mesh association specified after its root node. For `\_associ[ ... ]`, all mesh associations [`\_assoc[ ... ]`](abenmesh_path_assoc.md) suitable for the root node can be specified, namely:

- [Forward associations](abenmesh_path_assoc.md) with a [mesh association](../abap-declarations/abaptypes_mesh_association.md) of the mesh type that has the root node as the start node.

- [Inverse mesh associations](abenmesh_path_assoc.md) with a [mesh association](../abap-declarations/abaptypes_mesh_association.md) of the mesh type that has the root node as the target node.

The syntax used to specify the line of the entry node in the square brackets of the mesh association [`\_assoc[ ... ]`](abenmesh_path_assoc.md) is

\[ source \[[`cond`](abenmesh_path_assoc_cond.md)\] \]

A structure `source` of the line type of the root node must be specified as the source of the mesh association. This is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). When the mesh path is evaluated, the content of `source` is used as the starting point of the mesh association. Here, the evaluation of the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used and any additional conditions [`cond`](abenmesh_path_assoc_cond.md) produces a description of a set of lines of the follow-on node as a [result](abenmesh_path_result_init_assoc.md).

### Hint

A structure specified as `source` does not need to occur as a line in the root node. It is a good idea to use a [table expression](../../abap-glossary/abentable_expression_glosry.md) that read a line from the root node. A [mesh path expression](abenmesh_path_expression.md) can, however, also be specified to nest meshes.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Forward associations and an inverse mesh association as initial mesh associations of mesh paths. Table expressions that read a line from the root node are used as sources of the mesh associations.

``` abap
TYPES: 
  BEGIN OF MESH mesh, 
    node1 TYPE itab1 ASSOCIATION _assoc2 TO node2 ON ... 
    node2 TYPE itab2, 
  END OF MESH mesh. 
 
DATA(mesh) = VALUE mesh( ... ). 
 
... mesh-node1\_assoc2[ mesh-node1[ ... ] ]. 
... mesh-node1\_assoc2~node2[ mesh-node1[ ... ] ]. 
... mesh-node2\^_assoc2~node1[ mesh-node2[ ... ] ].
```

## Addition 3

`... \_assoc1[ [cond] ]\_assoc2[ [cond] ] ...`

### Description

Path extension of a mesh path. Any number of further mesh associations can be chained after the initial mesh association. All mesh associations [`\_assoc`](abenmesh_path_assoc.md) can be specified for `\_assoc1`, `\_assoc2`, ... that match the entry node in question, namely:

- [Forward associations](abenmesh_path_assoc.md) with a [mesh association](../abap-declarations/abaptypes_mesh_association.md) of the mesh type that has the entry node as the start node.

- [Inverse mesh associations](abenmesh_path_assoc.md) with a [mesh association](../abap-declarations/abaptypes_mesh_association.md) of the mesh type that has the entry node as the target node.

The syntax used to specify the line of the start node in the square brackets of the mesh association [`\_assoc[ ... ]`](abenmesh_path_assoc.md) is

\[ \[[`cond`](abenmesh_path_assoc_cond.md)\] \]

When the mesh path is evaluated, the result of the preceding mesh association, that is, the description of a set of lines in the entry node, is used as the starting point of the mesh association. Here, the evaluation of the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used and any additional conditions [`cond`](abenmesh_path_assoc_cond.md) produces a description of a set of lines of the follow-on node as a [result](abenmesh_path_result_chaining.md). If no further conditions are specified, the square brackets are empty.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Path extension of the initial mesh association. The follow-on node of the initial mesh association is `node2` and this node is the entry node of the path extension. The result of the entire mesh path is a description of lines in `node3`. The result of the initial mesh association, whose starting point is defined by a table expression, is the implicit source of the path extension.

``` abap
TYPES: 
  BEGIN OF MESH mesh, 
    node1 TYPE itab1 ASSOCIATION _assoc2 TO node2 ON ... 
    node2 TYPE itab2 ASSOCIATION _assoc3 TO node3 ON ... 
    node3 TYPE itab3, 
  END OF MESH mesh. 
 
DATA(mesh) = VALUE mesh( ). 
 
... mesh-node1\_assoc2[ mesh-node1[ ... ] ]\_assoc3[  ] ...
```
