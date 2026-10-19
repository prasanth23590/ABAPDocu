---
title: "itab - Loop with Key"
source_file: abenloop_at_itab_key_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, Basic Form > LOOP AT itab, cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Loop with Key

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the execution of the statement `LOOP AT itab` with different table keys.

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
CLASS cl_demo_loop_at_itab_using_key DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_at_itab_using_key IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF spfli_line, 
        carrid   TYPE spfli-carrid, 
        connid   TYPE spfli-connid, 
        cityfrom TYPE spfli-cityfrom, 
        cityto   TYPE spfli-cityto, 
      END OF spfli_line. 
 
    DATA output TYPE TABLE OF spfli_line WITH EMPTY KEY. 
 
    DATA spfli_tab TYPE HASHED TABLE 
                   OF spfli_line 
                   WITH UNIQUE KEY primary_key 
                     COMPONENTS carrid connid 
                   WITH NON-UNIQUE SORTED KEY city_from_to 
                     COMPONENTS cityfrom cityto 
                   WITH NON-UNIQUE SORTED KEY city_to_from 
                     COMPONENTS cityto cityfrom. 
 
    FIELD-SYMBOLS <spfli> LIKE LINE OF spfli_tab. 
 
    SELECT carrid, connid, cityfrom, cityto 
           FROM spfli 
           ORDER BY carrid, connid 
           INTO TABLE @spfli_tab. 
 
    CLEAR output. 
    out->next_section( 'LOOP without USING KEY' ). 
    LOOP AT spfli_tab ASSIGNING <spfli>. 
      output = VALUE #( BASE output ( <spfli> ) ). 
    ENDLOOP. 
    out->write( output ). 
 
    CLEAR output. 
    out->next_section( 'LOOP with USING KEY cityfrom cityto' ). 
    LOOP AT spfli_tab ASSIGNING <spfli> USING KEY city_from_to. 
      output = VALUE #( BASE output ( <spfli> ) ). 
    ENDLOOP. 
    out->write( output ). 
 
    CLEAR output. 
    out->next_section( 'LOOP with USING KEY cityto cityfrom' ). 
    LOOP AT spfli_tab ASSIGNING <spfli> USING KEY city_to_from. 
      output = VALUE #( BASE output ( <spfli> ) ). 
    ENDLOOP. 
    out->write( output ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `spfli_tab` is a hashed table with an unique primary key and two non-unique sorted secondary keys.

- The first `LOOP` takes place without a key specification. The table output is in the order in which the table was filled, that is, sorted by the fields specified after `ORDER BY` in the `SELECT` statement.

- The other two `LOOP` loops are performed with each of the secondary table keys `city_from_to` or `city_to_from` specified.
