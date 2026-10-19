---
title: "ALIASES"
source_file: abapaliases.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Implementing or Including Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ALIASES

## Syntax

``` abap
ALIASES alias FOR intf~comp.  
```

## Description

In the declaration part of a class or interface, this statement declares an alias name `alias` for a component `comp` of the interface `intf`. The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `alias`. The interface `intf` must be implemented in the same class or included in the same interface. The alias name can be used anywhere, where it is visible, instead of `intf~comp`, to access the interface component `comp`.

An alias name is a component of the class and the interface. It is in the same namespace as the other components and is inherited by subclasses. In classes, an alias name can be declared in every [visibility section](../../abap-glossary/abenvisibility_section_glosry.md).

## Hints

- Within a context, such as a class declaration or method, only one name should be used to access components. The syntax check issues a warning if both the alias name and the full name `intf~meth` are used together.

- When implementing interface methods in the implementation part of classes using `METHOD` and when [re-defining](../../abap-glossary/abenredefinition_glosry.md) methods using `METHODS ... REDEFINITION`, the alias name can also be used.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the interfaces `i2`, `i3` and the class `c1`, aliases are declared for the methods of the included or implemented interfaces. In the implementation part of the class, the interface methods in the [`METHODS`](abapmethods.md) statements are implemented using the interface component selector. However, the aliases of the classes could also be used here.

``` abap
INTERFACE i1. 
  METHODS meth. 
ENDINTERFACE. 
 
INTERFACE i2. 
  INTERFACES i1. 
  ALIASES m1 FOR i1~meth. 
  METHODS meth. 
ENDINTERFACE. 
 
INTERFACE i3. 
  INTERFACES i2. 
  ALIASES: m1 FOR i2~m1, 
           m2 FOR i2~meth. 
  METHODS meth. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES i3. 
    ALIASES: m1 FOR i3~m1, 
             m2 FOR i3~m2, 
             m3 FOR i3~meth. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD i1~meth. 
    ... m2( ) ... 
  ENDMETHOD. 
  METHOD i2~meth. 
    ... m3( ) ... 
  ENDMETHOD. 
  METHOD i3~meth. 
    ... m1( ) .... 
  ENDMETHOD. 
ENDCLASS.
```
