---
title: "ABAP SQL - LOB Interfaces"
source_file: abenlob_interfaces.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Streaming and Locators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - LOB Interfaces

ABAP SQL supports access to [LOBs](../../abap-glossary/abenlob_glosry.md) using [streams](abenabap_sql_streaming.md) and [locators](abenlocators.md). For similar reads on these streams and locators, there are the interfaces

- `IF_ABAP_DB_BLOB_HANDLE` and

- `IF_ABAP_DB_CLOB_HANDLE`,

which both include the superordinate interface

- `IF_ABAP_DB_LOB_HANDLE`

which then also includes the interface `IF_ABAP_CLOSE_RESOURCE`.

The connection to streams and locators is as follows:

- The system classes `CL_ABAP_DB_C_READER` and `CL_ABAP_DB_C_LOCATOR` both implement the interface `IF_ABAP_DB_CLOB_HANDLE`.

- The system classes `CL_ABAP_DB_X_READER` and `CL_ABAP_DB_X_LOCATOR` both implement the interface `IF_ABAP_DB_BLOB_HANDLE`.

- The interface `IF_ABAP_DB_READER` includes `IF_ABAP_DB_LOB_HANDLE`.

The instances of the system classes that implement the interface `IF_ABAP_DB_LOB_HANDLE` are called [LOB handles](../../abap-glossary/abenlob_handle_glosry.md).

## Hints

- The LOB interfaces shown here can only be used for reads. Reference variables for LOB handles that are specified as read targets of the [`INTO` clause](abapinto_clause.md) in the [`SELECT`](abapselect.md) statement can be typed statically using these interfaces. The class used to create the object must then be specified using the special addition [`CREATING`](abapselect_creating.md) in the statement `SELECT`. For writes with the statements [`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), or [`MODIFY`](abapmodify_dbtab.md), the reference variables that are used as a source must be typed using the classes for writer streams or locators.

- The LOB interfaces shown here cannot be used in combination with SQL expressions. To use streaming and locators on SQL expressions, the system classes for handling LOBs must be used directly.
