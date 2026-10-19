---
title: "COND, SWITCH, result"
source_file: abenconditional_expression_result.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Conditional Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COND, SWITCH, result

## Syntax

``` abap
...   operand 
  | { THROW [RESUMABLE|SHORTDUMP] cx_class( [message] 
                                            [p1 = a1 p2 = a2 ...] ) } ...  
```

[`message`](abapraise_exception_message.md)

### Alternative

[1. `... operand`](abenconditional_expression_result.md#alternative-1)

[2. `... THROW [RESUMABLE|SHORTDUMP] cx_class( [message] [p1 = a1 p2 = a2 ...] )`](abenconditional_expression_result.md#alternative-2)

## Overview

### Description

These specifications after `THEN` and `ELSE` in the [conditional expressions](../../abap-glossary/abenconditional_expression_glosry.md) [`COND`](abenconditional_expression_cond.md) and [`SWITCH`](abenconditional_expression_cond.md) determine the result of the expression when the corresponding branch is selected.

## Alternative 1

`... operand`

### Description

If an operand `operand` is specified, its value is converted to the data type `type` if necessary and returned as the result of the conditional expression. `operand` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md) with the following restrictions:

- If `operand` is specified as a [string expression](../../abap-glossary/abenstring_expression_glosry.md), `type` must be character-like.

- If `operand` is specified as a [bit expression](../../abap-glossary/abenbit_expression_glosry.md), `type` must be byte-like.

### Hint

When an operand is specified, the conditional operators `COND` and `SWITCH` create a temporary data object whose data type is determined by the specified type and whose content is determined by the selected operand. This data object is used as the operand of a statement and then deleted. It is deleted either when the current statement is completed or when a relational expression is evaluated after the truth value is determined.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of the operands `sum` and `sum + 1`. The number of times a random number is less than half of its maximum value is counted.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( 
  seed = CONV i( t ) min = 1 max = 101 ). 
 
DATA(sum) = 0. 
DO 100 TIMES. 
  sum = COND i( WHEN rnd->get_next( ) <= 50 THEN sum + 1 
                                            ELSE sum ). 
ENDDO. 
out->write( sum ). 
 
out->display( ).
```

## Alternative 2

`... THROW [RESUMABLE|SHORTDUMP] cx_class( [message] [p1 = a1 p2 = a2 ...] )`

### Description

The specification of `THROW` raises either an exception or a runtime error.

- If the addition `SHORTDUMP` is not specified, `THROW` works like the statement [`RAISE EXCEPTION TYPE`](abapraise_exception_class.md) and raises an exception of the [exception class](../../abap-glossary/abenexception_class_glosry.md) `cx_class`. The following applies here:

  - The addition `RESUMABLE` can be used to make the exception resumable.

  - A message can be passed to the exception object using the addition [`message`](abapraise_exception_message.md).

  - The input parameters `p1`, `p2`, ... of the instance constructor can be filled with actual parameters `a1`, `a2`.

- If the addition `SHORTDUMP` is specified, `THROW` works like the statement [`RAISE SHORTDUMP TYPE`](abapraise_shortdump.md) and raises a runtime error with the [exception class](../../abap-glossary/abenexception_class_glosry.md) `cx_class`, whereby a message can be also passed and the input parameters can be filled.

### Hints

- If the exception class is specified after `THROW`, the parentheses must always be specified, even if no messages or actual parameters are passed. `EXPORTING` cannot be specified, nor is it necessary.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of an exception of the class `CX_DEMO_DYN_T100` that implements the interface [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md).

``` abap
DATA cflag TYPE abap_boolean. 
 
... 
 
TRY. 
    FINAL(iflag) = COND i( WHEN cflag = abap_true  THEN 1 
                          WHEN cflag = abap_false THEN 0 
                          ELSE THROW cx_demo_dyn_t100( 
                                 MESSAGE e888(sabapdemos) 
                                   WITH 'Illegal value!' '' '' '' ) ). 
  CATCH cx_demo_dyn_t100. 
    ... 
ENDTRY.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of a runtime error with an exception object of the class `CX_DEMO_DYN_T100`, which implements the interface [`IF_T100_DYN_MSG`](../abap-text-repositories/abenif_t100_dyn_msg.md).

``` abap
FINAL(t) = cl_demo_date_time=>get_user_time( ). 
FINAL(time) = COND t( WHEN t BETWEEN '090000' AND '170000' 
                       THEN t 
                     ELSE 
                       THROW SHORTDUMP cx_demo_dyn_t100( 
                          MESSAGE e888(sabapdemos) 
                                  WITH `I` `don't` `work` `now!` ) ).
```
