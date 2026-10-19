---
title: "assertion"
source_file: abenassertion_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# assertion

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Assertion in an [ABAP program](abenabap_program_glosry.md). An assertion is defined as a conditional [checkpoint](abencheckpoint_glosry.md) using the [`ASSERT`](../abap-programming-language/abap-program-maintenance/abapassert.md) statement. Assertions are either always active or can be [activated](abenactivatable_checkpoint_glosry.md) by assigning them to a [checkpoint group](abencheckpoint_group_glosry.md). When an active assertion is reached, the corresponding condition is evaluated. If the condition is violated, the program terminates with a runtime error, accesses the [ABAP Debugger](abenabap_debugger_glosry.md), or creates a log entry. If a [checkpoint group](abencheckpoint_group_glosry.md) is assigned, the program behavior is controlled by the corresponding activation settings. Otherwise, the program is terminated.
