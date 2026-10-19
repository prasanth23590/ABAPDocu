---
title: "CALL FUNCTION, parameter_list"
source_file: abapcall_function_parameter.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION > CALL FUNCTION func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION, parameter_list

## Syntax

``` abap
... [EXPORTING  p1 = a1 p2 = a2 ...]   
    [IMPORTING  p1 = a1 p2 = a2 ...]   
    [TABLES     t1 = itab1 t2 = itab2 ...]   
    [CHANGING   p1 = a1 p2 = a2 ...]   
    [EXCEPTIONS [exc1 = n1 exc2 = n2 ...]   
                [error_message = n_error]   
                [OTHERS = n_others]].  
```

### Addition

[1. `... EXPORTING p1 = a1 p2 = a2 ...`](abapcall_function_parameter.md#addition-1)

[2. `... IMPORTING p1 = a1 p2 = a2 ...`](abapcall_function_parameter.md#addition-2)

[3. `... TABLES t1 = itab1 t2 = itab2 ...`](abapcall_function_parameter.md#addition-3)

[4. `... CHANGING p1 = a1 p2 = a2 ...`](abapcall_function_parameter.md#addition-4)

[5. `... EXCEPTIONS exc1 = n1 exc2 = n2 ... OTHERS = n_others`](abapcall_function_parameter.md#addition-5)

[6. `... EXCEPTIONS ... error_message = n_error ...`](abapcall_function_parameter.md#addition-6)

## Overview

### Description

With the exception of the addition `EXCEPTIONS`, these additions assign the actual parameters `a1`, `a2`, ... to the formal parameters `p1`, `p2`, ... or `t1`, `t2`, ... of the called function module. All data objects and some expressions whose data type [matches](../abap-declarations/abentyping_check.md) the [typing](../../abap-glossary/abentyping_glosry.md) of the corresponding formal parameter can be specified as actual parameters. With the exception of calculation expressions specified for input parameters, each formal parameter inherits all properties of the assigned actual parameter when called. Non-class-based exceptions can be handled using the addition `EXCEPTIONS`. The order of the additions is predefined.

A catchable exception is raised whenever a formal parameter is incorrect, and the name of the function module is specified by a constant or as a character literal. Unlike method calls, formal parameters are not fully checked by the syntax check. Only parameters that are recognizably misspelled, e.g. by using certain special characters, lead to a syntax warning. If the name of the function module is specified by a variable, the specification of an incorrect formal parameter is ignored at runtime.

## Addition 1

`... EXPORTING p1 = a1 p2 = a2 ...`

### Description

This addition assigns actual parameters to the [input parameters](../../abap-glossary/abeninput_parameter_glosry.md) of the called function module. `EXPORTING` can be used to assign actual parameters to the optional input parameters but is mandatory for non-optional input parameters. In [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md), a reference to an actual parameter is passed when the call is made. In [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the content of an actual parameter is assigned to the corresponding formal parameter.

`a1`, `a2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md), which means that, in addition to data objects, expressions can also be passed as actual parameters. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case.

### Hints

- [Substring access](../abap-operands/abenoffset_length.md) is not possible on an actual parameter of type `string` or `xstring` specified after `EXPORTING`.

- Unlike in [method calls](abapcall_method_parameters.md), a generic type specification `#` is not possible when a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) is specified. This is because the typing of the parameters is not determined until runtime.

## Addition 2

`... IMPORTING p1 = a1 p2 = a2 ...`

### Description

This addition assigns actual parameters to the [output parameters](../../abap-glossary/abenoutput_parameter_glosry.md) of the called function module. `IMPORTING` can be used to assign actual parameters to all output parameters, but this is not mandatory. In [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md), a reference is passed to an actual parameter when the call is made. In [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the content of an output parameter is assigned to the relevant actual parameter only if the function module is completed without errors.

### Hint

Unlike in [method calls](abapcall_method_parameters.md), no [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) and no [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) can be specified.

## Addition 3

`... TABLES t1 = itab1 t2 = itab2 ...`

### Description

This addition assigns actual parameters to the [table parameters](../../abap-glossary/abentable_parameter_glosry.md) of the called function module. If `TABLES` is used, internal tables `itab1`, `itab2`, ... must be assigned to all non-optional table parameters `t1`, `t2`, ... of the called function module and are optional for all optional table parameters. For `itab1`, `itab2`, ..., only [standard tables](../../abap-glossary/abenstandard_table_glosry.md) can be specified. The data is passed using a reference.

## Addition 4

`... CHANGING p1 = a1 p2 = a2 ...`

### Description

This addition assigns actual parameters to the [input/output parameters](../../abap-glossary/abeninput_output_parameter_glosry.md) of the called function module. `CHANGING` can be used to assign actual parameters to the optional input/output parameters but is mandatory for non-optional input/output parameters. In [pass by reference](../../abap-glossary/abenpass_by_reference_glosry.md), a reference to an actual parameter is passed when the call is made. In [pass by value](../../abap-glossary/abenpass_by_value_glosry.md), the content of an actual parameter is assigned to the relevant formal parameter and the modified content of an input/output parameter is only assigned to the relevant actual parameter if the function module is completed without errors.

### Hint

Unlike in [method calls](abapcall_method_parameters.md), no [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be specified.

## Addition 5

`... EXCEPTIONS exc1 = n1 exc2 = n2 ... OTHERS = n_others`

### Description

`EXCEPTIONS` can be used to assign return codes to [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) `exc1 exc2 ...` declared in the parameter interface. Each exception `exc1 exc2 ...` that the caller wants to handle must be assigned to a directly specified number `n1 n2 ...` All numbers between 0 and 65535 can be specified. The behavior outside of this range is undefined.

By specifying `OTHERS` as the last entry after `EXCEPTIONS`, a common return code can be assigned to all exceptions not specified explicitly in `exc1 exc2...`. This is done by assigning a number `n_others`. The same return code can be assigned to different exceptions (including `OTHERS`). The behavior when an exception is raised is as follows:

- If the statement [`RAISE`](../abap-program-flow-logic/abapraise_exception.md) or [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md) is used to raise an exception `exc1 exc2 ...` to which a return code is assigned, the statement is terminated immediately, any procedure parameters passed by value are not filled, and the number `n1 n2 ...` assigned to the exception is available to be evaluated in `sy-subrc`.

- If the call of an exception raised by [`RAISE`](../abap-program-flow-logic/abapraise_exception.md) does not assign a return code, the program is terminated with a runtime error.

- If the call of an exception raised by [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md) does not assign a return code, the [message](../../abap-glossary/abenmessage_glosry.md) is sent, and the system resumes in accordance with the message type.

If no exception is raised, a call sets `sy-subrc` to 0.

The addition `EXCEPTIONS` cannot be specified in the call if `RAISING` is used to declare [class-based exceptions](../../abap-glossary/abenclass_based_exception_glosry.md) in the parameter interface of the called procedure.

During program execution, a specified exception is not checked when a function module is called.

### Hints

- If the value 0 is assigned to an exception, this indicates that the caller wants to ignore this exception. If the exception is raised in the function module, no runtime error occurs, but the exception cannot be handled.

- For more information about the behavior of class-based exceptions in function modules, see [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

## Addition 6

`... EXCEPTIONS ... error_message = n_error ...`

### Description

Specifying the predefined exception `error_message` after `EXCEPTIONS` changes the processing of all messages that are sent as follows during function module processing:

- Messages sent using the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md) without the addition [`RAISING`](../abap-program-flow-logic/abapmessage_raising.md).

- Messages sent using the statement [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md) because no return code is assigned to them.

- Messages sent by the ABAP runtime framework.

For these cases, message processing is affected as follows:

- [Messages](../../abap-glossary/abenmessage_glosry.md) of the type S, I, or W are not sent.

- Messages of the type E and A raise the exception `error_message` and set `sy-subrc` to `n_error`. The message class, message type, message number, and the content of possible placeholders for the `MESSAGE` statement are available in the fields `sy-msgid`, `sy-msgno`, `sy-msgty`, and `sy-msgv1`, ... `sy-msgv4`. In the case of messages of type A, the statement [`ROLLBACK WORK`](../abap-database-access/abaprollback.md) is also executed implicitly.

- Messages of the type X are not affected. As always, they cause a program termination with a [short dump](../../abap-glossary/abenshort_dump_glosry.md).

### Hints

- When messages are handled with the predefined exception `error_message`, it does not matter whether the message was sent in the current function module or in a module that is called by it. Unlike the exceptions raised by the statement [`RAISE`](../abap-program-flow-logic/abapraise_exception.md), messages sent using the statement [`MESSAGE`](../abap-text-repositories/abapmessage.md) are propagated across call levels.

- The following situations can arise for the statement [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md) within the called function module:

  - If a return code is assigned to the exception specified after `RAISING`, the exception is handled independently of `error_message` and `sy-subrc` is set to this value.

  - If no return code is assigned to the exception specified after `RAISING` and `error_message` is specified, the sent message is affected as specified above.

  - If no return code is assigned to the exception specified after `RAISING` and `error_message` is not specified, the message is sent in accordance with its type.

- When a program is resumed after handling a type A message, it must be ensured that a complete [`ROLLBACK WORK`](../abap-database-access/abaprollback.md) has been performed and not just a database rollback.

- When programs are executed, the ABAP runtime framework can also send messages. These messages are caught using `error_message` in the same way as messages sent using `MESSAGE`.
