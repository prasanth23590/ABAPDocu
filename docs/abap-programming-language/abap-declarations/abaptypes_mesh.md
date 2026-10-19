---
title: "TYPES, BEGIN OF MESH mesh_type"
source_file: abaptypes_mesh.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, BEGIN OF MESH mesh_type

## Syntax

``` abap
TYPES BEGIN OF MESH mesh_type.   
  ...   
  TYPES node { TYPE {[REF TO] table_type}|ref_type } 
           | { LIKE {[REF TO] itab      }|dref     } 
                [association1], 
                [association2], 
                ...   
  ...   
TYPES END OF MESH mesh_type.  
```

[`association1`](abaptypes_mesh_association.md) · [`association2`](abaptypes_mesh_association.md)

## Description

Definition of a [mesh type](../../abap-glossary/abenmesh_type_glosry.md) for a [mesh](../abap-processing-internal-data/abenabap_meshes.md). A mesh type is a special structure type. The components of the structure type are referred to as mesh nodes and are subject to the following restrictions:

- The type of a mesh node must be a non-generic [table type](../../abap-glossary/abentable_type_glosry.md) or a [reference type](../../abap-glossary/abenreference_type_glosry.md) with the static type of a non-generic internal table. The node type can be defined as follows:

  - Using the addition `TYPE`, specifying a table type [`table_type`](abaptypes_itab.md) with or without `REF TO`, or by specifying such a reference type [`ref_type`](abaptypes_references.md) directly.

  - Using the addition `LIKE`, specifying an internal table [`itab`](abapdata_itab.md) with or without `REF TO`, or by specifying such a reference variable [`dref`](abapdata_references.md) directly.

- The [line type](../../abap-glossary/abenrow_type_glosry.md) of a mesh node must be structured and cannot contain internal tables or reference variables as components. Elementary data types and [substructures](../../abap-glossary/abensubstructure_glosry.md) are allowed as components. Substructures must meet the same prerequisite.

A regular structure type can be enhanced by defining one or more [mesh associations](../../abap-glossary/abenmesh_association_glosry.md) [`association`](abaptypes_mesh_association.md) for each mesh node. Each association connects two mesh nodes using a condition. The relationships between the tabular nodes of a mesh type defined using mesh associations are evaluated in the special [expressions and statements](../abap-processing-internal-data/abenmesh_path_usage.md) used to process [meshes](../abap-processing-internal-data/abenabap_meshes.md) in [mesh paths](../abap-processing-internal-data/abenmesh_pathes.md).

## Hints

- Meshes must be fully [compatible](../abap-data-types-and-data-objects/abencompatibility.md) for assignments, comparisons, and parameter passing. Meshes are compatible if their structures are compatible, the node names match, and the mesh associations match in names, `ON` conditions, and the table key used.

- Using the structure component selector (`-`), mesh nodes can be addressed and used as the components of the corresponding structure. If field symbols or reference variables point to mesh nodes, they are also handled like regular structure components. In particular, the statement [`MOVE-CORRESPONDING`](../abap-processing-internal-data/abapmove-corresponding.md) can also be used between incompatible meshes and between meshes and structures.

- A mesh type is always fully defined. Generic mesh types are not possible.

- Reference types as components can be particularly useful when meshes are injected into existing programs in which suitable internal tables already exist.

- The statements for defining a mesh type are usually summarized in a [chained statement](../../abap-glossary/abenchained_statement_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a mesh type with internal tables for the flight data model.

``` abap
TYPES: 
  t_scarr    TYPE HASHED TABLE OF scarr 
             WITH UNIQUE KEY carrid, 
  t_spfli    TYPE HASHED TABLE OF spfli 
             WITH UNIQUE KEY carrid connid, 
  t_sflight  TYPE HASHED TABLE OF sflight 
             WITH UNIQUE KEY carrid connid fldate, 
  t_sairport TYPE HASHED TABLE OF sairport 
             WITH UNIQUE KEY id, 
  BEGIN OF MESH t_flights, 
    scarr TYPE t_scarr 
      ASSOCIATION _spfli TO spfli 
               ON carrid = carrid, 
    spfli TYPE t_spfli 
      ASSOCIATION _sflight TO sflight 
               ON carrid = carrid AND 
                  connid = connid 
      ASSOCIATION _sairport TO sairport 
               ON id = airpfrom, 
    sflight  TYPE t_sflight, 
    sairport TYPE t_sairport, 
  END OF MESH t_flights.
```
