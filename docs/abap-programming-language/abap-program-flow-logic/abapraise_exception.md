---
title: "RAISE"
source_file: abapraise_exception.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Exceptions Before Class-Based Exceptions > Non-Class-Based Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAISE

## Deprecated Syntax

``` abap
RAISE exception.  
```

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

### Description

This statement raises the [non-class-based exception](abenexceptions_non_class.md) `exception`.

- `RAISE` can be specified in a method only if the non-class-based exception is defined in the interface of the method.

- `RAISE` should be specified in function modules only if the non-class-based exception is defined in the interface of the function module.

- It is possible to specify `RAISE` in all other positions, but it is not recommended.

After the exception `exception` is raised, the system behaves as follows:

- If the exception is raised in a method or function module whose caller assigns a return code to the exception, the [procedure](../../abap-glossary/abenprocedure_glosry.md) is terminated immediately, the system returns to the calling position, and the system field `sy-subrc` is set according to the assignment.

- If the exception is raised in a method or function module whose caller does not assign a return code to the exception, a runtime error is then raised whose [short dump](../../abap-glossary/abenshort_dump_glosry.md) contains the name of the exception.

- Special handling for function modules: If the exception is raised in a subroutine, the system searches the call stack for the first function module. If it finds a function module, and there are only subroutines or no procedures between the subroutine that raised the exception and the function module, and if the function module defines the exception, the system handles the exception as if it originated from that function module. Otherwise, a runtime error occurs.

- In all other processing blocks, raising a non class-based exception produces a runtime error that immediately terminates the execution of the program.

This form of the statement `RAISE` cannot be used in the same [processing block](../../abap-glossary/abenprocessing_block_glosry.md) as the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) or the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md) to raise class-based exceptions.

### Hints

- The statement `MESSAGE` with the addition [`RAISING`](abapmessage_raising.md) also raises a non-class-based exception and is to be preferred in cases in which non-class-based exceptions still have to be used, because it offers the option of adding a text to the exception.

- If a [procedure](../../abap-glossary/abenprocedure_glosry.md) is exited by raising an exception, the content of the formal parameter for which the [pass by value](../../abap-glossary/abenpass_by_value_glosry.md) is defined is not assigned to the respective actual parameters.
