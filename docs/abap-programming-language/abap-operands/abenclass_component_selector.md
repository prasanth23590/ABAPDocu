---
title: "Class Component Selector"
source_file: abenclass_component_selector.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Class Component Selector

A [static component](../../abap-glossary/abenstatic_component_glosry.md) `comp` of a class is accessed using the following name:

`class=>comp`

No instance of the class has to be created. The symbol `=>` is the class component selector. The name `class` of a class must be to the left of the class component selector. The name `comp` of the component must be to the right of the class component selector.

The class component selector can also be used to access the data types and constants of an interface:

`intf=>type`, `intf=>const`

The name `intf` of an interface must be to the left of the class component sector. The name `type` of a data type defined using `TYPES` or a constant `const` defined using `CONSTANTS` must be to the right of the object component selector.

## Hint

It is also possible to access the static components of a class using the object component selector if an instance of the class was created.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a class `factory` and access to its static attribute`oref`.

``` abap
CLASS factory DEFINITION CREATE PRIVATE. 
  PUBLIC SECTION. 
    CLASS-DATA oref TYPE REF TO factory. 
    CLASS-METHODS class_constructor. 
    METHODS do_something. 
ENDCLASS. 
 
CLASS factory IMPLEMENTATION. 
  METHOD class_constructor. 
    CREATE OBJECT oref. 
  ENDMETHOD. 
  METHOD do_something. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    ... 
 
    factory=>oref->do_something( ). 
 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
