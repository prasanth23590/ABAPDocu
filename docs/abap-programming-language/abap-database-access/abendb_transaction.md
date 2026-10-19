---
title: "Database LUW"
source_file: abendb_transaction.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Database LUW

A database [LUW](../../abap-glossary/abenluw_glosry.md) (also referred to as a database transaction) is a non-separable sequence of database operations that is completed with a [database commit](../../abap-glossary/abendatabase_commit_glosry.md). The database LUW is either executed completely by the database system or not at all. After a database LUW has been completed successfully, the database returns to a consistent state and a new database LUW is opened. If an error is detected within a database LUW, all database changes made since the start of the database LUW can be undone using a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). The database is subsequently restored to the same status as before the start of the database LUW. Isolation levels determine whether other users can perform reads on data modified in a database LUW before a database commit is performed.

- [Database commit](abendb_commit.md)

- [Database rollback](abendb_rollback.md)

- [Isolation levels](abendb_isolation.md)

## Hints

- At the end of a database LUW, all [reader streams](../../abap-glossary/abenreader_stream_glosry.md) and [locators](../../abap-glossary/abenlocator_glosry.md) created in it are closed implicitly. A writer stream that is still open is only closed as part of a database rollback and causes a runtime error during a a database commit.
