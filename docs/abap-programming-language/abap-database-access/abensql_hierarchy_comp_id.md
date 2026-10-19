---
title: "sql_func - Hierarchy Composite ID Function"
source_file: abensql_hierarchy_comp_id.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Hierarchy Composite ID Function

## Syntax

``` abap
... HIERARCHY_COMPOSITE_ID( sql_exp1, ..., sql_expn ) ...  
```

## Description

Calls the hierarchy composite ID function as an [SQL expression](abapsql_expr.md) or operand of an expression in ABAP SQL. The hierarchy composite ID function can have a comma-separated list with at least one argument.

This function concatenates multicolumn tuple-like node identifiers into single scalar values.

The arguments can be any [SQL expressions](abapsql_expr.md) that can be cast to `SSTRING`. The result type is `SSTRING`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Generates a composite node identifier `num` that is free of name clashes. Additionally, the length of the components is returned.

``` abap
SELECT FROM demo_expressions 
  FIELDS num1 AS num1, 
         num2 AS num2, 
         hierarchy_composite_id( num1, num2 ) AS num 
  INTO TABLE @DATA(result).
```
