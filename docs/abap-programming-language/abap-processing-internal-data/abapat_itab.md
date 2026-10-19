---
title: "AT, Group Level Processing"
source_file: abapat_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, Basic Form"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AT, Group Level Processing

## Deprecated Syntax

``` abap
LOOP AT itab result [cond].   
  [AT FIRST.   
     ...   
   ENDAT.]   
    [AT NEW comp1.   
       ...   
     ENDAT.   
       [AT NEW comp2.   
         ...   
       ENDAT.   
         [...]]]   
           [ ... ]   
       [[[...]   
       AT END OF comp2.   
         ...   
       ENDAT.]   
     AT END OF comp1.   
       ...   
     ENDAT.]   
  [AT LAST.   
     ...   
  ENDAT.]   
ENDLOOP.  
```

[`LOOP AT itab`](abaploop_at_itab.md) · [`result`](abaploop_at_itab_result.md) · [`cond`](abaploop_at_itab_cond.md) · [`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md) · [`comp2`](abenitab_components.md) · [`comp1`](abenitab_components.md)

### Addition

[1. `... FIRST`](abapat_itab.md#addition-1)

[2. `... {NEW}|{END OF} compi`](abapat_itab.md#addition-2)

[3. `... LAST`](abapat_itab.md#addition-3)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Overview

### Description

The statement block of a [`LOOP`](abaploop_at_itab.md) without the addition [`GROUP BY`](abaploop_at_itab_group_by.md) can contain control structures for [group level processing](../../abap-glossary/abengroup_level_processing_glosry.md). The corresponding control statement is `AT`. The statements `AT` and `ENDAT` define statement blocks that are executed at [group breaks](../../abap-glossary/abengroup_break_glosry.md), that is, in the transition of one [group level](../../abap-glossary/abengroup_level_glosry.md) to another group level. The additions of the statements `AT` define the criteria for a group break and hence the group levels. Group breaks between group levels are a result of the line structure and the processing order in which the `LOOP` reads the lines of the internal table.

Apart from the special variants `AT FIRST` and `AT LAST`, group levels are defined using the variants `AT NEW` `AT END OF` and by the consecutive lines of the internal table specified in accordance with the processing order of the loop. These lines have the same content in a group key defined by their initial part. Here, all lines of the internal table are respected without evaluating any restricting conditions [`cond`](abaploop_at_itab_cond.md).

Although it is syntactically possible to arrange `AT` control structures in any order and to nest them, however, effective group level processing is usually only achieved by the arrangement above. Here, the control structures are listed in accordance with the arrangement of the components in the group key and are not nested.

The statement blocks within the `AT`-`ENDAT` control structures are executed if a corresponding group break takes place in the current table line. Statements in the `LOOP`-`ENDLOOP` control structure that are not executed within an `AT`-`ENDAT` control structure are executed in each pass of the loop. If a table line with a group break is not read due to a restricting condition [`cond`](abaploop_at_itab_cond.md), the corresponding statement block is not executed.

The following rules must be observed for effective group level processing:

- A table key specified in `LOOP` in [`cond`](abaploop_at_itab_cond.md) must be chosen so that it produces the required processing order of the imported lines.

- The addition [`STEP`](abaploop_at_itab_cond.md) cannot be specified. Also other restricting conditions [`cond`](abaploop_at_itab_cond.md) should not be specified. If a condition is specified, it should select consecutive line groups, including the first line in the group where the group break takes place.

- The internal table must not be modified within the `LOOP` loop.

- A work area `wa` specified in the `LOOP` statement after the addition `INTO` must be [compatible](../../abap-glossary/abencompatible_glosry.md) with the line type of the table.

- A field symbol `<fs>` specified in the statement `LOOP` after the addition `ASSIGNING` must be typed with the line type of the table.

- The content of a work area [`wa`](abaploop_at_itab.md) specified in the statement [`LOOP`](abaploop_at_itab_result.md) after the addition `INTO` cannot be modified.

If the addition [`INTO wa`](abaploop_at_itab_result.md) is used in the statement [`LOOP`](abaploop_at_itab.md), the content of `wa` is overwritten when the `AT`-`ENDAT` control structure is entered, depending on the respective group level, and is reset to the content of the current line when the control structure is exited. When the additions [`ASSIGNING`](abaploop_at_itab_result.md) and [`REFERENCE INTO`](abaploop_at_itab_result.md) are used, the referenced table lines are not modified when entering and exiting the `AT`-`ENDAT` control structure.

### Hints

- The most common case is when the internal table is sorted exactly by the order of the components of its line type, that is, by the first component first, then by the second component, and so on. In this case, group level processing can also be expressed using a grouping with the addition [`GROUP BY`](abaploop_at_itab_group_by.md).

- If possible, the use of the addition [`GROUP BY`](abaploop_at_itab_group_by.md) is recommended, since the grouping does not depend on the structure of the lines and the processing order in this case.

- Group level processing with the statement `AT` is not possible in `LOOP` statements across line groups with the addition [`GROUP BY`](abaploop_at_itab_group_by.md), including member loops using [`LOOP AT GROUP`](abaploop_at_group.md).

- The group level processing described here can produce unexpected results when a restricting condition [`cond`](abaploop_at_itab_cond.md) is used, which means that extended syntax check messages can occur.

### Executable Example

Group Level Processing

## Addition 1

`... FIRST`

### Description

The group level is defined by the first line of the internal table. The group break takes place when this line is read. In the group level `AT FIRST`, the current group key does not contain any components.

If the addition [`INTO wa`](abaploop_at_itab_result.md) is used in the statement [`LOOP`](abaploop_at_itab.md), all character-like components of the work area `wa` are filled with *\** when the control structure `AT FIRST` is entered and all other components are set to their initial value. In the case of an elementary line type, this applies to the entire work area. When the `AT`-`ENDAT` control structure is exited, the content of the current table line is reassigned to the work area `wa`.

### Hint

If the first line of the internal table is not read due to a restricting condition [`cond`](abaploop_at_itab_cond.md), the statement block of the control structure `AT FIRST` is not executed.

## Addition 2

`... {NEW}|{END OF} compi`

### Description

Group levels are defined by the beginning or end of a group of lines with the same content in the component `compi` (where `i` = `1`, `2`, and so on) and in the components on the left of `compi`. The content of these components determines the group key. The group breaks take place when the content of the component `compi` or another component on the left of `compi` changes.

The `compi` components can be specified as described in [Specification of Components](abenitab_components.md), with the restriction that access to data objects using references is not possible here. The following is therefore not possible:

- Specifying data objects using data references

- Specifying attributes of objects using object references

Otherwise, the specified components can have any data type. The corresponding [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) apply to the evaluation. In the case of an elementary line type, only `table_line` can be specified as the group key.

If the addition [`INTO wa`](abaploop_at_itab_result.md) is used in the statement [`LOOP`](abaploop_at_itab.md), the content of `wa` is modified as follows when the `AT`-`ENDAT` control structure is entered:

- The components of the current group key remain unchanged.

- All components with a character-like [flat](../../abap-glossary/abenflat_glosry.md) data type on the right of the current control key are set to the character *\** in every place.

- All the other components to the right of the current group key are set to their [initial value](../../abap-glossary/abeninitial_value_glosry.md).

In the case of an elementary line type, the entire work area corresponds to the current group key and remains unchanged. When the `AT`-`ENDAT` control structure is exited, the content of the current table line is reassigned to the work area `wa`.

### Hints

- Group levels defined in this way consist of the consecutive lines of the internal table that have the same content in an initial part.

- If the first or last line of a line group is not read due to a restricting condition [`cond`](abaploop_at_itab_cond.md), the statement block of the control structure `AT NEW` or `AT END OF` is not executed.

## Addition 3

`... LAST`

### Description

The group level is defined by the last line of the internal table. The group break takes place when this line is read. In the group level `AT LAST`, the current group key does not contain any components.

If the addition [`INTO wa`](abaploop_at_itab_result.md) is used in the statement [`LOOP`](abaploop_at_itab.md), all character-like components of the work area `wa` are filled with *\** when the control structure `AT LAST` is entered and all other components are set to their initial value. In the case of an elementary line type, this applies to the entire work area. When the `AT`-`ENDAT` control structure is exited, the content of the current table line is reassigned to the work area `wa`.

### Hint

If the last line of the internal table is not read due to a restricting condition [`cond`](abaploop_at_itab_cond.md), the statement block of the control structure `AT LAST` is not executed.
