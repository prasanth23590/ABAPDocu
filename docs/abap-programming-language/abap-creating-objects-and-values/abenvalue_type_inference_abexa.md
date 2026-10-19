---
title: "Value Operator, Type Inference"
source_file: abenvalue_type_inference_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator > VALUE, Initial Value for All Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Value Operator, Type Inference

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a type inference for the value operator [`VALUE`](abenconstructor_expression_value.md).

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
CLASS cl_demo_value_type_inference DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES c10 TYPE c LENGTH 10. 
    METHODS: 
      meth1 IMPORTING p TYPE c10, 
      meth2 IMPORTING p TYPE c, 
      meth3 IMPORTING p TYPE csequence, 
      descr IMPORTING p TYPE any. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_value_type_inference IMPLEMENTATION. 
  METHOD main. 
 
    me->meth1( p = VALUE #(  ) ). 
    out->line( ). 
 
    "me->meth2( p = value #(  ) ). 
    "not possible 
 
    out->line( ). 
 
    me->meth3( p = VALUE #(  ) ) ##type. 
  ENDMETHOD. 
  METHOD descr. 
    DATA type   TYPE string. 
    DATA length TYPE i. 
 
    DATA(datadescr) = CAST cl_abap_datadescr( 
        cl_abap_typedescr=>describe_by_data( p ) ). 
 
    type = datadescr->type_kind. 
    IF type = 'g'. 
      type = 'STRING'. 
      length = strlen( p ). 
    ELSE. 
      length = datadescr->length / cl_abap_char_utilities=>charsize. 
    ENDIF. 
    out->write( |{ type } { length }| ). 
  ENDMETHOD. 
  METHOD meth1. 
    descr( p ). 
  ENDMETHOD. 
  METHOD meth2. 
    descr( p ). 
  ENDMETHOD. 
  METHOD meth3. 
    descr( p ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Constructor expressions with the value operator [`VALUE`](abenvalue_constructor_params_init.md) for initial values are passed to differently typed formal parameters of methods.

- Completely typed formal parameter

  When the method `meth1` is called with a completely typed formal parameter, the operand type for `#` is determined using this parameter and the result of the value operator is an initial field of type `c` with length 10.

- Formal parameter typed generically with `c`

  No call is possible here, since there is no inference rule for the generic type `c`.

- Formal parameter typed generically with `csequence`

  In accordance with the inference rule for `csequence`, the result of the value operator is an initial field of type `string`, which is indicated by a syntax check warning.
