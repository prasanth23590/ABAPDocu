---
title: "rel_exp - IS INITIAL"
source_file: abenlogexp_initial.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - IS INITIAL

## Syntax

``` abap
... operand IS [NOT] INITIAL ...  
```

## Description

This predicate expression checks whether the operand `operand` is initial. The expression is true, if the operand contains its type-dependent [initial value](../../abap-glossary/abeninitial_value_glosry.md). Any data objects can be specified for `operand`. This is an extended functional operand position in which, in addition to [functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md), [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), or [table expressions](../../abap-glossary/abentable_expression_glosry.md), certain built-in functions can also be specified.

With the addition `NOT`, the expression is true if the operand contains a value other than its type-dependent initial value

## Hints

- The expression `IS [NOT] INITIAL` is suitable for checking the type-dependent initial value regardless of its actual data type, instead of comparing it with a type-compliant operand that contains the initial value.

- If a [functional method call](../../abap-glossary/abenfunctional_method_call_glosry.md) is specified as `operand`, a potential short form of the following:

  `... operand IS NOT INITIAL ...` is a [predicative method call](abenpredicative_method_calls.md).

- The fact that built-in functions or expressions can be specified as operands should not always be exploited, e.g.:

  - It is better to use `str IS INITIAL` or `itab IS INITIAL` instead of `strlen( str ) IS INITIAL` or `lines( itab ) IS INITIAL`.

  - It is better to use the predicate function [`matches`](abenmatches_functions.md) instead of [`match( ... )`](../abap-processing-internal-data/abenmatch_functions.md) IS INITIAL.

  - It is better to evaluate the operands of the constructor expression instead of [`VALUE type( ... )`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) IS INITIAL.

- An [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) can be specified for `operand`. The initial value is checked in accordance with its [base type](../../abap-glossary/abenbase_type_glosry.md).

- [Calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md) cannot be specified for `operand`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The logical expression in the `IF` statement is true if the internal table in the `SELECT` statement was filled with lines.

``` abap
DATA spfli_tab TYPE TABLE OF spfli. 
... 
CLEAR spfli_tab. 
SELECT * 
       FROM spfli 
       WHERE ... 
       INTO TABLE @spfli_tab. 
 
IF spfli_tab IS NOT INITIAL. 
  ... 
ENDIF.
```
