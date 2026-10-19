---
title: "itab - Grouping with LOOP Using Column Values"
source_file: abenloop_group_by_values_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP Using Column Values

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the construction of the group key using simple value assignments.

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
CLASS cl_demo_loop_grp_by_values DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS initialize. 
 
  PRIVATE SECTION. 
    DATA: 
      carrier TYPE spfli-carrid VALUE 'LH', 
      flights TYPE TABLE OF spfli WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_values IMPLEMENTATION. 
  METHOD main. 
    initialize( ). 
 
    out->begin_section( `Flights` ). 
    out->write( flights ). 
    out->begin_section( `Grouping` ). 
    DATA members LIKE flights. 
    LOOP AT flights INTO FINAL(flight) 
         GROUP BY ( carrier = flight-carrid cityfr = flight-cityfrom 
                    size = GROUP SIZE index = GROUP INDEX ) 
                  ASCENDING 
                  REFERENCE INTO FINAL(group_ref). 
      out->begin_section( 
        |Group Key: { group_ref->carrier }, { group_ref->cityfr }| ). 
      out->write( 
        |Group Size: {  group_ref->size  }, | && 
        |Group Index: { group_ref->index }| ). 
      CLEAR members. 
      LOOP AT GROUP group_ref ASSIGNING FIELD-SYMBOL(<flight>). 
        members = VALUE #( BASE members ( <flight> ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD initialize. 
    cl_demo_input=>new( )->request( CHANGING field = carrier ). 
    carrier = to_upper( carrier ). 
    SELECT * FROM spfli 
             WHERE carrid = @carrier 
             INTO TABLE @flights. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[Grouping](abaploop_at_itab_group_by.md) of an internal table `flights` with [group key binding](abaploop_at_itab_group_by_binding.md). The [group key](abaploop_at_itab_group_by_key.md) of the [group loop](../../abap-glossary/abengroup_loop_glosry.md) is constructed as a structure, where the values of the columns `carrid` or `cityfrom` of each line of the internal table are assigned to the components `carrier` and `cityfr`. This creates groups of lines that have the same value in these columns. Furthermore, the components `size` and `index` are created for the special language elements `GROUP SIZE` or `GROUP INDEX` to determine the size and index of each group.

The group key that is bound to a reference variable `group_ref` and the additional components are produced in the group loop. In a [member loop](../../abap-glossary/abenmember_loop_glosry.md), the lines of each group are placed in an internal table `members` using the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) with the addition [`BASE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). This table is also displayed.

`members` could also be filled by evaluating a table comprehension using [`FOR ... IN GROUP`](abenfor_in_group.md), instead of in a [member loop](../../abap-glossary/abenmember_loop_glosry.md) [`LOOP AT GROUP`](abaploop_at_group.md):

`members = VALUE #( FOR <flight> IN GROUP group_ref ( <flight> ) ).`

The executable example for [grouping with `FOR`](abenfor_group_by_values_abexa.md) demonstrates how the entire group loop can be implemented using expressions.
