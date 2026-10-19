---
title: "graph workspace"
source_file: abengraph_workspace_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# graph workspace

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

A graph workspace is an object of the [SAP HANA database](abenhana_database_glosry.md) that defines a [graph](abengraph_glosry.md) in terms of tables and columns, i. e. it consists of two tables (for [vertices](abenvertex_glosry.md) and [edges](abenedge_glosry.md)) as sources for a graph model. It declares the key column of a [vertex table](abenvertex_table_glosry.md) and an [edge table](abenedge_table_glosry.md), and also the source and target column of an edge table. It is currently restricted to one key column and one source and target column. Graph workspaces are supported in ABAP by [AMDP](abenamdp_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-database-access/abenamdp_hdb_graph.md)
