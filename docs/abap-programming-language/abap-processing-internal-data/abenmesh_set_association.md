---
title: "SET ASSOCIATION mesh_path"
source_file: abenmesh_set_association.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET ASSOCIATION mesh_path

## Syntax

``` abap
SET ASSOCIATION mesh_path { = wa    } 
                        | { LIKE wa } 
                        | { INITIAL }.  
```

[`mesh_path`](abenmesh_path.md)

### Addition

[1. `... = wa`](abenmesh_set_association.md#addition-1)

[2. `... LIKE wa`](abenmesh_set_association.md#addition-2)

[3. `... INITIAL`](abenmesh_set_association.md#addition-3)

## Overview

### Description

Sets mesh associations for a [`mesh_path`](abenmesh_path.md). The statement takes columns in the second last path node of the mesh path that are specified as `scomp` in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association starting with this node and sets these columns to values that are determined by the additions on the right side. The content of the last path node is ignored.

- If the mesh path only contains one [initial mesh association](abenmesh_path.md), the second last node is the root node of the path whose content is neither read nor changed. Instead, the columns of the structure specified by the `ON` condition are set. The structure is specified as the `source` in the square brackets of the mesh association. The square brackets must not contain any [additional conditions](abenmesh_path_assoc_cond.md).

- If the mesh path contains [path extensions](abenmesh_path.md), it is evaluated down to the second last node. The columns specified using the `ON` condition are changed in the lines of the second last path node, which are described in the [result](abenmesh_path_result_chaining.md). All mesh associations but the last one of the mesh path can contain additional conditions, which can be specified using [`USING KEY`](abenmesh_path_assoc_cond.md) and [`WHERE log_exp`](abenmesh_path_assoc_cond.md). The square brackets `[ ]` for the mesh association of the last path extension must be empty.

The last mesh association of the mesh path is used only to determine the modifying components using their `ON` condition, therefore the last association cannot contain any [additional conditions](abenmesh_path_assoc_cond.md).

### Hints

- Using the statement `SET ASSOCIATION`, mesh association-relevant components can be set in structures and mesh nodes, without needing to know the component names. These structures can be used, for example, to build mesh nodes.

- Using the statement `SET ASSOCIATION`, change operations can be performed that provide additional options to those offered by the statements [`INSERT`](abenmesh_insert.md) and [`MODIFY`](abenmesh_insert.md).

- A mesh path that only contains an initial mesh association can also be used to modify mesh nodes by using a field symbol or data reference in `source` to reference a line in a mesh node.

## Addition 1

`... = wa`

### Description

Assigns columns of a work area `wa`. The work area `wa` must be a structure with the same line type as the last path node.

The content of the components of `wa` that are listed in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the last mesh association of the mesh path as `tcomp` is assigned to the assigned components `scomp` of the structure `source` or to the assigned columns of the lines found in the second last path node.

### Hint

In terms of semantics, key values in an instance of an entry node of a mesh association are set as they are in an instance of a follow-on node.

## Addition 2

`... LIKE wa`

### Description

Assigns columns of a work area `wa`. The work area `wa` must be a structure with the same line type as the second last path node.

The content of the components of `wa` is specified in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the last mesh association of the mesh path as `scomp`. This content is assigned to the identically named components in the structure `source` or to the identically named columns of the lines found in the second last path node.

### Hint

In terms of semantics, key values in an instance of an entry node of a mesh association are set as they are in a different instance of the same node.

## Addition 3

`... INITIAL`

### Description

Assigns initial values

All components of `source` or all columns of the lines found in the second last path node that are specified in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the last mesh association of the mesh path as `scomp` are assigned their type-dependent initial value.

### Hint

In terms of semantics, key values in an instance of an entry node of a mesh association are initialized.
