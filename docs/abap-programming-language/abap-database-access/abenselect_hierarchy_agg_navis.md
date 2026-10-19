---
title: "SELECT, FROM hierarchy_aggregate_navigator"
source_file: abenselect_hierarchy_agg_navis.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy_navigator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM hierarchy_aggregate_navigator

## Syntax

``` abap
... HIERARCHY_DESCENDANTS_AGGREGATE( ... ) 
  | HIERARCHY_ANCESTORS_AGGREGATE( ... ) ...  
```

[`HIERARCHY_DESCENDANTS_AGGREGATE( ... )`](abenselect_hierarchy_desc_agg.md) · [`HIERARCHY_ANCESTORS_AGGREGATE( ... )`](abenselect_hierarchy_ancs_agg.md)

## Description

Specifies a [hierarchy aggregate navigator](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) as a data source [`data_source`](abapselect_data_source.md) in an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md). A hierarchy aggregate navigator accesses an [SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) and uses [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) to evaluate it. The following hierarchy aggregate navigators are available:

- [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md)

- [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md)
