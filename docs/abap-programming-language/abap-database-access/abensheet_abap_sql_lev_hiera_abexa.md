---
title: "ABAP SQL - Level-based Hierarchy of Flight Data"
source_file: abensheet_abap_sql_lev_hiera_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy > SELECT, FROM HIERARCHY > SELECT, FROM HIERARCHY, LEVELS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Level-based Hierarchy of Flight Data

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example generates a [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) from flight model data.

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
CLASS cl_demo_sql_leveled_hierarchy DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_leveled_hierarchy IMPLEMENTATION. 
  METHOD main. 
 
    WITH +flights AS ( 
         SELECT FROM scarr AS s 
                  INNER JOIN spfli AS p 
                    ON s~carrid = p~carrid 
                  INNER JOIN sflight AS f 
                    ON p~carrid = f~carrid AND p~connid = f~connid 
                FIELDS s~carrid, 
                       s~carrname, 
                       p~connid, 
                       p~cityfrom, 
                       p~cityto, 
                       f~fldate, 
                       f~price, 
                       f~currency ) 
          SELECT FROM HIERARCHY( 
                        SOURCE +flights 
                        LEVELS ( carrid, connid, fldate ) 
                        SIBLINGS ORDER BY connid, fldate ) 
                 FIELDS node_id AS node, 
                        carrname, 
                        cityfrom, cityto, 
                        CAST( price AS CHAR( 20 ) ) AS price, currency 
                 WHERE carrid = 'LH' 
                 INTO TABLE @FINAL(flight_hiera). 
 
    out->write( flight_hiera ). 
 
 
    WITH +flights AS ( 
         SELECT FROM scarr AS s 
                  INNER JOIN spfli AS p 
                    ON s~carrid = p~carrid 
                  INNER JOIN sflight AS f 
                    ON p~carrid = f~carrid AND p~connid = f~connid 
                FIELDS s~carrid, 
                       s~carrname, 
                       p~connid, 
                       p~cityfrom, 
                       p~cityto, 
                       f~fldate, 
                       f~price, 
                       f~currency 
                WHERE  p~carrid = 'LH' AND f~currency = 'EUR' ) 
          SELECT FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
                        SOURCE HIERARCHY( 
                          SOURCE +flights 
                          LEVELS ( carrid, connid, fldate ) 
                          SIBLINGS ORDER BY connid, fldate  ) 
                    MEASURES MIN( price ) AS min, 
                             MAX( price ) AS max, 
                             SUM( price ) AS sum 
                    WHERE hierarchy_level = 2 ) AS agg 
                    FIELDS agg~carrid,  agg~carrname, agg~connid, 
                           agg~min, agg~max, agg~sum 
                    INTO TABLE @FINAL(flight_hiera_agg). 
 
    out->write( flight_hiera_agg ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Data from DDIC database tables `SCARR`, `SPFLI` and `SFLIGHT` are joined in a CTE of the [`WITH`](abapwith.md) statement that is used as a data source of the hierarchy generator [`HIERARCHY`](abenselect_hierarchy_generator.md) using the addition [`LEVELS`](abenselect_hierarchy_gen_level.md). The columns `CARRID`, `CONNID` and `FLDATE` are specified as level columns. The resulting [level-based hierarchy](../../abap-glossary/abenlevel_based_hiera_glosry.md) is used as a data source for the [hierarchy aggregate navigator](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md) that sums up the flight prices for each flight connection.
