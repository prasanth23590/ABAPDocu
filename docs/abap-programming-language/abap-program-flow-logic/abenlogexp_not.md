---
title: "log_exp - NOT"
source_file: abenlogexp_not.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > log_exp - Boolean Operators and Parentheses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# log_exp - NOT

## Syntax

``` abap
... NOT log_exp ...  
```

## Description

The negation of a logical expression [`log_exp`](abenlogexp.md) using `NOT` creates a new logical expression that is false if the logical expression `log_exp` is true and vice versa.

## Hints

- The operator `NOT` binds stronger than `AND`, `OR`, and `EQUIV`.

- The Boolean operator `NOT` must not be confused with the addition `NOT` of the [comparison operators](../../abap-glossary/abencomp_operator_glosry.md) [`BETWEEN`](abenlogexp_between.md), [`IN`](abenlogexp_select_option.md), and the [predicate operator](../../abap-glossary/abenpredicate_operator_glosry.md) [`IS`](abenpredicate_expressions.md). The following syntax is possible:

  `... NOT operand NOT IN range_tab ...` The first `NOT` is a Boolean operator that negates a comparison expression. The second `NOT` is a part of the comparison expression with&#x200E; the comparison operator `IN`. This is illustrated by parentheses around the comparison expression: `... NOT ( operand NOT IN range_tab ) ...`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Exit the current processing block if `sy-subrc` does not have the value 0.

``` abap
IF NOT sy-subrc = 0. 
  RETURN. 
ENDIF.
```
