---
title: "CLASS, LOCAL FRIENDS"
source_file: abapclass_local_friends.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, LOCAL FRIENDS

## Syntax

``` abap
CLASS class DEFINITION 
            LOCAL FRIENDS class1 class2 ... 
                          intf1  intf2  ...  
```

## Description

This statement makes the local classes and interfaces `class1 class2 ...` and `intf1 intf2 ...` of a [class pool](../../abap-glossary/abenclass_pool_glosry.md) [friends](../../abap-glossary/abenfriend_glosry.md) of its global class `class`. At least one class or one interface must be specified.

This statement does not introduce a declaration part and must not be closed using the `ENDCLASS` statement.

## Hints

- The declaration of local classes of a class pool as friends of the global class is particularly necessary for local [test classes](../../abap-glossary/abentest_class_glosry.md) that test the private components of the global class.

- This variant of the statement `CLASS` can also only be listed in the context described under [`CLASS`](abapclass.md).

- If the local classes and interfaces `class1 class2 ...` and `intf1 intf2 ...` are to have access to all components of the global class `class` in their declaration part, the statement must first be specified in the class pool, for which the local classes and interfaces must first be registered using [`CLASS -`](abapclass_deferred.md) or [`INTERFACE - DEFERRED`](abapinterface_deferred.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the `CL_DEMO_AMDP_MESH` class, the `cl_test_selects` class from the [test include](../../abap-glossary/abentest_include_glosry.md) is declared in the [CCDEF include](../../abap-glossary/abenccdef_glosry.md) as a local friend of the global class, so that its private methods can be tested.

``` abap
CLASS cl_test_selects DEFINITION DEFERRED. 
CLASS cl_demo_amdp_mesh DEFINITION LOCAL FRIENDS cl_test_selects.
```
