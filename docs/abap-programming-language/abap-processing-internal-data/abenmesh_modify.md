---
title: "MODIFY mesh_path"
source_file: abenmesh_modify.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY mesh_path

## Syntax

``` abap
MODIFY { TABLE mesh_path [USING KEY keyname] 
                         FROM wa 
                         [TRANSPORTING comp1 comp2 ...] 
                         result } 
     | { mesh_path FROM wa 
                   [TRANSPORTING comp1 comp2 ...] }.  
```

[`mesh_path`](abenmesh_path.md) · [`keyname`](abenkeyname.md) · [`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md) · [`result`](abapmodify_itab_result.md) · [`mesh_path`](abenmesh_path.md) · [`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md)

### Variant

[1. `MODIFY TABLE mesh_path FROM wa ...`](abenmesh_modify.md#variant-1)

[2. `MODIFY mesh_path FROM wa ...`](abenmesh_modify.md#variant-2)

### Addition

[`... TRANSPORTING comp1 comp2 ...`](abenmesh_modify.md#addition)

## Overview

### Description

Modifies one or more lines in the last path node of a mesh path [`mesh_path`](abenmesh_path.md). In the line or lines described by the mesh path, the following columns are assigned the corresponding values from the work area `wa`:

- If the optional addition `TRANSPORTING` is not specified, all columns are modified

  - that are not in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used,

  - that are no part of the primary key of the last path node, if the table is a sorted table or a hashed table.

- If the optional addition `TRANSPORTING` is specified, the columns listed after it are modified

`wa` expects a structure that is compatible with the line type of the last path node. No key fields of primary or secondary table keys in the last path node can be overwritten. The return code `sy-subrc` is set in the same way as in the corresponding statement [`MODIFY itab`](abapmodify_itab.md).

### Hint

It should be noted that the addition `TABLE` is highly significant for directly specified internal tables, as in [`MODIFY`](abapmodify_itab.md), and distinguishes different variants of statements from each other.

## Variant 1

`MODIFY TABLE mesh_path FROM wa ...`

### Description

Modifies exactly one line in the follow-on node of an [initial mesh association](abenmesh_path.md). In this variant, no path extensions can be specified, and the square brackets of the initial mesh association cannot contain any [additional conditions](abenmesh_path_assoc_cond.md). The line to be modified is determined using the table key used:

- If the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used covers all key fields of the table key it uses, the line to be modified is determined using the [result](abenmesh_path_result_init_assoc.md) of the mesh path. However, only those fields of the `ON` condition are respected that are also key fields.

- If the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used does not cover the key fields of the table key it uses, the missing key fields are taken from the associated components of the work area `wa`.

The line is modified in accordance with the rules of [`MODIFY`](abapmodify_itab.md). If the follow-on node contains multiple lines that match the specified key, the first line found is modified. If the line to be modified is not found, nothing is modified. The key used can be specified using the addition `USING KEY`, just as in the statement [`MODIFY`](abapmodify_itab_single.md) with directly specified internal table. [`result`](abapmodify_itab_result.md) can be used to specify the output behavior.

### Hint

Columns of the follow-on node that are listed in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) but are not part of the table key used are always ignored in this variant. This means that the line to be modified cannot be determined beyond the bounds of the table key.

### Executable Example

[Changing Single Lines in Mesh Paths](abenmesh_modify_table_abexa.md)

## Variant 2

`MODIFY mesh_path FROM wa ...`

### Description

Modifies multiple lines in the last path node of a mesh path [`mesh_path`](abenmesh_path.md). All lines in the last path node that are described by the [result](abenmesh_path_result.md) of the mesh path are modified. An additional condition can be specified in the square brackets [`[ ... ]`](abenmesh_path_assoc.md) of each mesh association of the mesh path using the additions [`USING KEY`](abenmesh_path_assoc_cond.md) and [`WHERE log_exp`](abenmesh_path_assoc_cond.md). In the last mesh association, the addition `USING KEY` cannot be specified if it is specified after `FROM wa`.

### Executable Example

[Changing Multiple Lines in Mesh Paths](abenmesh_modify_abexa.md)

## Addition

`... TRANSPORTING comp1 comp2 ...`

### Description

The same applies to the addition `TRANSPORTING` as to the statement [`MODIFY`](abapmodify_itab_single.md) with directly specified internal table, with the restriction that no columns can be specified that are part of the primary key of the last path node if the table is a sorted table or hashed table.

### Hint

The `TRANSPORTING` addition can also be used to modify columns that are specified in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used.
