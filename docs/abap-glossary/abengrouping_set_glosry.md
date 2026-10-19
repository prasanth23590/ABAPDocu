---
title: "grouping set"
source_file: abengrouping_set_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# grouping set

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

Grouping sets are used in the [`GROUP BY`](../abap-programming-language/abap-database-access/abapgroupby_clause.md) clause of a [query](abenasql_query_glosry.md). A grouping set is specified either as an empty grouping set or as a comma-separated list. Columns and SQL expressions can also be used in the list. The `GROUP BY` addition `GROUPING SETS` makes it possible to define multiple grouping sets under a `GROUP BY` clause. The grouping sets are aggregated separately and merged into one result set.

[***-\>* More about**](../abap-programming-language/abap-database-access/abapgrouping_sets_clause.md)
