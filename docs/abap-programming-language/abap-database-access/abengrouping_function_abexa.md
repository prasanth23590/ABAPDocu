---
title: "SELECT, Grouping Function"
source_file: abengrouping_function_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Grouping Function

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the grouping function [`GROUPING`](abengrouping_function.md).

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
CLASS cl_demo_grouping_function DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_grouping_function IMPLEMENTATION. 
  METHOD main. 
    SELECT FROM sflight 
       FIELDS carrid, 
              connid, 
              planetype, 
              SUM( seatsmax ) AS sum_seatsmax, 
              grouping( carrid ) AS grouping_carrid, 
              grouping( connid ) AS grouping_connid, 
              grouping( planetype ) AS grouping_planetype 
       WHERE carrid = 'LH' 
       GROUP BY GROUPING SETS ( ( carrid, connid, planetype ), 
                                ( carrid, connid ), 
                                ( carrid, planetype ), 
                                ( connid, planetype ), 
                                ( carrid ), 
                                ( connid ), 
                                ( planetype ), 
                                ( ) ) 
       INTO TABLE @FINAL(result_grouping). 
 
    out->write( result_grouping ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

For Lufthansa flights, this example calculates the sum of the maximum available seats depending on the plane type (column `planetype`), the connection (column `connid`), and the carrier (column `carrid`).

The grouping function for the plane type column, connection column, or carrier column is used to determine whether they are part of the aggregation. The following combinations of the grouping sets are used to do this:

- `( carrid, connid, planetype )`

- `( carrid, connid )`

- `( carrid, planetype )`

- `( connid, planetype )`

- `( carrid )`

- `( connid )`

- `( planetype )`

- Empty grouping set `( )`.
