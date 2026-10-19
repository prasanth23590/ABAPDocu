---
title: "rel_exp - Ternary Comparison Operator BETWEEN"
source_file: abenlogexp_between.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators > rel_exp - Comparison Operators for All Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Ternary Comparison Operator BETWEEN

## Syntax

``` abap
... operand [NOT] BETWEEN operand1 AND operand2 ...  
```

## Description

A comparison expression with the comparison operator `BETWEEN` checks the assignment of an interval. The comparison expression checks whether the content of an operand `operand` is within a closed interval that is restricted by the operands `operand1` and `operand2`. The ternary comparison expression is equivalent to the following combination of two binary comparison expressions:

... \[[`NOT`](abenlogexp_boole.md)\] ( operand [`>=`](abenlogexp_any_operand.md) operand1 [`AND`](abenlogexp_boole.md) operand [`<=`](abenlogexp_any_operand.md) operand2 ) ...

All operands are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md) and the usual [comparison rules](abenlogexp_rules.md) apply.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Check whether today is a working day and assigning the result to a variable declared inline.

``` abap
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
FINAL(day_of_week) = ( 5 + date  MOD 7 ) MOD 7 + 1. 
DATA(work_day_flag) = xsdbool( day_of_week BETWEEN 1 AND 5 ).
```
