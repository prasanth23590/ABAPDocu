---
title: "Exception Handling"
source_file: abenabap_exceptions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exception Handling

Exceptions are events during the execution of an ABAP program that interrupt the program flow because it is not possible for the program to continue in a meaningful way. Exception handling enables a response to these events.

Exception situations can be detected either by the program or by the runtime framework. When an exception situation is detected, either the ABAP program or the runtime framework raises an exception.

Exceptions are either catchable or uncatchable.

- Catchable exceptions are [class-based](abenexceptions.md). They are predefined in the system, or can be user-defined. They are raised either by the ABAP runtime framework or in an ABAP program using

  - The statement [`RAISE EXCEPTION`](abapraise_exception_class.md)

  - [`THROW`](abenconditional_expression_result.md) specified in a [conditional expression](abenconditional_expressions.md)

    They can be handled using [`TRY - CATCH - ENDTRY`](abaptry.md).

- Uncatchable exceptions are raised only by the ABAP runtime framework. They are a response to error situations that cannot generally be handled meaningfully in a program.

Exceptions that were not caught, that is, all uncatchable exceptions and all catchable exceptions not caught in the program, produce a [runtime error](../../abap-glossary/abenruntime_error_glosry.md), which means that the program is terminated with a [short dump](../../abap-glossary/abenshort_dump_glosry.md).
