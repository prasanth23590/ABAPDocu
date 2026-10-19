---
title: "rel_exp - IS SUPPLIED"
source_file: abenlogexp_supplied.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - IS SUPPLIED

## Syntax

``` abap
... para IS [NOT] SUPPLIED ...  
```

## Description

This predicate expression checks whether a formal parameter `para` of a [procedure](../../abap-glossary/abenprocedure_glosry.md) is filled or requested. The expression is true if an actual parameter was assigned to the formal parameter when it was called.

This relational expression is only possible in function modules and methods. For `para`, all optional formal parameters can be specified.

With the addition `NOT`, the expression is true if no actual parameter was assigned to the formal parameter in the call.

## Hints

- In a [functionally called](../../abap-glossary/abenfunctional_method_call_glosry.md) [functional method](../../abap-glossary/abenfunctional_method_glosry.md), the predicate expression `IS SUPPLIED` is true for its return value. In this case, a temporary actual parameter is always bound to the return value, which is used as the operand of the current operand position.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The logical expression of the first `IF` statement in method `m1` is true if an actual parameter is assigned to formal parameter `p1` at the call. The check for the initial value would not be sufficient here, because this is the value of the replacement parameter specified with `DEFAULT`. The logical expression of the second `IF` statement is true if at the call no actual parameter is assigned to formal parameter `p2`.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS m1 IMPORTING p1 TYPE i DEFAULT 0 
                     EXPORTING p2 TYPE i. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    IF p1 IS SUPPLIED. 
      ... 
    ELSE. 
      ... 
    ENDIF. 
    IF p2 IS NOT SUPPLIED. 
      RETURN. 
    ELSE. 
      ... 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```
