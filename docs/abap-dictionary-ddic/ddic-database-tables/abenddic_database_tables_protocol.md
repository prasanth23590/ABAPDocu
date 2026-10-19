---
title: "DDIC - Logging Database Tables"
source_file: abenddic_database_tables_protocol.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables > DDIC - Table-Specific Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Logging Database Tables

If logging is activated, any changes to table entries done in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) are logged in the log table `DBTABLOG`.

If a table row has more than 16000 bytes, logging is not possible for the table. The lengths of fields with the built-in types `STRING`, `RAWSTRING`, `LCHR`, `LRAW`, and `GEOM_EWKB` are counted completely here.

## Hints

- If logging is activated, access to the DDIC database table slows down accordingly. If logging is activated for many DDIC database tables, lock situations can occur for the log table.

- No data can be written to a DDIC database table with enabled logging using the statement [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md) with [subquery](../../abap-programming-language/abap-database-access/abapinsert_source.md).
