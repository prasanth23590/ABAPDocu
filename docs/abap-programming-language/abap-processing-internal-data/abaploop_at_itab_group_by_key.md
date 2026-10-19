---
title: "LOOP AT itab, group_key"
source_file: abaploop_at_itab_group_by_key.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT itab, group_key

## Syntax

``` abap
 ... key | ( key1 = dobj1 key2 = dobj2 ... 
           [gs = GROUP SIZE] [gi = GROUP INDEX] ) ...  
```

### Addition

[1. `... gs = GROUP SIZE`](abaploop_at_itab_group_by_key.md#addition-1)

[2. `... gi = GROUP INDEX`](abaploop_at_itab_group_by_key.md#addition-2)

## Overview

### Description

Group key expression for constructing the group key in the [grouping](abaploop_at_itab_group_by.md) of internal tables. The group key is the result of the group key expression, whose data type can be defined as follows:

- If `key` is specified, the group key is a single data object with any data type.

- If `( key1 = dobj1 key2 = dobj2 ... )` is specified, the group key is a structure with the components `key1`, `key2`, ... The components can have any name and any data type. The structure type is defined here as a bound data type of the structure.

`key` or `key1`, `key2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md) in which the current line can be used in accordance with the output behavior defined in [`result`](abaploop_at_itab.md). The data types of `key` or `key1`, `key2`, ... must be known completely and statically.

For each line of the internal table `itab` read in the grouping phase, the value of the group key is calculated from the data objects, expressions, or calls specified here using the group key expression.

If a group key binding is defined in the output behavior [`group_result`](abaploop_at_itab_group_by_binding.md) of the group loop, the data object or field symbol specified here can be used to access the value of the group key of every group in the group loop.

### Hints

- The calculated value of the group key for each read line of `itab` must depend on the appropriate type of the read line to achieve a useful grouping. The following are some special cases:

  - If the group key is a value independent of the line, there is only one group to which all read lines belong.

  - If the group key is different for each line, there are as many groups as lines and each group contains only one line.

    The simplest solution is to directly assign the values of the lines to the group key or its components. However, since they are general expression positions on the right side, any type of evaluation is possible.

- The ability to directly construct any type of structure makes it easy to create multicomponent group keys without having to declare a matching structure first or to concatenate the key components into, for example, a string.

- The syntax shown here applies both to groupings with [`LOOP AT itab ... GROUP BY`](abaploop_at_itab_group_by.md) and to groupings with [`FOR GROUPS ... OF`](abenfor_groups_of.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A structured group key is used to group by more than just one criterion. The group criteria here are simply columns of the internal table. This is a representative binding in which the work area `wa` is reused in the group loop to access the group key.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
LOOP AT spfli_tab INTO FINAL(wa) 
                  GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom ). 
  out->write( |{ wa-carrid } { wa-airpfrom }| ). 
ENDLOOP. 
 
out->display( ).
```

## Addition 1

`... gs = GROUP SIZE`

## Addition 2

`... gi = GROUP INDEX`

### Description

Declares additional components for a structured group key. These components are not part of the group key and are used to store group-specific information instead:

- The component `gs` is filled with the number of group members for each group.

- The component `gi` is filled with a group index for each group. The group index of the group key constructed first is 1 and is raised by 1 for each new group key.

Before the additional components can be declared, a group key binding must be defined in the output behavior [`group_result`](abaploop_at_itab_group_by_binding.md). The additional components can be accessed in the group loop using the data object or field symbol specified here.

The names of the components `gs` and `gi` can be freely defined. The language elements `GROUP SIZE` or `GROUP INDEX` on the right side give the components their special semantics.

### Hints

- If the groups are not sorted using [`ASCENDING`](abaploop_at_itab_group_by.md) or [`DESCENDING`](abaploop_at_itab_group_by.md), the groups in the group loop are processed in the order of the group index. If the groups are sorted differently, the original position is noted in the group index.

- The additional components can still be evaluated even if the addition [`WITHOUT MEMBERS`](abaploop_at_itab_group_by.md) is used and the group members cannot be accessed.

- Implicitly, no further values are created that match the results of [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) when [`GROUP BY`](../abap-database-access/abapgroupby_clause.md) is used in the ABAP SQL statement [`SELECT`](../abap-database-access/abapselect.md), except in the component `gs` with the right side `GROUP SIZE`. Aggregations like this are easy to program particularly when applying constructor operators such as [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) to the group members. The ABAP SQL addition [`HAVING`](../abap-database-access/abaphaving_clause.md) for restricting the loops of groups is a similar case. Here, for example, the [filter operator](../../abap-glossary/abenfilter_operator_glosry.md) [`FILTER`](abenconstructor_expression_filter.md) can be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a structured group key with additional components for group index and group size. A group key binding must be defined with `INTO data(key)`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
LOOP AT spfli_tab INTO FINAL(wa) 
                  GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom 
                             indx = GROUP INDEX 
                             size = GROUP SIZE ) 
                  INTO data(key). 
  out->write( |{ key-indx } { key-key1 
             } { key-key2 } { key-size }| ). 
ENDLOOP. 
 
out->display( ).
```
