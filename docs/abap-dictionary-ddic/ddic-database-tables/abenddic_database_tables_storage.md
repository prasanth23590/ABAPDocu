---
title: "DDIC - Storage Type of Database Tables"
source_file: abenddic_database_tables_storage.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables > DDIC - Table-Specific Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Storage Type of Database Tables

The storage type has an effect only if the current database is an [SAP HANA](../../abap-glossary/abenhana_database_glosry.md) database. The specified storage type is ignored by other database systems and the platform-dependent storage type is used instead. The following settings can be defined for the SAP HANA database:

- **Column store**

  This setting should be used in the following cases:

  - The DDIC database table is designed for application data analyzed in [SAP HANA](../../abap-glossary/abensap_hana_glosry.md).

  - The DDIC database table contains a very large number of rows since the storage type Column Store provides better compression.

  - The DDIC database table contains table fields with HANA data types that are supported only by the storage type column store.

- **Row store**

  This setting should only be used in SAP HANA databases if the database table is used mainly for frequent single row accesses. For [global temporary tables (GTTs)](abenddic_database_tables_gtt.md), it is the only possible setting.

## Hint

For more information about the differences between row store and column store on the SAP HANA database, see the SAP HANA documentation.
