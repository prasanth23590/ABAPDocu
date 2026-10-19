---
title: "Meshes - Result of a Path Extension"
source_file: abenmesh_path_result_chaining.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths > Meshes - Result of Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Result of a Path Extension

A path extension with the [syntax](abenmesh_path.md)

...[`\_assoc1`](abenmesh_path_assoc.md)\[ \[[`cond`](abenmesh_path_assoc_cond.md)\] \][`\_assoc2`](abenmesh_path_assoc.md)\[ \[[`cond`](abenmesh_path_assoc_cond.md)\] \] ...

describes a set of lines in the last path node.

**Result when Used in a Loop**

Each mesh association specified in a mesh path with path extension describes a set of lines in its follow-on node that is used as a starting point for its follow-on nodes of the lines and meets the following conditions:

- All lines meet the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used in relation to the set of lines described in the preceding mesh association. Every `tcomp` column listed in the `ON` condition has the same content as in the `scomp` column of the entry node assigned in the `ON` condition in a line of its result.

- Depending on the mesh path [usage](abenmesh_path_usage.md), the set of lines can be further restricted by using additional [`cond`](abenmesh_path_assoc_cond.md) conditions.

In the set of lines described by a path extension, each line occurs only once, even if it was found more than once in the evaluation of the mesh path.

**Result when Used in a Table Expression**

Each mesh association specified in a mesh path with path extension selects a single line in its follow-on node (or fails with one exception). This line is used as the starting point for the follow-on node in accordance with the conditions described above.

## Hint

The set of lines described by the result can be either one line or multiple lines.

## Executable Example

[Results of Mesh Paths](abenmesh_path_result_abexas.md)
