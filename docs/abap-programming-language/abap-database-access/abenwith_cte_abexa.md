---
title: "WITH, Common Table Expressions"
source_file: abenwith_cte_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, Common Table Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how common table expressions are used in the statement [`WITH`](abapwith.md).

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
CLASS cl_demo_cte DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: BEGIN OF struct, 
             carrname TYPE scarr-carrname, 
             connid   TYPE spfli-connid, 
             cityfrom TYPE spfli-cityfrom, 
             cityto   TYPE spfli-cityto, 
             cnt      TYPE int8, 
           END OF struct. 
    DATA itab TYPE TABLE OF struct WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cte IMPLEMENTATION. 
  METHOD main. 
    DATA carrid TYPE spfli-carrid VALUE 'LH'. 
    cl_demo_input=>new( )->request( CHANGING field = carrid ). 
    carrid = to_upper( carrid ). 
 
    WITH 
      +conns AS ( 
        SELECT carrname, connid, cityfrom, cityto 
              FROM spfli 
                JOIN scarr ON spfli~carrid = scarr~carrid 
              WHERE spfli~carrid = @carrid ), 
      +cnts AS ( 
        SELECT COUNT(*) AS cnt 
               FROM +conns ) 
      SELECT * 
             FROM +cnts 
               CROSS JOIN +conns 
             ORDER BY carrname, connid 
             INTO CORRESPONDING FIELDS OF TABLE @itab. 
 
    out->write( itab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A common table expression `+conns` creates a table of flight connections. A further expression, `+cnts`, determines the number of entries in the result set of `+conns`. The closing main query combines the result sets of both common table expressions using a [cross join](abapselect_join.md). This makes available the number of entries in every row of the result set of the `WITH` statement. The common table expression `+conns` is used twice in the `WITH` statement.
