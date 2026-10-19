---
title: "set operator"
source_file: abencds_set_operators_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# set operator

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

A set operator merges the result sets of multiple queries into a single result set. In [CDS view entities](abencds_v2_view_glosry.md) and [ABAP SQL](abenabap_sql_glosry.md), the following set operators are available:

- `EXCEPT` returns all distinct rows of the first result set that are not part of the following result sets.

- `INTERSECT` returns all distinct rows that are part of all result sets.

- `UNION` merges the result sets of all queries.

[Set operators in CDS view entities](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_set_operators.md)

[Set operators in ABAP SQL](../abap-programming-language/abap-database-access/abapunion.md)
