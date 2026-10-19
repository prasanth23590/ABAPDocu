---
title: "itab - Grouping with LOOP and Sort"
source_file: abenloop_group_by_sort_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP and Sort

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how groupings are used for sorts.

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
CLASS cl_demo_loop_grp_by_sort DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_sort IMPLEMENTATION. 
  METHOD main. 
    TYPES itab TYPE STANDARD TABLE OF string WITH EMPTY KEY. 
 
    FINAL(itab) = 
      VALUE itab( ( `d` ) ( `B` ) ( `D` ) ( `b` ) ( `a` ) 
                  ( `D` ) ( `a` ) ( `C` ) ( `A` ) ( `c` ) ). 
    out->write( itab ). 
 
    DATA jtab TYPE itab. 
    LOOP AT itab ASSIGNING FIELD-SYMBOL(<line>) 
                 GROUP BY to_upper( <line> ) ASCENDING 
                 ASSIGNING FIELD-SYMBOL(<grp1>). 
      LOOP AT GROUP <grp1> ASSIGNING FIELD-SYMBOL(<mbr1>) 
              GROUP BY <mbr1> DESCENDING 
              ASSIGNING FIELD-SYMBOL(<grp2>). 
        jtab = VALUE #( BASE jtab 
                        FOR <mbr2> IN GROUP <grp2> ( <mbr2> ) ). 
      ENDLOOP. 
    ENDLOOP. 
    out->write( jtab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In this example, the additions `ASCENDING` and `DESCENDING` of [`GROUP BY`](abaploop_at_itab_group_by.md) are used to sort a character-like table first while ignoring case and then sort within the groups to separate uppercase from lowercase. A further [executable example](abenfor_group_by_sort_abexa.md) shows how the `LOOP` statements can be replaced by a single expression.
