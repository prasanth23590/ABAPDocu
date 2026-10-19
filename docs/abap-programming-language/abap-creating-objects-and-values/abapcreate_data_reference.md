---
title: "CREATE DATA, REF TO"
source_file: abapcreate_data_reference.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE DATA, REF TO

## Syntax

``` abap
CREATE DATA dref     
                 TYPE REF TO {type|(name)}.  
```

## Description

The addition `TYPE REF TO` is used by the statement `CREATE DATA` to create a reference variable. The static type of the reference variable can be specified either directly as `type` or dynamically in `name`.

When `type` is specified, the same rules apply as to the definition of reference types using the statement [`TYPES`](../abap-declarations/abaptypes.md). For data reference variables, either the generic type `data` or a completely specified data type can be specified. For object reference variables, either a class or an interface can be specified.

For `name`, a character-like field can be specified that must contain the name of a class, an interface, or a data type when the statement is executed. The name of the reference type in `name` can also be specified as an [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md).

## Hint

Object types in `name` can also be specified dynamically in lowercase letters.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an anonymous data object as reference variable of the static type of a class. The dereferenced reference variable can be used to create an object of the class and to access its components.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE string VALUE `Oh my ...`. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    TYPES reftype TYPE REF TO cls. 
    DATA dref TYPE REF TO reftype. 
    CREATE DATA dref TYPE REF TO cls. 
    CREATE OBJECT dref->*. 
    out->write( dref->*->attr ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Creating Reference Variables](abencreate_reference_abexa.md)
