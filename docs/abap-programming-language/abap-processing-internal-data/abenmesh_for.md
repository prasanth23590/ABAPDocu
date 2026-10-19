---
title: "FOR ... IN mesh_path"
source_file: abenmesh_for.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR ... IN mesh_path

## Syntax

``` abap
... FOR wa|<fs> IN mesh_path [let_exp] ...  
```

[`FOR wa|<fs> IN`](abenfor_in_itab.md) · [`mesh_path`](abenmesh_path.md) · [`let_exp`](../abap-declarations/abaplet.md)

## Description

Evaluates all lines described by a [`mesh_path`](abenmesh_path.md) using a `FOR` expression of a constructor expression. The syntax and meaning are the same as for [`FOR` expressions](abenfor_in_itab.md) for lines of internal tables, however a mesh path is specified after `FOR ... IN`, instead of a directly specified internal table. Groupings and `FOR` expressions for groups, the addition `INDEX INTO`, and conditions outside of the mesh path cannot be specified here. A `FOR` expression with a mesh path can be used like a `FOR` expression with an internal table for [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md) and [table reductions](../../abap-glossary/abentable_reduction_glosry.md).

When specifying the mesh paths, the same applies as to mesh paths in the statement [`LOOP AT`](abenmesh_loop.md). The `FOR` expression works in the same way as the corresponding `LOOP` loop on the last path node of the mesh path. In particular, additional conditions can be specified in the square brackets [`[ ... ]`](abenmesh_path_assoc.md) of a mesh association of the mesh path using the additions [`USING KEY`](abenmesh_path_assoc_cond.md) and [`WHERE log_exp`](abenmesh_path_assoc_cond.md).

## Hint

In the constructor expression `NEW`, `VALUE`, or `REDUCE`, `FOR` expressions with mesh paths and `FOR` expressions with directly specified internal tables can occur together.

## Executable Example

[`FOR` Expressions for Mesh Paths](abenmesh_for_abexa.md)
