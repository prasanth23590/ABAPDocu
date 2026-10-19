---
title: "SELECT, FROM HIERARCHY"
source_file: abenselect_hierarchy_generator.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM HIERARCHY

## Syntax Forms

**Parent-child-based Hierarchy Generator**

``` abap
1. ... HIERARCHY( SOURCE hierarchy_source ... 
                 CHILD TO PARENT ASSOCIATION _hierarchy_assoc 
                 ... )
```

**Level-based Hierarchy Generator**

``` abap
2. ... HIERARCHY( SOURCE data_source ... 
                 LEVELS ( col1, col2,... ) 
                 ... )
```

[`HIERARCHY( SOURCE hierarchy_source ...`](abenselect_hierarchy_gen_assoc.md) · [`CHILD TO PARENT ASSOCIATION _hierarchy_assoc`](abenselect_hierarchy_gen_assoc.md) · [`...`](abenselect_hierarchy_gen_assoc.md) · [`HIERARCHY( SOURCE data_source ...`](abenselect_hierarchy_gen_level.md) · [`LEVELS ( col1, col2,... )`](abenselect_hierarchy_gen_level.md) · [`...`](abenselect_hierarchy_gen_level.md)

## Description

Specifies the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) `HIERARCHY` as an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md) in an ABAP SQL query. The hierarchy generator creates the SQL hierarchy. There are two ways for generating a SQL hierarchy using the hierarchy generator that are distinguished by the following additions:

- [`CHILD TO PARENT ASSOCIATION ...`](abenselect_hierarchy_gen_assoc.md)

  The hierarchy generator creates a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) that is defined by [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) between different columns of a so called hierarchy source that must expose a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md).

- [`LEVELS ( ... )`](abenselect_hierarchy_gen_level.md)

  The hierarchy generator creates a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md), where a set of columns of the data source defines the levels of the hierarchy.

In both cases, the rows of the tabular result set of the hierarchy generator are the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of the generated SQL hierarchy and their columns are composed of the elements of the source specified after `SOURCE` and additional [hierarchy columns](abenddddl_hierarchy.md). The hierarchy columns must be specified explicitly in the [`SELECT`](abapselect_list.md) list before they can be selected.

## Hint

Hierarchy functions cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.
