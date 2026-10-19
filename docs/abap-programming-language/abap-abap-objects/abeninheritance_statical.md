---
title: "ABAP Objects - Inheritance and Static Components"
source_file: abeninheritance_statical.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance and Static Components

[Static components](../../abap-glossary/abenstatic_component_glosry.md), like all components, exist only once in each inheritance tree, and can be used as of the declaring class:

- A subclass can access all non-private static components of its superclasses. The class in which the static component is declared is always addressed.

- From outside, the class component selector can be used to access all visible static components. Each class can be specified in which the component exists, that is, the declaring class and each subclass. Regardless of the class name used in the class component selector, however, the class in which the component is declared is always addressed.

The class in which the component is declared is always the class addressed, regardless of whether the static component is used internally or externally. This is important in the following cases:

- Calls of the [static constructors](../../abap-glossary/abenstatic_constructor_glosry.md).

  Static constructors are called the first time a class is addressed. If a static component is addressed using the class name of a subclass, but is declared in a superclass, only the static constructor of the superclass is called.

- Access to the [static attributes](../../abap-glossary/abenstatic_attribute_glosry.md)

  A subclass has access to the content of all non-private static attributes of all superclasses. Conversely, a superclass shares its public and protected static attributes with all subclasses. When inherited, static attributes are therefore not only usable in a single class but can also be used in the subtree of the inheritance tree that consists of all subclasses of the defining class. Changes to the values are visible in all involved classes, regardless of the class used to address an attribute.

- Registrations of [event handlers](../../abap-glossary/abenevent_handler_glosry.md).

  If an event handler is declared for a static event of a subclass inherited from a superclass, it can only react to this event if it is raised by a method of the subclass or one of its subclasses. If the event is raised in a static method of a superclass, it is not handled, even if the method is called in a subclass or if the name of the subclass is specified.

## Hint

A static attribute of a class can be declared as a private attribute to prevent it from being used by all subclasses.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of a static method of a superclass using the name of a subclass. Before the method is executed, the static constructor of the superclass is executed, but not the static constructor of the subclass. The method returns the value that is set in the superclass.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA     a1 TYPE string. 
    CLASS-METHODS: class_constructor, 
      m1 RETURNING VALUE(r1) LIKE a1. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD class_constructor. 
    a1 = 'c1'. 
  ENDMETHOD. 
  METHOD m1. 
    r1 = a1. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    CLASS-METHODS class_constructor. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD class_constructor. 
    a1 = 'c2'. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
 
    DATA v1 TYPE string. 
    v1 = c2=>m1( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example shows how a subclass is used to change a static attribute of a superclass, and how the change is visible in a subclass of a different path in the inheritance tree.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA a1 TYPE string. 
ENDCLASS. 
 
CLASS c11 DEFINITION INHERITING FROM c1. 
  ... 
ENDCLASS. 
 
CLASS c12 DEFINITION INHERITING FROM c1. 
  ... 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    c11=>a1 = 'Hello Sister'. 
    cl_demo_output=>display( c12=>a1 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Events in Inheritance](../abap-declarations/abenevent_inheritance_abexa.md)
