---
title: "COND, Conditional Operator"
source_file: abenconditional_expression_cond.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Conditional Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COND, Conditional Operator

## Syntax

``` abap
... COND type( [let_exp] 
               WHEN log_exp1 THEN [let_exp] result1 
             [ WHEN log_exp2 THEN [let_exp] result2 ] 
             ... 
             [ ELSE [let_exp] resultn ] ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md) · [`log_exp1`](abenlogexp.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`result1`](abenconditional_expression_result.md) · [`log_exp2`](abenlogexp.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`result2`](abenconditional_expression_result.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`resultn`](abenconditional_expression_result.md)

## Description

A [conditional expression](../../abap-glossary/abenconditional_expression_glosry.md) with the conditional operator `COND` has a result [`result`](abenconditional_expression_result.md) that is dependent on logical expressions. Either a value with the data type specified by `type` is created or a class-based exception is raised. The following can be specified for `type`:

- A non-generic data type `dtype`.

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md).

  - If the data type required in an operand position is unique and known completely, this type is used.

  - If the operand type is not known completely, an operand with a type known statically must be specified after the first `THEN`, except when passing the constructor parameter to an actual parameter with a generically typed formal parameter, and this type is then used. No [`THROW`](abenconditional_expression_result.md) statement can be specified after `THEN` in this case.

  - If the constructor expression is passed to an actual parameter with a generically typed formal parameter, the operand type is derived in accordance with [special rules](abencond_constructor_inference.md).

  - In other cases, the character `#` cannot be specified.

All operands specified after `THEN` must be convertible to the data type determined by `type`. In the case of reference variables, an [upcast](../../abap-glossary/abenup_cast_glosry.md) must be possible.

`WHEN` must be specified at least once with any [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) [`log_exp`](abenlogexp.md) in the parentheses. This can be followed by any number of `WHEN` statements with further logical expressions. An `ELSE` can be specified at the end. The expression evaluates the logical expressions one after the other and selects the [`result`](abenconditional_expression_result.md) specified after `THEN` of the first logical expression whose result is true. The selected [`result`](abenconditional_expression_result.md) determines the result of the conditional expression. If none of the logical expressions are true, the [`result`](abenconditional_expression_result.md) specified after `ELSE` is selected. If `ELSE` is not specified, the result is the initial value of the data type `type`.

To define local helper fields, an optional [`LET` expression](../abap-declarations/abaplet.md) can be specified before the first `WHEN`, after every `THEN`, and after `ELSE`.

## Hints

- The rules for derivations of the type where `#` is specified for actual parameters that are passed to generically typed formal parameters can prevent syntax errors in programs that call a procedure and in which the complete typing of a formal parameter is subsequently generalized by converting to a generic type.

- No suitable complete type can be derived for formal parameters with the generic types `c`, `n`, and `x`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Transformation of a time to 12 hour format using a conditional expression in an operand position. The type of the result is used by the operand after the first `THEN` specification and is therefore `string`.

``` abap
CLASS cx_cant_be DEFINITION INHERITING FROM cx_no_check. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    FINAL(time) = cl_demo_date_time=>get_user_time( ). 
    out->write( 
      COND #( LET t = '120000' IN 
              WHEN time < t THEN 
                |{ time TIME = ISO } AM| 
              WHEN time > t AND time < '240000' THEN 
                |{ CONV t( time - 12 * 3600 ) TIME = ISO } PM| 
              WHEN time = t THEN 
                `High Noon` 
              ELSE 
                THROW cx_cant_be( ) ) ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
