---
title: "correlated subquery"
source_file: abencorrelated_subquery_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# correlated subquery

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md)

## Definition

[Subquery](abensubquery_glosry.md) that uses columns of the surrounding [query](abenasql_query_glosry.md) in its [SQL conditions](abensql_cond_glosry.md). It must be possible to assign the column to a [SQL data source](abensql_data_source_glosry.md) in the surrounding query. A correlated subquery is evaluated for each individual row of the result set of the surrounding query.
