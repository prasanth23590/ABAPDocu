---
title: "LOOP AT itab, GROUP BY"
source_file: abaploop_at_itab_group_by.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT itab, GROUP BY

## Syntax

``` abap
LOOP AT itab result [cond] GROUP BY group_key 
                           [ASCENDING|DESCENDING [AS TEXT]] 
                           [WITHOUT MEMBERS] 
                           [group_result]. 
  ... 
  [LOOP AT GROUP ... 
    ... 
  ENDLOOP.] 
  ... 
ENDLOOP.  
```

[`result`](abaploop_at_itab_result.md) · [`cond`](abaploop_at_itab_cond.md) · [`group_key`](abaploop_at_itab_group_by_key.md) · [`group_result`](abaploop_at_itab_group_by_binding.md) · [`[LOOP AT GROUP ...`](abaploop_at_group.html) · [`...`](abaploop_at_group.html) · [`ENDLOOP.]`](abaploop_at_group.md)

### Addition

[1. `... ASCENDING|DESCENDING [AS TEXT]`](abaploop_at_itab_group_by.md#addition-1)

[2. `... WITHOUT MEMBERS`](abaploop_at_itab_group_by.md#addition-2)

## Overview

### Description

This variant of the statement [`LOOP AT itab`](abaploop_at_itab_variants.md) groups the lines of the internal table and executes a loop across the groups. The same applies to the syntax of the additions [`result`](abaploop_at_itab_result.md) and [`cond`](abaploop_at_itab_cond.md) as to a [loop across lines](abaploop_at_itab.md) with the exception that the addition [`TRANSPORTING NO FIELDS`](abaploop_at_itab_result.md) cannot be specified.

If the addition `GROUP BY` is specified, the `LOOP` is processed in two phases:

- **Grouping**

  In the first phase, all lines determined by the conditions [`cond`](abaploop_at_itab_cond.md) are read in the processing order described in a [loop across lines](abaploop_at_itab.md). The statements in the statement block between `LOOP` and `ENDLOOP` are not executed during this process. For each line read, a group key is constructed in the group key expression [`group_key`](abaploop_at_itab_group_by_key.md) instead. Each group key represents a group. Each line is assigned to exactly one group as a member, namely the group of all lines with the same group key. If the addition `WITHOUT MEMBERS` is not used, this assignment is internal and can be used for access to the members of a group in the second phase.

- **Group Loop**

  In the second phase, a loop is executed across all groups. The statements in the statement block between `LOOP` and `ENDLOOP` are executed for each loop pass. The output behavior for the group loop is defined in [`group_result`](abaploop_at_itab_group_by_binding.md) and the corresponding values can be accessed in the loop. If the assignment of the table lines to their groups is defined, a member loop [`LOOP AT GROUP`](abaploop_at_group.md) can be nested in the `LOOP` to read the lines in each group.

The default order of the groups in the group loop as well as the order of the members within a group is defined by the processing order of the `LOOP` in the first phase:

- The default order of the groups depends on the time their group key is first created, which itself can be overridden by an explicit sorting using the additions `ASCENDING` or `DESCENDING`.

- If the assignment of the lines to their group is defined, the order of the lines of a group is based on the time they are assigned to the group. This defines, in particular, the first line of each group that is used as a representative in the [representative binding](abaploop_at_itab_group_by_binding.md).

The internal table `itab` cannot be modified in the group loop unless the addition `WITHOUT MEMBERS` is specified.

### System Fields

This variant of the statement `LOOP AT` with the addition `GROUP BY` sets the values of the system field `sy-tabix` in the group loop as follows:

- If a representative binding is defined in the [output behavior](abaploop_at_itab_group_by_binding.md), `sy-tabix` is set to the value that would be set for the line representing the group in the `LOOP` without grouping.

- If a group key binding is defined in the [output behavior](abaploop_at_itab_group_by_binding.md), the groups are counted in `sy-tabix`. The first loop pass sets `sy-tabix` to 1 and each subsequent loop pass raises it by 1.

After leaving the loop using `ENDLOOP`, `sy-tabix` is set to the value that it had before entering the loop. The same applies to `sy-subrc` as in a [loop across lines](abaploop_at_itab.md).

### Hints

- A grouping, that is, the assignment of lines to a group, only exists within the group loop and a group can only be addressed after [`LOOP AT GROUP`](abaploop_at_group.md) or [`FOR ... IN GROUP`](abenfor_in_group.md).

- A member loop [`LOOP AT GROUP`](abaploop_at_group.md) is only possible in `LOOP` statements for which the internal table `itab` is specified directly as a data object and not as the result of a call or expression. If the table is specified as the result of a call or expression, only the group keys exist in the group loop and no longer the groups themselves.

- A `LOOP` with the addition `GROUP BY` is not possible for [mesh paths](../../abap-glossary/abenmesh_path_glosry.md).

- No [group level processing](../../abap-glossary/abengroup_level_processing_glosry.md) with the statement [`AT`](abapat_itab.md) is possible in a `LOOP` with the addition `GROUP BY`.

- Internal tables can also be grouped using the expression [`FOR GROUPS ... OF`](abenfor_groups_of.md).

- Unlike in [group level processing](../../abap-glossary/abengroup_level_processing_glosry.md), a grouping with `GROUP BY` does not depend on the structure of the lines and the processing order of the loop. A grouping with `GROUP BY` can usually replace group level processing in cases where the internal table is sorted before the loop by the group key.

- Groupings using `GROUP BY` replace self-programmed group loops.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows the simplest form of grouping by a column without explicitly specifying the output behavior of the group loop. Within the loop, there is access to the work area `wa`, in particular to the component `wa-carrid` that is used for grouping. The work area `wa` contains the first line of each group and represents the group in the loop. This is called a representative binding.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
LOOP AT spfli_tab INTO FINAL(wa) 
                  GROUP BY wa-carrid. 
  out->write( wa-carrid ). 
ENDLOOP. 
 
out->display( ).
```

### Executable Example

[Grouping Internal Tables](abenloop_group_by_abexas.md)

## Addition 1

`... ASCENDING|DESCENDING [AS TEXT]`

### Description

These additions sort the groups by the group key in ascending or descending order before the group loop is executed. The groups are sorted in exactly the same way as when the statement [`SORT`](abapsort_itab.md) is used on an internal table whose primary table key is the group key and the addition `AS TEXT` is applied accordingly.

The group loop is executed in the sort order. If the additions `ASCENDING` and `DESCENDING` are not specified, the groups are in the order in which the value of a group key was constructed for the first time.

### Hint

Groups can be sorted as an addition to the statement [`SORT`](abapsort_itab.md) if the criteria here are not sufficient.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the example above, but with sorting by group key in descending order.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
LOOP AT spfli_tab INTO FINAL(wa) 
                  GROUP BY wa-carrid DESCENDING. 
  out->write( wa-carrid ). 
ENDLOOP. 
 
out->display( ).
```

### Executable Example

[Grouping with `LOOP` and Sort](abenloop_group_by_sort_abexa.md)

## Addition 2

`... WITHOUT MEMBERS`

### Description

The addition `WITHOUT MEMBERS` deactivates the default internal variant of the assignment of each table line to its group. This addition constructs groups, but there is no access to the lines of the groups in the group loop. If the addition `WITHOUT MEMBERS` is specified, the following applies:

- The [output behavior](abaploop_at_itab_group_by_binding.md) cannot be defined for a line of the group as a representative and a group key binding must be defined.

- The group loop cannot contain a nested member loop [`LOOP AT GROUP`](abaploop_at_group.md).

- The internal table `itab` can be modified in the group loop.

### Hint

The addition `WITHOUT MEMBERS` is used to improve performance in all cases where the content of the groups is not required.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the example above, but with the addition `WITHOUT MEMBERS`, for which a group key binding is defined with `INTO DATA(key)`. There is no access to the lines of the groups in the loop.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
LOOP AT spfli_tab INTO FINAL(wa) 
                  GROUP BY wa-carrid WITHOUT MEMBERS 
                  INTO FINAL(key). 
  out->write( key ). 
ENDLOOP. 
 
out->display( ).
```
