---
title: "DELETE mesh_path"
source_file: abenmesh_delete.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE mesh_path

## Syntax

``` abap
DELETE { TABLE mesh_path table_key } 
     | { mesh_path }.  
```

[`mesh_path`](abenmesh_path.md) · [`table_key`](abapdelete_itab_key.md) · [`mesh_path`](abenmesh_path.md)

### Variant

[1. `DELETE TABLE mesh_path table_key.`](abenmesh_delete.md#variant-1)

[2. `DELETE mesh_path.`](abenmesh_delete.md#variant-2)

## Overview

### Description

Deletes one or more lines from the last path node of a mesh path [`mesh_path`](abenmesh_path.md).

### Hint

It should be noted that the addition `TABLE` is highly significant for directly specified internal tables, as in [`DELETE`](abapdelete_itab.md), and distinguishes different variants of statements from each other.

## Variant 1

`DELETE TABLE mesh_path table_key.`

### Description

Deletes exactly one line from the follow-on node of an [initial mesh association](abenmesh_path.md). In this variant, no path extensions can be specified, and the square brackets of the initial mesh association cannot contain any [additional conditions](abenmesh_path_assoc_cond.md). The line to be modified is determined using the table key:

- If the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used covers all key fields of the table key it uses, the line to be deleted is determined using the [result](abenmesh_path_result_init_assoc.md) of the mesh path. Here, only those fields of the `ON` condition are respected that are also key fields.

- If the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association used does not cover the key fields of the table key it uses, the missing key fields must be specified in the addition [`table_key`](abapdelete_itab_key.md) and these are combined with the [result](abenmesh_path_result_init_assoc.md) of the mesh path. The same can be specified for [`table_key`](abapdelete_itab_key.md) as in the statement [`DELETE`](abapdelete_itab.md) [`TABLE itab`](abapdelete_itab_line.md) with a directly specified internal table:

  - [`WITH TABLE KEY`](abapdelete_itab_key.md) must be used to specify all key fields not covered by the `ON` condition. No key fields can be specified that are already covered by the `ON` condition. Furthermore, all fields of the follow-on node used in the `ON` condition must exist in the table key used by the mesh association.

  - Only those components are taken from a work area specified using [`FROM wa`](abapdelete_itab_key.md) that match the non-covered key fields. All other components are ignored. The work area `wa` must be compatible with the line type of the last path node.

    If a table key is specified in [`table_key`](abapdelete_itab_key.md) using `keyname COMPONENTS` or `USING keyname`, this key overrides any [`USING KEY`](../abap-declarations/abaptypes_mesh_association.md) additions specified in the definition of the mesh association. The line is deleted with respect to this table key and its key fields must be completely covered.

The line is deleted in accordance with the rules of [`DELETE`](abapdelete_itab.md). If the follow-on node contains multiple lines that match the specified key, the first line found is deleted. If the line to be deleted is not found, nothing is deleted.

The return code `sy-subrc` is set in the same way as in the corresponding statement [`DELETE itab`](abapdelete_itab.md).

### Hints

- If the `ON` condition covers all key fields, the addition [`WITH TABLE KEY`](abapdelete_itab_key.md) cannot be specified. The addition [`FROM wa`](abapdelete_itab_key.md) can be specified, but is ignored.

- If no explicit table key is specified in the definition of the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) and in the statement `DELETE TABLE mesh_path`, the line is deleted with respect to the primary table key.

- Columns of the follow-on node that are listed in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) but are not part of the table key used are either forbidden or ignored in this variant. This means that the line to be deleted cannot be determined beyond the bounds of the table key.

### Executable Example

[Deleting Single Lines in Mesh Paths](abenmesh_delete_table_abexa.md)

## Variant 2

`DELETE mesh_path.`

### Description

Deletes multiple lines from the last path node of a mesh path [`mesh_path`](abenmesh_path.md). All lines from the last path node described by the [result](abenmesh_path_result.md) of the mesh path are deleted. An additional condition can be specified in the square brackets [`[ ... ]`](abenmesh_path_assoc.md) of each mesh association of the mesh path using the additions [`USING KEY`](abenmesh_path_assoc_cond.md) and [`WHERE log_exp`](abenmesh_path_assoc_cond.md).

### Executable Example

[Deleting Multiple Lines in Mesh Paths](abenmesh_delete_abexa.md)
