---
title: "LOOP AT mesh_path"
source_file: abenmesh_loop.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT mesh_path

## Syntax

``` abap
LOOP AT mesh_path result. 
  ... 
ENDLOOP.  
```

[`mesh_path`](abenmesh_path.md) · [`result`](abaploop_at_itab_result.md)

## Description

Reads all lines described by the [results](abenmesh_path_result.md) of a mesh path [`mesh_path`](abenmesh_path.md) in a loop. Essentially, the loop works like the statement [`LOOP AT itab`](abaploop_at_itab.md) across a directly specified table and accesses the lines of the last path node described by the mesh path instead. The output behavior [`result`](abaploop_at_itab_result.md) is specified in exactly the same way as in `LOOP AT itab` and must match the line type of the last path node. The system fields are set in the same way as in the corresponding statement `LOOP AT itab`, where `sy-tabix` depends on the table key used.

An additional condition can be specified in the square brackets [`[ ... ]`](abenmesh_path_assoc.md) of each mesh association using the additions [`USING KEY`](abenmesh_path_assoc_cond.md) and [`WHERE log_exp`](abenmesh_path_assoc_cond.md).

The order in which the lines of the last path node are read depends on the order in which the lines were found when the mesh path was evaluated. Here, an iteration is performed across every follow-on node in the mesh path, in accordance with the table key used.

If only the initial mesh association is specified, the same rules apply when changing the last path node in the loop as when using `LOOP AT itab`. If a path extension is specified, the following additional restrictions apply:

- No line can be deleted from the last path node.

- No line can be inserted into the last path node, unless a hash key is used.

- No component of the table key used can be changed.

The entire internal table must never be replaced or deleted in the loop. Mesh nodes that are evaluated when path extensions are used before the last path node, however, can be modified as required.

## Hints

- A loop across a mesh path can be understood as a nesting of loops [`LOOP AT itab`](abaploop_at_itab.md) across the matching follow-on nodes, whose [`WHERE` conditions](abaploop_at_itab_cond.md) are constructed from `ON` conditions and the explicitly specified additional conditions. The evaluation itself, however, does not take place in nested `LOOP` statements and multiple iterations across a single table line never take place.

- If [path extensions](abenmesh_path_result_chaining.md) are used, any lines found more than once in mesh path evaluations are iterated only once.

- Tables located in front of the last path node in path extensions can be modified in any way in the loop, since they are evaluated only once before the loop is executed across the last path node.

## Executable Example

[Loops Across Mesh Paths](abenmesh_loops_abexa.md)
