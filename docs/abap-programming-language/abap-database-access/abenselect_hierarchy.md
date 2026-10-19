---
title: "SELECT, FROM hierarchy"
source_file: abenselect_hierarchy.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM hierarchy

## Syntax

``` abap
... cds_hierarchy 
  | HIERARCHY( ... ) 
  | cte_hierarchy  
```

[`cds_hierarchy`](abenselect_cds_hierarchy.md) · [`HIERARCHY( ... )`](abenselect_hierarchy_generator.md) · [`cte_hierarchy`](abenselect_cte_hierarchy.md)

## Description

Specifies an [ABAP SQL hierarchy](abensql_hierarchies.md) as a data source in an ABAP SQL query.

- The following can be specified:

  - A [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) [`cds_hierarchy`](abenselect_cds_hierarchy.md)

  - The [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md)

  - A [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md) [`cte_hierarchy`](abenselect_cte_hierarchy.md)

- An ABAP SQL hierarchy can be specified in the following places:

  - As a data source [`data_source`](abapselect_data_source.md) in an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md).

  - As the source of a [hierarchy navigator](abenselect_hierarchy_navigators.md)

  - As the source of the hierarchy generator [`HIERARCHY`](abenselect_hierarchy_generator.md)

When an ABAP SQL hierarchy is used as a data source in an ABAP SQL query, its additional [hierarchy columns](abenddddl_hierarchy.md) can be accessed as follows:

- In the [`SELECT`](abapselect_list.md) list

  - Hierarchy columns can be specified as regular columns using [`colname`](abenabap_sql_columns.md) and then become part of the result set of the query.

  - If `*` or `...~*` is specified, hierarchy columns are not part of the result set of the query. Only the components of the source of the SQL hierarchy are respected. In this case, the hierarchy columns are also ignored by any structure or internal table created in the [`INTO` clause](abapinto_clause.md) by an inline declaration `@DATA|@FINAL(...)`.

- In other clauses, hierarchy columns can be specified regardless of the `SELECT` list and are evaluated accordingly.

## Hints

- It is possible to evaluate the [hierarchy columns](abenddddl_hierarchy.md) in a query, but this is not mandatory. In most cases, only the data content of an SQL hierarchy is of interest and not the technical properties of the hierarchy nodes.

- On [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md), the result sets of CDS hierarchies and the hierarchy generator `HIERARCHY` are created using the SAP HANA hierarchy generator function `HIERARCHY` and similar. For more information, see [SAP HANA documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).
