---
title: "log_exp - ( )"
source_file: abenlogexp_bracket.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > log_exp - Boolean Operators and Parentheses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# log_exp - ( )

## Syntax

``` abap
... ( log_exp ) ...  
```

## Description

A complete logical expression [`log_exp`](abenlogexp.md) can be placed in parentheses in order to define the priority of processing. `log_exp` can be a combination of multiple expressions using [`AND`](abenlogexp_and.md), [`OR`](abenlogexp_or.md), or [`EQUIV`](abenlogexp_equiv.md) or a logical expression negated using [`NOT`](abenlogexp_not.md). A logical expression in parentheses is itself a logical expression.

## Hint

The smallest unit of a logical expression that can be placed in parentheses is a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A combination of the following logical expressions

NOT log_exp1 OR log_exp2 AND NOT log_exp3 AND log_exp4 EQUIV log_exp5

can be parenthesized explicitly as follows to stress the [implicit parentheses](abenlogexp_boole.md):

Parentheses around the expressions with `NOT`

``` abap
( NOT log_exp1 ) OR 
log_exp2 AND ( NOT log_exp3 ) AND log_exp4 EQUIV log_exp5
```

Parentheses around the expressions with `AND`

``` abap
( NOT log_exp1 ) OR 
( log_exp2 AND ( NOT log_exp3 ) AND log_exp4 ) EQUIV log_exp5
```

Parentheses around the expressions with `OR`

``` abap
( ( NOT log_exp1 ) OR 
  ( log_exp2 AND ( NOT log_exp3 ) AND log_exp4 ) ) EQUIV log_exp5
```

Parentheses around the expressions with `EQUIV`

``` abap
( ( ( NOT log_exp1 ) OR 
  ( log_exp2 AND ( NOT log_exp3 ) AND log_exp4 ) ) EQUIV log_exp5 )
```

Changing the parentheses explicitly changes the meaning of the expression. For example, if explicit parentheses are set as follows in the expression above

``` abap
( NOT log_exp1 OR log_exp2 ) AND 
NOT ( log_exp3 AND log_exp4 EQUIV log_exp5 )
```

the expression looks as follows after implicit parentheses are set:

``` abap
( ( ( NOT log_exp1 ) OR log_exp2 ) AND 
( NOT ( ( log_exp3 AND log_exp4 ) EQUIV log_exp5 ) ) )
```
