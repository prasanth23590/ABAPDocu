---
title: "ABAP SQL - Streaming"
source_file: abenabap_sql_streaming.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Streaming and Locators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Streaming

ABAP SQL supports [streaming](../../abap-glossary/abenstreaming_glosry.md) for [LOBs](../../abap-glossary/abenlob_glosry.md) in data sources.

- [System Classes and System Interfaces for Reader and Writer Streams](abenabap_sql_streaming.md#system-classes-and-system-interfaces-for-reader-and-writer-streams)

- [Important Methods](abenabap_sql_streaming.md#important-methods)

- [Data Sources and Data Sinks](abenabap_sql_streaming.md#data-sources-and-data-sinks)

- [Creating Data Streams for LOBs](abenabap_sql_streaming.md#creating-data-streams-for-lobs)

  - [Reader Streams](abenabap_sql_streaming.md#reader-streams)

  - [Writer Streams](abenabap_sql_streaming.md#writer-streams)

- [Closing Data Streams for LOBs](abenabap_sql_streaming.md#closing-data-streams-for-lobs)

- [Examples](abenabap_sql_streaming.md#examples)

## System Classes and System Interfaces for Reader and Writer Streams

The [system classes](../../abap-glossary/abensystem_class_glosry.md) for the various types of [data streams](../../abap-glossary/abendata_stream_glosry.md) are:

- `CL_ABAP_DB_C_READER` for character-like reader streams. The [streaming data source](../../abap-glossary/abenstreaming_data_source_glosry.md) is a [CLOB](../../abap-glossary/abenclob_glosry.md).

- `CL_ABAP_DB_X_READER` for binary reader streams. The [streaming data source](../../abap-glossary/abenstreaming_data_source_glosry.md) a [BLOB](../../abap-glossary/abenblob_glosry.md).

- `CL_ABAP_DB_C_WRITER` for character-like writer streams. The [streaming data sink](../../abap-glossary/abenstreaming_data_sink_glosry.md) is a [CLOB](../../abap-glossary/abenclob_glosry.md).

- `CL_ABAP_DB_X_WRITER` for binary writer streams. The [streaming data sink](../../abap-glossary/abenstreaming_data_sink_glosry.md) a [BLOB](../../abap-glossary/abenblob_glosry.md).

The special interfaces

- `IF_ABAP_DB_READER`

- `IF_ABAP_DB_WRITER`

are used to access the reader and writer streams independently of the [stream type](../../abap-glossary/abenstream_type_glosry.md). For further resource-independent classes and interfaces, as well as for the hierarchy of the object types, see the figure and explanation under [Streaming](../abap-processing-internal-data/abenstreaming.md).

## Important Methods

The methods for streaming in ABAP SQL are the same as for general [streaming](../abap-processing-internal-data/abenstreaming.md).

## Data Sources and Data Sinks

Any [LOBs](../../abap-glossary/abenlob_glosry.md) declared in DDIC database tables can be considered as data sources or data sinks. The instances of the classes above are [data streams](../../abap-glossary/abendata_stream_glosry.md) bound to LOBs. These are [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) and implement the [corresponding interfaces](abenlob_interfaces.md). Their use in ABAP SQL involves reference variables that point to the relevant LOB handles.

## Creating Data Streams for LOBs

### Reader Streams

A reader stream that is bound to an LOB, that is, an instance of the class `CL_ABAP_DB_C_READER` or `CL_ABAP_DB_X_READER`, can only be created by assigning a LOB from the result set to a reference variable for a reader stream in the [`INTO`](abapinto_clause.md) clause of the statement [`SELECT`](abapinto_clause.md).

See [`SELECT` - LOB Handles](abenselect_into_lob_handles.md).

### Writer Streams

A writer stream that is bound to an LOB, that is, an instance of the class `CL_ABAP_DB_C_WRITER` or `CL_ABAP_DB_X_WRITER`, can only be created by specifying a reference variable for a reader stream as a source in the statements [`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), or [`MODIFY`](abapmodify_dbtab.md). It is not possible to specify more general reference variables.

See [`INSERT`, `UPDATE`, `MODIFY dbtab` - LOB Handles](abenium_lob.md).

## Closing Data Streams for LOBs

Since the number of simultaneously opened data streams is limited to 16, they should be closed as soon as possible using the `CLOSE` method. Regardless of this, reader streams are closed implicitly at the end of a `SELECT` loop and at the end of a database LUW. An open writer stream is closed implicitly only by using a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). In [database commits](../../abap-glossary/abendatabase_commit_glosry.md), on the other hand, an open writer stream produces the runtime error `COMMIT_STREAM_ERROR`.

## Examples

## Executable Examples
