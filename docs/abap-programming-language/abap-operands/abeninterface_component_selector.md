---
title: "Interface Component Selector"
source_file: abeninterface_component_selector.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions > Notations for Single Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Interface Component Selector

A component `comp` of an interface is accessed using the following name:

`intf~comp`

The symbol `~` is the interface component selector. The name `intf` of an interface must be to the left of the interface component selector. The name `comp` of the component must be to the right of the interface component selector.

The name `intf~comp` identifies the components of interfaces in classes, or component interfaces in linked interfaces.

## Hint

An interface contains each component exactly once, regardless of its combination of component interfaces. All the interface components are at the same hierarchical level. The name of an interface component is uniquely defined by `intf~comp`, where `intf` is always the interface in which the component is declared. A direct chaining of interface names `intf1~...~intfn~comp` is not possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of interfaces and access to their components.

``` abap
INTERFACE i1. 
  TYPES t1 TYPE string. 
ENDINTERFACE. 
 
INTERFACE i2. 
  INTERFACES i1. 
  METHODS m2 IMPORTING p1 TYPE i1~t1. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES i2. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD i2~m2. 
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
 
    DATA oref TYPE REF TO c1. 
    FINAL(p1) = `...`. 
    oref->i2~m2( p1 = p1 ). 
 
    ... 
 
  ENDMETHOD. 
ENDCLASS.
```
