---
title: "sql_cond - Subquery in WHERE Condition"
source_file: abenselect_subquery_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements > sql_cond - subquery_clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - Subquery in WHERE Condition

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a [subquery](../../abap-glossary/abensubquery_glosry.md) in a [`WHERE`](abapwhere.md) condition.

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
CLASS cl_demo_select_subquery DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_subquery IMPLEMENTATION. 
  METHOD main. 
    SELECT carrid, connid, planetype, seatsmax, 
           MAX( seatsocc ) AS seatsocc 
           FROM  sflight 
           GROUP BY carrid, connid, planetype, seatsmax 
           ORDER BY carrid, connid 
           INTO TABLE @FINAL(flights). 
 
    LOOP AT flights INTO FINAL(wa). 
      out->next_section(  |{ wa-carrid } { wa-connid }| 
        )->begin_section( |{ wa-planetype }, { 
                             wa-seatsmax  }, { wa-seatsocc  }| ). 
      SELECT planetype, seatsmax 
             FROM  saplane AS plane 
             WHERE seatsmax < @wa-seatsmax AND 
                   seatsmax >= ALL 
                     ( SELECT seatsocc 
                              FROM  sflight 
                              WHERE carrid = @wa-carrid AND 
                              connid = @wa-connid ) 
             ORDER BY seatsmax 
             INTO (@FINAL(plane), @FINAL(seats)). 
        out->write( |{ plane }, { seats }| )->end_section( ). 
      ENDSELECT. 
      IF sy-subrc <> 0. 
        out->write( 'No alternative plane types found' 
          )->end_section( ). 
      ENDIF. 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

For each flight, all alternative plane types, if available, are displayed that meet a connection and the current booking status but that have fewer seats than the current plane type.
