---
title: "database LUW"
source_file: abendatabase_luw_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# database LUW

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

Also referred to as database transaction. Indivisible sequence of database operations concluded by a [database commit](abendatabase_commit_glosry.md). The database LUW is either executed completely or not at all by the [database system](abendatabase_system_glosry.md). If an error is detected within a database LUW, all database changes made since the start of the database LUW can be canceled using a [database rollback](abendatabase_rollback_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-database-access/abendb_transaction.md)
