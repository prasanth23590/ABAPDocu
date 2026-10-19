---
title: "Table Buffering - Buffer Synchronization"
source_file: abenbuffer_synchro.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering - Buffer Synchronization

- [Invalidating and Updating](abenbuffer_synchro.md#invalidating-and-updating)

- [Displacement](abenbuffer_synchro.md#displacement)

## Invalidating and Updating

A buffered table or view usually exists in the [table buffers](../../abap-glossary/abentable_buffer_glosry.md) of every AS instance. If a program in one of the AS instances modifies data from a table using ABAP SQL, the data is updated as follows:

- The data is modified in the database table on the database.

- The buffers of the current AS instance are invalidated immediately.

  - In changes made using [work areas](../../abap-glossary/abenwork_area_glosry.md), the affected row is invalidated in tables with single record buffering. In generically buffered tables, the affected generic area is invalidated and in fully buffered tables, the whole table is invalidated.

  - In changes made using [UPDATE writable_obj, source](abapupdate_source.md)`UPDATE` ... `SET ... WHERE ...` or [DELETE writable_obj, cond](abapdelete_where.md)`DELETE ... WHERE ...`, the entire table is invalidated in tables with single record buffering and full buffering. In generically buffered tables, all generic areas are invalidated that are affected by a left-aligned generic subkey.

  - In buffered [CDS views](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_v1_views.md), the entire buffer is invalidated regardless of the buffering type. In client-dependent views, however, this only affects the content of the [current client](../../abap-glossary/abencurrent_client_glosry.md).

- The invalidated data is written to the log table `DDLOG` of the database interface.

- Provided that no [database commits](../../abap-glossary/abendatabase_commit_glosry.md) have been performed for a change to the buffered table, all database reads on the AS instance in which the change was performed access the database directly and bypass the buffer. After a [database commit](../../abap-glossary/abendatabase_commit_glosry.md), the following applies to reads on this AS instance:

  - In the case of single record buffering and a change, which only relates to a single record in this type of table, the buffer is updated immediately on read access.

  - In the case of generic, completely buffered tables, the number of reads that access the database directly bypassing the buffer is 5 by default. The buffer is updated afterwards during the read with the data from the database.

- On all other AS instances, the buffers are still in the old state. Reads are still performed via the buffer and can potentially access obsolete data. The buffers of this AS instance are synchronized using the following asynchronous method:

  - A synchronization is performed on every AS instance in a specified time interval. The default interval is two minutes. The database interface reads the log table `DDLOG` and invalidates the buffer content in the same way as on the AS instance where the original change was made.

  - After synchronization, in the case of single record buffering and a change, which only relates to a single record, the buffer is updated via read access. In the case of generic, completely buffered tables, the number of reads that access the database is 5 by default. The buffer is only properly updated afterwards during the next read.

### Hints

- Asynchronous synchronization has the benefit of keeping the network load on the system low, particularly when compared with synchronous methods where each change made to the buffered data of an AS instance is broadcast immediately to all other AS instances. The drawback of asynchronous synchronization is that, unlike synchronous methods, the data is not up-to-date in the time between two synchronizations.

- The asynchronous method of buffer synchronization affects the decision as to whether or not a DDIC database table can be buffered. Tables where many writes are performed are not suited to buffering, since the table buffers would then often be inconsistent, and the system would constantly be invalidating and loading the buffers.

- Changes made using a `WHERE` condition place a far greater load on buffer management on the current AS instance than changes made to single rows.

- In fully buffered client-specified tables or views, it should be noted that generic buffering is performed internally with the client column as a generic key. This means that an invalidation of the entire buffer only affects the content of the current client.

## Displacement

If the free memory in the buffer falls below a preset value or the quality of access is poor, data is displaced from the buffer. The quality of access depends on the number of accesses that can be met directly from the buffer.

The need for displacements is checked asynchronously at specific points in time that are determined dynamically using the accesses to the buffer, which means that the length of time between two displacements depends on the buffer load.

Data is displaced from those tables that are accessed least often. Here, accesses to a table are weighted differently depending on the time they take place. Older accesses, for example, are weighted less than those that take place shortly before the displacement. This makes it possible to displace those tables from the buffer that are accessed a lot at one particular point in time but then no longer used.

### Hint

The individual generic areas of [generically buffered tables](abenbuffer_generic_buffering.md) are handled like standalone tables, which means that certain generic areas of a table can be displaced while other generic areas of the same table are kept in the buffer.
