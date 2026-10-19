---
title: "SELECT, Grouping Sets"
source_file: abenselect_grouping_sets_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, GROUP BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Grouping Sets

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [`GROUP BY`](abapgroupby_clause.md) addition [`GROUPING SETS`](abapgrouping_sets_clause.md) of the statement [`SELECT`](abapselect.md).

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
CLASS cl_demo_select_grouping_sets DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_select_grouping_sets IMPLEMENTATION. 
  METHOD main. 
 
    "Example for GROUPING SETS 
    SELECT FROM sflight 
           FIELDS carrid, 
                  connid, 
                  planetype, 
                  SUM( seatsmax ) AS sum_seatsmax 
                  WHERE carrid = 'LH' 
           GROUP BY GROUPING SETS ( ( carrid, planetype ), 
                                    ( carrid, connid ) ) 
           ORDER BY connid, planetype 
           INTO TABLE @FINAL(result_grouping_sets). 
 
    "Example for UNION ALL 
    SELECT FROM sflight 
           FIELDS carrid, 
                  @( VALUE sflight-connid( ) ) AS connid, 
                  planetype, 
                  SUM( seatsmax ) AS sum_seatsmax 
           WHERE carrid = 'LH' 
           GROUP BY carrid, planetype 
    UNION ALL 
    SELECT FROM sflight 
           FIELDS carrid, 
                  connid, 
                  @( VALUE sflight-planetype( ) ) AS planetype, 
                  SUM( seatsmax ) AS sum_seatsmax 
           WHERE carrid = 'LH' 
           GROUP BY carrid, connid 
           ORDER BY carrid, connid, planetype, sum_seatsmax 
           INTO TABLE @FINAL(result_union). 
 
    ASSERT result_union = result_grouping_sets. 
 
    out->write( result_grouping_sets ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

For Lufthansa flights, this example calculates the sum of the maximum available seats depending on the plane type (column `planetype`) and the connection (column `connid`). Two grouping sets are defined, which contain either the plane type or the connection.

The example shows that `SELECT` statements that use [`UNION ALL`](abapunion.md) or `GROUPING SETS` are equivalent. The first [query](../../abap-glossary/abenasql_query_glosry.md) defines the grouping sets `( carrid, planetype )` and `( carrid, connid )` with a `GROUP BY` clause. The second query, on the other hand, specifies the same grouping sets using two `GROUP BY` clauses and merges them using `UNION ALL`.
