---
title: "SELECT, Hierarchy Navigator HIERARCHY_DESCENDANTS_AGGREGATE"
source_file: abenhier_desc_agg_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy_navigator > SELECT, FROM hierarchy_aggregate_navigator > SELECT, FROM hierarchy_descendants_aggregate"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Hierarchy Navigator HIERARCHY_DESCENDANTS_AGGREGATE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the hierarchy navigator `HIERARCHY_DESCENDANTS_AGGREGATE` with the addition `JOIN`.

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
CLASS cl_demo_hrrchy_descendants_agg DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS fill_table. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_hrrchy_descendants_agg IMPLEMENTATION. 
  METHOD main. 
    DATA(level) = 2. 
    cl_demo_input=>new( )->request( CHANGING field = level ). 
 
    DATA itab TYPE SORTED TABLE OF demo_child_num 
              WITH NON-UNIQUE KEY client id. 
 
    fill_table( ). 
 
    SELECT FROM demo_cds_parent_child( p_id = 'A' ) 
           FIELDS id, 
                  parent, 
                  hierarchy_level 
           INTO TABLE @FINAL(hierarchy). 
    out->write( hierarchy ). 
 
    out->line( ). 
 
    SELECT FROM demo_cds_parent_child( p_id = 'A' ) AS h 
             LEFT OUTER JOIN demo_child_num AS j 
               ON j~id = h~id 
           FIELDS h~id, 
                  h~parent, 
                  j~num, 
                  h~hierarchy_level 
           INTO TABLE @DATA(hierarchy_joined). 
    out->write( hierarchy_joined ). 
 
    SELECT agg~* 
           FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
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
                  WHERE hierarchy_level <= @level ) AS agg 
           INTO TABLE @DATA(asql_hierarchy_desc_aggregate). 
    out->write( asql_hierarchy_desc_aggregate ). 
 
    SELECT agg~* 
           FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
                  SOURCE demo_cds_parent_child( p_id = 'A' ) AS h 
                  JOIN demo_child_num AS j 
                    ON j~id = h~id 
                  MEASURES MIN( j~num ) AS min, 
                           MAX( j~num ) AS max, 
                           SUM( j~num ) AS sum, 
                           COUNT( j~num ) AS cnt 
                  WHERE hierarchy_level <= @level ) AS agg 
           INTO TABLE @DATA(cds_hierarchy_desc_aggregate). 
    ASSERT 
      cds_hierarchy_desc_aggregate = asql_hierarchy_desc_aggregate. 
 
    out->line( ). 
 
    SELECT * 
           FROM demo_child_num 
           INTO TABLE @itab.                            "#EC CI_NOWHERE 
    itab = VALUE #( BASE itab 
      ( client = sy-mandt id = 'A ' num = -1     ) 
      ( client = sy-mandt id = 'BC' num = 10000  ) 
      ( client = sy-mandt id = 'BD' num = 100000 ) 
      ( client = sy-mandt id = 'BD' num = 200000 ) 
      ( client = sy-mandt id = 'BD' num = 300000 ) ). 
 
    SELECT FROM demo_cds_parent_child( p_id = 'A' ) AS h 
             LEFT OUTER JOIN @itab AS j 
               ON j~id = h~id 
           FIELDS h~id, 
                  h~parent, 
                  j~num, 
                  h~hierarchy_level 
           INTO TABLE @hierarchy_joined. 
    out->write( hierarchy_joined ). 
 
    SELECT agg~* 
           FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
                  SOURCE HIERARCHY( 
                           SOURCE demo_cds_parent_child_source 
                           CHILD TO PARENT ASSOCIATION _relat 
                           START WHERE id = 'A' 
                           SIBLINGS ORDER BY id ) AS h 
                  JOIN @itab AS j 
                    ON j~id = h~id 
                  MEASURES MIN( j~num ) AS min, 
                           MAX( j~num ) AS max, 
                           SUM( j~num ) AS sum, 
                           COUNT( j~num ) AS cnt 
                  WHERE hierarchy_level <= @level ) AS agg 
           INTO TABLE @asql_hierarchy_desc_aggregate. 
    out->write( asql_hierarchy_desc_aggregate ). 
 
    SELECT agg~* 
           FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
                  SOURCE demo_cds_parent_child( p_id = 'A' ) AS h 
                  JOIN @itab AS j 
                    ON j~id = h~id 
                  MEASURES MIN( j~num ) AS min, 
                           MAX( j~num ) AS max, 
                           SUM( j~num ) AS sum, 
                           COUNT( j~num ) AS cnt 
                  WHERE hierarchy_level <= @level ) AS agg 
           INTO TABLE @cds_hierarchy_desc_aggregate. 
    ASSERT 
      cds_hierarchy_desc_aggregate = asql_hierarchy_desc_aggregate. 
 
    DELETE FROM demo_parent_chld. "GTT! 
    DELETE FROM demo_child_num.   "GTT! 
 
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
            ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Calls of the hierarchy navigator [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_agg_navis.md) where the [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) `DEMO_CDS_PARENT_CHILD` specified as a source is joined with a DDIC database table `DEMO_CHILD_NUM` and an internal table [`@itab`](abapselect_itab.md) using the addition `JOIN`. The aggregate functions evaluate the column `NUM` of the joined data sources. The results of the join expressions used are also displayed.

- In the first part, the table `DEMO_CHILD_NUM` is filled to produce a 1:1 relationship between the rows of the hierarchy and its own rows. The result of the hierarchy navigator is the same as in the executable example `CL_DEMO_HIERARCHY_AGGREGATE`, but here the number values are taken from the joined table.

- In the second part, the internal table `@itab` contains the rows of the DDIC database table `DEMO_CHILD_NUM` and further rows that also match the criteria for descendant nodes for nodes of the hierarchy. This example shows how these additional rows, produced in the result set of the join, are evaluated in the aggregate functions.

The statement [`ASSERT`](../abap-program-maintenance/abapassert.md) shows that the use of the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md) and a semantically identical [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) as the source of the hierarchy navigator produces the same results.
