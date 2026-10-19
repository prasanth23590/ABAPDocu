---
title: "itab - Key Accesses"
source_file: abenread_itab_using_key_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Key Accesses

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example measures the runtime of the statement `READ TABLE` with various table keys.

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
CLASS cl_demo_read_table_using_key DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: m    TYPE i, 
          itab TYPE STANDARD TABLE 
               OF i 
               WITH NON-UNIQUE    KEY primary_key 
                 COMPONENTS table_line 
               WITH UNIQUE SORTED KEY sorted_key 
                 COMPONENTS table_line 
               WITH UNIQUE HASHED KEY hashed_key 
                 COMPONENTS table_line 
          ##tabkey[hashed_key][sorted_key]. 
    METHODS: measure_static  IMPORTING key TYPE string, 
      measure_dynamic IMPORTING key TYPE string. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_read_table_using_key IMPLEMENTATION. 
  METHOD main. 
    DATA: n TYPE i, 
          j TYPE i. 
    DATA max TYPE i VALUE 1000. 
 
    out->begin_section( 'Accessing Internal Tables by Keys' ). 
    n = 10. 
    WHILE n <= max / 10. 
      IF n = 10. 
        m = 0. 
        j = 10. 
      ELSE. 
        m = n. 
        j = 9. 
      ENDIF. 
      DO j TIMES. 
        m += n. 
        itab = VALUE #( BASE itab FOR k = 1 UNTIL k > m ( k ) ). 
        out->line( ). 
        out->begin_section( 'Static:' ). 
        measure_static( key = `primary_key` ). 
        measure_static( key = `sorted_key`  ). 
        measure_static( key = `hashed_key`  ). 
        out->next_section( 'Dynamic:' ). 
        measure_dynamic( key = `primary_key` ). 
        measure_dynamic( key = `sorted_key`  ). 
        measure_dynamic( key = `hashed_key`  ). 
        out->end_section( ). 
        CLEAR itab. 
      ENDDO. 
      n *= 10. 
    ENDWHILE. 
  ENDMETHOD. 
  METHOD measure_dynamic. 
    DATA: t1  TYPE utclong, 
          t2  TYPE utclong, 
          t   TYPE decfloat34, 
          idx TYPE i. 
    CLEAR t. 
    DO m TIMES. 
      idx = sy-index. 
      t1 = utclong_current( ). 
      READ TABLE itab 
                 WITH TABLE KEY (key) 
                   COMPONENTS table_line = idx 
                 TRANSPORTING NO FIELDS. 
      t2 = utclong_current( ). 
      cl_abap_utclong=>diff( EXPORTING high    = t2 
                                       low   = t1 
                             IMPORTING seconds = DATA(tdelta) ). 
      t += tdelta. 
    ENDDO. 
    t /= m. 
    out->write( |{ m }   { t }| ). 
  ENDMETHOD. 
  METHOD measure_static. 
    DATA: t1  TYPE utclong, 
          t2  TYPE utclong, 
          t   TYPE decfloat34, 
          idx TYPE i. 
    CLEAR t. 
    IF key = `primary_key`. 
      DO m TIMES. 
        idx = sy-index. 
        t1 = utclong_current( ). 
        READ TABLE itab 
                   WITH TABLE KEY primary_key 
                     COMPONENTS table_line = idx 
                   TRANSPORTING NO FIELDS 
                   ##primkey[sorted_key] ##primkey[hashed_key]. 
        t2 = utclong_current( ). 
        cl_abap_utclong=>diff( EXPORTING high    = t2 
                                         low   = t1 
                               IMPORTING seconds = DATA(tdelta) ). 
        t += tdelta. 
      ENDDO. 
    ELSEIF key = `sorted_key`. 
      DO m TIMES. 
        idx = sy-index. 
        t1 = utclong_current( ). 
        READ TABLE itab 
                   WITH TABLE KEY sorted_key 
                     COMPONENTS table_line = idx 
                   TRANSPORTING NO FIELDS. 
        t2 = utclong_current( ). 
        cl_abap_utclong=>diff( EXPORTING high    = t2 
                                         low   = t1 
                               IMPORTING seconds = DATA(tdelta2) ). 
        t += tdelta2. 
      ENDDO. 
    ELSEIF key = `hashed_key`. 
      DO m TIMES. 
        idx = sy-index. 
        t1 = utclong_current( ). 
        READ TABLE itab 
                   WITH TABLE KEY hashed_key 
                     COMPONENTS table_line = idx 
                   TRANSPORTING NO FIELDS. 
        t2 = utclong_current( ). 
        cl_abap_utclong=>diff( EXPORTING high    = t2 
                                         low   = t1 
                               IMPORTING seconds = DATA(tdelta3) ). 
        t += tdelta3. 
      ENDDO. 
    ENDIF. 
    t /= m. 
    out->write( |{ m }   { t }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `itab` is a standard table with a non-unique primary key, a unique secondary sorted key, and a unique secondary hash key. For demonstration purposes, this class hides the syntax warning that different table keys in an internal table cannot contain the same components using the [pragma](../../abap-glossary/abenpragma_glosry.md) `##TABKEY`.

The class measures the average access time of the statement `READ TABLE` to individual table lines, depending on the number of lines in the table. The lines are accessed using the different keys. The keys are specified statically in the method `measure_static` and dynamically in the method `measure_dynamic`.

The result demonstrates that the response times for static access are as expected from around 50 to 100 table lines:

- When a standard table is accessed using the primary key, the average access time increases linearly with the number of table lines.

- When a standard table is accessed using a secondary sorted key, the average access time increases logarithmically with the number of table lines.

- When a standard table is accessed using a secondary hash key, the access time is constant.

In dynamic accesses, each access incurs the additional time required to evaluate the dynamically specified key.
