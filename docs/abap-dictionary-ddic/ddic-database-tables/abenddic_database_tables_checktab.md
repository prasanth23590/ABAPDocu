---
title: "DDIC - Check Table"
source_file: abenddic_database_tables_checktab.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Semantic Properties of Database Tables > DDIC - Table-Specific Semantic Properties of Database Tables > DDIC - Foreign Key Dependencies"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Check Table

Table fields of a DDIC database table whose data type is determined by a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) can be assigned a check table. The [value table](../../abap-glossary/abenvalue_table_glosry.md) of any [DDIC domain](../../abap-glossary/abendomain_glosry.md) of the data element is used as a default value. A table field to which a check table is assigned is called a [foreign key field](../../abap-glossary/abenforeign_key_field_glosry.md) and becomes a part of the [foreign key](abenddic_database_tables_forkey.md) of the table. The table itself becomes a foreign key table. The primary key of the check table is the foreign key of the foreign key table. Each key field of the check table corresponds to a field in the foreign key table. The corresponding field pairs must have the same data type.

## Hints

- Fields whose data type is specified directly (not by using a DDIC data element) cannot be assigned a check table.

- As long as a DDIC database table is a check table, none of its key fields can be deleted and the order of the key fields cannot be modified.

- As long as a DDIC database table is a check table, its primary key can be expanded only by appending new key fields to its end. The existing foreign keys then automatically become generic regarding the new key fields.

- A client field cannot be inserted later into an existing check table.
