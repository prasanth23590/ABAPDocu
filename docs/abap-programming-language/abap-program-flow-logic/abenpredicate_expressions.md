---
title: "rel_exp - Predicate Expressions"
source_file: abenpredicate_expressions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Predicate Expressions

## Syntax

``` abap
...   {operand  IS [NOT] INITIAL} 
    | {ref      IS [NOT] BOUND} 
    | {oref     IS [NOT] INSTANCE OF} 
    | {<fs>     IS [NOT] ASSIGNED} 
    | {para     IS [NOT] SUPPLIED} ... 
    | {operand} ...  
```

[`IS [NOT] INITIAL`](abenlogexp_initial.md) · [`IS [NOT] BOUND`](abenlogexp_bound.md) · [`IS [NOT] INSTANCE OF`](abenlogexp_instance_of.md) · [`IS [NOT] ASSIGNED`](abenlogexp_assigned.md) · [`IS [NOT] SUPPLIED`](abenlogexp_supplied.md)

## Description

A predicate expression uses the [predicate operator](../../abap-glossary/abenpredicate_operator_glosry.md) `IS` to determine a [truth value](../../abap-glossary/abentruth_value_glosry.md) from the state of an operand.

## Hints

- Apart from `INSTANCE OF`, no operands of the possible predicate expressions are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md). No predicate expression can be applied to a [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md).

- [Individual operands](abenpredicative_method_calls.md) without `IS ...` can represent predicate expressions. In this case, `IS NOT INITIAL` is used implicitly.
