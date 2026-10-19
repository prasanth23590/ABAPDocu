---
title: "LOOP AT GROUP"
source_file: abaploop_at_group.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT GROUP

## Syntax

``` abap
LOOP AT GROUP group result   [WHERE log_exp] [GROUP BY ...].   
  ...   
ENDLOOP.  
```

[`result `](abaploop_at_itab_result.md) · [`WHERE log_exp`](abaploop_at_itab_cond.md) · [`GROUP BY ...`](abaploop_at_itab_group_by.md)

### Addition

[`... WHERE log_exp`](abaploop_at_group.md#addition)

## Overview

### Description

Member loop across the lines of a group within the [group loop](abaploop_at_itab_group_by.md) in the [grouping](abaploop_at_itab_group_by.md) of internal tables. This loop is only possible within a [`LOOP`](abaploop_at_itab_variants.md) across an internal table with the addition [`GROUP BY`](abaploop_at_itab_group_by.md),

- for which the internal table `itab` is specified directly as a data object and not as the result of a call or expression,

- in which the addition `WITHOUT MEMBERS` is not used.

`group` is used to specify the group across which the member loop passes. The target object must be specified that is defined in the output behavior [`group_result`](abaploop_at_itab_group_by_binding.md) of the group loop and bound to the group:

- In the representative binding, this is a representative specified in the output behavior [`result`](abaploop_at_itab_result.md).

- In the group key binding, this is a data object or field symbol specified in the output behavior [`group_result`](abaploop_at_itab_group_by_binding.md).

The member loop across the current group is executed just like a regular [`LOOP`](abaploop_at_itab_variants.md) across a standard table with the line type of `itab` which contains the lines of the group. Both variants are possible:

- [Loop across lines](abaploop_at_itab.md) without the addition `GROUP BY`.

- [Loop across groups](abaploop_at_itab.md) with the addition `GROUP BY`.

The second option enables further groupings of existing groups.

### System Fields

The statement `LOOP AT GROUP` sets the value of the system field `sy-tabix` in the member loop to the value that would be set for the current line in the `LOOP` without grouping.

A member loop always sets the system field `sy-subrc` to 0.

### Hints

- Despite the fact that there is always only one grouping for a single `LOOP`, it is still necessary to specify the group `group` explicitly, since multiple groups can be accessed in nested `LOOP` statements.

- `group` expects the precise name specified in the output behavior, namely a field symbol with angle brackets specified after `ASSIGNING` and a data reference variable without dereferencing operator `->` specified after `REFERENCE INTO`.

- The statement `LOOP AT GROUP` can only be listed within a loop defined using [`LOOP AT ... GROUP BY`](abaploop_at_itab_group_by.md), since the name for the group defined using its [output behavior](abaploop_at_itab_group_by_binding.md) is only valid here. `LOOP AT GROUP` is in particular not possible in procedures called from a group loop, even if the data object or field symbol defined by the output behavior can be accessed here.

- Despite the syntax and semantics of `LOOP AT GROUP` being the same as a regular nested loop, the way the lines of the group are actually accessed is optimized. This exploits the internal variant of the assignment of the lines to their group.

- A loop `LOOP AT GROUP` does not allow [group level processing](../../abap-glossary/abengroup_level_processing_glosry.md) with the statement [`AT`](abapat_itab.md).

- A group loop does not create any empty groups, which means that a member loop is always passed as a rule. Only `WHERE` conditions can be used to prevent members of a group from being processed. Internally, however, this is not detected until the start of the first loop pass, which means that `sy-subrc` is set to 0 in this case as well.

- The statement `LOOP AT GROUP` corresponds to the expression [`FOR ... IN GROUP`](abenfor_in_group.md). This means its functions can often be expressed more elegantly using [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md) or [table reductions](../../abap-glossary/abentable_reduction_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Member loop in a group loop, where the flight numbers belonging to an airline are grouped together in a string.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
LOOP AT spfli_tab INTO FINAL(wa) 
                  GROUP BY wa-carrid 
                  INTO FINAL(key). 
  out->next_section( |{ key }| ). 
  DATA(str) = ``. 
  LOOP AT GROUP key ASSIGNING FIELD-SYMBOL(<members>). 
    str = str && ` ` && <members>-connid. 
  ENDLOOP. 
  out->write( str ). 
ENDLOOP. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows each of the six different syntax methods of specifying a group in a member loop:

- Work area `wa` of the `LOOP` in a [representative binding](abaploop_at_itab_group_by_binding.md).

- Field symbol `<fs>` of the `LOOP` in a [representative binding](abaploop_at_itab_group_by_binding.md).

- Data reference variable `dref` of the `LOOP` in a [representative binding](abaploop_at_itab_group_by_binding.md).

- Work area `group` of the group loop in a [group key binding](abaploop_at_itab_group_by_binding.md).

- Field symbol `group` of the group loop in a [group key binding](abaploop_at_itab_group_by_binding.md).

- Data reference variable `group_ref` of the group loop in a [group key binding](abaploop_at_itab_group_by_binding.md).

``` abap
TYPES itab TYPE STANDARD TABLE OF i WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( ( 1 ) ( 1 ) ( 2 ) ( 2 ) ). 
 
LOOP AT itab INTO DATA(wa) GROUP BY wa. 
  LOOP AT GROUP wa INTO DATA(member). 
    ... 
  ENDLOOP. 
ENDLOOP. 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>) GROUP BY <fs>. 
  LOOP AT GROUP <fs> INTO member. 
    ... 
  ENDLOOP. 
ENDLOOP. 
 
LOOP AT itab REFERENCE INTO FINAL(dref) GROUP BY dref->*. 
  LOOP AT GROUP dref INTO member. 
    ... 
  ENDLOOP. 
ENDLOOP. 
 
LOOP AT itab INTO wa GROUP BY wa 
             INTO FINAL(group). 
  LOOP AT GROUP group INTO member. 
    ... 
  ENDLOOP. 
ENDLOOP. 
 
LOOP AT itab INTO wa GROUP BY wa 
             ASSIGNING FIELD-SYMBOL(<group>). 
  LOOP AT GROUP <group> INTO member. 
    ... 
  ENDLOOP. 
ENDLOOP. 
 
LOOP AT itab INTO wa GROUP BY wa 
             REFERENCE INTO FINAL(group_ref). 
  LOOP AT GROUP group_ref INTO member. 
    ... 
  ENDLOOP. 
ENDLOOP.
```

## Addition

`... WHERE log_exp`

### Description

The lines read from the group can be restricted using a static [`WHERE` condition](abaploop_at_itab_cond.md). The syntax and semantics are the same as in a `LOOP` across an internal table with the line type of `itab`.

### Hint

The additions [`USING KEY`](abaploop_at_itab_cond.md), [`FROM`](abaploop_at_itab_cond.md), [`TO`](abaploop_at_itab_cond.md), and a dynamic `WHERE` condition cannot be specified after `LOOP AT GROUP`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the example above, but with a restricted `WHERE` condition for the member loop.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(spfli_tab). 
 
LOOP AT spfli_tab INTO FINAL(wa) 
                  GROUP BY wa-carrid 
                  INTO FINAL(key). 
  out->next_section( |{ key }| ). 
  DATA(str) = ``. 
  LOOP AT GROUP key ASSIGNING FIELD-SYMBOL(<members>) 
                    WHERE cityfrom = 'NEW YORK'. 
    str = str && ` ` && <members>-connid. 
  ENDLOOP. 
  out->write( str ). 
ENDLOOP. 
 
out->display( ).
```
