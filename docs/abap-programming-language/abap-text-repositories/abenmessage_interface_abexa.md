---
title: "Messages - IF_T100_MESSAGE in a Local Exception Class"
source_file: abenmessage_interface_abexa.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > Messages - System Interfaces > Messages - System Interface IF_T100_MESSAGE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages - IF_T100_MESSAGE in a Local Exception Class

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a local exception class is linked with a message

## Source Code

``` abap
* CCDEF 
CLASS cx_t100 DEFINITION INHERITING FROM cx_dynamic_check. 
  PUBLIC SECTION. 
    INTERFACES if_t100_message. 
    METHODS constructor IMPORTING id TYPE symsgid 
    no TYPE symsgno 
    text1 TYPE csequence OPTIONAL 
    text2 TYPE csequence OPTIONAL 
    text3 TYPE csequence OPTIONAL 
    text4 TYPE csequence OPTIONAL. 
    DATA text1 TYPE c LENGTH 50. 
    DATA text2 TYPE c LENGTH 50. 
    DATA text3 TYPE c LENGTH 50. 
    DATA text4 TYPE c LENGTH 50. 
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
CLASS cl_demo_message_oref DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS meth 
      RAISING cx_t100. 
ENDCLASS. 
 
* CCIMP 
CLASS cx_t100 IMPLEMENTATION. 
  METHOD constructor. 
    super->constructor( ). 
    me->text1 = text1. 
    me->text2 = text2. 
    me->text3 = text3. 
    me->text4 = text4. 
    if_t100_message~t100key-msgid = id. 
    if_t100_message~t100key-msgno = no. 
    if_t100_message~t100key-attr1 = 'TEXT1'. 
    if_t100_message~t100key-attr2 = 'TEXT2'. 
    if_t100_message~t100key-attr3 = 'TEXT3'. 
    if_t100_message~t100key-attr4 = 'TEXT4'. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_message_oref IMPLEMENTATION. 
  METHOD main. 
    TRY. 
        meth( ). 
      CATCH cx_t100 INTO FINAL(oref). 
        out->write( oref->get_text( ) ). 
        "MESSAGE oref TYPE 'I' DISPLAY LIKE 'E'. 
    ENDTRY. 
  ENDMETHOD. 
  METHOD meth. 
    RAISE EXCEPTION TYPE cx_t100 
      EXPORTING 
        id    = 'SABAPDEMOS' 
        no    = '104' 
        text1 = 'I' 
        text2 = 'am' 
        text3 = 'an' 
        text4 = 'Exception!'. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The functional method `meth` raises an exception from the local exception class `cx_t100` that implements the interface [`IF_T100_MESSAGE`](abenif_t100_message.md). When the exception is raised, the constructor is given a message class, a message number, and values for the placeholders of the message.

The constructor of the local exception class `cx_t100` fills the attribute `T100KEY` of the interface `IF_T100_MESSAGE` with the values passed. In this way, the exception class represents the passed message from the table `T100` in which the placeholders *&* are replaced with the content of the attributes `text1` to `text4`.

The method `main` catches the exception in the reference variable `oref` and indicates the following:

- The exception text can be obtained using the method `GET_TEXT` of the component interface `IF_MESSAGE` in the interface `IF_T100_MESSAGE`. The implementation of the method `GET_TEXT` is in the superclass `CX_ROOT`, which already includes the interface `IF_MESSAGE`.

- The reference variable can be used directly as an operand of the statement [`MESSAGE`](abapmessage.md) in ABAP language versions where that syntax is allowed.

See also the executable examples listed below.

- [System Interface `IF_T100_DYN_MSG` in Local Exception Class](abenraise_message_abexa.md)
