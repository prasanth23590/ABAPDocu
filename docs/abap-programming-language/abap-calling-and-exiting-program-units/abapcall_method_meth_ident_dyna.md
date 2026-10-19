---
title: "CALL METHOD, dynamic_meth"
source_file: abapcall_method_meth_ident_dyna.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Dynamic Method Call > CALL METHOD"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL METHOD, dynamic_meth

## Syntax

``` abap
... (meth_name)   
  | oref->(meth_name)   
  | class=>(meth_name)   
  | (class_name)=>(meth_name)   
  | (class_name)=>meth ...  
```

### Addition

[1. `... (meth_name) ...`](abapcall_method_meth_ident_dyna.md#addition-1)

[2. `... (class_name) ...`](abapcall_method_meth_ident_dyna.md#addition-2)

### Alternative

[1. `... (meth_name) ...`](abapcall_method_meth_ident_dyna.md#alternative-1)

[2. `... oref->(meth_name) ...`](abapcall_method_meth_ident_dyna.md#alternative-2)

[3. `... class=>(meth_name) ...`](abapcall_method_meth_ident_dyna.md#alternative-3)

[4. `... (class_name)=>(meth_name) ...`](abapcall_method_meth_ident_dyna.md#alternative-4)

[5. `... (class_name)=>meth ...`](abapcall_method_meth_ident_dyna.md#alternative-5)

## Overview

### Description

These names are used to specify methods dynamically.

## Addition 1

`... (meth_name) ...`

### Description

`meth_name` expects a character-like field that must contain the name of a method when the statement is executed.

## Addition 2

`... (class_name) ...`

### Description

`class_name` expects a character-like field that must contain the name of a class in uppercase letters when the statement is executed. An [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md) can also be specified. The following can be specified for `class_name`:

- Literal or constants

  If the data object `class_name` is specified as a character literal or as a constant, it can be evaluated statically, and the specified class is recognized as the used object.

- Variable

  If the data object `class_name` is specified as a variable, it is specified only dynamically, and the content is not evaluated statically.

When the statement is executed, `class_name` is not evaluated until runtime (in both cases).

## Alternative 1

`... (meth_name) ...`

### Description

This variant is only possible for methods of the same class. It works like `me->(meth_name)` (see alternative 2).

## Alternative 2

`... oref->(meth_name) ...`

### Description

This form is possible for all visible methods of objects. `oref` can be any [class reference variable](../../abap-glossary/abenclass_reference_variabl_glosry.md) or [interface reference variable](../../abap-glossary/abeninterface_ref_variable_glosry.md) that points to an object containing the method or interface method specified in `meth_name`. The system first searches in the [static type](../../abap-glossary/abenstatic_type_glosry.md) and then in the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of `oref` for the method.

### Hints

- In dynamic access as in static access, interface reference variables cannot be used to access any components, only interface components.

## Alternative 3

`... class=>(meth_name) ...`

## Alternative 4

`... (class_name)=>(meth_name) ...`

## Alternative 5

`... (class_name)=>meth ...`

### Description

These forms are possible for all visible static methods. Both the class and method can be specified dynamically. The class `class` and the method `meth` can also be specified directly.

For alternatives with a dynamic class specification `(class_name)`, the system first searches the class and then the method. If `class` is specified statically, the search for the method is carried out in the existing class.

### Hints

- Methods of local classes can be called externally only by specifying the [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md). In the case of classes defined in an [include program](../../abap-glossary/abeninclude_program_glosry.md), the name of the include program cannot be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates different types of dynamic method calls.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth1. 
  PRIVATE SECTION. 
    METHODS: meth2, 
      meth3. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth1. 
    FINAL(oref) = NEW demo( ). 
    FINAL(meth) = `METH2`. 
    CALL METHOD oref->(meth). 
  ENDMETHOD. 
  METHOD meth2. 
    FINAL(meth) = `METH3`. 
    CALL METHOD (meth). 
  ENDMETHOD. 
  METHOD meth3. 
    FINAL(out) = cl_demo_output=>new( ). 
    out->write( 'called' ). 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(class) = `CLS`. 
    FINAL(meth) = `METH1`. 
    CALL METHOD (class)=>(meth). 
  ENDMETHOD. 
ENDCLASS.
```
