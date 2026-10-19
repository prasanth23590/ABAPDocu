---
title: "LOOP AT itab, group_result"
source_file: abaploop_at_itab_group_by_binding.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT itab, group_result

## Syntax

``` abap
 ... { } 
  | {INTO group}|{ASSIGNING <group>}|{REFERENCE INTO group_ref} ...  
```

### Alternative

[1. `... { }`](abaploop_at_itab_group_by_binding.md#alternative-1)

[2. `... {INTO group}|{ASSIGNING <group>}|{REFERENCE INTO group_ref}`](abaploop_at_itab_group_by_binding.md#alternative-2)

## Overview

### Description

Defines the output behavior of the [group loop](abaploop_at_itab_group_by.md) in a [grouping](abaploop_at_itab_group_by.md) of an internal table in a `LOOP`. The output behavior defines the following:

- A data object or field symbol whose content is accessed in the group loop and which can also be passed to called procedures.

- A name for the group which can only be used within the current group loop and loops nested in the statement [`LOOP AT GROUP`](abaploop_at_group.md) or in an expression [`FOR ... IN GROUP`](abenfor_in_group.md) for specifying a group.

## Alternative 1

`... { }`

### Description

Representative binding. If nothing is specified for the output behavior `group_result`, the output behavior is determined for the table lines using the addition [`result`](abaploop_at_itab_result.md). In each loop pass, the first line of the current group is assigned as a representative of its group to the data object or field symbol defined there. The representative is bound to the current group and the group can be addressed using the name of the representative in the statement [`LOOP AT GROUP`](abaploop_at_group.md) or the expression [`FOR ... IN GROUP`](abenfor_in_group.md).

If the representative binding is used,

- the addition [`WITHOUT MEMBERS`](abaploop_at_itab_group_by.md) is not possible, since there would be no assignment of the representative to its group in this case,

- no additional components for [`GROUP SIZE`](abaploop_at_itab_group_by_key.md) and [`GROUP INDEX`](abaploop_at_itab_group_by_key.md) can be created for a structured group key, since it is impossible to access these components in this case.

Outside of the group loop, the representative is not bound to the group and cannot be used to specify it in [member loops](../../abap-glossary/abenmember_loop_glosry.md). This applies in particular to procedures called from the group loop.

### Hint

If a representative is bound to the current group, the associated group key cannot be addressed in the group loop.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The group key in the following example is a structure with two components `key1` and `key2` to which the columns `key1` and `key2` are assigned to each line of the internal table `itab` in the grouping. This produces three groups with the group key values `(a, a)`, `(a, b)`, and `(b, a)`. Accordingly, the group loop is passed three times and the first, second, and sixth line are assigned to the field symbol `<wa>` as representatives. See also the [executable example](abenloop_at_group_abexa.md) of output behavior.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struct, 
    key1 TYPE string, 
    key2 TYPE string, 
    col  TYPE i, 
  END OF struct, 
  itab TYPE STANDARD TABLE OF struct WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( 
  ( key1 = `a` key2 = `a` col = 1 ) 
  ( key1 = `a` key2 = `b` col = 2 ) 
  ( key1 = `a` key2 = `a` col = 3 ) 
  ( key1 = `a` key2 = `a` col = 4 ) 
  ( key1 = `a` key2 = `b` col = 5 ) 
  ( key1 = `b` key2 = `a` col = 6 ) 
  ( key1 = `b` key2 = `a` col = 7 )  ). 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<wa>) 
             GROUP BY ( key1 = <wa>-key1 key2 = <wa>-key2 ). 
  out->write( <wa> ). 
ENDLOOP. 
 
out->display( ).
```

## Alternative 2

`... {INTO group}|{ASSIGNING <group>}|{REFERENCE INTO group_ref}`

### Description

Group key binding. If an explicit output behavior `group_result` is specified, the group key of the current key is assigned to the data object or field symbol specified after `INTO`, `ASSIGNING`, or `REFERENCE INTO` in every loop pass. Here, the same syntax and semantics apply as in the output behavior [`result`](abaploop_at_itab_result.md). The data type of the specified data object or field symbol must match the data type of the group key. If the group key is constructed as a new structure in the [group key expression](abaploop_at_itab_group_by_key.md), the target type must be a structure whose components have the same name and in the same order as in the group key.

The specified data object or field symbol is bound to the current group and the group can be addressed using its name in the statement [`LOOP AT GROUP`](abaploop_at_group.md) or the expression [`FOR ... IN GROUP`](abenfor_in_group.md). Outside of the group loop, the data object or field symbol is not bound to the group and cannot be used to specify it in [member loops](../../abap-glossary/abenmember_loop_glosry.md). This applies in particular to procedures that are called from the group loop. At the end of the group loop, the grouping is canceled and a specified data object is initialized or a field symbol no longer has a group key assigned to it.

The data object or field symbol of the output behavior defined in [`result`](abaploop_at_itab_result.md) for the table lines can still be addressed in the group loop but it is either initial after the `LOOP` statement or does not point to a line.

### Hints

- To specify a type-compliant data object or field symbol as the target for the group key, it is best to use an [inline declaration](../abap-declarations/abeninline_declarations.md), which is always possible here.

- The output behavior [`result`](abaploop_at_itab_result.md) for the table lines is still required when `group_result` is specified explicitly for the construction of the group key [`group_key`](abaploop_at_itab_group_by_key.md).

- Unlike in [`result`](abaploop_at_itab_result.md) for table lines, no additions `CASTING` or `ELSE UNASSIGN` can be specified after `ASSIGNING`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like in the previous example, however the groups are not assigned to an implicit representative here and to the explicitly defined target area for the group key instead. In each of the three loop passes, the reference variable `group_key` declared inline points to the respective structured group key `(a, a)`, `(a, b)`, and `(b, a)`. See also the [executable example](abenloop_at_group_abexa.md) of output behavior.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struct, 
    key1 TYPE string, 
    key2 TYPE string, 
    col  TYPE i, 
  END OF struct, 
  itab TYPE STANDARD TABLE OF struct WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( 
  ( key1 = `a` key2 = `a` col = 1 ) 
  ( key1 = `a` key2 = `b` col = 2 ) 
  ( key1 = `a` key2 = `a` col = 3 ) 
  ( key1 = `a` key2 = `a` col = 4 ) 
  ( key1 = `a` key2 = `b` col = 5 ) 
  ( key1 = `b` key2 = `a` col = 6 ) 
  ( key1 = `b` key2 = `a` col = 7 )  ). 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<wa>) 
             GROUP BY ( key1 = <wa>-key1 key2 = <wa>-key2 ) 
             WITHOUT MEMBERS 
             REFERENCE INTO FINAL(group_key). 
  out->write( group_key->* ). 
ENDLOOP. 
 
out->display( ).
```
