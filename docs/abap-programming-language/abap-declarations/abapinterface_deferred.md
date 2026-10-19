---
title: "INTERFACE, DEFERRED"
source_file: abapinterface_deferred.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > INTERFACE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACE, DEFERRED

## Syntax

``` abap
INTERFACE intf DEFERRED.  
```

## Description

This variant of the statement `INTERFACE` is used to declare the interface `intf` independently of the location of the actual definition in the program. It does not introduce a declaration part and cannot be ended using `ENDINTERFACE`. The meaning is the same as for the corresponding variants of the statement [`CLASS`](abapclass_deferred.md).

## Hints

- This variant of the statement `INTERFACE` can also only be specified in the context described under [`INTERFACE`](abapinterface.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the interface `intf2` in front of the actual declaration in a type reference in the interface `intf1`. For this, it must be made known using `INTERFACE DEFERRED`.

``` abap
INTERFACE intf2 DEFERRED. 
 
INTERFACE intf1. 
  ... 
  DATA iref TYPE REF TO intf2. 
  ... 
ENDINTERFACE. 
 
INTERFACE intf2. 
  ... 
ENDINTERFACE.
```
