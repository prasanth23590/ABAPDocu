---
title: "SELECT"
source_file: abapselect.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT

## Syntax

``` abap
SELECT mainquery_clauses 
  [UNION|INTERSECT|EXCEPT ...] 
  INTO|APPENDING target 
  [UP TO ...] [OFFSET ...] 
  [OPTIONS ...]. 
  ... 
[ENDSELECT].  
```

[`mainquery_clauses`](abapselect_mainquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`INTO|APPENDING`](abapinto_clause.md) · [`UP TO ...] [OFFSET ...]`](abapselect_up_to_offset.html) · [`OPTIONS ...`](abapselect_options.md) · [`ENDSELECT`](abapendselect.md)

## Description

Use of the [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `SELECT` as a standalone statement. This statement reads data from one or more [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) or [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md), uses this data to create a multirow or a single row result set, and assigns this result set to suitable ABAP data objects.

The additions [`mainquery_clauses`](abapselect_mainquery.md) define which data is read from the database in which form. The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple queries. In this case, special rules [`query_clauses`](abapunion_clause.md) apply when specifying clauses. Finally, the following properties are defined:

- ABAP target objects

  In the [`INTO`](abapinto_clause.md) clause after `INTO` or `APPENDING`, the `target` data objects are specified, to which the result set is assigned by row or by package.

- Restricting the result set

  The additions [`UP TO`](abapselect_up_to_offset.md) and [`OFFSET`](abapselect_up_to_offset.md) determine the number of rows to be read.

- ABAP-specific additions

  Optional additions behind [`OPTIONS`](abapselect_options.md) disable [CDS access control](../../abap-glossary/abencds_access_control_glosry.md), define whether [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is to be bypassed.

In the following cases, the statement `SELECT` opens a loop that must be closed using [`ENDSELECT`](abapendselect.md).

- If an assignment is made to a non-table-like target range, that is, a `SELECT` statement without the addition [`INTO|APPENDING ... TABLE`](abapinto_clause.md), a loop closed by `ENDSELECT` always occurs, except in the following instances:

  - The addition [`SINGLE`](abapselect_single.md) for reading a single row is specified after `SELECT`

  - The columns of the result set are specified statically in the [`SELECT` list](abapselect_list.md), they contain only [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md), and the additions [`GROUP BY`](abapgroupby_clause.md), [`UNION`](abapunion_clause.md), [`INTERSECT`](abapunion_clause.md), and [`EXCEPT`](abapunion_clause.md) are not specified.

- If an assignment is made to a table-like target range, that is, a `SELECT` statement with the addition [`INTO|APPENDING ... TABLE`](abapinto_clause.md), a loop closed by `ENDSELECT` occurs whenever the addition `PACKAGE SIZE` is used.

In each loop iteration, the `SELECT` statement assigns a row or a package of rows to the data objects specified in `target`. If the last row has been assigned or the result set is empty, `SELECT` jumps to `ENDSELECT`. A [database cursor](../../abap-glossary/abendatabase_cursor_glosry.md) is opened implicitly to process a `SELECT` loop, and is closed again when the loop has ended. In a program, a maximum of 17 database cursors can be open simultaneously across the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md). If more than 17 database cursors are opened, the runtime error `DBSQL_TOO_MANY_OPEN_CURSOR` occurs. If the entire result set is passed to the data object in one step, no loop is opened and the statement `ENDSELECT` cannot be specified.

A `SELECT` loop can be exited with one of the following statements:

- [`EXIT`](../abap-calling-and-exiting-program-units/abapexit_loop.md) that exits a complete loop and resumes the program behind the closing statement of the loop.

- A statement for [exiting the current processing block](../abap-calling-and-exiting-program-units/abenleave_processing_blocks.md)

In order to exit the current loop pass and to continue with the next loop pass, the statements [`CONTINUE`](../abap-calling-and-exiting-program-units/abapcontinue.md) and [`CHECK`](../abap-calling-and-exiting-program-units/abapcheck_processing_blocks.md) can be used.

The [`INTO` clause](abapinto_clause.md) introduced using `INTO|APPENDING` must be specified as the final clause of the `SELECT` statement and the optional additions [`UP TO`](abapselect_up_to_offset.md), [`OFFSET`](abapselect_up_to_offset.md), and [`abap_options`](abapselect_options.md) must be specified after the `INTO` clause.

## System Fields

The statement `SELECT` sets the values of the system fields `sy-subrc` and `sy-dbcnt`.

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | In each value passing to an ABAP data object, the statement `SELECT` sets `sy-subrc` to 0. In addition, `SELECT` sets `sy-subrc` to 0 before a `SELECT` loop is exited using `ENDSELECT`, if at least one row was passed in the loop.                                                                                                                     |
| 4              | The statement `SELECT` sets `sy-subrc` to 4 if the result set is empty. This usually means that no data was found on the database. Special rules apply when only [aggregate expressions](abapselect_aggregate.md) [specified as columns](abapselect_clause_col_spec.md) are used in the [`SELECT` list](abapselect_list.md) of the `SELECT` clause. |
| 6              | The statement `SELECT` sets `sy-subrc` to 6 if no lock can be set for the addition [`FOR UPDATE NOWAIT`](abapselect_single.md).                                                                                                                                                                                                                         |
| 8              | The statement `SELECT` sets `sy-subrc` to 8 if the addition [`FOR UPDATE`](abapselect_single.md) is used in `result`, and the [primary key](../../abap-glossary/abenprimary_key_glosry.md) is not fully specified after `WHERE`.                                                                                                                                          |

After each value that is passed to an ABAP data object, the statement `SELECT` sets `sy-dbcnt` to the number of rows passed. If an overflow occurs because the number or rows is greater than 2,147,483,647, `sy-dbcnt` is set to -1. If the result set is empty, `sy-dbcnt` is set to 0. As with `sy-subrc`, special rules apply when only [aggregate expressions](abapselect_aggregate.md) [specified in columns](abapselect_clause_col_spec.md) are used in the [`SELECT` list](abapselect_list.md) of the `SELECT` clause.

## Hints

- The query formulated in the `SELECT` statement is implemented in the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) for the programming interface of the database system and is passed to this system. The data is read in [packages](abenabap_sql_oview.md) from the database and transported from the database server to the current AS ABAP. On AS ABAP, the data is passed to the data objects of the ABAP program in accordance with the settings specified in the [`INTO`](abapinto_clause.md) and [`APPENDING`](abapinto_clause.md) additions.

- `SELECT` loops can be nested. For performance reasons, it may be more efficient to use a join or a [subquery](../../abap-glossary/abensubquery_glosry.md).

- Within a `SELECT` loop, no statements can be used that produce a [database commit](abendb_commit.md) or a [database rollback](abendb_rollback.md), causing the corresponding [database cursor](../../abap-glossary/abendatabase_cursor_glosry.md) to be closed as a result.

- The dynamic forms of the statements [`WITH`](abapwith.md) enable fully dynamic `SELECT` statements, where all clauses except the `INTO` clause and the ABAP-specific additions can be specified in one dynamic token.

- If [write accesses](abenabap_sql_writing.md) are performed on the data sources read by a `SELECT` loop within the loop, the behavior is database-dependent and undefined. Such accesses should therefore be avoided.

- The statement `ENDSELECT` closes all the [reader streams](abenselect_into_lob_handles.md) linked to the `SELECT` loop.

- The current [isolation level](abendb_isolation.md) determines whether a `SELECT` statement accesses only data released by a [database commit](abendb_commit.md) or whether it also accesses unreleased data in a different [database LUW](../../abap-glossary/abendatabase_luw_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows two `SELECT` statements that differ only in the arrangement of their [`SELECT`](abapselect_clause.md) and [`FROM`](abapfrom_clause.md) clauses. The result of both statements, which access two DDIC database tables via an [`INNER JOIN`](abapselect_join.md), is identical.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA cityfrom TYPE spfli-cityfrom VALUE 'NEW YORK'. 
 
SELECT c~carrname, p~connid, p~cityfrom, p~cityto 
       FROM scarr AS c 
            INNER JOIN spfli AS p 
                  ON c~carrid = p~carrid 
       WHERE p~cityfrom = @cityfrom 
       ORDER BY c~carrname, p~connid, p~cityfrom, p~cityto 
       INTO TABLE @FINAL(result1) 
       UP TO 10 ROWS. 
 
SELECT FROM scarr AS c 
            INNER JOIN spfli AS p 
                  ON c~carrid = p~carrid 
       FIELDS c~carrname, p~connid, p~cityfrom, p~cityto 
       WHERE p~cityfrom = @cityfrom 
       ORDER BY c~carrname, p~connid, p~cityfrom, p~cityto 
       INTO TABLE @FINAL(result2) 
       UP TO 10 ROWS. 
 
ASSERT result2 = result1. 
out->write( result1 ). 
 
out->display( ).
```
