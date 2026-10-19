---
title: "Converting the Exception error_message to a Class-Based Exception"
source_file: abenraise_error_message_shrt_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > RAISE EXCEPTION > RAISE EXCEPTION, message"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Converting the Exception error_message to a Class-Based Exception

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the short form of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) with the addition [`MESSAGE`](abapraise_exception_message.md).

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
CLASS cl_demo_raise_error_msg_shrt DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_raise_error_msg_shrt IMPLEMENTATION. 
  METHOD main. 
    TRY. 
        CALL FUNCTION 'DEMO_FUNCTION_MESSAGE' 
          EXPORTING 
            message_type  = 'A' 
            message_place = 'in Function Module' 
            message_event = 'START-OF-SELECTION' 
          EXCEPTIONS 
            error_message = 4. 
        IF sy-subrc <> 0. 
          RAISE EXCEPTION TYPE cx_demo_dyn_t100 USING MESSAGE. 
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

The example has exactly the same functionality as the executable example [`IF_T100_DYN_MSG` for the exception `error_message`](../abap-text-repositories/abenraise_error_message_abexa.md). Here, the addition [`USING MESSAGE`](abapraise_exception_message.md) is used, which explicitly passes the system fields `sy-msgty`, `sy-msgid`, `sy-msgno`, and `sy-msgv1` to `sy-msgv4` to the corresponding additions of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md).
