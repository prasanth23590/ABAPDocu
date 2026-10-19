---
title: "Assignments Between Object Reference Variables"
source_file: abenconversion_references_objects.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Reference Variables > Assignment Rules for Reference Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Assignments Between Object Reference Variables

Object reference variables are either class references or interface reference variables.

- [Upcast in Object References](abenconversion_references_objects.md#upcast-in-object-references)

- [Downcast in Object References](abenconversion_references_objects.md#downcast-in-object-references)

## Upcast in Object References

An [upcast](../../abap-glossary/abenup_cast_glosry.md) in object references is possible in the following cases:

- If both static types are classes, the class of the target variable must be the same class or a superclass of the source variable.

- If both static types are interfaces, the interface of the target variable must be the same interface or a component interface of the source variable.

- If the static type of the target variable is an interface and the static type of the source variable is a class, the class of the source variable must implement the interface of the target variable.

- If the static type of the target variable is a class and the static type of the source variable is an interface, the class of the target variable must be the generic type or the root class `object`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `iref = NEW class( )` is an upcast, because it is followed by an interface reference variable that points to an object of a class.

``` abap
INTERFACE intf. 
ENDINTERFACE. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA iref TYPE REF TO intf. 
    iref = NEW cls( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Downcast in Object References

For all cases not specified under the upcast, assignments can only be programmed using a downcast.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of interfaces and classes, creation of an object in the subclass, and access to the components of the object. In the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md), an upcast occurs implicitly from `c2` to `iref`. The interface reference `iref` can only be used to access the components declared in the interface `i2`. Method `m1` of the object cannot be called using `iref`. Once the object reference has been assigned to the class reference `cref` using a downcast, `m1` can be accessed dynamically but not statically.

``` abap
INTERFACE i1. 
  DATA a1 TYPE string. 
ENDINTERFACE. 
 
INTERFACE i2. 
  INTERFACES i1. 
  ALIASES a1 FOR i1~a1. 
  DATA a2 TYPE string. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES i2. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    METHODS m1. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m1. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: iref TYPE REF TO i2, 
          cref TYPE REF TO c1. 
 
    ... 
 
    CREATE OBJECT iref TYPE c2. 
 
    iref->a1 = `...`. 
    iref->a2 = `...`. 
 
    ... 
 
    IF iref IS INSTANCE OF c1. 
      cref ?= iref. 
      TRY. 
          CALL METHOD cref->('M1'). 
        CATCH cx_sy_dyn_call_illegal_method. 
          ... 
      ENDTRY. 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```
