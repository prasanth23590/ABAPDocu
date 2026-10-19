---
title: "log_exp - AND"
source_file: abenlogexp_and.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > log_exp - Boolean Operators and Parentheses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# log_exp - AND

## Syntax

``` abap
... log_exp1 AND log_exp2 AND log_exp3 ...  
```

## Description

The combination of multiple logical expressions [`log_exp`](abenlogexp.md) using `AND` creates a new logical expression that is true if all logical expressions `log_exp` are true. If one of the logical expressions is false, the combined expression is also false.

## Hints

- The operator `AND` binds weaker than `NOT` and stronger than `OR` and `EQUIV`.

- The operator `AND` implements an `AND` operation. Using [`NOT`](abenlogexp_not.md) to negate such a operation is the same as using a `NAND` operation. It is true if at least one expression is false.

- The Boolean operator `AND` should not be confused with the addition `AND` of the [comparison operator](../../abap-glossary/abencomp_operator_glosry.md) [`BETWEEN`](abenlogexp_between.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Check of an assignment to an interval, ignoring interval boundaries.

``` abap
IF operand > limit1 AND operand < limit2. 
  ... 
ENDIF.
```
