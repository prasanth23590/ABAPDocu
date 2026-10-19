---
title: "itab - READ WHERE Versus WITH KEY"
source_file: abenread_itab_where_key_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - READ WHERE Versus WITH KEY

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example measures the runtime of the statement `READ TABLE` with a `WHERE` condition and an equivalent `WITH KEY` addition..

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
CLASS cl_demo_read_table_where_key DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_read_table_where_key IMPLEMENTATION. 
  METHOD main. 
 
    SELECT * 
           FROM sbook 
           ORDER BY carrid 
           INTO TABLE @FINAL(itab).                     "#EC CI_NOWHERE 
 
    IF line_exists( itab[ carrid = 'UA' ] ). 
 
      FINAL(t1) = utclong_current( ). 
      READ TABLE itab 
           ASSIGNING FIELD-SYMBOL(<fs2>) 
           WITH KEY carrid = 'UA'. 
      FINAL(idx1) = sy-tabix. 
      FINAL(t2) = utclong_current( ). 
 
      FINAL(t3) = utclong_current( ). 
      READ TABLE itab 
           ASSIGNING FIELD-SYMBOL(<fs1>) 
           WHERE carrid = 'UA' ##READ_WHERE_OK. 
      FINAL(idx2) = sy-tabix. 
      FINAL(t4) = utclong_current( ). 
 
      FINAL(t5) = utclong_current( ). 
      LOOP AT itab 
           ASSIGNING FIELD-SYMBOL(<fs3>) 
           WHERE carrid = 'UA'. 
        FINAL(idx3) = sy-tabix. 
        EXIT. 
      ENDLOOP. 
      FINAL(t6) = utclong_current( ). 
 
      ASSERT idx1  = idx2. 
      ASSERT idx2  = idx3. 
      ASSERT <fs1> = <fs2>. 
      ASSERT <fs2> = <fs3>. 
 
      cl_abap_utclong=>diff( EXPORTING high    = t2 
                                       low   = t1 
                             IMPORTING seconds = DATA(tdelta1) ). 
 
      cl_abap_utclong=>diff( EXPORTING high    = t4 
                                       low   = t3 
                             IMPORTING seconds = DATA(tdelta2) ). 
 
      cl_abap_utclong=>diff( EXPORTING high    = t6 
                                       low   = t5 
                             IMPORTING seconds = DATA(tdelta3) ). 
 
      out->write( |{ tdelta1 }\n{ tdelta2 }\n{ tdelta3 }| ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The internal table `itab` is filled with data and the first line of a set of lines is searched that is located pretty much at the bottom of the table. The example shows that searching with a [`WHERE`](abapread_table_where.md) condition is not as fast as searching with the [`WITH KEY`](abapread_table_free.md) addition. Because of that, the pragma `##read_where_ok` must be used.

Additionally, the same functionality is implemented with [`LOOP AT`](abaploop_at_itab.md) combined with [`EXIT`](../abap-calling-and-exiting-program-units/abapexit_loop.md). The performance of `LOOP ... WHERE` and `READ WHERE` are about the same. `READ WHERE` provides an easier to use syntax but no performance gain.
