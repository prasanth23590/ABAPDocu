---
title: "log_exp - Boolean Operators and Parentheses"
source_file: abenlogexp_boole.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# log_exp - Boolean Operators and Parentheses

The following Boolean operators combine logical expressions:

- [`AND`](abenlogexp_and.md)

- [`OR`](abenlogexp_or.md)

- [`EQUIV`](abenlogexp_equiv.md)

The following operator negates a logical expression:

- [`NOT`](abenlogexp_not.md)

Logical expressions can be parenthesized explicitly using the following:

- [`( )`](abenlogexp_bracket.md)

When multiple Boolean operators are combined, the system implicitly parenthesizes all logical expressions that are not closed by explicit parentheses according to the following hierarchy (operator order, precedence). This expresses the binding strength between Boolean operators:

1.  All Boolean operators `NOT` are combined with the adjacent logical expression on the right to form a logical expression.

2.  All logical expressions combined using `AND` form a logical expression.

3.  All logical expressions combined using `OR` form a logical expression.

4.  All logical expressions combined using `EQUIV` form a logical expression.

The logical expressions of a parenthesis level are processed from left to right. If the value of a logical expression determines the total value of the parenthesis level, the remaining logical expressions are no longer evaluated. In particular, the dynamic parts of the expressions that are not evaluated, such as field symbols or reference variables, are not checked for validity.

## Hints

- If multiple logical expressions are combined, the explicit and implicit parentheses always produce exactly one logical expression that is either true or false.

- The smallest unit of a combined logical expression is always a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md).

- If [functional methods](../../abap-glossary/abenfunctional_method_glosry.md) are used as operands in the involved relational expressions, they are executed directly before the respective relational expression is evaluated. Functional methods in relational expressions that do not need to be evaluated to get the result are not executed.
