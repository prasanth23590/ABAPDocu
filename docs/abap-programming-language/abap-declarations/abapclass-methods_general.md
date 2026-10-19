---
title: "CLASS-METHODS, IMPORTING, EXPORTING, CHANGING, RAISING"
source_file: abapclass-methods_general.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > CLASS-METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, IMPORTING, EXPORTING, CHANGING, RAISING

## Syntax

``` abap
CLASS-METHODS meth [DEFAULT IGNORE|FAIL]   
  [IMPORTING parameters [PREFERRED PARAMETER p]]   
  [EXPORTING parameters]   
  [CHANGING  parameters]   
  [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}   
  |{EXCEPTIONS exc1 exc2 ...}].  
```

[`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md)

## Description

This statement declares a general [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth`. The additions make an interface method optional, define the parameter interface of the method, and specify which exceptions the method can raise or propagate. The additions have the same syntax and meaning as those for [general instance methods](abapmethods_general.md).

## Hints

- Static methods cannot be redefined, which means that they cannot be flagged as abstract or final.

- Static methods are always executed in the class in which they were declared, even if they are called in subclasses or using the names of subclasses.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a static method with input/output parameters.

``` abap
CLASS xml DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS 
      escape_xml 
        CHANGING 
          xml TYPE xstring. 
    ... 
ENDCLASS.
```
