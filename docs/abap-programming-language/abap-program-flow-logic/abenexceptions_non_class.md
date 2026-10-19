---
title: "Non-Class-Based Exceptions"
source_file: abenexceptions_non_class.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Exceptions Before Class-Based Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Non-Class-Based Exceptions

***This concept is only supported temporarily in the current ABAP language version and must be replaced with a valid concept for that version.***

Non-class-based exceptions are the predecessors of class-based exceptions and should not be defined any more in new developments.

- [Definition](abenexceptions_non_class.md#definition)

- [Raising](abenexceptions_non_class.md#raising)

- [Handling](abenexceptions_non_class.md#handling)

## Definition

Non-class-based exceptions can be defined in the [parameter interfaces](../../abap-glossary/abenparameter_interface_glosry.md) of function modules and methods. These definitions take place as follows:

- In methods of local classes, by assigning a name for the exception after the addition [`EXCEPTIONS`](../abap-declarations/abapmethods_general.md) of the statement [`[CLASS-]`](../abap-declarations/abapclass-methods.md)[`METHODS`](../abap-declarations/abapmethods.md).

- In methods of global classes, global interfaces or function modules, by assigning a name for the exception, whereby the checkbox for exception classes is not selected.

The statement [`RAISE EXCEPTION`](abapraise_exception_class.md) or the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md) cannot be used to raise class-based exceptions in a method or a function module in whose interface non-class-based exceptions are defined.

### Hint

Before class-based exceptions were introduced, all exceptions defined in the [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) of methods or function modules were non-class-based.

## Raising

Non-class-based exceptions are raised by the following statements:

- [`RAISE`](abapraise_exception.md)

- [`MESSAGE ... RAISING`](abapmessage_raising.md)

## Handling

The handling of non-class-based exceptions is made possible by the addition `EXCEPTIONS` in [method calls](../abap-calling-and-exiting-program-units/abenmethod_calls.md) and [function module calls](../abap-calling-and-exiting-program-units/abapcall_function.md) by assigning numeric values to the exceptions, which are used to fill the system field `sy-subrc` when the exception is raised. The actual error handling takes place after the call, when `sy-subrc` is evaluated.

### Hints

- The exceptions that can be defined in the interfaces of methods and function modules are not real exceptions, since they do not change the control flow, but simply end the processing of the [procedure](../../abap-glossary/abenprocedure_glosry.md) prematurely and set the return code `sy-subrc` instead.

- A predefined exception [`error_message`](../abap-calling-and-exiting-program-units/abapcall_function_parameter.md) can be used when calling function modules to handle [messages](../abap-text-repositories/abenabap_messages.md) of types *E* and *A* sent during the processing of the function module as non-class-based exceptions.
