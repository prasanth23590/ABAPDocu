---
title: "table buffering"
source_file: abentable_buffering_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table buffering

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md) [DDIC](../abap-dictionary-ddic/abenddic_glossary.md)

## Definition

[Buffering](abensap_buffering_old_glosry.md) of data from [DDIC database tables](abenddic_db_table_glosry.md), [DDIC database views](abendatabase_view_glosry.md), or from [CDS entities](abencds_entity_glosry.md) in a [table buffer](abentable_buffer_glosry.md) in the [shared memory](abenshared_memory_glosry.md) of the current [AS instance](abenas_instance_glosry.md). Whether and how a DDIC database table or a DDIC database view is buffered is determined by its [technical settings](../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_buffer.md). For a CDS entity, the buffering is determined by annotations and a [CDS entity buffer](abencds_entity_buffer_glosry.md). Buffering is managed by the [database interface](abendatabase_interface_glosry.md). Table buffering is applied implicitly when the database is accessed using [ABAP SQL](abenabap_sql_glosry.md) In ABAP SQL, the [ABAP SQL in-memory engine](abenabap_sql_inmemeng_glosry.md) processes the tabular data in the table buffer.

[***-\>* More about**](../abap-programming-language/abap-database-access/abensap_puffering.md)
