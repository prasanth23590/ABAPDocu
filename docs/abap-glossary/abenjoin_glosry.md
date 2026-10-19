---
title: "join"
source_file: abenjoin_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# join

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md) [DDIC](../abap-dictionary-ddic/abenddic_glossary.md)

## Definition

A combination of two [SQL data sources](abensql_data_source_glosry.md) into one result set, consisting of columns of both data sources. The rows of the result set are determined by the [join type](abenjoin_type_glosry.md) and by [join conditions](abenjoin_condition_glosry.md) between columns of the data sources. The relation between the rows of the data sources can be expressed by a [cardinality](abencardinality_glosry.md). Joins can be implemented in ABAP as follows:

- [Join expressions](abenjoin_expression_glosry.md) in [queries](abenasql_query_glosry.md) of [ABAP SQL](abenabap_sql_glosry.md)

- [Join expressions](abenjoin_expression_glosry.md) in the [CDS DDL](abencds_ddl_glosry.md) of [ABAP CDS](abenabap_cds_glosry.md)

Furthermore, [CDS associations](abencds_association_glosry.md) and [CTE associations](abencte_association_glosry.md) define join relationships that are instantiated when the associations are used in [SQL path expressions](abensql_path_expression_glosry.md).
