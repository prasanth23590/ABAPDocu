---
title: "itab - Grouping Internal Tables, Step by Step"
source_file: abenloop_group_by_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping Internal Tables, Step by Step

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example is a step-by-step introduction to grouping with [`LOOP AT GROUP BY`](abaploop_at_itab_group_by.md).

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_loop_at_itab_group_by DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_at_itab_group_by IMPLEMENTATION. 
  METHOD main. 
 
    DATA: 
      wa      TYPE spfli, 
      member  TYPE spfli, 
      members TYPE STANDARD TABLE OF spfli WITH EMPTY KEY. 
 
 
    SELECT * 
           FROM spfli 
           INTO TABLE @FINAL(spfli_tab). 
 
    out->begin_section( `Representative Binding` ). 
 
    out->begin_section( 
     `Grouping by one column` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY wa-carrid. 
      out->write( wa-carrid ). 
    ENDLOOP. 
 
    out->next_section( 
     `Members of one column groups` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY wa-carrid. 
      CLEAR members. 
      LOOP AT GROUP wa INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members ). 
    ENDLOOP. 
 
    out->next_section( 
     `Grouping by two columns` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom ). 
      out->write( |{ wa-carrid } { wa-airpfrom }| ). 
    ENDLOOP. 
 
    out->next_section( 
     `Members of two column groups` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom ). 
      CLEAR members. 
      LOOP AT GROUP wa INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members ). 
    ENDLOOP. 
 
    out->end_section( )->next_section( `Group Key Binding` ). 
 
    out->next_section( 
     `Grouping by one column` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY wa-carrid 
                      INTO DATA(key). 
      out->write( key ). 
    ENDLOOP. 
 
    out->next_section( 
     `Members of one column groups` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY wa-carrid 
                      INTO key. 
      CLEAR members. 
      LOOP AT GROUP key INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members ). 
    ENDLOOP. 
 
    out->next_section( 
     `Grouping by two columns` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom ) 
                      INTO DATA(keys). 
      out->write( keys ). 
    ENDLOOP. 
 
    out->next_section( 
     `Members of two column groups` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom ) 
                      INTO keys. 
      CLEAR members. 
      LOOP AT GROUP keys INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members ). 
    ENDLOOP. 
 
 
    out->next_section( 
     `Two column groups without members` ). 
    LOOP AT spfli_tab INTO wa 
                      GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom 
                                 index = GROUP INDEX size = GROUP SIZE ) 
                      WITHOUT MEMBERS 
                      INTO FINAL(keysplus). 
      out->write( keysplus ). 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Similar to SQL's [`GROUP BY`](../abap-database-access/abapgroupby_clause.md), there is also a [`GROUP BY`](abaploop_at_itab_group_by.md) for working with internal tables that can be used behind [`LOOP AT itab`](abaploop_at_itab_variants.md) or in the form [`IN GROUP`](abenfor_in_group.md) in a table iteration with [`FOR`](abenfor_itab.md). It replaces the clumsy group level processing with statements [`AT NEW ...`](abapat_itab.md) that relies on the order of table columns and content that is sorted respectively.

While there are more examples for all the powerful features of `GROUP BY` and `IN GROUP` under

- [Examples of Grouping with `LOOP`](abenloop_group_by_abexas.md),

- [Examples of Grouping with `FOR`](abenfor_grouping_abexas.md),

the above example shows the grouping of internal tables step by step using a very simple case of an internal table `spfli_tab` that is filled with data from the database table `SPFLI`. The following steps explain how the content of the internal table can be grouped using [`LOOP AT GROUP BY`](abaploop_at_itab_group_by.md):

## Grouping by One Column

The simplest form of grouping is by one column without explicitly specifying the output behavior of the group loop:

``` abap
LOOP AT spfli_tab INTO wa 
                  GROUP BY wa-carrid. 
       ... wa-carrid ... 
ENDLOOP.
```

Within the loop, there is access to the work area `wa`, in particular to the component `wa-carrid` that is used for grouping. The work area `wa` contains the first line of each group and represents the group in the loop. This is called representative binding.

To access the members of a group, a member loop can be inserted into the group loop:

``` abap
LOOP AT spfli_tab INTO wa 
                  GROUP BY wa-carrid. 
  ... 
  LOOP AT GROUP wa INTO DATA(member). 
    ... member-... ... 
  ENDLOOP. 
  ... 
ENDLOOP.
```

The member loop is executed using the group represented by `wa` and its members are assigned to `member` and are available in the member loop.

## Grouping by More than One Column

To group by more than just one criterion, a structured group key is defined as follows. In the simplest case, the grouping criteria are columns of the internal table:

``` abap
LOOP AT spfli_tab INTO wa 
                  GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom ). 
  ... wa-carrid ... wa-airpfrom ... 
ENDLOOP.
```

This is also a representative binding in which the work area `wa` is reused in the group loop to access the group key.

To access the members of the groups, the exact same member loop can be inserted as when grouping by one column.

## Group Key Binding when Grouping by One Column

By explicitly specifying an [output area](abaploop_at_itab_group_by_binding.md) for the group key, a group key binding can be defined explicitly instead of the representative binding in which the output area of the group loop is reused:

``` abap
LOOP AT spfli_tab INTO wa 
                  GROUP BY wa-carrid 
                  INTO DATA(key). 
  ... key ... 
ENDLOOP.
```

The difference to the example with representative binding is the `INTO` addition after `GROUP BY`. Instead of reusing `wa`, an elementary data object `key` represents the group. This can be generated inline. The additions [`GROUP SIZE`](abaploop_at_itab_group_by_key.md), [`GROUP INDEX`](abaploop_at_itab_group_by_key.md), and [`WITHOUT MEMBERS`](abaploop_at_itab_group_by.md) can only be used in the group key binding, which gives it more functions than the representative binding. If these are not required, the representative binding can be used. The group key binding can also be used to make the use of the group key in the loop more explicit.

Inserting a member loop works in the same way as in the representative binding, with the difference that a group is now addressed by `key` instead of `wa`.

``` abap
LOOP AT spfli_tab INTO wa 
                  GROUP BY wa-carrid 
                  INTO key. 
  ... 
  LOOP AT GROUP key INTO member. 
    ... members ... 
  ENDLOOP. 
  ... 
ENDLOOP.
```

## Group Key Binding when Grouping by More than One Column

Finally, the group key binding for structured group keys:

``` abap
LOOP AT spfli_tab INTO wa 
                  GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom ) 
                  INTO DATA(key). 
  ... key-key1 ... key-key2 ... 
ENDLOOP.
```

Here, `key` is a structure with the components `key1` and `key2`. A member loop can be inserted in exactly the same way as when grouping by one column.

If the group members are not relevant, the addition [`NO MEMBERS`](abaploop_at_itab_group_by.md) can be used to save time and memory.

``` abap
LOOP AT spfli_tab INTO wa 
                  GROUP BY ( key1 = wa-carrid key2 = wa-airpfrom 
                             index = GROUP INDEX size = GROUP SIZE ) 
                  WITHOUT MEMBERS 
                  INTO DATA(key). 
  ... key-key1 ... key-key2 ... key-index ... key-size ... 
ENDLOOP.
```

It is no longer possible to use a member loop here. Instead, the group key was enriched with optional components for further information using [`GROUP INDEX`](abaploop_at_itab_group_by_key.md) [`GROUP SIZE`](abaploop_at_itab_group_by_key.md).
