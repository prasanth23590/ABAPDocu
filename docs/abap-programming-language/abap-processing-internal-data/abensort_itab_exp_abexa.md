---
title: "Sorting Internal Tables Dynamically"
source_file: abensort_itab_exp_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > SORT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Sorting Internal Tables Dynamically

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how internal tables are sorted dynamically using an expression.

## Source Code

``` abap
* CCDEF 
CLASS cx_illegal_direction DEFINITION INHERITING FROM cx_static_check. 
ENDCLASS. 
 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_sort_itab_exp DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA itab TYPE TABLE OF string WITH EMPTY KEY. 
    METHODS sort_itab 
      IMPORTING direction TYPE string 
      RETURNING VALUE(r)  LIKE itab 
      RAISING   cx_illegal_direction. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sort_itab_exp IMPLEMENTATION. 
  METHOD main. 
    itab = VALUE #( ( `b` ) ( `a` ) ( `c` ) ). 
    TRY. 
        out->write( sort_itab( 'DOWN' ) 
          )->write( sort_itab( 'UP' ) ). 
      CATCH cx_illegal_direction. 
        RETURN. 
    ENDTRY. 
  ENDMETHOD. 
  METHOD sort_itab. 
    SORT itab BY VALUE abap_sortorder_tab( 
       ( name       = 'TABLE_LINE' 
         descending = SWITCH #( direction 
                                WHEN 'UP'   THEN ' ' 
                                WHEN 'DOWN' THEN 'X' 
                                ELSE THROW cx_illegal_direction( ) ) 
         astext     = 'X ' ) ). 
    r = itab. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `sort_itab` sorts an internal table using the statement [`SORT itab`](abapsort_itab.md), where the sort criteria are specified as a table of type `abap_sortorder_tab` constructed using the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md). The component `descending` of this table is set using a [conditional expression](../../abap-glossary/abenconditional_expression_glosry.md) with the case distinction [`SWITCH`](../abap-program-flow-logic/abenconditional_expression_switch.md), depending on the input parameter `direction`.
