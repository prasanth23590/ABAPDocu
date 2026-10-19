---
title: "meth( ... ), Standalone Method Call"
source_file: abapcall_method_static_short.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Static Method Calls"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# meth( ... ), Standalone Method Call

## Syntax

``` abap
{ meth( )   
| meth( a )   
| meth( p1 = a1 p2 = a2 ... )   
| meth( [EXPORTING  p1 = a1 p2 = a2 ...]   
        [IMPORTING  p1 = a1 p2 = a2 ...]   
        [CHANGING   p1 = a1 p2 = a2 ...]   
        [RECEIVING  r  = a]   
        [EXCEPTIONS [exc1 =n1 exc2 = n2 ...]   
                    [OTHERS = n_others]] ) }.  
```

[`meth`](abapcall_method_meth_ident_stat.md) · [`meth`](abapcall_method_meth_ident_stat.md) · [`meth`](abapcall_method_meth_ident_stat.md) · [`meth`](abapcall_method_meth_ident_stat.md) · [`EXPORTING p1 = a1 p2 = a2 ...`](abapcall_method_parameters.md) · [`IMPORTING p1 = a1 p2 = a2 ...`](abapcall_method_parameters.md) · [`CHANGING p1 = a1 p2 = a2 ...`](abapcall_method_parameters.md) · [`RECEIVING r = a`](abapcall_method_parameters.md) · [`EXCEPTIONS [exc1 =n1 exc2 = n2 ...]`](abapcall_method_parameters.md) · [`OTHERS = n_others]]`](abapcall_method_parameters.html)

### Alternative

[1. `meth( ).`](abapcall_method_static_short.md#alternative-1)

[2. `meth( a ).`](abapcall_method_static_short.md#alternative-2)

[3. `meth( p1 = a1 p2 = a2 ... ).`](abapcall_method_static_short.md#alternative-3)

[4. `meth( EXPORTING ... IMPORTING ... CHANGING ... RECEIVING ... ).`](abapcall_method_static_short.md#alternative-4)

## Overview

### Description

Static call of a method specified as a standalone statement using the name [`meth`](abapcall_method_meth_ident_stat.md). The [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) of the method is filled with the actual parameters in the parentheses. In the first alternative, no formal parameters are supplied with actual parameters. The second and third alternatives are short forms for methods where only the input parameters are supplied with actual parameters. The fourth alternative allows all possible formal parameters to be supplied with actual parameters and non-class-based exceptions to be handled.

### System Fields

Each method call sets the system field `sy-subrc` to 0 in the moment the method is called. Handling [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) can change this value.

### Hint

The static method call described here must not be confused with the call of [static methods](../../abap-glossary/abenstatic_method_glosry.md). A static method call is the static specification of an [instance method](../../abap-glossary/abeninstance_method_glosry.md) or a static method. In addition, there is the [dynamic method call](abenmethod_calls_dynamic.md), for which the methods are specified dynamically.

## Alternative 1

`meth( ).`

### Description

Call of the method [`meth`](abapcall_method_meth_ident_stat.md) without passing parameters. The method cannot have any or can have only optional input parameters or input/output parameters. No actual parameters are assigned to any output parameters or to a return value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of a method without parameters.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS do_something. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD do_something. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    c1=>do_something( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 2

`meth( a ).`

### Description

This is the short form of:

meth( [`EXPORTING`](abapcall_method_parameters.md) p = a ).

The method [`meth`](abapcall_method_meth_ident_stat.md) can have the following parameters:

- Either exactly one non-optional input parameter `p` and any number of optional input parameters

- Or only optional input parameters from which `p` is defined as a preferred parameter using `PREFERRED PARAMETER`

The value of `a` is passed to the non-optional input parameter or to the preferred parameter. The actual parameter `a` can be specified as a data object, a function, or an expression.

The method can only have optional input/output parameters. No actual parameter is assigned to these input/output parameters, any output parameters, or return values.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of a method with an input parameter.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS do_something IMPORTING p TYPE i. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD do_something. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    c1=>do_something( 333 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 3

`meth( p1 = a1 p2 = a2 ... ).`

### Description

This is the short form of:

meth( [`EXPORTING`](abapcall_method_parameters.md) p1 = a1 p2 = a2 ... ).

The method [`meth`](abapcall_method_meth_ident_stat.md) can have any number of input parameters `p1`, `p2`, ... that are supplied with the actual parameters `a1`, `a2`, .... The actual parameters can be specified as a data object, a function, or an expression.

The method can only have optional input/output parameters. No actual parameter is assigned to these input/output parameters, any output parameters, or return values.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of a method with two input parameters.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS do_something IMPORTING p1 TYPE i 
                                         p2 TYPE i. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD do_something. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
  CLASS exa IMPLEMENTATION. 
  METHOD main. 
    c1=>do_something( p1 = 333 p2 = 444 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 4

`meth( EXPORTING ... IMPORTING ... CHANGING ... RECEIVING ... ).`

### Description

Call of the method [`meth`](abapcall_method_meth_ident_stat.md) with explicit [parameter passing](abapcall_method_parameters.md) and the option of handling non-class-based exceptions. This format can be used to call methods with any number of parameter interfaces.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of a method with explicit parameter passing.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS do_something IMPORTING p1       TYPE i 
                                         p2       TYPE i 
                               EXPORTING p3       TYPE i 
                                         p4       TYPE i 
                               RETURNING VALUE(r) TYPE i. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD do_something. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    c1=>do_something( EXPORTING p1 = 333 
                              p2 = 444 
                    IMPORTING p3 = FINAL(a1) 
                              p4 = FINAL(a2) 
                    RECEIVING r  = FINAL(a3) ). 
  ENDMETHOD. 
ENDCLASS.
```
