---
title: "MESSAGE, INTO"
source_file: abapmessage_into.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > MESSAGE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MESSAGE, INTO

## Syntax

``` abap
MESSAGE msg [WITH dobj1 ... dobj4] 
        INTO text.  
```

[`msg`](abapmessage_msg.md) · [`[WITH dobj1 ... dobj4]`](abapmessage.md)

## Description

The statement [`MESSAGE`](abapmessage.md) with the addition `INTO` assigns the short text of the message to the target field `text`. The [message type](../../abap-glossary/abenmessage_type_glosry.md) is irrelevant. The program flow is not interrupted and no message processing takes place. The following can be specified for `text`:

- An existing character-like variable.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where a variable of type `string` is declared.

The addition `INTO` cannot be specified when a text `text` is specified or when an object reference variable is specified in `msg`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The short text of a message sent in a function module is assigned to the data object `mtext` declared inline when handling the exception [`error_message`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md) using the corresponding system fields.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
CALL FUNCTION 'DEMO_FUNCTION_ERROR_MESSAGE' 
  EXCEPTIONS 
    error_message = 4. 
IF sy-subrc = 4. 
  MESSAGE ID sy-msgid TYPE sy-msgty NUMBER sy-msgno 
          INTO FINAL(mtext) 
          WITH sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4. 
  out->write( mtext ). 
ENDIF. 
 
out->display( ).
```
