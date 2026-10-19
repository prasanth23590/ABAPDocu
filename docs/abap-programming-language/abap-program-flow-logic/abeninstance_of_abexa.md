---
title: "rel_exp - Predicate Expression IS INSTANCE OF"
source_file: abeninstance_of_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Expressions > rel_exp - IS INSTANCE OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Predicate Expression IS INSTANCE OF

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the predicate expression [`IS INSTANCE OF`](abenlogexp_instance_of.md).

## Source Code

``` abap
* CCDEF 
INTERFACE intf. 
ENDINTERFACE. 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
ENDCLASS. 
 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_is_instance_of DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_is_instance_of IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      oref  TYPE REF TO object, 
      iref  TYPE REF TO intf, 
      c1ref TYPE REF TO c1, 
      c2ref TYPE REF TO c2. 
 
    FIELD-SYMBOLS <fs> TYPE any. 
 
    out->next_section( `Reference Variable Not Initial` ). 
 
    out->begin_section( `TYPE REF TO object` ). 
    oref = NEW c1( ). 
    ASSERT oref IS NOT INSTANCE OF c2. 
    out->write( `oref pointing to c1 is not instance of c2` ). 
    ASSERT oref IS INSTANCE OF c1. 
    out->write( `oref pointing to c1 is instance of c1` ). 
    ASSERT oref IS INSTANCE OF intf. 
    out->write( `oref pointing to c1 is instance of intf` ). 
    oref = NEW c2( ). 
    ASSERT oref IS INSTANCE OF c2. 
    out->write( `oref pointing to c2 is instance of c2` ). 
    ASSERT oref IS INSTANCE OF c1. 
    out->write( `oref pointing to c2 is instance of c1` ). 
    ASSERT oref IS INSTANCE OF intf. 
    out->write( `oref pointing to c2 is instance of intf` ). 
    out->end_section( ). 
 
    out->begin_section( `TYPE REF TO intf` ). 
    iref = NEW c1( ). 
    ASSERT iref IS NOT INSTANCE OF c2. 
    out->write( `iref pointing to c1 is not instance of c2` ). 
    ASSERT iref IS INSTANCE OF c1. 
    out->write( `iref pointing to c1 is instance of c1` ). 
    ASSERT iref IS INSTANCE OF intf. 
    out->write( `iref pointing to c1 is instance of intf` ). 
    iref = NEW c2( ). 
    ASSERT iref IS INSTANCE OF c2. 
    out->write( `iref pointing to c2 is instance of c2` ). 
    ASSERT iref IS INSTANCE OF c1. 
    out->write( `iref pointing to c2 is instance of c1` ). 
    ASSERT iref IS INSTANCE OF intf. 
    out->write( `iref pointing to c2 is instance of intf` ). 
    out->end_section( ). 
 
    out->begin_section( `TYPE REF TO c1` ). 
    c1ref = NEW c1( ). 
    ASSERT c1ref IS NOT INSTANCE OF c2. 
    out->write( `c1ref pointing to c1 is not instance of c2` ). 
    ASSERT c1ref IS INSTANCE OF c1. 
    out->write( `c1ref pointing to c1 is instance of c1` ). 
    ASSERT c1ref IS INSTANCE OF intf. 
    out->write( `c1ref pointing to c1 is instance of intf` ). 
    c1ref = NEW c2( ). 
    ASSERT c1ref IS INSTANCE OF c2. 
    out->write( `c1ref pointing to c2 is instance of c2` ). 
    ASSERT c1ref IS INSTANCE OF c1. 
    out->write( `c1ref pointing to c2 is instance of c1` ). 
    ASSERT c1ref IS INSTANCE OF intf. 
    out->write( `c1ref pointing to c2 is instance of intf` ). 
    out->end_section( ). 
 
    out->begin_section( `TYPE REF TO c2` ). 
    c2ref = NEW c2( ). 
    ASSERT c2ref IS INSTANCE OF c2. 
    out->write( `c2ref pointing to c2 is instance of c2` ). 
    ASSERT c2ref IS INSTANCE OF c1. 
    out->write( `c2ref pointing to c2 is instance of c1` ). 
    ASSERT c2ref IS INSTANCE OF intf. 
    out->write( `c2ref pointing to c2 is instance of intf` ). 
    out->end_section( ). 
 
    out->next_section( `Reference Variable Initial` ). 
 
    out->begin_section( `TYPE REF TO object` ). 
    ASSIGN oref TO <fs>. 
    CLEAR <fs>. 
    ASSERT <fs> IS NOT INSTANCE OF c1. 
    out->write( `oref pointing to nothing is not instance of c1` ). 
    ASSERT <fs> IS NOT INSTANCE OF c2. 
    out->write( `oref pointing to nothing is not instance of c2` ). 
    ASSERT <fs> IS NOT INSTANCE OF intf. 
    out->write( `oref pointing to nothing is not instance of intf` ). 
    out->end_section( ). 
 
    out->begin_section( `TYPE REF TO intf` ). 
    ASSIGN iref TO <fs>. 
    CLEAR <fs>. 
    ASSERT <fs> IS NOT INSTANCE OF c1. 
    out->write( `iref pointing to nothing is not instance of c1` ). 
    ASSERT <fs> IS NOT INSTANCE OF c2. 
    out->write( `iref pointing to nothing is not instance of c2` ). 
    ASSERT <fs> IS INSTANCE OF intf. 
    out->write( `iref pointing to nothing is instance of intf` ). 
    out->end_section( ). 
 
    out->begin_section( `TYPE REF TO c1` ). 
    ASSIGN c1ref TO <fs>. 
    CLEAR <fs>. 
    ASSERT <fs> IS INSTANCE OF c1. 
    out->write( `c1ref pointing to nothing is instance of c1` ). 
    ASSERT <fs> IS NOT INSTANCE OF c2. 
    out->write( `c1ref pointing to nothing is not instance of c2` ). 
    ASSERT <fs> IS INSTANCE OF intf. 
    out->write( `c1ref pointing to nothing is instance of intf` ). 
    out->end_section( ). 
 
    out->begin_section( `TYPE REF TO c2` ). 
    ASSIGN c2ref TO <fs>. 
    CLEAR <fs>. 
    ASSERT <fs> IS INSTANCE OF c1. 
    out->write( `c2ref pointing to nothing is instance of c1` ). 
    ASSERT <fs> IS INSTANCE OF c2. 
    out->write( `c2ref pointing to nothing is instance of c2` ). 
    ASSERT <fs> IS INSTANCE OF intf. 
    out->write( `c2ref pointing to nothing is instance of intf` ). 
    out->end_section( ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A class `c1` contains the interface `intf` and is the superclass of a class `c2`. For reference variables of the static types `object`, `intf`, `c1`, and `c2`, this example demonstrates the behavior of the predicate expression [`IS INSTANCE OF`](abenlogexp_instance_of.md) if these variables point to instances of `c1` or `c2` or are initial.

If the object reference variable is non-initial, the predicate expression is always true if a [downcast](../../abap-glossary/abendown_cast_glosry.md) to the comparison type is possible. If the object reference variable is initial, the predicate expression is true only if an [upcast](../../abap-glossary/abenup_cast_glosry.md) is possible. This example checks a generically typed field symbol for which this can only be determined at runtime.

For an initial reference variable with the static type `object`, the result of the expression for all comparison types except for `object` is false. For an initial reference variable with the static type `intf`, the result of the expression for all comparison types except for the interface `intf` is itself false.
