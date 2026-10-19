---
title: "itab - Grouping with LOOP in Group Levels"
source_file: abenloop_group_by_levels_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP in Group Levels

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates simple group level processing using [`GROUP BY`](abaploop_at_itab_group_by.md).

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
CLASS cl_demo_loop_grp_by_levels DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: BEGIN OF line, 
             col1 TYPE c LENGTH 1, 
             col2 TYPE i, 
             col3 TYPE i, 
           END OF line. 
    METHODS sum IMPORTING line       TYPE line 
                                base       TYPE line 
                      RETURNING VALUE(sum) TYPE line. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_levels IMPLEMENTATION. 
  METHOD main. 
 
    DATA itab TYPE HASHED TABLE OF line 
              WITH UNIQUE KEY col1 col2. 
 
    itab = VALUE #( 
      FOR j = 1 UNTIL j > 3 
       ( col1 = 'A' 
         col2 = j 
         col3 = j ** 2 ) 
       ( col1 = 'B' 
         col2 = 2 * j 
         col3 = ( 2 * j ) ** 2 ) ). 
 
    out->write( itab )->line( ). 
 
    DATA sum   TYPE line. 
    DATA total TYPE line. 
    DATA group LIKE itab. 
    LOOP AT itab ASSIGNING FIELD-SYMBOL(<line>) 
                 GROUP BY <line>-col1 ASCENDING. 
      CLEAR sum. 
      CLEAR group. 
      LOOP AT GROUP <line> INTO FINAL(line). 
        group = VALUE #( BASE group ( line ) ). 
        sum = sum( EXPORTING line = line 
                             base = sum ). 
      ENDLOOP. 
      out->write( group )->line( )->write( sum )->line( ). 
      total = sum( EXPORTING line = sum 
                             base = total ). 
    ENDLOOP. 
    total-col1 = '*'. 
    out->line( )->write( total ). 
  ENDMETHOD. 
  METHOD sum. 
    sum = VALUE #( BASE base 
                   col1 = line-col1 
                   col2 = sum-col2 + line-col2 
                   col3 = sum-col3 + line-col3 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the executable example for group level processing. Here, the group key is constructed explicitly using the value of the column `col1` and, unlike in group level processing, does not depend on the structure of the table and its sorting.

The statement `SUM` is replaced by a functional method that replaces the implicit behavior of the statement with an explicit and self-definable function.

`group` and `sum` could also be filled by the evaluation of a table comprehension or table reduction using [`FOR ... IN GROUP`](abenfor_in_group.md), instead of in a [member loop](../../abap-glossary/abenmember_loop_glosry.md) [`LOOP AT GROUP`](abaploop_at_group.md):

``` abap
sum = REDUCE #( INIT s = VALUE line( ) 
                FOR line IN GROUP <line> 
                NEXT s = sum( EXPORTING line = line 
                                        base = s ) ). 
group = #( FOR <wa> IN GROUP <line> ( <wa> ) ).
```

The executable example for [grouping with `FOR`](abenfor_group_by_levels_abexa.md) demonstrates how the entire group loop can be implemented using expressions.
