---
title: "METHODS, REDEFINITION"
source_file: abapmethods_redefinition.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, REDEFINITION

## Syntax

``` abap
METHODS meth [FINAL] REDEFINITION.  
```

[`FINAL`](abapmethods_abstract_final.md)

### Addition

[`... FINAL`](abapmethods_redefinition.md#addition)

## Overview

### Description

This statement is possible only in subclasses and redefines an inherited instance method `meth`. It has the effect that the method `meth` must be reimplemented in the implementation part of the subclass. The new implementation in the current class hides the implementation of the superclass. The redefined method accesses the [private](../../abap-glossary/abenprivate_glosry.md) components of the redefined class and not any private components of the same name in the superclass. In the redefined method, the implementation of the direct superclass can be called using [`super->meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_super.md). The redefinition is valid for the subclasses of the redefined class until the method is redefined again.

With the exception of the [instance constructor](abapmethods_constructor.md), any non-final instance method declared in the [public](../../abap-glossary/abenpublic_glosry.md) or [protected](../../abap-glossary/abenprotected_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a superclass of the current class can be specified for `meth`. In particular, `meth` can be an abstract method of an abstract superclass. The [redefinition](../../abap-glossary/abenredefinition_glosry.md) must take place in the same visibility section as the method declaration. The interface and the category of the method (a [general](abapmethods_general.md) or [functional](abapmethods_functional.md) [instance method](../../abap-glossary/abeninstance_method_glosry.md) or [event handler](abapmethods_event_handler.md)) are not changed in a redefinition. Private methods in superclasses cannot be redefined.

### Hints

- Every object reference that points to an object of a subclass, independent of its static type, addresses the redefined methods. This applies in particular to the [self-reference](../../abap-glossary/abenself_reference_glosry.md) `me->`.

- When an [instance constructor](../../abap-glossary/abeninstance_constructor_glosry.md) of a superclass is executed during the creation of an object, the method implementations of the superclass are always called and not the redefined methods of the subclass. Specifying the self-reference `me->` has no effect at this time.

- In the redefinition of a method of an interface, an alias name of the class defined using [`ALIASES`](abapaliases.md) can be specified for `meth`.

- The explicit implementation can be omitted when redefining an optional interface method declared using [`DEFAULT`](abapmethods_default.md). Instead, the default behavior defined using `DEFAULT` applies in calls from the current subclass. However, this is not recommended. The default behavior is often not as expected, particularly if an explicit implementation already exists in a preceding superclass.

## Addition

`... FINAL`

A method can be redefined repeatedly along a path in the inheritance tree until the addition [`FINAL`](abapmethods_abstract_final.md) is used in the redefinition. The method is then final as of the current class and can no longer be redefined in its subclasses.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the method `m1` of superclass `c1` is redefined in subclass `c2`, where the original implementation is called using `super->m1`. Both methods use the private attribute `a1` of the respective class. When called using the reference variable `oref`, which has the static type `c1` and the dynamic type `c2`, the redefined method is executed.

``` abap
CLASS output DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA out TYPE REF TO if_demo_output. 
    CLASS-METHODS class_constructor. 
ENDCLASS. 
 
CLASS output IMPLEMENTATION. 
  METHOD class_constructor. 
    out = cl_demo_output=>new( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    METHODS m1 IMPORTING p1 TYPE string. 
  PRIVATE SECTION. 
    DATA a1 TYPE string VALUE `c1: `. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    METHODS m1 REDEFINITION. 
  PRIVATE SECTION. 
    DATA a1 TYPE string VALUE `c2: `. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    a1 &&= p1. 
    output=>out->write_data( a1 ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m1. 
    super->m1( p1 ). 
    a1 &&= p1. 
    output=>out->write_data( a1 ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA oref TYPE REF TO c1. 
    oref = NEW c2( ). 
    oref->m1( `...` ). 
 
    output=>out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
