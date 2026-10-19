---
title: "itab - Grouping with LOOP Using a Function"
source_file: abenloop_group_by_func_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP Using a Function

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the construction of the group key using a string function.

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
CLASS cl_demo_loop_grp_by_string_fnc DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA text TYPE TABLE OF string WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_string_fnc IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `Text` ). 
    out->write( text ). 
    out->next_section( `Grouping` ). 
    DATA members LIKE text. 
    LOOP AT text INTO FINAL(line) 
         GROUP BY replace( val = line pcre = `\D` with = `` occ =  0 ) 
                  ASCENDING AS TEXT 
                  ASSIGNING FIELD-SYMBOL(<group>). 
      out->begin_section( |Group Key: { <group> }| ). 
      CLEAR members. 
      LOOP AT GROUP <group> ASSIGNING FIELD-SYMBOL(<member>). 
        members = VALUE #( BASE members ( <member> ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    text = VALUE #( ( `aaa1aaaaa2aaaaa` ) 
                    ( `bbbbb3bbbbbbbbb` ) 
                    ( `cccccccccc3cccc` ) 
                    ( `ddddddddddddddd` ) 
                    ( `eeeee1eeeeee2ee` ) 
                    ( `ffff1fff2ff3fff` ) 
                    ( `ggggggggggggggg` ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[Grouping](abaploop_at_itab_group_by.md) of an internal table `text` with [group key binding](abaploop_at_itab_group_by_binding.md). The [group key](abaploop_at_itab_group_by_key.md) of the [group loop](../../abap-glossary/abengroup_loop_glosry.md) is constructed as a value of the type `string`, which is calculated from the content of each table line using the built-in function `replace`. This creates groups of lines that contain the same digits in the same order in their text. The groups are sorted in ascending order according to the group key.

The group key that is bound to a field symbol `<group>` is produced in the group loop. The first group key is an initial text string. In a [member loop](../../abap-glossary/abenmember_loop_glosry.md), the lines of each group are placed in an internal table `members` using the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) with the addition [`BASE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). This table is also displayed.

`members` could also be filled by evaluating a table comprehension using [`FOR ... IN GROUP`](abenfor_in_group.md), instead of in a [member loop](../../abap-glossary/abenmember_loop_glosry.md) [`LOOP AT GROUP`](abaploop_at_group.md):

`members = VALUE #( FOR <member> IN GROUP <group> ( <member> ) ).`

The executable example for [grouping with `FOR`](abenfor_group_by_func_abexa.md) demonstrates how the entire group loop can be implemented using expressions.
