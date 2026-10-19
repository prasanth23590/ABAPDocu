---
title: "DELETE itab, itab_lines"
source_file: abapdelete_itab_lines.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > DELETE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE itab, itab_lines

## Syntax

``` abap
... itab [USING KEY keyname] [FROM idx1] [TO idx2] 
                             [STEP n]|[WHERE log_exp|(cond_syntax)] ...  
```

[`keyname`](abenkeyname.md) · [`log_exp`](../abap-program-flow-logic/abenlogexp.md)

### Addition

[1. `... USING KEY keyname`](abapdelete_itab_lines.md#addition-1)

[2. `... [FROM idx1] [TO idx2]`](abapdelete_itab_lines.md#addition-2)

[3. `... STEP n`](abapdelete_itab_lines.md#addition-3)

## Overview

### Description

To delete multiple lines, at least one of the additions `FROM`, `TO`, `STEP`, or `WHERE` must be specified. USING KEY [`keyname`](abenkeyname.md) is used to determine the table key to which the additions refer.

If multiple additions are specified, the lines that result from the intersection of the individual additions are deleted.

## Addition 1

`... USING KEY keyname`

### Description

The addition `USING KEY` can be used to specify a table key in [`keyname`](abenkeyname.md) with which the processing is executed. The specified table key affects the order in which the table lines are accessed, and the evaluation of the remaining conditions.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified, the processing behaves in the same way as if no key were explicitly specified. If a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) is specified, the order in which the lines are accessed is as follows:

- **Specification of a [sorted key](../../abap-glossary/abensorted_key_glosry.md)**

  The lines are processed by ascending line number in the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md)

- **Specification of a [hash key](../../abap-glossary/abenhash_key_glosry.md)**

  The lines are processed in the order in which they were inserted into the table.

### Hints

- Unlike the processing of a hashed table when a primary key is used, a preceding sort using the statement `SORT` has no affect on the processing order when a secondary hash key is specified.

- If a secondary table key is specified, any `WHERE` condition also specified must be [optimizable](abenitab_where_optimization.md). Otherwise a syntax error occurs, or an exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `DELETE` deletes the first three lines of the internal table `itab` because they occur from line 4 in the secondary table index of the secondary key `skey`.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY 
          WITH UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
itab = VALUE #( ( 6 ) ( 5 ) ( 4 ) ( 3 ) ( 2 ) ( 1 ) ). 
 
DELETE itab USING KEY skey FROM 4.
```

## Addition 2

`... [FROM idx1] [TO idx2]`

### Description

These optional additions have the effect that only table rows from row number `idx1` or up to and including row number `idx2` are respected in the table index used. The table index used is either the primary index or a secondary sorted index specified by `USING KEY`.

If only `FROM` is specified, all lines of the table from line number `idx1` up to and including the last line are respected. If only `TO` is specified, all lines in the table from the first line up to line number `idx2` are respected.

- If the addition `USING KEY` is not used, or the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified in `keyname`, the additions `FROM` and `TO` can only be used for [index tables](../../abap-glossary/abenindex_table_glosry.md) and refer to the line numbers of the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md).

- If a [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary key](../../abap-glossary/abensecondary_table_key_glosry.md) is specified in `keyname` after `USING KEY`, the additions `FROM` and `TO` can be used for all table categories and refer to the line numbers of the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md).

`idx1` and `idx2` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`.

The following restrictions apply:

- If the value of `idx1` is less than or equal to 0, a runtime error occurs. If the value of `idx1` is greater than the total number of table lines, no processing takes place.

- If the value of `idx2` is less than or equal to 0, a runtime error occurs. If the value of `idx2` is greater than the number of table lines, it is set to the number of table lines.

- If the value of `idx2` is less than the value of `idx1`, no processing takes place.

The additions `FROM` and `TO` can be specified together with `STEP` and then special rules apply.

### Hint

The statement `DELETE FROM itab` has the statement [`DELETE FROM dbtab`](../abap-database-access/abapdelete_dbtab.md) with identical syntax. If an internal table has the same name as a database table, a statement like this accesses the internal table.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of all lines in an internal table from line 4. The result is the same as in the example for [`APPEND ...`](abapappend.md), [`SORTED BY`](abapappend.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: carrid TYPE sflight-carrid VALUE 'LH', 
      connid TYPE sflight-connid VALUE '0400'. 
cl_demo_input=>new( 
  )->add_field( CHANGING field = carrid 
  )->add_field( CHANGING field = connid )->request( ). 
 
DATA: BEGIN OF seats, 
        fldate    TYPE sflight-fldate, 
        seatsocc  TYPE sflight-seatsocc, 
        seatsmax  TYPE sflight-seatsmax, 
        seatsfree TYPE sflight-seatsocc, 
      END OF seats. 
 
DATA seats_tab LIKE STANDARD TABLE OF seats. 
 
SELECT fldate, seatsocc, seatsmax, seatsmax - seatsocc AS seatsfree 
       FROM sflight 
       WHERE carrid = @carrid AND 
             connid = @connid 
       INTO TABLE @seats_tab. 
 
SORT seats_tab BY seatsfree DESCENDING. 
DELETE seats_tab FROM 4. 
 
out->write( seats_tab ). 
 
out->display( ).
```

## Addition 3

`... STEP n`

### Description

The optional addition `STEP n` defines the step size for processing an internal table. The step size is defined by the value of `n` which must be positive. `n` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`. If the addition `STEP` is not specified, the step size is 1.

The step size can be combined with the additions `FROM` and `TO` and then works on the subset of table lines defined by these conditions. If `FROM idx1` and `TO idx2` are combined with `STEP`, `idx1` needs to be less than or equal to `idx2`.

Depending on the value of `n`, every nth line is processed. The value of `n` must not be 0. For more details, see [`LOOP AT itab, cond`](abaploop_at_itab_cond.md).

### Hints

- `STEP n` cannot be used in combination with `WHERE`.

- In contrast to the [`STEP`](abaploop_at_itab_cond.md) addition for `LOOP AT`, the processing order cannot be changed by negative values of `n` here. The processing order is only defined by the table category or the addition `USING KEY`.

- `STEP n` can, however, be positioned otherwise. Its use after `FROM idx1` and `TO idx2` is recommended.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows that every second table line between line 1 and 8 is deleted from the internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       ORDER BY carrid 
       INTO TABLE @DATA(itab). 
 
DELETE itab FROM 1 TO 8 STEP 2. 
 
out->write( itab ). 
 
out->display( ).
```
