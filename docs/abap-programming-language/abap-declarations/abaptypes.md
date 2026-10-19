---
title: "TYPES"
source_file: abaptypes.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES

## Syntax Forms

**[Using Built-In Types](abaptypes_simple.md)**

``` abap
1. TYPES { {dtype[(len)] TYPE abap_type [DECIMALS dec]} 
        | {dtype TYPE abap_type [LENGTH len] [DECIMALS dec]}}.
```

**[Reference to Existing Types](abaptypes_referring.md)**

``` abap
2. TYPES dtype { {TYPE [LINE OF] type} 
              | {LIKE [LINE OF] dobj}  }. 
```

**[Reference Types](abaptypes_references.md)**

``` abap
3. TYPES ref_type { {TYPE REF TO type} 
                 | {LIKE REF TO dobj} }.
```

**[Structured Types](abaptypes_struc.md)**

``` abap
4. TYPES BEGIN OF struc_type. 
     ... 
     TYPES comp ... 
     TYPES comp TYPE struc_type BOXED. 
     INCLUDE {TYPE|STRUCTURE} ... 
     ... 
  TYPES END OF struc_type.
```

**[Enumerated Types](abaptypes_enum.md)**

``` abap
5. TYPES BEGIN OF ENUM enum_type 
                [STRUCTURE struc] 
                [BASE TYPE dtype]. 
    TYPES val1 [VALUE IS INITIAL]. 
    TYPES val2 [VALUE val]. 
    TYPES val3 [VALUE val]. 
    ... 
  TYPES END OF ENUM enum_type 
              [STRUCTURE struc]. 
```

**[Mesh Types](abaptypes_mesh.md)**

``` abap
6. TYPES BEGIN OF MESH mesh_type. 
     ... 
     TYPES node TYPE [REF TO] table_type associations 
     ... 
  TYPES END OF MESH mesh_type.
```

**[Table Types](abaptypes_itab.md)**

``` abap
7. TYPES table_type { {TYPE tabkind OF [REF TO] type} 
                   | {LIKE tabkind OF dobj} } 
                     [tabkeys][INITIAL SIZE n].
```

**[Ranges Table Types](abaptypes_ranges.md)**

``` abap
8. TYPES dtype {TYPE RANGE OF type}|{LIKE RANGE OF dobj} 
              [INITIAL SIZE n]. 
```

**[Indicators](abaptypes_indicators.md)**

``` abap
9. TYPES dtype TYPE struct WITH INDICATORS ind 
                         [TYPE type].
```

**[Structure with Client Column](abaptypes_client_specified.md)**

``` abap
10. TYPES dtype TYPE cds_entity CLIENT SPECIFIED clnt.
```

**[LOB Handle Structures](abaptypes_lob_handle.md)**

``` abap
11. TYPES dtype TYPE dbtab|view 
                   lob_handle_type FOR lob_handle_columns 
                  [lob_handle_type FOR lob_handle_columns 
                   ...                                   ].
```

**[BDEF Derived Types](../../abap-rap-business-objects/abap-for-rap-business-objects/abenrpm_derived_types.md)**

``` abap
12. TYPES dtype { {TYPE TABLE FOR} 
               | {TYPE STRUCTURE FOR} 
               | {TYPE REQUEST FOR} 
               | {TYPE RESPONSE FOR} } ...
```

[`associations`](abaptypes_mesh_association.md) · [`tabkind`](abaptypes_tabcat.md) · [`tabkind`](abaptypes_tabcat.md) · [`tabkeys`](abaptypes_keydef.md) · [`lob_handle_type`](abaptypes_lob_handle_type.md) · [`lob_handle_columns`](abaptypes_lob_handle_columns.md) · [`lob_handle_type`](abaptypes_lob_handle_type.md) · [`lob_handle_columns`](abaptypes_lob_handle_columns.md)

## Description

The statement `TYPES` defines a standalone data type. [Naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the names. The defined data type can be viewed within the current context from this position.

The syntax allows the definition of elementary data types, reference types, structured types, table types, and mesh types.

For the definition of a structured type `struc_type`, any type definitions of two `TYPES` statements are included with the additions `BEGIN OF` and `END OF`. A structured data type `struc_type` is then defined that contains the enclosed data types as components `struc_type-...`. Structure definitions can be nested. A mesh type is a special structure type whose components are tabular nodes for which mesh [associations](../../abap-glossary/abenmesh_association_glosry.md) can be defined.
