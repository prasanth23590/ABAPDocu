---
title: "ANY STRUCTURE"
source_file: abapany_structure.html
section: "ABAP Programming Language > ABAP - Declarations > Typing > typing Addition > typing Addition, generic_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ANY STRUCTURE

## Syntax

``` abap
... TYPE ANY STRUCTURE.  
```

## Description

The syntax `TYPE ANY STRUCTURE` without additions creates fully generic structured types, similar to the `ANY TABLE` type used for generic internal tables.

Generic structured types can be used for defining [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) and field symbols. The following criteria apply to typing formal parameters with generic structured types:

- Any optional parameter requires the specification of a default value.

- Importing and changing parameters can be specified with fully generic structured types when they are mandatory or defined as default by specifying a default structure.

- Exporting parameters cannot be defined with generic structured types since their passing is inherently optional.

- Returning parameters cannot be defined with generic structured types because the formal parameter must be completely typed.

- In the case of AMDP database procedures, parameters cannot be defined with generic structured types.

Any structure can be assigned to field symbols and formal parameters typed with the fully generic structured type.

## Hints

- Concrete data objects cannot be declared with generic structured types because there is no implicit type completion. This differs from other generic ABAP types, such as the generic type `c`, which automatically completes to type `c LENGTH 1`.

- Casting generic types to character-like types (such as type `c`) is not supported because the compiler handles generic structures as deep structures.

- In ABAP SQL, generic structures are not allowed as target areas.

- Generic structures cannot be used for table parameters or as global interfaces for function modules.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a field symbol typed with `ANY STRUCTURE`, which is assigned a variety of structures.

``` abap
    FIELD-SYMBOLS <gs> TYPE ANY STRUCTURE. 
 
    TYPES: BEGIN OF ts_flat, 
             comp1 TYPE c LENGTH 3, 
             comp2 TYPE i, 
             comp3 TYPE n LENGTH 5, 
           END OF ts_flat, 
           BEGIN OF ts_nested, 
             comp1 TYPE c LENGTH 10, 
             comp2 TYPE ts_flat, 
           END OF ts_nested, 
           BEGIN OF ts_deep, 
             comp1 TYPE string, 
             comp2 TYPE REF TO i, 
             comp3 TYPE ts_nested, 
             comp4 TYPE string_table, 
           END OF ts_deep. 
 
    TYPES BEGIN OF ts_include. 
    INCLUDE TYPE ts_flat AS a. 
    INCLUDE TYPE ts_nested AS b RENAMING WITH SUFFIX _n. 
    TYPES END OF ts_include. 
 
    DATA: struc_flat    TYPE ts_flat, 
          struc_nested  TYPE ts_nested, 
          struc_deep    TYPE ts_deep, 
          struc_include TYPE ts_include. 
 
    ASSIGN struc_flat TO <gs>. 
    ASSIGN struc_nested TO <gs>. 
    ASSIGN struc_deep TO <gs>. 
    ASSIGN struc_include TO <gs>.
```
