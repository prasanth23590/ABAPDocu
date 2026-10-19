---
title: "LOOP AT itab, cond"
source_file: abaploop_at_itab_cond.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, Basic Form"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT itab, cond

## Syntax

``` abap
 ... [USING KEY keyname] 
    [FROM idx1] [TO idx2] [STEP n] 
    [WHERE log_exp|(cond_syntax)] ...  
```

[`keyname`](abenkeyname.md) · [`log_exp`](../abap-program-flow-logic/abenlogexp.md)

### Addition

[1. `... USING KEY keyname`](abaploop_at_itab_cond.md#addition-1)

[2. `... [FROM idx1] [TO idx2]`](abaploop_at_itab_cond.md#addition-2)

[3. `... STEP n`](abaploop_at_itab_cond.md#addition-3)

## Overview

### Description

These optional additions to [`LOOP AT itab`](abaploop_at_itab.md) specify a subset of lines to be processed and the order in which the loop is executed.

- The subset of lines can be defined with:

  - `FROM` and `TO` that define an interval of line numbers for index tables

  - `WHERE` that selects lines that fulfill a condition specified in a logical expression

  - `STEP` that allows lines to be skipped by defining a step size greater than 1.

- The processing order can be defined with:

  - USING KEY [`keyname`](abenkeyname.md) that defines the table key that is used for the loop and thus overrides the standard order determined by the table category.

  - `STEP` that can define a reverse order by specifying a negative step size.

If none of the conditions are specified, all table lines are read in the standard order that is defined by the table category as described under [`LOOP AT itab`](abaploop_at_itab.md).

## Addition 1

`... USING KEY keyname`

### Description

The optional addition `USING KEY` specifies a table key [`keyname`](abenkeyname.md) with which the processing is executed. The specified table key affects the order in which the table lines are accessed, and the evaluation of the other conditions.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified using its name `primary_key`, the processing behaves in the same way as if no key were explicitly specified. If a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) is specified, the order in which the lines are accessed is as follows.

- **[Specification of a sorted key](../../abap-glossary/abensorted_key_glosry.md)**

  The lines are processed by ascending line number in the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) In each loop pass, the system field `sy-tabix` contains the line number of the current line in the associated secondary table index.

- **[Specification of a hash key](../../abap-glossary/abenhash_key_glosry.md)**

  The lines are processed in the order in which they were inserted into the table. In each loop pass, the system field `sy-tabix` contains the value 0. A preceding sort using the statement [`SORT`](abapsort_itab.md) does not change this processing order.

The order defined by `USING KEY` can be reversed by using the addition `STEP` with a negative step size.

Within the loop, the key used can be addressed using the predefined name `loop_key`. This is possible in all statements where the table key [`keyname`](abenkeyname.md) to be used can be specified explicitly. This type of statement must then be listed in the loop itself. Including the statement in a procedure that is called in the loop is not sufficient.

### Hints

- The fact that the processing order defined by a secondary hash key is not affected by a preceding sort using the statement `SORT` is a different behavior than for the processing order defined by the primary key of a hashed table that is affected by a preceding sort.

- If a secondary table key is specified, a simultaneously specified `WHERE` condition also must be [optimizable](abenitab_where_optimization.md), otherwise a syntax error occurs or an exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the difference between loops across a standard table of random numbers with and without a sorted secondary table key specification. The first loop returns the lines in the order in which they were appended. The second loop returns the lines sorted in ascending order.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = CONV i( t ) 
                                         min  = 1 
                                         max  = 100 ). 
 
DATA itab TYPE STANDARD TABLE OF i WITH EMPTY KEY 
          WITH NON-UNIQUE SORTED KEY key COMPONENTS table_line. 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( rnd->get_next( ) ) ). 
 
DATA output1 TYPE TABLE OF i WITH EMPTY KEY. 
LOOP AT itab INTO FINAL(number1). 
  output1 = VALUE #( BASE output1 ( number1 ) ). 
ENDLOOP. 
out->write( output1 ). 
 
DATA output2 TYPE TABLE OF i WITH EMPTY KEY. 
LOOP AT itab INTO FINAL(number2) USING KEY key. 
  output2 = VALUE #( BASE output2 ( number2 ) ). 
ENDLOOP. 
out->write( output2 ). 
 
out->display( ).
```

### Executable Example

[Loop Across Internal Table with Key Specified](abenloop_at_itab_key_abexa.md)

## Addition 2

`... [FROM idx1] [TO idx2]`

### Description

These optional additions have the effect that only table rows from row number `idx1` or up to and including row number `idx2` are respected in the table index used. The table index used is either the primary index or a secondary sorted index specified by `USING KEY`.

If only `FROM` is specified, all lines of the table from line number `idx1` up to and including the last line are respected. If only `TO` is specified, all lines in the table from the first line up to line number `idx2` are respected.

- If the addition `USING KEY` is not used, or the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified in `keyname`, the additions `FROM` and `TO` can only be used for [index tables](../../abap-glossary/abenindex_table_glosry.md) and refer to the line numbers of the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md).

- If a [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary key](../../abap-glossary/abensecondary_table_key_glosry.md) is specified in `keyname` after `USING KEY`, the additions `FROM` and `TO` can be used for all table categories and refer to the line numbers of the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md).

`idx1` and `idx2` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`.

The following restrictions apply:

- If the value of `idx1` is less than or equal to 0, it is set to 1 in the statement `LOOP`. If the value of `idx1` is greater than the total number of table lines, no processing takes place.

- If the value of `idx2` is less than or equal to 0, the statement `LOOP` is not executed. If the value of `idx2` is greater than the number of table lines, it is set to the number of table lines.

- If the value of `idx2` is less than the value of `idx1`, no processing takes place.

The value of `idx1` is evaluated once when the loop is entered. Any changes to `idx1` during loop processing are ignored. In contrast, the value of `idx2` is evaluated in each loop pass and any changes made to `idx2` during loop processing are respected.

The additions `FROM` and `TO` can be specified together with `STEP` and then special rules apply.

### Hint

To determine when loop processing is exited and whether the value specified in `idx2` has been reached, the current line number is evaluated. Note that this number can be changed if lines are inserted or deleted during a loop pass as described in [`LOOP`](abaploop_at_itab.md). When lines are inserted, the loop may be processed less often and when lines are deleted, it may be processed more often than specified by the difference between `idx2` and `idx1`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the primary index of a particular table line using the built-in function [`line_index`](abenline_index_function.md) and a loop across the internal table from this line.

``` abap
DATA itab TYPE SORTED TABLE OF scarr 
               WITH UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @itab. 
 
FINAL(idx) = line_index( itab[ carrid = 'LH' ] ). 
IF idx = 0. 
  RETURN. 
ENDIF. 
 
LOOP AT itab FROM idx ASSIGNING FIELD-SYMBOL(<fs>). 
  ... 
ENDLOOP.
```

## Addition 3

`... STEP n`

### Description

The optional addition `STEP n` defines the step size and the direction of the loop. The step size is defined by the absolute value of `n` and the direction is defined by the positive or negative sign of `n`. `n` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`. If the addition `STEP` is not specified, the step size is 1 and the loop order is defined by the table category or the addition `USING KEY` only.

The addition step size can be combined with the additions `FROM`, `TO` and `WHERE` and then works on the subset of table lines defined by these conditions. For such combinations the following special rules apply:

- If `FROM idx1` or `TO idx2` are combined with `STEP`:

  - If the value of `n` is greater than 0, `idx1` needs to be less than or equal to `idx2`.

  - If the value of `n` is less than 0, `idx1` needs to be greater than or equal to `idx2`.

    If none of the above restrictions are met, the loop is interpreted as empty. All other settings for `FROM idx1` and `TO idx2` are described as for [`... [FROM idx1] [TO idx2]`](abaploop_at_itab_cond.md).

- If a `WHERE` condition is combined with `STEP`, the operand `n` can only have the value 1 or -1. Other values lead to a syntax error or the uncatchable runtime error `ITAB_ILLEGAL_STEP_SIZE`. The `WHERE` condition needs to be placed after `STEP n`.

The detailed effect of the addition `STEP` is as follows:

- **Step size**

  The absolute value of `n` specifies the step size of the loop over all table lines or the subset of table lines defined by the conditions `FROM`, `TO` and `WHERE`. Starting from the first line of the table or subset for a forwards order or from the last line of the subset for a backwards order,

  - if the absolute value of `n` is equal to 1, every line is read,

  - if the absolute value of `n` is equal to 2, every second line is read,

  - and so on.

    If the absolute value of `n` is greater than the lines available in the subset, only the first or last line of the subset are processed.

- **Loop order**

  The sign of `n` keeps or reverses the loop order as it is defined by the table category or the addition `USING KEY`:

  - If the value of `n` is greater than 0,the loop order is not changed. A forward loop is executed that starts with the first table line or the first line of the subset.

  - If the value of `n` is less than 0, the loop order is reversed. A backward loop is executed, that starts with the last table line or the last line of the subset.

    Specifying a reverse loop order changes the standard order as follows:

  - A reverse loop order without specifying a secondary key behind `USING KEY` reverses the loop order defined by the table category. For index tables, the primary table index is processed backwards starting with the highest index entry in descending order and the corresponding table lines are read. For hashed tables, the table lines are read backward in the reverse order in which they were inserted into the table or are sorted after a [`SORT`](abapsort_itab.md) statement.

  - A reverse loop order together with a secondary key specified behind `USING KEY` reverses the loop order defined by the secondary key. For a sorted secondary key, the corresponding secondary index is processed backwards starting with the highest index entry in descending order and the corresponding table lines are read. For a secondary hashed key, the table lines are read backward in the reverse order in which they were inserted into the table (a preceding sort using [`SORT`](abapsort_itab.md) has no effect here).

The value of `n` must not be 0. If the value 0 is known statically for `n`, a syntax error occurs. If the value 0 is known at runtime only, the program is aborted with the runtime error `ITAB_ILLEGAL_STEP_SIZE` which is not catchable. Changing the value of `n` inside the loop has no effect on the step size or loop order.

As usual, `sy-tabix` contains the line number of the current line read in a loop pass when using a table index or 0 when using a hashed key.

### Hints

- The addition `STEP` does not change the actual sort order of the table as defined by table category or for a secondary index. It changes the processing order of the current loop with respect to this sort order.

- The control structures for [group level processing](../../abap-glossary/abengroup_level_processing_glosry.md) [`AT FIRST`, `AT LAST`, `AT NEW`, and `AT END OF`](abapat_itab.md) are not supported with `STEP`.

- `STEP n` can, however, be positioned otherwise. Its use after `FROM idx1` and `TO idx2` is recommended.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows the use of `STEP n` as reverse loop in combination with `FROM idx1` and `TO idx2`. As result, line 3, line 2, and line 1 as defined by the primary table index are processed in the mentioned order.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM scarr 
       ORDER BY carrid 
       INTO TABLE @FINAL(itab). 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>) 
             FROM 3 TO 1 STEP -1. 
  out->write( <fs> ). 
ENDLOOP. 
 
out->display( ).
```

### Executable Example

[`LOOP` with Step Size](abenloop_at_itab_step_abexa.md)
