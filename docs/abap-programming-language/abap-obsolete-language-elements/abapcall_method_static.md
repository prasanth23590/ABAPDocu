---
title: "CALL METHOD, Static Method Call (Obsolete)"
source_file: abapcall_method_static.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Calls"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL METHOD, Static Method Call (Obsolete)

## Syntax Obsolete

``` abap
CALL METHOD { meth( ) 
            | ( a ) 
            | ( p1 = a1 p2 = a2 ... ) 
            | ( p1 = a1 p2 = a2 ... ) 
            | ( [parameter_list] ) }.
```

``` abap
CALL METHOD   `meth` `[parameter_list]`.
```

[`meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_ident_stat.md) · [`meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_ident_stat.md) · [`meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_ident_stat.md) · [`meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_ident_stat.md) · [`[parameter_list]`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) · [`meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_ident_stat.md) · [`[parameter_list]`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md)

## Description

Both statements have the same semantics and call the method that is specified statically with the name [`meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_ident_stat.md).

- The first statement prefixes the [standalone method call](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) with a `CALL METHOD`.

- The second statement does not have any parentheses for filling the parameter interface. Instead, either an explicit [parameter list](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) is specified or no parameter list at all.

In the second variant without parentheses, no [chained method calls](../../abap-glossary/abenchained_method_call_glosry.md) are possible and the operators [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) and [`CAST`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) cannot be used to specify the method.

## Hints

- The static method call described here must not be confused with the call of [static methods](../../abap-glossary/abenstatic_method_glosry.md). A static method call is the static specification of an [instance method](../../abap-glossary/abeninstance_method_glosry.md) or a static method. In addition, there is the [dynamic method call](../abap-calling-and-exiting-program-units/abenmethod_calls_dynamic.md), for which the methods are specified dynamically.

  The statement `CALL METHOD` is now only intended for [dynamic method calls](../abap-calling-and-exiting-program-units/abenmethod_calls_dynamic.md) and distinguishes them clearly from static calls.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The three method calls in the following source code section have the same meaning. The first two calls are the obsolete variants with `CALL METHOD`: one without parentheses and one with. The third call is the recommended variant without `CALL METHOD`.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    METHODS do_something IMPORTING p1       TYPE i 
                                   p2       TYPE i 
                         EXPORTING p3       TYPE i 
                                   p4       TYPE i 
                         RETURNING VALUE(r) TYPE i. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD do_something. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(oref) = NEW demo( ). 
 
    CALL METHOD oref->do_something 
      EXPORTING 
        p1 = 333 
        p2 = 444 
      IMPORTING 
        p3 = FINAL(a1) 
        p4 = FINAL(a2) 
      RECEIVING 
        r  = FINAL(a3). 
 
    CALL METHOD oref->do_something( 
      EXPORTING 
        p1 = 333 
        p2 = 444 
      IMPORTING 
        p3 = FINAL(b1) 
        p4 = FINAL(b2) 
      RECEIVING 
        r  = FINAL(b3) ). 
 
    oref->do_something( 
      EXPORTING 
        p1 = 333 
        p2 = 444 
      IMPORTING 
        p3 = FINAL(c1) 
        p4 = FINAL(c2) 
      RECEIVING 
        r  = FINAL(c3) ). 
  ENDMETHOD. 
ENDCLASS.
```
