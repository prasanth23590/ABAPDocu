---
title: "sql_exp - sql_null"
source_file: abensql_null.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_null

## Syntax

``` abap
... NULL ...  
```

## Description

Special null expression in ABAP SQL. The operand `NULL` represents the [null value](../../abap-glossary/abennull_value_glosry.md). Null expressions are context-dependent and the type of `NULL` is determined by the [context](../../abap-glossary/abenobj_context_glosry.md). Generally, null expressions can be used in operand positions of [SQL expressions](abapsql_expr.md). Any exception is documented for the respective position.

## Hints

- At any operand position, it must be possible to determine an exact type for `NULL`. If this is not the case, a syntax error occurs or a catchable exception is raised.

- The expression `NULL` must not be confused with the relational expression with the predicate syntax [`IS [NOT] NULL`](abenwhere_logexp_null.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Returns the airline code, flight connection number, null value, and distance of all Lufthansa flights. When passing `NULL` to the result table, the null value is converted to the initial value.

``` abap
SELECT FROM spfli 
       FIELDS carrid, 
              connid, 
              CAST( NULL AS INT1 ) AS start, 
              distance 
       WHERE carrid = 'LH' 
       INTO TABLE @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Executable Example

[SQL Expressions, Null Expression](abensql_expr_null_abexa.md)
