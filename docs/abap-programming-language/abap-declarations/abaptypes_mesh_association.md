---
title: "TYPES, association"
source_file: abaptypes_mesh_association.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, BEGIN OF MESH mesh_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, association

## Syntax

``` abap
... ASSOCIATION _assoc TO node ON tcomp1 = scomp1 
                             [AND tcomp2 = scomp2 
                             [AND ... ]] 
                             [USING KEY key_name] ...  
```

### Addition

[1. `... ON tcomp1 = scomp1 [AND tcomp2 = scomp2 [AND ... ]]`](abaptypes_mesh_association.html#addition-1)

[2. `... USING KEY key_name`](abaptypes_mesh_association.md#addition-2)

## Overview

### Description

Definition of a mesh association named `_assoc` for a mesh node of a mesh type. The addition `ASSOCIATION` to `TYPES` can only be used in the definition of a node of a mesh type between [`TYPES BEGIN OF MESH`](abaptypes_mesh.md) and [`TYPES END OF MESH`](abaptypes_mesh.md). The mesh node for which a mesh association is defined is its start node and the mesh node `node` specified after `TO` is the target node. Any node in the current mesh can be specified as the target node `node`, including the start node itself. A mesh association with the same start and target node is a [self-association](../../abap-glossary/abenself_association_glosry.md) or reflexive association.

The name of a mesh association can be up to 30 characters long and can only consist of the letters A-Z, the digits 0-9, and the underscore *\_* character, and cannot start with a digit.

### Hints

- The mesh associations defined for a mesh node are evaluated in [expressions and statements](../abap-processing-internal-data/abenmesh_path_usage.md) for [meshes](../abap-processing-internal-data/abenabap_meshes.md) in [mesh paths](../abap-processing-internal-data/abenmesh_pathes.md).

- A target node does not have to be defined before the start node to be visible to it. However, the Code Completion function of the editor only works properly if this is the case.

- The prefix `_` is recommended as the naming convention for mesh associations. The name that follows this prefix should contain the target node name in non-reflexive mesh associations. This convention makes it easier to read the [mesh path](../abap-processing-internal-data/abenmesh_path.md).

## Addition 1

`... ON tcomp1 = scomp1 [AND tcomp2 = scomp2 [AND ... ]]`

### Description

For each mesh association, a condition must be specified after `ON` that consists of at least one [comparison](../../abap-glossary/abencomparison_glosry.md) for equality. Further comparisons for equality can be added using `AND`. The left operand `tcomp` of each comparison must be a directly specified column of the target node and the right operand `scomp` must be a directly specified column of the start node that must be compatible with the column of the target node.

A mesh association creates a relationship between the start node and target node where all the rows of the target node that meet the condition are assigned to a line of the start node.

The mesh associations are type-only properties and also affect the compatibility of mesh types. Mesh associations are evaluated in [mesh paths](../abap-processing-internal-data/abenmesh_pathes.md) in expressions and in statements for meshes.

### Hints

- In the `ON` condition, the target node components are on the left and the start node components are on the right, like in other statements and expressions for internal tables, where the columns of the table to be searched are always listed on the left.

- As a rule of thumb, the target node components that are listed on the left in an `ON` condition should be key fields of the table key used for the condition, in order to achieve the most efficient access.

## Addition 2

`... USING KEY key_name`

### Description

The addition `USING KEY` can be used for the `ON` condition of a mesh association to specify a table key of the target node that is used in expressions and statements to evaluate [meshes](../abap-processing-internal-data/abenabap_meshes.md) for accessing the mesh node:

- A [secondary key](../../abap-glossary/abensecondary_key_glosry.md) using its name

- The primary key using its predefined name `primary_key` or an alias. If the primary key is specified, the target node must be a sorted table or a hashed table.

The name of the table key must be specified directly, that is, it cannot be specified dynamically in a data object. If the table key is specified explicitly, the `ON` condition must be defined to allow optimal key access.

- If a sorted key or the primary key of a sorted table is specified, the conditions specified after `ON` must cover a left initial part of the key fields in the target table.

- If a secondary hash key or a primary key of a hashed table is specified, the conditions specified after `ON` must cover all key fields in the target table.

Without the addition `USING KEY`, the primary key is used to access the mesh node and that access is not always optimized.

### Hint

The table key specified in the definition of the `ON` condition can be overridden when the mesh association is used in a [mesh path](../abap-processing-internal-data/abenmesh_path.md) by specifying `USING KEY` in an [additional condition](../abap-processing-internal-data/abenmesh_path_assoc_cond.md). In this case, the `ON` condition and the additional condition are combined into a condition that must meet the above prerequisites.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a mesh type. Some of the keys of the internal tables used are secondary keys that are used with `USING` in the definitions of the mesh associations.

``` abap
TYPES: 
  t_scarr    TYPE HASHED TABLE OF scarr 
             WITH UNIQUE KEY carrid, 
  t_spfli    TYPE HASHED TABLE OF spfli 
             WITH UNIQUE KEY carrid connid 
             WITH NON-UNIQUE SORTED KEY carrid 
                             COMPONENTS carrid, 
  t_sflight  TYPE HASHED TABLE OF sflight 
             WITH UNIQUE KEY carrid connid fldate 
             WITH NON-UNIQUE SORTED KEY carrid_connid 
                             COMPONENTS carrid connid, 
  t_sairport TYPE HASHED TABLE OF sairport 
             WITH UNIQUE KEY id, 
  BEGIN OF MESH t_flights, 
    scarr TYPE t_scarr 
      ASSOCIATION _spfli TO spfli 
               ON carrid = carrid USING KEY carrid, 
    spfli TYPE t_spfli 
      ASSOCIATION _sflight TO sflight 
               ON carrid = carrid AND 
                  connid = connid USING KEY carrid_connid 
      ASSOCIATION _sairport TO sairport 
               ON id = airpfrom, 
    sflight TYPE t_sflight, 
    sairport TYPE t_sairport, 
  END OF MESH t_flights.
```
