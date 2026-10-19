---
title: "DELETE writable_obj, cond"
source_file: abapdelete_where.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > DELETE writable_obj"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE writable_obj, cond

## Syntax

``` abap
... [WHERE sql_cond] 
    [db_hints] 
    [ORDER BY ... [OFFSET o]] [UP TO n ROWS] ...  
```

[`sql_cond`](abenasql_cond.md) · [`db_hints`](../../abap-glossary/abendatabase_hint_glosry.md)

### Addition

[1. `... WHERE sql_cond`](abapdelete_where.md#addition-1)

[2. `... db_hints`](abapdelete_where.md#addition-2)

[3. `... [ORDER BY ... [OFFSET o]] [UP TO n ROWS]`](abapdelete_where.html#addition-3)

## Overview

### Description

In the variant `DELETE FROM target` of the statement [`DELETE`](abapdelete_dbtab.md), these additions determine the rows to be deleted.

## Addition 1

`... WHERE sql_cond`

### Description

The addition `WHERE` determines which rows in a [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) are deleted. Those rows are deleted for which the logical expression [`sql_cond`](abenabap_sql_stmt_logexp.md) is true. The logical expression `sql_cond` is subject to the restriction that no subqueries can be evaluated on the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be changed. If there is no database row that satisfies the `WHERE` condition, no rows are deleted and `sy-subrc` is set to 4. If no `WHERE` condition is specified, all rows are deleted or as many rows as specified by the addition `UP TO`. [Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies. In a client-specific target, only rows in the [current client](../../abap-glossary/abencurrent_client_glosry.md) are deleted by default. The [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent target cannot be specified in the `WHERE` condition.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following example, all today's flights of an airline in which no seats are occupied are deleted from the DDIC database table `SFLIGHT`. See also the example for [`dtab-source`](abapdelete_source.md).

``` abap
DATA carrid TYPE sflight-carrid. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
DELETE FROM sflight 
WHERE carrid = @carrid AND 
      fldate = @( cl_demo_date_time=>get_user_date( ) ) AND 
      NOT seatsocc > 0.
```

## Addition 2

`... db_hints`

### Description

In the variant `DELETE FROM TARGET`, [`db_hints`](abenabap_sql_db_hints.md) can be used to specify [database hints](../../abap-glossary/abendatabase_hint_glosry.md).

## Addition 3

`... [ORDER BY ... [OFFSET o]] [UP TO n ROWS]`

### Description

The addition `ORDER BY` is used to sort the rows defined by the `WHERE` condition. The addition `OFFSET` is used to delete only rows from the counter `o`. The addition `UP TO` restricts the number of rows to delete to `n`.

The addition `OFFSET` can only be specified together with `ORDER BY`. The addition `ORDER BY` cannot be specified without `OFFSET` or `UP TO`. If the addition `UP TO` is specified without `ORDER BY`, it is not possible to define which of the possible rows are deleted.

`n` and `o` expect [host variables](abenabap_sql_host_variables.md), [host expressions](abenabap_sql_host_expressions.md), or [literals](abenabap_sql_literals.md) with the type `i`, which can represent all non-negative numbers of the value range of `i` except its maximum value +2,147,483,647. If 0 is specified for `n`, this maximum value is used. If 0 is specified for `o`, the addition `OFFSET` is ignored. Only the types `b`, `s`, `i`, or `int8` can be specified. If `n` or `o` is specified as a literal or constant, the value 0 is not allowed.

The addition `ORDER BY` has the same [syntax and semantics](abaporderby_clause.md) as in the [`SELECT`](abapselect.md) statement, with the difference that it is not possible to sort explicitly by the [client column](../../abap-glossary/abenclient_column_glosry.md) in the `DELETE` statement and that a column cannot be specified by its position `n`. The `SELECT`-specific restrictions, on the other hand, are ignored.

### Hints

- The addition `UP TO` can be used to prevent errors when deleting tables with a large number of entries. Errors of this type can occur, for example, if the internal transaction manager has run out of memory. Exceptions can be raised on the database here if `UP TO` is not used and not followed by a [database commit](../../abap-glossary/abendatabase_commit_glosry.md). These resource bottlenecks can be prevented by distributing the delete action to multiple `DELETE` statements and hence deleting the corresponding log entries.

- If the addition `ORDER BY` is specified but does not sort uniquely, it is not defined which rows are deleted.

- A `DELETE` statement with the additions `OFFSET` and `UP TO` is executed on the database as a single operation, if possible. In databases not supported by the additions `OFFSET` and `ORDER BY`, the statements `SELECT` and `DELETE` are separated internally. If [database table logging](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_protocol.md) is enabled, these statements are always separated. This is generally slower than executing a single database operation.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of entries from a DDIC database table filled using [`MODIFY`](abapmodify_dbtab.md) in multiple iterations.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES bigtab TYPE TABLE OF demo_big_table WITH EMPTY KEY. 
 
MODIFY demo_big_table FROM TABLE 
  @( VALUE bigtab( FOR i = 1 UNTIL i > 1111111 
     ( id = i value = |{ i }| ) ) ). 
 
DATA subrc TYPE sy-subrc. 
DATA dbcnt TYPE sy-dbcnt. 
WHILE subrc = 0. 
  DELETE FROM demo_big_table UP TO 100000 ROWS. 
  subrc = sy-subrc. 
  dbcnt = sy-dbcnt. 
  out->write( |sy-subrc: { subrc 
            }, sy-dbcnt: { dbcnt } | ). 
ENDWHILE. 
 
out->display( ).
```
