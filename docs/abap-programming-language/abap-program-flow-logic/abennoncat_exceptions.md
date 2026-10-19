---
title: "Runtime Errors"
source_file: abennoncat_exceptions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Runtime Errors

Runtime errors indicate situations in which the execution of an ABAP program cannot be continued but must be terminated. Runtime errors can occur in one of the following situations when ABAP programs are executed:

- Non-handled exceptions:

  - A catchable exception is not handled.

  - A uncatchable exception is raised.

- Program-driven raise:

  - The statement [`RAISE SHORTDUMP`](abapraise_shortdump.md) or the addition [`THROW SHORTDUMP`](abenconditional_expression_result.md) is used.

  - An [assertion](../../abap-glossary/abenassertion_glosry.md) fails.

  - An [exit message](../../abap-glossary/abenexit_message_glosry.md) or [message](../../abap-glossary/abenmessage_glosry.md) of type *X* is sent.

Each runtime error is identified by a name and assigned to a specific error situation and leads to a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). Following a program termination caused by a runtime error, the system generates a [short dump](../../abap-glossary/abenshort_dump_glosry.md) which contains the name of the runtime error, the associated exception class, content of data objects, active calls, control structures, and so on, and allows the user to branch directly to the ABAP Debugger. Short dumps are kept in the system for 14 days by default and managed using the [ABAP dump analysis](../../abap-glossary/abenabap_dump_analsyis_glosry.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of the runtime error `COMPUTE_INT_ZERODIVIDE` when the exception `CX_SY_ZERODIVIDE` is not caught.

cl_demo_output=\>display( 1 / 0 ).
