---
title: "runtime error"
source_file: abenruntime_error_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# runtime error

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Caused by uncatchable exceptions when a program is executed, or it can be forced by the language elements [`RAISE SHORTDUMP`](../abap-programming-language/abap-program-flow-logic/abapraise_shortdump.md), [`THROW SHORTDUMP`](../abap-programming-language/abap-program-flow-logic/abenconditional_expression_result.md), or [`ASSERT`](../abap-programming-language/abap-program-maintenance/abapassert.md) or by [exit messages](abenexit_message_glosry.md). Every runtime error terminates the program, which in turn raises a [database rollback](abendatabase_rollback_glosry.md) and is documented by default in a [short dump](abenshort_dump_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-program-flow-logic/abennoncat_exceptions.md)
