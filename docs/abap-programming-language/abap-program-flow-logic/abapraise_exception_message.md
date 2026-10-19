---
title: "RAISE EXCEPTION, message"
source_file: abapraise_exception_message.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > RAISE EXCEPTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAISE EXCEPTION, message

## Syntax

``` abap
... { MESSAGE tn(id) 
            | { ID mid TYPE mtype NUMBER num } 
              [WITH dobj1 ... dobj4] } 
  | { USING MESSAGE } ...  
```

### Variant

[1. `... MESSAGE msg ...`](abapraise_exception_message.md#variant-1)

[2. `... USING MESSAGE ...`](abapraise_exception_message.md#variant-2)

## Overview

### Description

The addition `MESSAGE` of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) and of the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md) passes the specification of a [message](../../abap-glossary/abenmessage_glosry.md) to the exception object.

## Variant 1

`... MESSAGE msg ...`

### Description

The addition `tn(id)` or `ID mid TYPE mtype NUMBER num` is used to specify the [message type](../../abap-glossary/abenmessage_type_glosry.md), the [message class](../../abap-glossary/abenmessage_class_glosry.md), and the [message number](../../abap-glossary/abenmessage_number_glosry.md) of a message [`msg`](../abap-text-repositories/abapmessage_msg.md) for the table `T100`, statically or dynamically like in the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md). Also like in [`MESSAGE`](../abap-text-repositories/abapmessage.md), the optional addition `WITH` can be used to provide the placeholders of a message with content. The exception class of the raised exception must implement one of the [system interfaces for messages](../abap-text-repositories/abenmessage_interfaces.md):

- [Using `IF_T100_DYN_MSG`](abapraise_exception_message.md#using-if_t100_dyn_msg)

- [Using `IF_T100_MESSAGE`](abapraise_exception_message.md#using-if_t100_message)

The addition `MESSAGE` fills the attributes of these interfaces with values. This assignment takes place after the instance constructor is executed. This overwrites any values that were assigned to these attributes when the exception object was constructed.

The attributes of the system interfaces are used to link the exception object to the message specified after `MESSAGE`. Using an object reference, the object can be used directly in the variant [`MESSAGE oref`](../abap-text-repositories/abapmessage_msg.md) of the [`MESSAGE` statement](../abap-text-repositories/abapmessage.md) and the message texts can be read using the interface methods.

If the addition `MESSAGE` is used, the input parameter `TEXTID` of the constructor of the exception class must not be filled. This parameter is only intended for specifying a predefined [exception text](abenexception_texts.md).

### Hints

- The addition `MESSAGE` cannot be specified after the variant [`RAISE EXCEPTION oref`](abapraise_exception_class.md).

- The position behind `MESSAGE` is contained in the where-used list for the message specified.

- See also [Exception Classes for Messages](abenmessage_exceptions.md).

## Using `IF_T100_DYN_MSG`

The full functionality of the addition `MESSAGE` is available only if the system interface [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md) is implemented in the used exception class. This interface includes the system interface [`IF_T100_MESSAGE`](../abap-text-repositories/abenif_t100_message.md) requested by the syntax check. If an exception class is used with the system interface `IF_T100_DYN_MSG`, the addition `MESSAGE` fills its attributes as follows after the instance constructor is executed:

- The message type specified after `MESSAGE` is assigned to the attribute `MSGTY` of the interface `IF_T100_DYN_MSG`.

- The components of the structured attribute `T100KEY` of the component interface `IF_T100_MESSAGE` are filled as follows:

  - `MSGID` is assigned the message class specified after `MESSAGE`.

  - `MSGNO` is assigned the message number specified after `MESSAGE`.

  - `ATTR1` to `ATTR4` are assigned the names `IF_T100_DYN_MSG~MSGV1` to `IF_T100_DYN_MSG~MSGV4` of the interface attributes for the placeholders of the message. If the addition `WITH` is not specified, `ATTR1` to `ATTR4` remain initial.

- The attributes `MSGV1` to `MSGV4` of the interface `IF_T100_DYN_MSG` are assigned the texts specified using `WITH`.

### Hints

- If `IF_T100_DYN_MSG` is used, the addition `MESSAGE` assigns the correct values to all required attributes of the exception class to link them to the message. More specifically, the attributes for the placeholders of the message are mapped to the structure `T100KEY` of the interface `IF_T100_MESSAGE` automatically.

- In exception classes with the interface `IF_T100_DYN_MSG`, `MESSAGE` used together with the `EXPORTING` addition can produce unexpected results in the placeholder texts if the addition `WITH` is not specified. Implicit assignments of the input parameters specified after `EXPORTING` to the components `ATTR1` to `ATTR4` are intended for exception classes with the interface `IF_T100_MESSAGE` where `WITH` cannot be specified. Implicit assignments of the names of the input parameters or of initial values can be prevented by specifying `WITH` with a dummy value `space`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of the exception `CX_DEMO_DYN_T100` that implements the interface `IF_T100_DYN_MSG`. The addition `MESSAGE` is used to pass the properties of a message that determines the exception text.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TRY. 
    RAISE EXCEPTION TYPE cx_demo_dyn_t100 
      MESSAGE ID 'SABAPDEMOS' 
      TYPE 'I' 
      NUMBER '888' 
      WITH 'Message'. 
  CATCH cx_demo_dyn_t100 INTO FINAL(oref). 
    out->write( oref->get_text( ) && 
                `, ` && oref->msgty ). 
ENDTRY. 
 
out->display( ).
```

## Executable Examples

- [System Interface `IF_T100_DYN_MSG` in a Local Exception Class](../abap-text-repositories/abenraise_message_abexa.md)

- [System Interface `IF_T100_DYN_MSG` for Exception `error_message`](../abap-text-repositories/abenraise_error_message_abexa.md)

## Using `IF_T100_MESSAGE`

If only the system interface [`IF_T100_MESSAGE`](../abap-text-repositories/abenif_t100_message.md) is implemented, the addition `WITH` must not be used and only a restricted set of functions is available. When an exception class is used that implements only the system interface `IF_T100_MESSAGE`, the addition `MESSAGE` fills its attributes as follows after the instance constructor is executed:

- The specification of a message type has no effect.

- The components of the structured attribute `T100KEY` of the component interface `IF_T100_MESSAGE` are filled as follows:

  - `MSGID` is assigned the message class specified after `MESSAGE`.

  - `MSGNO` is assigned the message number specified after `MESSAGE`.

  - `ATTR1` to `ATTR4` are assigned the names of the first four input parameters of the instance constructors specified after `EXPORTING` that can be converted to a character-like target field, in the specified order. Components that cannot be assigned input parameters are initialized.

### Hints

- It is recommended that the system interface [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md) is used for exceptions raised using the addition `MESSAGE`.

- The use of the addition `MESSAGE` for an exception class with [`IF_T100_MESSAGE`](../abap-text-repositories/abenif_t100_message.md) is intended for cases where existing exception classes that cannot be switched to [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md) must be used.

- The addition `MESSAGE` is suitable for existing exception classes with [`IF_T100_MESSAGE`](../abap-text-repositories/abenif_t100_message.md) that already have a generic [exception text](abenexception_texts.md) without semantic meaning. Previously, structures of the type `SCX_T100KEY`, filled in the program, had to be passed to such exceptions.

- The use of the addition `MESSAGE` is not recommended for an exception class with [`IF_T100_MESSAGE`](../abap-text-repositories/abenif_t100_message.md) whose exception texts all have a fixed semantic meaning.

### Executable Example

System Interface `IF_T100_MESSAGE` for Exception with Message

## Variant 2

`... USING MESSAGE ...`

### Description

This variant is a short form of the preceding variant of the `MESSAGE` addition. It can be used if the exception class of the raised exception implements the [system interface](../abap-text-repositories/abenmessage_interfaces.md) [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md), and has the following effect:

``` abap
... MESSAGE ID     sy-msgid 
            TYPE   sy-msgty 
            NUMBER sy-msgno 
            WITH   sy-msgv1 sy-msgv2 sy-msgv3 sy-msgv4 ...
```

The addition `USING MESSAGE` implicitly passes the specification of the message that is stored during the execution of the statement in the system fields `sy-msgid`, `sy-msgty` `sy-msgno`, and `sy-msgv1` to `sy-msgv4` to the exception class.

### Hint

The short form is particularly suitable for converting classic exceptions that were raised in function modules or methods with the statement [`MESSAGE RAISING`](abapmessage_raising.md), or messages that were caught with [`error_message`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md), into class-based exceptions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of the exception `CX_DEMO_DYN_T100` that implements the interface `IF_T100_DYN_MSG`. The addition `USING MESSAGE` implicitly passes the properties of a [status message](../../abap-glossary/abenstatus_message_glosry.md) that was previously output with the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md). In the restricted language scope, the message needs to be written in a string `msg`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
MESSAGE ID 'SABAPDEMOS' TYPE 'S' 
        NUMBER '888' 
        WITH 'Message' 
        INTO FINAL(msg). 
TRY. 
    RAISE EXCEPTION TYPE cx_demo_dyn_t100 USING MESSAGE. 
  CATCH cx_demo_dyn_t100 INTO FINAL(oref). 
    out->write( oref->get_text( ) && 
                `, ` && oref->msgty ). 
ENDTRY. 
 
out->display( ).
```

## Executable Examples

- [Converting the Exception `error_message` to a Class-Based Exception](abenraise_error_message_shrt_abexa.md)
