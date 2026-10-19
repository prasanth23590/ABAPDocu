---
title: "DDIC - Key Fields of Database Tables"
source_file: abenddic_database_tables_key.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Semantic Properties of Database Tables > DDIC - Table-Specific Semantic Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Key Fields of Database Tables

At least one table field must be flagged as a [key field](../../abap-glossary/abenkey_field_glosry.md) in the structure of a DDIC database table. The table fields flagged as key fields become the [primary key](../../abap-glossary/abenprimary_key_glosry.md) of the table. The key fields of a table must be located together at the beginning of the table, which means that no non-key fields are allowed between two key fields. The primary key formed by the key fields is a unique identification for a table row. If other combinations of table rows identify a table row uniquely, they are called key candidates. The [primary index](../../abap-glossary/abenprimary_index_glosry.md) is created for the primary key of the table. This index provides optimized key access to the table rows when values are specified for the key fields.

There can be a maximum of 16 key fields in each table. The total number of bytes in all key fields on the database cannot exceed 900. If the number is greater than 120, however, the following restrictions apply:

- Table content cannot be transported by specifying the complete key values. Instead, the generic key values must be specified with a maximum total of 120 bytes or characters.

The following [built-in data types](../ddic-built-in-data-types/abenddic_builtin_types.md) are not allowed for key fields: `DF16_SCL` and `DF34_SCL` (both obsolete) plus `FLTP`, `STRING`, `RAWSTRING`, `LCHR`, `LRAW`, and `GEOM_EWKB`. A key field with the type `RAW` must not be longer than 69 bytes.

## Hints

- The [flag for initial values](abenddic_database_tables_init.md) is always set automatically for key fields.

- No [null values](../../abap-glossary/abennull_value_glosry.md) can be inserted in key fields. Any attempts to do this raise an exception on the database.
