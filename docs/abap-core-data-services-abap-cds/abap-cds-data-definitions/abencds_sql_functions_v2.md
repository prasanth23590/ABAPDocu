---
title: "CDS DDL - CDS View Entity, sql_functions"
source_file: abencds_sql_functions_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, sql_functions

## Syntax

``` abap
... func( arg1[, arg2] ... ) ...  
```

## Description

Calls built-in [SQL functions](../../abap-glossary/abensql_function_glosry.md) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). For passed arguments `arg1`, `arg2`, ..., a built-in SQL function returns a numeric, character-like, or byte-like result. The possible functions are:

- [Numeric functions](abencds_sql_functions_numeric_v2.md)

- [String functions](abencds_sql_functions_character_v2.md)

- [Coalesce function](abencds_coalesce_expression_v2.md)

If an argument contains the [null value](../../abap-glossary/abennull_value_glosry.md), the result is always the null value, except in the coalesce function. If an argument contains an invalid value or the value range of a result type is exceeded, an exception is raised.
