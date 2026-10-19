---
title: "Table Buffering - Restrictions"
source_file: abenbuffer_restrictions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering - Restrictions

Only [transparent tables](../../abap-glossary/abentransparent_table_glosry.md) can be buffered. [Global temporary tables](../../abap-glossary/abenglobal_temporary_table_glosry.md) cannot be buffered. There is no special restriction on the key length of the table when buffering, which means that keys in buffered tables can be up to [900 bytes](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_key.md) long. For database accesses using [AMDP](../../abap-glossary/abenamdp_glosry.md), the table buffer is not used in principle.

Any [writes](abenabap_sql_writing.md) access the data in the database table directly and trigger [asynchronous buffer synchronization](abenbuffer_synchro.md). After the invalidation of an entry in the buffer using a write statement, the next five reads that should have accessed the entry bypass the buffer of the current AS instance by default. The next read performed on the changed entry reloads it into the buffer and removes the invalidation.

A [read](abenabap_sql_reading.md) statement should generally access the table buffer, but there are some restrictions that cause the buffer to be bypassed. Then, the statement is processed on the database and the DDIC database tables, DDIC views or CDS entities accessed directly.

- For read accesses, the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) is used, which does not support all elements of ABAP SQL statements. If an ABAP SQL statement is used that is not supported by the ABAP SQL in-memory engine (see the topic [ABAP SQL In-Memory Engine, Restrictions](abensql_engine_restr.md)), the table buffer is bypassed.

- For the [buffering types](abenbuffer_type.md) [single record buffering](abenbuffer_single_buffering.md) and [generic buffering](abenbuffer_generic_buffering.md) there are additional restrictions for `WHERE` conditions that can also cause the buffer to be bypassed:

  - When a table or view with single record buffering is accessed, all key fields of the primary key must be listed using equality conditions joined using `AND`.

  - When a generically buffered area is accessed, it must be specified completely using equality conditions joined using `AND`.

  - Only [host variables](../../abap-glossary/abenhost_variable_glosry.md) or [host expressions](../../abap-glossary/abenhost_expression_glosry.md) can be used on the right side of a relational expression that is used to identify a single record or a generically buffered area.

  - If [`FOR ALL ENTRIES`](abenwhere_all_entries.md) is used when accessing a table or view with generic buffering, the generic area must be specified exactly, and multiple generic areas cannot be joined using `OR`.

  - In the variant of the operator `IN` with an [operand list](abenwhere_logexp_list_in.md), only column specifications are allowed on the left side of `IN` and only host variables or expressions on the right side.

- Reads on a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) that does not meet the [prerequisites](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_v1_buffering.md) for buffering bypass the buffer.

## Hints

- For performance reasons, the fact that the table buffer is bypassed when these restrictions are not met should always be remembered when accessing buffered tables or views.

- To bypass the table buffer in the statement `SELECT` explicitly, the addition [`BYPASSING BUFFER`](abapselect_bypassing_buffer.md) should always be used. It is not enough to rely on the implicit behavior itself.

- [`JOIN`](abapselect_join.md) expressions currently always bypass the buffer. The ABAP SQL in-memory engine supports join expressions for internal tables accessed by [`SELECT ... FROM @itab`](abapselect_itab.md) but not yet for database tables in the table buffer.

- The prerequisites for [table buffering of CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_view_buffering.md) are checked as restrictions for the view itself. If a CDS view entity can be enabled for table buffering and buffering is switched on with a [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md), there should be no reason for ABAP SQL to bypass the buffer.
