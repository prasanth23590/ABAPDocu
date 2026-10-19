---
title: "Meshes - Mesh Path Expressions"
source_file: abenmesh_path_expression.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Using Mesh Paths"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - Mesh Path Expressions

## Syntax

``` abap
... mesh_path ...  
```

[`mesh_path`](abenmesh_path.md)

## Description

Specifies a mesh path [`mesh_path`](abenmesh_path.md) as a standalone mesh path expression at an operand position. The result of a mesh path expression is a line from the last path node of the mesh path described by the [result](abenmesh_path_result.md) of the mesh path and has the corresponding line type.

In the square brackets [`[ ... ]`](abenmesh_path_assoc.md) of each mesh association, an additional condition can be specified using [`col1 = ... col2 = ...`](abenmesh_path_assoc_cond.md). If a path node contains multiple lines that fit the description, the first line found is read.

A mesh path expression is a special type of [table expression](abentable_expressions.md) and can be used in the same way as a table expression:

- Possible operand positions are all read and write positions listed for [table expressions](abentable_expressions.md). In a write position, key fields of primary or secondary table keys of the last path node must not be overwritten.

- [`VALUE`](abentable_exp_result.md) and [`REF`](abentable_exp_result.md) can be used to control how the result is passed as in regular table expressions.

- A [chaining](abentable_exp_chaining.md) with the structure component selector (`-`) can be used to access a component of the read line.

If the follow-on node does not contain any lines that meet the condition in the square brackets [`[ ... ]`](abenmesh_path_assoc.md), the response is the same as in regular table expressions. In other words, the exception `CX_SY_ITAB_LINE_NOT_FOUND` is raised, except when used in the statement [`ASSIGN`](abapassign_mem_area_writable_exp.md), in the predicate function [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md), or in the table function [`line_index`](abenline_index_function.md).

## Hint

Since the lines of a mesh node cannot have tabular components, a mesh path expression cannot have any [chainings](abentable_exp_chaining.md) to other table expressions.

## Executable Example

[Mesh Path Expressions](abenmesh_table_expressions_abexa.md)
