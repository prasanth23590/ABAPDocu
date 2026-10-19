---
title: "Data Consistency"
source_file: abendata_consistency.html
section: "ABAP Programming Language > ABAP - Database Access"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Data Consistency

When data in database tables is modified by application programs, it must be ensured that the data is consistent after the changes have been made. This is particularly important when data is processed in the database. The time span in which a consistent data state is transferred to another consistent state is known as a Logical Unit of Work (LUW). If an error occurs in an LUW, it is possible to undo all changes made up to this point and restore the data to its original consistent state (rollback). When a new consistent state has been reached, this new state can be committed and a new LUW can be opened.

For an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) two types of LUWs play a role:

- [Database LUWs](abendb_transaction.md) realized by the database system

- [SAP LUWs](abensap_luw.md) realized using special ABAP programming techniques

- Only data of the [current client](../../abap-glossary/abencurrent_client_glosry.md) can be accessed. The topic [Client Isolation](abenclient_isolation.md) describes the respective concept that is based on the implicit client handling of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [client-safe](../../abap-glossary/abenclient_safe_glosry.md) repository objects for [AMDP](../../abap-glossary/abenamdp_glosry.md).

## Hint

The [authorizations](../abap-authorizations/abenbc_authority_check.md) of a user when accessing data are also relevant for data consistency. The statement [`AUTHORITY-CHECK`](../abap-authorizations/abapauthority-check.md) is used for explicit authorization checks in ABAP programs. [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) also offers its own [access control](../../abap-glossary/abencds_access_control_glosry.md) based on implicit evaluations of [access conditions](../../abap-glossary/abenaccess_condition_glosry.md).
