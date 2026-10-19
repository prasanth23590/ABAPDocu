---
title: "Exceptions in EXPORT"
source_file: abenrabax_export_to_database.html
section: "ABAP Programming Language > ABAP - Data Cluster > EXPORT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exceptions in EXPORT

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

## Catchable Exceptions

`CX_SY_COMPRESSION_ERROR`

- *Cause:* More than 2 GB of data is to be exported.

  *Runtime error:* `EXPORT_TOO_MUCH_DATA`

`CX_SY_EXPIMP_DB_SQL_ERROR`

- *Cause:* SQL error in export to the database.

  *Runtime error:* [`DBIF_...`](../abap-database-access/abenabap_sql_exceptions.md)

`CX_SY_EXPORT_BUFFER_NO_MEMORY`

- *Cause:* The size of the data cluster exceeds a quarter of the total size of the associated application buffer.

  *Runtime error:* `EXPORT_BUFFER_NO_MEMORY`

`CX_SY_EXPORT_NO_SHARED_MEMORY`

- *Cause:* Data cluster is too large for the associated application buffer. This buffer is almost completely filled.

  *Runtime error:* `EXPORT_NO_SHARED_MEMORY`
