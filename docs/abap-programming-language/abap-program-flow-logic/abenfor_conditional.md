---
title: "FOR, Conditional Iteration"
source_file: abenfor_conditional.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions > FOR, Iteration Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR, Conditional Iteration

## Syntax

``` abap
 ... FOR var = rhs [THEN expr] UNTIL|WHILE log_exp [let_exp] ...  
```

[`log_exp`](abenlogexp.md) · [`let_exp`](../abap-declarations/abaplet.md)

## Description

This syntax form of an [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) executes a conditional iteration.

- If it is used in a constructor expression with the reduction operator [`REDUCE`](abenconstructor_expression_reduce.md), the reduction result is created in the iteration steps.

- If it is used in a constructor expression with the instance operator [`NEW`](../abap-creating-objects-and-values/abennew_constructor_params_itab.md) or with the value operator [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md) for internal tables, new table lines are created in the iteration steps and inserted into the tabular result.

The operands of the iteration expression must be specified as follows:

- First, a local helper variable `var` must be declared as an iteration variable and assigned a start value `rhs` with `=`. The same applies to the namespace and visibility of `var` as to the helper fields declared in a [`LET` expression](../abap-declarations/abaplet.md). The syntax of the declaration is exactly the same as in a [`LET` expression](../abap-declarations/abaplet.md) and it follows the rules that apply here.

- The next position depends on the data type of the iteration variable `var`:

  - If the iteration variable `var` does not have a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md) and is not of type `d` or `t`, an expression `expr` must be specified after `THEN`. The result of this expression can be converted into a data type of `var`. The expression is calculated for every iteration and its result is assigned to the iteration variable `var`. This is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

  - If the iteration variable `var` has a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md), or is of type `d` or `t`, `THEN expr` is optional. If `THEN expr` is not specified explicitly, `THEN var + 1` is added implicitly or the value of the iteration variable is increased by 1 for every iteration.

- Afterwards, a termination condition [`log_exp`](abenlogexp.md) must be specified after `UNTIL` or `WHILE`. `log_exp` is any [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) whose operands can be any data objects visible at this position and any calls possible here.

  - If the termination condition is specified after `UNTIL`, the logical expression `log_exp` is evaluated after every iteration step. If the result of the logical expression is true, the iteration is ended. At least one iteration step is executed.

  - If the termination condition is specified after `WHILE`, the logical expression `log_exp` is evaluated before every iteration step. If the result of the logical expression is false, the iteration is terminated. If the result of the logical expression is already false before the first iteration step, no iteration steps are executed.

- An optional `LET` expression [`let_exp`](../abap-declarations/abaplet.md) can be specified at the end to define local helper fields that can be used in the context of the `FOR` loop. The helper fields are filled in every iteration step and can be used to construct the result.

The variables declared in `FOR` expressions are local. The local data of all outer `FOR` expressions can be used when their values are set. The iteration variable and any helper variables can be used after the `FOR` expression, either in additional subexpressions or to construct the result.

The system field `sy-index` is not set by a `FOR` expression.

## Hints

- Usually, the expression `expr` (after `THEN`) and the termination condition `log_exp` after `UNTIL` or `WHILE` depend on the iteration variable `var`, but this not a prerequisite. The value of the iteration variable or the termination condition can also be determined in other ways. Status changes, for example, can be queried using method calls.

- Usually, a termination condition after `UNTIL` is preferable to a termination condition after `WHILE` in all cases where the termination condition does not have to be checked before the first iteration step.

- In many cases, iteration expressions for conditional iterations can replace [`DO`](abapdo.md) and [`WHILE`](abapwhile.md) loops, which construct values and internal tables.

- Multiple sequential `FOR` expressions with different variants, including the [tabular iterations](../abap-processing-internal-data/abenfor_itab.md), can be specified in a constructor expression. These expressions then work in the same way as nested loops.

- Unlike in a [`LET` expression](../abap-declarations/abaplet.md), a local field symbol cannot be declared instead of the iteration variable `var`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example creates a string from the numbers 0 to 9.

``` abap
cl_demo_output=>display( 
  REDUCE string( INIT s = `` 
                 FOR  i = 1 UNTIL i > 10 
                 NEXT s &&= |{ i - 1 }| ) ).
```

## Executable Examples

[Examples of Iteration Expressions](abeniteration_expressions_abexas.md)
