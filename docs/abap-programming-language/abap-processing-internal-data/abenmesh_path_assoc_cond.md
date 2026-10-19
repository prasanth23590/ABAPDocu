---
title: "Meshes - [... cond]"
source_file: abenmesh_path_assoc_cond.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Meshes > Meshes - Mesh Paths > Meshes - mesh_path > Meshes - _assoc[...]"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes - \[... cond\]

## Syntax

``` abap
... { col1 = val1 col2 = val2 ... } 
  | { [USING KEY key] [WHERE log_exp] } ...  
```

### Variant

[1. `... col1 = val1 col2 = val2 ...`](abenmesh_path_assoc_cond.md#variant-1)

[2. `... [USING KEY key] [WHERE log_exp]`](abenmesh_path_assoc_cond.md#variant-2)

## Overview

### Description

Specifies an additional condition in the square brackets, [`[ ... ]`](abenmesh_path_assoc.md), of a mesh association in a [mesh path](abenmesh_path.md). In an initial mesh association, a condition of this type can be specified alongside the structure `source`. In the case of a path extension, the square brackets contain an additional condition or are empty.

## Variant 1

`... col1 = val1 col2 = val2 ...`

### Description

Additional condition when using mesh paths in [mesh path expressions](abenmesh_path_expression.md). `col1`, `col2`, ... can be used to specify columns of the follow-on node of the mesh association that do not already occur in their [`ON` condition](../abap-declarations/abaptypes_mesh_association.md). Each of these columns is assigned a value `val1`, `val2`, ... Their content must match this value to meet the condition. `val1`, `val2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). The additional condition is joined with the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) to create a full condition. In the case of an initial mesh association, the comparison values of the `ON` condition are specified explicitly as a structure `source`. In the case of a path extension, the comparison values are taken from the result set of the preceding mesh association.

### Executable Example

[Mesh Path Expressions](abenmesh_table_expressions_abexa.md)

## Variant 2

`... [USING KEY key] [WHERE log_exp]`

### Description

Additional condition when using mesh paths in the statements and expressions:

- [`LOOP AT mesh_path ...`](abenmesh_loop.md)

- [`FOR ... IN mesh_path ...`](abenmesh_for.md)

- [`INSERT ... INTO TABLE mesh_path ...`](abenmesh_insert.md)

- [`MODIFY mesh_path.`](abenmesh_modify.md)

- [`DELETE mesh_path.`](abenmesh_delete.md)

- [`SET ASSOCIATION mesh_path ...`](abenmesh_set_association.md)

Only one `WHERE` condition, `USING KEY` with a `WHERE` condition, or only `USING KEY` can be specified. `USING KEY` must be specified in front of a `WHERE` condition. The syntax and semantics of the `WHERE` condition are the same as when [`WHERE log_exp`](abaploop_at_itab_cond.md) is specified statically for the statement [`LOOP AT itab`](abaploop_at_itab.md), but the comparison is made for columns of the follow-on node.

`USING KEY` can be used to specify a [table key](../abap-data-types-and-data-objects/abenitab_key.md) `key` of the follow-on node. The name or alias name of the table key must be specified directly.

- If only one `WHERE` condition is specified, any comparisons for columns of the follow-on node are possible in this condition. These columns can also already be specified in the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association. The `WHERE` condition works like an additional condition joined with the evaluation of the `ON` condition using `AND`.

- The specification `USING KEY` defines the table key used to access the follow-on node. It overrides any other `USING KEY` specifications in the [definition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association.

  - If `USING KEY` is specified in front of a `WHERE` condition, the equality comparisons of the `WHERE` condition joined using `AND` are also joined using `AND` with the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) to form a condition. Optimized key access must be possible here: There can be no duplicate columns in the joined condition and, in the case of a sorted table key, it must cover a left initial part. In the case of a hash key, it must cover all key fields of the follow-on node. Further parts of the `WHERE` condition, such as comparisons joined using `OR` or comparisons for properties other than equality, are not required for optimized key access and work in the same way as only specifying a `WHERE` condition as an additional condition.

  - If `USING KEY` is specified without a `WHERE` condition, the [`ON` condition](../abap-declarations/abaptypes_mesh_association.md) of the mesh association must meet the prerequisites for optimized access for the table key.

### Hint

`USING KEY` can be specified without a `WHERE` condition, for example, to use a table key with a different order of key fields as in a table key specified in a mesh association.
