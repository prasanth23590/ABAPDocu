---
title: "ABAP Objects - Friendship"
source_file: abenfriends_abexa.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Friendship

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates an interface that is a [friend](abenfriends.md) of a class.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_oo_friendship DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    INTERFACES if_demo_friend. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_oo_friendship IMPLEMENTATION. 
  METHOD main. 
    out->write( cl_demo_friendship=>attr ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The empty global interface `IF_DEMO_FRIEND` is a friend of the global class `CL_DEMO_FRIENDSHIP`. Every class that implements `IF_DEMO_FRIEND` can access the private components of `CL_DEMO_FRIENDSHIP`.
