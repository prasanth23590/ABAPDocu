---
title: "Meshes - Result of the Initial Mesh Association"
source_file: abenmesh_path_result_init_assoc.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths > Meshes - Result of Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Result of the Initial Mesh Association

An initial mesh association with the [syntax](abenmesh_path.md)

...rnode[`\_associ`](abenmesh_path_assoc.md)\[ source \[[`cond`](abenmesh_path_assoc_cond.md)\] \] ...

describes a set of lines in the follow-on node of the used mesh association that meets the following conditions:

- All lines meet the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the used mesh association with respect to the specified structure `source`. Every `tcomp` column specified in the `ON` condition has the same content as in the `scomp` column of the root node in the `source` structure that is assigned to the `ON` condition.

- Depending on the mesh path [usage](abenmesh_path_usage.md), the set of lines can be further restricted by using additional [`cond`](abenmesh_path_assoc_cond.md) conditions.

## Hint

The set of lines described by the result can be either one line or multiple lines.

## Executable Examples

[Results of Mesh Paths](abenmesh_path_result_abexas.md)
