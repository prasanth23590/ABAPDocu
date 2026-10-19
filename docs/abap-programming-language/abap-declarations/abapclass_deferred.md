---
title: "CLASS, DEFERRED"
source_file: abapclass_deferred.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, DEFERRED

## Syntax

``` abap
CLASS class DEFINITION DEFERRED.  
```

## Description

This variant of the statement `CLASS` is used to make the class `class` known temporarily in the program, regardless of the location of the actual definition of the class in the program. It does not introduce a declaration part and must not be closed using `ENDCLASS`.

The statement makes a local class known before its actual definition. The program must contain a declaration part for `class` at a later point. It is not possible to access individual components before the actual definition. The statement is necessary if a reference to a local class is to be made before it is defined.

## Hints

- This variant of the statement `CLASS` can only be listed in the same context as described under [`CLASS`](abapclass.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the class `c1` uses the class `c2` and vice versa. This means that one of the classes must be made known before it is actually defined.

``` abap
CLASS c1 DEFINITION DEFERRED. 
 
CLASS c2 DEFINITION. 
  PUBLIC SECTION. 
    DATA c1ref TYPE REF TO c1. 
ENDCLASS. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    DATA c2ref TYPE REF TO c2. 
ENDCLASS.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A typical use case for the need of `CLASS class DEFINITION DEFERRED` are [test classes](../../abap-glossary/abentest_class_glosry.md) of [ABAP Unit](../../abap-glossary/abenabap_unit_glosry.md) that must access private components of a global class and thus must be declared as friends of that class. Since the [test include](../../abap-glossary/abentest_include_glosry.md), where the test classes are defined is located behind the [CCDEF include](../../abap-glossary/abenccdef_glosry.md) where the friendship is declared, the test classes must be declared deferred in the CCDEF include.

See the class pool of `CL_DEMO_ABAP_UNIT`.
