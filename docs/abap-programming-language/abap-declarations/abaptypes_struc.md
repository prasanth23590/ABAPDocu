---
title: "TYPES, BEGIN OF struct_type"
source_file: abaptypes_struc.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, BEGIN OF struct_type

## Syntax

``` abap
TYPES BEGIN OF struc_type.   
  ...   
  TYPES comp ...   
  TYPES comp TYPE struc_type BOXED.   
  INCLUDE TYPE|STRUCTURE ...   
  TYPES comp REF TO struc_type.   
  ...   
TYPES END OF struc_type.  
```

[`BOXED`](abaptypes_boxed.md) · [`INCLUDE TYPE|STRUCTURE ...`](abapinclude_type.md) · [`TYPES comp REF TO struc_type.`](abaprecursive_struc_references.md)

## Description

Definition of a structured type `struc_type`. This is introduced using a `TYPES` statement with the addition `BEGIN OF` and must end with a `TYPES` statement with the addition `END OF`.

The following can be included between these `TYPES` statements:

- Any `TYPES` statements, particularly other completed structure definitions.

- The definition of [static boxes](../../abap-glossary/abenstatic_box_glosry.md) using [`BOXED`](abaptypes_boxed.md).

- The statements [`INCLUDE TYPE`](abapinclude_type.md) and [`INCLUDE STRUCTURE`](abapinclude_type.md) for including components from other structures.

Structured types must not be created without at least one component.

The `TYPES` statements within the statements `BEGIN OF` and `END OF` define the components of the structured type `struc_type`. If a component is a structured type or if a new structured type is defined within a structure using `BEGIN OF` and `END OF`, substructures are created. A structure with substructures is a nested structure.

A component of `struc_type` can be declared with reference to `struc_type` itself. If the name `struc_type` is specified after `TYPE` in the declaration of a component, a search is performed for the next type with this name in a higher [visibility section](../abap-data-types-and-data-objects/abenlifetime_and_visibility.md), and used if found. If there is no other global type of this name, a syntax error occurs.

If a component is created as a [table type](abaptypes_itab.md), it must not be generic. The name of a component cannot be the reserved name of the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line`.

The statement `INCLUDE` defines components of the structured type `struc_type` by copying the components of a differently structured type or an existing structure at the same level.

The components of a structured type are addressed using the name `struc_type` and the name of the component, separated by the structure component selector (`-`).

## Hints

- The [value operator](../../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can be used to [construct](../abap-creating-objects-and-values/abenvalue_constructor_params_struc.md) the content of structures.

- A structure type is always fully specified. There is no generic structure type.

- The statements for defining a structure type are usually summarized in a [chained statement](../../abap-glossary/abenchained_statement_glosry.md) if possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example defines two structured types, `street_type` and `address_type`. `address_type` contains structured types as components. The definition of `zipcode_type` shows the access to substructures.

``` abap
TYPES: BEGIN OF street_type, 
         name TYPE c LENGTH 40, 
         no   TYPE c LENGTH 4, 
       END OF street_type. 
 
TYPES: BEGIN OF address_type, 
         name   TYPE c LENGTH 30, 
         street TYPE street_type, 
         BEGIN OF city, 
           zipcode TYPE n LENGTH 5, 
           name TYPE c LENGTH 40, 
         END OF city, 
       END OF address_type. 
 
TYPES zipcode_type TYPE address_type-city-zipcode.
```
