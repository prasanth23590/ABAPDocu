---
title: "The Self-Reference me"
source_file: abenme.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# The Self-Reference me

Within the implementation of each instance method, an implicitly created local reference variable called `me` is available at runtime, which points to the instance in which the method is currently being executed. `me` is handled like a local constant, which means that the value of `me` cannot be changed in an instance method. The static type of `me` is the class in which the instance method is implemented.

The name `me` is reserved and cannot be used in a class for attributes, formal parameters, and local data objects.

## Hint

When an object is created, `me` also points to the instance of the generated subclass during the execution of an [instance constructor](../../abap-glossary/abeninstance_constructor_glosry.md) of a superclass called using [`super->constructor`](../abap-calling-and-exiting-program-units/abapcall_method_meth_super.md). However, in the instance constructor of the superclass, or in methods called by the instance constructor, `me->` has not effect in the method call if specified. Instead, the method implementations of the superclass are always called.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Access to identically named data objects of a class in a method. If specified on its own, `str` indicates the local data object of the method. The self-reference `me` is used to access the instance attribute `str` of the method.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth. 
  PRIVATE SECTION. 
    DATA str TYPE string VALUE `attr`. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    DATA str TYPE string VALUE `local`. 
    cl_demo_output=>display( |{ str }\n{ 
                                me->str }| ). 
  ENDMETHOD. 
ENDCLASS.
```
