---
title: "DDIC - SQL Functions for UUIDs"
source_file: abensql_functions_uuid.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Functions > DDIC - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - SQL Functions for UUIDs

The following table shows the SQL functions for [UUIDs](../../abap-glossary/abenuuid_glosry.md) that can be used by [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). The columns **CDS DDIC-Based Views**, **CDS View Entities**, and **ABAP SQL** indicate where a function can be used. The **ABAP SQL In-Memory Engine** column indicates whether the function can be processed by the [ABAP SQL in-memory engine](../../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table with [`FROM @itab`](../../abap-programming-language/abap-database-access/abapselect_itab.md).

| **SQL Function** | **Result**                                   | **CDS DDIC-Based Views** | **CDS View Entities** | **ABAP SQL**           | **ABAP SQL In-Memory Engine** |
|------------------|----------------------------------------------|--------------------------|-----------------------|------------------------|-------------------------------|
| `UUID( )`        | Creates [UUID](../../abap-glossary/abenuuid_glosry.md) values. | \-                       | \-                    | [x](../../abap-programming-language/abap-database-access/abensql_uuid.md) | \-                            |

The function is described in the relevant [ABAP SQL](../../abap-programming-language/abap-database-access/abensql_uuid.md) documentation.
