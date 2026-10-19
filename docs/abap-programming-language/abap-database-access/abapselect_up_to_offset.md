---
title: "SELECT, UP TO, OFFSET"
source_file: abapselect_up_to_offset.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, UP TO, OFFSET

## Syntax

``` abap
... [UP TO n ROWS]   
    [OFFSET o] ...  
```

### Addition

[1.`... UP TO n ROWS`](abapselect_up_to_offset.md#addition-1)

[2.`... OFFSET o`](abapselect_up_to_offset.md#addition-2)

## Overview

### Description

These optional additions of a [query](../../abap-glossary/abenasql_query_glosry.md) of a [`SELECT`](abapselect.md) statement or [`WITH`](abapwith.md) statement restrict the result set using an offset and the maximum number of rows to be read. The syntax varies as follows for [main queries](../../abap-glossary/abenmainquery_glosry.md) and [subqueries](../../abap-glossary/abensubquery_glosry.md):

- **Main query**

  If the [`INTO` clause](abapinto_clause.md) is specified as last clause of the `SELECT` statement, the additions must be after the `INTO` clause. Otherwise, they can also be after the [`SELECT` clause](abapselect_list.md) or after the [`FROM` clause](abapfrom_clause.md). The order of the two additions is not fixed. The addition `OFFSET` can be used only if there is an [`ORDER BY`](abaporderby_clause.md) clause.

- **Subquery**

  The addition `UP TO` can only be specified after an [`ORDER BY`](abaporderby_clause.md) clause and the addition `OFFSET` can only be specified after `UP TO`.

### Hint

These additions affect the result set defined by the preceding clauses.

## Addition 1

`... UP TO n ROWS`

### Description

The addition `UP TO` limits the number of rows in the result set of a `SELECT` statement to `n`. For `n`, a [host variable](abenabap_sql_host_variables.md), a [host expression](abenabap_sql_host_expressions.md), or a [literal](abenabap_sql_literals.md) of type `i` is expected, which can represent all non-negative numbers from the value range of `i` except its maximum value +2,147,483,647. Only the types `b`, `s`, `i`, or `int8` can be specified for `n`. Furthermore, a literal or constant specified for `n` cannot have the value 0. If `n` is an untyped literal or a host variable, its content must match the data type `i` in accordance with the rules for a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md).

- If `n` contains the value 0, a maximum of 2,147,483,647 rows are placed in the result set.

- A positive number in `n` indicates the maximum number of rows in the result set.

- If `n` contains a negative number or +2,147,483,647, a syntax error is produced, or an uncatchable exception is raised.

The addition `UP TO` cannot be used with addition [`SINGLE`](abapselect_single.md) and cannot be used with [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md).

### Hints

- The addition `UP TO n ROWS` is preferable to a `SELECT` loop that is terminated after importing `n` rows. In the latter case, the last [package](abenabap_sql_oview.md) passed from the database to the AS ABAP usually contains superfluous rows.

- Without the addition [`ORDER BY`](abaporderby_clause.md), the addition `UP TO 1 ROWS` provides the same result as the addition [`SINGLE`](abapselect_single.md) and there are no major differences in performance.

  - If `SINGLE` is used, data can be read into a non-table-like work area without opening a loop closed using [`ENDSELECT`](abapendselect.md).

  - If `UP TO 1 ROWS` is used, the addition [`ORDER BY`](abaporderby_clause.md) can be specified to determine the first row in a multirow set of hits.

    It is advisable to use the addition `UP TO 1 ROWS` to read at most one row from a set of selected rows. The addition [`SINGLE`](abapselect_single.md), on the other hand, should generally be used to read a completely specified row.

- If the addition [`ORDER BY`](abaporderby_clause.md) is also specified, the rows of the hit list are sorted on the database server and only the number of sorted rows specified in `n` are passed to the result set. If the addition `ORDER BY` is not specified, `n` arbitrary rows that meet the [`WHERE`](abapwhere.md) condition are passed to the result set. If the `ORDER BY` clause does not sort the result set uniquely, it is not possible to define which rows are in the result set.

- If the addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md) is also specified, all selected rows are initially read into an internal table and the addition `UP TO n ROWS` only takes effect during the passing from the system table to the actual target area. This can produce unexpected memory bottlenecks.

- The addition `UP TO 1 ROWS` is often used to determine whether a [data source](abapselect_data_source.md) contains any rows that meet a certain condition. To avoid unnecessary transports of data, a `SELECT` list can also be used that contains nothing but a single constant.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the three business customers with the highest discount rates.

``` abap
SELECT * 
       FROM scustom 
       WHERE custtype = 'B' 
       ORDER BY discount DESCENDING 
       INTO TABLE @FINAL(result) 
       UP TO 3 ROWS.
```

## Addition 2

`... OFFSET o`

### Description

The addition `OFFSET` is used to return only the rows after the row with the count `o` from the result set. If `OFFSET` is specified, the result set must be sorted using [`ORDER BY`](abaporderby_clause.md). `o` expects a [host variable](abenabap_sql_host_variables.md), a [host expression](abenabap_sql_host_expressions.md), or a [literal](abenabap_sql_literals.md) of the type `b`, `s`, `i`, or `int8`, which can represent all non-negative numbers in the value range of `i` except its maximum value +2,147,483,647. A literal or constant specified for `n` cannot have the value 0.

- If `o` contains the value 0, all rows from the first row are respected.

- If `o` contains a positive number, only the rows after the row indicated by `o` are respected.

- If `o` contains a negative number or +2,147,483,647, a syntax error is produced, or an uncatchable exception is raised.

The addition `OFFSET` cannot be used together with the additions [`SINGLE`](abapselect_single.md) and [`FOR ALL ENTRIES`](abenwhere_all_entries.md), and not when [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md) is used.

### Hints

- It only makes sense to specify the addition `OFFSET` if the order of the rows in the result set is not undefined. Therefore, [`ORDER BY`](abaporderby_clause.md) must be specified as well, followed by appropriate columns.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the data of all flights of a connection, except for the ten flights with the fewest seats taken.

``` abap
SELECT fldate 
       FROM sflight 
       WHERE carrid = 'LH' AND connid = '400' 
       ORDER BY seatsocc ASCENDING, fldate 
       INTO TABLE @FINAL(result) 
       OFFSET 10.
```

### Executable Example

[Restricting the result set](abenselect_up_to_offset_abexa.md)
