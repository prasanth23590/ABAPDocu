---
title: "ABAP SQL - SQL Conditions sql_cond"
source_file: abenasql_cond.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - SQL Conditions sql_cond

## Syntax

``` abap
 ...   rel_exp 
    | [NOT] sql_cond [AND|OR sql_cond] ...  
```

## Description

Logical expression `sql_cond` for formulating a condition in ABAP SQL. A logical expression consists of either a single relational expression `rel_exp`, or an expression composed of the Boolean operators [`NOT`](abenwhere_logexp_andornot.md), [`AND`](abenwhere_logexp_andornot.md), or [`OR`](abenwhere_logexp_andornot.md) and one or more logical expressions, in which parentheses are possible. An atomic component of a compound logical expression is always one relational expression. There are different types of relational expressions:

- [Relational expressions for statements](abenabap_sql_stmt_logexp.md)

- [Relational expressions for expressions](abenabap_sql_expr_logexp.md)
