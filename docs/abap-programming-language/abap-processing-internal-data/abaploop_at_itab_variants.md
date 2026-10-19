---
title: "LOOP AT itab"
source_file: abaploop_at_itab_variants.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT itab

## Syntax Forms

**[Loop Across Table Lines](abaploop_at_itab.md)**

``` abap
1. LOOP AT itab result [cond]. 
    ... 
  ENDLOOP. 
```

**[Loop Across Line Groups](abaploop_at_itab_group_by.md)**

``` abap
2. LOOP AT itab result [cond] GROUP BY group_key 
                             [ASCENDING|DESCENDING [AS TEXT]] 
                             [WITHOUT MEMBERS] 
                             [group_result]. 
    ... 
  ENDLOOP.
```

[`result`](abaploop_at_itab_result.md) · [`cond`](abaploop_at_itab_cond.md) · [`result`](abaploop_at_itab_result.md) · [`cond`](abaploop_at_itab_cond.md) · [`group_key`](abaploop_at_itab_group_by_key.md) · [`group_result`](abaploop_at_itab_group_by_binding.md)

## Description

Executes a [table iteration](../../abap-glossary/abentable_iteration_glosry.md) as a [loop](../../abap-glossary/abenloop_glosry.md) across an internal table `itab`. `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

The statements `LOOP` and `ENDLOOP` define the statement block of the loop. The statement `LOOP` reads lines from the internal table `itab` sequentially that meet an optional condition [`cond`](abaploop_at_itab_cond.md).

- [If the addition `GROUP BY`](abaploop_at_itab.md) is not specified, the statement block is executed for each read line and the line can be processed here. The way in which the read line can be addressed in the statement block is specified in the output behavior [`result`](abaploop_at_itab_result.md).

- [The addition `GROUP BY`](abaploop_at_itab_group_by.md) is used to group the read lines by a group key [`group_key`](abaploop_at_itab_group_by_key.md) and the statement block is then executed for each group. The way in which the current group can be addressed in the statement block is specified in the output behavior [`group_result`](abaploop_at_itab_group_by_binding.md).

To exit processing of the loop, the following statements can be used:

- [`EXIT`](../abap-calling-and-exiting-program-units/abapexit_loop.md) that exits a complete loop and resumes the program behind the closing statement of the loop.

- A statement for [exiting the current processing block](../abap-calling-and-exiting-program-units/abenleave_processing_blocks.md)

In order to exit the current loop pass and to continue with the next loop pass, the statements [`CONTINUE`](../abap-calling-and-exiting-program-units/abapcontinue.md) and [`CHECK`](../abap-calling-and-exiting-program-units/abapcheck_processing_blocks.md) can be used.

**Caution**

[Special rules apply](abenitab_loop_change.md) when changing the internal table within a loop. In particular you should never perform write accesses on a complete table body.

## Hint

Internal tables can also be specified as a [data source](../abap-database-access/abapselect_itab.md) of a [query](../../abap-glossary/abenasql_query_glosry.md) in ABAP SQL.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Simple `LOOP` over an internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( i ) ). 
 
DATA(str) = ``. 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
  str = str && CONV string( <fs> ) && ` `. 
ENDLOOP. 
out->write( str ). 
 
out->display( ).
```
