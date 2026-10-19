---
title: "ABAP SQL - Database Hints"
source_file: abenabap_sql_db_hints.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Database Hints

## Syntax

``` abap
 ... %_HINTS db @dbhint1 
           [db @dbhint2 
            ... ]  ...  
```

## Description

The addition `%_HINTS` can be used to specify [database hints](../../abap-glossary/abendatabase_hint_glosry.md) at the following positions in ABAP SQL statements:

- After the [main query](../../abap-glossary/abenmainquery_glosry.md) or [subquery](../../abap-glossary/abensubquery_glosry.md) clauses of `SELECT` statements.

- After the `WHERE` condition of the statements [`UPDATE`](abapupdate.md) and [`DELETE`](abapdelete_dbtab.md).

One or more database hints can be specified after `%_HINTS` as a blank-separated list in flat, character-like [literals](abenabap_sql_literals.md) or [host variables](abenabap_sql_host_variables.md) `dbhint1`, `dbhint2`, .... The addition `db` must be used in front of each database hint to specify the database system for which the hint is intended. The following table shows the possible additions and the associated database system:

| **Addition `db`** | **Database System**                                            |
|-------------------|----------------------------------------------------------------|
| `ABAP`            | [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) |
| `ADABAS`          | SAP MaxDB                                                      |
| `AS400`           | IBM System i (AS/400)                                          |
| `DB2`             | IBM DB2                                                        |
| `DB6`             | IBM DB2 UDB                                                    |
| `HDB`             | SAP HANA database                                              |
| `MSSQLNT`         | Microsoft SQL Server                                           |
| `ORACLE`          | Oracle DB                                                      |
| `SYBASE`          | Sybase ASE                                                     |

A database system can be specified more than once if there are multiple database hints for this system. The possible database hints are database-specific and may depend on the release of the database system.

- The database hints for the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) are listed under ABAP SQL In-Memory Engine, Database Hints.

- The database hints for [database systems](../../abap-glossary/abendatabase_system_glosry.md) can be found in the documentation of the respective database system.

An empty hint is ignored. Database hints are considered by the respective database system. If the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) is used for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) or an internal table with [`FROM @itab`](abapselect_itab.md), only the database hints listed behind `ABAP` are evaluated.

## Hints

- A database hint usually only affects the part of an ABAP SQL statement for which is it specified. It does not usually affect the way a statement works, but may affect performance.

- Database hints should only be used with extreme caution. For example, they can be used as a last resort to affect the optimizer of the database system when selecting a secondary index.

- If database hints are used, they should generally be checked every time the database release or system configuration is changed.

- Database hints of the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) are intended for internal use only. These are noted between `&` characters and are evaluated by the database interface before they are transferred to the database system.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of a [HANA-specific database hint](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f) for the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md).

``` abap
SELECT * 
       FROM scarr 
       WHERE carrid = 'LH' 
       %_HINTS HDB 'INDEX_SEARCH' 
       INTO TABLE @FINAL(result).
```
