---
title: "CREATE OBJECT oref"
source_file: abapcreate_object_implicit.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE OBJECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE OBJECT oref

## Syntax

``` abap
CREATE OBJECT oref [parameter_list].  
```

[`parameter_list`](abapcreate_object_parameters.md)

## Description

If the addition `TYPE` is not specified, the object reference variable `oref` must be a class reference variable. An instance of the class is created that is the static type of the object reference variable. The static type of the class reference variable must not be an [abstract](../../abap-glossary/abenabstract_glosry.md) class, and in particular not the root class `object`.

## Hint

If the character `#` is used in an operand position with the operand type of a class reference variable, the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abenconstructor_expression_new.md) works like the statement `CREATE DATA dref`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an instance of a class `cls` by implicitly referring to the static type of the reference variables.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE string VALUE 'Object'. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA oref TYPE REF TO cls. 
    CREATE OBJECT oref. 
    out->write( oref->attr ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
