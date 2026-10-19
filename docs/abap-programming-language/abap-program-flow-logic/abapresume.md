---
title: "RESUME"
source_file: abapresume.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > TRY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RESUME

## Syntax

``` abap
RESUME.  
```

## Description

This statement exits the [`CATCH`](abapcatch_try.md) handling of a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md) and resumes processing after the place where the exception was raised. The statement `RESUME` can only be listed in a [`CATCH`](abapcatch_try.md) block of a [`TRY`](abaptry.md) control structure for which the addition `BEFORE UNWIND` is declared. When exception handling is exited using `RESUME`, the context of the exception is not deleted, and any `CLEANUP` blocks are not executed.

Prerequisites for resuming processing are:

- The exception was raised as a resumable exception by the addition `RESUMABLE` of the statement [`RAISE EXCEPTION`](abapraise_exception_class.md) or by the addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md).

- The exception was declared with the addition `RESUMABLE` of `RAISING` in the interface of all procedures from which it was propagated, where exceptions derived from `CX_NO_CHECK` are always implicitly declared with that addition.

Otherwise, an exception of the class `CX_SY_ILLEGAL_HANDLER` is raised. To check whether the prerequisites are met, the instance attribute `IS_RESUMABLE` with type `abap_bool` of the current exception object can be checked. The value of the attribute is set using the addition `INTO` when the statements `CATCH` and `CLEANUP` are executed as long as the addition `BEFORE UNWIND` is specified for `CATCH`.

## Hints

- If the resumable exception was not raised by the variant [`RAISE RESUMABLE EXCEPTION oref`](abapraise_exception_class.md), the handler can send information to the raiser of the event by assigning values to appropriate attributes of the exception object.

- Resuming processing after an exception is particularly useful if the exception was raised when a special method was called, such as a constructor or a functional method in an operand position.

- If a `CATCH` block is not exited using `RESUME` when handling a resumable exception, the program flow does not continue in the context of the statement that raised the exception, as described in [System Response After a Class-Based Exception](abenexceptions_system_response.md). This context is deleted when the `CATCH` block is exited, at the latest.

- The transformation option [`OPTIONS exception = 'resumable'`](../abap-data-interchange-formats/abapcall_transformation_options.md) can be used to make exceptions of the class `CX_ST_DESERIALIZATION_ERROR` that are raised in [Simple Transformations](../../abap-glossary/abensimple_transformation_glosry.md) resumable. If [`CATCH BEFORE UNWIND`](abapcatch_try.md) is used, the canceled transformation can also be resumed after the break using `RESUME`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the statement `RESUME` in the handling of a resumable exception `cx_demo`.

``` abap
CLASS cx_demo DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth RAISING RESUMABLE(cx_demo). 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    ... 
    RAISE RESUMABLE EXCEPTION TYPE cx_demo. 
    cl_demo_output=>display( 'Resumed ...' ). 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
 
    TRY. 
        cls=>meth( ). 
      CATCH BEFORE UNWIND cx_demo. 
        RESUME. 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

**[Exceptions](abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ILLEGAL_HANDLER`

- *Cause:* Exception cannot be resumed. The ID of the exception text is `NOT_RESUMABLE`

  *Runtime error:* `UNCAUGHT_EXCEPTION`
