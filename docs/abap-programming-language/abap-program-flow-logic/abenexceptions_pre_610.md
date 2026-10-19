---
title: "Exceptions Before Class-Based Exceptions"
source_file: abenexceptions_pre_610.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exceptions Before Class-Based Exceptions

***This concept is only supported temporarily in the current ABAP language version and must be replaced with a valid concept for that version.***

Exceptions are [class-based](abenexceptions.md). Before the introduction of exception classes, there were the following types of exceptions:

- Exception situations detected by the system (and whose causes could be handled effectively by the program) raised catchable runtime errors that could be handled by the statement `CATCH SYSTEM-EXCEPTIONS`. Catchable runtime errors are now obsolete. Each catchable runtime error is assigned an exception class instead, which is handled in a [`TRY` block](abaptry.md). Conversely, not all predefined class-based exceptions are assigned to a catchable runtime error. No new catchable runtime errors are created and existing runtime errors that are to be made catchable are no longer transformed to catchable runtime errors. Instead, exception classes are assigned to them.

- [User-defined catchable exceptions](abenexceptions_non_class.md) were only possible in the interfaces of function modules and methods. These types of exceptions can be raised within the [procedure](../../abap-glossary/abenprocedure_glosry.md) when an exception situation is recognized by the statement [`RAISE`](abapraise_exception.md) or [`MESSAGE RAISING`](abapmessage_raising.md). The caller of the procedure can use the addition `EXCEPTIONS` of the statement [`CALL FUNCTION`](../abap-calling-and-exiting-program-units/abapcall_function.md) or [`meth( ... )`](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) to assign return codes for the system field `sy-subrc` to the exceptions the caller wants to handle and evaluate them after the call. However, this does not represent true exception handling in the sense of reacting to an event.

## Interaction of the Exception Concepts

The class-based exceptions replace and enhance the previous concepts completely. Class-based exceptions can be raised and handled in all ABAP contexts (programs, processing blocks). In particular, all previously catchable runtime errors can be handled as class-based exceptions, whereby the previous exception groups are mapped by shared superclasses. For reasons of downward-compatibility, the catchable runtime errors and the non-class-based exceptions defined in the interfaces of methods and function modules have not been abolished, but their use has been restricted as follows:

- Within a [processing block](../../abap-glossary/abenprocessing_block_glosry.md), only one kind of exception can be raised.

- Within a procedure interface, the declaration of class-based exceptions and the definition of non-class-based exceptions are mutually exclusive.

- Within a processing block, catchable runtime errors cannot be caught using `CATCH SYSTEM-EXCEPTIONS` if class-based exceptions are handled there in [`TRY`](abaptry.md) blocks or are raised using [`RAISE EXCEPTION`](abapraise_exception.md) or the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md). Instead, catchable runtime errors must be caught when handling the associated class-based exception.

For reasons of interoperability, class-based exceptions and return values of function modules should be handled or evaluated within a processing block using non-class-based exceptions.
