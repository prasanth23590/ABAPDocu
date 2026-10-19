---
title: "CLEANUP"
source_file: abapcleanup.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > TRY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLEANUP

## Syntax

``` abap
CLEANUP [INTO oref].  
```

### Addition

[`... INTO oref`](abapcleanup.md#addition)

## Overview

### Description

Introduces a statement block of a [`TRY`](abaptry.md) control structure where cleanups can be performed.

A `CLEANUP` block is executed exactly when a class-based exception in the `TRY` block of the same `TRY` control structure is raised but is handled in a `CATCH` block of an external `TRY` control structure. A `CLEANUP` block is executed immediately before the context of the exception is deleted:

- If the addition `BEFORE UNWIND` is specified for the handling [`CATCH`](abapcatch_try.md) block, the context is deleted when the `CATCH` block is exited, and the `CLEANUP` block is executed accordingly after handling.

- If the addition `BEFORE UNWIND` is not specified, the context is deleted before the `CATCH` block is executed and the `CLEANUP` block is executed accordingly before it is processed.

- If [`RESUME`](abapresume.md) is used to resume processing after a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md), the context is not deleted and therefore no `CLEANUP` block is executed.

The `CLEANUP` block must be executed completely and must be exited using `ENDTRY` so that the exception can be propagated to its handler. If an attempt is made to exit the context of a `CLEANUP` block prematurely, a runtime error occurs. No [statements](../abap-calling-and-exiting-program-units/abenleave_program_units.md) can be specified in a `CLEANUP` block where it is statically known that returning to the `CLEANUP` block is not possible.

### Hints

- The context of the `TRY` block can be cleaned up in a `CLEANUP` block. For example, objects can be updated to a consistent state or external resources released to which an external handler would no longer have access.

- Since a `CLEANUP` block must always be executed completely, all the exceptions raised there must also be handled there.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In an inner `TRY` block, either the exception `cx_demo0` or `cx_demo1` can be raised. If `cx_demo1` is raised, the `CLEANUP` block of the inner `TRY` block is executed before handling in the outer `TRY` block.

``` abap
TYPES: 
  BEGIN OF ENUM exception, 
    cx_demo0, 
    cx_demo1, 
  END OF ENUM exception. 
 
CLASS cx_demo0 DEFINITION INHERITING FROM cx_no_check. 
ENDCLASS. 
CLASS cx_demo1 DEFINITION INHERITING FROM cx_no_check. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA(exception) = cx_demo1. 
    cl_demo_input=>request( CHANGING field = exception ). 
 
    DATA exc TYPE REF TO cx_no_check. 
    exc = COND #( WHEN exception = cx_demo0 THEN NEW cx_demo0( ) 
                  ELSE NEW cx_demo1( ) ). 
 
    TRY. 
        TRY. 
            RAISE EXCEPTION exc. 
          CATCH cx_demo0. 
            out->write( 'Catching cx_demo0' ). 
          CLEANUP. 
            out->write( 'Cleanup' ). 
        ENDTRY. 
      CATCH cx_demo1. 
        out->write( 'Catching cx_demo1' ). 
    ENDTRY. 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Examples

- [Exceptions, `TRY`](abentry_abexa.md)

- [Exceptions, `CATCH`](abencatch_exception_abexa.md)

## Addition

`... INTO oref`

### Description

If the addition `INTO` is specified, a reference to the exception object is stored in `oref`. The following can be specified for `oref`:

- An existing object reference variable of the type `CX_ROOT`

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md), where an object reference variable of the type `CX_ROOT` is declared.

`oref` can be used to access the exception object.

### Hints

- Within the `CLEANUP` block, the current exception should not be raised again using `RAISE EXCEPTION oref`, since this would modify the attributes of the exception object.

- Within a `CLEANUP` block, the attribute `IS_RESUMABLE` of the exception object is undefined.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `CLEANUP` block of the inner `TRY` block is executed before handling of the exception `cx_demo1` in the outer `TRY` block. The reference variable `exc` points to the exception object of the class `cx_demo1`.

``` abap
CLASS cx_demo0 DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
CLASS cx_demo1 DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    TRY. 
        TRY. 
            RAISE EXCEPTION TYPE cx_demo1. 
          CATCH cx_demo0. 
            ... 
          CLEANUP INTO DATA(exc). 
            out->write( 
              cl_abap_classdescr=>get_class_name( p_object = exc ) ). 
        ENDTRY. 
      CATCH cx_demo1. 
        ... 
    ENDTRY. 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
