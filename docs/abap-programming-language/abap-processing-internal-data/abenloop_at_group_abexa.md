---
title: "itab - Grouping with LOOP, Output Behavior"
source_file: abenloop_at_group_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP, Output Behavior

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the different output behavior in groupings of internal tables.

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
CLASS cl_demo_loop_at_group_syntax DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_at_group_syntax IMPLEMENTATION. 
  METHOD main. 
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
 
    DATA members TYPE itab. 
 
    out->begin_section( `Representative Binding` 
      )->begin_section( `INTO wa` ). 
    LOOP AT itab INTO FINAL(wa) 
                 GROUP BY ( key1 = wa-key1 key2 = wa-key2 ). 
      DATA(idx) = sy-tabix. 
      CLEAR members. 
      out->begin_section( |Group { idx }| ). 
      LOOP AT GROUP wa INTO DATA(member). 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
    out->next_section( `ASSIGNING <fs>` ). 
    LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>) 
                 GROUP BY ( key1 = <fs>-key1 key2 = <fs>-key2 ). 
      idx = sy-tabix. 
      CLEAR members. 
      out->begin_section( |Group { idx }| ). 
      LOOP AT GROUP <fs> INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
    out->next_section( `REFERENCE INTO dref` ). 
    LOOP AT itab REFERENCE INTO FINAL(dref) 
                 GROUP BY ( key1 = dref->key1 key2 = dref->key2 ). 
      idx = sy-tabix. 
      CLEAR members. 
      out->begin_section( |Group { idx }| ). 
      LOOP AT GROUP dref INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
    out->end_section( )->end_section( ). 
 
    out->begin_section( `Group Key Binding` 
      )->begin_section( `INTO group` ). 
    LOOP AT itab ASSIGNING <fs> 
                 GROUP BY ( key1 = <fs>-key1 key2 = <fs>-key2 ) 
                 INTO FINAL(group). 
      idx = sy-tabix. 
      CLEAR members. 
      out->begin_section( 
        |Group { idx }, Key { group-key1 } { group-key2 }| ). 
      LOOP AT GROUP group INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
    out->next_section( `ASSIGNING <group>` ). 
    LOOP AT itab ASSIGNING <fs> 
                 GROUP BY ( key1 = <fs>-key1 key2 = <fs>-key2 ) 
                 ASSIGNING FIELD-SYMBOL(<group>). 
      idx = sy-tabix. 
      CLEAR members. 
      out->begin_section( 
        |Group { idx }, Key { <group>-key1 } { <group>-key2 }| ). 
      LOOP AT GROUP <group> INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
    out->next_section( `REFERENCE INTO group_ref` ). 
    LOOP AT itab ASSIGNING <fs> 
                 GROUP BY ( key1 = <fs>-key1 key2 = <fs>-key2 ) 
                 REFERENCE INTO FINAL(group_ref). 
      idx = sy-tabix. 
      CLEAR members. 
      out->begin_section( 
        |Group { idx }, Key { group_ref->key1 } { group_ref->key2 }| ). 
      LOOP AT GROUP group_ref INTO member. 
        members = VALUE #( BASE members ( member ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In the [grouping](abaploop_at_itab_group_by.md) of an internal table `itab`, the six ways of combining the [output behavior](abaploop_at_itab_result.md) of the `LOOP` statement with the [output behavior](abaploop_at_itab_group_by_binding.md) of the [group loop](../../abap-glossary/abengroup_loop_glosry.md) are demonstrated. The three [group loops](../../abap-glossary/abengroup_loop_glosry.md) with [representative binding](abaploop_at_itab_group_by_binding.md) and three group loops with [group key binding](abaploop_at_itab_group_by_binding.md) are executed, each using the three ways of defining the [output behavior](abaploop_at_itab_result.md) of the `LOOP` statement.

In each group loop a [member loop](../../abap-glossary/abenmember_loop_glosry.md) is executed. Here, the group is specified after [`LOOP AT GROUP`](abaploop_at_group.md) that is produced by the output behavior. In the member loop, the members are placed in an internal table `members` using the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) with the addition [`BASE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). This table is then output in the group loop. The result is the same in all cases.

In addition, the value of `sy-tabix` in the group loop is produced, which is different in the representative binding and in the group key binding. In the group key binding, the group key can also be addressed and produced, which is not possible in the representative binding.
