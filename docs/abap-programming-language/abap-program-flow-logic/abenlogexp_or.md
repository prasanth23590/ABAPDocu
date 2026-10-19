---
title: "log_exp - OR"
source_file: abenlogexp_or.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > log_exp - Boolean Operators and Parentheses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# log_exp - OR

## Syntax

``` abap
... log_exp1 OR log_exp2 OR log_exp3 ...  
```

## Description

If multiple logical expressions [`log_exp`](abenlogexp.md) are combined using `OR`, a new logical expression is created that is true if at least one of the logical expressions `log_exp` is true. The combination is false only if all logical expressions of the combination are false.

## Hints

- The operator `OR` binds weaker than `NOT` or `AND` and binds stronger than `EQUIV`.

- The operator `OR` implements an `OR` operation. Negating such an operation using [`NOT`](abenlogexp_not.md) is the same as using a `NOR` operation. It is true if all expressions are false.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Check whether the local time is within one of two intervals. The language elements `AND` are not Boolean operators in this case but belong to the comparison operator [`BETWEEN`](abenlogexp_between.md).

``` abap
FINAL(time) = cl_demo_date_time=>get_user_time( ). 
IF time BETWEEN '080000' AND '120000' OR 
   time BETWEEN '130000' AND '170000'. 
  ... 
ENDIF.
```
