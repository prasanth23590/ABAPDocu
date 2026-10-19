---
title: "INSERT, UPDATE, MODIFY writable_obj, LOB Handles"
source_file: abenium_lob.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, UPDATE, MODIFY writable_obj, LOB Handles

In the [`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), or [`MODIFY`](abapmodify_dbtab.md) statements, [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) can be created as [writer streams](../../abap-glossary/abenwriter_stream_glosry.md) and specified as [locators](../../abap-glossary/abenlocator_glosry.md).

- [Prerequisites](abenium_lob.md#prerequisites)

- [Rules](abenium_lob.md#rules)

  - [Writes Using Writer Streams](abenium_lob.md#writes-using-writer-streams)

  - [Changing Accesses Using Locators](abenium_lob.md#changing-accesses-using-locators)

- [Restriction](abenium_lob.md#restriction)

- [Examples](abenium_lob.md#examples)

## Prerequisites

An [LOB](../../abap-glossary/abenlob_glosry.md) in a row to be inserted or changed can be supplied from an [LOB handle component](../../abap-glossary/abenlob_handle_glosry.md) of a work area or an individual reference variable for an LOB handle (at `UPDATE` with `SET`). The static type of each LOB handle component must be one of the following system classes for [streaming](abenabap_sql_streaming.md) or [locators](abenlocators.md):

- `CL_ABAP_DB_C_WRITER` or `CL_ABAP_DB_C_LOCATOR` in the case of [CLOBs](../../abap-glossary/abenclob_glosry.md).

- `CL_ABAP_DB_X_WRITER` or `CL_ABAP_DB_X_LOCATOR` in the case of [BLOBs](../../abap-glossary/abenblob_glosry.md).

The [stream type](../../abap-glossary/abenstream_type_glosry.md) or [locator type](../../abap-glossary/abenlocator_type_glosry.md) must match the data type of the LOBs.

## Rules

Unlike in [reads](abenselect_into_lob_handles.md), the behavior for streams does not match the behavior for locators.

### Writes Using Writer Streams

If, in a changing access, an [LOB](../../abap-glossary/abenlob_glosry.md) is linked with a reference variable of the type `CL_ABAP_DB_C_WRITER` or `CL_ABAP_DB_X_WRITER`, a corresponding writer stream is usually created, and the reference variable points to the object after execution. The LOB to be changed can be processed using the methods of the writer stream. When an LOB is linked with a writer stream that is referenced by an [LOB handle component](../../abap-glossary/abenlob_handle_component_glosry.md) from the source work area, the following various platform-dependent behavior may occur:

- On some database systems (MaxDB, Oracle), the components of the work area that are not LOB handle components are written directly to the database when executing the statement. If the rows cannot be inserted or changed, `sy-subrc` and `sy-dbcnt` respectively are set immediately and no writer stream is created for the LOB handle components. If the rows can be inserted or changed, writer streams are created and their content is passed to the database when closing the last writer stream of the ABAP SQL statement at the latest.

- On other database systems, the components of the work area that are not LOB handle components are not written directly to the database when executing the statement. Instead, writer streams are always created for the LOB handle components. The content of the remaining components is also delayed, that is, it is passed when closing the last writer stream of the ABAP SQL statement at the latest. Between executing the statement and actually writing the remaining components, the status is undefined since it is not yet determined whether the operation can be executed at all. In this case, `sy-subrc` is set to the value 2 and `sy-dbcnt` is set to -1 after the execution of the statement. Before a writer stream is closed, a reference to an object from the class `CL_ABAP_SQL_CHANGING_STMNT`, a subclass of `CL_ABAP_SQL_STATEMENT_HANDLE`, from the interface `IF_ABAP_DB_WRITER`, can be obtained using the method `GET_STATEMENT_HANDLE`. The `GET_STATE` method provides information about the status of the ABAP SQL statement and the `GET_DB_COUNT` method returns the number of inserted or changed rows after the last writer stream of the ABAP SQL statement was closed. The methods of the abstract superclass can be used to check the status of the ABAP SQL statement and all streams that are still open can be closed. If the ABAP SQL statement is not closed by the closing of the last writer stream, `GET_DB_COUNT` also returns the value -1. If the operation cannot be executed, for example, due to duplicate key entries, the exception `CX_STREAM_IO_EXCEPTION` or `CX_CLOSE_RESOURCE_ERROR` is raised when the data is passed to the database, depending on exactly when the data is passed.

A writer stream created in this way exists until it is explicitly closed using its method `CLOSE` from the `IF_ABAP_CLOSE_RESOURCE` interface. As long as a writer stream for an ABAP SQL statement is still open, the corresponding database operation is not completed. The state of the ABAP SQL statement is described using an object of the `CL_ABAP_SQL_STATEMENT_HANDLE` class, for which the `GET_STATEMENT_HANDLE` method returns a reference for every writer stream.

When using writer streams, an uncatchable exception is raised in the following cases:

- If a writer stream is still open when closing a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) using a [database commit](../../abap-glossary/abendatabase_commit_glosry.md).

- When accessing a writer stream that is already closed.

### Hints

- Exactly when the data of a writer stream is passed to the database is not defined. The data is passed at the latest when the last writer stream is closed but can also occur during writing in the stream, for example, because a buffer is no longer sufficient.

- A writer stream should always be closed explicitly and as soon as possible using its method `CLOSE`. See also [Streaming and Locators](abenstreams_locators.md).

### Changing Accesses Using Locators

If, in a changing access, an [LOB](../../abap-glossary/abenlob_glosry.md) is linked with a reference variable of type `CL_ABAP_DB_C_LOCATOR` or `CL_ABAP_DB_X_LOCATOR`, this variable must point to an appropriate locator, [created](abenselect_into_lob_handles.md) in a statement `SELECT` for a LOB in a different DDIC database table or the same table. If the statement can be executed (`sy-subrc` is 0), the LOB to be changed is replaced directly in the database system using the complete LOB of the locator.

## Restriction

The following restrictions apply:

- A maximum of 16 data streams can be opened for an ABAP SQL statement.

- In a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) there can be a maximum of 16 ABAP SQL statements whose data streams are open at the same time.

- A maximum of 1000 LOB handles can be open in a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md).

### Hint

A LOB handle should always be closed as soon as possible using its method `CLOSE`. See also [Streaming and Locators](abenstreams_locators.md).

## Examples

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Components `string1` and `string2` in structure `wa` are declared as LOB handles for character-like writer streams. The statement `MODIFY` creates the writer streams. Character strings are passed to both writer streams via reference variable `stmnt`. Once the writer streams have been closed, the associated database fields `STRING1` and `STRING2` contain the chained content of the streams.

``` abap
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
DATA wa TYPE demo_expressions WRITER FOR COLUMNS string1 string2. 
 
wa = VALUE #( id = 'X' ). 
 
MODIFY demo_expressions FROM @wa. 
 
DATA(stmnt) = wa-string1->get_statement_handle( ). 
DO 10 TIMES. 
  wa-string1->write( CONV #( sy-index ) ). 
ENDDO. 
wa-string1->close( ). 
 
stmnt = wa-string2->get_statement_handle( ). 
 
DO 26 TIMES. 
  wa-string2->write( substring( val = abcde 
                                 off = sy-index - 1 
                                len = 1 ) ). 
ENDDO. 
wa-string2->close( ). 
 
SELECT SINGLE string1, string2 
       FROM demo_expressions 
        WHERE id = 'X' 
       INTO @FINAL(result). 
cl_demo_output=>display( result ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the statement `UPDATE`, column `STRING2` is modified with a locator, which was created in a `SELECT` statement for column `STRING1` of the same CDS table entity. Afterwards, `STRING1` and `STRING2` have the same content.

``` abap
FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
 
DELETE FROM demo_cds_expressions. 
INSERT demo_cds_expressions FROM @( VALUE #( id = 'X' string1 = abcde ) 
). 
 
DATA locator TYPE REF TO cl_abap_db_c_locator. 
 
SELECT SINGLE string1 
       FROM   demo_cds_expressions 
       WHERE  id = 'X' 
       INTO   @locator. 
 
UPDATE demo_cds_expressions SET string2 = @locator WHERE id = 'X'. 
 
SELECT SINGLE string1, string2 
       FROM demo_cds_expressions 
       WHERE id = 'X' 
       INTO @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Executable Examples

- [Locator, Copy Column](abendb_copy_abexa.md)
