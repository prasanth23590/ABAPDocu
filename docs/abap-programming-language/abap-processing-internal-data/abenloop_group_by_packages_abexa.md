---
title: "itab - Grouping with LOOP in Packages"
source_file: abenloop_group_by_packages_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP in Packages

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a construction of the group key that does not depend on the line content.

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
CLASS cl_demo_loop_grp_by_packages DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA 
      itab TYPE TABLE OF decfloat34 WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_packages IMPLEMENTATION. 
  METHOD main. 
 
    DATA(n) = 10. 
    cl_demo_input=>new( 
     )->request( EXPORTING text  = `Package size` 
                 CHANGING  field = n ). 
    IF n <= 0. 
      RETURN. 
    ENDIF. 
 
    out->begin_section( |Packages of { n }| ). 
    DATA group LIKE itab. 
    LOOP AT itab INTO FINAL(wa) 
         GROUP BY ( sy-tabix - 1 ) DIV n + 1. 
      CLEAR group. 
      LOOP AT GROUP wa ASSIGNING FIELD-SYMBOL(<wa>). 
        group = VALUE #( BASE group ( <wa> ) ). 
      ENDLOOP. 
      out->write( group ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    itab = VALUE #( FOR j = 1 UNTIL j > 100 ( 1 / j ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[Grouping](abaploop_at_itab_group_by.md) of an internal table `text` with [representative binding](abaploop_at_itab_group_by_binding.md). The [group key](abaploop_at_itab_group_by_key.md) of the [group loop](../../abap-glossary/abengroup_loop_glosry.md) is constructed as a value of the type `i`, which is calculated from the line index of the current line in `sy-tabix`. This creates groups of lines with the same definable size.

In the group loop, the lines of each group are placed in an internal table `group` in a [member loop](../../abap-glossary/abenmember_loop_glosry.md) using the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) with the addition [`BASE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). This table is also displayed. Here, the group is addressed using the work area `wa` of the original output behavior of the `LOOP` due to the representative binding.

`group` could also be filled by the evaluation of a table comprehension using [`FOR ... IN GROUP`](abenfor_in_group.md), instead of in a [member loop](../../abap-glossary/abenmember_loop_glosry.md) [`LOOP AT GROUP`](abaploop_at_group.md):

`group = VALUE #( FOR <wa> IN GROUP wa ( <wa> ) ).`

The executable example for [grouping with `FOR`](abenfor_group_by_packages_abexa.md) demonstrates how the entire group loop can be implemented using expressions.
