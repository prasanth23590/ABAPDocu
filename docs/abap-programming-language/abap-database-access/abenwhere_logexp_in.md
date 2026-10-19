---
title: "sql_cond - IN ( ... )"
source_file: abenwhere_logexp_in.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - IN ( ... )

## Syntax Forms

**[Single Operand](abenwhere_logexp_operand_in.md)**

``` abap
1. ... operand [NOT] IN { (operand1[, operand2[, ...]]) } 
                     | { ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) } ...
```

**[Operand List](abenwhere_logexp_list_in.md)**

``` abap
2. ... ( operand1, operand2[, ...] ) IN { ( ( operand11, operand21[, ...] )[, 
                                           ( operand12, operand22[, ...] )] ) } 
                                     | { ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) } ...
```

[`operand`](abenwhere_logexp_operand_in.md) · [`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`( operand1, operand2[, ...] )`](abenwhere_logexp_list_in.md) · [`subquery_clauses`](abenwhere_logexp_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md)

## Description

This variant of the operator `IN` checks whether the operands on the left side match a value from a set of values specified in parentheses. A [single operand](abenwhere_logexp_operand_in.md) or an [operand list](abenwhere_logexp_list_in.md) can be specified on the left side. The set of values on the right side is determined using either comma-separated lists or subqueries.
