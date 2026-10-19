---
title: "SELECT, LOB Handles"
source_file: abenselect_into_lob_handles.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, INTO, APPENDING"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, LOB Handles

In a standalone [`SELECT`](abapselect.md) statement or a [`WITH`](abapwith.md) statement, but not in a `FETCH` statement, [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) can be created as [reader streams](../../abap-glossary/abenreader_stream_glosry.md) and as [locators](../../abap-glossary/abenlocator_glosry.md) in the [`INTO`](abapinto_clause.md) clause.

- [Prerequisites](abenselect_into_lob_handles.md#prerequisites)

- [Rules](abenselect_into_lob_handles.md#rules)

- [Restriction](abenselect_into_lob_handles.md#restriction)

- [Examples](abenselect_into_lob_handles.md#examples)

## Prerequisites

An [LOB](../../abap-glossary/abenlob_glosry.md) from the result set can be assigned to an [LOB handle component](../../abap-glossary/abenlob_handle_component_glosry.md) of a work area, or to an individual reference variable for an LOB handle. The static type of all LOB handle components must contain the [interface](../../abap-glossary/abenoo_intf_glosry.md) `IF_ABAP_DB_LOB_HANDLE` and match the corresponding [data source](abapselect_data_source.md) component, that is, they must be less specific or the same as one of the following system classes for [streaming](abenabap_sql_streaming.md) or [locators](abenlocators.md):

- `CL_ABAP_DB_C_READER` or `CL_ABAP_DB_C_LOCATOR` in the case of [CLOBs](../../abap-glossary/abenclob_glosry.md).

- `CL_ABAP_DB_X_READER` or `CL_ABAP_DB_X_LOCATOR` in the case of [BLOBs](../../abap-glossary/abenblob_glosry.md).

The [stream type](../../abap-glossary/abenstream_type_glosry.md) or [locator type](../../abap-glossary/abenlocator_type_glosry.md) must match the data type of the LOBs.

## Rules

If an [LOB](../../abap-glossary/abenlob_glosry.md) from the result set of a selection is assigned to an LOB handle component of a work area or to an individual reference variable for an [LOB handle](../../abap-glossary/abenlob_handle_glosry.md), either

- a [reader stream](../../abap-glossary/abenreader_stream_glosry.md) is created as an instance of one of the classes `CL_ABAP_DB_C_READER`, `CL_ABAP_DB_X_READER` or,

- a [locator](../../abap-glossary/abenlocator_glosry.md) is created as an instance of one of the classes `CL_ABAP_DB_C_LOCATOR` or `CL_ABAP_DB_X_LOCATOR`

and after the execution of the `SELECT` statement the reference variable points to the object. The class used is determined using the data type of the column of the result sets and the static type of the target variable, or using the addition [`CREATING`](abapselect_creating.md) if required. The LOB to be read can be evaluated or forwarded using LOB handle methods.

An LOB handle created in this way, that is, a reader stream or a locator, exists until it:

- is closed explicitly using its `CLOSE` method from the `IF_ABAP_CLOSE_RESOURCE` interface, or

- is closed implicitly at the end of the current [database LUW](../../abap-glossary/abendatabase_luw_glosry.md).

Reader streams, but not locators, are also closed implicitly by the statement [`ENDSELECT`](abapendselect.md).

Accessing a closed LOB handle produces a runtime error.

Special properties of open reader streams and locators:

- As long as a reader stream for an ABAP SQL statement is still open, the associated database is not closed. This state can only occur with [`SELECT SINGLE`](abapselect_single.md), since there is no implicit termination of the reader stream using `ENDSELECT`. In this case, a reference to an object of the class `CL_ABAP_SQL_SELECT_STATEMENT`, a subclass of `CL_ABAP_SQL_STATEMENT_HANDLE`, can be obtained from the interface `IF_ABAP_DB_READER` using the method `GET_STATEMENT_HANDLE` before closing the reader stream. The methods of the abstract superclass implemented there can be used to check the state of the ABAP SQL statement, and all streams that are still open can be closed.

- It is guaranteed that, once created, a locator always works with the same LOB data. If the associated LOB column is modified while a locator is open, an internal copy of the LOB data for the locator is created on the database first.

## Restriction

The following restrictions apply:

- A maximum of 16 data streams can be opened for an ABAP SQL statement.

- In a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) there can be a maximum of 16 ABAP SQL statements whose data streams are open at the same time.

- A maximum of 1000 LOB handles can be open in a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md).

- If LOB handles are created together with the addition [`SINGLE`](abapselect_single.md), all primary key fields in logical expressions joined using `AND` in the [`WHERE` condition](abapwhere.md) are checked for equality.

### Hint

A LOB handle should always be closed as soon as possible using its method `CLOSE`. See also [Streaming and Locators](abenstreams_locators.md).

## Examples

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a BLOB to a reader stream.

``` abap
DATA reader TYPE REF TO cl_abap_db_x_reader. 
 
SELECT SINGLE picture 
       FROM demo_blob_table 
       WHERE name = '...' 
       INTO @reader.
```

## Executable Examples

- [Locator, copy column](abendb_copy_abexa.md)
