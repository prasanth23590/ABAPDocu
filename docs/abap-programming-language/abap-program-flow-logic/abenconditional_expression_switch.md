---
title: "SWITCH, Conditional Operator"
source_file: abenconditional_expression_switch.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Conditional Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SWITCH, Conditional Operator

## Syntax

``` abap
... SWITCH type( [let_exp] 
                 operand 
                 WHEN const1 THEN [let_exp] result1 
               [ WHEN const2 THEN [let_exp] result2 ] 
               ... 
               [ ELSE [let_exp] resultn ] ) ...  
```

[`let_exp`](../abap-declarations/abaplet.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`result1`](abenconditional_expression_result.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`result2`](abenconditional_expression_result.md) · [`let_exp`](../abap-declarations/abaplet.md) · [`resultn`](abenconditional_expression_result.md)

## Description

A [conditional expression](../../abap-glossary/abenconditional_expression_glosry.md) with the conditional operator `SWITCH` has a result, [`result`](abenconditional_expression_result.md), that is dependent on a case distinction. Either a value with the data type specified by `type` is produced or a class-based exception is raised. The following can be specified for `type`:

- A non-generic data type `dtype`.

- The `#` character as a symbol for the [operand type](../../abap-glossary/abenoperand_type_glosry.md).

  - If the data type required in an operand position is unique and known completely, this type is used.

  - If the operand type is not known completely, an operand with a type known statically must be specified after the first `THEN`, except when passing the constructor parameter to an actual parameter with a generically typed formal parameter, and this type is then used. No [`THROW`](abenconditional_expression_result.md) statement can be specified after `THEN` in this case.

  - If the constructor expression is passed to an actual parameter with a generically typed formal parameter, the operand type is derived in accordance with [special rules](abencond_constructor_inference.md).

  - In other cases, the character `#` cannot be specified.

All operands specified after `THEN` must be convertible to the data type determined by `type`. In the case of reference variables, an [upcast](../../abap-glossary/abenup_cast_glosry.md) must be possible.

The position `operand` in the parentheses is the value that is checked in the case distinction. This is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). It must be followed by at least one `WHEN`. Literals and [constants](../../abap-glossary/abenconstant_glosry.md) can be specified for `const` after `WHEN`. It must be possible to [compare](abenlogexp_rules.md) them with `operand`. [Substring access](../abap-operands/abenoffset_length.md) is not possible. This can be followed by any number of `WHEN` statements with further constant values. An `ELSE` can be specified at the end. This expression compares the values of the operand `operand` with the specified constant values one after another and chooses the [`result`](abenconditional_expression_result.md) after `THEN` for which the values of operand and constant are identical for the first time. The selected [`result`](abenconditional_expression_result.md) determines the result of the conditional expression. If no matches are found, the [`result`](abenconditional_expression_result.md) specified after `ELSE` is selected. If `ELSE` is not specified, the result is the initial value of the data type `type`.

If a specification after `THEN` or `ELSE` can be selected, either the result is set or a class-based exception is raised, just as with a conditional expression [`COND`](abenconditional_expression_cond.md).

To define local helper fields, an optional [`LET` expression](../abap-declarations/abaplet.md) can be specified in front of the operand `operand`, after every `THEN`, and after `ELSE`.

## Hints

- No [text symbols](../../abap-glossary/abentext_symbol_glosry.md) for `const` can be specified after `WHEN`.

- A conditional expression with `SWITCH` has the same meaning as the following conditional expression with [`COND`](abenconditional_expression_cond.md):

  `COND type( WHEN operand = const1 THEN result1 [ WHEN operand = const2 THEN result2 ] ... [ ELSE resultn ] )`

- The rules for derivations of the type where `#` is specified for actual parameters that are passed to generically typed formal parameters can prevent syntax errors in programs that call a procedure and in which the complete typing of a formal parameter is subsequently generalized by converting to a generic type.

- No suitable complete type can be derived for formal parameters with the generic types `c`, `n`, and `x`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conditional operator `SWITCH` in an operand position in a loop. The loop is exited when the exception after `ELSE` is caught.

``` abap
CLASS cx_overflow DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
    DO. 
      TRY. 
          out->write( 
            SWITCH string( sy-index 
                           WHEN 1 THEN 'one' 
                           WHEN 2 THEN 'two' 
                           WHEN 3 THEN 'three' 
                           ELSE THROW cx_overflow( ) ) ). 
        CATCH cx_overflow. 
          out->display( ). 
          EXIT. 
      ENDTRY. 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```
