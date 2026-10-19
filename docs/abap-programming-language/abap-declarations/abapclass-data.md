---
title: "CLASS-DATA"
source_file: abapclass-data.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Data Types and Attributes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-DATA

## Syntax

``` abap
CLASS-DATA attr [options].  
```

[`options`](abapdata.md)

## Description

The statement `CLASS-DATA` can only be used in the declaration part of a class or an interface. It declares a static attribute `attr` whose validity is not tied to instances of a class, but to the class itself. All instances of the class and its subclasses access a static attribute.

The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `attr`. The syntax of the additions `options` is identical to the statement [`DATA`](abapdata.md) for instance attributes (only the addition [`WITH HEADER LINE`](abapdata_itab.md) must not be used).

## Hints

- Like all [static components in the inheritance](../abap-abap-objects/abeninheritance_statical.md), the static attributes of a superclass exist in all subclasses. A static attribute that is visible externally can be addressed using the class component selector and all the names of the classes in which it exists. This means that the class in which it is declared is always addressed, which, for example, has an effect on the execution of the [static constructor](../../abap-glossary/abenstatic_constructor_glosry.md). A change to a static attribute applies to all classes in which it exists, independently of the addressing.

- Static attributes declared using `CLASS-DATA` can be accessed using the class component selector only with class names, not with interface names.

- Structured static attributes can be declared as a [static box](../../abap-glossary/abenstatic_box_glosry.md) using the addition [`BOXED`](abapdata_boxed.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the static attribute `text` of class `c1` is accessed using the class component selector without creating an instance of the class.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA text TYPE string VALUE `Static data`. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    out->write_text( c1=>text ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
