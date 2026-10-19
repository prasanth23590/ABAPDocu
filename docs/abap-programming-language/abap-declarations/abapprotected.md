---
title: "PROTECTED SECTION"
source_file: abapprotected.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS > CLASS, DEFINITION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PROTECTED SECTION

## Syntax

``` abap
PROTECTED SECTION.  
```

## Description

This statement can only be used in the [declaration part](abapclass_definition.md) of a class and defines the protected [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of the class `class`.

All components of the class that are declared in the area behind the statement `PROTECTED SECTION` can be addressed directly only in the subclasses of the class and in the class itself, as well as its [friends](../../abap-glossary/abenfriend_glosry.md), if allowed by the [package concept](../../abap-glossary/abenpackage_concept_glosry.md). In particular, protected methods in subclasses can be redefined.

## Hints

- The class is the smallest encapsulation unit in ABAP Objects. Therefore a method can use all protected components of all instances of its class besides the protected components of its own class.

- In subclasses, it is not possible to access the protected components of superclasses using reference variables of the type of the superclass, because otherwise an attribute of an object of the dynamic type of the superclass or another subclass could be changed. However, the latter only produces a warning from the extended syntax check.

- A subclass cannot access the protected components of a subclass of a different branch of the inheritance hierarchy inherited from a shared superclass.

- The declaration of attributes in the protected section does not prevent methods in subclasses or in the class itself from passing [references](../../abap-glossary/abenreference_glosry.md) to these attributes in the form of [reference variables](../../abap-glossary/abenreference_variable_glosry.md) or [field symbols](../../abap-glossary/abenfield_symbol_glosry.md), so that the attributes become visible and modifiable outside the protected section.

- For technical reasons a [global class](../../abap-glossary/abenglobal_class_glosry.md) that can be part of an inheritance tree that is

  - a [subclass](../../abap-glossary/abensubclass_glosry.md)

  - a non-[final](../../abap-glossary/abenfinal_glosry.md) class that is not a subclass but can be a [superclass](../../abap-glossary/abensuperclass_glosry.md)

    must contain the statement `PROTECTED SECTION` also for an empty protected section.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a protected constant `const` in a superclass `cls1` and its use as a start value of a public attribute of a subclass `cls2`.

``` abap
CLASS cls1 DEFINITION. 
  PROTECTED SECTION. 
    CONSTANTS const TYPE string VALUE `I'm protected`. 
ENDCLASS. 
 
CLASS cls2 DEFINITION INHERITING FROM cls1. 
  PUBLIC SECTION. 
    CLASS-DATA attr TYPE string VALUE cls1=>const. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    out->write( cls2=>attr ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
