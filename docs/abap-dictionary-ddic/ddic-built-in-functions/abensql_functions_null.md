---
title: "DDIC - SQL Functions for Null Values"
source_file: abensql_functions_null.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Functions > DDIC - SQL Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - SQL Functions for Null Values

The following table shows the SQL functions for [null values](../../abap-glossary/abennull_value_glosry.md) that can be used by [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) and [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). The columns **CDS DDIC-Based Views**, **CDS View Entities**, and **ABAP SQL** indicate where a function can be used. The **ABAP SQL In-Memory Engine** column indicates whether the function can be executed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md).

| **SQL Function** | **Result**                                              | **CDS DDIC-Based Views**                 | **CDS View Entities**                    | **ABAP SQL**               | **ABAP SQL In-Memory Engine** |
|------------------|---------------------------------------------------------|------------------------------------------|------------------------------------------|----------------------------|-------------------------------|
| `COALESCE`       | Returns the first non-null value from a specified list. | [x](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_coalesce_expression_v1.md) | [x](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_coalesce_expression_v2.md) | [x](../../abap-programming-language/abap-database-access/abensql_coalesce.md) | [x](../../abap-programming-language/abap-database-access/abensql_engine_expr.md) |

The possible operands and data types are described in the corresponding documentation for [ABAP CDS, DDIC-Based Views](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_coalesce_expression_v1.md), [ABAP CDS, View Entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_coalesce_expression_v2.md) and [ABAP SQL](../../abap-programming-language/abap-database-access/abensql_coalesce.md).
