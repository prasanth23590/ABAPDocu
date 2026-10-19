---
title: "ABAP SQL - Performance Notes"
source_file: abenabap_sql_perfo.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Performance Notes

The performance of a program is often determined by the efficiency of the database reads it contains. In a client/server environment, each database read places a load on both the database system and the connection between the database system and the AS ABAP. This load must be kept as low as possible if programs are to demonstrate a good level of performance.

Generally speaking, the following rules must be followed. The overall performance of a program can depend on the data being processed, any evaluations required, and the database system itself, which means that the application and prioritization of rules can vary from case to case.

- **Keep the number of hits low**

  The set of rows selected should be kept as small as possible by using specific conditions to restrict the set to those rows actually needed. Superfluous rows should never be transported from the database system to the AS ABAP and then evaluated there.

- **Keep the data volume low**

  The volume of data transported should always be restricted to the columns required. The columns can be specified explicitly, or an appropriate view can be used. Furthermore, [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) can be combined with corresponding groupings [SQL expressions](../../abap-glossary/abensql_expression_glosry.md) to reduce the volume of data transferred, since here the data is already aggregated before the transport in the database system.

- **Keep the number of reads low**

  To keep the number of database reads low, mass operations should always be used instead of single operations. More specifically, ABAP SQL statements should not be used within loops. Instead, joins, views, or subqueries can be used when reading multiple DDIC database tables.

- **Use local buffers**

  The same data should be not be read more than once. Storing database tables in the local buffer in [table buffering](../../abap-glossary/abentable_buffering_glosry.md) can produce significant time savings, since it takes much longer for the AS ABAP to read the database system than a locally buffered table. DDIC database tables should always be buffered if they are read frequently and modified rarely. If the same data is to be sorted multiple times in different orders, the data should be sorted in the ABAP program.

- **Efficient search using indexes**

  In all cases where [secondary indexes](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_index.md) of DDIC database tables improve selection performance, these indexes should be created and used.
