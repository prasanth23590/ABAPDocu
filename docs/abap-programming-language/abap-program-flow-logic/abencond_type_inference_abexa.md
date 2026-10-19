---
title: "Conditional Operator, Type Inference"
source_file: abencond_type_inference_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Conditional Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conditional Operator, Type Inference

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a type inference for the conversion operator [`COND`](abenconditional_expression_cond.md).

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
CLASS cl_demo_cond_type_inference DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: 
      c10 TYPE c LENGTH 10 . 
    METHODS meth1 
      IMPORTING 
        !p TYPE c10 . 
    METHODS meth2 
      IMPORTING 
        !p TYPE c . 
    METHODS meth3 
      IMPORTING 
        !p TYPE csequence . 
    METHODS descr 
      IMPORTING 
        !p TYPE any . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cond_type_inference IMPLEMENTATION. 
  METHOD main. 
    FIELD-SYMBOLS <fs> TYPE any. 
    DATA txt TYPE c LENGTH 20. 
    DATA num TYPE i. 
    ASSIGN num TO <fs>. 
 
    me->meth1( 
          p = COND #( WHEN 1 = 1 THEN txt ) ). 
    me->meth1( 
          p = COND #( WHEN 1 = 1 THEN txt ) ). 
    me->meth1( 
          p = COND #( WHEN 1 = 1 THEN <fs> ) ). 
    out->line( ). 
 
    me->meth2( 
          p = COND #( WHEN 1 = 1 THEN txt ) ). 
    "me->meth2( 
    "     p = COND #( WHEN 1 = 1 THEN num ) ).  "not possible 
    "me->meth2( 
    "     p = COND #( WHEN 1 = 1 THEN <fs> ) ). "not possible 
    out->line( ). 
 
    me->meth3( 
          p = COND #( WHEN 1 = 1 THEN txt ) ). 
    me->meth3( 
          p = COND #( WHEN 1 = 1 THEN num ) )  ##type. 
    me->meth3( 
          p = COND #( WHEN 1 = 1 THEN <fs> ) ) ##type. 
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

Constructor expressions with the conditional operator [`COND`](abenconditional_expression_cond.md) are passed to differently typed formal parameters of methods. In the case of generic formal parameters, [special rules](abencond_constructor_inference.md) apply when determining the operand type. Replacing the conditional operator `COND` with [`SWITCH`](abenconditional_expression_switch.md) produces the same results.

- Completely typed formal parameter

  When the method `meth1` is called with a completely typed formal parameter, the operand type for `#` is determined using this parameter and the result of the conditional expression is converted to `c` with length 10 in all three calls.

- Formal parameter typed generically with `c`

  The operand type for `#` is determined from the data type of the operand after `THEN`.

  - In the first call, the type `c` with length 20 of the operand after `THEN` matches the generic type and is used.

  - In the second call, the type `i` of the operand after `THEN` does not match the generic type and the call is not possible.

  - In the third call, no type can be derived from the generically typed field symbol `<fs>` after `THEN`. No call is possible here, since there is no inference rule for the generic type `c`.

- Formal parameter typed generically with `csequence`

  - In the first call, the type `c` with length 20 of the operand after `THEN` matches the generic type and is used.

  - In the second call, the type `i` of the operand after `THEN` does not match the generic type and the type `string` is used, which is indicated by a syntax check warning.

  - In the third call, no type is derived from the generically typed field symbol `<fs>` after `THEN` and the type `string` is used, which is indicated by a syntax check warning.
