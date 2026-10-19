---
title: "SELECT, FROM hierarchy_data"
source_file: abenselect_hierarchy_data.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM hierarchy_data

## Syntax

``` abap
... hierarchy 
  | hierarchy_navigator ...  
```

[`hierarchy`](abenselect_hierarchy.md) · [`hierarchy_navigator`](abenselect_hierarchy_navigators.md)

## Description

Specifies hierarchy data as a data source [`data_source`](abapselect_data_source.md) in an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md). Possible hierarchy data is:

- An [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md)

- A [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) [`hierarchy_navigator`](abenselect_hierarchy_navigators.md) that accesses an SQL hierarchy.

Access to hierarchy data is not supported by all databases.

## Hints

- Hierarchy data as data sources are handled like any other data source. They can have alias names defined using [`AS`](abapfrom_clause.md) and can be used in join expressions. There are no restrictions on which [queries](../../abap-glossary/abenasql_query_glosry.md) they can be used in.

- Hierarchy data cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). An ABAP SQL statement that accesses hierarchy data bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Access to the [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) [`HIERARCHY_SIBLINGS`](abenselect_hierarchy_navigators.md) as the data source of a query. The hierarchy navigator uses a CDS hierarchy as a source.

``` abap
FINAL(id) = 5. 
 
SELECT FROM HIERARCHY_SIBLINGS( 
              SOURCE demo_cds_simple_tree( p_id = 1 ) 
              START WHERE id = @id ) 
       FIELDS id, 
              parent_id, 
              hierarchy_rank, 
              hierarchy_level, 
              hierarchy_tree_size, 
              hierarchy_sibling_distance 
       INTO TABLE @FINAL(ancestors).
```
