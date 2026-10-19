---
title: "DDIC - Flag for Initial Values in Database Tables"
source_file: abenddic_database_tables_init.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Semantic Properties of Database Tables > DDIC - Table-Specific Semantic Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Flag for Initial Values in Database Tables

Table fields of DDIC database tables can be flagged for initial values. If the field is flagged for an initial value, it is created with the initial value and the flag is set to `NOT NULL` in the database. If the field is not flagged for an initial value, the field can be `NOT NULL` or `NULL`. It depends on the data type if the field can have a null value or not. If an initial value exists for a data type, the value will be `NOT NULL`; otherwise it can be `NULL`. The flag is always set automatically for [key fields](abenddic_database_tables_key.md).

If a new table field without the property `NOT NULL` is inserted into an existing table, the field is given a [null value](../../abap-glossary/abennull_value_glosry.md) in all rows. There is no equivalent to the null value in ABAP. The null value can be queried in ABAP SQL using the `WHERE` condition with the addition [`IS [NOT] NULL`](../../abap-programming-language/abap-database-access/abenwhere_logexp_null.md).

Generally, table fields on most database platforms are created as `NOT NULL`, even if the flag for the initial value is not set in the ABAP Dictionary. Furthermore, in the following scenarios, all fields are given the property `NOT NULL`:

- When a new table is created.

- When a table is [adjusted](abenddic_database_tables_adj.md).

Only if new fields can be appended or inserted using `ALTER TABLE` without an [adjustment](abenddic_database_tables_adj.md), they are created without the flag `NOT NULL` on some database platforms, given they are not flagged for initial values in ABAP Dictionary. This does not apply to key fields, which are always flagged as `NOT NULL`. Whether a field is defined as `NOT NULL` on the database can be seen by displaying the database object in the ABAP Dictionary tool.

If the flag is set for an entire include structure, it is applied only to those structure components that were originally flagged. The other structure components are skipped. If the flag is not set for an include structure, all structure components do not have the flag, regardless of the original definition.

## Hints

- The flag cannot be set for the following data types:

  - `LCHR`, `LRAW`, and the obsolete `VARC`. No [initial value](../ddic-built-in-data-types/abenddic_builtin_types.md) is assigned to these data types.

  - `NUMC` and `RAW` with a length greater than or equal to 70.

  - `GEOM_EWKB`

    It is possible to set the flag for the data type `RAW` with a length less than 70 even though this data type does not have any [initial value](../ddic-built-in-data-types/abenddic_builtin_types.md).

- Except when inserting new fields, the indicator is not needed and the initial value is always set, which is especially true for [adjusting tables](abenddic_database_tables_adj.md).

- In tables with many rows, it can take a long time to set the type-dependent initial value and the initial value flag should only be used if absolutely necessary or if the table has a small number of entries.
