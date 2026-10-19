---
title: "SELECT, Hierarchy Navigator HIERARCHY_DESCENDANTS_AGGREGATE with WITH"
source_file: abenhier_desc_agg_with_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy_navigator > SELECT, FROM hierarchy_aggregate_navigator > SELECT, FROM hierarchy_descendants_aggregate"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Hierarchy Navigator HIERARCHY_DESCENDANTS_AGGREGATE with WITH

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the hierarchy navigator `HIERARCHY_DESCENDANTS_AGGREGATE` with the addition `JOIN` and the addition `WITH`.

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
CLASS cl_demo_hrrchy_desc_with DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS fill_table. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_hrrchy_desc_with IMPLEMENTATION. 
  METHOD main. 
    DATA(level) = 3. 
    cl_demo_input=>new( )->request( CHANGING field = level ). 
 
    fill_table( ). 
 
    SELECT FROM demo_cds_parent_child( p_id = 'A' ) AS h 
                  RIGHT OUTER JOIN demo_child_num AS j 
                    ON j~id = h~id 
           FIELDS 
              coalesce( CAST( h~id AS CHAR( 4 ) ), 
                        'Null' ) AS id, 
              coalesce( CAST( h~parent AS CHAR( 4 ) ), 
                        'Null' ) AS parent, 
              coalesce( CAST( hierarchy_level AS CHAR( 20 ) ), 
                        'Null' ) AS hierachy_level, 
              j~num AS num 
           INTO TABLE @FINAL(joined_hierarchy) ##no_text. 
    out->write( joined_hierarchy ). 
 
    SELECT FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
                  SOURCE HIERARCHY( 
                           SOURCE demo_cds_parent_child_source 
                           CHILD TO PARENT ASSOCIATION _relat 
                           START WHERE id = 'A' 
                           SIBLINGS ORDER BY id ) AS h 
                  JOIN demo_child_num AS j 
                    ON j~id = h~id 
                  MEASURES MIN( j~num ) AS min, 
                           MAX( j~num ) AS max, 
                           SUM( j~num ) AS sum, 
                           COUNT( j~num ) AS cnt 
                  WHERE hierarchy_level >= @level 
              WITH SUBTOTAL 
              WITH BALANCE 
              WITH NOT MATCHED 
              WITH TOTAL ) AS agg 
            FIELDS 
              coalesce( CAST( id AS CHAR( 4 ) ), 
                        'Null' ) AS id, 
              coalesce( CAST( parent AS CHAR( 4 ) ), 
                        'Null' ) AS parent, 
              coalesce( CAST( hierarchy_level AS CHAR( 20 ) ), 
                        'Null' ) AS hierachy_level, 
              coalesce( CAST( hierarchy_aggregate_type AS CHAR( 4 ) ), 
                        'Null' ) AS hierarchy_aggregate_type, 
              min, 
              max, 
              sum, 
              cnt 
           INTO TABLE @FINAL(asql_hierarchy_desc_aggregate) ##no_text. 
 
    SELECT FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
                  SOURCE demo_cds_parent_child( p_id = 'A' ) AS h 
                  JOIN demo_child_num AS j 
                    ON j~id = h~id 
                  MEASURES MIN( j~num ) AS min, 
                           MAX( j~num ) AS max, 
                           SUM( j~num ) AS sum, 
                           COUNT( j~num ) AS cnt 
                  WHERE hierarchy_level >= @level 
              WITH SUBTOTAL 
              WITH BALANCE 
              WITH NOT MATCHED 
              WITH TOTAL ) AS agg 
            FIELDS 
              coalesce( CAST( id AS CHAR( 4 ) ), 
                        'Null' ) AS id, 
              coalesce( CAST( parent AS CHAR( 4 ) ), 
                        'Null' ) AS parent, 
              coalesce( CAST( hierarchy_level AS CHAR( 20 ) ), 
                        'Null' ) AS hierachy_level, 
              coalesce( CAST( hierarchy_aggregate_type AS CHAR( 4 ) ), 
                        'Null' ) AS hierarchy_aggregate_type, 
              min, 
              max, 
              sum, 
              cnt 
           INTO TABLE @FINAL(cds_hierarchy_desc_aggregate) ##no_text. 
 
    ASSERT 
      cds_hierarchy_desc_aggregate = asql_hierarchy_desc_aggregate. 
 
    DELETE FROM demo_parent_chld. "GTT! 
    DELETE FROM demo_child_num.   "GTT! 
 
    out->write( asql_hierarchy_desc_aggregate ). 
  ENDMETHOD. 
  METHOD fill_table. 
    INSERT demo_parent_chld FROM TABLE @( VALUE #( 
            ( cnt = 1 id = 'A'   parent_id = ' '  ) 
            ( cnt = 2 id = 'AA'  parent_id = 'A'  ) 
            ( cnt = 3 id = 'AB'  parent_id = 'A'  ) 
            ( cnt = 4 id = 'AC'  parent_id = 'A'  ) 
            ( cnt = 5 id = 'BA'  parent_id = 'AB' ) 
            ( cnt = 6 id = 'BB'  parent_id = 'AB' ) 
            ( cnt = 7 id = 'BC'  parent_id = 'AB' ) 
            ( cnt = 8 id = 'BD'  parent_id = 'AB' ) 
            ) ). 
 
    INSERT demo_child_num FROM TABLE @( VALUE #( 
            ( id = 'A'  num = 0   ) 
            ( id = 'AA' num = 10  ) 
            ( id = 'AB' num = 20  ) 
            ( id = 'AC' num = 30  ) 
            ( id = 'BA' num = 100 ) 
            ( id = 'BB' num = 200 ) 
            ( id = 'BC' num = 300 ) 
            ( id = 'BD' num = 400 ) 
            ( id = 'CA' num = 4000 ) 
            ( id = 'CB' num = 5000 ) 
            ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates the way the different `WITH` additions work in the hierarchy navigator [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md). The source is a hierarchy joined with another data source by the `JOIN` addition. Before the function is called, the result set of a join is produced containing all rows to which the `WITH` additions are applied. Depending on the value entered for the host variable `level` used in the `WHERE` condition, the additions `WITH SUBTOTAL` and `WITH BALANCE` return different results. The results of `WITH NOT MATCHED` and `WITH TOTAL` are independent of `level`.

The function [`COALESCE`](abensql_coalesce.md) is used here to highlight the null values in the output. If this function is not used, the null values are converted to type-dependent initial values and hence cannot be detected as null values.
