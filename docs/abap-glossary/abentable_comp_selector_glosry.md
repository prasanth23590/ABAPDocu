---
title: "column selector"
source_file: abentable_comp_selector_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# column selector

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md)

## Definition

Character `~`. A column `col` of a [data source](../abap-programming-language/abap-database-access/abapselect_data_source.md) can be addressed in a [query](abenasql_query_glosry.md) of [ABAP SQL](abenabap_sql_glosry.md) using `name~col`, where `name` is the name of the entity in which the column is defined. This type of addressing is necessary if, when multiple database tables are accessed, the name of a column occurs in a number of different database tables, when a comparison of a [SQL condition](abensql_cond_glosry.md) compares two columns.
