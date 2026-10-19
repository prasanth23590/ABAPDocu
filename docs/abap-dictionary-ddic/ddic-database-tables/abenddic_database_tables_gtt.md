---
title: "DDIC - Global Temporary Tables"
source_file: abenddic_database_tables_gtt.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Global Temporary Tables

Global temporary tables (GTTs) are a special kind of [transparent tables](../../abap-glossary/abentransparent_table_glosry.md) intended for storing temporary data. This data exists only within a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) and can be accessed only by a consumer. GTTs are used to store temporary interim results to split complicated database processes into multiple steps. GTTs are designed for this purpose only and hence incur far lower administration costs than regular transparent tables.

The GTT concept specifies that a GTT is always empty at the start of a database LUW and hence always must be cleared at the end of each database LUW. Most database systems provide native support for this concept by implicitly defining data in a GTT database table as transaction-specific data. This data is deleted automatically at the end of a database LUW, that means, during a [database commit](../../abap-glossary/abendatabase_commit_glosry.md) or [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md).

In ABAP Dictionary, the [table category](abenddic_database_tables_tab_cat.md) *global temporary table* can be specified for a DDIC database table. Tables in this category are created as a GTT in the database. The following additional rules apply in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) access to GTTs to avoid platform-dependent behavior and unexpected responses when handling GTTs:

- If an ABAP Dictionary GTT was filled by a modifying ABAP SQL statement, it must be cleared explicitly before the end of the current [database LUW](../../abap-glossary/abendatabase_luw_glosry.md). The following can be used here:

  - The ABAP SQL statement [`DELETE FROM dbtab`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md) without specifying a `WHERE` condition.

  - All explicit [database commits](../../abap-programming-language/abap-database-access/abendb_commit.md) and [database rollbacks](../../abap-programming-language/abap-database-access/abendb_rollback.md), such as the ABAP SQL statements [`COMMIT WORK`](../../abap-programming-language/abap-database-access/abapcommit.md), [`COMMIT CONNECTION`](../../abap-programming-language/abap-database-access/abapcommit_rollback_connection.md), [`ROLLBACK WORK`](../../abap-programming-language/abap-database-access/abaprollback.md), [`ROLLBACK CONNECTION`](../../abap-programming-language/abap-database-access/abapcommit_rollback_connection.md)

- If an ABAP Dictionary GTT filled using ABAP SQL was not cleared explicitly using one of these methods before an [implicit database commit](../../abap-programming-language/abap-database-access/abendb_commit.md), the runtime error `COMMIT_GTT_ERROR` occurs independently of its content.

Besides these rules, GTTs can be used like regular transparent tables. Regarding their definition in ABAP Dictionary, the following settings are predefined and cannot be modified:

- The [data type](abenddic_database_tables_dat_type.md) and [size category](abenddic_database_tables_siz_cat.md) are irrelevant and undefined.

- [Table buffering](abenddic_database_tables_buffer.md) is not allowed.

- [Logging](abenddic_database_tables_protocol.md) is disabled.

- The [storage type](abenddic_database_tables_storage.md) is row store.

- The [delivery class](abenddic_database_tables_delivery.md) is L.

- No replacement objects can be defined.

The number of [key fields](abenddic_database_tables_key.md) of a GTT is limited to 15.

## Hints

- Only the variant [`DELETE FROM dbtab`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md) without a `WHERE` condition specified prevents the runtime error `COMMIT_GTT_ERROR`. Other variants of the `DELETE` statement do not prevent the runtime error, even if they clear the entire table.

- It is advisable to only use [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) to access ABAP Dictionary GTTs.

- [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md) statements with a [subquery](../../abap-glossary/abensubquery_glosry.md) after [`FROM`](../../abap-programming-language/abap-database-access/abapinsert_source.md) are particularly well suited for filling GTTs, since the operation is then performed only on the database and no data transports are required between the database and the AS ABAP.

- If the data of a GTT is only required for the time span of a database access, [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md) might be an alternative option.

- When accessed using ABAP SQL, explicit clears of ABAP Dictionary GTTs are enforced before implicit database commits for the following reasons:

  - It prevents errors caused by any platform dependencies. It cannot be guaranteed that every database platform deletes the data of a GTT in an implicit database commit. This is guaranteed, however, when the GTT is cleared explicitly.

## Executable Examples

- [Union with Global Temporary Table](../../abap-programming-language/abap-database-access/abenselect_union_sum_gtt_abexa.md)
