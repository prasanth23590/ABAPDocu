---
title: "table function"
source_file: abentable_function_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table function

[General](abenabap_glossary.md)

## Definition

Generally, a table function is a function that returns a tabular result set. Usable in ABAP as follows:

- In [ABAP SQL](abenabap_sql_glosry.md), a table function is a function with a tabular result set that can be used as a [data source](../abap-programming-language/abap-database-access/abapselect_data_source.md) in the [`FROM`](../abap-programming-language/abap-database-access/abapfrom_clause.md) clause of a [query](abenasql_query_glosry.md) and in other operand positions. Currently, ABAP SQL contains only [hierarchy functions](abenhierarchy_function_glosry.md) as table functions.

- In the [SAP HANA database](abenhana_database_glosry.md), a [database function](abendatabase_function_glosry.md) with a tabular return value. In [SQLScript](abensql_script_glosry.md), table functions can be used as operands in the same places as [database tables](abendatabase_glosry.md) or [views](abenview_glosry.md). A table function can be managed as an [AMDP function](abenamdp_function_glosry.md) in an [AMDP class](abenamdp_class_glosry.md).

- In [ABAP CDS](abenabap_cds_glosry.md), [CDS table functions](abencds_table_function_glosry.md) are [CDS persistent entities](abencds_sql_entity_glosry.md) defined using [`DEFINE TABLE FUNCTION`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_table_function.md).

Besides function that return tabular results, there are also [built-in functions](../abap-programming-language/abap-processing-internal-data/abenitab_functions.md) that work with [internal tables](abeninternal_table_glosry.md) as arguments. Those might also be called table functions.
