---
title: "sql_func - UUID Function"
source_file: abensql_uuid.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - UUID Function

## Syntax

``` abap
... UUID( ) ...  
```

## Description

Calls the UUID function as an [SQL expression](abapsql_expr.md) or operand of an expression in ABAP SQL. The function `UUID` does not have any parameters and creates a new unique [UUID](../../abap-glossary/abenuuid_glosry.md) of the type [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with the length 16 for each row read from the result set.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a UUID for each row read from the DDIC database table `SCARR`. These UUIDs are unique for each row and for each execution of the statement.

``` abap
SELECT carrid, carrname, uuid( ) AS uuid 
       FROM scarr 
       INTO TABLE @FINAL(result). 
 
cl_demo_output=>display( result ).
```
