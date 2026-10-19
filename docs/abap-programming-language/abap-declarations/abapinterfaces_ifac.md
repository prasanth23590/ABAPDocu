---
title: "INTERFACES, composition"
source_file: abapinterfaces_ifac.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Implementing or Including Interfaces > INTERFACES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACES, composition

## Syntax

``` abap
INTERFACES intf.  
```

## Description

In the declaration of an interface, the statement `INTERFACES` includes the interface `intf` in the declared interface. Additions cannot be specified. As a result, the interface `intf` becomes a component interface of a composite interface.

An interface can be composed of any number of different component interfaces. All component interfaces are equal and on one level. If a component interface itself is a composite, that is, it contains its own component interfaces, the nesting hierarchy is irrelevant for the composition of the interface. It is relevant, however, for accessing the interface components.

To access the component `comp` of a component interface `intf` within a composite interface, the expression `intf~comp` can be used with the interface component selector `(~)`. It is not possible to use the interface component selector multiple times in a name (`intf1~intf2~comp`). In a composite interface, it is possible to use the interface component selector to access only those interface components of the component interface that are included in this interface using the statement `INTERFACES`. Since all nested interfaces are at the same level, however, this is sufficient to access the interface components of all component interfaces using the name of their interface.

## Hints

- Each interface and its components appear only once in a composite interface. Even an interface that is seemingly implemented more than once in an interface, because it is an interface component of one or more other interfaces, really exists only once.

- Since there are no separate namespaces for global and local interfaces, it must be ensured that combinations of local interfaces do not result in combinations of global and local interfaces with identical names, because they cannot be equal and on the same level in their implementation.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows how the statement `INTERFACES` can be used to compose and implement interfaces. Class `c1` implements the composite interfaces `i2` and `i3`. Although `i1` is a component interface of `i2` and `i3`, it exists only once in class `c1`. A reference variable `iref1` of the static type `i1` creates an object class `c1` and calls the method `i1~m1`, which is implemented there.

``` abap
INTERFACE i1. 
  METHODS m1. 
ENDINTERFACE. 
 
INTERFACE i2. 
  INTERFACES i1. 
  METHODS m2. 
ENDINTERFACE. 
 
INTERFACE i3. 
  INTERFACES i1. 
  METHODS m3. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES: i2, i3. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD i1~m1. 
    ... 
  ENDMETHOD. 
  METHOD i2~m2. 
    ... 
  ENDMETHOD. 
  METHOD i3~m3. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA iref1 TYPE REF TO i1. 
    CREATE OBJECT iref1 TYPE c1. 
    iref1->m1( ). 
  ENDMETHOD. 
ENDCLASS.
```
