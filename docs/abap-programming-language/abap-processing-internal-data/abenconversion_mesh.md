---
title: "Conversion Rules for Meshes"
source_file: abenconversion_mesh.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Rules for Meshes

[Meshes](../../abap-glossary/abenmesh_glosry.md) are not converted. Meshes can only be assigned to meshes and meshes can be assigned to each other only if they are fully [compatible](../abap-data-types-and-data-objects/abencompatibility.md), that is:

- Their node structure must be identical, including the names of the nodes.

- The mesh associations of each node are completely identical, which means that

  - They must have the same name.

  - The same `ON` conditions must be specified.

  - The same table key must be used.

Assignments between meshes and data objects that cannot be assigned to meshes lead to a syntax error or the runtime error `OBJECTS_MOVE_NOT_SUPPORTED`.

## Hint

[`MOVE-CORRESPONDING`](abapmove-corresponding.md) can also be used to assign incompatible meshes or structures and meshes to each other.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See [Comparing Meshes](../abap-program-flow-logic/abenlogexp_rules_operands_mesh.md)
