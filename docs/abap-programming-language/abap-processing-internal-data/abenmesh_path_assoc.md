---
title: "Meshes - _assoc[...]"
source_file: abenmesh_path_assoc.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths > Meshes - mesh_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - \_assoc\[...\]

## Syntax

``` abap
... \_assoc[+|*][ ... ] 
  | \_assoc~node[+|*][ ... ] 
  | \^_assoc~node[+|*][ ... ] ...  
```

### Variant

[1. `... \_assoc`](abenmesh_path_assoc.md#variant-1)

[2. `... \_assoc~node`](abenmesh_path_assoc.md#variant-2)

[3. `... \^_assoc~node`](abenmesh_path_assoc.md#variant-3)

### Addition

[1. `... [ ... ]`](abenmesh_path_assoc.md#addition-1)

[2. `... +|*`](abenmesh_path_assoc.md#addition-2)

## Overview

### Description

Specifies a mesh association in a [mesh path](abenmesh_path.md). A mesh association specification is introduced using a backslash character, `\`, and is always located directly to the right of an entry node of the mesh path. A mesh association leads from its entry node to a follow-on node in the same mesh. A mesh association is either an initial mesh association [`\_associ[ ... ]`](abenmesh_path.md), for which the entry node of the [root node](abenmesh_path.md) specified explicitly is at the start of a mesh path, or a path extension [`\_assoc1[ ... ]`](abenmesh_path.md), [`\_assoc2[ ... ]`](abenmesh_path.md), ..., for which the entry node is the follow-on node of a preceding mesh association.

The syntax variants define whether the association is a forward association or an inverse mesh association. The addition in square brackets `[ ]` determines the table line of the entry node from which the mesh association originates at runtime. The optional additions `+` or `*` can be used to make reflexive mesh associations ([self-associations](../../abap-glossary/abenself_association_glosry.md)) transitive.

### Hint

In the [definition](../abap-declarations/abaptypes_mesh_association.md) of a mesh association, its nodes are known as start nodes and target nodes. In evaluations of mesh associations, however, they are known as entry nodes and follow-on nodes. In a forward association, the entry node is always a start node and the follow-on node is always a target node. In inverse mesh associations, the reverse applies.

## Variant 1

`... \_assoc`

## Variant 2

`... \_assoc~node`

### Description

Specifies a forward association. In a forward association, the entry node is a start node and the follow-on node is a target node of a mesh association [`_assoc`](../abap-declarations/abaptypes_mesh_association.md) of the mesh. Both variants have the same semantics. `_assoc` is used to specify the name of a mesh association defined for the entry node in the [mesh type](../abap-declarations/abaptypes_mesh.md). The follow-on node is the target node of this mesh association and can be specified as `node` after `~` in alternative 2.

### Hint

The follow-on node `node` can be specified explicitly for logging purposes on the consumer side. If the recommended naming convention with the prefix `to_` in front of the name of the target node is used for [mesh associations](../abap-declarations/abaptypes_mesh_association.md), however, it is redundant.

## Variant 3

`... \^_assoc~node`

### Description

Specifies an inverse mesh association. In an inverse mesh association, the entry node is a target node and the follow-on node is a start node of an association [`_assoc`](../abap-declarations/abaptypes_mesh_association.md) of the mesh. `_assoc` is used to specify the name of a mesh association that has the entry node as a target node in the [mesh type](../abap-declarations/abaptypes_mesh.md). The start node of the required mesh association must be specified explicitly as the follow-on node using `node` after `~`.

### Hints

- The follow-on node `node` must be specified since the entry node can be the target node of different mesh associations of an identically named mesh type.

- An inverse mesh association can also be specified for a reflexive mesh association ([self association](../../abap-glossary/abenself_association_glosry.md)) with the same start node and target node.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Forward associations and an inverse mesh association as initial mesh associations of mesh paths.

``` abap
TYPES: 
  BEGIN OF MESH mesh, 
    node1 TYPE REF TO itab1 ASSOCIATION _node2 TO node2 ON ... 
    node2 TYPE REF TO itab2, 
  END OF MESH mesh. 
 
DATA(mesh) = VALUE mesh( ... ). 
 
"Forward associations 
... mesh-node1\_node2[ ... ] ... 
... mesh-node1\_node2~node2[ ... ] ... 
 
"Inverse association 
... mesh-node2\^_node2~node1[ ... ] ...
```

## Addition 1

`... [ ... ]`

### Description

The square brackets are part of the syntax. The square brackets define the table line of the entry node from which the mesh association originates at runtime. This specification in square brackets depends on whether the association is an initial mesh association or a path extension and where the mesh path is used:

- \[ source \[[`cond`](abenmesh_path_assoc_cond.md)\] \]

  Specifies a structure `source` as a source in an initial mesh association [`\_associ[ ... ]`](abenmesh_path.md).

- \[ \[[`cond`](abenmesh_path_assoc_cond.md)\] \]

  Implicitly specifies the source in a path extension [`\_assoc1[ ... ]`](abenmesh_path.md), [`\_assoc2[ ... ]`](abenmesh_path.md). The source is the result of the preceding mesh association.

Depending on where the association is used, further conditions [`cond`](abenmesh_path_assoc_cond.md) can be specified. If no further conditions are specified, the square brackets of an initial mesh association contain only `source` and the square brackets of a path extension are empty.

### Executable Example

[Mesh Path Expressions](abenmesh_table_expressions_abexa.md)

## Addition 2

`... +|*`

### Description

An optional `+` or `*` can be specified after the name of the mesh association to make it transitive. To be used transitively, the mesh association [`_assoc`](../abap-declarations/abaptypes_mesh_association.md) must be reflexive and have the same start node and target node ([self-association](../../abap-glossary/abenself_association_glosry.md)). If the last mesh association in the mesh path is used transitively, it can only be used for single lines with [`LOOP`](abenmesh_loop.md) and [`FOR`](abenmesh_loop.md) or [`DELETE`](abenmesh_delete.md) and [`MODIFY`](abenmesh_delete.md)

If an mesh association is used transitively, it is evaluated more than once when the mesh path is used. First, the regular [result](abenmesh_path_result.md) of the mesh association is determined. Starting with this result, the mesh association is evaluated recursively until no new lines are found in the follow-on node. Here, the result of each evaluation is the starting point of the next recursion. The result set of the transitive mesh association is the union set of the individual recursions

The variants `+` and `*` differ as follows:

- If `+` is specified, the result set is only determined by the [results](abenmesh_path_result.md) of the mesh associations.

- If `*` is specified, the source of the mesh association is included in the result set. If the association is the initial mesh association, the line is determined from the specified source `source` using the primary table key and it cannot be empty. If no line is found, the result set is empty.

Each line of the follow-on node occurs only once in the result set, even if it was found more than once when the mesh path was evaluated.

### Hints

- Transitive mesh associations are useful for evaluating hierarchical structures within a mesh node.

- For a result set created with `+`, a line of an initial mesh association described using `source` does not need to exist in the internal table to ensure that this set is not empty. If `*` is used, however, this line must exist.

### Executable Example

[Reflexive Mesh Associations in Mesh Paths](abenmesh_for_reflex_sngl_abexa.md)
