---
title: "itab - Table Comprehensions, Use of Step Size"
source_file: abentable_cmprhnsns_step_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Comprehensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Comprehensions, Use of Step Size

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the step size and the processing order are used in [table comprehensions](../../abap-glossary/abentable_comprehension_glosry.md).

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
CLASS cl_demo_table_comprh_step DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_table_comprh_step IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: BEGIN OF line, 
             tabix TYPE sy-tabix, 
             value TYPE i, 
           END OF line. 
    DATA output TYPE TABLE OF line WITH EMPTY KEY. 
 
    out->write_doc( 
      `An internal table itab is declared and filled as follows:` 
      )->begin_code( `itab` ). 
 
    DATA itab TYPE STANDARD TABLE OF i 
         WITH EMPTY KEY 
         WITH UNIQUE SORTED KEY sortkey COMPONENTS table_line. 
 
    itab = VALUE #( FOR i = 1 UNTIL i > 20 ( i ) ). 
 
    out->end_code( `itab` ). 
 
    SORT itab BY table_line DESCENDING. 
 
    output = VALUE #( FOR <fs> IN itab INDEX INTO tabix FROM 4 TO 16 
      STEP 2 ( tabix = tabix value = <fs> ) ). 
    out->next_section( `FOR STEP 2` )->write( output ). 
    CLEAR output. 
 
    output = VALUE #( FOR <fs> IN itab INDEX INTO tabix 
      USING KEY sortkey FROM 4 TO 16 STEP 2 
            ( tabix = tabix value = <fs> ) ). 
    out->next_section( `FOR STEP 2 USING KEY sortkey` 
      )->write( output ). 
    CLEAR output. 
 
    output = VALUE #( FOR <fs> IN itab INDEX INTO tabix 
      USING KEY sortkey FROM 16 TO 4 STEP -2 
            ( tabix = tabix value = <fs> ) ). 
    out->next_section( `FOR STEP -2 USING KEY sortkey` 
      )->write( output ). 
    CLEAR output. 
 
    output = VALUE #( FOR <fs> IN itab INDEX INTO tabix FROM 16 TO 4 
      STEP -2 ( tabix = tabix value = <fs> ) ). 
    out->next_section( `FOR STEP -2` )->write( output ). 
    CLEAR output. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The content of an internal table `itab` is defined by using the additions `STEP` and `USING KEY`.

1.  Every second table line is read in descending order based on the `STEP` statement, starting at the fourth table line from last because of the `FROM` addition.

2.  Every second table line is read in ascending order based on the `USING KEY` and `STEP` statement, starting at the fourth first table line because of the `FROM` addition.

3.  Every second table line is read in descending order based on the `USING KEY` and `STEP` statement, starting at the fifth table line from last because of the `FROM` addition.

4.  Every second table line is read in ascending order based on the `STEP` statement, starting at the fifth first table line because of the `FROM` addition.

See also the [executable example](abenloop_at_itab_step_abexa.md) for the `LOOP` statement using the addition `STEP`.
