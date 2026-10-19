---
title: "ABAP SQL - Write Access with DML"
source_file: abenabap_sql_writing.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Write Access with DML

Write accesses include inserting, modifying, and deleting content in [writable database objects](../../abap-glossary/abenwritable_db_obj_glosry.md), such as [CDS table entities](../../abap-glossary/abencds_table_entity_glosry.md), [writable CDS view entities](../../abap-glossary/abenwritable_v2_glosry.md), or [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md). All write accesses can be made as individual accesses or as bulk access. If multiple rows of a [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) are to be changed, bulk access using internal tables generally gives better performance than individual accesses.

The following ABAP SQL statements implement the [DML](../../abap-glossary/abendml_glosry.md) part of [SQL](../../abap-glossary/abensql_glosry.md) in the ABAP language:

- [`INSERT`](abapinsert_dbtab.md)

- [`UPDATE`](abapupdate.md)

- [`MODIFY`](abapmodify_dbtab.md)

- [`DELETE`](abapdelete_dbtab.md)

## Hints

- In the case of writes, [data consistency](abendata_consistency.md) must always be ensured. The [LUW](../../abap-glossary/abenluw_glosry.md) concept is designed for this purpose. In application programs of an AS ABAP, the implicit [database LUWs](../../abap-glossary/abendatabase_luw_glosry.md) are normally not sufficient for consistent data storage. Instead, explicit [SAP LUWs](../../abap-glossary/abensap_luw_glosry.md) must be programmed, which normally contain multiple database LUWs.

- Once a [global temporary table](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md) is filled using ABAP SQL, this table must be emptied again explicitly before the next implicit [database commit](../../abap-glossary/abendatabase_commit_glosry.md) using the ABAP SQL statement [`DELETE FROM`](abapdelete_dbtab.md) without `WHERE` or using an explicit [database commit](abendb_commit.md) or [database rollback](abendb_rollback.md), otherwise the runtime error `COMMIT_GTT_ERROR` is produced.

- When making writes to a DDIC database table for which a database cursor is opened in a [`SELECT` loop](abapselect.md), the result set is database-dependent and undefined. This kind of parallel access should therefore be avoided.
