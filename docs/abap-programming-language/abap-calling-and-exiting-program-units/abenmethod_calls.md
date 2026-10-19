---
title: "Method Calls"
source_file: abenmethod_calls.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Method Calls

There are two types of method call, static method calls and dynamic method calls. In static method calls, the name of the method must be completely known in the program. In dynamic method calls, the name of the method is determined partially or completely at runtime.

When an instance method is called using a reference variable and the static type of the reference variable is a superclass of the dynamic type, the dynamic method call can be used to call all visible methods of the dynamic type. In static method calls, however, only the visible methods of the static type can be called.

Static method calls have the pattern `meth( )`. They do not need a keyword, but the method is specified directly and the parameters passing is in parentheses instead. Dynamic method calls are introduced using `CALL METHOD`.

- [Static method calls](abenmethod_calls_static.md)

- [Dynamic method calls](abenmethod_calls_dynamic.md)

## System Fields

The system field `sy-subrc` is set to 0 when a method is called. If a [non-class-based exception](../abap-program-flow-logic/abenexceptions_non_class.md) is raised and is handled by the assignment of a value, `sy-subrc` is set to this value.
