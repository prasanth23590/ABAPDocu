---
title: "sql_func - SQL Functions"
source_file: abenabap_sql_functions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - SQL Functions

The following built-in [SQL functions](../../abap-dictionary-ddic/ddic-built-in-functions/abensql_functions.md) can either be specified as standalone functions in ABAP SQL or as operands of [SQL expressions](abapsql_expr.md), in all places where SQL expressions are possible.

- [Numeric functions](abensql_arith_func.md)

- [String functions](abensql_string_func.md)

- [Coalesce function](abensql_coalesce.md)

- [UUID function](abensql_uuid.md)

- [Spatial functions](abensql_spatial_func.md)

- [Hierarchy composite ID function](abensql_hierarchy_comp_id.md)

## Hint

[Certain SQL expressions](abensql_engine_expr.md) can be calculated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). If any other SQL expressions are used, [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is bypassed and internal tables accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.
