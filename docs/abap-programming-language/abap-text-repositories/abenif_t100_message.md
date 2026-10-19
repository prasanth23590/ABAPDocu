---
title: "Messages - System Interface IF_T100_MESSAGE"
source_file: abenif_t100_message.html
section: "ABAP Programming Language > ABAP - Text Repositories > Messages > Messages - System Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Messages - System Interface IF_T100_MESSAGE

The interface `IF_T100_MESSAGE` associates classes with [messages](../../abap-glossary/abenmessage_glosry.md). Classes that implement this interface can be used to access and send messages. To do this, `IF_T100_MESSAGE` contains a structured attribute `T100KEY` of the type `SCX_T100KEY`. In a class that implements the interface, the content of this structure specifies a [message](../../abap-glossary/abenmessage_glosry.md) in the database table `T100`:

- The content of component `MSGID` is the [message class](../../abap-glossary/abenmessage_class_glosry.md).

- The content of component `MSGNO` is the [message number](../../abap-glossary/abenmessage_number_glosry.md).

- The content of components `ATTR1` to `ATTR4` is the names of attributes of the implementing class whose content is used as placeholder texts for the possible placeholders in the texts of the message.

Using an implementing class, the message text can be accessed as follows:

- The interface `IF_T100_MESSAGE` includes the interface `IF_MESSAGE`, which should not be used as a standalone interface. This interface contains the methods `GET_TEXT` and `GET_LONGTEXT`, which can be implemented by a class with the interface `IF_T100_MESSAGE` so that they return the short text and long text of the current message. To do this, the corresponding methods of the class `CL_MESSAGE_HELPER` can be used.

- In the variant [`MESSAGE oref`](abapmessage_msg.md) of the statement [`MESSAGE`](abapmessage.md), an [interface reference variable](../../abap-glossary/abeninterface_ref_variable_glosry.md) of the type `IF_T100_MESSAGE` or a [class reference variable](../../abap-glossary/abenclass_reference_variabl_glosry.md) of a class that implements this interface can be specified to output the message that is specified by the content of the structure `T100KEY`.

To do this, the statement `MESSAGE` or the class `CL_MESSAGE_HELPER` evaluates the content of the structure `T100KEY` as follows:

- In database table `T100`, a message is searched for whose message class and message number correspond to the components `MSGID` and `MSGNO` of the structure `T100KEY`. If a message is found, its texts are used. If not, a short text is generated that lists the message class and message number as well as the placeholder texts from the class attributes that are specified in the structure.

- The possible placeholders *&1* to *&4* and *&* of the short text or *&V1&* to *&V4&* of the long text of the message are replaced by the content of the class attributes specified in the components `ATTR1` to `ATTR4` of structure `T100KEY` in accordance with the rules of the addition [`WITH`](abapmessage.md) of the statement [`MESSAGE`](abapmessage.md). If an attribute specified in the components `ATTR1` to `ATTR4` does not exist or if the content of an attribute cannot be converted to a placeholder text, the character *&* is added to the start and the end of the attribute name and the resulting string is used as the placeholder text. If one of the components `ATTR1` to `ATTR4` is initial, the corresponding placeholder text is initialized.

## Hints

- The interface `IF_T100_MESSAGE` is mainly intended for use with [exception texts](../abap-program-flow-logic/abenexception_texts.md) in [exception classes](../../abap-glossary/abenexception_class_glosry.md). If the interface is implemented in regular classes and in local exception classes, the filling of the interface structure `T100KEY` must be programmed here explicitly. For global exception classes, however, the implementation of the interface methods `GET_TEXT` and `GET_LONGTEXT` is already contained in the superclass `CX_ROOT` and alias names are declared for these methods here. When creating global exception classes, tool support is provided for filling the structure `T100KEY` and for mapping attributes to placeholders. This is done using structured constants that can be specified when an exception is raised.

- It should be noted that with interface `IF_T100_MESSAGE` there is a double indirection for the possible placeholders of a message. The text for a placeholder is taken from an attribute of the implementing class whose name is itself contained in a component of structure `T100KEY`.

- The method `GET_LATEST_T100_EXCEPTION` in the class `CL_MESSAGE_HELPER` can be used to return the last object in a chain of exception objects that are chained by the attribute `PREVIOUS` that has an [exception text](../abap-program-flow-logic/abenexception_texts.md) defined by a message.

- The interface `IF_T100_MESSAGE` does not have any attributes for the message type.

- The interface [`IF_T100_DYN_MSG`](abenif_t100_dyn_msg.md) adds predefined attributes for the message type and the placeholders of the message to the interface `IF_T100_MESSAGE`. While `IF_T100_MESSAGE` is intended for static [exception texts](../abap-program-flow-logic/abenexception_texts.md) of exception classes, `IF_T100_DYN_MSG` can [associate](../abap-program-flow-logic/abenmessage_exceptions.md) any messages with exception classes.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of an exception of the class `CX_DEMO_T100`, which implements the interface `IF_T100_MESSAGE` by using [`THROW`](../abap-program-flow-logic/abenconditional_expression_result.md).

``` abap
DATA col TYPE c LENGTH 1. 
 
... 
 
TRY. 
    FINAL(color) = COND string( 
                    WHEN col = 'R' THEN 'red' 
                    WHEN col = 'B' THEN 'blue' 
                    WHEN col = 'G' THEN 'green' 
                    ELSE THROW cx_demo_t100( 
                         textid = cx_demo_t100=>demo 
                         text1  = 'Illegal value:' 
                         text2  = CONV #( col ) ) ). 
  CATCH cx_demo_t100. 
    ... 
ENDTRY.
```

## Executable Examples

- [System Interface `IF_T100_MESSAGE` in a Regular Class](abenif_t100_message_abexa.md)

- [System Interface `IF_T100_MESSAGE` in a Local Exception Class](abenmessage_interface_abexa.md)
