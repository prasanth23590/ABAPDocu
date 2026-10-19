---
title: "READ TABLE itab"
source_file: abapread_table.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ TABLE itab

## Syntax

``` abap
READ TABLE itab result { table_key 
                       | free_key 
                       | where_cond 
                       | index }.  
```

[`result`](abapread_table_outdesc.md) · [`table_key`](abapread_table_key.md) · [`free_key`](abapread_table_free.md) · [`where_cond`](abapread_table_where.md) · [`index`](abapread_table_index.md)

## Description

This statement reads a line from the internal table `itab`. `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The output behavior [`result`](abapread_table_outdesc.md) determines how and to where the line content is read.

The line must be specified by specifying values for either

- [`table_key`](abapread_table_key.md) for a table key

- [`free_key`](abapread_table_free.md) for a free search key

- [`where_cond`](abapread_table_where.md) for an arbitrary condition

- [`index`](abapread_table_index.md) for a table index. This is possible only for [index tables](../../abap-glossary/abenindex_table_glosry.md) and when using a [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary key](../../abap-glossary/abensecondary_table_key_glosry.md).

If the line to be read is not specified uniquely, the first suitable line is read. In index tables, this line has the lowest line number of all suitable lines with respect to the table index used.

If the internal table is specified as the return value or result of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md), a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md), or a [table expression](../../abap-glossary/abentable_expression_glosry.md), the value only exists when the statement is executed. Afterwards, it is no longer possible to access the internal table.

## System Fields

The statement `READ TABLE` sets the values for the system fields `sy-subrc` and `sy-tabix`.

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | Line is found. `sy-tabix` is set to the line number of the entry in the primary or secondary table index used. If a [hash key](../../abap-glossary/abenhash_key_glosry.md) is used, it is set to 0.                                                                                                                                                                                                                                                                                                                                                                 |
| 2              | Like `sy-subrc` equals 0. Distinguishes cases that use the addition `COMPARING` in `result`.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 4              | Line was not found. If the entry was found using a binary search, `sy-tabix` is set to the line number of the entry in the primary or secondary table index in front of which it would be inserted using `INSERT ... INDEX ...`, to preserve the sort order. A binary search takes place when a [sorted key](../../abap-glossary/abensorted_key_glosry.md) is used by specifying it with additions [`table_key`](abapread_table_key.md) or [`free_key`](abapread_table_free.md) or if the addition `BINARY SEARCH` is used. Otherwise, `sy-tabix` is undefined. |
| 8              | Line was not found. The entry was searched using a binary search and the end of the table was reached. `sy-tabix` is set to the number of table lines + 1.                                                                                                                                                                                                                                                                                                                                                                                        |

## Hints

- There is no implicit selection of a suitable key or index. The used table key or table index is always specified uniquely. A syntax check warning occurs if there is a suitable [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) available but not used. This warning should be removed by using the key. However, in exceptional cases, it can also be bypassed using a [pragma](../../abap-glossary/abenpragma_glosry.md).

- As an alternative to the statement `READ TABLE`, [table expressions](abentable_expressions.md) can be used to allow reads to be performed on individual table lines at operand positions.

- Internal tables can also be specified as a [data source](../abap-database-access/abapselect_itab.md) of a [query](../../abap-glossary/abenasql_query_glosry.md) in ABAP SQL.

- If multiple lines of an internal table are to be read, the statement [`LOOP`](abaploop_at_itab.md) generally has better performance than using the statement `READ TABLE` in a loop.

- A value of 8 in `sy-subrc` means generally the same as 4 but shows that `sy-tabix` is set differently.

- When a [`WHERE` condition](abapread_table_where.md) is used, `sy-subrc` can have the values 0 and 4 only and `sy-tabix` is set to a defined value only if a line is found.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of individual table lines from a standard table in a `WHILE` loop. The table lines are read in reverse order with respect to the sorted secondary key `sort_key`. A `CHECK` statement exits the loop if the specified condition is not met. This construct demonstrates how an internal table could be processed in reverse order, before the addition [`STEP`](abaploop_at_itab_cond.md) was introduced for the [`LOOP`](abaploop_at_itab.md) statement. See also the corresponding [executable example](../abap-program-flow-logic/abeninverse_itab_for_abexa.md) with a `FOR` expression.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE STANDARD TABLE OF i 
          WITH EMPTY KEY 
          WITH NON-UNIQUE SORTED KEY sort_key COMPONENTS table_line. 
 
itab = VALUE #( ( 2 ) ( 5 ) ( 1 ) ( 3 ) ( 4 ) ). 
 
DATA(output) = ``. 
DATA(idx) = lines( itab ). 
WHILE idx > 0. 
  READ TABLE itab INDEX idx USING KEY sort_key 
             ASSIGNING FIELD-SYMBOL(<fs>). 
  idx -= 1. 
  CHECK <fs> > 2. 
  output = output && <fs> && ` `. 
ENDWHILE. 
out->write( output ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Demonstration of a case where `sy-subrc` is set to 8 because a binary search on a sorted key reached the end of the table.

``` abap
DATA itab TYPE STANDARD TABLE OF i 
               WITH EMPTY KEY 
               WITH UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
itab = VALUE #( FOR i = 9 THEN i - 2 UNTIL i < 0 ( i ) ). 
 
 
READ TABLE itab WITH KEY table_line = 10 
                         TRANSPORTING NO FIELDS ##PRIMKEY[SKEY]. 
                         "sy-subrc = 4, sy-tabix = 0 
 
READ TABLE itab WITH KEY skey COMPONENTS table_line = 10 
                         TRANSPORTING NO FIELDS. 
                         "sy-subrc = 8, sy-tabix = 6
```
