---
title: "Exceptions in ABAP Statements"
source_file: abenabap_language_exceptions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exceptions in ABAP Statements

Error situations that occur during the execution of an ABAP statement raise exceptions. These exceptions are fully integrated into the [exception concept](abenabap_exceptions.md) and are raised by the runtime framework. Two types of exception exist:

- **Catchable exceptions**, which are based on predefined [exception classes](../../abap-glossary/abenexception_class_glosry.md).

- **Uncatchable exceptions**, which directly produce [runtime errors](../../abap-glossary/abenruntime_error_glosry.md).

Each catchable exception is assigned to a runtime error that terminates the program if the exception is neither caught by using the [`CATCH`](abapcatch_try.md) statement with a suitable exception class nor propagated to a caller. The keyword documentation lists the type of exceptions that can be raised for each statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Unhandled exception.

The following program lines produce the runtime error `COMPUTE_INT_ZERODIVIDE` because division by zero is invalid and this exception situation is not handled:

``` abap
DATA result TYPE i. 
result = 1 / 0.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Handling exceptions using exception classes.

The above exception is represented by the exception class `CX_SY_ZERODIVIDE`, which is a subclass of the exception class `CX_SY_ARITHMETIC_ERROR`. Therefore, the exception can be handled as follows (the `ERR_TEXT` variable is passed the text *Division by zero.*):

``` abap
DATA myref TYPE REF TO cx_sy_arithmetic_error. 
DATA err_text TYPE string. 
DATA result TYPE i. 
TRY. 
    result = 1 / 0. 
  CATCH cx_sy_arithmetic_error INTO myref. 
    err_text = myref->get_text( ). 
ENDTRY.
```
