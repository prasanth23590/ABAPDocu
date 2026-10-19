---
title: "Class-Based Exceptions"
source_file: abenexceptions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Class-Based Exceptions

Class-based exceptions are implemented as instances of [exception classes](abenexceptions_classes.md). Exception classes are either predefined globally in the system or can be defined by the user both globally and locally. Class-based exceptions are raised either by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) or by a program.

- Exception situations detected by the system and whose causes can be handled properly in the program, raise predefined class-based exceptions.

- The exceptions of all exception classes visible in a program can be raised by the program as follows:.

  - Using the statement [`RAISE EXCEPTION`](abapraise_exception_class.md).

  - Using the addition [`THROW`](abenconditional_expression_result.md) in [conditional expressions](abenconditional_expressions.md).

- Class-based exceptions can be declared in the interface of [procedures](abenexceptions_procedures.md). This is done using the addition `RAISING` of the statements [`METHODS`](../abap-declarations/abapmethods.md) and [`FORM`](../abap-obsolete-language-elements/abapform.md). The declared exceptions can occur at the call position of a procedure if the exception is not handled in the procedure.

When an exception is raised, an exception object can be created, whose attributes contain information about the error situation. A class-based exception can be handled in a [`TRY`](abaptry.md) control structure. The `TRY` block defines a protected area whose exceptions can be handled in subsequent `CATCH` blocks. The statement [`RETRY`](abapretry.md) enables a full `TRY` block to be repeated after an exception. Because all exception classes are subclasses of common superclasses, the associated exceptions can be handled at the same time by handling the respective superclasses. The system [propagates](abenexceptions_system_response.md) the exception object or the class-based exception until the exception is handled or an interface is violated.

There are two different exception handling cases:

1.  The context in which the exception was raised is deleted completely before or after handling. This removes all procedures from the memory, including their local data, which was called from the handler context and caused the exception, and handling is resumed depending on how the handler is exited.

2.  The context in which the exception was raised is retained and the program is resumed after the statement that raised the exception.

A prerequisite for the second case are [resumable exceptions](../../abap-glossary/abenresumable_exception_glosry.md). These must be raised using the addition `RESUMABLE` of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) and declared using the addition `RESUMABLE` in the interface of the procedures from which they were propagated. The statement [`RESUME`](abapresume.md) is used to resume the program.
