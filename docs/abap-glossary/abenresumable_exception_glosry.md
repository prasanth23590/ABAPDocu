---
title: "resumable exception"
source_file: abenresumable_exception_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# resumable exception

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

[Class-based exception](abenclass_based_exception_glosry.md) that is raised by the addition `RESUMABLE` of the statement [`RAISE EXCEPTION`](../abap-programming-language/abap-program-flow-logic/abapraise_exception_class.md) or by the addition [`THROW`](../abap-programming-language/abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional expression](../abap-programming-language/abap-program-flow-logic/abenconditional_expressions.md). When a resumable exception is handled in a [`CATCH`](../abap-programming-language/abap-program-flow-logic/abapcatch_try.md) block, processing can be resumed using the statement [`RESUME`](../abap-programming-language/abap-program-flow-logic/abapresume.md) directly after the raising statement if the context of the exception still exists. The property of resumability of an exception can be lost when the exception is propagated from [procedures](abenprocedure_glosry.md) if it is not marked as resumable in all relevant [parameter interfaces](abenparameter_interface_glosry.md) by the addition `RESUMABLE` in the `RAISING` declaration of the procedures.
