---
title: "ABAP SQL - Table Buffering"
source_file: abensap_puffering.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Table Buffering

[Table buffering](../../abap-glossary/abentable_buffering_glosry.md) buffers data from the database in a [table buffer](../../abap-glossary/abentable_buffer_glosry.md) in the [shared memory](../../abap-glossary/abenshared_memory_glosry.md) of the current AS instance. Table buffering is possible for the following objects and takes place when they are accessed using ABAP SQL:

- [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md)

  For more information, see [DDIC - Table Buffering of Database Tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_buffer.md).

- [DDIC database views](../../abap-glossary/abendatabase_view_glosry.md) defined in the ABAP Dictionary

  For more information, see DDIC - Database Views.

- [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) defined in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md)

  For more information, see [ABAP CDS - Table Buffering of CDS View Entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_view_buffering.md).

- [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md) defined in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md)

  For more information, see [ABAP CDS - Projection Views](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_proj_views.md).

- [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) defined in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md)

  For more information, see [ABAP CDS - Table Buffering of CDS DDIC-Based Views](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_v1_buffering.md).

Whether and how a DDIC database table or DDIC database view is buffered is determined by its [technical settings](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_buffer.md). For a CDS entity, the buffering is determined by annotations and a [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md). Using buffering generally improves performance (by factors of between 50 and 500), since the data does not need to be transported between the AS ABAP and the database server each time and because changes between can be prevented.

When a DDIC or CDS object for which table buffering is defined is accessed using ABAP SQL, [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is active by default. The buffering of the tabular data in the table buffer is performed by the [database interface](../../abap-glossary/abendatabase_interface_glosry.md). The [buffering type](abenbuffer_type.md) defines which records are loaded into the buffer when it is accessed. When such database tables of views are accessed using ABAP SQL statements in a program the following process takes place:

- For [read accesses](abenabap_sql_reading.md), the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md) determines whether this data is in the table buffer of the current AS instance. If this is the case, the data is read directly from the buffer. If the data is not contained in the buffer of the AS instance, the data is read from the database and loaded into the buffer. This means the data can be accessed from the buffer next time.

- For [write accesses](abenabap_sql_writing.md), an [asynchronous buffer synchronization](abenbuffer_synchro.md) is invoked.

For processing the ABAP SQL statements for the buffered tabular data the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) is used. There are restrictions on accessing the table buffer for the following reasons.

- The ABAP SQL in-memory engine supports a large subset of ABAP SQL but there are also some [restrictions](abenabap_sql_inmemeng.md). If an ABAP SQL statement is used that is not supported by the ABAP SQL in-memory engine, a buffered table cannot be accessed in the table buffer. The table buffer is bypassed and the database table is accessed on the database.

- Depending on the [buffering type](abenbuffer_type.md), further [restrictions](abenbuffer_restrictions.md) can cause a bypassing of the table buffer.

The following sections go into more detail about table buffering:

- [Table Buffering - Buffering Types](abenbuffer_type.md)

- [Table Buffering - Buffer Synchronization](abenbuffer_synchro.md)

- [Table Buffering - Buffer Management](abenbuffer_memory.md)

- [Table Buffering - Restrictions](abenbuffer_restrictions.md)

- [Table Buffering](abentable_buffering_abexa.md) [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) are applied to the database directly and therefore always bypass table buffering.

## Hints

- Typical candidates for buffering are customizing tables and system tables. In certain cases, customizing-like tables with master data can also be buffered. If it is vital that current data is accessed from a buffered table, the addition [`BYPASSING BUFFER`](abapselect_bypassing_buffer.md) of the statement `SELECT` can be used. If this addition is used a lot, the table should be checked for its suitability for buffering or whether the current data is really always required.

- Buffering is not recommended for tables in the following cases:

  - The application must always have access to the current data and the delay caused by [asynchronous synchronization](abenbuffer_synchro.md) is not acceptable.

  - Many writes are performed on the tables. If more than one percent of the accesses are writes, buffering should be avoided, so that the extra work caused by synchronization does not outweigh the benefits of buffering.

- When accessing data clusters in export/import tables using the statements [`EXPORT ... TO DATABASE`](../abap-data-cluster/abapexport_data_cluster.md) and [`IMPORT ... FROM DATABASE`](../abap-data-cluster/abapimport_data_cluster.md), [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is not supported.

- If table buffering is [enabled](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_v1_buffering.md) for a [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), it is implicitly applied to its [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md). For [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), table buffering is applied directly to the CDS entity.

- Tables or views that can also be accessed using [AMDP](../../abap-glossary/abenamdp_glosry.md) should not be buffered. If AMDP methods modify data in buffered tables or views, this is ignored by the database interface and the buffers are not synchronized accordingly. This can cause inconsistencies between the data in the buffers and on the database.
