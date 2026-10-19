---
title: "DDIC - SQL Functions"
source_file: abensql_functions.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - SQL Functions

The following sections describe the built-in SQL functions that can be used by [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

- [SQL functions for numeric values](abensql_functions_numeric.md)

- [SQL functions for strings](abensql_functions_string.md)

- [SQL functions for null values](abensql_functions_null.md)

- [SQL functions for UUIDs](abensql_functions_uuid.md)

The possible operands and data types are described in the corresponding documentation for [ABAP CDS, DDIC-Based Views](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_sql_functions_v1.md), [ABAP CDS, View Entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_functions_v2.md), and [ABAP SQL](../../abap-programming-language/abap-database-access/abenabap_sql_functions.md).

## Hint

[Certain SQL expressions](../../abap-programming-language/abap-database-access/abensql_engine_expr.md) can be calculated by the [ABAP SQL in-memory engine](../../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md). If any other SQL expressions are used, [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is bypassed and internal tables accessed by [`FROM @itab`](../../abap-programming-language/abap-database-access/abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.
