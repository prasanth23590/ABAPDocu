---
title: "DDIC - Load Unit of Database Tables"
source_file: abenddic_database_tables_load_unit.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Technical Properties of Database Tables > DDIC - Table-Specific Technical Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Load Unit of Database Tables

The load unit of a table specifies how the data of the table is loaded into the main memory of the SAP HANA database. The SAP HANA database offers the following settings:

- **Column Loadable**

  The complete table is considered as in-memory. The table data is loaded upon system start in a column-oriented format into the main memory of the SAP HANA database. This is the default behavior.

- **Page Loadable**

  By using a feature of the SAP HANA database called Native Storage Extension (NSE), table data is stored on disk in pages rather than in columns. These pages are loaded only on request into a special buffer in the HANA main memory. Unused data in the buffer can be paged out.

Typically, `Page Loadable` is used for large tables with less frequent accesses. While the SAP HANA database offers the load unit attribute also for single columns and partitions of a table, in the ABAP Dictionary this setting always affects the complete table and its indexes.

The ABAP Dictionary provides this setting in two flavors:

- **Column Preferred** or **Page Preferred**

  - `Column Preferred` is the default behavior.

  - The load unit is only specified upon creation of the table.

  - Changing from one preferred load unit to another does not change the load unit on the database.

  - The ABAP DDIC consistency check does not consider the load unit. It is accepted if the load unit on the database differs from the values specified in the DDIC.

- **Column Enforced** or **Page Enforced**

  - The load unit is specified upon creation of the table. Furthermore, changes to the load unit in the ABAP DDIC result in corresponding changes on the database.

  - Changing the enforced load unit results in a corresponding change on the database.

  - The ABAP Dictionary consistency check respects the load unit. Different values for the load unit in the ABAP Dictionary and on the database result in tables that are inconsistent from the DDIC point of view.

The `Column Preferred` and `Page Preferred` settings for the load unit setting in the ABAP Dictionary offer the possibility for a database administrator or a tool like the SAP HANA NSE Advisor to overwrite the DDIC settings without making the table inconsistent. In general, most of the tables should use one of the `Preferred` settings for the load unit. Only if you are sure that the table should keep a specific load unit in all relevant scenarios (on premise, cloud, ...), you should use the `Enforced` load unit settings.

The load unit setting is completely transparent to applications.

**Limitations:**

- `Page Loadable` cannot be used for database tables with [storage type](abenddic_database_tables_storage.md) `Row store`.

- `Page Loadable` cannot be used for [global temporary tables (GTTs)](abenddic_database_tables_gtt.md).

- `Page Loadable` cannot be set for tables that have [data aging](../../abap-glossary/abendata_aging_glosry.md) enabled.

## Hint

For more information about the Native Storage Extension on the SAP HANA database, see the [SAP HANA documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/4efaa94f8057425c8c7021da6fc2ddf5).
