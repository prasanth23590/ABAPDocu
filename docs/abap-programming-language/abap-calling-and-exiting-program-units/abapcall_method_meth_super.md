---
title: "super->meth( ... )"
source_file: abapcall_method_meth_super.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Static Method Calls > meth( ... ), Standalone Method Call"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# super-\>meth( ... )

## Syntax

``` abap
... super->meth   
  | super->constructor ...  
```

### Alternative

[1. `... super->meth ...`](abapcall_method_meth_super.md#alternative-1)

[2. `... super->constructor ...`](abapcall_method_meth_super.md#alternative-2)

## Overview

### Description

This special form of a [static method specification](abapcall_method_meth_ident_stat.md) can be used in methods of subclasses to call the implementation of an identically named method in the direct superclass. The superclass is addressed using the [pseudo reference](../../abap-glossary/abenpseudo_reference_glosry.md) `super`.

## Alternative 1

`... super->meth ...`

### Description

Can be specified in the [redefinition](../../abap-glossary/abenredefinition_glosry.md) of the method `meth` in the implementation in a subclass and calls the implementation of the method `meth` in the direct superclass.

A method call `super->meth` can be used in the same operand positions and in the same syntax forms as [`oref->meth`](abapcall_method_meth_ident_stat.md), and the same rules apply to the parameter passing.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the implementation of the method `meth` in superclass `cls1` in the redefinition of the method in the subclass `cls2`.

``` abap
CLASS cls1 DEFINITION ABSTRACT. 
  PUBLIC SECTION. 
    METHODS meth. 
ENDCLASS. 
 
CLASS cls1 IMPLEMENTATION. 
  METHOD meth. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS cls2 DEFINITION INHERITING FROM cls1. 
  PUBLIC SECTION. 
    METHODS meth REDEFINITION. 
ENDCLASS. 
 
CLASS cls2 IMPLEMENTATION. 
  METHOD meth. 
    super->meth( ). 
    ... 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 2

`... super->constructor ...`

### Description

Must be specified in an instance constructor implemented in a subclass to call the instance constructor of the direct superclasses. The following restrictions apply before the superclass constructor is called:

- The instance constructor does not have access to the instance components of its class. The self-reference [`me->`](../abap-built-in-types-data-objects-functions-and-constructors/abenme.md) cannot be used. The static components of its class can be accessed, but not with `me->`.

- Before the superclass constructor is called, an instance constructor cannot be exited using statements such as `RETURN` or `CHECK`.

After the superclass constructor is called, the self-reference `me->` can be used and instance components can be accessed.

The superclass constructor can only be called using `super->constructor` as a [standalone statement](abapcall_method_static_short.md).

### Hints

- During the execution of a superclass constructor called using `super->constructor`, `meth` and `me->meth` do not address the method implementations of the subclass, but those of the superclass instead.

- The instance constructor of the superclass must be called, even if it is not declared explicitly.

- See also [Inheritance and Constructors](../abap-abap-objects/abeninheritance_constructors.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the superclass constructor in instance constructor of a subclass. Without this call, a syntax error occurs.

``` abap
CLASS cls1 DEFINITION. 
  ... 
ENDCLASS. 
 
CLASS cls2 DEFINITION INHERITING FROM cls1. 
  PUBLIC SECTION. 
    METHODS constructor. 
ENDCLASS. 
 
CLASS cls2 IMPLEMENTATION. 
  METHOD constructor. 
    super->constructor( ). 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
