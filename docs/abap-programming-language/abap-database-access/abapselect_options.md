---
title: "SELECT, OPTIONS"
source_file: abapselect_options.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, OPTIONS

## Syntax

``` abap
... [OPTIONS] 
      [PRIVILEGED ACCESS] 
      [BYPASSING BUFFER] 
      [CONNECTION ...] ...  
```

[`[PRIVILEGED ACCESS]`](abapselect_privileged_access.md) · [`[BYPASSING BUFFER]`](abapselect_bypassing_buffer.md) · [`[CONNECTION ...]`](abapselect_connection.md)

## Description

`OPTIONS` introduces a set of ABAP-specific additions to [`SELECT`](abapselect.md), [`WITH`](abapwith.md):

- [`PRIVILEGED ACCESS`](abapselect_privileged_access.md) disables [CDS access control](../../abap-glossary/abencds_access_control_glosry.md).

- [`BYPASSING BUFFER`](abapselect_bypassing_buffer.md) bypasses [table buffering](../../abap-glossary/abentable_buffering_glosry.md).

- [`CONNECTION`](abapselect_connection.md) specifies a [database connection](../../abap-glossary/abendatabase_connection_glosry.md).

The addition `OPTIONS` itself is optional but should be used in front of these additions. It must be placed at the end of a `SELECT` statement. If `OPTIONS` is specified, it must be followed by at least one of the additions and none of the additions must be placed before `OPTIONS`.

If `OPTIONS` is not specified, the additions must be placed after the [`INTO` clause](abapinto_clause.md) of a `SELECT` statement. The order of the additions is prescribed as shown above.
