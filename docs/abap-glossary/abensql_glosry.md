---
title: "SQL"
source_file: abensql_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SQL

[General](abenabap_glossary.md)

## Definition

Short for Structured Query Language. A widely standardized language for accessing [relational databases](abenrelational_database_glosry.md). Divided into [DQL](abendql_glosry.md), [DML](abendml_glosry.md), [DDL](abenddl_glosry.md), and [DCL](abendcl_glosry.md) (sometimes the term DML includes DQL). Each [database system](abendatabase_system_glosry.md) has its own platform-specific variant of SQL. The SQL variant of the [standard database](abenstandard_db_glosry.md) of an [AS ABAP](abenas_abap_glosry.md), the [SAP HANA database](abenhana_database_glosry.md), is HANA SQL. AS ABAP offers different ways for accessing its standard database with SQL:

- The DQL and DML parts are implemented predominantly by [ABAP SQL](abenabap_sql_glosry.md).

- The DDL part is implemented by the [ABAP Dictionary](abenabap_dictionary_glosry.md) and the [CDS DDL](abencds_ddl_glosry.md) of [ABAP CDS](abenabap_cds_glosry.md).

- The DCL part is implemented by the [CDS DCL](abencds_dcl_glosry.md) of ABAP CDS.

Furthermore, the entire scope of the SQL statements of the standard database is available in [AMDP methods](abenamdp_method_glosry.md).

All accesses of an AS ABAP to the standard database are done using its [database interface](abendatabase_interface_glosry.md), where ABAP-specific SQL is translated to the platform-specific SQL variant.
