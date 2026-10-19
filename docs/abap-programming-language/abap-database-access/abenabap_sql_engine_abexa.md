---
title: "ABAP SQL In-Memory Engine, Multiple Internal Tables"
source_file: abenabap_sql_engine_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - ABAP SQL In-Memory Engine > ABAP SQL In-Memory Engine, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL In-Memory Engine, Multiple Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the access to multiple internal tables with the ABAP SQL in-memory engine.

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
CLASS cl_demo_abap_sql_engine DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_abap_sql_engine IMPLEMENTATION. 
  METHOD main. 
 
    SELECT * FROM scarr   INTO TABLE @FINAL(scarr_tab). 
    SELECT * FROM spfli   INTO TABLE @FINAL(spfli_tab). 
 
    WITH 
      +cte AS ( SELECT 
                  FROM scarr 
                  FIELDS carrid ) 
    SELECT 
      FROM +cte AS scarr 
        INNER JOIN spfli 
          ON scarr~carrid = spfli~carrid 
      FIELDS 
        scarr~carrid, 
        spfli~connid 
      ORDER BY scarr~carrid, spfli~connid 
      INTO TABLE @FINAL(result1). 
 
    WITH 
      +cte AS ( SELECT 
                  FROM @scarr_tab AS scarr 
                  FIELDS carrid ) 
      SELECT 
        FROM +cte AS scarr 
        INNER JOIN @spfli_tab AS spfli 
          ON scarr~carrid = spfli~carrid 
      FIELDS 
        scarr~carrid, 
        spfli~connid 
      ORDER BY scarr~carrid, spfli~connid 
      INTO TABLE @FINAL(result2). 
 
    IF result1 = result2. 
      out->write( 'result1 equals result2' ). 
    ELSE. 
      out->write( 'result1 does not equal result2' ). 
    ENDIF. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example shows that reading from database tables and reading from internal tables with the same content yield the same results. While the database tables are accessed on the database, the `WITH` statement for the internal tables can be processed on the AS ABAP since none of the restrictions listed under [ABAP SQL In-Memory Engine, Restrictions](abensql_engine_restr.md) occur.
