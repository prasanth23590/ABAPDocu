---
title: "Table Buffering"
source_file: abentable_buffering_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Table Buffering"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Table Buffering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the effect of [table buffering](../../abap-glossary/abentable_buffering_glosry.md).

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
CLASS cl_demo_table_buffering DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_table_buffering IMPLEMENTATION. 
  METHOD main. 
    DATA(sum1) = CONV decfloat34( 0 ). 
    DATA(sum2) = CONV decfloat34( 0 ). 
 
    "Load table buffer 
    SELECT * 
           FROM spfli 
           INTO TABLE @FINAL(result0). 
 
    DO 1000 TIMES. 
 
      FINAL(t1) = utclong_current( ). 
 
      SELECT * 
             FROM spfli 
             INTO TABLE @FINAL(result1) . 
 
      FINAL(t2) = utclong_current( ). 
 
      SELECT * 
             FROM spfli 
             INTO TABLE @FINAL(result2) 
             BYPASSING BUFFER. 
 
      FINAL(t3) = utclong_current( ). 
 
      cl_abap_utclong=>diff( EXPORTING high  = t2 
                                       low   = t1 
                             IMPORTING seconds = DATA(tdelta1) ). 
 
      cl_abap_utclong=>diff( EXPORTING high  = t3 
                                       low   = t2 
                             IMPORTING seconds = DATA(tdelta2) ). 
 
 
      sum1 += tdelta1. 
      sum2 += tdelta2. 
 
    ENDDO. 
 
    out->write( |Ratio: { sum2 / sum1 DECIMALS = 2 }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[ABAP SQL queries](../../abap-glossary/abenasql_query_glosry.md) are processed for the fully buffered DDIC database table `SPFLI`. The ratio of the execution times with and without access to the table buffer is determined and shown. Normally, accessing the data in the table buffer is considerably faster than bypassing the buffer and fetching the data from the database again and again.
