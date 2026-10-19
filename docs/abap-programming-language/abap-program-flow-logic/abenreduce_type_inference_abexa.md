---
title: "Reduce Operator, Type Inference"
source_file: abenreduce_type_inference_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions > REDUCE, Reduction Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Reduce Operator, Type Inference

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a type inference for the conversion operator [`REDUCE`](abenconstructor_expression_reduce.md).

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
CLASS cl_demo_reduce_type_inference DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    TYPES c10 TYPE c LENGTH 10. 
    METHODS: 
      meth1 IMPORTING p TYPE c10, 
      meth2 IMPORTING p TYPE c, 
      meth3 IMPORTING p TYPE csequence, 
      descr IMPORTING p TYPE any. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_reduce_type_inference IMPLEMENTATION. 
  METHOD main. 
 
    DATA txt TYPE c LENGTH 20. 
    DATA num TYPE i. 
 
    me->meth1( 
                 p = REDUCE #( INIT r1 = txt 
                               FOR i = 1 
                               UNTIL i > 9 
                               NEXT r1 &&= 'x' ) ). 
    me->meth1( 
                 p = REDUCE #( INIT r2 = num 
                               FOR i = 1 
                               UNTIL i > 9 
                               NEXT r2 += 1 ) ). 
    out->line( ). 
 
    me->meth2( 
                 p = REDUCE #( INIT r1 = txt 
                               FOR i = 1 
                               UNTIL i > 9 
                               NEXT r1 &&= 'x' ) ). 
    "me->meth2( 
    "             p = REDUCE #( INIT r2 = num 
    "                           FOR i = 1 
    "                           UNTIL i > 9 
    "                           NEXT r2 +=+ 1 ) ). "not possible 
    out->line( ). 
 
    me->meth3( 
                 p = REDUCE #( INIT r1 = txt 
                               FOR i = 1 
                               UNTIL i > 9 
                               NEXT r1 &&= 'x' ) ). 
    me->meth3( 
                 p = REDUCE #( INIT r2 = num 
                               FOR i = 1 
                               UNTIL i > 9 
                               NEXT r2 += 1 ) ) ##type. 
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

Constructor expressions with the conversion operator [`REDUCE`](abenconstructor_expression_reduce.md) are passed to differently typed formal parameters of methods. In the case of generic formal parameters, [special rules](abenreduce_constructor_inference.md) apply when determining the operand type.

- Completely typed formal parameter

  When the method `meth1` is called with a completely typed formal parameter, the operand type for `#` is determined by this parameter and the result of the reduction is converted to `c` with length 10 in both calls.

- Formal parameter typed generically with `c`

  The operand type for `#` is determined by the first declaration after `INIT`.

  - In the first call, the type `c` with length 20 of the declaration after `INIT` matches the generic type and is used.

  - It is not possible to perform a call with the type `i` of the declaration after `INIT`, since it does not match the typing and there are no inference rules for the generic type `c`.

- Formal parameter typed generically with `csequence`

  - In the first call, the type `c` with length 20 of the declaration after `INIT` matches the generic type and is used.

  - In the second call, the type `i` of the declaration after `INIT` does not match the generic type and the type `string` is used, which is indicated by a syntax check warning.
