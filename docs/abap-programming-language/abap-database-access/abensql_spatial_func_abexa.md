---
title: "sql_func - Spatial Functions"
source_file: abensql_spatial_func_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - SQL Functions > sql_func - Spatial Functions > sql_func - Examples of Spatial Aggregate Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Spatial Functions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [spatial functions](abensql_spatial_func.md) in [SQL expressions](abapsql_expr.md).

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
CLASS cl_demo_sql_function_spatial DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_function_spatial IMPLEMENTATION. 
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
          point1 AS point1, 
          point2 AS point2, 
          st_3dlength( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) ) 
            AS st_3dlength, 
          st_addmeasure( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) , 
              fltp`0`, fltp`10` ) AS st_addmeasure, 
          st_alphashape( 
            st_new_multipoint( 'MultiPoint((0 0), (0 1), (1 1))' ), 
              fltp`4.0` ) AS st_alphashape, 
          st_alphashapearea( st_new_multipoint( 
            'MultiPoint((0 0), (0 1), (1 1), (0.2 0))' ), fltp`0.5` ) 
              AS st_alphashapearea, 
          st_alphashapeedge( st_new_multipoint( 
            'MultiPoint((0 0), (0 1), (1 1), (0.2 0))' ), fltp`0.9` ) 
              AS st_alphashapeedge, 
          st_area( st_new_multipolygon( 
            'MultiPolygon((( 0 0, 2 0, 1 2, 0 0 )),' && 
            '((10 2, 11 0, 12 2, 10 2)))' ) ) AS st_area, 
          st_asbinary( point1 ) AS st_asbinary, 
          st_asesrijson( point1 ) AS st_asesrijson, 
          st_asewkb( point1 ) AS st_asewkb, 
          st_asewkt( point1 ) AS st_asewkt, 
          st_asgeojson( point1 ) AS st_asgeojson, 
          st_asmvtgeom( 
            st_new_polygon( 'Polygon((1 2, 6 2, 6 4, 1 4, 1 2))' ), 
            bounds = st_geomfromtext( 'LineString(0 0, 4096 4096)' ) ) 
            AS st_asmvtgeom, 
          st_assvg( point1 ) AS st_assvg, 
          st_astext( point1 ) AS st_astext, 
          st_aswkb( point1 ) AS st_aswkb, 
          st_aswkt( point1 ) AS st_aswkt, 
          st_boundary( point1 ) AS st_boundary, 
          st_buffer( st_new_polygon( 
            'Polygon((1 2, 10 2, 10 10, 1 2),(9 3, 5 3, 9 9, 9 3))' ), 
            fltp`1.0` ) AS st_buffer, 
          st_centroid( st_new_polygon( 
            'Polygon((3 3, 8 3, 4 8, 3 3))' ) ) AS st_centroid, 
          st_closestpointofapproach( st_new_linestring( 
            'LineString M(0 10 1, 5 2 2, 10 10 3)' ), 
            st_new_linestring( 'LineString M(0 0 1, 5 0 2, 10 0 3)' ) ) 
            AS st_closestpointofapproach, 
          st_collect( point1, point2 ) AS st_collect, 
          st_concavehull( point1 ) AS st_concavehull, 
          st_contains( point1, point2 ) AS st_contains, 
          st_convexhull( point1 ) AS st_convexhull, 
          st_coorddim( point1 ) AS st_coorddim, 
          st_coveredby( point1, point2 ) AS st_coveredby, 
          st_covers( point1, point2 ) AS st_covers, 
          st_difference( point1, point2 ) AS st_difference, 
          st_dimension( point1 ) AS st_dimension, 
          st_disjoint( point1, point2 ) AS st_disjoint, 
          st_distance( point1, point2 ) AS st_distance, 
          st_endpoint( st_new_linestring( 
            'LineString(0 0, 5 5, 5 0, 0 0)' ) ) AS st_endpoint, 
          st_envelope( st_new_linestring( 
            'LineString(0 0, 5 5, 5 0, 0 0)' ) ) AS st_envelope, 
          st_equals( point1, point2 ) AS st_equals, 
          st_exteriorring( st_new_polygon( 
            'Polygon(( 0 0, 2 0, 1 2, 0 0 ))' ) ) AS st_exteriorring, 
          st_force2d( point1 ) AS st_force2d, 
          st_force3dm( point1 ) AS st_force3dm, 
          st_force3dz( point1 ) AS st_force3dz, 
          st_force4d( point1 ) AS st_force4d, 
          st_frechetdistance( st_new_linestring( 
            'LineString M(0 10 1, 5 2 2, 10 10 3)' ), 
            st_new_linestring( 
            'LineString M(0 0 1, 5 0 2, 10 0 3)' ) ) 
            AS st_frechetdistance, 
          st_geohash( point1 ) AS st_geohash, 
          st_geometrytype( point1 ) AS st_geometrytype, 
          st_geomfromesrijson( 
            '{ "points": [[0,0,1]],' && 
            ' "spatialReference": {"wkid": 0} }' 
            ) AS st_geomfromesrijson, 
          st_geomfromewkb( @ewkb ) AS st_geomfromewkb, 
          st_geomfromewkt( 'SRID=0;POINT (2.0 4.0)' ) 
            AS st_geomfromewkt, 
          st_geomfromgeohash( 's02equ0', 4326 ) AS st_geomfromgeohash, 
          st_geomfromtext( 'CircularString(0 0, 1 1, 0 2)' ) 
            AS st_geomfromtext, 
          st_geomfromwkb( @wkb ) AS st_geomfromwkb, 
          st_geomfromwkt( 'Point (2.0 4.0)' ) AS st_geomfromwkt, 
          st_interiorringn( 
            st_new_polygon( 'Polygon(( 0 0, 2 0, 1 2, 0 0 ))' ), 1 ) 
            AS st_interiorringn, 
          st_intersection( point1, point2 ) AS st_intersection, 
          st_intersects( point1, point2 ) AS st_intersects, 
          st_intersectsfilter( point1, point2 ) AS st_intersectsfilter, 
          st_intersectsrect( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            point1, point2 ) 
            AS st_intersectsrect, 
          st_intersectsrectplanar( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            point1, point2 ) 
            AS st_intersectsrectplanar, 
          st_invalidreason( point1 ) AS st_invalidreason, 
          st_is3d( point1 ) AS st_is3d, 
          st_isclosed( 
            st_new_linestring( 'Linestring( 0 0, 2 0, 1 2, 0 0 )' ) ) 
            AS st_isclosed, 
          st_isempty( point1 ) AS st_isempty, 
          st_ismeasured( point1 ) AS st_ismeasured, 
          st_isring( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) ) 
            AS st_isring, 
          st_issimple( point1 ) AS st_issimple, 
          st_isvalid( point1 ) AS st_isvalid, 
          st_isvalidtrajectory( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) ) 
            AS st_isvalidtrajectory, 
          st_length( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) ) 
            AS st_length, 
          st_lineinterpolatepoint( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            fltp`0.5` ) 
            AS st_lineinterpolatepoint, 
          st_linelocatepoint( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            point1 ) AS st_linelocatepoint, 
          st_linesubstring( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            fltp`0.1`, fltp`0.9` ) 
            AS st_linesubstring, 
          st_locatealong( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            fltp`1.0` ) AS st_locatealong, 
          st_locatebetween( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            fltp`1.0`, fltp`1.0` ) AS st_locatebetween, 
          st_m( point1 ) AS st_m, 
          st_makeline( point1, point2 ) AS st_makeline, 
          st_makepolygon( 
            st_new_linestring( 
            'LineString(0 0, 10 0, 10 10, 0 10, 0 0)' ) 
            ) AS st_makepolygon, 
          st_mmax( 
            st_new_linestring( 'LineString ZM( 1 2 3 4, 5 6 7 8 )' ) ) 
            AS st_mmax, 
          st_mmin( 
            st_new_linestring( 'LineString ZM( 1 2 3 4, 5 6 7 8 )' ) ) 
            AS st_mmin, 
          st_new_circularstring( ) AS st_new_circularstring1, 
          st_new_circularstring( 'CircularString(0 0, 1 1, 0 2)' ) 
            AS st_new_circularstring2, 
          st_new_geometrycollection( ) AS st_new_geometrycollection1, 
          st_new_geometrycollection( 
            'GeometryCollection (LineString(5 10, 10 12, 15 10),' && 
            ' Polygon ((10 -5, 15 5, 5 5, 10 -5)))' ) 
            AS st_new_geometrycollection2, 
          st_new_linestring( ) AS st_new_linestring1, 
          st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) 
            AS st_new_linestring2, 
          st_new_multilinestring( ) AS st_new_multilinestring1, 
          st_new_multilinestring( 
            'MultiLineString Z((10 10 10, 12 12 12),' 
            && ' (14 10 10, 16 12 12))' ) AS st_new_multilinestring2, 
          st_new_multipoint( ) AS st_new_multipoint1, 
          st_new_multipoint( 'MultiPoint ((10 10), (12 12), (14 10))' ) 
            AS st_new_multipoint2, 
          st_new_multipolygon( ) AS st_new_multipolygon1, 
          st_new_multipolygon( 'MultiPolygon((( 0 0, 2 0, 1 2, 0 0 )),' 
          && '((10 2, 11 0, 12 2, 10 2)))' ) AS st_new_multipolygon2, 
          st_new_point( 'Point (10 20)' ) AS st_new_point2, 
          st_new_point( fltp`1`, fltp`2` ) AS st_new_point3, 
          st_new_pointm( fltp`1`, fltp`1`, fltp`1` ) AS st_new_pointm, 
          st_new_pointz( fltp`1`, fltp`1`, fltp`1` ) AS st_new_pointz, 
          st_new_pointzm( fltp`1`, fltp`1`, fltp`1`, fltp`1` ) 
            AS st_new_pointzm, 
          st_new_polygon( ) AS st_new_polygon1, 
          st_new_polygon( 'Polygon(( 0 0, 2 0, 1 2, 0 0 ))' ) 
            AS st_new_polygon2, 
          st_numgeometries( 
            st_new_multipoint( 'MultiPoint ((10 10), (12 12), (14 10))' 
             ) ) AS st_numgeometries, 
          st_numinteriorring( 
            st_new_polygon( 'Polygon(( 0 0, 2 0, 1 2, 0 0 ))' ) ) 
            AS st_numinteriorring, 
          st_numinteriorrings( 
            st_new_polygon( 'Polygon(( 0 0, 2 0, 1 2, 0 0 ))' ) ) 
            AS st_numinteriorrings, 
          st_numpoints( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) ) 
            AS st_numpoints, 
          st_orderingequals( point1, point2 ) AS st_orderingequals, 
          st_overlaps( point1, point2 ) AS st_overlaps, 
          st_perimeter( 
            st_new_multipolygon( 
            'MultiPolygon((( 0 0, 2 0, 1 2, 0 0 )),' 
            && '((10 2, 11 0, 12 2, 10 2)))' ) ) AS st_perimeter, 
          st_pointfromgeohash( 's02equ0', 4326 ) 
            AS st_pointfromgeohash, 
          st_pointn( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 
            1 ) AS st_pointn, 
          st_pointonsurface( 
            st_new_polygon( 'Polygon(( 0 0, 2 0, 1 2, 0 0 ))' ) ) 
            AS st_pointonsurface, 
          st_removepoint( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ), 1 ) 
            AS st_removepoint, 
          st_reverse( point1 ) AS st_reverse, 
          st_rotate( point1, fltp`3.14159265359`, 
            fltp`0.0`, fltp`1.0` ) AS st_rotate, 
          st_scale( point1, fltp`2` ) AS st_scale, 
          st_simplify( point1, fltp`1.0` ) AS st_simplify, 
          st_snaptogrid( point1, fltp`1.0` ) AS st_snaptogrid, 
          st_srid( point1, 4326 ) AS st_srid, 
          st_startpoint( 
            st_new_linestring( 'LineString(0 0, 5 5, 5 0, 0 0)' ) ) 
            AS st_startpoint, 
          st_symdifference( point1, point2 ) AS st_symdifference, 
          st_touches( point1, point2 ) AS st_touches, 
          st_transform( 
            st_new_point( 'Point(-86 36)',4326 ), 1000004326 ) 
            AS st_transform, 
          st_translate( point1, fltp`2.5`, fltp`1.0` ) AS st_translate, 
          st_translate3d( 
            st_new_pointz( fltp`1`, fltp`1`, fltp`1` ), 
            fltp`2.5`, fltp`1.0`, fltp`2.0` ) AS st_translate3d, 
          st_union( point1, point2 ) AS st_union, 
          st_within( point1, point2 ) AS st_within, 
          st_withindistance( point1, point2, fltp`1` ) 
            AS st_withindistance, 
          st_x( point1 ) AS st_x, 
          st_xmax( point1 ) AS st_xmax, 
          st_xmin( point1 ) AS st_xmin, 
          st_y( point1 ) AS st_y, 
          st_ymax( point1 ) AS st_ymax, 
          st_ymin( point1 ) AS st_ymin, 
          st_z( point1 ) AS st_z, 
          st_zmax( point1 ) AS st_zmax, 
          st_zmin( point1 ) AS st_zmin 
         FROM demo_geo_point 
         INTO @FINAL(spatial_fcts). 
 
        out->write( spatial_fcts ). 
      CATCH cx_root INTO DATA(error). 
        out->write( error->get_longtext( ) ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Uses the spatial functions supported by ABAP SQL as elements of a `SELECT` list.
