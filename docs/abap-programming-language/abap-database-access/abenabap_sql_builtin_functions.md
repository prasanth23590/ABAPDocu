---
title: "ABAP SQL - Built-In Functions sql_func"
source_file: abenabap_sql_builtin_functions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Built-In Functions sql_func

The following [built-in database functions](../../abap-dictionary-ddic/ddic-built-in-functions/abenddic_builtin_functions.md) managed by the ABAP Dictionary can be specified in ABAP SQL as [SQL expressions](abapsql_expr.md) in all places where these are possible:

- [SQL functions](abenabap_sql_functions.md)

- [Special functions](abenabap_sql_special_functions.md)

## Hint

[Certain SQL expressions](abensql_engine_expr.md) can be calculated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). If any other SQL expressions are used, [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is bypassed and internal tables accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.
