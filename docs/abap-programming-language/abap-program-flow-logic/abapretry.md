---
title: "RETRY"
source_file: abapretry.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > TRY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RETRY

## Syntax

``` abap
RETRY.  
```

## Description

This statement exits the [`CATCH`](abapcatch_try.md) handling of a [class-based exception](../../abap-glossary/abenclass_based_exception_glosry.md) and continues processing with the [`TRY`](abaptry.md) statement of the current `TRY` control structure.

The `RETRY` statement can only be executed within a `CATCH` block of a `TRY` control structure.

## Hints

- The `RETRY` statement enables a `TRY` block that raised an exception to be executed again completely.

- If the `BEFORE UNWIND` addition is specified for a `CATCH` block, exiting using `RETRY` deletes the context of the exception and recreates it in the `TRY` block. With respect to the context, therefore, `RETRY` behaves like any exit of a `CATCH` block, with the exception of [`RESUME`](abapresume.md).

- The cause of the exception must be removed either before `RETRY` in the `CATCH` block or after `RETRY` in the `TRY` block. If a `TRY` block is repeated and the cause of the exception is not removed, an endless loop occurs.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following exception handling extends the ABAP-specific handling of a division by zero to dividends not equal to zero, by setting these to the value zero before a second pass.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: number1 TYPE i, 
      number2 TYPE i. 
cl_demo_input=>add_field( CHANGING field = number1 ). 
cl_demo_input=>request(   CHANGING field = number2 ). 
 
DATA result  TYPE p DECIMALS 2. 
 
TRY. 
    result = number1 / number2. 
    out->write( |Result: { result ALIGN = LEFT }| ). 
  CATCH cx_sy_zerodivide. 
    number1 = 0. 
    RETRY. 
ENDTRY. 
 
out->display( ).
```
