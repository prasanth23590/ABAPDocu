---
title: "DATA, BOXED"
source_file: abapdata_boxed.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, BOXED

## Syntax

``` abap
DATA struc TYPE struc_type BOXED.  
```

## Description

This statement defines a structured attribute of a class or an interface as a [static box](../abap-data-types-and-data-objects/abenstatic_boxes.md). It can only be in the declaration section of a class or an interface and only at the highest level.

`struc_type` expects a structured data type. This can be a program-local structured type, a visible structured type of a global class or of a global interface, or a structure from the ABAP Dictionary, and can also contain static boxes.

Static boxes support [initial value sharing](../../abap-glossary/abeninitial_value_sharing_glosry.md). Here, the structure is not saved in the superordinate context itself. Instead, an internal reference that points to the actual structure is stored instead of the component. This makes a static box a [deep](../../abap-glossary/abendeep_glosry.md) component.

## Hints

- A structure with a static box is a [deep structure](../../abap-glossary/abendeep_structure_glosry.md) and the corresponding restrictions apply.

- The addition `BOXED` defines the static box in relation to its context (structure or class). A data type declared using a direct `TYPE` reference or `LIKE` reference to a static box inherits its data type but is not a static box itself.

- When a static box is included in one structure from another structure using the statement [`INCLUDE TYPE|STRUCTURE`](abapinclude_type.md), its property as a static box is inherited.

- The addition `BOXED` can also be used in the statement [`TYPES`](abaptypes_boxed.md) to declare a substructure of a nested structured data type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following section shows the allowed use of the addition `BOXED` with the statement `[CLASS-]DATA`. In a class, a static structure `struc1` and a structured instance attribute `struc2` are declared as static boxes.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    TYPES: BEGIN OF t_struc, 
             comp1 TYPE c LENGTH 100, 
             comp2 TYPE n LENGTH 100, 
           END OF t_struc. 
  PRIVATE SECTION. 
    CLASS-DATA struc1 TYPE t_struc BOXED. 
    DATA       struc2 TYPE t100    BOXED. 
ENDCLASS.
```
