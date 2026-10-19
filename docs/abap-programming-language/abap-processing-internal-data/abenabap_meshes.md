---
title: "Meshes"
source_file: abenabap_meshes.html
section: "ABAP Programming Language > ABAP - Processing Internal Data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Meshes

Meshes are instances of mesh types defined as follows:

``` abap
TYPES BEGIN OF MESH
  ... 
  TYPES snode ... ASSOCIATION _assoc
                  TO tnode ON tcomp1 = scomp1 [AND ...]. 
  ... 
TYPES END OF MESH
```

[`TYPES BEGIN OF MESH`](../abap-declarations/abaptypes_mesh.md) · [`ASSOCIATION _assoc`](../abap-declarations/abaptypes_mesh_association.md) · [`TYPES END OF MESH`](../abap-declarations/abaptypes_mesh.md)

These are special [structures](../../abap-glossary/abenstructure_glosry.md) whose components, which are referred to as nodes, are either structured internal tables or reference variables that refer to such internal tables.

The addition [`ASSOCIATION`](../abap-declarations/abaptypes_mesh_association.md) can be used to declare [mesh associations](../../abap-glossary/abenmesh_association_glosry.md) defined using `ON` conditions between start nodes and target nodes of the mesh. These semantic relationships between the mesh nodes can be evaluated in mesh paths. The mesh paths can be used in expressions and processing statements for meshes.

- [Mesh paths](abenmesh_pathes.md)

- [Results of mesh paths](abenmesh_path_usage.md)

## Hints

- A mesh node is addressed in the same way as a regular structure component; by using the structure component selector (`-`) or the object component selector (`->`). Mesh associations are evaluated in [mesh paths](abenmesh_path.md). If no path is specified, a mesh node is handled in the same way as a regular structure component. The same applies to field symbols or reference variables that point to mesh nodes. The statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) also handles a mesh like a regular structure.

- In the simplest case, the relationships implemented between mesh nodes using mesh associations can be compared to [foreign key dependencies](../../abap-glossary/abenforeign_key_dependency_glosry.md). Here, the start node of a mesh association is the check table and the target node is the foreign key table. The use of mesh paths makes it easier to evaluate these relationships, without the need to program the relevant selections.
