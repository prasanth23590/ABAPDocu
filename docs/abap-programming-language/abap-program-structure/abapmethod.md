---
title: "METHOD"
source_file: abapmethod.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Procedures > Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHOD

## Syntax

``` abap
METHOD meth.   
  ...   
ENDMETHOD.  
```

## Description

Between the statements `METHOD` and `ENDMETHOD`, the functionality of a [method](../../abap-glossary/abenmethod_glosry.md) `meth` declared using [`[CLASS-]`](../abap-declarations/abapclass-methods.md)[`METHODS`](../abap-declarations/abapmethods.md) is implemented in a class. The implementation of a method is only possible in an implementation part of a class that was initiated using [`CLASS class IMPLEMENTATION`](../abap-declarations/abapclass.md).

Local data types and data objects can be declared within the method. It is also possible to access the formal parameters of the method as well as all components of all instances of its own class.

In [instance methods](../../abap-glossary/abeninstance_method_glosry.md), all components of the class and instance of the method can be addressed explicitly using the [self-reference](../../abap-glossary/abenself_reference_glosry.md) `me->`, besides their names. In addition, all components of other instances of the class of the method can be addressed using reference variables.

A method can be called [statically](../abap-calling-and-exiting-program-units/abenmethod_calls_static.md) or [dynamically](../abap-calling-and-exiting-program-units/abenmethod_calls_dynamic.md). For static calls, there is a standalone and a functional call form. Dynamic calls are always standalone calls.

## Hints

- During the implementation of a method of an interface `intf`, either the name declared in the prefix with `intf~` or an alias name of the class defined with [`ALIASES`](../abap-declarations/abapaliases.md), can be specified for `meth`. The method must exist in the interface, otherwise a syntax error occurs. If `intf~` is used, a syntax warning occurs for global interfaces only if an unused methods is deleted from the global interface, so that initial classes do not immediately become invalid because of this.

- The addition [`BY DATABASE PROCEDURE`](../abap-database-access/abapmethod_by_db_proc.md) transforms a method that is implemented in a database-specific language and not in ABAP and is executed in the database system into an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the two methods `m1` and `m2` of the class `c1` between `METHOD` and `ENDMETHOD` are implemented. Although the local data object `a1` hides the attribute of the same name, the attribute `a1` can be addressed using `me->a1`.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    METHODS m1 IMPORTING p1 TYPE string. 
  PRIVATE SECTION. 
    DATA a1 TYPE string. 
    METHODS m2. 
ENDCLASS. 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    a1 = p1. 
    m2( ). 
  ENDMETHOD. 
  METHOD m2. 
    DATA a1 TYPE string. 
    a1 = me->a1. 
  ENDMETHOD. 
ENDCLASS.
```
