---
title: "INSERT mesh_path"
source_file: abenmesh_insert.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT mesh_path

## Syntax

``` abap
INSERT line_spec INTO TABLE mesh_path result.  
```

[`line_spec`](abapinsert_itab_linespec.md) · [`mesh_path`](abenmesh_path.md) · [`result`](abapinsert_itab_result.md)

## Description

Inserts lines in the last path node of a mesh path [`mesh_path`](abenmesh_path.md). As in [inserts](abapinsert_itab.md) into a directly specified table using [`INTO TABLE`](abapinsert_itab_position.md), the position of the lines to be inserted is determined using the primary table key. The behavior for duplicate lines encountered with respect to unique table keys is also the same. When specifying the inserted lines using [`line_spec`](abapinsert_itab_linespec.md), the same applies when inserting lines into directly specified internal tables and they must be compatible with the line type of the last path node.

A set of lines with the line type of the last path node is instantiated internally from the specification in `line_spec` and the [result](abenmesh_path_result.md) of the mesh path. This set is inserted into the last path node in accordance with the rules of [`INSERT`](abapinsert_itab.md):

- For each line in [`line_spec`](abapinsert_itab_linespec.md) or for each line in a table to be inserted, the same number of lines is created as described by the [result](abenmesh_path_result.md). If the mesh path contains only the initial mesh associations, one line is created. In the case of path extensions, multiple lines can be created.

- In the new lines, the columns in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the last mesh association of the mesh path are filled as follows:

  - If the mesh path contains only an initial mesh association, each of these columns is filled with the current comparison value from `source`.

  - If the mesh path contains path extensions, each of these columns is filled with the value described by the result of the preceding mesh association.

    The remaining components have the value of the lines specified in [`line_spec`](abapinsert_itab_linespec.md).

The following applies when specifying the mesh associations:

- If the mesh path contains only an initial mesh association, the square brackets cannot contain an [additional condition](abenmesh_path_assoc_cond.md).

- If the mesh path contains path extensions, all mesh associations can contain additional conditions using the additions [`USING KEY`](abenmesh_path_assoc_cond.md) and [`WHERE log_exp`](abenmesh_path_assoc_cond.md). The square brackets `[ ]` for the mesh association of the last path extension must be empty.

The number of lines to be inserted is the number of lines specified in `lin_spec` multiplied by the number of lines described in [result](abenmesh_path_result.md). If, due to an additional `WHERE` condition, the result set is empty, no lines are inserted.

[`result`](abapinsert_itab_result.md) can be used to specify the output behavior when exactly one line is inserted, as in [`INSERT`](abapinsert_itab.md). Since more than one line can be inserted when path extensions are used, the addition `result` can only be specified in the following cases:

- If the variant `LINES OF` is not used in [`line_spec`](abapinsert_itab_linespec.md).

- The mesh path contains only the initial mesh association.

## System Fields

The return code in system field `sy-subrc` is set in the same way as in the corresponding statement [`INSERT`](abapinsert_itab.md).

## Hints

- When `INITIAL LINE` is used to specify an initial line in [`line_spec`](abapinsert_itab_linespec.md), only those components remain initial that are not specified in the `ON` condition.

- The square brackets of the mesh association of the last path extension are empty, since it needs only to indicate the mesh node in which the lines are inserted.

## Executable Examples

- [Insertions in Mesh Paths](abenmesh_insert_abexa.md)

- [Table Builds Using Mesh Paths](abenmesh_build_abexa.md)
