---
title: "CDS DDL - DDIC-Based View, sql_functions"
source_file: abencds_sql_functions_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, sql_functions

## Syntax

``` abap
... func( arg1[, arg2] ... ) ...  
```

## Description

Calls built-in [SQL functions](../../abap-glossary/abensql_function_glosry.md) in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). For passed arguments `arg1`, `arg2`, ..., a built-in SQL function returns a numeric, character-like, or byte-like result. The possible functions are:

- [Numeric functions](abencds_sql_functions_numeric_v1.md)

- [String functions](abencds_sql_functions_character_v1.md)

- [Coalesce function](abencds_coalesce_expression_v1.md)

If an argument contains the [null value](../../abap-glossary/abennull_value_glosry.md), the result is always the null value (except in the [Coalesce function](abencds_coalesce_expression_v1.md)). If an argument contains an invalid value or the value range of a result type is exceeded, an exception is raised.
