---
title: "METHODS, ABSTRACT, FINAL"
source_file: abapmethods_abstract_final.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, ABSTRACT, FINAL

## Syntax

``` abap
METHODS meth ... ABSTRACT|FINAL ...  
```

### Addition

[1. `... ABSTRACT`](abapmethods_abstract_final.md#addition-1)

[2. `... FINAL`](abapmethods_abstract_final.md#addition-2)

## Overview

### Description

The additions `ABSTRACT` and `FINAL` make an instance method abstract or final. They cannot be used in interfaces, only in classes. All instance methods can be declared as abstract except for instance constructors. The addition `FINAL` can be used in all variants of the statement `METHODS`.

## Addition 1

`... ABSTRACT`

### Description

The addition `ABSTRACT` defines an abstract method `meth`. The addition `ABSTRACT` is allowed only in abstract classes, not in interfaces. An abstract method is not implemented in the implementation part of its class. To implement an abstract method, it must be redefined in a [specific](../../abap-glossary/abenconcrete_glosry.md) subclass using the addition `REDEFINITION`. Private methods cannot be redefined and can therefore not be declared as abstract.

### Hints

- Abstract methods can also be defined in classes that are both abstract and final, but they can never be implemented and therefore are not usable.

- Methods in interfaces are always implicitly abstract, because interfaces do not contain method implementations.

- With the exception of the instance constructor, concrete instance methods of a class can also call their abstract methods.

- Static methods cannot be redefined, and the addition `ABSTRACT` is not allowed in their declarations.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of an abstract method of an abstract superclass and its implementation in a concrete subclass.

``` abap
CLASS cls1 DEFINITION ABSTRACT. 
  PROTECTED SECTION. 
    METHODS meth ABSTRACT. 
ENDCLASS. 
 
CLASS cls2 DEFINITION INHERITING FROM cls1. 
  PROTECTED SECTION. 
    METHODS meth REDEFINITION. 
ENDCLASS. 
 
CLASS cls2 IMPLEMENTATION. 
  METHOD meth. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```

## Addition 2

`... FINAL`

### Description

The addition `FINAL` defines a final method `meth`. The addition `FINAL` is allowed only in classes, not in interfaces. A final method cannot be redefined in a subclass. In final classes, all methods are automatically final and the addition `FINAL` is not allowed. An instance constructor [`constructor`](abapmethods_constructor.md) is always final and `FINAL` can be specified but is not mandatory.

### Hints

- Static methods cannot be redefined, and the addition `FINAL` is not allowed in their declarations.

- The addition `FINAL` closes a path of an inheritance tree with regards to the possibility to redefine the method.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The final method `get_the_truth` of a superclass returns a value, which cannot be changed in a subclass. Method `get_opinion` can be redefined in a subclass, but the subclass shown here prevents the method from being redefined in subclasses.

``` abap
CLASS cls1 DEFINITION. 
  PUBLIC SECTION. 
    METHODS: 
      get_the_truth FINAL 
        RETURNING VALUE(truth) TYPE string, 
      get_opinion 
        RETURNING VALUE(opinion) TYPE string. 
ENDCLASS. 
 
CLASS cls2 DEFINITION INHERITING FROM cls1. 
  PUBLIC SECTION. 
    METHODS get_opinion FINAL REDEFINITION. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS cls1 IMPLEMENTATION. 
  METHOD get_the_truth. 
    truth = `The final truth`. 
  ENDMETHOD. 
  METHOD get_opinion. 
    opinion = `Opinion of superclass`. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS cls2 IMPLEMENTATION. 
  METHOD get_opinion. 
    opinion = `Opinion of subclass`. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    FINAL(oref) = NEW cls2( ). 
    out->write( 
      |{ oref->get_the_truth( ) }\n{ oref->get_opinion( ) }| ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
