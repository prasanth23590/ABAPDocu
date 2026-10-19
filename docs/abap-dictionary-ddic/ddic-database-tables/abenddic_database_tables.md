---
title: "DDIC - Database Tables"
source_file: abenddic_database_tables.html
section: "ABAP Dictionary (DDIC)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Database Tables

The term [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) (or database table or table for short) describes a physical database table in the current [standard database](../../abap-glossary/abenstandard_db_glosry.md) in the ABAP Dictionary:

- A DDIC database table is a two-dimensional matrix that consists of rows and columns.

- A field or combination of fields that uniquely identifies every row in a table is known as a [table key](../../abap-glossary/abentable_key_glosry.md). This is a minimal property, that is, if one of the fields is removed from the key, the remaining fields cannot uniquely identify the table rows.

- A [primary key](../../abap-glossary/abenprimary_key_glosry.md) must exist for every table.

- In the [relational model](../../abap-glossary/abenrelational_data_model_glosry.md), the relationship between objects is expressed by a [foreign key](../../abap-glossary/abenforeign_key_glosry.md).

In [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), only database tables can be accessed that are defined in ABAP Dictionary.

The name of a DDIC database table must follow the [naming rules for DDIC database tables](abenddic_dbtab_names.md).

The definition of a DDIC database table consists of the following:

- A non-nested [DDIC structure](../ddic-data-types/abenddic_structures.md) with its [technical](abenddic_database_tables_techstruc.md) and [semantic](abenddic_database_tables_semastruc.md) properties.

- Additional [technical properties](abenddic_database_tables_techspec.md) of the DDIC database table.

- Additional [semantic properties](abenddic_database_tables_sema.md) of the DDIC database table.

The most common [table category](abenddic_database_tables_tab_cat.md) of a DDIC database table is the [transparent table](../../abap-glossary/abentransparent_table_glosry.md). When the table is activated, the platform-dependent SQL DDL statement `CREATE TABLE` is used to generate a physical database table with all [indexes](abenddic_database_tables_index.md) from its definition in the ABAP Dictionary for those indexes for which this is not excluded explicitly in the definition. This is done in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) in the [standard AS ABAP database](../../abap-glossary/abenstandard_db_glosry.md). The [built-in DDIC types](../ddic-built-in-data-types/abenddic_builtin_types.md) used to define the components of the structure are implemented as database-dependent types. Besides transparent tables, there are also [global temporary tables (GTTs)](../../abap-glossary/abenglobal_temporary_table_glosry.md) for storing temporary data within a work step.

The order of the fields in the ABAP Dictionary and on the database does not need to match. Therefore, the order of the table fields, except for key fields, of existing DDIC database tables can be modified without affecting the corresponding database object. When accessing a DDIC database table using [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), the database interface considers potential differences and respects the order defined in ABAP Dictionary. If [AMDP](../../abap-programming-language/abap-database-access/abenamdp.md) is used, the results are sorted in the same order as in the ABAP Dictionary (if possible).

- [Technical properties of database tables](abenddic_database_tables_tech.md)

- [Semantic properties of database tables](abenddic_database_tables_sema.md)

- [Global temporary tables](abenddic_database_tables_gtt.md)

DDIC database tables can be defined with source-code-based editors using [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). The following section describes the syntax of the source-code-based definition:

- [Dictionary DDL for Defining Database Tables](abenddic_define_table.md)

If existing DDIC database tables are modified, adjustments may be necessary.

- [Adjusting database tables](abenddic_database_tables_adj.md)

## Hints

- DDIC database tables can be released for developer extensibility under the [C0 release contract](../../abap-glossary/abenc0_contract_glosry.md).

- If existing ABAP Dictionary objects in the definition of DDIC database tables are changed, it may be necessary to [adjust](abenddic_database_tables_adj.md) these tables on the database. This can be very time-consuming for tables with a large number of rows. Furthermore, [foreign keys](../../abap-glossary/abenforeign_key_glosry.md) in the converted tables can become inconsistent. A where-used list should be created before ABAP Dictionary objects such as data elements or domains are changed.
