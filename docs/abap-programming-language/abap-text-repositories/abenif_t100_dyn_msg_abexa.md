---
title: "Messages - IF_T100_DYN_MSG in a Regular Class"
source_file: abenif_t100_dyn_msg_abexa.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > Messages - System Interfaces > Messages - System Interface IF_T100_DYN_MSG"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages - IF_T100_DYN_MSG in a Regular Class

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a regular class is linked with a message

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
CLASS cl_demo_if_t100_dyn_msg DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS msg DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES if_t100_dyn_msg. 
    ALIASES: msgty FOR if_t100_dyn_msg~msgty, 
    get_text FOR if_message~get_text, 
    get_longtext FOR if_message~get_longtext. 
    METHODS constructor IMPORTING id TYPE symsgid 
    no TYPE symsgno 
    ty TYPE symsgty 
    v1 TYPE string OPTIONAL 
    v2 TYPE string OPTIONAL 
    v3 TYPE string OPTIONAL 
    v4 TYPE string OPTIONAL. 
ENDCLASS. 
 
CLASS msg IMPLEMENTATION. 
  METHOD constructor. 
    if_t100_message~t100key-msgid = id. 
    if_t100_message~t100key-msgno = no. 
    if_t100_dyn_msg~msgty = ty. 
    if_t100_message~t100key-attr1 = 'IF_T100_DYN_MSG~MSGV1'. 
    if_t100_message~t100key-attr2 = 'IF_T100_DYN_MSG~MSGV2'. 
    if_t100_message~t100key-attr3 = 'IF_T100_DYN_MSG~MSGV3'. 
    if_t100_message~t100key-attr4 = 'IF_T100_DYN_MSG~MSGV4'. 
    if_t100_dyn_msg~msgv1 = v1. 
    if_t100_dyn_msg~msgv2 = v2. 
    if_t100_dyn_msg~msgv3 = v3. 
    if_t100_dyn_msg~msgv4 = v4. 
  ENDMETHOD. 
  METHOD if_message~get_text. 
    result = cl_message_helper=>get_text_for_message( me ). 
  ENDMETHOD. 
  METHOD if_message~get_longtext. 
    result = cl_message_helper=>get_longtext_for_message( me ). 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_if_t100_dyn_msg IMPLEMENTATION. 
  METHOD main. 
    DATA(id) = `SABAPDEMOS`. 
    DATA(no) = `104`. 
    DATA(ty) = `I`. 
    DATA(v1) = `Hello,`. 
    DATA(v2) = `I am`. 
    DATA(v3) = `a`. 
    DATA(v4) = `Message!`. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = id 
      )->add_field( CHANGING field = no 
      )->add_field( CHANGING field = ty 
      )->add_field( CHANGING field = v1 
      )->add_field( CHANGING field = v2 
      )->add_field( CHANGING field = v3 
      )->add_field( CHANGING field = v4 
      )->request( ). 
    IF strlen( ty ) > 1 OR 'AEISX' NS ty. 
      out->write( 
        |Invalid message type: { ty }|  ). 
      RETURN. 
    ENDIF. 
 
    FINAL(mref) = NEW msg( id = CONV #( id ) 
                           no = CONV #( no ) 
                           ty = CONV #( ty ) 
                           v1 = v1 
                           v2 = v2 
                           v3 = v3 
                           v4 = v4 ). 
 
    out->write( 
      |{ mref->get_text( ) }, Type: { mref->msgty }| ). 
 
    "MESSAGE mref TYPE 'I' DISPLAY LIKE mref->msgty. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example applies the [executable example](abenif_t100_message_abexa.md) for the interface `IF_T100_MESSAGE` to the interface `IF_T100_DYN_MSG` directly. If `IF_T100_DYN_MSG` is used, it is no longer necessary to create separate attributes for the placeholders of the message. The attributes of the interface are used instead. Furthermore, the message type can be stored and evaluated in the interface attribute `msgty`. If `IF_T100_MESSAGE` is used, a separate attribute must be declared here. The attribute can then be used in the `MESSAGE` statement in ABAP language versions where that syntax is allowed.
