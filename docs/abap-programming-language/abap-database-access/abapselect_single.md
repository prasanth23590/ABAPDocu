---
title: "SELECT, SINGLE"
source_file: abapselect_single.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, SINGLE

## Syntax

``` abap
... SINGLE ... [FOR UPDATE] ...  

... SINGLE ... [FOR UPDATE NOWAIT].  
```

### Addition

[`[... FOR UPDATE ... | ... FOR UPDATE NOWAIT.]`](abapselect_single.md#addition)

## Overview

### Description

Using the ABAP-specific addition `SINGLE`, the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) contains a single row set. The addition is possible with a standalone [`SELECT`](abapselect.md) statement or with the [main query](../../abap-glossary/abenmainquery_glosry.md) of a standalone [`WITH`](abapwith.md) statement. If `SINGLE` is specified, a `SELECT` statement does not open a loop that must be closed using [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md) when reading into a non-table-like [target area](abapinto_clause.md). No internal tables can be specified as a [target area](abapinto_clause.md).

- If the selection of the `SELECT` statement covers exactly one row, this row is included in the result set.

- If the selection of the `SELECT` statement covers more than one row, one of these rows is included in the result set.

The following restrictions apply:

- The additions [`FOR ALL ENTRIES`](abenwhere_all_entries.md), [`ORDER BY`](abaporderby_clause.md), [`UP TO`](abapselect_up_to_offset.md), and [`OFFSET`](abapselect_up_to_offset.md) cannot be used together with `SINGLE`.

- The addition `SINGLE` cannot be used in the [main query](../../abap-glossary/abenmainquery_glosry.md) of the statement `OPEN CURSOR` or in [subqueries](../../abap-glossary/abensubquery_glosry.md).

### Hints

- A `SELECT` statement with the addition `SINGLE` is generally faster for completely specified rows than for incompletely specified rows.

- The result set of `SELECT` statements with the addition `SINGLE` matches the set from the addition [`UP TO 1 ROWS`](abapselect_up_to_offset.md) without using the addition [`ORDER BY`](abaporderby_clause.md). The difference between the statements is:

  - If the addition `SINGLE` is used, ABAP SQL handles the result set as a single row. The target area is a structure or a list of elementary fields, but the statement [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md) is not necessary. The row cannot be read into an internal table. Not all additions of the `SELECT` statement, however, can be used.

  - If the addition [`UP TO 1 ROWS`](abapselect_up_to_offset.md) is used, ABAP SQL handles the result set as tabular. The statement [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md) must be specified or the row must be read into an internal table. The addition [`ORDER BY`](abaporderby_clause.md) can, however, be specified.

    A `SELECT` statement with the addition `SINGLE` is optimized for reading a single row. This means that a `SELECT` statement with the addition `SINGLE` is generally slightly faster than with the addition [`UP TO 1 ROWS`](abapselect_up_to_offset.md), since no loop has to be opened. In practice, however, this difference can usually be ignored. The following is recommended:

  - Use of the addition `SINGLE` to read exactly one completely specified row.

  - Use of the addition [`UP TO 1 ROWS`](abapselect_up_to_offset.md) to read a maximum of one row from a set of selected rows.

- The addition [`ORDER BY`](abaporderby_clause.md) cannot be specified together with `SINGLE`, which means that it is not possible to define which row is read from a non-unique selection. Instead, the addition [`UP TO 1 ROWS`](abapselect_up_to_offset.md) can be specified with the addition [`ORDER BY`](abaporderby_clause.md) to define which row is read from a non-unique selection.

- If `SINGLE` is specified and [LOB handles](abenselect_into_lob_handles.md) are created in the [`INTO` clause](abapinto_clause.md), all primary key fields joined by `AND` in logical expressions must be checked for equality in the [`WHERE` condition](abapwhere.md). If this is not possible, the addition [`UP TO 1 ROWS`](abapselect_up_to_offset.md) can be used instead of `SINGLE`.

- If the addition `SINGLE` is used and [LOB handles](abenselect_into_lob_handles.md) are created, all [reader streams](abenselect_into_lob_handles.md) that are created when the `SELECT` statement is executed as well as [locators](abenselect_into_lob_handles.md) continue to exist until they are closed, either explicitly with one of their methods, or implicitly at the end of the current database LUW. During this time, the associated database operation is not completed. It is recommended that all LOB handles are closed explicitly as soon as possible.

- The addition `SINGLE` is designed to pass exactly one row to a [flat structure](../../abap-glossary/abenflat_structure_glosry.md) as a work area without opening a loop that must be closed using [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md).

  - Usually, the row must be identified exactly, and it must be specified uniquely in the [`WHERE` condition](abapwhere.md). In a [data source](abapselect_data_source.md), this is usually done by specifying comparison values for the [primary key](../../abap-glossary/abenprimary_key_glosry.md).

  - If a row is not uniquely determined, the addition `SINGLE` can also be used to detect whether a corresponding row exists. In this case, the warning from the extended program check must be hidden using a [pragma](../../abap-glossary/abenpragma_glosry.md). To avoid unnecessary transports of data, a `SELECT` list can also be used that contains nothing but a single constant.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the row with the information about Lufthansa flight 0400 from the DDIC database table `SPFLI`.

``` abap
SELECT SINGLE * 
       FROM spfli 
       WHERE carrid = 'LH' AND 
             connid = '0400' 
       INTO @FINAL(wa).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_DEMO_SELECT_SINGLE_VS_UP_TO` compares the performance of `SELECT` statements with the addition `SINGLE` with equivalent statements with the addition [`UP TO 1 ROWS`](abapselect_up_to_offset.md).

## Addition

`[... FOR UPDATE ... | ... FOR UPDATE NOWAIT.]`

\*\* This syntax is not available in the current ABAP language version.\*\*
