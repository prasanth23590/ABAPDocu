---
title: "Recursive Structure References"
source_file: abaprecursive_struc_references.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, BEGIN OF struct_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Recursive Structure References

Recursive structure references are components of a structured type that represent data references to the same structure in which they are defined (self-recursive structure references).

They can be used in both local structures and global [DDIC structures](../../abap-glossary/abenddic_structure_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the definition of a structured type that includes a component referencing the same structure.

``` abap
TYPES: BEGIN OF struc_type, 
         num  TYPE i, 
         text TYPE string, 
         sref TYPE REF TO struc_type, 
       END OF struc_type.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Recursive structure references can reference superordinate structures.

``` abap
TYPES: BEGIN OF s_ty_1, 
         comp1 TYPE REF TO s_ty_1, 
         BEGIN OF s_ty_2, 
           comp1 TYPE REF TO s_ty_1, 
           comp2 TYPE REF TO s_ty_1-s_ty_2, 
           BEGIN OF s_ty_3, 
             comp1 TYPE REF TO s_ty_1, 
             comp2 TYPE REF TO s_ty_1-s_ty_2, 
             comp3 TYPE REF TO s_ty_1-s_ty_2-s_ty_3, 
           END OF s_ty_3, 
         END OF s_ty_2, 
       END OF s_ty_1.
```

## Hints

- Recursive structure references enable, for example, linked lists and trees that can be processed in a type-safe manner.

- Recursive references can only be specified in structured type definitions, not in structured data object declarations that use `DATA: BEGIN OF ...` with a component defined as `LIKE REF TO` and referencing the same structure. You can only declare a structured data object that includes recursive references using the structured type (`DATA struct TYPE struc_type.`).

## Executable Example

The class `CL_DEMO_RECURSIVE_STRUC_REF` demonstrates the use of self-recursive structure references. It includes methods for adding elements and reversing linked lists. Additionally, it incorporates another structure that contains a component of type `REF TO data`. The processing of the structures shows that the recursive structure reference can be managed in a type-safe manner, while the other structure must account for potential exceptions due to the generic type used.
