---
title: "INSERT, UPDATE, MODIFY, DELETE writable_obj, OPTIONS"
source_file: abapiumd_options.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, UPDATE, MODIFY, DELETE writable_obj, OPTIONS

## Syntax

``` abap
 ... [OPTIONS] 
     [CONNECTION ...] ...  
```

[`CONNECTION ...`](abapiumd_conn.md)

## Description

`OPTIONS` introduces a set of ABAP-specific additions to [`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), [`MODIFY`](abapmodify_dbtab.md), [`DELETE`](abapdelete_dbtab.md).

[`CONNECTION`](abapiumd_conn.md) specifies a [database connection](../../abap-glossary/abendatabase_connection_glosry.md).

The addition `OPTIONS` itself is optional but should be used in front of these additions. It must be placed at the end of a DML statement.

If `OPTIONS` is specified, it must be followed by at least one addition and no addition must be placed before `OPTIONS`.

If `OPTIONS` is not specified, the addition `CONNECTION` can be placed after the target specification.
