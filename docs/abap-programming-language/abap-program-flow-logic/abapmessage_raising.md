---
title: "MESSAGE, RAISING"
source_file: abapmessage_raising.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Exceptions Before Class-Based Exceptions > Non-Class-Based Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MESSAGE, RAISING

## Deprecated Syntax

``` abap
MESSAGE { msg | text } [DISPLAY LIKE dtype] [WITH dobj1... dobj4] 
        RAISING exception.  
```

[`msg`](../abap-text-repositories/abapmessage_msg.md) · [`[DISPLAY LIKE dtype]`](../abap-text-repositories/abapmessage.md) · [`[WITH dobj1... dobj4]`](../abap-text-repositories/abapmessage.md)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

### Description

The statement [`MESSAGE`](../abap-text-repositories/abapmessage.md) with the addition `RAISING` raises a non-class-based exception `exception` and only sends a message if the exception is not handled. The semantics of [`msg`](../abap-text-repositories/abapmessage_msg.md), `text`, and [`WITH`](../abap-text-repositories/abapmessage.md) is the same as in the statement `MESSAGE` without the addition `RAISING`.

This addition only makes sense during the processing of methods and function modules in which the non-class-based exception `exception` is defined. Furthermore, it cannot be used in the same [processing block](../../abap-glossary/abenprocessing_block_glosry.md) as the statement `RAISE EXCEPTION` or the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md) to raise class-based exceptions.

- If the `MESSAGE` statement is executed with the addition `RAISING` during processing of a method or a function module whose caller assigns a return value to the [exception](abenexceptions_non_class.md) `exception` using the addition `EXCEPTIONS` of the statement `CALL`, the statement has the same effect as the statement [`RAISE`](abapraise_exception.md).

- If no return code is assigned to the exception `exception`, the addition `RAISING` is ignored, and the message is sent using the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md) and processed according to its [message type](../../abap-glossary/abenmessage_type_glosry.md).

The system fields of the statement `MESSAGE` are filled in both cases and are available in the calling program after an exception raised using `MESSAGE ...RAISING` is handled.

### Hints

- The statement `MESSAGE ... RAISING` is to be seen primarily as a statement for raising exceptions and not for sending messages. Such an exception should always be handled like an exception raised using `RAISE`, since the behavior of the message depends strongly on the context and cannot usually be predicted when the function module is created.

- Using `MESSAGE ... RAISING` in cases in which non class-based exceptions must still be used is preferable to using the `RAISE` statement, because it offers the option of providing additional text information with an exception.

- A return code can be assigned to messages that are sent in function modules without the addition `RAISING` by using the predefined exception [`error_message`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md).

- Messages that are sent as messages when a function module is called and that are not caught despite the addition `RAISING` are affected like messages with [`error_message`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md).

- If a [procedure](../../abap-glossary/abenprocedure_glosry.md) is exited by raising an exception, the content of the formal parameter for which the [pass by value](../../abap-glossary/abenpass_by_value_glosry.md) is defined is not assigned to the respective actual parameters.
