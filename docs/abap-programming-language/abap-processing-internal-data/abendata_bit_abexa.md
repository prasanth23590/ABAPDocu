---
title: "bit_exp - Bit Operations"
source_file: abendata_bit_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing > Bit Expressions (bit_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# bit_exp - Bit Operations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how bit operators are used.

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
CLASS cl_demo_data_bit DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_data_bit IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: BEGIN OF t_spfli, 
             carrid   TYPE spfli-carrid, 
             cityfrom TYPE spfli-cityfrom, 
           END OF t_spfli. 
 
    DATA: frankfurt TYPE x LENGTH 4, 
          frisco    TYPE x LENGTH 4, 
          intersect TYPE x LENGTH 4, 
          union     TYPE x LENGTH 4, 
          bit       TYPE i, 
          spflitab  TYPE TABLE OF t_spfli, 
          wa        TYPE t_spfli, 
          carrid    TYPE t_spfli-carrid, 
          carrier   LIKE SORTED TABLE OF carrid 
                                WITH UNIQUE KEY table_line. 
 
 
    SELECT carrid FROM scarr INTO TABLE @carrier. 
 
    SELECT carrid, cityfrom 
           FROM spfli 
           INTO CORRESPONDING FIELDS OF TABLE @spflitab. 
 
    out->begin_section( 
      'Airlines with departure cities' 
      )->write_data( spflitab 
      )->end_section( ). 
 
    LOOP AT spflitab INTO wa. 
 
      READ TABLE carrier FROM wa-carrid TRANSPORTING NO FIELDS. 
 
      CASE wa-cityfrom. 
        WHEN 'FRANKFURT'. 
          SET BIT sy-tabix OF frankfurt. 
        WHEN 'SAN FRANCISCO'. 
          SET BIT sy-tabix OF frisco. 
      ENDCASE. 
 
    ENDLOOP. 
 
    intersect = frankfurt BIT-AND frisco. 
    union     = frankfurt BIT-OR  frisco. 
 
    out->begin_section( 
      'Airlines flying from Frankfurt and San Francisco' ). 
    DO 32 TIMES. 
      GET BIT sy-index OF intersect INTO bit. 
      IF bit = 1. 
        carrid = carrier[ sy-index ]. 
        out->write( |{ carrid }| ). 
      ENDIF. 
    ENDDO. 
 
    out->next_section( 
      'Airlines flying from Frankfurt or San Francisco' ). 
    DO 32 TIMES. 
      GET BIT sy-index OF union INTO bit. 
      IF bit = 1. 
        carrid = carrier[ sy-index ]. 
        out->write( |{ carrid }| ). 
      ENDIF. 
    ENDDO. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `main` works with four hexadecimal fields of length 4, namely `frankfurt`, `frisco`, `intersect`, and `union`. These fields can represent sets with a maximum of 32 elements. Here, the basic set is supposed to be the set of all possible airlines from the database table `SCARR`. Each bit of the corresponding bit sequence represents an airline. To index the airlines, an internal table `carrier` is created and filled with the abbreviations for the airlines from `SCARR`. An airline is identified using the internal index of the table `carrier`.

Depending on the departure city, the `SELECT` loop across the database table `SPFLI` sets the bit at the position that matches the line number of the airline in the table `carrier`, in either in the `frankfurt` field or in the `frisco` field. For this purpose, the line number `sy-tabix` is determined using a `READ` statement, in which no other fields are transported.

Using the bit operations `BIT-AND` and `BIT-OR`, the intersection and union of `frankfurt` and `frisco` are created.

In the two `DO` loops, the bits from `intersect` and `union` are read and evaluated individually. For every set position, the airline abbreviations are read from the table `carrier` using a `READ` statement.
