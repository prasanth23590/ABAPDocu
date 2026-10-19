---
title: "LOAD-OF-PROGRAM"
source_file: abapload-of-program.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Event Blocks > Program Constructor"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOAD-OF-PROGRAM

## Syntax

``` abap
LOAD-OF-PROGRAM.  
```

## Description

This event keyword defines the [program constructor](../../abap-glossary/abenprogram_constructor_glosry.md) of a function pool The program constructor is an event block whose event is raised by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) if such a program is loaded into the [internal session](../../abap-glossary/abeninternal_session_glosry.md).

The first time an external [procedure](../../abap-glossary/abenprocedure_glosry.md) is called, the [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md) of the called procedure is loaded into the internal session of the caller and the event `LOAD-OF-PROGRAM` is raised. The event block is executed before the called procedure. Each time a procedure of the same compilation unit is called again by a caller of the same internal session, the event `LOAD-OF-PROGRAM` is no longer raised.

## Hints

- The event `LOAD-OF-PROGRAM` should not be used to call sophisticated processes, where the program flow cannot be controlled by the caller. This includes especially those that involve user interactions, because then it cannot be guaranteed that the event block is fully executed.

- If a program is only loaded because declarations are required of it, for example, when using [absolute type names](../../abap-glossary/abenabsolute_typename_glosry.md), the `LOAD-OF-PROGRAM` event is not raised. The program constructor is only executed if an executable unit of the program is called afterwards.

- [Class pools](../../abap-glossary/abenclass_pool_glosry.md) do not have a program constructor, since the [static constructor](../../abap-glossary/abenstatic_constructor_glosry.md) of the global class defined in the class pool can be used instead.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The include program `LABAP_DOCUE00` implements the `LOAD-OF-PROGRAM` event block of a function pool. It sets a global variable and triggers an action that is relevant for the complete function pool.
