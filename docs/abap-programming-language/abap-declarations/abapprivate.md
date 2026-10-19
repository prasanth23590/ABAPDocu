---
title: "PRIVATE SECTION"
source_file: abapprivate.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS > CLASS, DEFINITION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PRIVATE SECTION

## Syntax

``` abap
PRIVATE SECTION.  
```

## Description

This statement can only be used in the [declaration part](abapclass_definition.md) of a class and defines the private [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of the class `class`. All components of the class that are declared in the area after the statement `PRIVATE SECTION` can only be addressed in the class itself and in its [friends](../../abap-glossary/abenfriend_glosry.md).

## Hints

- The class is the smallest encapsulation unit in ABAP Objects. Therefore, a method can use all private components of all instances of the same class, apart from the private components of its own class. An exception to this rule are subclasses that cannot access the private components of superclasses if they are not their [friends](../../abap-glossary/abenfriend_glosry.md).

- The declaration of attributes in the private section does not prevent methods of the class from passing [references](../../abap-glossary/abenreference_glosry.md) to these attributes to the outside in the form of [reference variables](../../abap-glossary/abenreference_variable_glosry.md) or [field symbols](../../abap-glossary/abenfield_symbol_glosry.md), which makes the attributes visible and modifiable outside the private section.

- Private components declared in a class but not used statically there produce a warning in the extended program check.

- For technical reasons a [global class](../../abap-glossary/abenglobal_class_glosry.md) that can be part of an inheritance tree that is

  - a [subclass](../../abap-glossary/abensubclass_glosry.md)

  - a non-[final](../../abap-glossary/abenfinal_glosry.md) class that is not a subclass but can be a [superclass](../../abap-glossary/abensuperclass_glosry.md)

    must contain the statement `PRIVATE SECTION` also for an empty private section.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a private constant `const` in a class `cls1` and uses it as a start value of a public attribute of a friend `cls2`.

``` abap
CLASS cls2 DEFINITION DEFERRED. 
 
CLASS cls1 DEFINITION FRIENDS cls2. 
  PRIVATE SECTION. 
    CONSTANTS const TYPE string VALUE `I'm private`. 
ENDCLASS. 
 
CLASS cls2 DEFINITION. 
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
