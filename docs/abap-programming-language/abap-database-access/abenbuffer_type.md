---
title: "Table Buffering - Buffering Types"
source_file: abenbuffer_type.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering - Buffering Types

The following buffering types can be defined for a DDIC database table or CDS view entity:

- [Table Buffering - Single Record Buffering](abenbuffer_single_buffering.md)

- [Table Buffering - Generic Buffering](abenbuffer_generic_buffering.md)

- [Table Buffering - Full Buffering](abenbuffer_complete_buffering.md)

The buffering type is defined and transported separately from the buffered entity.

- For DDIC database tables this is done as [part](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_buffer.md) of their [technical settings](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_techspec.md).

- For CDS entities, a tuning object named [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md) is defined that defines table buffering settings.

## Hint

If generic buffering or full buffering is activated, and the database table is specified statically in an ABAP SQL statement, the [secondary indexes](../../abap-glossary/abensecondary_index_glosry.md) of the table are not ignored when the data is read from the [table buffer](../../abap-glossary/abentable_buffer_glosry.md). If single record buffering is used, only the primary index is read. A secondary index defined in the ABAP Dictionary is evaluated regardless of whether the index was created on the database or not.
