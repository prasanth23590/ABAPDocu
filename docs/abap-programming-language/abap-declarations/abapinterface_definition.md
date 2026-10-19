---
title: "INTERFACE intf"
source_file: abapinterface_definition.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > INTERFACE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACE intf

## Syntax

``` abap
INTERFACE intf [PUBLIC].   
  [components]   
ENDINTERFACE.  
```

[`components`](abeninterface_component.md)

### Addition

[`... PUBLIC`](abapinterface_definition.md#addition)

## Overview

### Description

The statement block `INTERFACE - ENDINTERFACE` defines an [interface](../../abap-glossary/abenoo_intf_glosry.md) `intf`. [Naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `intf`. The [`components`](abeninterface_component.md) of the interface are declared between `INTERFACE` and `ENDINTERFACE`.

An interface defined using `INTERFACE` can be implemented in classes and included in other interfaces using the statement [`INTERFACES`](abapinterfaces.md).

### Hint

The definition of an interface can only be specified in the context described under [`INTERFACE`](abapinterface.md).

## Addition

`... PUBLIC`

### Description

The addition `PUBLIC` makes the interface `intf` a [global interface](../../abap-glossary/abenglobal_interface_glosry.md) of the class library. The addition `PUBLIC` can only be used for the global interface of an [interface pool](../../abap-glossary/abeninterface_pool_glosry.md).

### Hint

A global interface is a global [object type](../../abap-glossary/abenobject_type_glosry.md) and is in the same namespace as all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, an interface `i1` is declared using three interface components `a1`, `m1`, and `e1`. The class `c1` implements the interface and the interface components therefore become [public](../../abap-glossary/abenpublic_glosry.md) components of the class, which can be addressed using the interface component selector (`~`).

``` abap
INTERFACE i1. 
  DATA    a1 TYPE string. 
  METHODS m1. 
  EVENTS  e1 EXPORTING value(p1) TYPE string. 
ENDINTERFACE. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES i1. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD i1~m1. 
    RAISE EVENT i1~e1 EXPORTING p1 = i1~a1. 
  ENDMETHOD. 
ENDCLASS.
```
