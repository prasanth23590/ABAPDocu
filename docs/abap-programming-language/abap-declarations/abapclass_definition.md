---
title: "CLASS, DEFINITION"
source_file: abapclass_definition.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, DEFINITION

## Syntax

``` abap
CLASS class DEFINITION [class_options].   
  [PUBLIC SECTION.   
    [components]]   
  [PROTECTED SECTION.   
    [components]]   
  [PRIVATE SECTION.   
    [components]]   
ENDCLASS.  
```

[`class_options`](abapclass_options.md) · [`PUBLIC SECTION`](abappublic.md) · [`components`](abenclass_component.md) · [`PROTECTED SECTION`](abapprotected.md) · [`components`](abenclass_component.md) · [`PRIVATE SECTION`](abapprivate.md) · [`components`](abenclass_component.md)

## Description

The statement block `CLASS class DEFINITION - ENDCLASS` declares a class named `class`. [Naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `class`. The components [`components`](abenclass_component.md) of the class are declared between `CLASS` and `ENDCLASS`. Each component must be listed in a [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) after one of the statements `PUBLIC SECTION`, `PROTECTED SECTION`, or `PRIVATE SECTION` which must be specified in the order above. The class does not need to contain all the `SECTION` statements.

The [`class options`](abapclass_options.md) additions of the statement `CLASS` can be used to publish a class globally in the class library, define an inheritance relationship, make the class abstract or final, control instantiability, and offer [friendship](../../abap-glossary/abenfriend_glosry.md) to other classes or interfaces.

## Hints

- The class is the smallest encapsulation unit in ABAP Objects. A method can therefore use all components of all instances of the same class in addition to the components of its own instance. An exception to this rule are subclasses that cannot access the private components of superclasses if they are not their [friends](../../abap-glossary/abenfriend_glosry.md).

- The declaration part of a class can only be specified in the context described under [`CLASS`](abapclass.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration part of a class with statements for declaring [static components](../../abap-glossary/abenstatic_component_glosry.md) and [instance components](../../abap-glossary/abeninstance_component_glosry.md).

``` abap
CLASS cls DEFINITION FINAL. 
  PUBLIC SECTION. 
    TYPES: 
      type1 TYPE ... 
    CLASS-DATA: 
      attr1 TYPE ... 
    ... 
    CLASS-METHODS: 
      meth1 ... 
    ... 
    CLASS-EVENTS: 
       evt1 ... 
    ... 
    DATA: 
      attr2 TYPE ... 
    ... 
    METHODS: 
      meth2 ... 
    ... 
    EVENTS: 
       evt2 ... 
    ... 
ENDCLASS.
```
