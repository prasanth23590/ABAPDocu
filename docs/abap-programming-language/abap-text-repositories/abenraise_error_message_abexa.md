---
title: "Messages - IF_T100_DYN_MSG for Exception error_message"
source_file: abenraise_error_message_abexa.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > Messages - System Interfaces > Messages - System Interface IF_T100_DYN_MSG"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages - IF_T100_DYN_MSG for Exception error_message

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a caught message of a function module is forwarded.

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
CLASS cl_demo_raise_error_message DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_raise_error_message IMPLEMENTATION. 
  METHOD main. 
    TRY. 
        CALL FUNCTION 'DEMO_FUNCTION_MESSAGE' 
          EXPORTING 
            message_type  = 'A' 
            message_place = 'in Function Module' 
            message_event = 'Method MAIN' 
          EXCEPTIONS 
            error_message = 4. 
        IF sy-subrc <> 0. 
          RAISE EXCEPTION TYPE cx_demo_dyn_t100 
            MESSAGE ID sy-msgid 
            TYPE sy-msgty 
            NUMBER sy-msgno 
            WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4. 
        ENDIF. 
      CATCH cx_demo_dyn_t100 INTO FINAL(oref). 
        out->write( 
          |Caught exception:\n\n| && 
          |"{ oref->get_text( ) }", Type { oref->msgty } | ). 
        "MESSAGE oref TYPE 'I' DISPLAY LIKE oref->msgty. 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in basically the same way as the executable example for transforming a classic exception raised using `MESSAGE RAISING` to a class-based exception. Here, however, a message of type A caught using [`error_message`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md) is transformed.

## Hint

See also the executable [example](../abap-program-flow-logic/abenraise_error_message_shrt_abexa.md) for using a short form of statement [`RAISE EXCEPTION MESSAGE`](../abap-program-flow-logic/abapraise_exception_message.md).
