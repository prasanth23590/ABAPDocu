---
title: "Meshes - Result of Mesh Paths"
source_file: abenmesh_path_result.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Result of Mesh Paths

The mesh path result is a description of a set of lines in the last node path node of the expression. The result is used in statements and expressions for [using mesh paths](abenmesh_path_usage.md) (with one exception); either for navigating in the last path node or for manipulating the last path node. The exception is statement [`SET ASSOCIATION`](abenmesh_set_association.md), which works with the second last path node.

- [Result of the initial mesh association](abenmesh_path_result_init_assoc.md)

- [Result of a path extension](abenmesh_path_result_chaining.md)

## Hints

- At runtime, the mesh path result expresses the relationship defined by mesh associations between the entry node and follow-on node. The result is managed internally by the ABAP runtime framework and evaluated in line with [Using Mesh Paths](abenmesh_path_usage.md).

- Loops implemented with [`LOOP AT`](abenmesh_loop.md) or [`FOR`](abenmesh_for.md) are suitable for performing reads on all the lines described by the mesh path result.
