---
title: "CLASS-METHODS, RETURNING"
source_file: abapclass-methods_functional.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > CLASS-METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, RETURNING

## Syntax

``` abap
CLASS-METHODS meth [DEFAULT IGNORE|FAIL]   
  [IMPORTING parameters [PREFERRED PARAMETER p]]   
  [EXPORTING parameters]   
  [CHANGING  parameters]   
  RETURNING VALUE(r) typing   
  [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}   
  |{EXCEPTIONS exc1 exc2 ...}].  
```

[`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`typing`](abentyping_syntax.md)

## Description

This statement declares a [functional](../../abap-glossary/abenfunctional_method_glosry.md) [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth`. The additions have exactly the same syntax and meaning as those for [functional instance methods](abapmethods_functional.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `circle` contains two functional static methods, `circumference` and `area`, which work with the constant `pi`.

``` abap
CLASS circle DEFINITION. 
  PUBLIC SECTION. 
    CONSTANTS pi TYPE decfloat34 
                 VALUE '3.141592653589793238462643383279503'. 
    CLASS-METHODS: circumference IMPORTING r        TYPE decfloat34 
                                 RETURNING VALUE(c) TYPE decfloat34, 
      area          IMPORTING r        TYPE decfloat34 
                    RETURNING VALUE(a) TYPE decfloat34. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS circle IMPLEMENTATION. 
  METHOD circumference. 
    c = 2 * pi * r. 
  ENDMETHOD. 
  METHOD area. 
    a = pi * r ** 2. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: circ   TYPE decfloat34, 
          area   TYPE decfloat34, 
          radius TYPE decfloat34. 
    radius = '1.00'. 
    circ = circle=>circumference( radius ). 
    area = circle=>area( radius ). 
  ENDMETHOD. 
ENDCLASS.
```
