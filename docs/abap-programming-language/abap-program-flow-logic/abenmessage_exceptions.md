---
title: "Exception Classes for Messages"
source_file: abenmessage_exceptions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Exception Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exception Classes for Messages

The [exception texts](abenexception_texts.md) described in the previous section are assigned to an exception class statically and express a predefined semantic meaning. This applies to both categories of exception texts, namely [messages as exception texts](abenexception_texts_t100.md) and internal exception texts from [OTR](abenexception_texts_t100.md).

Another frequent use case is passing a message from the table `T100` to the exception object when an exception is raised. This is the case, for example, when a non-class-based exception raised using [`MESSAGE RAISING`](abapmessage_raising.md) is handled or a message of a function module is caught using [`error_message`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md) and then passed as a class-based exception.

The predefined exception texts that are selected using the input parameter `TEXTID` of the instance constructor are not suitable for this purpose. Instead, the following are available:

- The system interface [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md).

- The addition [`MESSAGE`](abapraise_exception_message.md) of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) and of the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md).

Exception objects of exception classes that include the system interface `IF_T100_DYN_MSG` can be linked with any message from the table `T100` using the addition `MESSAGE`. Exception objects of exception classes that include only the system interface `IF_T100_MESSAGE` can also be linked with messages using the addition `MESSAGE` with restrictions. The latter option is intended only for exception classes that previously had no specific exception texts for generic use before `IF_T100_DYN_MSG` was introduced. In other cases, the concept of exception texts and the linking of any messages are strictly separated with special exception classes provided specifically for this purpose. In particular, the addition `MESSAGE` cannot be combined with the input parameter `TEXTID`.
