---
title: "Exceptions, TRY"
source_file: abentry_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Examples of Exceptions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exceptions, TRY

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the `TRY` control structure.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_try DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    DATA: result TYPE p LENGTH 8 DECIMALS 2, 
          oref   TYPE REF TO cx_root, 
          text   TYPE string. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA number TYPE i. 
    METHODS calculation 
      IMPORTING p_number LIKE number 
      CHANGING  p_result LIKE result 
                p_text   LIKE text 
      RAISING   cx_sy_arithmetic_error. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_try IMPLEMENTATION. 
  METHOD main. 
 
    cl_demo_input=>new( )->request( CHANGING field = number ). 
    TRY. 
        IF abs( number ) > 100. 
          RAISE EXCEPTION TYPE cx_demo_abs_too_large. 
        ENDIF. 
        calculation( EXPORTING p_number = number 
                     CHANGING  p_result = result 
                               p_text   = text ). 
      CATCH cx_sy_arithmetic_error INTO oref. 
        text = oref->get_text( ). 
      CATCH cx_root INTO oref. 
        text = oref->get_text( ). 
    ENDTRY. 
    IF NOT text IS INITIAL. 
      out->write( text ). 
    ENDIF. 
    out->write( |Final result: { result ALIGN = LEFT }| ). 
  ENDMETHOD. 
  METHOD calculation. 
    DATA l_oref TYPE REF TO cx_root. 
    TRY. 
        p_result =  1 / p_number. 
        out->write( 
          |Result of division: { p_result ALIGN = LEFT }| ). 
        p_result = sqrt( p_number ). 
        out->write( 
          |Result of square root: { p_result ALIGN = LEFT }| ). 
      CATCH cx_sy_zerodivide INTO l_oref. 
        p_text = l_oref->get_text( ). 
      CLEANUP. 
        CLEAR p_result. 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

- If the content of `number` is greater than 100, the `TRY` control structure of the [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md) raises an exception of the class `CX_DEMO_ABS_TOO_LARGE` in the `TRY` block. This exception is handled by the second `CATCH` block of the same `TRY` control structure, since the subclass of the most general exception is `CX_ROOT`.

- If the content of `number` is 0, the runtime framework in the `TRY` block of the `TRY` control structure of the called method `calculation` raises an exception of the predefined class `CX_SY_ZERODIVIDE`. This is handled in the `CATCH` block of the same `TRY` control structure.

- If the content of `number` is a negative number, the runtime framework in the `TRY` block of the `TRY` control structure of the called method `calculation` raises an exception of the predefined class `CX_SY_ARG_OUT_OF_DOMAIN`. Since no handler is defined for this exception in this `TRY` control structure, the exception is propagated from the method, which is made possible by the declaration of the superclass `CX_SY_ARITHMETIC_ERROR` using `RAISING` in the method interface. The `CLEANUP` block of the inner `TRY` control structure is executed first.

- Any other exceptions are handled in the final `CATCH` block of the `TRY` control structure of the compilation unit, which catches all possible exceptions by specifying the most generic exception class `CX_ROOT`. If, for example, `CX_SY_ARG_OUT_OF_DOMAIN` or one of its superclasses was not declared in the method interface, the exception `CX_SY_NO_HANDLER` would be raised and would be handled in the final `CATCH` block.
