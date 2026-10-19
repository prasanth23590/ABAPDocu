---
title: "CLASS, IMPLEMENTATION"
source_file: abapclass_implementation.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, IMPLEMENTATION

## Syntax

``` abap
CLASS class IMPLEMENTATION.   
  ...   
  METHOD ...   
    ...   
  ENDMETHOD.   
  ...   
ENDCLASS.  
```

## Description

In the statement block ` CLASS class IMPLEMENTATION - ENDCLASS`, the following methods of a class `class` must be implemented, in any order:

- All [concrete](../../abap-glossary/abenconcrete_glosry.md) methods declared using [`METHODS`](abapmethods.md) or [`CLASS-METHODS`](abapclass-methods.md) in the declaration part of the class.

- All concrete methods of interfaces listed using the statement [`INTERFACES`](abapinterfaces.md) in the declaration part of the class.

- All methods inherited from superclasses that are listed using the statement [`METHODS ... REDEFINITION`](abapmethods_redefinition.md) in the declaration part of the class

The implementation of each method corresponds to a processing block [`METHOD - ENDMETHOD`](../abap-program-structure/abapmethod.md). No statements are allowed in the implementation part outside of method implementations. In a method implementation, all components can be accessed in an instance method, and all static components of the class can be accessed in a static method implementation. No component selector is necessary to address the components of personal classes. Within the implementation of each instance method, there is an implicitly created, local reference variable named `me` available at runtime, which points to the current instance of the method.

When implementing methods declared in an interface bound by the class using [`INTERFACES`](abapinterfaces.md) `intf`, the name of the method in `METHOD` must have either `intf~` in front of it or use an alias name declared using [`ALIASES`](abapaliases.md). The interface method must be declared in the interface. Otherwise, a syntax error occurs when local interfaces are used. If a global interface is specified using `intf~`, only a syntax warning occurs. In this way, the classes remain usable even after subsequent removal of the methods from the global interface, provided they have not used the methods themselves.

## Hints

- A class that does not have to implement any methods because of its declaration part either has an empty implementation part or none at all.

- Abstract methods in abstract classes cannot be implemented in the implementation part.

- The implementation part of a class can only be specified in the context described under [`CLASS`](abapclass.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, three methods of the class `c2` must be implemented. The method `m1` in `c1` is abstract and must not be implemented there.

``` abap
INTERFACE i1. 
  METHODS m1. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION ABSTRACT. 
  PROTECTED SECTION. 
    METHODS m1 ABSTRACT. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    INTERFACES i1. 
    METHODS m2. 
  PROTECTED SECTION. 
    METHODS m1 REDEFINITION. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m1. 
    ... 
  ENDMETHOD. 
  METHOD m2. 
    ... 
  ENDMETHOD. 
  METHOD i1~m1. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
