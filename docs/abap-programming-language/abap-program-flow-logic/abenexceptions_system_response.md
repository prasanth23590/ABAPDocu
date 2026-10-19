---
title: "System Response After a Class-Based Exception"
source_file: abenexceptions_system_response.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Response After a Class-Based Exception

A class-based exception occurs in a statement block for one of the following reasons:

- The exception is raised explicitly using the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) or the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md).

- The exception is raised implicitly by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md).

In both cases, the occurrence of a class-based exception interrupts the sequential processing of the current statement block, and the system responds as follows:

- If the exception occurs when a `TRY` block of a [`TRY`](abaptry.md) control structure is executed, an appropriate `CATCH` block is searched as a handler. The execution of each `TRY` block opens a context, also referred to as a protected area, into which the execution of other `TRY` blocks can be embedded. Usually, the embedding takes place by calling [procedures](abenexceptions_procedures.md) and less frequently by nesting `TRY` blocks in the source code. Starting at the position where the exception is raised, the system scans the `TRY` control structures of the involved `TRY` blocks from the inside to the outside for the first [`CATCH`](abapcatch_try.md) block in which the exception class or one of its superclasses is listed. If such a `CATCH` block is found, there are two possible cases:

  - If the addition `BEFORE UNWIND` is not specified in the statement [`CATCH`](abapcatch_try.md), the context in which the exception was raised is deleted, including all called procedures and their local data. The `CATCH` block is then executed.

  - If the addition `BEFORE UNWIND` is specified in the statement [`CATCH`](abapcatch_try.md), the `CATCH` block is executed immediately. If the `CATCH` block is exited using the statement [`RESUME`](abapresume.md) in a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md), processing resumes after the raising position. In all other cases, the system deletes the context in which the exception was raised, after the `CATCH` block is exited.

    If the `CATCH` block is not exited using a statement such as [`RESUME`](abapresume.md), [`RETRY`](abapretry.md), or any other processing block [exits](../abap-calling-and-exiting-program-units/abenleave_processing_blocks.md), processing continues after the `TRY` control structure of the block by default.

- If no handler is found in any of the participating `TRY` control structures of a protected area, or if the exception is not raised during processing of a `TRY` block of a `TRY` control structure, a runtime error occurs at the point where the exception was raised. The [short dump](../../abap-glossary/abenshort_dump_glosry.md) of the runtime error contains the name of the exception class and the exception text.

Note the following special features:

- If the context of a procedure is exited during the handler search, the procedure's interface will be checked. Only exceptions declared there can be propagated from the procedure. Exceptions of the categories `CX_STATIC_CHECK` and `CX_DYNAMIC_CHECK` must be declared explicitly, while exceptions of category `CX_NO_CHECK` are always declared implicitly but can also be declared explicitly. If the exception is not declared in the interface, the exception of the predefined class `CX_SY_NO_HANDLER` is raised at the call position of the procedure. The attribute `PREVIOUS` of the new exception object of class `CX_SY_NO_HANDLER` contains a reference to the original exception object that cannot pass the interface directly due to the missing declaration.

- If a handler is found, the [`CLEANUP`](abapcleanup.md) blocks of all `TRY` control structures that were so far scanned unsuccessfully are executed from the inside to the outside, directly before their context is deleted. This means that, if `BEFORE UNWIND` is specified in the `CATCH` block, the `CLEANUP` blocks are executed when the handler is exited. Otherwise, they are executed before being handled. Exceptions that are raised within a `CLEANUP` block cannot exit the block and must be handled there.

  No `CLEANUP` blocks are executed in the following cases:

  - If the handling of a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md) is exited using [`RESUME`](abapresume.md).

  - `TRY` control structures whose exception is raised in a `CATCH` block (a `CATCH` block is not part of the protected range).

See also:

- [Class-Based Exceptions in Procedures](abenexceptions_procedures.md)

- [Class-Based Exceptions in Event Handlers](abenexceptions_events.md)
