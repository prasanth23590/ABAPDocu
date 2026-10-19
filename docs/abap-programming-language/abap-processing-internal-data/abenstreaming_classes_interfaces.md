---
title: "Classes and Interfaces for Streams"
source_file: abenstreaming_classes_interfaces.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Streaming"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Classes and Interfaces for Streams

The classes and interfaces of streams are in the package `SABP_STREAMS_AND_LOCATORS`. Interfaces and classes that have been released for use are exposed in their package interface `SABP_STREAMS_AND_LOCATORS`. The following figure shows the hierarchy of the most important interfaces and classes for streams. ![figure](images_abdoc_streaming.gif)

## Classes for Data Streams and Filter Streams

The classes for data streams and filter streams are the templates for data stream objects and filter stream objects.

The classes for the data stream category start with `CL_ABAP_`, followed by

1.  an ID `resource` for the resource that is used as a [streaming data source](../../abap-glossary/abenstreaming_data_source_glosry.md) or a [streaming data sink](../../abap-glossary/abenstreaming_data_sink_glosry.md). Currently, data streams are supported for the following resources:

    - [LOBs](../../abap-glossary/abenlob_glosry.md) in database tables; the associated resource ID is *[DB](../abap-database-access/abenabap_sql_streaming.md)*.

    - [Strings](../../abap-glossary/abenstring_glosry.md); the associated resource ID is [*STRING*](abenstring_streams.md).

    - [Internal tables](../../abap-glossary/abeninternal_table_glosry.md); the associated resource ID is [*ITAB*](abenitab_streams.md).

2.  an ID `type` for the stream type. Here the IDs *C* and *X* are possible for the binary streams or character streams.

3.  an ID `direction` for the stream direction. Here the IDs *READER* and *WRITER* are possible for reader streams or writer streams.

The classes for the filter stream category start with `CL_ABAP_FILTER_`, followed by the IDs `type` and `direction` with the same meanings as for data stream classes. Currently, no filter streams are implemented.

## Interfaces and Superclasses

All public methods of the data stream and filter stream classes are declared in interfaces which allow general access to the classes.

- The `IF_ABAP_direction` interface enables general access to all reader and writer streams.

- The `IF_ABAP_TYPE_direction` interface enables a type-dependent access to reader and writer streams.

- The `IF_ABAP_RESOURCE_direction` interface enables resource-dependent access to reader and writer streams.

- The `IF_ABAP_CLOSE_RESOURCE` interface contains the `CLOSE` method, which is required by all stream kinds in order to close an open resource. This also applies to filter streams, since these are usually connected to data streams and the resource can then only be closed using the filter stream.

Data stream classes inherit `CL_ABAP_TYPE_direction` from abstract superclasses. In these classes, methods are implemented that are dependent on the stream type and stream direction but independent of the resource.

## Important Methods

In the case of data streams, the following methods. The actual access to the [streaming data source](../../abap-glossary/abenstreaming_data_source_glosry.md) or [streaming data sink](../../abap-glossary/abenstreaming_data_sink_glosry.md) is completed by the ABAP runtime framework.

**Methods for Reader Streams**

Methods from the interface `IF_ABAP_READER`:

- `DATA_AVAILABLE` returns *X* if there is still data in the reader stream.

- `IS_X_READER` returns *X* if it is a binary stream.

- `READ` returns a string with a predefined number of bytes or characters from the reader stream.

- `SKIP` skips a predefined number of bytes or characters from the reader stream.

**Methods for Writer Streams**

Methods from the interface `IF_ABAP_WRITER`:

- `WRITE` writes the content of a passed string to a writer stream.

**Methods for Both Stream Categories**

Methods from the `IF_ABAP_CLOSE_RESOURCE` interface:

- `CLOSE` closes the stream.

- `IS_CLOSED` returns *X* if the stream is closed.
