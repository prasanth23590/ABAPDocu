---
title: "PUBLIC SECTION"
source_file: abappublic.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS > CLASS, DEFINITION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# PUBLIC SECTION

## Syntax

``` abap
PUBLIC SECTION.  
```

## Description

This statement can only be used in the [declaration part](abapclass_definition.md) of a class and defines the public [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of the class `class`. All components of the class that are declared in the area after the statement `PUBLIC SECTION` can be addressed from outside the class, in their subclasses, and in the class itself, provided this is allowed by the [package concept](../../abap-glossary/abenpackage_concept_glosry.md). Public methods in particular can be redefined in subclasses.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a public constant `const` and accesses it from outside of the class.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    CONSTANTS const TYPE string VALUE `I'm public`. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    out->write( cls=>const ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
