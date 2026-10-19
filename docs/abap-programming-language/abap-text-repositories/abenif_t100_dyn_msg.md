---
title: "Messages - System Interface IF_T100_DYN_MSG"
source_file: abenif_t100_dyn_msg.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > Messages - System Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages - System Interface IF_T100_DYN_MSG

The interface `IF_T100_DYN_MSG` contains the interface [`IF_T100_MESSAGE`](abenif_t100_message.md) as a component interface and adds the following to it:

- The attribute `MSGTY` for the message type

- The attributes `MSGV1` to `MSGV4` for the placeholders of the message

Like `IF_T100_MESSAGE`, the interface `IF_T100_DYN_MSG` associates classes with messages, whereby the attributes for the message type and placeholders of the message are already predefined.

## Hints

- The interface `IF_T100_DYN_MSG` is designed specifically for raising class-based exceptions with the addition [`MESSAGE`](../abap-program-flow-logic/abapraise_exception_message.md) of the statement [`RAISE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md) or the addition [`THROW`](../abap-program-flow-logic/abenconditional_expression_result.md) in [conditional expressions](../abap-program-flow-logic/abenconditional_expressions.md). The properties of the message specified after `MESSAGE` are assigned automatically to the associated attributes in [exception classes](../abap-program-flow-logic/abenexceptions_classes.md) that include `IF_T100_DYN_MSG`.

- The addition [`MESSAGE`](../abap-program-flow-logic/abapraise_exception_message.md) of `RAISE EXCEPTION` and/or `THROW` has a short form `USING MESSAGE`. This can be used for exception classes with the interface `IF_T100_DYN_MSG` and enables determining the message from the current content of the system fields `sy-msg...`. The short form can be used particularly for converting classical exceptions to class-based exceptions.

- If the object reference variable `oref` points to an object that includes the system interface `IF_T100_DYN_MSG` in the variant [`MESSAGE oref`](abapmessage_msg.md) of the statement [`MESSAGE`](abapmessage.md), the addition `TYPE` can be omitted and the message type from the interface attribute `MSGTY` of the object is used implicitly.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

[`THROW`](../abap-program-flow-logic/abenconditional_expression_result.md) is used to raise an exception of the class `CX_DEMO_DYN_T100`, which implements the interface `IF_T100_DYN_MSG`.

``` abap
DATA col TYPE c LENGTH 1. 
 
... 
 
TRY. 
    FINAL(color) = COND string( 
                    WHEN col = 'R' THEN 'red' 
                    WHEN col = 'B' THEN 'blue' 
                    WHEN col = 'G' THEN 'green' 
                    ELSE THROW cx_demo_dyn_t100( 
                         MESSAGE e888(sabapdemos) 
                           WITH 'Illegal value:' col ) ). 
  CATCH cx_demo_dyn_t100. 
    ... 
ENDTRY.
```

## Executable Examples

- [System Interface `IF_T100_DYN_MSG` in a Regular Class](abenif_t100_dyn_msg_abexa.md)

- [System Interface `IF_T100_DYN_MSG` in a Local Exception Class](abenraise_message_abexa.md)

- [System Interface `IF_T100_DYN_MSG` for Exception `error_message`](abenraise_error_message_abexa.md)
