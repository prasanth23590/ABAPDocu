---
title: "FOR ... IN GROUP"
source_file: abenfor_in_group.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR ... IN GROUP

## Syntax

``` abap
... FOR { wa|<fs> IN GROUP group [INDEX INTO idx] [WHERE ( log_exp )] } 
      | { GROUPS OF 
          wa|<fs> IN GROUP group [INDEX INTO idx] [WHERE ( log_exp )] 
          GROUP BY group_key 
          [ASCENDING|DESCENDING [AS TEXT]] 
          [WITHOUT MEMBERS] } [let_exp] ...  
```

[`WHERE ( log_exp )`](abenfor_cond.md) · [`WHERE ( log_exp )`](abenfor_cond.md) · [`group_key`](abaploop_at_itab_group_by_key.md) · [`let_exp`](../abap-declarations/abaplet.md)

### Addition

[`... INDEX INTO idx`](abenfor_in_group.md#addition)

## Overview

### Description

These variants of an [iteration expression](../../abap-glossary/abeniteration_expression_glosry.md) for [table iterations](../../abap-glossary/abentable_iteration_glosry.md) using [`FOR`](abenfor_itab.md) evaluate a line group `group` sequentially like a [member loop](../../abap-glossary/abenmember_loop_glosry.md) [`LOOP AT GROUP`](abaploop_at_group.md). These `FOR` expressions can only be specified in those places in which a group `group` can be accessed, that is:

- in a constructor expression after an expression [`FOR GROUPS ... OF`](abenfor_groups_of.md),

- in a `LOOP` with the addition [`GROUP BY`](abaploop_at_itab_group_by.md).

where in both cases

- the internal table must be specified directly and not specified as the result of an expression or a function,

- the addition `WITHOUT MEMBERS` must not be specified.

`group` is used to specify the group to be evaluated using the data object or field symbol to which the group is bound.

- In the variant `FOR ... IN GROUP` without `GROUPS OF`, the expression evaluates the members of the current group in the same way as the variant [`FOR ... IN itab`](abenfor_in_itab.md) evaluates the lines of the internal table `itab`. The result is the lines of the group.

- In the variant `FOR GROUPS OF ... IN GROUP`, the expression evaluates the members of the current group in the same way as the variant [`FOR GROUPS ... OF`](abenfor_groups_of.md). The current group is grouped again and the result is either representatives or group keys of the subgroups.

The condition [`WHERE ( log_exp )`](abenfor_cond.md) can be used to restrict the lines of the group to be evaluated. Conditions other than this static `WHERE` condition cannot be specified.

### Hint

As in [`LOOP AT GROUP`](abaploop_at_group.md), access to the groups is optimized internally.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of a list of the total occupied seats for each airline. A `LOOP` with the addition [`GROUP BY`](abaploop_at_itab_group_by.md) evaluates its groups in a table reduction using `FOR flight IN GROUP <carrier>`. Here, the total for each group is calculated for the column `seatsocc`.

``` abap
SELECT * FROM sflight INTO TABLE @FINAL(sflight). 
 
TYPES group_keys TYPE STANDARD TABLE OF spfli-carrid WITH EMPTY KEY. 
 
TYPES: 
  BEGIN OF list_line, 
    carrier  TYPE sflight-carrid, 
    bookings TYPE i, 
  END OF list_line, 
  list TYPE STANDARD TABLE OF list_line WITH EMPTY KEY. 
 
DATA(list) = VALUE list( ). 
LOOP AT sflight INTO FINAL(wa) 
     GROUP BY wa-carrid 
     ASCENDING 
     ASSIGNING FIELD-SYMBOL(<carrier>). 
 
  list = VALUE list( 
           BASE list 
           ( carrier = <carrier> 
             bookings = REDUCE #( 
                        INIT s = 0 
                        FOR flight IN GROUP <carrier> 
                        NEXT s += flight-seatsocc ) ) ). 
ENDLOOP. 
 
cl_demo_output=>display( list ).
```

## Addition

`... INDEX INTO idx`

### Description

For each read line of the associated `FOR` expression, this addition sets the helper variable `idx` to the value to which the system field `sy-tabix` would be set in a corresponding [`LOOP AT GROUP`](abaploop_at_group.md) loop. The same applies to the local data object `idx` as in the variant [`FOR ... IN itab`](abenfor_in_itab.md).
