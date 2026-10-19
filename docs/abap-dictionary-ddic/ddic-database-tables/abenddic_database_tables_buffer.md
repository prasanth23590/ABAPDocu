---
title: "DDIC - Table Buffering of Database Tables"
source_file: abenddic_database_tables_buffer.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables > DDIC - Table-Specific Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Table Buffering of Database Tables

It is possible to define whether and how [table buffering](../../abap-glossary/abentable_buffering_glosry.md) of a DDIC database table is allowed in the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) of an AS instance.

- [Buffering Permission](abenddic_database_tables_buffer.md#buffering-permission)

- [Buffering Type](abenddic_database_tables_buffer.md#buffering-type)

The table buffer is managed by the [database interface](../../abap-glossary/abendatabase_interface_glosry.md). When tables with active buffering are accessed using [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the table buffer is used implicitly.

## Buffering Permission

Table buffering can be configured for a DDIC database table as follows:

- **Buffering not allowed**

  The table is not buffered. The database interface always passes the accesses to the DDIC database table and the current data is used directly. This setting also specifies that table buffering should not be activated for this table in any other systems due to the way the table is used.

- **Buffering allowed, but switched off**

  The table is not buffered when delivered. This setting indicates, however, that buffering is possible in principle and can be activated in other systems depending on how the table is used.

- **Buffering switched on**

  The table is buffered. The database interface redirects any reads to the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) of the current AS instance, if possible.

### Hint

Certain [prerequisites](../../abap-programming-language/abap-database-access/abenbuffer_restrictions.md), some of which depend on the buffering type, must be met before ABAP SQL can access the table buffer instead of accessing the DDIC database table directly.

## Buffering Type

The buffering type determines which data is loaded from the table to the table buffer when a table entry is accessed and buffering is switched on. The possible buffering types are:

- [Single record buffering](../../abap-programming-language/abap-database-access/abenbuffer_single_buffering.md)

- [Generic buffering](../../abap-programming-language/abap-database-access/abenbuffer_generic_buffering.md)

- [Full buffering](../../abap-programming-language/abap-database-access/abenbuffer_complete_buffering.md)
