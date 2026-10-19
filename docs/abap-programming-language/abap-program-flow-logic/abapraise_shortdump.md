---
title: "RAISE SHORTDUMP"
source_file: abapraise_shortdump.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Runtime Errors"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAISE SHORTDUMP

## Syntax

``` abap
RAISE SHORTDUMP 
  { {TYPE cx_class [message] [EXPORTING p1 = a1 p2 = a2 ...]}   
  | oref }.  
```

[`message`](abapraise_shortdump_message.md)

## Description

This statement interrupts the execution of the current statement block and raises the [runtime error](../../abap-glossary/abenruntime_error_glosry.md) `RAISE_SHORTDUMP`, which performs a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). This runtime error is linked with an [exception object](../../abap-glossary/abenexception_object_glosry.md) using `TYPE` or `oref`:

- If the addition `TYPE` is specified, an exception object of the [exception class](../../abap-glossary/abenexception_class_glosry.md) `cx_class` is created. Every exception class `cx_class` visible at this point can be specified after `TYPE`. The [exception category](../../abap-glossary/abenexception_category_glosry.md) is ignored.

  - The addition `EXPORTING` can be used to assign actual parameters to the input parameters of the instance constructor. The syntax and semantics are the same as for the statement [`RAISE EXCEPTION`](abapraise_exception_class.md).

  - The addition [`message`](abapraise_shortdump_message.md) can be used to link the exception object to a [message](../../abap-glossary/abenmessage_glosry.md).

- If `oref` is specified, no new exception object is created. `oref` expects an object reference variable that points to an existing exception object. The static type of `oref` must be an exception class, that is, a subclass of `CX_ROOT` or the class itself. `oref` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). In the existing exception object, the internal attributes that describe the location of the exception are converted to the position of the `RAISE` statement.

The [short dump](../../abap-glossary/abenshort_dump_glosry.md) of the runtime error contains the name of the exception class and the exception text. The attributes of the exception object can be listed in the transaction `ST22`. Under *Chain of Exception Objects*, the long text of the short dump contains the attributes referenced in the attribute `PREVIOUS` of the exception object.

## Hints

- The statement `RAISE SHORTDUMP` works in roughly the same way as when raising a [class-based exception](../../abap-glossary/abenclass_based_exception_glosry.md) that does not have a handler. There is no [propagation from procedures](abenexceptions_procedures.md), however, which removes the risk of violating interfaces and raising further exceptions such as `CX_SY_NO_HANDLER`. This means that the [exception category](../../abap-glossary/abenexception_category_glosry.md) of the used exception class is not relevant in `RAISE SHORTDUMP`.

- The statement `RAISE SHORTDUMP` does not raise [class-based exception](../../abap-glossary/abenclass_based_exception_glosry.md) that can be caught using [`CATCH`](abapcatch_try.md). The exception object is used exclusively for the transport of information to the short dump.

- The statement `RAISE SHORTDUMP` is an alternative to raising [exit messages](../../abap-glossary/abenexit_message_glosry.md), that is, [messages](../../abap-glossary/abenmessage_glosry.md) of type *X*. The attributes of the exception class can be used to send more information about an error to the short dump than a message text. More specifically, the attribute `PREVIOUS` can reference previous exceptions.

- If `oref` is specified, either an exception object instantiated using [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) or [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) can be used or a previously caught exception can be transformed into a runtime error in exception handling.

- If a caught exception is transformed into a runtime error, it should be noted that the exception object does not remain unchanged and the information about the position of the exception is changed instead. If the original information is transported to the short dump, a new exception object of the same class can be created. The original exception object is passed to the constructor parameter `PREVIOUS` of the new object.

- The addition [`THROW SHORTDUMP`](abenconditional_expression_result.md) in a [conditional expression](abenconditional_expressions.md) makes it possible to raise a runtime error in an operand position.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of a runtime error with an exception object of the exception class `CX_DEMO_T100`. The instance constructor is supplied with parameters that define the exception text and supply any variable text parts with values.

``` abap
RAISE SHORTDUMP TYPE cx_demo_t100 
     EXPORTING 
       textid = cx_demo_t100=>demo 
       text1  = 'I' 
       text2  = 'need' 
       text3  = 'a' 
       text4  = 'break!'.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the previous example, but the exception object is created first and not in the statement `RAISE SHORTDUMP`.

``` abap
FINAL(oref) = NEW cx_demo_t100( 
  textid = cx_demo_t100=>demo 
  text1  = 'I' 
  text2  = 'need' 
  text3  = 'a' 
  text4  = 'break!' ). 
 
RAISE SHORTDUMP oref.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of a runtime error when an exception is handled. A reference to the preceding exception object of the class `cx_sy_zerodivide` is passed to the attribute `PREVIOUS` of the created exception object of the class `cx_demo`. The *chain of exception objects* is listed in the long text of the short dump.

``` abap
CLASS cx_demo DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main RAISING cx_sy_zerodivide. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    FINAL(num) = 1 / 0. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS user DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main RAISING cx_sy_zerodivide. 
ENDCLASS. 
 
 
CLASS user IMPLEMENTATION. 
  METHOD main. 
    TRY. 
        demo=>main( ). 
      CATCH cx_sy_zerodivide INTO FINAL(oref). 
        RAISE SHORTDUMP TYPE cx_demo EXPORTING previous = oref. 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```
