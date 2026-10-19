---
title: "log_exp - EQUIV"
source_file: abenlogexp_equiv.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > log_exp - Boolean Operators and Parentheses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# log_exp - EQUIV

## Syntax

``` abap
... log_exp1 EQUIV log_exp2 ...  
```

## Description

Combining two logical expressions [`log_exp`](abenlogexp.md) with `EQUIV` creates a new logical expression that is true if both expressions are true or both expressions are false. If one of the expressions is true and the other one is false, the combined expression is false.

Within a [parenthesis level](abenlogexp_bracket.md), only two logical expressions can be combined using `EQUIV`.

## Hints

- The operator `EQUIV` binds weaker than `NOT`, `AND`, and `OR`.

- The operator `EQUIV` implements an equivalence operation. Negating such an operation using [`NOT`](abenlogexp_not.md) is the same as using an `XOR` operation (`eXclusive OR`). It is true if one of the expressions is true and the other one is false.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The condition in the `IF` statement is true if `o1`, `o2`, and `o3`, `o4` are either both equal or both unequal.

``` abap
DATA: o1 TYPE i, 
      o2 TYPE i, 
      o3 TYPE i, 
      o4 TYPE i. 
 
... 
 
IF o1 = o2 EQUIV o3 = o4. 
  ... 
ENDIF.
```
