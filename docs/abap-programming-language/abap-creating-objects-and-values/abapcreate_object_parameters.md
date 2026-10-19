---
title: "CREATE OBJECT, parameter_list"
source_file: abapcreate_object_parameters.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE OBJECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE OBJECT, parameter_list

## Syntax

``` abap
 ... [EXPORTING  p1 = a1 p2 = a2 ...] 
    [EXCEPTIONS exc1 = n1 exc2 = n2 ... [OTHERS = n_others]].  
```

## Description

The additions `EXPORTING` and `EXCEPTIONS` are used to pass actual parameters to the instance constructor statically or to assign return values to non-class-based exceptions.

- The addition `EXPORTING` must be used to supply the non-optional input parameters `p1 p2 ...` of the instance constructor of the instantiated class with the type-compliant actual parameters `a1 a2 ...`. The other input parameters are optional. As in regular method calls, `a1`, `a2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). This means that expressions can be passed as actual parameters in addition to data objects. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case. If a subclass does not have an instance constructor implemented explicitly, the interface of the instance constructor from the next-highest superclass that explicitly implements the instance constructor is filled.

- The addition `EXCEPTIONS` can be used to assign return codes to [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) `exc1 exc2...`

The syntax and semantics are the same as in the parameter list for [static method calls](../abap-calling-and-exiting-program-units/abenmethod_calls_static.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an instance of a local class `cls1` and passing input parameters to its instance constructor. The class is specified implicitly using the static type of the reference variable `oref`.

``` abap
CLASS cls1 DEFINITION. 
  PUBLIC SECTION. 
    METHODS constructor 
      IMPORTING p1 TYPE string 
                p2 TYPE i. 
ENDCLASS. 
 
CLASS cls1 IMPLEMENTATION. 
  METHOD constructor. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS cls2 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth. 
ENDCLASS. 
 
CLASS cls2 IMPLEMENTATION. 
  METHOD meth. 
    DATA oref TYPE REF TO cls1. 
    CREATE OBJECT oref 
      EXPORTING 
        p1 = `...` 
        p2 = 333. 
  ENDMETHOD. 
ENDCLASS.
```
