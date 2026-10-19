---
title: "itab - Performance Notes"
source_file: abenitab_perfo.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Performance Notes

- [Table Sharing](abenitab_perfo.md#table-sharing)

- [Initial Memory Requirement](abenitab_perfo.md#initial-memory-requirement)

- [Index Administration](abenitab_perfo.md#index-administration)

- [Block Processing of Table Lines](abenitab_perfo.md#block-processing-of-table-lines)

- [Selective Data Transport](abenitab_perfo.md#selective-data-transport)

- [Using Secondary Keys](abenitab_perfo.md#using-secondary-keys)

- [Deleting Table Lines](abenitab_perfo.md#deleting-table-lines)

- [Free Key Specified for Sorted Tables and Hashed Tables](abenitab_perfo.md#free-key-specified-for-sorted-tables-and-hashed-tables)

- [Sorting](abenitab_perfo.md#sorting)

## Table Sharing

When assignments are made between internal tables of the same type whose line type does not contain any table types, only the internal administration functions are passed to the [table body](../../abap-glossary/abentable_body_glosry.md) for performance reasons. [Table sharing](../../abap-glossary/abentable_sharing_glosry.md) is revoked only when write access to one of the tables involved is initiated. The actual copy process then takes place.

## Initial Memory Requirement

Internal tables are [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md) whose area in the memory is extended block by block. The size of the first block in the memory is called [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md) and can be affected in the declaration of an internal table using the additions [`INITIAL SIZE`](../abap-declarations/abaptypes_itab.md) and the obsolete `OCCURS`.

It is usually up to the system to determine the size of the first block. `INITIAL SIZE` is not used or specified with the value 0. In this case, a suitable block size is chosen the first time lines are added to an internal table.

Specifying a concrete value greater than 0 after `INITIAL SIZE` is only practical if it is known in advance how many entries are to be made in the table, and the first block is therefore to be created with the most suitable dimensions. This can be particularly important for internal tables that are components of other internal tables, and which only contain a few lines (no more than around 5).

To avoid excessive memory demands, the system ignores values that produce memory demands greater than the constant block size.

## Index Administration

In an [index table](../../abap-glossary/abenindex_table_glosry.md), the logical order of the table entries is not generally consistent with the physical order of the entries in the main memory. In this case, the logical order is no longer administrated by a physical index, but by a logical index. The same basically applies to the [secondary table indexes](../../abap-glossary/abensecondary_table_index_glosry.md) used to manage [secondary](../../abap-glossary/abensecondary_table_key_glosry.md) [sorted keys](../../abap-glossary/abensorted_key_glosry.md).

Use of the logical index produces additional memory requirements, and index maintenance places a high demand on resources (time and memory) when inserting or deleting table lines. The resource requirements increase proportionally with the number of remaining lines after the insertion or deletion position. For very large internal tables, this can result in considerable demands on performance at runtime.

The logical index is only created when it is needed, that is, when a line is inserted in front of another line, if the order of the table lines is changed, or a line other than the last line is deleted. A logical index is not required if an internal table is filled using only[`APPEND`](abapappend.md), and if only its last line or lines is/are deleted using [`DELETE`](abapdelete_itab.md).

### Hint

In contrast to filling a table with [`INSERT`](abapinsert_itab.md), appending lines with [`APPEND`](abapappend.md) does not require any resources for index maintenance. It is therefore preferable to use `APPEND` instead of `INSERT` to create a [standard table](../../abap-glossary/abenstandard_table_glosry.md). This is possible if the order of the entries is not important, or if entries can be appended in the correct order.

## Block Processing of Table Lines

If entire line areas of a table can be processed at once, this should not be done line-by-line, but using block operations. Block operations are possible using the `FROM` and `TO` additions of the statements [`INSERT`](abapinsert_itab.md), [`APPEND`](abapappend.md) and [`DELETE`](abapdelete_itab.md). Block operations are also more efficient than single record operations when reading from or modifying database tables with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements with the additions `FROM|APPENDING|TO TABLE`.

## Selective Data Transport

If, when reading table lines using [`READ TABLE`](abapread_table.md) or [`LOOP AT`](abaploop_at_itab.md), a work area is used or table lines can be changed using [`MODIFY`](abapmodify_itab.md) instead of direct access, the `TRANSPORTING` addition can be used to prevent unnecessary assignments of table components to the work area. This can lead to a noticeable improvement in performance, particularly if table-like components are excluded from processing.

## Using Secondary Keys

The [use of secondary table keys](../abap-data-types-and-data-objects/abenitab_key_secondary_usage.md) should be planned and executed carefully and sparingly. The time gained when accessing individual lines should not be lost again by the increased memory and time requirements for managing the secondary keys. Secondary keys are generally recommended for internal tables that are filled once and rarely changed during program execution.

## Deleting Table Lines

When lines are deleted from an internal table, administration costs are incurred for all table keys and table indexes. The primary key and all unique secondary keys are updated directly, but non-unique secondary keys are updated only if the line to be deleted is included in the updated part of an associated index ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)).

It should be noted that, particularly for standard tables, the mean runtime of the statement [`DELETE`](abapdelete_itab.md) always depends linearly on the number of table lines, even when secondary keys are specified using [`WITH TABLE KEY`](abapdelete_itab_key.md) or [`USING KEY`](abapdelete_itab_key.md). This is because a linear search is required to update the primary index, even though the line to be deleted can itself be found quickly.

Deleting lines in internal tables using [`DELETE`](abapdelete_itab.md) does not usually release any memory in the internal table. Statements such as [`CLEAR`](abapclear.md) or [`FREE`](abapfree_dataobject.md) must be used to release memory in internal tables.

## Free Key Specified for Sorted Tables and Hashed Tables

When using the [`READ`](abapread_table.md) statement with a specified free key of the form [`WITH KEY ...`](abapread_table_free.md), the search is optimized in all cases where this is possible, that is:

- In [sorted tables](../../abap-glossary/abensorted_table_glosry.md), if any initial section of the [table key](../../abap-glossary/abentable_key_glosry.md) or the complete table key is covered by the specified key.

- In [hashed tables](../../abap-glossary/abenhashed_table_glosry.md), if the complete table key is covered.

If part of a free key meets these conditions, this partial key is first used to search for an entry. In sorted tables, this is done using a binary search with a logarithmic consumption of resources, and in hashed tables using a hash algorithm, that is, with constant resource consumption. If an entry is found, the system checks whether the rest of the key conditions are also met. This means that over-specific keys in particular are optimized.

### Hint

See also [Optimization of the `WHERE` Condition](abenitab_where_optimization.md).

## Sorting

For textual sorting of an internal table in accordance with the current [text environment](../../abap-glossary/abentext_environment_glosry.md), it can be more efficient to use the statement [`CONVERT TEXT INTO SORTABLE CODE`](abapconvert_text.md) instead of [`SORT AS TEXT`](abapsort_itab.md) in the following cases:

- If an internal table is sorted by locale and then searched binarily using the statement `READ TABLE` or using a [table expression](abentable_expressions.md).

- An internal table must be sorted more than once.

- Indexes for database tables should be structured in accordance with a locale.
