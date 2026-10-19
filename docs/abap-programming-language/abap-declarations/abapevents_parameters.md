---
title: "EVENTS, parameters"
source_file: abapevents_parameters.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EVENTS, parameters

## Syntax

``` abap
... VALUE(p1) typing   [OPTIONAL|{DEFAULT def1}]   
    VALUE(p2) typing   [OPTIONAL|{DEFAULT def2}]   
    ...  
```

[`typing`](abentyping_syntax.md) · [`typing`](abentyping_syntax.md)

## Description

The syntax of the additions `VALUE`, `OPTIONAL`, and `DEFAULT` and the typing using [`typing`](abentyping_syntax.md) corresponds to the [definition of formal parameters](abapmethods_parameters.md) in the interface of methods.

When an event is raised using `RAISE EVENT`, suitable actual parameters must be specified for all non-optional output parameters; these actual parameters are optional for all optional output parameters. Optional parameters for which no actual parameter has been specified are set to their type-dependent [initial value](../../abap-glossary/abeninitial_value_glosry.md) or to the replacement parameter `def1 def2 ...`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of an instance event with an output parameter in the class `CL_DEMO_OUTPUT_STREAM`.

``` abap
CLASS cl_demo_output_stream DEFINITION. 
  ... 
  PUBLIC SECTION. 
    ... 
    EVENTS completed 
      EXPORTING 
        VALUE(ev_output) TYPE xstring. 
    ... 
ENDCLASS.
```
