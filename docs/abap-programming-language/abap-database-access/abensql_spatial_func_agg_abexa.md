---
title: "sql_func - Aggregate Spatial Functions"
source_file: abensql_spatial_func_agg_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - Spatial Functions > sql_func - Examples of Spatial Aggregate Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Aggregate Spatial Functions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [aggregate spatial functions](abensql_spatial_func_a.md) in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_function_spatial_a DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_function_spatial_a IMPLEMENTATION. 
  METHOD main. 
    DATA ewkb TYPE x 
      VALUE `01010000200000000000000000000000000000000000000000` 
      LENGTH 25. 
    DATA wkb TYPE x VALUE `010100000000000000000000400000000000001040` 
      LENGTH 21. 
 
    DELETE FROM demo_geo_point.                         "#EC CI_NOWHERE 
    INSERT demo_geo_point FROM TABLE @( VALUE #( 
      ( point1 = `010100002000000000E561A1D634A748400D71AC8BDB482140` 
        point2 = `0101000020000000006919A9F754BC49408A20CEC3090C1F40` ) 
      ) ). 
 
    TRY. 
        SELECT SINGLE 
          st_alphashapeaggr( point1, fltp`1.0`, 'meter' ) 
            AS alphashapeaggr, 
          st_alphashapeareaaggr( point1, fltp`1.0` ) 
            AS alphashapeareaaggr, 
          st_assvgaggr( point1 ) AS st_assvgaggr, 
          st_collectaggr( point1 ) AS st_collectaggr, 
          st_concavehullaggr( point1 ) AS st_concavehullaggr, 
          st_convexhullaggr( point1 ) AS st_convexhullaggr, 
          st_envelopeaggr( point1 ) AS st_envelopeaggr, 
          st_intersectionaggr( point1 ) AS st_intersectionaggr, 
          st_unionaggr( point1 ) AS st_unionaggr 
          FROM demo_geo_point 
          INTO @DATA(aggregate_fcts). 
 
        WITH +cte AS ( 
          SELECT st_new_polygon( 'Polygon(( 0 0, 2 0, 1 2, 0 0 ))' ) 
            AS geo, 1 AS anint, 'ABC' AS achar, 'DEF' AS anotherchar 
          FROM demo_geo_point ) 
          SELECT SINGLE 
            st_asesrijson_multicolumn( geo, anint, achar, 
              geom_name = 'GEO', object_id_name = 'ANINT' ) 
                AS st_asesrijson_multicolumn, 
            st_asgeojson_multicolumn( geo, anint, achar, 
              geom_name = 'GEO', feature_id_name = 'ANINT' ) 
                AS st_asgeojson_multicolumn, 
            st_asmvt( geo, anint, achar, geom_name = 'GEO', 
              layer_name = 'ANINT' ) AS st_asmvt 
            FROM +cte 
            INTO @DATA(aggregate_fcts_exp_list). 
 
        out->write( aggregate_fcts ). 
        out->write( aggregate_fcts_exp_list ). 
      CATCH cx_root INTO DATA(error). 
        out->write( error->get_longtext( ) ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Uses the aggregate spatial functions supported by ABAP SQL as elements of a `SELECT` list.
