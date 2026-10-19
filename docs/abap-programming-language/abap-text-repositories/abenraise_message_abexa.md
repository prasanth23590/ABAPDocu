---
title: "Messages - IF_T100_DYN_MSG in a Local Exception Class"
source_file: abenraise_message_abexa.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > Messages - System Interfaces > Messages - System Interface IF_T100_DYN_MSG"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages - IF_T100_DYN_MSG in a Local Exception Class

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a local exception class is linked with a message

## Source Code

``` abap
* CCDEF 
CLASS cx_dyn_t100 DEFINITION INHERITING FROM cx_dynamic_check. 
  PUBLIC SECTION. 
    INTERFACES if_t100_dyn_msg. 
    ALIASES msgty FOR if_t100_dyn_msg~msgty. 
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
CLASS cl_demo_raise_msg DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS meth 
      RAISING cx_dyn_t100. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_raise_msg IMPLEMENTATION. 
  METHOD main. 
    TRY. 
        meth( ). 
      CATCH cx_dyn_t100 INTO FINAL(oref). 
        out->write( 
          |Caught exception:\n\n| && 
          |"{ oref->get_text( ) }", Type { oref->msgty } | ). 
        "MESSAGE oref TYPE oref->msgty. 
    ENDTRY. 
  ENDMETHOD. 
  METHOD meth. 
    RAISE EXCEPTION TYPE cx_dyn_t100 
          MESSAGE e104(sabapdemos) WITH 'I' 'am' 'an' 'Exception!'. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example applies the [executable example](abenmessage_interface_abexa.md) for the interface `IF_T100_MESSAGE` directly to the interface `IF_T100_DYN_MSG`. The local class `cx_dyn_t100` implements the interface [`IF_T100_DYN_MSG`](abenif_t100_dyn_msg.md) and the addition [`MESSAGE`](../abap-program-flow-logic/abapraise_exception_message.md) of the statement [`RAISE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md) is used to raise the exception in the method `meth`.

Unlike when using [`IF_T100_MESSAGE`](abenif_t100_message.md), no separate attributes for the placeholders of the message and no implementation of the instance constructor are required in `cx_dyn_t100`. Furthermore, the message type is passed in an attribute of the exception object when `IF_T100_DYN_MSG` is used. An alias name is introduced for this attribute here.
