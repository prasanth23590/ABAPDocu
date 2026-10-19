---
title: "DDIC - Foreign Keys"
source_file: abenddic_database_tables_forkey.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Semantic Properties of Database Tables > DDIC - Table-Specific Semantic Properties of Database Tables > DDIC - Foreign Key Dependencies"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Foreign Keys

A foreign key consists of one or more [foreign key fields](../../abap-glossary/abenforeign_key_field_glosry.md) of a [foreign key table](../../abap-glossary/abenforeign_key_table_glosry.md). The foreign key fields form the [primary key](../../abap-glossary/abenprimary_key_glosry.md) of a [check table](../../abap-glossary/abencheck_table_glosry.md). A DDIC database table can have multiple foreign keys. A [foreign key dependency](../../abap-glossary/abenforeign_key_dependency_glosry.md) exists between a foreign key table and its check tables. A foreign key table usually only contains entries where the content of the foreign key also occurs exactly once as content of the primary key in the check table. The developer must consider this in [writes](../../abap-programming-language/abap-database-access/abenabap_sql_writing.md) made using ABAP SQL, since there is no automatic check.

Foreign keys can have the following properties:

- **Input check**

  In the definition of the foreign key, input checks by means of foreign key dependencies can be switched on or off. Furthermore, the standard message can be replaced by a custom [message](../../abap-glossary/abenmessage_glosry.md). Any placeholders in the message are filled as follows when the message is sent: The first three placeholders are filled with the content of the foreign key fields that are assigned to the first three key fields of the check table after the client field. The fourth placeholder is filled with the name of the check table.

- **Generic foreign key fields**

  Foreign key fields can be flagged as *generic* in the definition of a foreign key. Generic foreign key fields are not checked against their check table in input checks.

- **Constant values**

  Foreign key fields can be given constant values in the definition of a foreign key. In input checks, the field of the check table assigned to a foreign key field with a constant value must have this constant value in the row determined by the remaining foreign key fields.

- **Inheritance**

  The fields of included include structures can be foreign key fields and are part of the foreign key of the DDIC database table. An inheritance relationship with the included structure exists by default and any changes to the definition of the foreign key in the included structure affect the foreign key of the including DDIC database table. This inheritance relationship can be removed. When removed, any changes to the definition of the foreign key in the included structure are not applied to the DDIC database table.

- **Cardinality**

  A [cardinality](../../abap-glossary/abencardinality_glosry.md) `n:m` can be defined for each foreign key. This cardinality mainly serves a documentation purpose. Possible values for `n`:

  - `1`

    Precisely one row of the check table must exist for each record of the foreign key table.

  - `C`

    No rows must exist in the check table for a record of the foreign key table. Possible values for `m`:

  - `1`

    Precisely one row in the foreign key table must exist for each row of the check table.

  - `C`

    There can be no more than one assigned row in the foreign key table for each row of the check table.

  - `N`

    There must be at least one row in the foreign key table for each row of the check table.

  - `CN`

    There can be any number of rows in the foreign key table for each row of the check table. Defining a generic foreign key turns the cardinalities `1:m` or `C:m` into `CN:m`. There can be multiple rows in the check table for each dependent row. This cardinality cannot, however, be specified explicitly.

- **Type of the foreign key fields**

  The type of the foreign key fields can be defined to describe the meaning of the foreign key fields in the foreign key table. The possible values are as follows, whereby the first two are only for documentation purposes:

  - `No key fields/key candidates`

    The foreign key fields are neither primary key fields of the foreign key table nor do they identify a record of the foreign key table uniquely.

  - `Key fields/key candidates`

    The foreign key fields are either primary key fields of the foreign key table or they identify a record of the foreign key table uniquely as a key candidate.

  - `Key fields of a text table`

    If this type of foreign key field is defined, the foreign key table is handled as a text table of the check table. The primary key of the foreign key table must match the check table and it must have one additional language key field with the type `LANG`. There can be only one text table for each check table, otherwise an activation warning occurs.
