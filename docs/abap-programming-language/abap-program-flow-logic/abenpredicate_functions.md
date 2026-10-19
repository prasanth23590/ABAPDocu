---
title: "rel_exp - Predicate Functions"
source_file: abenpredicate_functions.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Predicate Functions

The return value of a predicate function is a [truth value](../../abap-glossary/abentruth_value_glosry.md). A predicate function is a special formulation of a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) and, like any relational expression, can be a full [logical expression](../../abap-glossary/abenlogical_expression_glosry.md) or part of one. This means it can be specified as a condition in [control statements](../../abap-glossary/abencontrol_statement_glosry.md) and other statements, as an argument in [Boolean functions](../../abap-glossary/abenboole_function_glosry.md) or [conditional expressions](../../abap-glossary/abenconditional_expression_glosry.md), or in combinations with [Boolean operators](../../abap-glossary/abenboolean_operator_glosry.md).

- [Predicate Functions for Character-Like Arguments](abenpredicate_functions_strgs.md)

- [Predicate Functions for Table-Like Arguments](abenpredicate_functions_tabs.md)

## Hint

The return value of a predicate function cannot be used in all operand positions for data objects since ABAP does not recognize Boolean data objects for the truth values true or false.
