---
title: "RAISE EXCEPTION"
source_file: abapraise_exception_class.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAISE EXCEPTION

## Syntax

``` abap
RAISE [RESUMABLE] EXCEPTION 
  { {TYPE cx_class [message] [EXPORTING p1 = a1 p2 = a2 ...]}   
  | oref }.  
```

[`message`](abapraise_exception_message.md)

### Addition

[1. `... RESUMABLE`](abapraise_exception_class.md#addition-1)

[2. `... EXPORTING p1 = a1 p2 = a2 ...`](abapraise_exception_class.md#addition-2)

## Overview

### Description

This statement interrupts execution of the current statement block and raises a [class-based exception](../../abap-glossary/abenclass_based_exception_glosry.md). It can be used at any point in a [processing block](../../abap-glossary/abenprocessing_block_glosry.md). The statement interrupts the program flow and searches for a [handler](abapcatch_try.md) as described in [System Response After a Class-Based Exception](abenexceptions_system_response.md). Depending on the definition of the handler, the context of the exception is closed before or after the handler is executed, where some [cleanup tasks](abapcleanup.md) may be performed. During handling, processing can only be resumed again after the statement `RAISE EXCEPTION`, without closing the context, if the addition `RESUMABLE` is specified.

- If the addition `TYPE` is specified, an exception of exception class `cx_class` is raised and, if necessary, an exception object is created. Every exception class `cx_class` visible at this point can be specified after `TYPE`.

  - The addition `EXPORTING` can be used to assign actual parameters to the input parameters of the instance constructor.

  - The addition [`message`](abapraise_exception_message.md) can be used to link the exception object to a [message](../../abap-glossary/abenmessage_glosry.md).

- If `oref` is specified, no new exception object is created when the exception is raised. For `oref`, an object reference variable must be specified that points to an existing exception object. The static type of `oref` must be an exception class, that is, a subclass of `CX_ROOT` or the class itself. `oref` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). In the existing exception object, the internal attributes that describe the position of the exception and that can be read using the method `GET_SOURCE_POSITION` are converted to the position of the statement `RAISE`.

### Hints

- If the addition `TYPE` is used exception objects are only created if they are required for performance reasons, that is:

  - If a suitable `CATCH` block or `CLEANUP` block is specified in a wrapper [`TRY`](abaptry.md) control structure with the addition `INTO`.

  - If the exception is not caught and a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) occurs.

    In principle, however, an exception can be regarded as an instance of an exception object being generated. A difference in behavior can occur only if a non-handled exception of the instance constructor replaces the original exception when the object is generated. However, this situation should never occur.

- If `oref` is specified, either an exception object instantiated using [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) can be used, or an exception that was previously caught during exception handling can be raised again.

- If a caught exception is raised again, note that the exception object does not remain unchanged because the information about the position of the exception is changed. If the original information is to be propagated to an external handler, a new exception of the same class can be raised, passing the original exception object to the `PREVIOUS` parameter of its constructor. It may also be enough to propagate the original exception implicitly, and not raise it again using `RAISE`. The associated original exception object can then be evaluated in the [`CLEANUP`](abapcleanup.md) block, if required

- The exception class after `TYPE` can be specified only statically. To raise an exception dynamically, the dynamic variant of [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object_explicit.md) can be used to create an exception object and specify it using `oref`.

- If a [procedure](../../abap-glossary/abenprocedure_glosry.md) is exited by raising an exception, the content of the formal parameter for which the [pass by value](../../abap-glossary/abenpass_by_value_glosry.md) is defined is not assigned to the respective actual parameters.

- The addition [`THROW`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md) makes it possible to raise a class-based exception in an operand position.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of an exception `cx_demo` in a method.

``` abap
CLASS cx_demo DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth RAISING cx_demo. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    ... 
    RAISE EXCEPTION TYPE cx_demo. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    TRY. 
        cls=>meth( ). 
      CATCH cx_demo. 
        out->write( 'Catching exception' ). 
    ENDTRY. 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of a caught exception of the class `cx_demo` again using the exception object.

``` abap
CLASS cx_demo DEFINITION INHERITING FROM cx_static_check. 
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
            RAISE EXCEPTION TYPE cx_demo. 
          CATCH cx_demo INTO FINAL(exc). 
            out->write( 'Inner CATCH' ). 
            RAISE EXCEPTION exc. 
        ENDTRY. 
      CATCH cx_demo. 
        out->write( 'Outer CATCH' ). 
    ENDTRY. 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of an exception using a dynamically created exception object.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA exception TYPE seoclass-clsname VALUE 'CX_SY_ZERODIVIDE'. 
cl_demo_input=>request( CHANGING field = exception ). 
 
DATA oref TYPE REF TO cx_root. 
exception = to_upper( exception ). 
TRY. 
    CREATE OBJECT oref TYPE (exception). 
  CATCH cx_root INTO DATA(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
TRY. 
    RAISE EXCEPTION oref. 
  CATCH cx_root INTO exc. 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```

### Executable Example

[Exceptions, `RAISE`](abenraise_abexa.md)

## Addition 1

`... RESUMABLE`

### Description

The addition `RESUMABLE` raises an exception as a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md). When an exception of this type is handled in a [`CATCH`](abapcatch_try.md) block, the statement [`RESUME`](abapresume.md) can be used to return to the point directly after the raising statement, as long as the context of the exception was not deleted before the exception was handled.

### Hints

- If the statement `RESUMABLE` is used to raise an exception as a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md), the handler has to determine whether processing is resumed after `RAISE EXCEPTION`, or whether processing of the current context is terminated completely. Both alternatives can occur when an exception is raised. It is important to ensure that [`CLEANUP`](abapcleanup.md) blocks are only executed when the context is deleted.

- When exceptions of the types `CX_STATIC_CHECK` and `CX_DYNAMIC_CHECK` are propagated, which are raised as resumable, they can become non-resumable if the addition `RESUMABLE` is not specified in each interface involved for the addition `RAISING` to declare the exception.

- When exceptions of type `CX_NO_CHECK` are propagated, the resumability is always retained. However, exceptions of type `CX_NO_CHECK` should only be raised as resumable with caution, and it must be ensured that a procedure always has the required behavior.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of a resumable exception `cx_demo` using the addition `RESUMABLE` in a method.

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

## Addition 2

`... EXPORTING p1 = a1 p2 = a2 ...`

### Description

The addition `EXPORTING` can be used to assign suitable actual parameters to the input parameters of the instance constructor of the exception class. The syntax is the same as for the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md).

As in regular method calls, `a1`, `a2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). In other words, expressions can be passed as actual parameters, in addition to data objects. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case.

### Hint

An important input parameter of the instance constructor of an exception class is `TEXTID`, which determines the [exception text](abenexception_texts.md) for the current exception.

- Passing the specification of a text as an actual parameter to the parameter `TEXTID` is not contained in the where-used list of that text. For example, the where-used list of a [message](../../abap-glossary/abenmessage_glosry.md) does not contain this dynamic use of the message.

The addition [`MESSAGE`](abapraise_exception_message.md) is used to link any messages with an exception. This addition cannot be specified with the parameter `TEXTID`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A predefined exception is raised explicitly for which an exception text other than the standard exception text is selected and whose placeholder `&TOKEN&` is filled by passing a value to the attribute with the same name.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TRY. 
    ... 
    RAISE EXCEPTION TYPE cx_sy_dynamic_osql_semantics 
      EXPORTING 
        textid = cx_sy_dynamic_osql_semantics=>unknown_table_name 
        token  = 'Test'. 
    ... 
  CATCH cx_sy_dynamic_osql_semantics INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```
