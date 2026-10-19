---
title: "meth( ... ), Static Method Specification"
source_file: abapcall_method_meth_ident_stat.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Static Method Calls > meth( ... ), Standalone Method Call"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# meth( ... ), Static Method Specification

## Syntax

``` abap
... meth   
  | oref->meth   
  | class=>meth   
  | super->meth ...  
```

[`super->meth`](abapcall_method_meth_super.md)

### Alternative

[1. `... meth ...`](abapcall_method_meth_ident_stat.md#alternative-1)

[2. `... oref->meth ...`](abapcall_method_meth_ident_stat.md#alternative-2)

[3. `... class=>meth ...`](abapcall_method_meth_ident_stat.md#alternative-3)

## Overview

### Description

These names are used for to specify methods statically, where `meth` is a valid name for the method in the current context. A special case of specifying methods statically is the specification after the pseudo reference [`super`](abapcall_method_meth_super.md) in methods of subclasses.

### Hint

The name of a method can be the name of the method declared in [`METHODS`](../abap-declarations/abapmethods.md), a name composed using the [interface component selector](../../abap-glossary/abeninterface_comp_selector_glosry.md), or an [alias name](../../abap-glossary/abenalias_glosry.md).

## Alternative 1

`... meth ...`

### Description

Can be specified in method implementations for any method `meth` of the same class. In instance methods, `meth` is a short form of `me->meth`, where `me` is the [self-reference](../../abap-glossary/abenself_reference_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of method `meth2` from another method `meth1`.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth1. 
  PRIVATE SECTION. 
    METHODS meth2. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth1. 
    ... 
    meth2( ). 
    ... 
  ENDMETHOD. 
  METHOD meth2. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 2

`... oref->meth ...`

### Description

Can be specified in processing blocks in which any method `meth` is visible. Here, `oref` contains an object reference to an object that contains the method as a component. The following can be specified for `oref`:

- A reference variable

- A single or chained [table expression](../../abap-glossary/abentable_expression_glosry.md) whose result is a reference variable

- A [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) with a [constructor operator](../../abap-glossary/abenconstructor_operator_glosry.md) [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or [`CAST`](../abap-processing-internal-data/abenconstructor_expression_cast.md)

This applies to both [standalone method calls](abapcall_method_static_short.md) and [functional method calls](abapcall_method_functional.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the instance method `meth` via a temporary reference variable created using the [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) operator.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    NEW demo( )->meth( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 3

`... class=>meth ...`

### Description

Can be specified in processing blocks in which a [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth` is visible, where `class` is one of the classes allowed by the package check that contains the method as a [static component](../../abap-glossary/abenstatic_component_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the static method `meth` using the name of the class.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    demo=>meth( ). 
  ENDMETHOD. 
ENDCLASS.
```
