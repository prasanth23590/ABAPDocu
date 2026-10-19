---
title: "CLASS"
source_file: abapclass.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS

## Syntax Forms

**[Declaration Part of a Class](abapclass_definition.md)**

``` abap
1. CLASS class DEFINITION [class_options]. 
    [PUBLIC SECTION. 
      [components]] 
    [PROTECTED SECTION. 
      [components]] 
    [PRIVATE SECTION. 
      [components]] 
  ENDCLASS.
```

**[Implementation Part of a Class](abapclass_implementation.md)**

``` abap
2. CLASS class IMPLEMENTATION. 
    ... 
    METHOD ... 
      ... 
    ENDMETHOD. 
    ... 
  ENDCLASS.
```

**[Publication of Classes](abapclass_deferred.md)**

``` abap
3. CLASS class DEFINITION DEFERRED [PUBLIC].
```

**[Local Friends of Global Classes](abapclass_local_friends.md)**

``` abap
4. CLASS class DEFINITION 
              LOCAL FRIENDS class1 class2 ... 
                            intf1  intf2  ...
```

[`class_options`](abapclass_options.md) · [`components`](abenclass_component.md) · [`components`](abenclass_component.md) · [`components`](abenclass_component.md)

## Description

The statement `CLASS` defines a class `class`, publishes it, or specifies properties.

- The complete definition of a class consists of a [declaration part](abapclass_definition.md) and an [implementation part](abapclass_implementation.md), which are both introduced by `CLASS` and ended by `ENDCLASS`. In the declaration part, the properties of the class are specified, and its components are declared. In the implementation part, the methods of the class are implemented.

- The variants of `CLASS` without `ENDCLASS` are used for the [publication of classes](abapclass_deferred.md) in a program and the declaration of [local friends](abapclass_local_friends.md) of a global class.

The statements `CLASS` and associated statements `ENDCLASS` can be specified in the following contexts:

- `CLASS` and `ENDCLASS` can only be specified in the global context of a program.

- `CLASS` and `ENDCLASS` cannot be listed within classes, procedures.

This applies in particular also to the variants of `CLASS` listed here, which are not closed using `ENDCLASS`.

## Hints

- The declaration part of a class, and the variants of `CLASS` that are not closed using `ENDCLASS` are handled like other declaration statements (`DATA`, `TYPE`, ...). In a processing block without a local context, they are handled like global program declarations and do not close the processing block.

- The implementation part of a class works like a separate processing block and closes any other processing blocks.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration and implementation of a local class `demo` with some of the possible components.

``` abap
CLASS demo DEFINITION CREATE PRIVATE. 
  PUBLIC SECTION. 
    TYPES result TYPE string. 
    CLASS-METHODS new 
      RETURNING VALUE(ref) TYPE REF TO demo. 
    METHODS main 
      RETURNING VALUE(result) TYPE result. 
  PRIVATE SECTION. 
    METHODS util CHANGING text TYPE result. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD new. 
    ref = NEW demo( ). 
  ENDMETHOD. 
  METHOD main. 
    DATA var TYPE result. 
    ... 
    me->util( CHANGING text = var ). 
    ... 
  ENDMETHOD. 
  METHOD util. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
