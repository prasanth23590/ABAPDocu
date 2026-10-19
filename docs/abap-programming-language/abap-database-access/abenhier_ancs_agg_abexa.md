---
title: "SELECT, Hierarchy Navigator HIERARCHY_ANCESTORS_AGGREGATE"
source_file: abenhier_ancs_agg_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy_navigator > SELECT, FROM hierarchy_aggregate_navigator > SELECT, hierarchy_ancestors_aggregate"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Hierarchy Navigator HIERARCHY_ANCESTORS_AGGREGATE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the hierarchy navigator `HIERARCHY_ANCESTORS_AGGREGATE`.

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
CLASS cl_demo_hrrchy_ancestors_agg DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS fill_table. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_hrrchy_ancestors_agg IMPLEMENTATION. 
  METHOD main. 
    DATA(start_id) = 'A '. 
    DATA(end_id1)  = 'F1'. 
    DATA(end_id2)  = 'D2'. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = start_id 
      )->add_field( CHANGING field = end_id1 
      )->request(   CHANGING field = end_id2 ). 
 
    fill_table( ). 
 
    SELECT * 
           FROM HIERARCHY( 
             SOURCE demo_cds_parent_child_src_agg 
             CHILD TO PARENT ASSOCIATION _relat 
             START WHERE id = 'A' 
             SIBLINGS ORDER BY id ) 
           INTO TABLE @FINAL(hierarchy). 
    out->write( hierarchy ). 
 
    SELECT FROM HIERARCHY_ANCESTORS_AGGREGATE( 
                  SOURCE HIERARCHY( 
                    SOURCE demo_cds_parent_child_src_agg 
                    CHILD TO PARENT ASSOCIATION _relat 
                    START WHERE id = 'A' 
                    SIBLINGS ORDER BY id ) 
                  START WHERE id <= @start_id 
                  MEASURES COUNT(*) AS cnt, 
                           AVG( num ) AS avg, 
                           MIN( num ) AS min, 
                           MAX( num ) AS max, 
                           SUM( num ) AS sum, 
                           PRODUCT( num ) AS prod, 
                           STRING_AGG( id, '-' ) AS strg_agg 
                  WHERE id = @end_id1 OR 
                        id = @end_id2 ) AS agg 
           FIELDS id, 
                  cnt, avg, min, max, sum, prod, strg_agg 
           INTO TABLE @FINAL(asql_hiera_ancestors_aggregate). 
 
    SELECT FROM HIERARCHY_ANCESTORS_AGGREGATE( 
                  SOURCE demo_cds_parent_child_agg( p_id = 'A' ) 
                  START WHERE id <= @start_id 
                  MEASURES COUNT(*) AS cnt, 
                           AVG( num ) AS avg, 
                           MIN( num ) AS min, 
                           MAX( num ) AS max, 
                           SUM( num ) AS sum, 
                           PRODUCT( num ) AS prod, 
                           STRING_AGG( id, '-' ) AS strg_agg 
                  WHERE id = @end_id1 OR 
                        id = @end_id2 ) AS agg 
           FIELDS id, 
                  cnt, avg, min, max, sum, prod, strg_agg 
           INTO TABLE @FINAL(cds_hiera_ancestors_aggregate). 
 
    ASSERT 
      cds_hiera_ancestors_aggregate = asql_hiera_ancestors_aggregate. 
 
    DELETE FROM demo_parchld_agg. "GTT! 
 
    out->write( asql_hiera_ancestors_aggregate ). 
  ENDMETHOD. 
  METHOD fill_table. 
    INSERT demo_parchld_agg FROM TABLE @( VALUE #( 
            ( cnt = 1 id = 'A'   parent_id = ' '  num = 1 ) 
            ( cnt = 2 id = 'B'   parent_id = 'A'  num = 2 ) 
            ( cnt = 3 id = 'C'   parent_id = 'B'  num = 3 ) 
            ( cnt = 4 id = 'D1'  parent_id = 'C'  num = 4 ) 
            ( cnt = 5 id = 'E1'  parent_id = 'D1' num = 5 ) 
            ( cnt = 6 id = 'F1'  parent_id = 'E1' num = 6 ) 
            ( cnt = 7 id = 'D2'  parent_id = 'C'  num = 4 ) 
            ( cnt = 8 id = 'E2'  parent_id = 'D2' num = 5 ) 
            ( cnt = 9 id = 'F2'  parent_id = 'E2' num = 6 ) 
            ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Calls of the hierarchy navigator [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md). If the example is executed with the predefined input values, the result set contains two rows, representing paths from a start node with the ID *A* to two hierarchy nodes with the IDs `F1` and `D2`. The paths are highlighted as a result of the aggregate function `STRING_AGG`.

If the input value for the start node is raised, further start nodes are added by the comparison operator after `START WHERE` and hence further rows are added to the result set. In this example, the aggregated paths can be taken from the last column, however there is currently no way of interpreting the start node from the hierarchy columns.
