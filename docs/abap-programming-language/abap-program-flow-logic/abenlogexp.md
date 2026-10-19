---
title: "Logical Expressions (log_exp)"
source_file: abenlogexp.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Logical Expressions (log_exp)

## Syntax

``` abap
 ...   rel_exp 
    | [NOT] log_exp [AND|OR|EQUIV log_exp] ...  
```

## Description

A logical expression formulates a condition for operands. The result of a logical expression `log_exp` is a [truth value](../../abap-glossary/abentruth_value_glosry.md), which means it can be true or false.

A logical expression is either a single [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) `rel_exp`, or an expression combined from one or more logical expressions with the [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md) [`NOT`, `AND`, `OR`, `EQUIV`](abenlogexp_boole.md) where [parentheses](abenlogexp_bracket.md) are possible. An atomic component of a compound logical expression is always one of the following relational expressions:

- [Comparisons](../../abap-glossary/abencomparison_glosry.md)

  - [Comparison expressions](abenlogexp_comp.md)

- [Predicates](../../abap-glossary/abenpredicate_glosry.md)

  - [Predicate expressions](abenpredicate_expressions.md)

  - [Predicate functions](abenpredicate_functions.md)

  - [Predicative method calls, data objects as relational expressions](abenpredicative_method_calls.md)

Logical expressions can be used as follows:

- To formulate conditions in [control statements](../../abap-glossary/abencontrol_statement_glosry.md) and other statements used to control the program flow.

- in [conditional expressions](../../abap-glossary/abenconditional_expression_glosry.md)

- As an argument of a [Boolean function](../../abap-glossary/abenboole_function_glosry.md) to represent a truth value in a character-like or byte-like data object.

- In `WHERE` conditions of [processing statements](../abap-processing-internal-data/abentable_processing_statements.md) for [internal tables](../../abap-glossary/abeninternal_table_glosry.md).

## Hints

- The operand positions `operand` of most relational expressions are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md), which means that, depending on the expression, [data objects](../../abap-glossary/abendata_object_glosry.md), [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md), [functional methods](../../abap-glossary/abenfunctional_method_glosry.md), [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md), [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), or [table expressions](../../abap-glossary/abentable_expression_glosry.md) can be specified.

- If [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) are specified as operands of a relational expression in a logical expression, they are executed from left to right and from inside to outside before the relational expression is evaluated. In the case of [combination](abenlogexp_boole.md) of relational expressions, this applies to each individual relational expression and not to the entire logical expression.

- Since ABAP does not recognize Boolean data objects for the truth values true or false, the result of a logical expression cannot currently be directly assigned to a data object, as is possible for [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md). Instead, the return value of a [Boolean function](../../abap-glossary/abenboole_function_glosry.md) can be used.

- Logical expressions cannot be mixed with [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md). However, a logical expression can be listed as an argument of a [Boolean function](../../abap-glossary/abenboole_function_glosry.md) in a suitable calculation expression.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Logical expression that is composed of a predicate expression, a comparison expression, and a predicate function using the Boolean operator `AND`, in a control statement.

``` abap
IF p1 IS SUPPLIED    AND 
   p1 <= upper_limit AND 
   matches( val = p2 pcre = regular_expression ). 
  ... 
ENDIF.
```
