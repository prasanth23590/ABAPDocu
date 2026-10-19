---
title: "Messages - IF_T100_MESSAGE in a Regular Class"
source_file: abenif_t100_message_abexa.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > Messages - System Interfaces > Messages - System Interface IF_T100_MESSAGE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages - IF_T100_MESSAGE in a Regular Class

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
CLASS cl_demo_if_t100_message DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS msg DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES if_t100_message. 
    ALIASES: get_text FOR if_message~get_text, 
    get_longtext FOR if_message~get_longtext. 
    METHODS constructor IMPORTING id TYPE symsgid 
    no TYPE symsgno 
    v1 TYPE string OPTIONAL 
    v2 TYPE string OPTIONAL 
    v3 TYPE string OPTIONAL 
    v4 TYPE string OPTIONAL. 
    DATA: attr1 TYPE c LENGTH 50, 
    attr2 TYPE c LENGTH 50, 
    attr3 TYPE c LENGTH 50, 
    attr4 TYPE c LENGTH 50. 
ENDCLASS. 
 
CLASS msg IMPLEMENTATION. 
  METHOD constructor. 
    if_t100_message~t100key-msgid = id. 
    if_t100_message~t100key-msgno = no. 
    if_t100_message~t100key-attr1 = 'ATTR1'. 
    if_t100_message~t100key-attr2 = 'ATTR2'. 
    if_t100_message~t100key-attr3 = 'ATTR3'. 
    if_t100_message~t100key-attr4 = 'ATTR4'. 
    attr1 = v1. 
    attr2 = v2. 
    attr3 = v3. 
    attr4 = v4. 
  ENDMETHOD. 
  METHOD if_message~get_text. 
    result = cl_message_helper=>get_text_for_message( me ). 
  ENDMETHOD. 
  METHOD if_message~get_longtext. 
    result = cl_message_helper=>get_longtext_for_message( me ). 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_if_t100_message IMPLEMENTATION. 
  METHOD main. 
    DATA(id) = `SABAPDEMOS`. 
    DATA(no) = `104`. 
    DATA(v1) = `Hello,`. 
    DATA(v2) = `I am`. 
    DATA(v3) = `a`. 
    DATA(v4) = `Message!`. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = id 
      )->add_field( CHANGING field = no 
      )->add_field( CHANGING field = v1 
      )->add_field( CHANGING field = v2 
      )->add_field( CHANGING field = v3 
      )->add_field( CHANGING field = v4 
      )->request( ). 
 
    FINAL(mref) = NEW msg( id = CONV #( id ) 
                          no = CONV #( no ) 
                          v1 = v1 
                          v2 = v2 
                          v3 = v3 
                          v4 = v4 ). 
 
    out->write( mref->get_text( ) ). 
 
    "MESSAGE mref TYPE 'I'. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Objects in the example class `msg` shown here can represent any messages from the table `T100` and can be used in the statement [`MESSAGE`](abapmessage.md). There are four attributes `ATTR1` to `ATTR4` for the content of four placeholders. The constructor provides input parameters for all necessary values. In the constructor, the message class and the message number are written directly to the associated components of the interface structure `T100KEY`. The identically named attributes are assigned to the components `ATTR1` to `ATTR4` and filled with the passed values.

After the class is instantiated, the message text is obtained using the interface method `GET_TEXT`, which is implemented appropriately in the class and for which an alias name is declared. The object of the class can be used directly as an operand of the statement [`MESSAGE`](abapmessage.md) in ABAP language versions where that syntax is allowed. The message type is not stored as an attribute of the class but must be specified in the calling method.

## Hint

See also the executable example [System Interface `IF_T100_DYN_MSG` in Regular Class](abenif_t100_dyn_msg_abexa.md).
