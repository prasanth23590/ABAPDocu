---
title: "Program Constructor"
source_file: abenprogram_constructor.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Event Blocks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Program Constructor

The program constructor can be used to initialize the global data of a program. It is introduced using the statement:

- [`LOAD-OF-PROGRAM`](abapload-of-program.md)

The associated event occurs when a program is loaded into the [internal session](../../abap-glossary/abeninternal_session_glosry.md).

## Hints

- [Class pools](../../abap-glossary/abenclass_pool_glosry.md) do not have a program constructor, since the [static constructor](../../abap-glossary/abenstatic_constructor_glosry.md) from the global class defined in the class pool can be used instead.
