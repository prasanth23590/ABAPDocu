---
title: "rel_exp - Predicate Expression IS NOT BOUND"
source_file: abenbound_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Expressions > rel_exp - IS BOUND"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Predicate Expression IS NOT BOUND

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the predicate expression [`IS NOT BOUND`](abenlogexp_bound.md).

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
CLASS cl_demo_is_not_bound DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    DATA dref TYPE REF TO i. 
    METHODS meth. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_is_not_bound IMPLEMENTATION. 
  METHOD main. 
    me->meth( ). 
    IF me->dref IS NOT INITIAL AND 
       me->dref IS NOT BOUND. 
      out->write( 
        'stack reference is not initial but not bound' ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD meth. 
    DATA number TYPE i. 
    dref = REF #( number ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The static attribute `dref` of a class is assigned a reference to a local data object in a method. This [stack reference](../../abap-glossary/abenstack_reference_glosry.md) is invalid once the method is exited. Therefore, both predicate expressions `IS NOT INITIAL` and `IS NOT BOUND` are true for `dref`.
