---
title: "DDIC - Adjusting Database Tables"
source_file: abenddic_database_tables_adj.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Adjusting Database Tables

When an existing modified DDIC database table is activated, existing content must be adjusted on the database in the following cases:

- When a [client column](../../abap-glossary/abenclient_column_glosry.md) is inserted. During the adjustment, the data of the table is copied to all clients listed in the client table `T000`.

- When fields of existing DDIC database tables are deleted. When key fields are deleted, rows can be lost.

- When fields of existing DDIC database tables are renamed. The field with the old name is deleted and a field with the new name is appended. This leads to the loss of the data in column with the old field name.

- Changing the technical properties of table fields.

## Hints

- The order of table fields in transparent tables in the ABAP Dictionary may be different from the order of the columns of the physical database table on the database. This means that modifying the order of table fields does not necessarily require an adjustment.

- In adjustments, initial fields are filled with their type-dependent initial value, regardless of the [flag for initial values](abenddic_database_tables_init.md).

- For more information, see [Adjustment of Database Structures](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ec1c9c8191b74de98feb94001a95dd76/cf21f1ab446011d189700000e8322d00).
