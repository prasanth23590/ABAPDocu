---
title: "Table Buffering - Buffer Management"
source_file: abenbuffer_memory.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering - Buffer Management

- [Storage in the Memory](abenbuffer_memory.md#storage-in-the-memory)

## Storage in the Memory

Table buffering takes place in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) of each AS instance. The [table buffer](../../abap-glossary/abentable_buffer_glosry.md) consists of a central management structure, an alphabetical directory of tables, and a data area. The individual areas of a [generically buffered](abenbuffer_generic_buffering.md) table or view are managed as individual [fully buffered](abenbuffer_complete_buffering.md) tables. The buffered data is stored in the data area as [internal tables](../../abap-glossary/abeninternal_table_glosry.md). The data area is managed using SAP Memory Management.

When a buffered table or view is accessed using ABAP SQL, a search first takes place for the name of the table in the table directory and then a binary search takes place for the data.

In both single record buffering and in generic buffering, information about nonexistent rows in a table or view is also saved. The first time a nonexistent row is read, the key values of the primary key or generic key are loaded into the associated data area with an otherwise empty row and a corresponding flag. The next time an attempt is made to read this row, the buffer already indicates that this row does not exist.

### Hints

- The management of single record buffering slightly less efficient than generic or full buffering. In single record buffering, the rows are loaded into the internal table in the data area gradually. In generic buffering and full buffering, all data of a table or view is loaded in a single step and sorted on the database.

- When saved to memory, [null values](../../abap-glossary/abennull_value_glosry.md) are handled as such and are not transformed to type-dependent initial values.
